from sklearn.metrics import f1_score

y_true = [0, 0, 1, 1, 1]
y_pred = [0, 1, 1, 0, 1]

f1 = f1_score(y_true, y_pred)

print("F1 Score:", f1)

# Manual calculation
precision = 2 / (2 + 1)
recall = 2 / (2 + 1)

f1_manual = 2 * (precision * recall) / (precision + recall)

print("Manual F1 Score:", f1_manual)
