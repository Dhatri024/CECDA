
Paste this skeleton:

```markdown
# CECDA: Claim–Evidence Coverage Divergence Analyzer

## 1. Introduction
Scientific papers often contain strong claims with varying levels of evidence.
CECDA detects divergence between claims and support.

## 2. Problem Definition
We define:

- Claim Strength Vector (CSV)
- Evidence Breadth Vector (EBV)
- Coverage Divergence Score (CDS)

CDS = CSV − EBV

## 3. Dataset Collection
We collected papers from:

- NeurIPS 2023
- ICML 2023
- ICLR 2023

## 4. Annotation Pilot
A pilot set of claims was manually labeled.
Self-consistency agreement reached 100%.

## 5. Claim Extraction Module
Rule-based extraction from abstract + conclusion.

Precision and recall evaluated using fuzzy matching.

## 6. CSV Scoring
Multi-dimensional scoring:

- Modality
- Comparative strength
- Generality
- Scope

## 7. EBV Evidence Extraction
Evidence signals extracted:

- Experiments
- Ablations
- Baselines
- Appendix salience weighting

## 8. CDS Computation
Divergence computed claim-wise and aggregated paper-wise.

## 9. Calibration & Severity Bands
Bands:

- Supported
- Aligned
- Moderate Divergence
- High Divergence Risk

## 10. Validation
Proxy validation:

- CDS vs EBV negative correlation
- CDS vs CSV positive correlation

## 11. Conclusion
CECDA provides a scalable framework to detect overclaiming risk in ML research.
