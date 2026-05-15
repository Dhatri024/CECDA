# CECDA — Claim–Evidence Calibration & Divergence Analysis

CECDA is a research prototype that detects overclaiming risk in scientific machine learning papers by comparing how strong a paper’s claims are versus how much evidence the paper actually provides.

The main idea is simple:

- Papers often make very strong claims
- But sometimes the supporting evidence is weak or limited
- CECDA automatically measures this mismatch using a divergence score

This system extracts explicit claims from research papers, scores their strength, extracts evidence signals from the paper, and computes a final Claim–Evidence Divergence Score (CDS) to highlight potential overclaiming.

---

## What This Project Does

CECDA provides an end-to-end pipeline for analyzing research papers:

- Converts PDF papers into text
- Extracts scientific claim sentences automatically
- Scores claim strength using linguistic dimensions
- Extracts evidence indicators such as experiments, results, baselines, and ablations
- Computes divergence between claim strength and evidence breadth
- Assigns severity bands (Aligned vs Overclaim Risk)
- Runs calibration, ablation testing, and proxy validation
- Supports testing on any user-provided PDF paper (IEEE, NeurIPS, ICML, ICLR, arXiv)

---

## Core Components

### Claim Strength Vector (CSV)

Each extracted claim is scored based on multiple dimensions:

- Modality (strong vs hedged language)
- Comparative force (outperforms, improves, achieves)
- Generality (broad claim vs narrow claim)
- Scope (extent of applicability)

This produces a normalized claim strength score between 0 and 1.

---

### Evidence Breadth Vector (EBV)

Evidence is extracted from the paper based on the presence of:

- Experiments
- Results
- Baselines
- Ablations
- Appendix evidence

A salience-aware weighting is applied:

- Main-text evidence is weighted higher than appendix-only evidence

This produces an evidence breadth score between 0 and 1.

---

### Claim Divergence Score (CDS)

The final divergence score is computed as:

CDS = CSV − EBV

Interpretation:

- High CDS → Strong claim but weak evidence → Overclaim risk
- Low CDS → Strong evidence supporting the claim → Well-supported paper

---

## Outputs Produced

CECDA generates the following outputs:

- Extracted claims from papers
- CSV-scored claim strength results
- EBV evidence breadth scores (salience-aware)
- Final claim-level CDS divergence scores
- Calibrated severity band assignments
- Paper-level divergence summaries
- Ablation study reports
- Validation correlation reports

All outputs are stored inside the `outputs/` directory.

---
# Tech Stack Used

| Component | Technology / Library | Purpose |
|---|---|---|
| Programming Language | Python | Core pipeline implementation |
| PDF Processing | PyMuPDF (`fitz`) | PDF-to-text extraction |
| Data Handling | Pandas | CSV generation and result processing |
| Numerical Computation | NumPy | Score computation and normalization |
| Visualization | Matplotlib | Graphs and divergence visualizations |
| File Management | OS, Glob | Batch paper processing |
| Claim Extraction | Rule-Based NLP | Scientific claim sentence detection |
| Scoring Framework | Custom CSV/EBV/CDS Modules | Divergence computation |
| Development Environment | VS Code | Project development and testing |
| Platform | macOS / Windows / Linux | Cross-platform execution |
| Research Paper Sources | NeurIPS, ICML, ICLR, IEEE | Evaluation corpus |

---

# Project Workflow

The CECDA pipeline follows the architecture below:

1. PDF Research Paper Input  
2. PDF-to-Text Conversion  
3. Scientific Claim Extraction  
4. Claim Strength Vector (CSV) Scoring  
5. Evidence Breadth Vector (EBV) Extraction  
6. Coverage Divergence Score (CDS) Computation  
7. Calibration and Severity Band Assignment  
8. Final Claim-Level and Paper-Level Report Generation  

---

# Folder Structure

```bash
CECDA/
│
├── data/
│   └── paper_texts/
│
├── outputs/
│   ├── claims/
│   ├── csv_scores/
│   ├── ebv_scores/
│   ├── final_scores/
│   └── user_demo/
│
├── scripts/
│   ├── pdf_to_text.py
│   └── run_single_paper.py
│
├── src/
│   ├── claim_extraction/
│   ├── csv_scoring/
│   ├── ebv_extraction/
│   └── cds_scoring/
│
├── user_inputs/
│
└── README.md
```

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone <your-github-repo-link>
cd CECDA
```

---

## 2. Create a Virtual Environment

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install pymupdf pandas numpy matplotlib
```

---

# Running the Full Pipeline

## Option 1 — Run on a Single Research Paper

Place your PDF inside:

```bash
user_inputs/
```

Example:

```bash
user_inputs/my_paper.pdf
```

Run:

```bash
python scripts/run_single_paper.py --pdf user_inputs/my_paper.pdf
```

---

## Option 2 — Convert PDF to Text Only

```bash
python scripts/pdf_to_text.py --single user_inputs/my_paper.pdf
```

---

# Example Output

After execution, the system produces:

```text
✅ Claims Extracted
✅ CSV Scores Generated
✅ EBV Scores Generated
✅ CDS Divergence Scores Computed
✅ Severity Bands Assigned
✅ Final CSV Reports Saved
```

Generated outputs are stored inside:

```bash
outputs/
```

---

# Example CDS Interpretation

| CDS Range | Interpretation |
|---|---|
| CDS < -0.2 | Strongly Supported |
| -0.2 ≤ CDS < 0.1 | Aligned |
| 0.1 ≤ CDS < 0.3 | Moderate Divergence |
| CDS ≥ 0.3 | High Overclaim Risk |

---

# Supported Research Paper Formats

CECDA supports scientific papers from:

- NeurIPS
- ICML
- ICLR
- IEEE
- arXiv
- General PDF research papers

---

# Research Contributions

CECDA introduces:

- Claim–Evidence Divergence Analysis for scientific auditing
- Multi-dimensional Claim Strength Vector (CSV)
- Salience-aware Evidence Breadth Vector (EBV)
- Coverage Divergence Score (CDS)
- Cross-venue scientific paper generalization
- Lightweight reproducibility-oriented auditing framework

---

# Future Improvements

Potential future extensions include:

- Transformer-based claim extraction
- Multi-annotator evaluation benchmarks
- Reviewer-assistance dashboard
- Large-scale scientific auditing
- Integration with LLM-based reasoning systems
- Real-time conference paper auditing tools
