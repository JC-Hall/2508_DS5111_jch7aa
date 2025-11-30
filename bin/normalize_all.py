import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from bin.gainers.wsj import GainerWSJ
from bin.gainers.yahoo import GainerYahoo


DATA_DIR = ROOT / "data"
SEEDS_DIR = ROOT / "my_dbt_project" / "myfirstproject" / "seeds"

SEEDS_DIR.mkdir(parents=True, exist_ok=True)

wsj = GainerWSJ()
yahoo = GainerYahoo()

print("Starting normalization...\n")
print(f"DATA_DIR = {DATA_DIR}")
print("CSV files:")
for f in DATA_DIR.glob("*.csv"):
    print(" -", f.name)
print()


# Normalize WSJ files
for csv in DATA_DIR.glob("wsjgainers_*.csv"):
    out = SEEDS_DIR / csv.name
    print(f"WSJ → {csv.name}")
    wsj.normalize_data(filepath=str(csv), outpath=str(out))

# Normalize Yahoo files
for csv in DATA_DIR.glob("ygainers_*.csv"):
    out = SEEDS_DIR / csv.name
    print(f"Yahoo → {csv.name}")
    yahoo.normalize_data(filepath=str(csv), outpath=str(out))

print("All files normalized into seeds/")
