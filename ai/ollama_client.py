import requests

class OllamaClient:
    def __init__(self, model="gemma3:4b", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url

    def generate_privacy_report(self, osint_data):
        prompt = f"""
        You are an expert Privacy Exposure Auditor. 
        Analyze the following social media OSINT data.
        Your goal is to infer what a stranger could figure out about this person's real life.
        
        DATA:
        --- START DATA ---
        {osint_data}
        --- END DATA ---
        
        Provide a structured report in EXACTLY this format:
        
        [INFERRED LOCATION]
        - What area, city, or landmarks can be inferred based on bios, posts, or tags?
        
        [INFERRED ROUTINE]
        - What daily habits, work hours, or routines can be inferred?
        
        [INFERRED RELATIONSHIPS]
        - What family, friends, or workplace connections can be inferred based on followers or bio?
        
        [ACTIONABLE FIXES]
        - List 3 concrete steps the user should take to reduce this exposure.
        """
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(f"{self.base_url}/api/generate", json=payload)
            return response.json()["response"].strip()
        except Exception as e:
            return f"Error connecting to Ollama: {e}"