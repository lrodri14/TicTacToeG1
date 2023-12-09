$(window).on('load', ()=>{
    const innerText = document.querySelector('.progress-bar > .porcentaje-llenado').innerText
    let barra = $('.progress-bar > .barra-llenado')[0];
    barra.style.setProperty('--width',  0);
    let intervalID = setInterval(() => {
        let progreso = parseFloat(getComputedStyle(barra).getPropertyValue('--width'));
        if(progreso < 100){
            barra.style.setProperty('--width',  progreso + 1);
            document.querySelector('.progress-bar > .porcentaje-llenado').innerText = innerText + "..."+(progreso + 1) + "%";
        }else{
            clearInterval(intervalID);
        }
    }, 20);
});
