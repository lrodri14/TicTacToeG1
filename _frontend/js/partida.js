document.addEventListener('DOMContentLoaded', function () {
    // Espera a que el contenido del DOM se cargue completamente

    // Variable para rastrear el jugador actual
    var currentPlayer = 'X';

    // Obtén todas las celdas del tablero
    var cells = document.querySelectorAll('.cell');

    // Itera sobre cada celda y añade un evento de clic
    cells.forEach(function (cell) {
        cell.addEventListener('click', function () {
            // Crea un elemento de imagen
            var img = document.createElement('img');

            // Configura el ícono y alterna entre 'X' y 'O'
            if (currentPlayer === 'X') {
                img.src = '../img/x.svg';
                img.alt = 'x';
                currentPlayer = 'O'; // Cambia al siguiente jugador
            } else {
                img.src = '../img/o.svg';
                img.alt = 'o';
                currentPlayer = 'X'; // Cambia al siguiente jugador
            }

            // Añade la imagen al contenido de la celda
            cell.innerHTML = '';
            cell.appendChild(img);
        });
    });
});
