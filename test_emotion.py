import json
from emotion_detection import emotion_detector

result = emotion_detector('I am so happy today')
formatted = json.loads(result)
print(json.dumps(formatted, indent=4))