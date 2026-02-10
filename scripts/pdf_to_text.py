import fitz  # PyMuPDF
from pathlib import Path
import os
import argparse


# ----------------------------
# Convert ONE PDF → Text
# ----------------------------
def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    return full_text


# ----------------------------
# Convert and Save Text File
# ----------------------------
def convert_and_save(pdf_file, output_dir):
    paper_id = Path(pdf_file).stem

    text = pdf_to_text(pdf_file)

    out_path = Path(output_dir) / f"{paper_id}.txt"
    out_path.write_text(text, encoding="utf-8")

    print("✅ Converted:", Path(pdf_file).name)


# ----------------------------
# MAIN Runner
# ----------------------------
def main():
    parser = argparse.ArgumentParser()

    # Optional single paper mode
    parser.add_argument(
        "--single",
        type=str,
        help="Convert ONE PDF file instead of full dataset"
    )

    args = parser.parse_args()

    output_dir = "data/paper_texts"
    os.makedirs(output_dir, exist_ok=True)

    # ----------------------------
    # MODE 1: Single PDF Input
    # ----------------------------
    if args.single:
        pdf_path = args.single

        if not os.path.exists(pdf_path):
            print("❌ PDF not found:", pdf_path)
            return

        convert_and_save(pdf_path, output_dir)

        print("\n🎉 Single PDF converted successfully!")
        return

    # ----------------------------
    # MODE 2: Convert Dataset Folder
    # ----------------------------
    input_dir = "data/papers/neurips"

    print("\n📌 Converting all PDFs from:", input_dir)

    for pdf_file in Path(input_dir).glob("*.pdf"):
        convert_and_save(pdf_file, output_dir)

    print("\n🎉 All dataset PDFs converted to text!")


# ----------------------------
# ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    main()
