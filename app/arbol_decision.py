import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.preprocessing import StandardScaler

#Obtener datos del dataset
pacientes = pd.read_csv("app\data\Dataset-Depresion.csv")
#pacientes = np.array(pacientes)

#Variables predictoras
X = pacientes.iloc[:,1:24]
#Variable a predecir
Y = pacientes.iloc[:,25]

#X_train y Y_train para entrenamiento
#Y_test y Y_test para prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.75, random_state=42)

#Llamamos al constructos del arbol de decision
arbol = DecisionTreeClassifier(max_depth=4)#max_depth es la maxima cantidad de ramificiaciones que se quieren ver al generar la grafica del arbol

#Entrenamos el modelo
arbol_enfermedad = arbol.fit(X_train, Y_train)

tree.plot_tree(arbol_enfermedad, feature_names=list(X.columns.values),
               class_names=list(Y.values), filled=True)

#Predict the response for test dataset
Y_pred = arbol_enfermedad.predict(X_test)

#Creación de la matriz de confusión
from sklearn.metrics import confusion_matrix

Matriz_de_confusion = confusion_matrix(Y_test, Y_pred)


#Estandarizar los datos
#Calculamos la precisión
sc = StandardScaler()
sc.fit(X_train)

X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Ajuste del modelo
arbol.fit(X_train_std, Y_train)

# Precision global de clasificación corecta
print('Train Accuracy : %.5f' % arbol.score(X_train_std, Y_train))
print('Test Accuracy : %.5f' % arbol.score(X_test_std, Y_test))