# CECDA Annotation Guidelines (Sprint 4)

## 1. Claim Identification Rules

A sentence is a CLAIM if it asserts:

- A new method or contribution  
- A performance/generalization advantage  
- An interpretability/scientific insight  
- A strong conclusion about results  

Not claims:

- Background statements  
- Related work summaries  
- Motivation text  

---

## 2. Claim Strength Labels

### LOW
- Narrow or cautious claim  
- Uses: "may", "suggest", "preliminary"

Example:
"Our results suggest potential improvement."

---

### MEDIUM
- Clear contribution but scoped  
- Uses: "we propose", "we introduce"

Example:
"We propose a new VAE architecture."

---

### HIGH
- Strong general or comparative claim  
- Uses: "outperforms", "achieves SOTA", "generalizes"

Example:
"Our model outperforms all baselines on OOD tasks."

---

## 3. Evidence Breadth Labels

### LOW
- Only 1 dataset  
- No ablations  
- No baselines  
- No variance reporting  

---

### MEDIUM
- 2 datasets  
- Some baselines  
- Limited analysis  

---

### HIGH
- Multiple datasets + OOD  
- Ablations + baselines  
- Variance/seeds + failure discussion  

---

## 4. Annotation Output Format

Each row must contain:

paper_id, claim_text, claim_strength_label, evidence_breadth_label, annotator
