import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def describe_dataset(data_set: pd.DataFrame):
    '''Prints dataset properties'''
    print(data_set.head())
    print("DataFrame' shape: ", data_set.shape)
    print("Datasset types: \n", data_set.dtypes)
    print("Object description: \n", data_set.describe(include=['O']))
    print("Numerical description: \n", data_set.describe())


def plot_float_vs_objects(data_set: pd.DataFrame, ref_column: str):
    '''Plots ref_column compared to every Object column'''
    for col in data_set.columns:
        if data_set[col].dtype == "O":
            sns.catplot(x=col, y=ref_column, data=data_set, kind="bar", palette="deep")
            plt.show()


def plot_distribution(data_set: pd.DataFrame, ref_column: str):
    '''Plots numercial data distribution as an histogram'''
    plt.figure(figsize=(10, 5))
    plt.title("%s'distribution" % ref_column)
    sns.distplot(data_set[ref_column])
    plt.show()


def plot_distribution_by(data_set: pd.DataFrame, ref_column: str, by_column: str):
    values_choices = data_set[by_column].unique()
    plt.figure(figsize=(10, 5))
    for i, choice in enumerate(values_choices):
        sns.distplot(data_set[data_set[by_column] == choice][ref_column],color=sns.color_palette("Pastel2")[i], label=choice)
    plt.legend()
    plt.title("%s's distribution depending of %s" % (ref_column, by_column))
    plt.xlabel(ref_column)
    plt.show()
