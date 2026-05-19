import time
import pandas as pd
from collections import defaultdict

from test_dataset import test_cases
from agent.agent_executor import run_agent


# ==========================================
# METRICS VARIABLES
# ==========================================

total_samples = len(test_cases)

intent_correct = 0
tool_correct = 0

total_response_time = 0

# Per-intent tracking
intent_total = defaultdict(int)
intent_success = defaultdict(int)

results = []


# ==========================================
# TEST LOOP
# ==========================================

for case in test_cases:

    text = case["input"]

    expected_intent = case["intent"]

    expected_tool = case["tool"]

    print("\n===================================")
    print("INPUT:", text)

    # ⏱ START TIMER
    start = time.time()

    # 🔥 RUN AGENT
    result = run_agent(text)

    # ⏱ END TIMER
    end = time.time()

    response_time = end - start

    total_response_time += response_time

    # 🔥 GET RESULTS
    predicted_intent = result["intent"]

    selected_tool = result["tool"]

    response = result["response"]

    # ==========================================
    # INTENT ACCURACY
    # ==========================================

    if predicted_intent == expected_intent:

        intent_correct += 1

        intent_success[expected_intent] += 1

    intent_total[expected_intent] += 1

    # ==========================================
    # TOOL ACCURACY
    # ==========================================

    if selected_tool == expected_tool:

        tool_correct += 1

    # ==========================================
    # PRINT RESULTS
    # ==========================================

    print("EXPECTED INTENT:",
          expected_intent)

    print("PREDICTED INTENT:",
          predicted_intent)

    print("EXPECTED TOOL:",
          expected_tool)

    print("SELECTED TOOL:",
          selected_tool)

    print("RESPONSE TIME:",
          round(response_time, 3), "sec")

    print("RESPONSE:",
          str(response)[:100])

    # ==========================================
    # SAVE CSV RESULTS
    # ==========================================

    results.append({

        "Input": text,

        "Expected Intent": expected_intent,

        "Predicted Intent": predicted_intent,

        "Expected Tool": expected_tool,

        "Selected Tool": selected_tool,

        "Correct Intent":
            predicted_intent == expected_intent,

        "Correct Tool":
            selected_tool == expected_tool,

        "Response Time":
            round(response_time, 3)
    })


# ==========================================
# FINAL METRICS
# ==========================================

overall_intent_accuracy = (
    intent_correct / total_samples
) * 100

tool_selection_accuracy = (
    tool_correct / total_samples
) * 100

average_response_time = (
    total_response_time / total_samples
)

# ==========================================
# PER-INTENT ACCURACY
# ==========================================

reminder_accuracy = (
    intent_success["reminder"] /
    intent_total["reminder"]
) * 100

emergency_accuracy = (
    intent_success["emergency"] /
    intent_total["emergency"]
) * 100

news_accuracy = (
    intent_success["news"] /
    intent_total["news"]
) * 100

chat_accuracy = (
    intent_success["chat"] /
    intent_total["chat"]
) * 100


# ==========================================
# FINAL OUTPUT
# ==========================================

print("\n\n======================================")
print("FINAL EVALUATION RESULTS")
print("======================================")

print("\n✅ OVERALL INTENT ACCURACY:",
      round(overall_intent_accuracy, 2), "%")

print("✅ TOOL SELECTION ACCURACY:",
      round(tool_selection_accuracy, 2), "%")

print("✅ AVERAGE RESPONSE TIME:",
      round(average_response_time, 3), "sec")

print("\n--------------------------------------")

print("✅ REMINDER DETECTION ACCURACY:",
      round(reminder_accuracy, 2), "%")

print("✅ EMERGENCY DETECTION ACCURACY:",
      round(emergency_accuracy, 2), "%")

print("✅ NEWS DETECTION ACCURACY:",
      round(news_accuracy, 2), "%")

print("✅ CHAT DETECTION ACCURACY:",
      round(chat_accuracy, 2), "%")

print("======================================")


# ==========================================
# SAVE RESULTS TO CSV
# ==========================================

df = pd.DataFrame(results)

df.to_csv(
    "evaluation_results.csv",
    index=False
)

print("\n✅ evaluation_results.csv saved successfully")