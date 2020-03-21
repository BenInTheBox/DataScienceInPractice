#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:16:40 2020

@author: Gabriel
"""

#RECONSTITUTION DU DELIRE

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import precision_score, recall_score, confusion_matrix
import scikitplot as skplt
from sklearn.model_selection import train_test_split

def result_analysis(y: np.ndarray, y_pred: np.ndarray): #Fonction Analyse de Précision, renvoi recall, précision et F-Score 
    
    Recall = recall_score(y,y_pred) #true positif/(true positif+false negatif)
    Precision = precision_score(y,y_pred) #=true positif/(true positif+false positive)
    Fscore = 2*(Precision*Recall)/(Precision+Recall) #Classique Classifier score
    return(Recall, Precision, Fscore)

def Confusion(y: np.ndarray, y_pred: np.ndarray): #Renvoie la matrice de Confusion pour notre prédiction (à utiliser que pour avoir l'image de la matrice de confusion, donc sur le meilleur classifier)
    Conf = confusion_matrix(y, y_pred)
    Confshow = skplt.metrics.plot_confusion_matrix(y, y_pred, normalize=True)


data = pd.read_csv('customers.csv')
#print(data.shape)
#print(data.dtypes)
#data.head()


# REMPLACEMENT DES DATA PAR YANNICK GENRE OUI = 1 ; NON = 0 ect... Bon Job de chinois

DataFrame=data.copy()

DataFrame.gender=DataFrame.gender.replace("Male",1)
DataFrame.gender=DataFrame.gender.replace("Female",0)

DataFrame.Partner=DataFrame.Partner.replace("Yes",1)
DataFrame.Partner=DataFrame.Partner.replace("No",0)

DataFrame.Dependents=DataFrame.Dependents.replace("Yes",1)
DataFrame.Dependents=DataFrame.Dependents.replace("No",0)

DataFrame.PhoneService=DataFrame.PhoneService.replace("Yes",1)
DataFrame.PhoneService=DataFrame.PhoneService.replace("No",0)

DataFrame.MultipleLines=DataFrame.MultipleLines.replace("Yes",2)
DataFrame.MultipleLines=DataFrame.MultipleLines.replace("No",1)
DataFrame.MultipleLines=DataFrame.MultipleLines.replace("No phone service",0)

DataFrame.InternetService=DataFrame.InternetService.replace("Fiber optic",2)
DataFrame.InternetService=DataFrame.InternetService.replace("DSL",1)
DataFrame.InternetService=DataFrame.InternetService.replace("No",0)

DataFrame.OnlineSecurity=DataFrame.OnlineSecurity.replace("Yes",2)
DataFrame.OnlineSecurity=DataFrame.OnlineSecurity.replace("No",1)
DataFrame.OnlineSecurity=DataFrame.OnlineSecurity.replace("No internet service",0)

DataFrame.OnlineBackup=DataFrame.OnlineBackup.replace("Yes",2)
DataFrame.OnlineBackup=DataFrame.OnlineBackup.replace("No",1)
DataFrame.OnlineBackup=DataFrame.OnlineBackup.replace("No internet service",0)

DataFrame.DeviceProtection=DataFrame.DeviceProtection.replace("Yes",2)
DataFrame.DeviceProtection=DataFrame.DeviceProtection.replace("No",1)
DataFrame.DeviceProtection=DataFrame.DeviceProtection.replace("No internet service",0)

DataFrame.TechSupport=DataFrame.TechSupport.replace("Yes",2)
DataFrame.TechSupport=DataFrame.TechSupport.replace("No",1)
DataFrame.TechSupport=DataFrame.TechSupport.replace("No internet service",0)

DataFrame.StreamingTV=DataFrame.StreamingTV.replace("Yes",2)
DataFrame.StreamingTV=DataFrame.StreamingTV.replace("No",1)
DataFrame.StreamingTV=DataFrame.StreamingTV.replace("No internet service",0)

DataFrame.StreamingMovies=DataFrame.StreamingMovies.replace("Yes",2)
DataFrame.StreamingMovies=DataFrame.StreamingMovies.replace("No",1)
DataFrame.StreamingMovies=DataFrame.StreamingMovies.replace("No internet service",0)

DataFrame.Contract=DataFrame.Contract.replace("Two year",24)
DataFrame.Contract=DataFrame.Contract.replace("One year",12)
DataFrame.Contract=DataFrame.Contract.replace("Month-to-month",1)

DataFrame.PaperlessBilling=DataFrame.PaperlessBilling.replace("Yes",1)
DataFrame.PaperlessBilling=DataFrame.PaperlessBilling.replace("No",0)

DataFrame.PaymentMethod=DataFrame.PaymentMethod.replace("Electronic check",3)
DataFrame.PaymentMethod=DataFrame.PaymentMethod.replace("Mailed check",2)
DataFrame.PaymentMethod=DataFrame.PaymentMethod.replace("Bank transfer (automatic)",1)
DataFrame.PaymentMethod=DataFrame.PaymentMethod.replace("Credit card (automatic)",0)

DataFrame.TotalCharges=DataFrame.Contract*DataFrame.MonthlyCharges

DataFrame.Churn=DataFrame.Churn.replace("Yes",1)
DataFrame.Churn=DataFrame.Churn.replace("No",0)

DataFrame.head()

#INDICATION DU TYPE SI JAMAIS YA UN DOUTE
#print(DataFrame.dtypes)   

#RÉPARTITION STATISTIQUES DE CE QU'on a 
for col in DataFrame.columns:
    print(DataFrame[col].value_counts(normalize=True))

#CELLE QUI NOUS INTERESSE PAS MAL
#print(DataFrame['Churn'].value_counts(normalize=True))

y=DataFrame.Churn.copy()
y.head()

df_comp = DataFrame.drop(columns="customerID")
df=DataFrame.drop(columns="customerID" and "Churn")
df.head()

# LOYAUX OU NON, SÉPARATION DES DATAFRAMES
data_loyal = df_comp[df_comp['Churn'] == 1].reset_index()
data_churn = df_comp[df_comp['Churn'] == 0].reset_index()

#Définition RATIO d'entrainement et Définition des SETS ? Je suppose

(data_loyal_train, data_loyal_test) = train_test_split(data_loyal,test_size = 0.8)
(data_churn_train, data_churn_test) = train_test_split(data_churn, test_size = 0.8)

per_train = 0.8
n_row_loyal = data_loyal.shape[0]
n_row_churn = data_churn.shape[0]

row_loyal = round(per_train*n_row_loyal)
row_churn = round(per_train*n_row_churn)

print(row_loyal)
print(row_churn)
#print(data_churn.shape)
#print(data_loyal.shape)

#il y a bcp plus de churn ici !!!!!!juste
#Ouais mais tant que le ratio de base est vérifié cest tt bon je pense non ? 73% de Non churn environ

#j'arrive pas  à selectionner les lignes que je veux veux. je crois que c'est pas concideré comme un tableau 

#train_loyal = data_loyal[:,:row_loyal]
#test_loyal = data_loyal[:,(n_row_loyal-row_loyal):]

#train_churn = data_churn[:,:row_churn]
#test_churn = data_churn[:,(n_row_churn-row_churn):]

#np.random.shuffle(train_loyal)
#np.random.shuffle(test_loyal)

#np.random.shuffle(train_churn)
#np.random.shuffle(test_churn)
"""
x_train_loyal = train_loyal.drop(columns="Churn")
x_train_loyal.head()
x_test_loyal = test_loyal.drop(columns="Churn")
x_test_loyal.head()

x_train_churn = train_churn.drop(columns="Churn")
x_train_churn.head()
x_test_churn = test_churn.drop(columns="Churn")
x_test_churn.head()



y_train_loyal = train_loyal.Churn.copy()
y_train_loyal.head()
y_test_loyal = test_loyal.Churn.copy()
y_test_loyal.head()

y_train_churn = train_churn.Churn.copy()
y_train_churn.head()
y_test_churn = test_churn.Churn.copy()
y_test_churn.head()

"""





