import pandas as pd


def main():
    data = pd.read_csv("customers.csv")
    print(data.head())
    print(data.columns)

    # Takes only staying consumers
    churn = data[data["Churn"] == "No"]
    print(churn.head())
    print("Ta mere")

if __name__ == "__main__":
    main()
