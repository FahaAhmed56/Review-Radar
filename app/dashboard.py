import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
import streamlit as st
from src.engine import analyze

st.set_page_config(page_title="ReviewRadar AI", page_icon="📊", layout="wide")
st.title("📊 ReviewRadar AI")
st.caption("AI customer-review sentiment and complaint triage · Educational demo trained on synthetic text")
tab1, tab2 = st.tabs(["Analyze one review", "Analyze CSV batch"])
with tab1:
    review = st.text_area("Customer review", "My item arrived broken and I need a refund.", height=120)
    if st.button("Analyze review", type="primary"):
        try:
            result = analyze(review)
            a,b,c = st.columns(3)
            a.metric("Sentiment", result["sentiment"].title())
            b.metric("Confidence", f'{result["confidence"]:.1%}')
            c.metric("Urgent complaint", "Yes" if result["urgent"] else "No")
            st.json(result)
        except ValueError as exc:
            st.error(str(exc))
with tab2:
    st.markdown("Upload a CSV containing a `review` column. Try `data/reviews.csv`.")
    uploaded = st.file_uploader("Reviews CSV", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        if "review" not in df.columns:
            st.error("CSV needs a review column")
        else:
            df = df.dropna(subset=["review"]).head(2000).copy()
            outcomes = [analyze(str(x)) for x in df["review"] if str(x).strip()]
            if outcomes:
                result_df = pd.DataFrame(outcomes)
                st.metric("Reviews analyzed", len(result_df))
                st.bar_chart(result_df["sentiment"].value_counts())
                st.dataframe(result_df, use_container_width=True)
                st.download_button("Download results",result_df.to_csv(index=False),"reviewradar_results.csv","text/csv")
            else:
                st.info("No non-empty reviews found")
