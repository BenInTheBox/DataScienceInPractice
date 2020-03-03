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

    # Describe the dataset
    functions.describe_dataset(data_sorted)

    '''
    We see that total charges is an object but it should be a float, so we check the min to spot empty value
    '''
    print("Total charges min: ", data_sorted["TotalCharges"].min())
    data_sorted["TotalCharges"] = data_sorted["TotalCharges"].astype("float64")
    print(data_sorted["SeniorCitizen"].head(10))  # Binary values => object
    data_sorted["SeniorCitizen"] = data_sorted["SeniorCitizen"].astype("object")

    '''
    Mean charges are more relevant than monthly charges
    '''
    data_sorted["MeanMonthlyCharges"] = data_sorted["TotalCharges"]/data_sorted["tenure"]
    functions.describe_dataset(data_sorted)

    '''
    Plot every object vs Mean charges
    '''
    functions.plot_float_vs_objects(data_sorted, "MeanMonthlyCharges")

    '''
    Distribution analysis
    '''
    functions.plot_distribution(data_sorted, "tenure")
    functions.plot_distribution(data_sorted, "TotalCharges")
    functions.plot_distribution(data_sorted, "MeanMonthlyCharges")

    functions.plot_distribution_by(data_sorted, "tenure", "Contract")
    functions.plot_distribution_by(data_sorted, "MeanMonthlyCharges", "Contract")
    '''
    # See the distribution of the tenure
    data_sorted['tenure'].hist(bins=15)
    plt.title("Histogram of tenure")
    plt.xlabel('tenure')
    plt.ylabel('Sum of clients')
    plt.show()

    # Binning the data per loyalty
    threshold = data_sorted['tenure'].max()
    bins = np.array([0, threshold/3, 2*threshold/3, threshold])
    group_names = ['New', 'Loyal', 'Very Loyal']
    data_sorted["Loyauty"] = pd.cut(data_sorted['tenure'], bins, labels=group_names)
    distribution = [data_sorted["Loyauty"][data_sorted["Loyauty"] == status].count() for status in group_names]
    x = np.arange(3)
    plt.bar(x, distribution)
    plt.xticks(x, group_names)
    plt.ylabel("Total number")
    plt.title("Loyauty count")
    plt.show()

    print("Loyauty distribution :\n")
    total = sum(distribution)
    for name, val in zip(group_names, distribution):
        print(name+": "+str(val*100/total)+" %%")
    print(data_sorted.head())

    # Plot Tenure vs charges
    data_sorted['MeanCharges'] = pd.to_numeric(data_sorted['TotalCharges'])/pd.to_numeric(data_sorted['tenure'])
    x = pd.to_numeric(data_sorted['tenure']).to_numpy()
    y = pd.to_numeric(data_sorted['MeanCharges']).to_numpy()
    plt.scatter(x, y)
    plt.xlabel('Tenure [Months]')
    plt.ylabel('MeanCharges[$/Month]')
    plt.title("Tenure Vs Mean Charges")
    plt.show()

    # Grouping the data by labels and gender <---> you may want to change that
    grouped = data_sorted.groupby([data_sorted["Loyauty"], 'gender'])
    gender_loyalty = grouped.size().unstack()
    gender_loyalty.plot.barh(title='Loyalty by gender')
    plt.show()
    # From this plot one can observe the distribution of clients within the loyalty classification made above

    # Getting all the services into one plot
    # Normalize the services for their binary value
    # Setting bool to int
    my_dict = {'Yes': 1, 'No': 0}
    data_sorted['PhoneService_int'] = data_sorted['PhoneService'].map(my_dict)

    grouped2 = data_sorted.groupby(data_sorted["Loyauty"])
    phone_service_norm = grouped2['PhoneService_int'].sum() / grouped2.size()
    normed_infos = pd.DataFrame(phone_service_norm, columns=['Has_PhoneService'])

    # Getting the proportion on people with internet service

    my_dict2 = {'DSL': 1, 'Fiber optic': 1, 'No': 0}
    data_sorted['InternetService_int'] = data_sorted['InternetService'].map(my_dict2)

    internet_service_norm = grouped2['InternetService_int'].sum() / grouped2.size()
    normed_infos['Has_InternetService'] = internet_service_norm

    props = {
        'title': 'Percent of clients who have different services per loyalty',
        'ylabel': 'Normalized "Yes"'
    }

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set(**props)
    ax.legend(loc='best')
    normed_infos.plot.bar(ax=ax, rot=30)
    plt.show()

    # Analyze the internet services
    data_cleaned_with_internet = data_sorted[data_sorted['InternetService'] != 'No']
    labels2 = pd.cut(data_cleaned_with_internet['tenure'], bins, labels=group_names)
    grouped3 = data_cleaned_with_internet.groupby(labels2)

    internet_services_df = normed_infos.copy()

    for x in data_sorted.columns[9:15]:
        new_col = x + '_int'
        data_cleaned_with_internet[new_col] = data_cleaned_with_internet[x].map(my_dict)

        current_norm = grouped3[new_col].sum() / grouped3.size()
        internet_services_df['Has_' + x] = current_norm

    internet_services_df.drop(columns=['Has_InternetService', 'Has_PhoneService'], inplace=True)

    props2 = {
        'title': 'Percent of clients who have different internet services per loyalty',
        'ylabel': 'Normalized "Yes"'
    }

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set(**props)
    ax.legend(loc='best')
    internet_services_df.plot.bar(ax=ax, rot=30)
    plt.show()

    # money spent per loyalty

    data_sorted['Labels'] = data_sorted["Loyauty"]
    plt.figure()
    sns.barplot(x='Labels', y='MonthlyCharges', data=data_sorted)
    sns.set(style="whitegrid")
    plt.show()

    # Do women spend more money ?

    sns.catplot(x='Labels', y='MonthlyCharges', hue='gender', data=data_sorted)
    sns.set(style="whitegrid")
    plt.show()

    # Other representation

    sns.catplot(x='Labels', y='MonthlyCharges', hue='gender', kind="bar", data=data_sorted)
    sns.set(style="whitegrid")
    plt.show()'''


if __name__ == "__main__":
    main()
