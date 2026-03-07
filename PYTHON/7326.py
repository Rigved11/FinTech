import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler 
import scipy.cluster.hierarchy as sch 
import time 

print("Libraries Imported Successfully!")

data = {
    'Customer': [1,2,3,4,5,6,7,8,9,10,11],
    'Spending': [20,80,88,24,45,30,32,90,65,78,85]
}

df = pd.DataFrame(data)
X = df[['Spending']].values

print(df.head(5))

# Original elbow plot (untimed)
inertia = []
K_range = range(1,8)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10,4))
plt.plot(K_range, inertia, marker='o')     
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method (Customer Spending)')
plt.show()

# Performance measurement (corrected)
start_total = time.time()  # Fixed: was undefined start_total
inertia_times = []  # Fixed: was 'inertie' and 'time'
times = []  # Fixed: was 'times' but defined as 'time'

for k in K_range:
    start_k = time.time()
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia_times.append(kmeans.inertia_)
    times.append(time.time() - start_k)

total_time = time.time() - start_total
print(f"Total: {total_time:.4f}s, Avg per k: {total_time/7:.4f}s")
print("Per k times:", [f"{t:.4f}s" for t in times])


start_time=time.perf_counter()

kmeans = KMeans(n_clusters=2,random_state=42,n_init=10)
df['Kmeans_Cluster']=kmeans.fit_predict(X)

print(df)
plt.figure(figsize=(10,4))
sns.scatterplot(data=df,x='Customer',y='Spending',hue='Kmeans_Cluster',palette='viridis',s=100)
plt.title('K-Means Clustering (K=2)')
plt.show()

end_time=time.perf_counter()

elapsed_time=end_time-start_time
print(f"Function executed in {elapsed_time:.4f}seconds")


end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"K=2 clustering executed in {elapsed_time:.4f} seconds")

plt.figure(figsize=(10,4))
dendrogram=sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrogram (Customer Spending)')
plt.show()

hc = AgglomerativeClustering(n_clusters=2,linkage='ward')
df['Hierarchical_Cluster']=hc.fit_predict(X)

print(df)
plt.figure(figsize=(10,5))
sns.scatterplot(data=df,x='Customer',y='Spending',hue='Hierarchical_Cluster',palette='magma',s=100)
plt.title('Hierarchical Clustering (2 Clusters)')
plt.show()

loan_data={
    'Loan ID':[1,2,3,4,5,6,7,8,9,10],
    'Age':[25,35,28,45,22,50,45,45,80,27],
    'Loan Amt':[5,15,30,10,10,12,18,35,80,22],
    'Rate':[8,6.5,9.5,5,10,4.5,7.5,8,6,8.5],
    'Income':[60,60,35,80,25,90,55,100,70,40]
}

df_loan=pd.DataFrame(loan_data)
print("Loan Dataset Preview:")
print(df_loan.head())

features = ['Age','Loan Amt','Rate','Income']
X_loan=df_loan[features].values

scaler=StandardScaler()
X_loan_scaled=scaler.fit_transform(X_loan)