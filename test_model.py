import mlflow.pyfunc

print("Loading model...")

model = mlflow.pyfunc.load_model("model")

print("Model berhasil di-load.")
print(model)