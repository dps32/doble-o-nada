const buttons = document.querySelectorAll(".menu a");
const menu = document.querySelector(".menu");
const menuBtn = document.querySelector(".menu-button");

buttons.forEach(function (button) {
    button.addEventListener("click", function (event) {
        event.preventDefault();

        document.querySelector('.menu a.selected').classList.remove('selected'); // quitamos la clase selected del boton seleccionado

        menu.style.pointerEvents = "none"; // deshabilitamos el boton para que la animacion termine
        button.style.backgroundColor = "var(--secondary-color)"; // cambiamos el color de fondo del boton

        setTimeout(() => {
            var target = event.target.getAttribute("href"); // pillamos el destino del boton
            location.href = target; // redirigimos a la pagina
            menu.style.pointerEvents = "auto"; // habilitamos los eventos del boton por si el usuario vuelve atras
        }, 400);
})});

menuBtn.addEventListener("click", function () {
    menu.classList.toggle("open");
    document.addEventListener("click", function (event) {
        if (!menu.contains(event.target) && !menuBtn.contains(event.target)) {
            menu.classList.remove("open");
        }
    });
});