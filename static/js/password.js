function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var showPasswordIcon = document.querySelector(".show-password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showPasswordIcon.src = "../img/ocultarPass.svg";
    } else {
        passwordInput.type = "password";
        showPasswordIcon.src = "../img/mostrarPass.svg";
    }
}


function togglePasswordVisibility2() {
    var passwordInput = document.getElementById("confirmarContrasena");
    var showPasswordIcon = document.querySelector(".show-password2");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showPasswordIcon.src = "../img/ocultarPass.svg";
    } else {
        passwordInput.type = "password";
        showPasswordIcon.src = "../img/mostrarPass.svg";
    }
}
