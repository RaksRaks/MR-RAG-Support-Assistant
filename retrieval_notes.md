# 1. My Chunking Strategy
- I first looked at what differentiates the paragraphs or spaces between words.
- Identified that '##' separates the Paragraphs
- chose it as a spltter

# 2. Chunk Size
- My chunk size was 5-8 chunks per document 

# K-Value 
- My k-value was chosen to be three in order for optionality, and also for capturing how accurate is the retrival of the first match and how far off is it from the second one. k=3 also means the LLM gets enough context from multiple angles without being overwhelmed with too much noise. But that's optional polish.

# Observations
- I saw that the flow works together to retrieve relevant sources for example this:
Testing the question:  What are the requirements to open a cheque account?
Source: 01_account_types_eligibility.md
Cheque Account
- For customers aged 18 and older with a verified South African ID or valid work permit.
- Requires proof of residence not older than 3 months and proof of income for credit-linked p
---
the retrieval wen straight to account eligibility.
