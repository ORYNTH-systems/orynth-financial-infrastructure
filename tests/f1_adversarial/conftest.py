from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "04-settlement-integrity" / "runtime"

if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))
