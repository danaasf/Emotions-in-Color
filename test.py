from transformers import pipeline # type: ignore

# Load emotion classification model
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# Test text
text = "I am so happy and excited about today!"

# Run emotion analysis
result = classifier(text)
print(result)
