import os
import fitz  # PyMuPDF
import pandas as pd

from src.claim_extraction.extract_claims_rulebased import extract_claim_sentences
from src.csv_scoring.score_claims_multidim import score_claim
from src.ebv_extraction.extract_evidence_salience import extract_ebv_salience


# ----------------------------
# Convert PDF → Text
# ----------------------------
def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text


# ----------------------------
# Main Pipeline for Single Paper
# ----------------------------
def main(pdf_path):

    paper_name = os.path.basename(pdf_path).replace(".pdf", "")
    print("\n📌 Running CECDA on User Paper:", paper_name)

    # ----------------------------
    # Step 1: Convert PDF → Text
    # ----------------------------
    text = pdf_to_text(pdf_path)
    print("✅ Converted:", paper_name + ".pdf")

    # ----------------------------
    # Step 2: Extract Claims
    # ----------------------------
    claims = extract_claim_sentences(text)

    if len(claims) == 0:
        print("❌ No claims detected.")
        return

    print("✅ Claims Extracted:", len(claims))

    # ----------------------------
    # Step 3: EBV Evidence Score
    # ----------------------------
    ebv_result = extract_ebv_salience(text)

    # If function returns only float
    if isinstance(ebv_result, float):
        ebv_score_value = ebv_result
        main_ev = 0
        appendix_ev = 0

    # If function returns tuple (score, main, appendix)
    else:
        ebv_score_value, main_ev, appendix_ev = ebv_result
        
    print("\n✅ EBV Score:", round(ebv_score_value, 3))
    print("   Main Evidence:", main_ev)
    print("   Appendix Evidence:", appendix_ev)


    # ----------------------------
    # Step 4: Score Claims + CDS
    # ----------------------------
    rows = []

    print("\n📌 Claim-Level Results:\n")

    for c in claims[:10]:  # limit top 10 claims

        result = score_claim(c)

        # score_claim returns tuple → first value is csv_score
        csv_score = result[0]

        # CDS = CSV - EBV
        cds_score = csv_score - ebv_score_value

        rows.append({
            "claim_sentence": c,
            "csv_score": round(csv_score, 3),
            "ebv_score": round(ebv_score_value, 3),
            "cds_score": round(cds_score, 3)
        })

        print("Claim:", c[:90], "...")
        print("CSV:", round(csv_score, 3),
              "| EBV:", round(ebv_score_value, 3),
              "| CDS:", round(cds_score, 3))
        print("-" * 70)

    # ----------------------------
    # Step 5: Save Output CSV
    # ----------------------------
    os.makedirs("outputs/user_demo", exist_ok=True)

    out_file = f"outputs/user_demo/{paper_name}_cecda_results.csv"
    pd.DataFrame(rows).to_csv(out_file, index=False)

    print("\n🎉 DONE! Results saved to:")
    print(out_file)


# ----------------------------
# Run from Terminal
# ----------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="Path to user PDF file")

    args = parser.parse_args()

    main(args.pdf)
