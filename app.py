import pandas as pd
import os
def load_and_analyze_data():
	file_path='data.csv'
	
if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please provide a valid CSV file.")
        return

    print("--- 1. Loading CSV File ---")
    df = pd.read_csv(file_path)
    print(f"Successfully loaded {df.shape[0]} rows and {df.shape[1]} columns.\n")

    print("--- 2. First 5 Rows of Data ---")
    print(df.head(), "\n")

    print("--- 3. Data Summary & Statistics ---")
    print(df.describe(), "\n")

    print("--- 4. Missing Values Check ---")
    print(df.isnull().sum(), "\n")

    print("Data processing completed successfully!")

if __name__ == "__main__":
    load_and_analyze_data()
