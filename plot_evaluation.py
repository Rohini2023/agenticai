import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# ==========================================
# LOAD CSV
# ==========================================

csv_file = "evaluation_results.csv"


df = pd.read_csv(csv_file)

print(df.head())


# ==========================================
# CONFUSION MATRIX
# ==========================================

true_labels = df["Expected Intent"]
predicted_labels = df["Predicted Intent"]

labels = [
    "reminder",
    "emergency",
    "news",
    "chat"
]

cm = confusion_matrix(
    true_labels,
    predicted_labels,
    labels=labels
)


# ==========================================
# PLOT CONFUSION MATRIX
# ==========================================

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels
)

plt.title("Intent Classification Confusion Matrix")

plt.xlabel("Predicted Intent")

plt.ylabel("Actual Intent")

plt.savefig("confusion_matrix.png")

plt.show()


# ==========================================
# CLASSIFICATION REPORT
# ==========================================

print("\n==============================")
print("CLASSIFICATION REPORT")
print("==============================")

report = classification_report(
    true_labels,
    predicted_labels
)

print(report)

print("\nGraphs Saved Successfully")