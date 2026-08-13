import sys
import pandas as pd

from evidently import Report
from evidently.presets import DataDriftPreset


REFERENCE_DATA = "data/train.csv"
CURRENT_DATA = "data/production_simulasi.csv"
REPORT_FILE = "drift_report.html"


def check_drift():

    # =========================
    # 1. Load data
    # =========================
    try:
        reference_data = pd.read_csv(REFERENCE_DATA)
        current_data = pd.read_csv(CURRENT_DATA)

    except FileNotFoundError as e:
        print(f"GAGAL: File tidak ditemukan: {e}")
        sys.exit(1)

    print(f"Reference data : {REFERENCE_DATA}")
    print(f"Current data   : {CURRENT_DATA}")

    # =========================
    # 2. Create Evidently report
    # =========================
    report = Report([
        DataDriftPreset()
    ])

    # =========================
    # 3. Run drift detection
    # =========================
    snapshot = report.run(
        reference_data=reference_data,
        current_data=current_data
    )

    # =========================
    # 4. Save HTML report
    # =========================
    snapshot.save_html(REPORT_FILE)

    print(f"Laporan drift tersimpan di: {REPORT_FILE}")
    print("LOLOS: Data drift detection berhasil dijalankan.")


if __name__ == "__main__":
    check_drift()