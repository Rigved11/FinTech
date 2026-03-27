from sklearn.metrics import precision_score, recall_score

y_true = [0, 0, 1, 1, 1]
y_pred = [0, 1, 1, 0, 1]

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

print("Precision:", precision)
print("Recall:", recall)

# Manual calculation
TP = 2
FP = 1
FN = 1

manual_precision = TP / (TP + FP)
manual_recall = TP / (TP + FN)

print("\nManual Precision:", manual_precision)
print("Manual Recall:", manual_recall)