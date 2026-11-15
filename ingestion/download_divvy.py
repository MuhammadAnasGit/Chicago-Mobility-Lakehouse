import io, sys, zipfile
from pathlib import Path
import requests

month = sys.argv[1]  # e.g. 202610
url = f"https://divvy-tripdata.s3.amazonaws.com/{month}-divvy-tripdata.zip"
out_dir = Path(r"C:\lakehouse-data\bronze\divvy") / f"year={month[:4]}" / f"month={month[4:]}"
out_dir.mkdir(parents=True, exist_ok=True)

print(f"Downloading {url} ...")
resp = requests.get(url, timeout=300)
resp.raise_for_status()

with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
    csv_name = next(n for n in z.namelist() if n.endswith(".csv") and "MACOSX" not in n)
    (out_dir / "trips.csv").write_bytes(z.read(csv_name))

print(f"Saved to {out_dir / 'trips.csv'}")