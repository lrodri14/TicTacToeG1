const pk = document.querySelector('#pk')
const username = document.querySelector('#username')
const jugador_actual_username = document.querySelector('#jugador_actual_username')
let currentPlayer = 'X';
const cells = document.querySelectorAll('.cell');

document.addEventListener('DOMContentLoaded', function () {
    // Espera a que el contenido del DOM se cargue completamente

    const socket = new WebSocket('wss://www.tictactoe.sealena.com/ws/partidas/jugar/' + pk.textContent);

    socket.onopen = function (event) {
        console.log('WebSocket connection opened:', event);
    };

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        switch(data.tipo){
            case 'gane':
                window.location.pathname = '/partidas/gane/' + pk.textContent
                break
            case 'empate':
                window.location.pathname = '/partidas/empate/' + pk.textContent
            default:
                currentPlayer = data.jugador_actual
                jugador_actual_username.textContent = data.jugador_actual_username
                for (let i = 0; i <= cells.length; i++){
                    const marcador_x = cells[i].querySelector('.x')
                    const marcador_0 = cells[i].querySelector('.o')
                    if (data.tabla[i] === 'X'){
                        marcador_x.classList.remove('hidden')
                        marcador_0.classList.add('hidden')
                    }else if (data.tabla[i] === '0'){
                        marcador_0.classList.remove('hidden')
                        marcador_x.classList.add('hidden')
                    }else{
                        marcador_0.classList.add('hidden')
                        marcador_x.classList.add('hidden')
                    }
                }
        }
    };

    socket.onclose = function (event) {
        console.log('WebSocket connection closed:', event);
    };

    // Itera sobre cada celda y añade un evento de clic
    cells.forEach(function (cell) {
        cell.addEventListener('click', function (e) {
            // Configura el ícono y alterna entre 'X' y 'O'
            if (jugador_actual_username.textContent === username.textContent){
                if (currentPlayer === 'X') {
                    let marcador = e.target.querySelector('.x')
                    let marcadorPrevio = e.target.querySelector('.o')
                    marcadorPrevio.classList.add('hidden')
                    marcador.classList.remove('hidden')
                    socket.send(JSON.stringify({marcador: 'X', posicion: e.target.id}))
                } else {
                    let marcador = e.target.querySelector('.o')
                    let marcadorPrevio = e.target.querySelector('.x')
                    marcadorPrevio.classList.add('hidden')
                    marcador.classList.remove('hidden')
                    socket.send(JSON.stringify({marcador: '0', posicion: e.target.id}))
                }
            }
        });
    });
});
