
import pandas as pd

# Load dataset
df = pd.read_csv("data/air_quality_data.csv")

# Check missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Save cleaned dataset
df.to_csv("data/cleaned_air_quality.csv", index=False)
print("Data cleaning complete. Saved as cleaned_air_quality.csv")
