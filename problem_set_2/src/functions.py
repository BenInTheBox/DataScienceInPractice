import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def describe_dataset(data_set: pd.DataFrame):
    '''
    Prints dataset properties
    '''
    print(data_set.head())
    print("DataFrame' shape: ", data_set.shape)  # Shape
    print("Datasset types: \n", data_set.dtypes)  # Columns type
    print("Object description: \n", data_set.describe(include=['O']))  # Description of object columns
    print("Numerical description: \n", data_set.describe())  # Description of float columns


def plot_float_vs_objects(data_set: pd.DataFrame, ref_column: str):
    '''Plots ref_column compared to every Object column'''
    for col in data_set.columns:  # Iter on dataset columns
        if data_set[col].dtype == "O":  # Takes only obect columns
            sns.catplot(x=col, y=ref_column, data=data_set, kind="bar",
                        palette="deep")  # Plot the columns "distribution" against the ref column
            plt.show()


def plot_distribution(data_set: pd.DataFrame, ref_column: str):
    '''Plots numercial data distribution as an histogram'''
    plt.figure(figsize=(10, 5))
    plt.title("%s'distribution" % ref_column)
    sns.distplot(data_set[ref_column])  # Plot the ref_column's distribution
    plt.show()


def plot_distribution_by(data_set: pd.DataFrame, ref_column: str, by_column: str):
    values_choices = data_set[by_column].unique()
    plt.figure(figsize=(10, 5))
    for i, choice in enumerate(values_choices):
        sns.distplot(data_set[data_set[by_column] == choice][ref_column], color=sns.color_palette("Pastel2")[i],
                     label=choice)  # Plot the superposition of the ref_column distribution for each by_column choice
    plt.legend()
    plt.title("%s's distribution depending of %s" % (ref_column, by_column))
    plt.xlabel(ref_column)
    plt.show()


def string_to_int(data_set: pd.DataFrame) -> pd.DataFrame:
    '''Convert string values into intergers'''
    uniques = [[col, data_set[col].unique()] for col in data_set.columns if data_set[
        col].dtype == "O"]  # Create a list of list containing the column name and a list columns uniques values
    for col in uniques:
        #  Repllace the string values with an int corresponding to each uniques values
        if len(col[1]) == 1:
            data_set[col[0]] = data_set[col[0]].map(lambda s: 1)
        if len(col[1]) == 2:
            data_set[col[0]] = data_set[col[0]].map(lambda s: 0 if s == col[1][0] else 1)
        if len(col[1]) == 3:
            data_set[col[0]] = data_set[col[0]].map(lambda s: 1 if s == col[1][0] else (0 if s == col[1][1] else 2))
        if len(col[1]) == 4:
            data_set[col[0]] = data_set[col[0]].map(
                lambda s: 0 if s == col[1][0] else (1 if s == col[1][1] else (2 if s == col[1][0] else 3)))
    return data_set.astype("float64")


def plot_correlation(data_set: pd.DataFrame):
    '''Plot the correlation maxtrix of the dataset columns as a color map'''
    plt.figure(figsize=(12, 6))
    corr = data_set.apply(lambda x: pd.factorize(x)[0]).corr()
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, linewidths=.2,
                cmap="YlGnBu")  # Correlation plot
    plt.show()
