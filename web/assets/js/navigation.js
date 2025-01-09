var buttons = document.querySelectorAll(".menu a");

buttons.forEach(function (button) {
    button.addEventListener("click", function (event) {
        event.preventDefault();

        document.querySelector('.menu a.selected').classList.remove('selected'); // quitamos la clase selected del boton seleccionado

        button.style.pointerEvents = "none"; // deshabilitamos el boton para que la animacion termine
        button.style.backgroundColor = "var(--secondary-color)"; // cambiamos el color de fondo del boton

        setTimeout(() => {
            var target = event.target.getAttribute("href"); // pillamos el destino del boton
            location.href = target; // redirigimos a la pagina
            button.style.pointerEvents = "auto"; // habilitamos los eventos del boton por si el usuario vuelve atras
        }, 400);
})});