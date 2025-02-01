```markdown
# 🏥 Hospital Feedback Analysis System 💬

An AI-powered system for analyzing customer feedback sentiments using Azure Speech-to-Text and OpenAI GPT-3.5 Turbo.

## Features

- 🎙️ Batch audio transcription (Tamil language support)
- 🤖 AI-powered sentiment analysis
- 📦 JSON input/output format
- 🌐 RESTful API endpoints
- 🚀 Memory-efficient batch processing
- 📊 Sentiment visualization and insights
- 🔄 Automatic conversion between audio and text

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/HospitalFeedbackAnalysis.git

# Navigate to the project directory
cd HospitalFeedbackAnalysis

# Install required dependencies
pip install -r requirements.txt
```

## Dependencies

- Python 3.7+
- Flask
- Azure Cognitive Services Speech SDK
- OpenAI API
- python-dotenv
- requests

## Usage

### Basic Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Send a POST request to the API endpoint:
   ```bash
   curl -X POST http://localhost:5000/api/analyze \
     -H "Content-Type: application/json" \
     -d '{"audio_url": "https://example.com/feedback.wav"}'
   ```

### Example Response

```json
{
  "transcription": "உங்கள் சேவை மிகவும் நன்றாக இருந்தது.",
  "sentiment_analysis": {
    "sentiment": "positive",
    "issues": []
  }
}
```

## API Reference

### POST `/api/analyze`

Analyzes customer feedback from an audio file.

#### Request Body
```json
{
  "audio_url": "string (URL to the audio file)"
}
```

#### Response
```json
{
  "transcription": "string (Transcribed text)",
  "sentiment_analysis": {
    "sentiment": "string (positive|neutral|negative)",
    "issues": ["list", "of", "key", "issues"]
  }
}
```

## Examples

### Analyzing Feedback

```python
import requests

url = "http://localhost:5000/api/analyze"
payload = {
    "audio_url": "https://example.com/feedback.wav"
}

response = requests.post(url, json=payload)
print(response.json())
```

### Batch Processing

For batch processing, you can loop through multiple audio URLs and send requests to the API.

```python
audio_urls = [
    "https://example.com/feedback1.wav",
    "https://example.com/feedback2.wav",
    "https://example.com/feedback3.wav"
]

for url in audio_urls:
    response = requests.post("http://localhost:5000/api/analyze", json={"audio_url": url})
    print(response.json())
```

## Configuration

1. Create a `.env` file in the root directory:
   ```bash
   cp config/.env.example .env
   ```

2. Add your Azure and OpenAI credentials:
   ```
   AZURE_SPEECH_KEY=your_azure_speech_key
   AZURE_SPEECH_REGION=your_azure_region
   AZURE_OPENAI_KEY=your_openai_key
   AZURE_OPENAI_ENDPOINT=your_openai_endpoint
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Author

Sasidharan B

## Acknowledgments

- Thanks to Azure Cognitive Services for Speech-to-Text capabilities
- Thanks to OpenAI for GPT-3.5 Turbo sentiment analysis
- Built with Flask and Python
```
