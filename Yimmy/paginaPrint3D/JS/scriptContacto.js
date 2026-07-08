function esEmailValido(email) {
    let regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
    }

document.getElementById('contact-form').addEventListener('submit', function(event) {

    let errores = [];
    let nombre = document.getElementById('name').value.trim();
    let email = document.getElementById('email').value.trim();

    if (nombre === '') {
        errores.push('Que? no tienes nombre?');
        }
    if (email === '') {
        errores.push('Pon tu correo pequeño Billy');
        }   else if (!esEmailValido(email)) {
        errores.push('El formato del email es incorrecto.');
    }
    if (errores.length > 0) {
        event.preventDefault();
        document.getElementById('errores').innerHTML = errores.join('<br>');
        }
    else {
    document.getElementById('errores').innerHTML = '';}
        });