import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

# Load data
df = pd.read_csv("fraud_data.csv")

print("sample data:")
print(df.head())

print("data information : ")
print(df.info())

print("basic statistics table:")
print(df.describe())

# Fraud count
fraud_only = df[df['is_fraud'] == 1]
print(f"total fraud cases found : {len(fraud_only)}")

print("class distribution:")
print(df['is_fraud'].value_counts(normalize=True))

# Countplot
sns.countplot(x='is_fraud', data=df)
plt.title('Imbalanced Classes')
plt.show()

# Pie chart
df['is_fraud'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)
plt.title('Fraud Probability Distribution')
plt.ylabel('')
plt.show()

# Missing values
print("missing before handling : ")
print(df.isnull().sum())

df['amount'] = df.groupby('device_type')['amount'].transform(
    lambda x: x.fillna(x.median())
)

df['device_type'] = df['device_type'].fillna('unknown')

print("missing after handling :")
print(df.isnull().sum())

# Outlier detection
plt.boxplot(df['amount'])
plt.title('Spotting Outliers in Transaction Amounts')
plt.show()

# Cap outliers
df['amount_cleaned'] = df['amount'].clip(upper=5000)

plt.boxplot(df['amount_cleaned'])
plt.title('After Capping Outliers')
plt.show()

# Encoding
df_ml = pd.get_dummies(df, columns=['device_type'], drop_first=True)

# Features & Target
features = ['amount_cleaned'] + [col for col in df_ml.columns if 'device_type' in col]
X = df_ml[features]
y = df_ml['is_fraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training Size: {X_train.shape[0]}, Testing Size: {X_test.shape[0]}")

# Train Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train, y_train)

# Predictions
y_pred = log_model.predict(X_test)
y_prob = log_model.predict_proba(X_test)[:, 1]

# Custom threshold
new_threshold = 0.3
y_pred_new = (y_prob >= new_threshold).astype(int)

# Confusion matrices
cm_default = confusion_matrix(y_test, y_pred)
cm_custom = confusion_matrix(y_test, y_pred_new)

print("Confusion Matrix (Default 0.5 Threshold):")
print(cm_default)

print("\nConfusion Matrix (Custom 0.3 Threshold):")
print(cm_custom)

print("\nClassification Report (Custom Threshold):")
print(classification_report(y_test, y_pred_new))

print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

# Plot confusion matrices
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

sns.heatmap(cm_default, annot=True, fmt='d', cmap='Blues', ax=ax1)
ax1.set_title('Default Threshold (0.5)')
ax1.set_xlabel('Predicted Label')
ax1.set_ylabel('True Label')

sns.heatmap(cm_custom, annot=True, fmt='d', cmap='Blues', ax=ax2)
ax2.set_title('Custom Threshold (0.3)')
ax2.set_xlabel('Predicted Label')
ax2.set_ylabel('True Label')

plt.tight_layout()
plt.show()