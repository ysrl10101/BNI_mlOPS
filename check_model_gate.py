import sys

MINIMUM_AUC = 0.51

def check_gate(auc: float):
    if auc < MINIMUM_AUC:
        print(f"GAGAL: Model tidak lolos gate (AUC={auc:.4f} < {MINIMUM_AUC})")
        sys.exit(1)
    print(f"LOLOS: Model lolos gate (AUC={auc:.4f} >= {MINIMUM_AUC})")

if __name__ == "__main__":
    check_gate(float(sys.argv[1]))
