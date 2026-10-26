from functools import lru_cache
from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parents[1] / "data" / "sentiment_model.joblib"
URGENT_WORDS = ("refund", "charged", "payment failed", "security", "unsafe", "fraud", "broken", "crashes", "defective")

@lru_cache(maxsize=1)
def model():
    return joblib.load(MODEL_PATH)

def analyze(text: str) -> dict:
    text = text.strip()
    if not text:
        raise ValueError("Review must not be empty")
    predictor = model()
    label = str(predictor.predict([text])[0])
    confidence = float(max(predictor.predict_proba([text])[0]))
    signals = [word for word in URGENT_WORDS if word in text.lower()]
    urgent = label == "negative" and bool(signals)
    return {"review": text, "sentiment": label, "confidence": round(confidence, 4),
            "urgent": urgent, "signals": signals,
            "needs_review": confidence < 0.65 or urgent}
