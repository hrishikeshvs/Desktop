import pandas as pd

# Load the dataset
df = pd.read_csv('sample_advertisement_ecommerce_dataset.csv')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Check for missing values
missing_values = df.isnull().sum()

# Ensure numeric columns are formatted correctly
df[['Ad_Spend', 'Sales', 'Clicks', 'Conversions']] = df[['Ad_Spend', 'Sales', 'Clicks', 'Conversions']].apply(pd.to_numeric)

# Display cleaned DataFrame and missing values
print(df.head())
print(missing_values)
