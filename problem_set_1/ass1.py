import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from src import functions


def main():
    data = pd.read_csv("customers.csv")

    # Cleaning Dataset to keep only active loyal members
    data_sorted = data[data['Churn'] == 'Yes'].reset_index()
    data_sorted.drop(columns="customerID", inplace=True)  # usless data

    '''
    Description of the dataset.
    In order to be able to work with our dataset, we must know its contents, size, columns, columns type and so on...
    '''
    functions.describe_dataset(data_sorted)

    '''
    We see that total charges is an object but it should be a float, so we check the min to spot empty value. 
    Then if every value is defined we can convert the column to float
    '''
    print("Total charges min: ", data_sorted["TotalCharges"].min())
    data_sorted["TotalCharges"] = data_sorted["TotalCharges"].astype("float64")
    print(data_sorted["SeniorCitizen"].head(10))  # Binary values => object
    data_sorted["SeniorCitizen"] = data_sorted["SeniorCitizen"].astype("object")

    '''
    Mean charges are more relevant than monthly charges.
    So we create a new column which is the mean of the TotalCharges column
    '''
    data_sorted["MeanMonthlyCharges"] = data_sorted["TotalCharges"]/data_sorted["tenure"]
    functions.describe_dataset(data_sorted)

    '''
    Plot every object vs Mean charges.
    The mean charges is very interesting because if is the main source of revenue for the firm.
    So we plot for every obeject column the mean and ???std or quantile + median??? of the tnure for every choice.
    '''
    functions.plot_float_vs_objects(data_sorted, "MeanMonthlyCharges")

    '''
    Distribution analysis.
    Now we do the same as the previous part but for the distribution of continous float columns.
    '''
    functions.plot_distribution(data_sorted, "tenure")
    functions.plot_distribution(data_sorted, "TotalCharges")
    functions.plot_distribution(data_sorted, "MeanMonthlyCharges")

    functions.plot_distribution_by(data_sorted, "tenure", "Contract")
    functions.plot_distribution_by(data_sorted, "MeanMonthlyCharges", "Contract")

    '''
    Convert string to int.
    In order to be able to use this data in some algorithms we need to convert the object columns into float colums.
    To de so, we replace each differant choice with an interger.
    '''
    data_toint = functions.string_to_int(data_sorted)

    '''
    Correlation analysis.
    In order to identify the most important features, we performed a correlation analysis.
    We can decuce that the correlated options could be a good choice to create pack offers.
    And also that uncorrelated ones are good candidates for classification.
    '''
    functions.plot_correlation(data_toint)


if __name__ == "__main__":
    main()
