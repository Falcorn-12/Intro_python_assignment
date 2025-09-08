# Data Analysis Assignment - Jupyter Notebook

# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset directly from sklearn
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first 5 rows
print(" First 5 rows of the dataset:")
print(df.head(), "\n")

# Check data types and missing values
print(" Data info:")
print(df.info(), "\n")
print(" Missing values per column:")
print(df.isnull().sum(), "\n")

# Task 2: Basic Data Analysis
print(" Basic Statistics:")
print(df.describe(), "\n")

# Grouping: Mean of numerical columns by species
grouped = df.groupby("species").mean()
print(" Mean values per species:")
print(grouped, "\n")

# Task 3: Data Visualizations

# Line chart (simulated time-series by using index as x-axis)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# Bar chart: Average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.show()

# Histogram: Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Sepal length vs Sepal width
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)", y="sepal width (cm)", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Sepal Width")
plt.show()

# Findings
print(" Observations:")
print("1. Iris-setosa generally has smaller petal length compared to others.")
print("2. Sepal width shows more spread than sepal length.")
print("3. Sepal length and width show clustering patterns based on species.")