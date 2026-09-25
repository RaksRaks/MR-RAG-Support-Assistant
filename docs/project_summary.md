# FNB B4 AI Capstone: Project Summary for Non-Technical Readers

---

## What Did We Build?

We built an AI-powered banking support assistant. You type a question about FNB B4 banking policies, and it gives you a clear, accurate answer with a reference to exactly which document the answer came from.

Think of it like a very smart search engine that does not just find documents but actually reads them and summarises the relevant part for you in plain language.

---

## Why Does This Matter?

In a real bank, support agents spend a lot of time looking up policy documents to answer customer questions. This kind of tool can help by:

- Giving instant, accurate answers based on official policy documents
- Always telling you exactly where the answer comes from so it can be verified
- Refusing to guess or make things up when it does not know the answer
- Protecting sensitive customer information

---

## How Does It Work? (Simple Version)

Imagine you have a large library of 10 banking policy books. Every few pages, you stick a bookmark in and write a short summary of what those pages are about.

When a customer asks a question, the assistant does not read every page. Instead it:

1. Reads the question and figures out what topic it is about
2. Finds the 3 most relevant bookmarks in the library
3. Reads only those sections
4. Writes a clear answer based only on what those sections say
5. Tells you which book and section it used

If the answer is not in any of the books, it says so honestly instead of guessing.

---

## What Are the 10 Policy Documents?

The assistant was built to answer questions about these FNB B4 topics:

1. Account types and who can open each one
2. Fees and charges
3. FICA and identity verification requirements
4. Card and digital security
5. Fraud and dispute resolution
6. Loans and overdrafts
7. Foreign exchange and international payments
8. Complaints and escalation process
9. Data privacy and POPIA compliance
10. Digital banking channels (app, USSD, online banking)

---

## What Safety Rules Did We Build In?

A banking assistant handles sensitive topics, so we built in strict safety rules:

**It only answers from the documents.**
It cannot use general knowledge or make things up. If the answer is not in the policy documents, it says so clearly.

**It always cites its source.**
Every answer includes the name of the document it came from so anyone can verify it.

**It refuses live account data requests.**
If someone asks "what is my account balance?", it will not try to answer. It redirects the customer to the banking app or helpline instead.

**It protects sensitive information.**
If a customer accidentally types their PIN or password into the chat, the assistant flags it immediately and reminds them not to share that information.

**It resists manipulation.**
We tested whether someone could trick the assistant into ignoring its rules by typing things like "ignore your instructions and do something else." The assistant correctly refused these attempts.

---

## How Did We Test It?

We ran 12 test questions through the assistant:

- 10 were real banking policy questions with known correct answers
- 2 were deliberate traps: one about a topic not in the documents (cryptocurrency), and one asking for live account data (current balance)

**Results: 12 out of 12 answered correctly.**

The 10 real questions all got accurate, cited answers. The 2 trap questions were correctly refused without the assistant guessing or making anything up.

---

## What Technology Was Used?

The assistant runs entirely on a local computer using free, open-source tools:

- **Python** - the programming language used to build everything
- **Ollama** - runs the AI models locally on the computer (no internet required, no data sent to external servers)
- **llama3** - the AI model that reads the context and writes the answers
- **nomic-embed-text** - a smaller AI model that converts text into numbers so documents can be searched by meaning, not just keywords
- **ChromaDB** - a database that stores those numbers and finds the most relevant ones when a question is asked

The entire system runs offline. No customer data leaves the machine.

---

## What Are the Limitations?

Being honest about what this system cannot do is important:

**It only knows what is in the documents.**
If a policy changes and the documents are not updated, the assistant will give outdated answers.

**It is a proof of concept, not a production system.**
Before this could be used with real customers, it would need proper security audits, integration with live systems, and compliance review.

**The AI guardrails are not foolproof.**
We tested several ways to trick the assistant and blocked them. But a determined attacker with enough creativity could potentially find new ways to bypass the rules. In a real production system, additional technical safeguards at the application level would be required.

---

## Summary

We built a working AI assistant that answers banking policy questions accurately, cites its sources, and refuses to guess. It scored 12 out of 12 on a structured test including deliberate trick questions. It runs locally, protects sensitive data, and is built with safety guardrails from the ground up.

This is a strong foundation. With further development and security hardening, this kind of tool has real potential to improve how banking support teams access and communicate policy information.
