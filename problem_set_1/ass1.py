import pandas as pd

def main():
    data = pd.read_csv("customers.csv")
    print(data.head())
    print(data.columns)

if __name__ == "__main__":
    main()