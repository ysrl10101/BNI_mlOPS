from fastapi import FastAPI, HTTPException
import mlflow.pyfunc
import pandas as pd

app = FastAPI()

print("Loading MLflow model...")
model = mlflow.pyfunc.load_model("model")
print("Model loaded successfully.")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: dict):

    # Buat DataFrame dari request
    df = pd.DataFrame([payload])

    # target bukan feature
    if "target" in df.columns:
        raise HTTPException(
            status_code=400,
            detail="'target' tidak boleh dikirim karena merupakan label."
        )

    try:
        pred = model.predict(df)

        return {
            "prediction": pred.tolist()
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )