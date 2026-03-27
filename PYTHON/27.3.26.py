from sklearn.metrics import roc_auc_score

y_true = [0, 0, 1, 1]
y_prob = [0.1, 0.4, 0.35, 0.8]

auc = roc_auc_score(y_true, y_prob)

print("ROC-AUC Score:", auc)

# Explanation prints
print("\nNOTE:")
print("Predicted labels = 0 or 1")
print("Predicted probabilities = confidence (0 to 1)")
print("AUC = 1 → Perfect model")
print("AUC = 0.5 → Random guessing")
