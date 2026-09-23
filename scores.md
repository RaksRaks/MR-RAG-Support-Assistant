# Evaluation Scorecard - FNB B4 RAG Support Assistant

## Scoring Categories
- Correct + cited: right answer with source filename(s)
- Correct but missing citation: right answer, no filename
- Wrong: incorrect or hallucinated answer
- Incorrectly refused or hallucinated: refused when it should not have, or invented an answer

---

## Results

| ID  | Question | Score | Notes |
|-----|----------|-------|-------|
| Q01 | What documents do I need to open a Business Account? | Correct + cited | Cited `01_account_types_eligibility.md`. Also pulled FICA doc as expected. |
| Q02 | How much does a lost debit card replacement cost? | Correct + cited | R95.00 correct. Cited `02_fees_and_charges.md`. |
| Q03 | How long does FICA verification usually take? | Correct + cited | 2 business days correct. Cited `03_fica_kyc_requirements.md`. |
| Q04 | Am I liable for fraud if my card was stolen and I reported it immediately? | Correct + cited | Not liable if reported correctly. Cited `04_card_digital_security.md`. |
| Q05 | What happens after I report a fraudulent transaction? | Correct + cited | 30-day window and investigation process correct. Cited `05_fraud_dispute_resolution.md`. |
| Q06 | What is the maximum overdraft limit available? | Correct + cited | R1,000 to R150,000 range correct. Cited `06_loans_overdraft.md`. |
| Q07 | How much money can I send abroad without Reserve Bank approval? | Correct + cited | R1 million SDA correct. Cited `07_forex_international_payments.md`. |
| Q08 | How do I escalate a complaint if I am not happy with the outcome? | Correct + cited | Team leader to Client Experience Office path correct. Cited `08_complaints_escalation.md`. |
| Q09 | Can I ask FNB B4 what personal data they hold about me? | Correct + cited | Data access right confirmed. Cited `09_data_privacy_popia.md`. |
| Q10 | Can I do an EFT payment using USSD banking? | Correct + cited | Pre-registered beneficiaries only, correct. Cited `10_digital_channels_guide.md`. |
| Q11 | What is FNB B4's stance on cryptocurrency trading accounts? | Correct refusal | Out-of-scope topic. Refused cleanly without hallucinating. |
| Q12 | What is my current account balance? | Correct refusal | Live account data request. Refused cleanly. |

---

## Summary

| Category | Count |
|----------|-------|
| Correct + cited | 10 |
| Correct refusal (trap questions) | 2 |
| Correct but missing citation | 0 |
| Wrong | 0 |
| Incorrectly refused or hallucinated | 0 |
| **Total** | **12/12** |

**Final Score: 12/12 - 100%**

> Note: Q11 and Q12 initially failed before guardrail improvements in Milestone 4.
> Q11 hallucinated an answer and Q12 gave a USSD workaround instead of refusing.
> Both were fixed by strengthening the system prompt refusal rules.
