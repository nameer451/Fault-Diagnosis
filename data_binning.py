import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_excel("C:\\Users\\Nameer Ahmed\\Desktop\\fault_data.xlsx")

# Initialize the scaler (StandardScaler performs Z-score normalization)
z_scaler = StandardScaler()

# Normalize specific columns using Z-score scaling
columns_to_normalize_with_zscore = [
    'alignment_error',
    'noise_level',
]
df[columns_to_normalize_with_zscore] = z_scaler.fit_transform(df[columns_to_normalize_with_zscore])

# Function to categorize based on Z-score
def categorize_using_zscore(zscore):
    if zscore < -2:
        return 'Critical'
    elif -2 <= zscore < -1:
        return 'Low'
    elif -1 <= zscore < 1:
        return 'Medium'
    elif 1 <= zscore < 2:
        return 'High'
    else:
        return 'Critical'  # Values above +2 are categorized as 'Critical'

# Replace the original columns with categories
for col in columns_to_normalize_with_zscore:
    df[col] = df[col].apply(categorize_using_zscore)


df['system_failure'] = df['system_failure'].astype(bool).astype(str)

# Define a mapping function to convert 0 and 1 values
def map_values(value):
    return 'low' if value == 0 else 'high'

# Apply the mapping function to all the specified columns
columns_to_transform = ['emission_level', 'power_draw', 'system_load']
for col in columns_to_transform:
    df[col] = df[col].apply(map_values)

# Map vibration and temp levels to 'low', 'medium', 'high'
map = {1: 'low', 2: 'medium', 3: 'high'}
df['vibration'] = df['vibration'].map(map)
df['temp'] = df['temp'].map(map)

df.to_excel('categorized_data.xlsx', index=False)
# Print the updated DataFrame to check the results
print(df)
