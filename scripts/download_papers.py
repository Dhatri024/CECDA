import os
import csv
import requests
from pathlib import Path

# -----------------------------
# CONFIG
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "papers"
META_FILE = BASE_DIR / "data" / "metadata" / "papers_metadata.csv"

CONFERENCES = {
    "neurips": "scripts/neurips_urls.txt",
    "icml": "scripts/icml_urls.txt",
    "iclr": "scripts/iclr_urls.txt"
}


# -----------------------------
# DOWNLOAD FUNCTION
# -----------------------------
def download_pdf(url, save_folder):
    # Special handling for OpenReview
    if "openreview.net/pdf?id=" in url:
        paper_id = url.split("id=")[-1]
        filename = f"{paper_id}.pdf"
    else:
        filename = url.split("/")[-1]

    save_path = save_folder / filename

    if save_path.exists():
        print(f"✅ Already exists: {filename}")
        return filename

    print(f"⬇ Downloading: {filename}")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        print(f"✅ Saved: {save_path}")
        return filename

    else:
        print(f"❌ Failed download ({response.status_code}): {url}")
        return None



# -----------------------------
# MAIN SCRIPT
# -----------------------------
def main():
    # Create metadata file with header if not exists
    if not META_FILE.exists():
        with open(META_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "paper_id", "venue", "year", "pdf_path",
                "source", "openreview_id", "accepted"
            ])

    # Append rows
    with open(META_FILE, "a", newline="") as meta_f:
        writer = csv.writer(meta_f)

        for venue, url_file in CONFERENCES.items():
            url_path = BASE_DIR / url_file

            if not url_path.exists():
                print(f"⚠ Missing file: {url_file}")
                continue

            save_folder = DATA_DIR / venue
            save_folder.mkdir(parents=True, exist_ok=True)

            with open(url_path, "r") as f:
                urls = [line.strip() for line in f if line.strip()]

            print(f"\n📌 Venue: {venue.upper()} | Papers: {len(urls)}")

            for url in urls:
                filename = download_pdf(url, save_folder)
                if filename:
                    paper_id = filename.split("-")[0]
                    pdf_rel_path = f"data/papers/{venue}/{filename}"

                    writer.writerow([
                        paper_id,
                        venue.upper(),
                        2023,
                        pdf_rel_path,
                        "manual_url_list",
                        "",
                        True
                    ])

    print("\n🎉 Sprint 3 Download Complete!")
    print(f"Metadata saved at: {META_FILE}")


if __name__ == "__main__":
    main()
