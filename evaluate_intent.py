from agent.intent_classifier import detect_intent
from test_cases import test_data

correct = 0

for case in test_data:
    predicted = detect_intent(case["text"])
    actual = case["intent"]

    print(f"Input: {case['text']}")
    print(f"Predicted: {predicted}, Actual: {actual}")

    if predicted == actual:
        correct += 1

accuracy = (correct / len(test_data)) * 100

print(f"\n🎯 Intent Accuracy: {accuracy:.2f}%")