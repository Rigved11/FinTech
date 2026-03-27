from sklearn.metrics import confusion_matrix

y_true = [0, 0, 1, 1, 1]
y_pred = [0, 1, 1, 0, 1]

cm = confusion_matrix(y_true, y_pred)

print("Confusion Matrix:\n", cm)

# Extract values
TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

print("\nTrue Negatives:", TN)
print("False Positives:", FP)
print("False Negatives:", FN)
print("True Positives:", TP)

print("\nTotal Correct Predictions:", TN + TP)
