
function cambiarContenido() {
    let div = document.getElementById('miDiv');
    div.innerHTML = 'Contenido cambiado';
}


document.getElementById('miFormulario').addEventListener('submit', function(event) {
    let errores = [];
    let nombre = document.getElementById('nombre').value;
    let email = document.getElementById('email').value;
    let edad = document.getElementById('edad').valu

    if (nombre === '') {
        errores.push('Que? no tienes nombre?');
        }

    if (email === '') {
        errores.push('Pon tu correo pequeño Billy');
        }

    if (edad === '') {
        errores.push('El campo edad es obligatorio.');
        }

    if (errores.length > 0) {
        event.preventDefault();
        document.getElementById('errores').innerHTML = errores.join('<br>');
        }
        });


function esEmailValido(email) {
    let regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
    }
document.getElementById('miFormulario').addEventListener('submit', function(event) {

    let errores = [];
    let email = document.getElementById('email').value;

    if (!esEmailValido(email)) {
        errores.push('El formato del email es incorrecto.');
    }
    if (errores.length > 0) {
        event.preventDefault();
        document.getElementById('errores').innerHTML = errores.join('<br>');
    }
    });


function esEdadValida(edad) {
    let min = 18;
    let max = 65;
    return edad >= min && edad <= max;
    }
    document.getElementById('miFormulario').addEventListener('submit', function(event) {
    let errores = [];
    let edad = document.getElementById('edad').value;

    if (!esEdadValida(edad)) {
    errores.push('La edad debe estar entre 18 y 65 años.');
    }

    if (errores.length > 0) {
    event.preventDefault();
    document.getElementById('errores').innerHTML = errores.join('<br>');
    }
    });