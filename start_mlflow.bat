@echo off
title MLflow Tracking Server

echo ========================================
echo       MLOps Training - MLflow
echo ========================================
echo.

echo [1/2] Preparing MLflow database...
mlflow db upgrade sqlite:///D:/pusilkom/mlops-training/mlflow.db

if errorlevel 1 (
    echo.
    echo ERROR: MLflow database migration failed.
    echo.
    pause
    exit /b 1
)

echo.
echo [2/2] Starting MLflow Tracking Server...
echo.
echo MLflow UI:
echo http://127.0.0.1:5000
echo.
echo Press CTRL+C to stop MLflow Server.
echo.

mlflow server ^
    --backend-store-uri "sqlite:///D:/pusilkom/mlops-training/mlflow.db" ^
    --host 127.0.0.1 ^
    --port 5000