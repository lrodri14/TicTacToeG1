document.addEventListener("DOMContentLoaded", function () {
    // Datos para el gráfico de pastel
    let datosPersonales = [];
    const data = document.querySelector('#c2')
    datosPersonales.push(data.getAttribute('value-ganes'))
    datosPersonales.push(data.getAttribute('value-perdidas'))
    datosPersonales.push(data.getAttribute('value-empates'))

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
                    data: datosPersonales,
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
