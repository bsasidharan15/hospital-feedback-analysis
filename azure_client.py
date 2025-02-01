import os
import time
import requests
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer

class AzureBatchTranscriptionClient:
    def __init__(self):
        self.speech_key = os.getenv("AZURE_SPEECH_KEY")
        self.service_region = os.getenv("AZURE_SPEECH_REGION")
        self.endpoint_url = f"https://{self.service_region}.api.cognitive.microsoft.com/speechtotext/v3.1/transcriptions"

    def create_transcription_job(self, audio_url):
        headers = {
            "Ocp-Apim-Subscription-Key": self.speech_key,
            "Content-Type": "application/json"
        }
        
        body = {
            "contentUrls": [audio_url],
            "locale": "ta-IN",
            "displayName": "HospitalFeedbackAnalysis"
        }
        
        response = requests.post(self.endpoint_url, json=body, headers=headers)
        return response.json()['self']

    def get_transcription_result(self, transcription_url):
        headers = {"Ocp-Apim-Subscription-Key": self.speech_key}
        
        while True:
            response = requests.get(transcription_url, headers=headers)
            status = response.json()['status']
            
            if status == 'Succeeded':
                files = response.json()['results']['files']
                result_url = next(f['links']['contentUrl'] for f in files if f['kind'] == 'Transcription')
                return requests.get(result_url).json()['combinedRecognizedPhrases'][0]['display']
                
            time.sleep(15)

    def process_audio(self, audio_url):
        job_url = self.create_transcription_job(audio_url)
        return self.get_transcription_result(job_url)
