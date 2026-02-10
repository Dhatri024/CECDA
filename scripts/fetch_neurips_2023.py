import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv
import argparse

BASE_URL = "https://papers.nips.cc"


# -----------------------------
# Fetch NeurIPS 2023 Paper Links
# -----------------------------
def fetch_paper_pdf_links(limit=50):
    year_url = f"{BASE_URL}/paper_files/paper/2023"
    print("🔍 Fetching NeurIPS 2023 paper list...")

    html = requests.get(year_url).text
    soup = BeautifulSoup(html, "html.parser")

    pdf_links = []

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and "Paper-Conference.pdf" in href:
            full_link = f"{BASE_URL}{href}"
            pdf_links.append(full_link)

        if len(pdf_links) >= limit:
            break

    return pdf_links


# -----------------------------
# Download PDFs
# -----------------------------
def download_pdfs(pdf_links):
    out_dir = Path("data/papers/neurips")
    out_dir.mkdir(parents=True, exist_ok=True)

    metadata_path = Path("data/metadata/neurips_metadata.csv")
    metadata_path.parent.mkdir(parents=True, exist_ok=True)

    with open(metadata_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["paper_id", "venue", "year", "pdf_path", "source", "accepted"])

        for url in pdf_links:
            filename = url.split("/")[-1]
            paper_id = filename.split("-")[0]

            pdf_file = out_dir / filename

            if pdf_file.exists():
                print("✅ Already exists:", filename)
            else:
                print("⬇ Downloading:", filename)
                r = requests.get(url)

                if r.status_code == 200:
                    pdf_file.write_bytes(r.content)
                    print("✅ Saved:", pdf_file)
                else:
                    print("❌ Failed:", url)
                    continue

            writer.writerow([
                paper_id,
                "NeurIPS",
                2023,
                str(pdf_file),
                "papers.nips.cc",
                True
            ])

    print("\n🎉 Download Complete!")
    print("Metadata saved at:", metadata_path)


# -----------------------------
# Main
# -----------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=50, help="Number of papers to fetch")
    args = parser.parse_args()

    pdf_links = fetch_paper_pdf_links(limit=args.n)
    print(f"✅ Found {len(pdf_links)} PDF links")

    download_pdfs(pdf_links)


if __name__ == "__main__":
    main()
