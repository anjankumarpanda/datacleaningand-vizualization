# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Original Data:\n", df)

# -------------------------------
# Step 1: Handle Missing Values
# -------------------------------
print("\nMissing Values:\n", df.isnull().sum())

df['Sales'].fillna(df['Sales'].mean(), inplace=True)
df['Profit'].fillna(df['Profit'].mean(), inplace=True)

# -------------------------------
# Step 2: Remove Duplicates
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# Step 3: Convert Data Types
# -------------------------------
df['Date'] = pd.to_datetime(df['Date'])

# -------------------------------
# Step 4: Handle Outliers
# -------------------------------
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Sales'] >= Q1 - 1.5 * IQR) & 
        (df['Sales'] <= Q3 + 1.5 * IQR)]

# -------------------------------
# Step 5: Visualization
# -------------------------------

# Bar chart
df.groupby('Product')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Product")
plt.show()

# Line chart
plt.plot(df['Date'], df['Sales'])
plt.title("Sales Trend")
plt.xticks(rotation=45)
plt.show()

# Histogram
plt.hist(df['Sales'])
plt.title("Sales Distribution")
plt.show()

# Heatmap
sns.heatmap(df[['Sales','Profit']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# Step 6: Insights
# -------------------------------
print("\nInsights:")
print("Highest sales product:", df.groupby('Product')['Sales'].sum().idxmax())
print("Average Sales:", df['Sales'].mean())
print("Average Profit:", df['Profit'].mean())