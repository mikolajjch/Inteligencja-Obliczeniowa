import pandas as pd
import numpy as np

#a
df = pd.read_csv('iris_with_errors.csv')
numeric_columns = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce') #zmienia error na NaN

missing_values = df.isnull().sum()
print("Brakujące wartości w każdej kolumnie:")
print(missing_values)
print("\n\n\nStatystyki danych:")
print(df.describe())

#b
for column in numeric_columns:
    invalid_data = df[(df[column] <= 0) | (df[column] >= 15)]
    if not invalid_data.empty:
        print(f"\nNieprawidłowe dane w kolumnie {column}:")
        print(invalid_data)
        median_value = df[column].median()
        df[column] = np.where((df[column] <= 0) | (df[column] >= 15), median_value, df[column])

#c
valid_species = ['Setosa', 'Versicolor', 'Virginica']
invalid_species = df[~df['variety'].isin(valid_species)]
if not invalid_species.empty:
    print("\nNieprawidłowe gatunki:")
    print(invalid_species)

############ poprawienie danych i zapisanie do nowego pliku
#    df['variety'] = df['variety'].apply(lambda x: x if x in valid_species else 'Unknown')
#df.to_csv('iris_corrected.csv', index=False)
###########################################################