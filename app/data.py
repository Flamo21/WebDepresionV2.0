import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.preprocessing import StandardScaler
import warnings
import pickle
warnings.filterwarnings("ignore")

#Obtener datos del dataset
pacientes = pd.read_csv("app\data\Dataset-Depresion.csv")
#Variables predictoras
X = pacientes.iloc[:,0:22]
#Variable a predecir
Y = pacientes.iloc[:,24]


#X_train y Y_train para entrenamiento
#Y_test y Y_test para prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.75, random_state=42)

arbol = DecisionTreeClassifier(max_depth=4)#max_depth es la maxima cantidad de ramificiaciones que se quieren ver al generar la grafica del arbol

arbol_enfermedad = arbol.fit(X_train, Y_train)
#log_reg.fit(X_train, y_train)

inputt=[int(x) for x in "1 1 1 2 1 1 1 1 1 0 3 1 2 2 3 3 2 1 1 2 1 1".split(' ')]
final=[np.array(inputt)]

b = arbol.predict_proba(final)

pickle.dump(arbol,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

print(b)