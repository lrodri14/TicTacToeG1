document.addEventListener("DOMContentLoaded", function () {
    // Datos proporcionados
    const data = [
        ["elsyamaya", 1200, 5, 3, 2],
        ["usuario2", 1000, 5, 3, 2],
        ["usuario3", 1000, 5, 3, 2],
        ["usuario4", 1000, 5, 3, 2],
        ["usuario5", 1000, 5, 3, 2],
        ["usuario6", 1000, 5, 3, 2],
        ["usuario7", 1000, 5, 3, 2],
        ["usuario8", 1000, 5, 3, 2],
        ["usuario9", 1000, 5, 3, 2],
        ["usuario10", 1000, 5, 3, 2],
        ["usuario11", 1000, 5, 3, 2],
        ["usuario12", 1000, 5, 3, 2],
        // ... (más datos)
    ];

    // Obtener el cuerpo de la tabla
    const tableBody = document.getElementById("table-body");

    // Llenar la tabla con los datos y alternar colores de fondo
    data.forEach((row, index) => {
        const [user, points, won, lost, tied] = row;

        const tableRow = document.createElement("tr");
        tableRow.innerHTML = `
            <td class="medal-cell">${index < 3 ? `<img src="../img/medalla_${index + 1}.svg" alt="Medalla ${index + 1}" width="20">` : index + 1}</td>
            <td>${user}</td>
            <td>${points}</td>
            <td>${won} - ${lost} - ${tied}</td>
        `;

        // Alternar colores de fondo
        tableRow.style.backgroundColor = index % 2 === 0 ? '#EFEFEF' : 'white';

        tableBody.appendChild(tableRow);
    });

    // Datos para el gráfico de pastel
    const personalData = [5, 3, 2];

    // Crear elemento canvas para el gráfico de pastel
    const tabContentC2 = document.getElementById("c2");
    const personalChartCanvas = document.createElement("canvas");
    personalChartCanvas.id = "personalChart";

    // Agregar el canvas al contenedor de la pestaña "Personales"
    tabContentC2.appendChild(personalChartCanvas);

    // Obtener el contexto 2D del canvas
    const personalChartCanvasContext = personalChartCanvas.getContext("2d");

    // Función para crear el gráfico de pastel con animación
    function createPersonalChart() {
        return new Chart(personalChartCanvasContext, {
            type: 'pie',
            data: {
                labels: ['Ganadas', 'Perdidas', 'Empatadas'],
                datasets: [{
                    data: personalData,
                    backgroundColor: ['#9DDF2C', '#DC4C22', '#0081C6'],
                    borderWidth: 1,
                }],
            },
            options: {
                legend: {
                    display: true,
                    position: 'bottom',
                    labels: {
                        font: {
                            family: 'Fredoka',
                        },
                    },
                },
                animation: {
                    animateRotate: true,
                    animateScale: true,
                },
            },
        });
    }
    

    // Crear el gráfico de pastel
    let personalChart = createPersonalChart();

    // Manejar el cambio de pestaña
    const tabInputs = document.querySelectorAll('.tab-input');
    const tabContentContainer = document.querySelector('.tab-content-container');

    tabInputs.forEach(tabInput => {
        tabInput.addEventListener('change', () => {
            // Restablecer la posición de desplazamiento al top en ambas pestañas
            tabContentContainer.scrollTop = 0;
            // Agregar o quitar la clase de desbordamiento según la pestaña seleccionada
            if (tabInput.id === 'tab1') {
                tabContentContainer.classList.remove('overflow-hidden');
            } else {
                tabContentContainer.classList.add('overflow-hidden');
            }

            // Destruir el gráfico existente
            personalChart.destroy();

            // Crear y mostrar el nuevo gráfico al cambiar a la pestaña "Personales"
            if (tabInput.id === 'tab2') {
                personalChart = createPersonalChart();
            }
        });
    });

});
