from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("student_exam_data.csv")
df.columns = ["study_hours", "prev_score", "result"]

X = df[["study_hours", "prev_score"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Probabilities:\n", model.predict_proba(X_test))
# assumes model, X_test, y_test already defined

pred = model.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

prob = model.predict_proba(X_test)[:, 1]
print("AUC:", roc_auc_score(y_test, prob))