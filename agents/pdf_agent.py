# agents/pdf_agent.py
from crewai import Agent
import fitz  # PyMuPDF

class PDFAgent(Agent):
    def __init__(self, memory):
        super().__init__(
            name="PDFAgent",
            role="PDF Extractor",
            goal="Extract and interpret data from PDF documents",
            backstory="This agent specializes in understanding invoices, RFQs, and formal documents from PDFs."
        )
        object.__setattr__(self, 'memory', memory)

    def run(self, pdf_path):
        try:
            doc = fitz.open(pdf_path)
            text = "\n".join([page.get_text() for page in doc])
            doc.close()

            self.memory.log(
                source=pdf_path,
                input_type="PDF",
                intent="Extracted PDF content",
                data=text[:500]
            )

            return {"status": "success", "content": text[:1000]}
        except Exception as e:
            return {"status": "error", "message": str(e)}
