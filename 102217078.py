import sys
import pandas as pd
import numpy as np

def read_excel(file_path, roll_number):
    try:
        data = pd.read_excel(file_path, engine='openpyxl')
        csv_file = f"{roll_number}-data.csv"
        data.to_csv(csv_file, index=False)
        return csv_file
    except FileNotFoundError:
        print("Error: Excel file not found")
        sys.exit()

def validate_input(args):
    if len(args) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit()

def topsis(data, weights, impacts):
    weights = np.array([float(w) for w in weights.split(',')])
    impacts = impacts.split(',')

    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must be '+' or '-' only.")
        sys.exit()

    print("Data before normalization:")
    print(data)

    data_normalized = data.iloc[:, 1:].apply(lambda x: x / np.sqrt((x**2).sum()), axis=0)

    print("Normalized Data:")
    print(data_normalized)

    print("Weights:", weights)
    print("Number of columns in normalized data:", data_normalized.shape[1])

    if data_normalized.shape[1] != len(weights):
        print("Error: Number of weights does not match the number of criteria columns.")
        sys.exit()

    weighted_normalized = data_normalized * weights

    ideal = pd.Series([0] * weighted_normalized.shape[1], index=weighted_normalized.columns)
    anti_ideal = pd.Series([0] * weighted_normalized.shape[1], index=weighted_normalized.columns)

    for col, impact in zip(weighted_normalized.columns, impacts):
        if impact == '+':
            ideal[col] = weighted_normalized[col].max()
            anti_ideal[col] = weighted_normalized[col].min()
        else:
            ideal[col] = weighted_normalized[col].min()
            anti_ideal[col] = weighted_normalized[col].max()

    dist_ideal = np.sqrt(((weighted_normalized - ideal) ** 2).sum(axis=1))
    dist_anti_ideal = np.sqrt(((weighted_normalized - anti_ideal) ** 2).sum(axis=1))

    score = dist_anti_ideal / (dist_anti_ideal + dist_ideal)

    data['Topsis Score'] = score
    data['Rank'] = score.rank(method='min', ascending=True)

    return data

if __name__ == "__main__":
    validate_input(sys.argv)
    input_file, weights, impacts, result_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    csv_file = read_excel(input_file, '102217078') 
    data = pd.read_csv(csv_file)
    results = topsis(data, weights, impacts)
    results.to_csv(result_file, index=False)
