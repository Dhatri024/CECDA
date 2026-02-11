# 📌 CECDA Documentation

## Project Title  
**CECDA – Claim–Evidence Calibration & Divergence Analysis**

---

## 1. Project Overview

CECDA is a research-oriented system designed to detect overclaiming in scientific research papers.  
Many papers present strong claims in their abstract and conclusion, but the supporting experimental evidence may not always match the claim strength.  
CECDA addresses this gap by automatically extracting claims, measuring their strength, extracting evidence breadth, and computing a divergence score that highlights potential overclaim risk.

The system works across multiple research domains and venues such as NeurIPS, ICML, ICLR, and also general papers such as IEEE publications.

---

## 2. Core Idea

CECDA is built around one central question:

**Do the claims made in a paper match the breadth of evidence provided?**

To answer this, we define three key vectors:

- **CSV (Claim Strength Vector)**  
- **EBV (Evidence Breadth Vector)**  
- **CDS (Coverage Divergence Score)**  

These allow scientific claim calibration rather than subjective judgment.

---

## 3. Sprint 1 – Problem Lock & Scope Freeze

In Sprint 1, we finalized the definition and scope of the project.

### Key outcomes:
- Locked the official definition of CECDA  
- Clearly specified what the system measures and what it does not  
- Defined the three core metrics:

**CSV** → measures strength of claims  
**EBV** → measures evidence coverage  
**CDS** → divergence between claim strength and evidence breadth  

Deliverables:
- Formal project definition  
- Scope boundary document  
- Metric formulation ready for research writing  

---

## 4. Sprint 2 – Paper Mode Classification Design

In Sprint 2, we ensured scientific fairness across disciplines.

### Paper Modes:
- Empirical Papers  
- Theoretical Papers  
- Hybrid Papers  

We designed EBV dimensions differently depending on paper type.

Example:
- Empirical → datasets, experiments, ablations  
- Theoretical → proofs, lemmas, definitions  

Deliverables:
- Paper taxonomy  
- Mode-aware EBV specification  
- Mode detection logic (rule-based)

---

## 5. Sprint 3 – Dataset Collection

In Sprint 3, we created the evaluation corpus.

### Dataset Sources:
- NeurIPS papers  
- ICML papers  
- ICLR papers  
- OpenReview-based downloads  

Stored components:
- PDF files  
- Metadata CSV  
- Venue and year information  

Deliverables:
- Paper corpus stored in `data/papers/`  
- Metadata stored in `data/metadata/`  
- Clean dataset foundation ready

---

## 6. Sprint 4 – Annotation Guidelines & Pilot Labels

Sprint 4 focused on controlling annotation noise.

### Annotation Tasks:
- Claim identification  
- Claim strength labeling  
- Evidence breadth labeling  

We manually annotated pilot papers and created gold labels.

Agreement measurement:
- Self-consistency and agreement reports generated

Deliverables:
- Annotation guideline document  
- Pilot labeled dataset  
- Agreement evaluation script outputs

---

## 7. Sprint 5 – Claim Extraction Pipeline

Sprint 5 implemented automated claim extraction.

### Approach:
- Rule-based extraction from Abstract + Conclusion  
- Claim patterns such as:
  - "we propose"
  - "we demonstrate"
  - "our method outperforms"

Outputs:
- Extracted claims saved to:
  `outputs/claims/extracted_claims.csv`

Evaluation:
- Precision/Recall computed using fuzzy matching against pilot gold claims

Deliverables:
- Claim extraction module  
- Claim evaluation scripts  
- Improved universal extraction support

---

## 8. Sprint 6 – Claim Strength Scoring (CSV)

Sprint 6 quantified claim strength.

### CSV Dimensions:
- Modality (certainty level)  
- Comparative force (outperforms, improves)  
- Generality (broad vs narrow claim)  
- Scope (task-level vs universal)

We implemented multi-dimensional scoring:

Output file:
- `outputs/csv_scored_claims_multidim.csv`

Deliverables:
- CSV scoring module  
- Dimension-level claim scoring support

---

## 9. Sprint 7 – Evidence Extraction (EBV)

Sprint 7 extracted evidence signals from papers.

### Evidence indicators:
- datasets  
- experiments  
- baselines  
- ablation studies  
- results tables  

EBV scores computed per paper:

Output:
- `outputs/ebv_scores.csv`

Deliverables:
- EBV extraction module  
- Evidence scoring output

---

## 10. Sprint 8 – Evidence Salience & Weighting

Sprint 8 prevented appendix dumping and evidence gaming.

### Salience weighting:
- Main text evidence > Appendix-only evidence

We computed:

- Main evidence count  
- Appendix evidence count  
- Salience-aware EBV score

Output:
- `outputs/ebv_scores_salience.csv`

Deliverables:
- Salience-aware EBV scoring  
- Evidence weighting resistance

---

## 11. Sprint 9 – CDS Computation & Ablations

Sprint 9 implemented the divergence metric.

### CDS Formula:
**CDS = CSV – EBV**

Interpretation:
- High CDS → overclaim risk  
- Negative CDS → strongly supported claims  

We also ran ablation studies removing CSV dimensions:

Output:
- `outputs/cds_ablation_report.csv`

Deliverables:
- CDS computation module  
- Ablation correlation analysis

---

## 12. Sprint 10 – Calibration & Threshold Bands

Sprint 10 made CDS interpretable.

We calibrated divergence thresholds using percentiles:

- Moderate Divergence  
- High Divergence  

Output:
- `outputs/final_claim_scores_calibrated.csv`

Deliverables:
- CDS band calibration  
- Severity labeling

---

## 13. Sprint 11 – Validation & Proxy Meta-Analysis

Sprint 11 validated CDS without direct ground truth.

### Proxy checks:
- CDS vs EBV correlation (negative expected)  
- CDS vs CSV correlation (positive expected)

Validation report:
- `outputs/sprint11_validation_report.csv`

Deliverables:
- Scientific sanity validation  
- Paper-level divergence risk ranking

---

## 14. User Paper Testing (Generalization)

We extended CECDA beyond benchmark datasets.

The system now supports:

- Any user-uploaded PDF  
- IEEE papers  
- Papers outside NeurIPS/ICML/ICLR  

Single paper demo output:
- Claim-level CSV, EBV, CDS results  
- Saved under:
  `outputs/user_demo/`

This confirms cross-domain generalization.

---

## 15. Final Outputs Generated

The project produces:

- Extracted Claims CSV  
- Multi-dimensional CSV scores  
- EBV evidence breadth scores  
- Salience-weighted EBV  
- CDS divergence scores  
- Calibration bands  
- Validation reports  
- Demo outputs for user papers  

All results are stored inside the `outputs/` folder.

---

## 16. Conclusion

CECDA provides an automated framework to evaluate whether research claims are proportionally supported by evidence.  
It highlights divergence risks, encourages scientific accountability, and works across venues and user-provided papers.

This project demonstrates a full pipeline from dataset creation → annotation → claim scoring → evidence extraction → divergence calibration → validation → real-world deployment.

---

✅ Project Status: Functional End-to-End Prototype Complete  

