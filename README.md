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

## Running the Pipeline

### Convert PDFs to Text

```bash
python scripts/pdf_to_text.py
