# agents/json_agent.py
from crewai import Agent
import json

class JSONAgent(Agent):
    def __init__(self, memory):
        super().__init__(
            name="JSONAgent",
            role="JSON Validator",
            goal="Extract and validate structured data from JSON payloads",
            backstory="This agent checks for anomalies or missing fields in JSON data used for business operations."
        )
        object.__setattr__(self, 'memory', memory)

    def run(self, data):
        try:
            obj = json.loads(data)
            anomalies = [k for k in ['invoice_id', 'amount', 'vendor'] if k not in obj]
            self.memory.log(
                source="JSON input",
                input_type="JSON",
                intent="Invoice",
                data=str(obj)
            )
            return {"status": "success", "parsed": obj, "anomalies": anomalies}
        except json.JSONDecodeError:
            return {"status": "error", "message": "Invalid JSON"}
