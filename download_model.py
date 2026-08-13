import mlflow
from pathlib import Path


TRACKING_URI = "http://127.0.0.1:5000"

# GANTI dengan Run ID model yang ingin digunakan
RUN_ID = "24e14a490bc34b9d8e6fb2b1e4ec7fad"

OUTPUT_DIR = Path("model")


mlflow.set_tracking_uri(TRACKING_URI)

print("Downloading model artifact...")
print(f"Run ID : {RUN_ID}")
print(f"Output : {OUTPUT_DIR.resolve()}")

path = mlflow.artifacts.download_artifacts(
    run_id=RUN_ID,
    artifact_path="model",
    dst_path=str(OUTPUT_DIR)
)

print()
print("Model berhasil di-download.")
print(f"Lokasi: {path}")