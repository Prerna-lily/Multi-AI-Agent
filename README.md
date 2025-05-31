# 🧠 Multi-Agent AI System with CrewAI

This is a Python-based multi-agent system using [CrewAI](https://github.com/joaomdmoura/crewai) that intelligently classifies and routes inputs in various formats — **PDF**, **JSON**, or **Email** — to specialized agents for structured extraction and processing.
Objective
Build a multi-agent AI system that accepts input in PDF, JSON, or Email (text) format, classifies the format and intent, and routes it to the appropriate agent. The system must maintain shared context (e.g., sender, topic, last extracted fields) to enable chaining and traceability.

System Overview
You will build 3 agents, orchestrated via a central Classifier Agent:

1. Classifier Agent
Input: raw file/email/JSON
Classifies:
Format: PDF / JSON / Email
Intent: Invoice, RFQ, Complaint, Regulation, etc.
Routes to correct agent
Logs format + intent in memory

2. JSON Agent
Accepts structured JSON payloads
Extracts/reformats to a target schema
Flags anomalies or missing fields

3. Email Agent
Accepts email content
Extracts sender, intent, urgency
Formats for CRM-style usage

---

## 📦 Features

- 🧭 **Classifier Agent**: Detects format (PDF/JSON/Email) and intent (Invoice, RFQ, etc.)
- 📨 **Email Agent**: Extracts sender, urgency, and body from plain-text emails
- 🧾 **JSON Agent**: Validates JSON structure and flags anomalies
- 📄 **PDF Agent**: Parses PDFs and extracts content using PyMuPDF
- 🧠 **Shared Memory**: Lightweight context store for logging and chaining

---

## 🧰 Tech Stack

- **Python 3.10+**
- [CrewAI](https://github.com/joaomdmoura/crewai)
- **PyMuPDF** for PDF parsing
- **In-memory shared memory** for context tracking

---

## 🚀 Setup

### 1. Clone this Repo

```bash
git clone https://github.com/prerna-lily/Multi-Agent-AI-System-with-CrewAI.git
cd Multi-Agent-AI-System-with-CrewAI

---

### Folder Structure

multi_agent_system/
├── agents/
│   ├── classifier_agent.py
│   ├── email_agent.py
│   ├── json_agent.py
│   └── pdf_agent.py
├── examples/
│   ├── sample_email.txt
│   ├── sample_data.json
│   └── sample.pdf
├── memory/
│   └── shared_memory.py
├── main.py
└── README.md

