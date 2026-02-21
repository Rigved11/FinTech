import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay


df = pd.read_csv("fraud_data.csv")

print("Sample Data:")
print(df.head())

print("Data Info:")
df.info()

print("Basic Statistics:")
print(df.describe())

print("Class Distribution:")
print(df['is_fraud'].value_counts())
print(df['is_fraud'].value_counts(normalize=True))

sns.countplot(x='is_fraud', data=df)
plt.title("Imbalanced Classes")
plt.show()

df['is_fraud'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Fraud Probability Distribution")
plt.ylabel('')
plt.show()

print("Missing Before:")
print(df.isnull().sum())

df['amount'] = df.groupby('device_type')['amount'].transform(
    lambda x: x.fillna(x.median())
)

df['device_type'] = df['device_type'].fillna('unknown')

print("Missing After:")
print(df.isnull().sum())

plt.boxplot(df['amount'])
plt.title("Outliers in Transaction Amount")
plt.show()

# Cap extreme outliers
df['amount_cleaned'] = df['amount'].clip(upper=5000)

plt.boxplot(df['amount_cleaned'])
plt.title("After Outlier Capping")
plt.show()

df['amount_log'] = np.log1p(df['amount_cleaned'])
df['account_age_years'] = df['account_age_days'] / 365


df_ml = pd.get_dummies(
    df,
    columns=['device_type', 'transaction_type'],
    drop_first=True
)

print("Encoded Data Sample:")
print(df_ml.head())

features = [col for col in df_ml.columns 
            if col not in ['transaction_id', 'is_fraud', 'amount']]

X = df_ml[features]
y = df_ml['is_fraud']

print("Feature Columns:")
print(features)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(
    n_estimators=200,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

RocCurveDisplay.from_predictions(y_test, y_prob)
plt.title("ROC Curve")
plt.show()

importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)

importance.head(10).plot(kind='bar')
plt.title("Top 10 Important Features")
plt.show()
