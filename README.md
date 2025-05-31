# 🧠 Multi-Agent AI System with CrewAI

This is a Python-based multi-agent system using [CrewAI](https://github.com/joaomdmoura/crewai) that intelligently classifies and routes inputs in various formats — **PDF**, **JSON**, or **Email** — to specialized agents for structured extraction and processing.

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
git clone https://github.com/prerna-lily/Multi-AI-Agent.git
cd Multi-AI-Agent
