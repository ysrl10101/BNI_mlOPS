import sys
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import pandas as pd


# Hyperparameter dari command line
n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 100
max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 5


# Load data
df = pd.read_csv("data/train.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df.drop("target", axis=1),
    df["target"],
    test_size=0.2,
    random_state=42
)


# MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("training-siang")


# Run name
run_name = f"RandomForest_n{n_estimators}_depth{max_depth}"


with mlflow.start_run(run_name=run_name) as run:

    print(f"Run Name : {run_name}")
    print(f"Run ID   : {run.info.run_id}")

    params = {
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "random_state": 42
    }

    mlflow.log_params(params)

    print("Training model...")

    model = RandomForestClassifier(**params).fit(
        X_train,
        y_train
    )

    print("Training selesai.")

    auc = roc_auc_score(
        y_test,
        model.predict_proba(X_test)[:, 1]
    )

    with open("auc.txt", "w") as f:
        f.write(str(auc))

    mlflow.log_metric("auc", auc)

    print(f"AUC: {auc:.4f}")

    # Simpan model ke MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        name="model"
    )
    print("Model berhasil dicatat ke MLflow.")


print("MLflow run FINISHED.")