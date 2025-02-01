import os
import openai

class OpenAIClient:
    def __init__(self):
        openai.api_type = "azure"
        openai.api_key = os.getenv("AZURE_OPENAI_KEY")
        openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    def analyze_sentiment(self, text):
        prompt = f"""Analyze this Tamil customer feedback and provide sentiment and key issues:
        {text}
        
        Respond with JSON format:
        {{
            "sentiment": "positive|neutral|negative",
            "issues": ["list", "of", "key", "issues"]
        }}"""
        
        response = openai.ChatCompletion.create(
            engine=self.deployment_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        return eval(response.choices[0].message.content)
