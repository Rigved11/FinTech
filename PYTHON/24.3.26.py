from sklearn.metrics import accuracy_score

y_true = [0, 0, 1, 1, 1]
y_pred = [0, 1, 1, 0, 1]

# sklearn accuracy
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy (sklearn):", accuracy)

# Manual accuracy
correct = sum([1 for i in range(len(y_true)) if y_true[i] == y_pred[i]])
manual_accuracy = correct / len(y_true)

print("Accuracy (manual):", manual_accuracy)