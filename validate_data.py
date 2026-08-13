import great_expectations as gx
import pandas as pd
import sys
from pathlib import Path


# ============================================================
# 1. Load dataset
# ============================================================

data_path = Path("data/train.csv")

if not data_path.exists():
    print(f"GAGAL: File tidak ditemukan: {data_path}")
    sys.exit(1)

df = pd.read_csv(data_path)

print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")


# ============================================================
# 2. Check required columns
# ============================================================

required_columns = [
    "income",
    "age",
    "target"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    print(
        f"GAGAL: Kolom berikut tidak ditemukan: "
        f"{missing_columns}"
    )
    sys.exit(1)


# ============================================================
# 3. Great Expectations
# ============================================================

context = gx.get_context()

validator = context.sources.pandas_default.read_csv(
    str(data_path)
)


# ============================================================
# 4. Data Quality Rules
# ============================================================

validator.expect_column_values_to_not_be_null(
    "income"
)

validator.expect_column_values_to_not_be_null(
    "age"
)

validator.expect_column_values_to_not_be_null(
    "target"
)

validator.expect_column_values_to_be_between(
    "age",
    min_value=18,
    max_value=100
)

validator.expect_column_values_to_be_in_set(
    "target",
    [0, 1]
)


# ============================================================
# 5. Validate
# ============================================================

results = validator.validate()


# ============================================================
# 6. Quality Gate
# ============================================================

if not results.success:

    print()
    print("=" * 60)
    print("GAGAL: Data quality check tidak lolos")
    print("Pipeline dihentikan.")
    print("=" * 60)

    sys.exit(1)


print()
print("=" * 60)
print("LOLOS: Data quality check berhasil")
print("Dataset siap digunakan untuk training.")
print("=" * 60)