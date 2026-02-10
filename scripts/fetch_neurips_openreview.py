import requests
from pathlib import Path
import argparse
import time

BASE_API = "https://api2.openreview.net/notes"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; CECDA-ResearchBot/1.0)"
}


def fetch_neurips_papers(limit=10):
    print("🔍 Fetching NeurIPS 2023 papers from OpenReview API2...")

    params = {
        "content.venueid": "NeurIPS.cc/2023/Conference",
        "limit": limit
    }

    # Retry logic
    for attempt in range(5):
        response = requests.get(BASE_API, params=params, headers=HEADERS)

        if response.status_code == 200:
            data = response.json()
            papers = data.get("notes", [])

            pdf_links = []
            for paper in papers:
                paper_id = paper["id"]
                pdf_url = f"https://openreview.net/pdf?id={paper_id}"
                pdf_links.append((paper_id, pdf_url))

            return pdf_links

        elif response.status_code == 429:
            wait_time = 5 * (attempt + 1)
            print(f"⚠ Rate limited (429). Waiting {wait_time}s...")
            time.sleep(wait_time)

        else:
            print("❌ Failed API request")
            print("Status Code:", response.status_code)
            print("Response:", response.text[:200])
            return []

    print("❌ Too many retries. Try again later.")
    return []


def download_pdfs(papers):
    out_dir = Path("data/papers/neurips_openreview")
    out_dir.mkdir(parents=True, exist_ok=True)

    for pid, url in papers:
        pdf_path = out_dir / f"{pid}.pdf"

        if pdf_path.exists():
            print("✅ Already exists:", pdf_path.name)
            continue

        print("⬇ Downloading:", pdf_path.name)

        r = requests.get(url, headers=HEADERS)
        if r.status_code == 200:
            pdf_path.write_bytes(r.content)
            print("✅ Saved:", pdf_path)
        else:
            print("❌ Failed download:", url)

        # polite delay
        time.sleep(2)

    print("\n🎉 Download Complete!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=10)
    args = parser.parse_args()

    papers = fetch_neurips_papers(limit=args.n)
    print(f"✅ Found {len(papers)} papers")

    download_pdfs(papers)


if __name__ == "__main__":
    main()
