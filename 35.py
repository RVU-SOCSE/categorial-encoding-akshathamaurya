import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Step 1: Create Laptop Dataset

data = {
    'Brand': ['Dell', 'HP', 'Apple', 'Dell', 'HP'],
    'Processor': ['i5', 'i7', 'M1', 'i3', 'i5'],
    'Price': [50000, 65000, 120000, 40000, 52000]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)


# Step 2: Label Encoding

le = LabelEncoder()

df['Brand_Label'] = le.fit_transform(df['Brand'])
df['Processor_Label'] = le.fit_transform(df['Processor'])

print("\nAfter Label Encoding:\n")
print(df)


# Step 3: One-Hot Encoding

ohe = OneHotEncoder(sparse_output=False)

encoded = ohe.fit_transform(df[['Brand', 'Processor']])

encoded_df = pd.DataFrame(
    encoded,
    columns=ohe.get_feature_names_out(['Brand', 'Processor'])
)

print("\nOne-Hot Encoded Data:\n")
print(encoded_df)


# Step 4: Combine Everything

final_df = pd.concat([df, encoded_df], axis=1)

print("\nFinal Combined Dataset:\n")
print(final_df)
