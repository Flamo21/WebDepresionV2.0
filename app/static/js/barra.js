// Obtener el elemento de la barra
var barra = document.getElementById("barra");

// Función para actualizar la barra y el color
function actualizarBarra(probability) {
  var color;

  // Establecer el color en base a la probabilidad
  if (probability = "Depresión minima") {
    color = "green";
  } else if (probability = "Depresion moderada") {
    color = "orange";
  } else {
    color = "red";
  }

  // Actualizar el ancho de la barra y el color
  //barra.style.width = (probability * 100) + "%";
  //barra.style.backgroundColor = color;
}

// Ejemplo de uso (suponiendo que 'probability' contiene la probabilidad)
var probability = prediction; // Ejemplo
actualizarBarra(probability);