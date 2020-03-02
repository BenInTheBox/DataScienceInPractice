import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    data = pd.read_csv("customers.csv")
    print(data.head())
    print(data.columns)

    # Takes only staying consumers
    churn = data[data["Churn"] == "No"]
    print(churn.head())

    print("bibaboum ou")

    # Cleaning Dataset to keep only active loyal members
    data_sorted = data[data['Churn'] == 'Yes']
    print(data_sorted.head())

    # See teh distribution of the tenure
    data_sorted['tenure'].hist(bins=15)
    plt.title("Histogram of tenure")
    plt.xlabel('tenure')
    plt.ylabel('Sum of clients')
    plt.show()

    # Binning the data per loyalty
    bins = np.array([0, 10, 45, data_sorted['tenure'].max()])
    group_names = ['New', 'Loyal', 'Very Loyal']
    labels = pd.cut(data_sorted['tenure'], bins, labels=group_names)

    # Grouping the data by labels and gender <---> you may want to change that
    grouped = data_sorted.groupby([labels, 'gender'])
    gender_loyalty = grouped.size().unstack()

    gender_loyalty.plot.barh(title='Loyalty by gender')
    plt.show()
    # From this plot one can observe the distribution of clients within the loyalty classification made above

    # Getting all the services into one plot
    # Normalize the services for their binary value
    # Setting bool to int
    my_dict = {'Yes': 1, 'No': 0}
    data_sorted['PhoneService_int'] = data_sorted['PhoneService'].map(my_dict)

    grouped2 = data_sorted.groupby(labels)
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

    data_sorted['Labels'] = labels
    plt.figure()
    sns.barplot(x='Labels', y='MonthlyCharges', data=data_sorted)
    sns.set(style="whitegrid")
    plt.show()

    # Do women spend more money ?

    plt.figure()
    sns.catplot(x='Labels', y='MonthlyCharges', hue='gender', data=data_sorted)
    sns.set(style="whitegrid")
    plt.show()

    # Other representation

    plt.figure()
    sns.catplot(x='Labels', y='MonthlyCharges', hue='gender', kind="bar", data=data_cleaned)
    sns.set(style="whitegrid")
    plt.show()


if __name__ == "__main__":
    main()
