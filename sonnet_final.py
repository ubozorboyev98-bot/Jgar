import runpy
import sys
from pathlib import Path


app_dir = Path(__file__).resolve().parent / "sonnet_final"
sys.path.insert(0, str(app_dir))
runpy.run_path(str(app_dir / "sonnet_final.py"), run_name="__main__")