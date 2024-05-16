from flask import Flask, render_template, request
import pickle
import numpy as np
import os
app = Flask(__name__, static_folder='static')



# Obtener la ruta del directorio actual del script
dir_path = os.path.dirname(os.path.abspath(__file__))
modelo_path = os.path.join(dir_path, 'model.pkl')

# Cargar el modelo
with open(modelo_path, 'rb') as file:
    model = pickle.load(file)
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    # Obtener los datos del formulario
    data = request.form.to_dict()

    input_data=[int(x) for x in request.form.values()]
    final=[np.array(input_data)]
    # Convertir los datos a un array de NumPy
    #input_array = np.array([input_data])

    # Hacer la predicción
    prediction = model.predict(final)
    probability = model.predict_proba(final)[:, 1]  # Probabilidad de que sea positivo
    probability = np.array([probability])
    # Condición para determinar si hay depresión mínima
    if prediction == "Depresión minima":
        result = "Este resultado no es Clínico, sin embargo no presenta síntomas de depresión."
    elif prediction == "Depresión leve":
        result = "La probabilidad de tener DEPRESIÓN es Mínima, se recomienda acceder a un especialista."
    elif prediction == "Depresión moderada":
        result = "La probabilidad de tener DEPRESIÓN es Moderada, se recomienda acceder a un especialista."   
    else:
        result = "La probabilidad de tener DEPRESIÓN es Alta, este resultado no es Clínico pero se recomienda acceder con prioridad alta y urgencia alta a un especialista"
    probability_porcentaje = probability * 100
    return render_template('result.html', prediction=result, probability=probability, probability_porcentaje=probability_porcentaje)

if __name__ == '__main__':
    app.run(debug=True)