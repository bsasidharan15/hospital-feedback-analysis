def validate_input(data):
    required_fields = ['audio_url']
    return all(field in data for field in required_fields)
