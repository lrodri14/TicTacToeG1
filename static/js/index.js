$(window).on('load', ()=>{
    let barra = $('.progress-bar > .barra-llenado')[0];
    barra.style.setProperty('--width',  0);
    let intervalID = setInterval(() => {
        let progreso = parseFloat(getComputedStyle(barra).getPropertyValue('--width'));
        if(progreso < 100){
            barra.style.setProperty('--width',  progreso + 1);
            document.querySelector('.progress-bar > .porcentaje-llenado').innerText = "Cargando..."+(progreso + 1) + "%";
        }else{
            clearInterval(intervalID);
            window.location.href = window.location.origin + '/home'
        }
    }, 20); //Intervalo de repeticion en milesima de segundo
});
