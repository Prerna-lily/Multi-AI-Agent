from agents.pdf_agent import PDFAgent
from memory.shared_memory import SharedMemory
from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent

def run_system(input_data, input_type="text"):
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)
    json_agent = JSONAgent(memory)
    email_agent = EmailAgent()
    pdf_agent = PDFAgent(memory)

    # If input is a PDF file path, we skip format detection
    if input_type == "pdf":
        fmt = "PDF"
        intent = "Document"
    else:
        fmt, intent = classifier.run(input_data)

    # Route based on format
    if fmt == "JSON":
        result = json_agent.run(input_data)
    elif fmt == "Email":
        result = email_agent.run(input_data)
    elif fmt == "PDF":
        result = pdf_agent.run(input_data)
    else:
        result = {"status": "Unsupported format"}

    memory.log(source="processor", input_type=fmt, intent=intent, data=str(result))
    return result

if __name__ == "__main__":
    # Test with email
    with open("examples/sample_email.txt") as f:
        email_content = f.read()
    print(">> EMAIL TEST RESULT:")
    print(run_system(email_content))

    # Test with JSON
    with open("examples/sample_invoice.json") as f:
        json_content = f.read()
    print("\n>> JSON TEST RESULT:")
    print(run_system(json_content))

    # Test with PDF
    pdf_path = "examples/sample.pdf"
    print("\n>> PDF TEST RESULT:")
    print(run_system(pdf_path, input_type="pdf"))
