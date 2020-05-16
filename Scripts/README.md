# Rover Control Scripts

## List of dependencies per module

### Actuator Control
- BrickPi3 Python library (included in Raspbian for Robots)
- identification of multiple BrickPis by Serial Number

### Camera Feed
- PiCamera Python library for use with original Cam V2
- colour recognition with OpenCV

### Text To Speech
- pyttsx3
- espeak (other TTS engines might be possible)

### Voice Recognition
- SpeechRecognition Python library (has many dependencies itself)
- Snowboy hotword detection to be implemented (currently disabled to avoid runtime errors)
- target detection engine: (pocket)sphinx (offline recognition)
- current detection engine: google web service for speech recognition
  - higher accuracy (with current microphone)
  - better performance (with current microphone)
  - requires internet connection
