# agents/email_agent.py
from crewai import Agent
import re

class EmailAgent(Agent):
    def __init__(self):
        super().__init__(
            name="EmailAgent",
            role="Email Extractor",
            goal="Extract sender, urgency, and content from emails",
            backstory="This agent processes emails and extracts key CRM-style data like sender and intent."
        )
        # No memory needed

    def run(self, email_text):
        sender = re.findall(r"From: (.+)", email_text)
        urgency = "high" if any(w in email_text.lower() for w in ['urgent', 'asap']) else "normal"
        return {
            "sender": sender[0] if sender else "unknown",
            "urgency": urgency,
            "content": email_text[:500]
        }
