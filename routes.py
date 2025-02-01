from flask import Blueprint, request, jsonify
from app.services.azure_client import AzureBatchTranscriptionClient
from app.services.openai_client import OpenAIClient
from app.utils.helpers import validate_input

analysis_bp = Blueprint('analysis', __name__, url_prefix='/api')

@analysis_bp.route('/analyze', methods=['POST'])
def analyze_feedback():
    try:
        data = request.json
        if not validate_input(data):
            return jsonify({"error": "Invalid input"}), 400
            
        audio_url = data['audio_url']
        
        # Transcribe audio
        azure_client = AzureBatchTranscriptionClient()
        transcription = azure_client.process_audio(audio_url)
        
        # Analyze sentiment
        openai_client = OpenAIClient()
        analysis_result = openai_client.analyze_sentiment(transcription)
        
        return jsonify({
            "transcription": transcription,
            "sentiment_analysis": analysis_result
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
