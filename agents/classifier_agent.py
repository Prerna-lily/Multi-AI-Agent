from crewai import Agent
from utils import detect_format_and_intent

class ClassifierAgent(Agent):
    def __init__(self, memory):
        super().__init__(
            name="ClassifierAgent",
            role="Classifier",
            goal="Classify the input's format and intent",
            backstory="This agent determines the type of input (email, JSON, PDF) and its business intent (invoice, RFQ, complaint)."
        )
        object.__setattr__(self, 'memory', memory)

    def run(self, input_data):
        format_type, intent = detect_format_and_intent(input_data)
        self.memory.log(source="input", input_type=format_type, intent=intent, data=str(input_data)[:500])
        return format_type, intent
