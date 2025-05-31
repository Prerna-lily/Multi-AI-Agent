
import json
import re

def detect_format_and_intent(data):
    if isinstance(data, dict):
        return "JSON", "Invoice" if "invoice" in json.dumps(data).lower() else "Unknown"
    elif isinstance(data, str):
        if data.strip().startswith("{"):
            return "JSON", "Unknown"
        elif "From:" in data:
            if "quote" in data.lower():
                return "Email", "RFQ"
            elif "complaint" in data.lower():
                return "Email", "Complaint"
            else:
                return "Email", "General"
        else:
            return "Text", "Unknown"
    else:
        return "Unknown", "Unknown"
