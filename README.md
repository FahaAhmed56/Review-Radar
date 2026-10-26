# ReviewRadar AI — Customer Review Intelligence

A portfolio-friendly, offline NLP demo that labels reviews **positive**, **negative**, or **neutral**, and flags urgent negative feedback with explainable keyword signals.

## Features
- Trained TF-IDF + Logistic Regression model (`data/sentiment_model.joblib` included).
- Streamlit dashboard for single reviews and CSV batch analytics.
- FastAPI endpoint for programmatic integration, with built-in API docs.
- 300 synthetic labeled sample reviews, Python tests, and GitHub Actions CI.
- No external API keys, accounts, or MongoDB required.

## Requirements
- Python 3.10+ (tested in Python 3.11 environment)

## Windows / VS Code setup
```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app/dashboard.py
```
Visit http://localhost:8501.

## API (second terminal)
```powershell
.venv\Scripts\python.exe -m uvicorn api.main:app --reload
```
Open http://127.0.0.1:8000/docs or send:
```bash
curl -X POST http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d '{"review":"Broken item and terrible service"}'
```

## Tests
```powershell
.venv\Scripts\python.exe -m pytest -q
```

## CSV format
Upload CSV file with a `review` column. Example: `data/reviews.csv`. Dashboard processes up to 2,000 rows per upload.

## Architecture
`review text → TF-IDF features → Logistic Regression → sentiment + confidence → keyword-based urgency signal → web dashboard/API`

## Important limitations
- All sample labels are synthetic; training and test examples share templated phrasing. **Do not infer real-world accuracy from tests**.
- Confidence values are model outputs, not validated probabilities.
- Urgency requires a negative prediction plus an explicit trigger phrase; it will miss subtler issues.
- This is not a production safety, moderation, or customer service decision system. Human review recommended.

## GitHub
Suggested name: `ReviewRadar-AI`
Suggested description: `NLP-powered customer review analyzer with sentiment prediction, urgent complaint flags, Streamlit dashboard, and FastAPI.`
