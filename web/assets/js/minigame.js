const playTable = document.querySelector(".game-wrapper");
const message = document.querySelector(".message");
const restartButton = document.querySelector(".restart");

// jugador
const playerGame = document.querySelector(".player.game");
const hitButton = playerGame.querySelector(".hit");
const standButton = playerGame.querySelector(".stand");
const playerCounter = playerGame.querySelector(".counter");
const playerCardHistory = playerGame.querySelector(".card-history");

// bot
const botGame = document.querySelector(".bot.game");
const botCounter = botGame.querySelector(".counter");
const botCardHistory = botGame.querySelector(".card-history");

const cards = [
    { url: "assets/img/cards/a.png", value: 1 },
    { url: "assets/img/cards/2.png", value: 2 },
    { url: "assets/img/cards/3.png", value: 3 },
    { url: "assets/img/cards/4.png", value: 4 },
    { url: "assets/img/cards/5.png", value: 5 },
    { url: "assets/img/cards/6.png", value: 6 },
    { url: "assets/img/cards/7.png", value: 7 },
    { url: "assets/img/cards/8.png", value: 0.5 },
    { url: "assets/img/cards/9.png", value: 0.5 },
    { url: "assets/img/cards/10.png", value: 0.5 },
    { url: "assets/img/cards/j.png", value: 0.5 },
    { url: "assets/img/cards/q.png", value: 0.5 },
    { url: "assets/img/cards/k.png", value: 0.5 }
];

hitButton.addEventListener("click", () => {
    playerPulse(); // animacion para indicar que es el turno del jugador
    disableButtons(); // deshabilitamos botones para que no pueda pedir otra carta mientras aparece

    // seleccionar carta aleatoria
    const randomCard = cards[Math.floor(Math.random() * cards.length)];

    // valor e imagen de la carta
    const cardValue = randomCard.value;
    const cardImage = randomCard.url;

    // crear la imagen y ponerla en el historial de cartas
    const cardElement = document.createElement("img");
    cardElement.src = cardImage;
    cardElement.style.zIndex = playerCardHistory.children.length;
    playerCardHistory.appendChild(cardElement);

    // actualizar el valor del contador
    setTimeout(() => {
        playerCounter.innerHTML = (parseFloat(playerCounter.innerHTML) + cardValue).toFixed(1);
        enableButtons();
        checkPlayerOverflow();
    }, 700);
});

restartButton.addEventListener("click", () => {
    resetGame();
});

standButton.addEventListener("click", () => {
    disableButtons();
    startBot();
});

// deshabilitar botones
function disableButtons() {
    hitButton.disabled = true;
    standButton.disabled = true;
}

// habilitar botones
function enableButtons() {
    hitButton.disabled = false;
    standButton.disabled = false;
}

function checkPlayerOverflow() {
    const playerResult = parseFloat(playerCounter.innerHTML);

    if (playerResult > 7.5){ // si el jugador se pasa de 7.5 pierde
        playerCounter.style.color = "#ff3232";
        botCounter.style.color = "#32ff32";
        endGame();
    } else if (playerResult === 7.5){ // si el jugador llega a 7.5 se planta para que juegue el bot
        disableButtons();
        startBot();
    }
}

// comprobar quien gana
function checkWinner() {
    const playerResult = parseFloat(playerCounter.innerHTML);
    const botResult = parseFloat(botCounter.innerHTML);

    // gana el bot
    if (botResult >= playerResult && botResult <= 7.5) {
        playerCounter.style.color = "#ff3232";
        botCounter.style.color = "#32ff32";
        endGame();
        return;
    }

    // gana el jugador
    else {
        playerCounter.style.color = "#32ff32";
        botCounter.style.color = "#ff3232";
        endGame(true);
        return;
    }
}

// Iniciar el bot
async function startBot() {
    botPulse(); // animacion para indicar que es el turno del bot
    let botResult = 0;

    // mientras el bot tenga menos puntos que el jugador
    while (botResult < parseFloat(playerCounter.innerHTML)) {
        // tiempo entre 800ms - 2s
        const timeout = Math.floor(Math.random() * 1200) + 800;

        // esperar para simular que el bot está pensando

        const randomCard = cards[Math.floor(Math.random() * cards.length)];
        const cardValue = randomCard.value;
        const cardImage = randomCard.url;

        const cardElement = document.createElement("img");
        cardElement.src = cardImage;
        cardElement.style.zIndex = botCardHistory.children.length;
        botCardHistory.appendChild(cardElement);

        botResult = parseFloat(botCounter.innerHTML) + cardValue;

        // https://www.geeksforgeeks.org/how-to-delay-a-javascript-function-call-using-javascript/
        await new Promise(resolve => {
            setTimeout(() => {
                botCounter.innerHTML = botResult.toFixed(1);
                resolve();
            }, 1000);
        });
    }

    checkWinner();
}

function playerPulse() {
    playerGame.classList.add("pulse");
    botGame.classList.remove("pulse");
}

function botPulse() {
    botGame.classList.add("pulse");
    playerGame.classList.remove("pulse");
}

function removePulse() {
    botGame.classList.remove("pulse");
    playerGame.classList.remove("pulse");
}

function resetGame() {
    playerCounter.innerHTML = "0";
    playerCounter.style.color = "";
    botCounter.innerHTML = "0";
    botCounter.style.color = "";
    playerCardHistory.innerHTML = "<div class='placeholder'></div>";
    botCardHistory.innerHTML = "<div class='placeholder'></div>";
    message.classList.remove("active");
    enableButtons();
    removePulse();
}

function showMessage(text, color) {
    const span = message.querySelector("span");
    span.innerHTML = text;
    span.style.color = color;
    message.classList.add("active");
}

function endGame(won = false) {
    disableButtons();
    removePulse();
    if (won){
        var colors = ["#0016bb", "#ffffff"];
        setTimeout(() => {
            showMessage("¡Has ganado!", "#7c8cff");
        }, 1000);
    }
    else{
        var colors = ["#bb0000", "#ffffff"];
        setTimeout(() => {
            showMessage("¡Has perdido!", "#ff5959");
        }, 1000);
    }
    

    const ld = playTable.getBoundingClientRect();
        var lx = ld.x; 
        var ly = ld.y + ld.height - 50;

        var rx = lx + ld.width;
        var ry = ly;

        // Convertir coordenadas absolutas a proporciones relativas al tamaño de la ventana
        lx = lx / window.innerWidth;
        ly = ly / window.innerHeight;

        rx = rx / window.innerWidth;
        ry = ry / window.innerHeight;
        // esquina inferior izquierda del elemento
        for (let i = 0; i < 20; i++) {
            setTimeout(() => {
                confetti({
                    particleCount: 10,
                    angle: 60,
                    spread: 55,
                    origin: { x: lx, y: ly },
                    colors: colors,
                });
                confetti({
                    particleCount: 10,
                    angle: 120,
                    spread: 55,
                    origin: { x: rx, y: ry },
                    colors: colors,
                });
            }, i * 50);
        }
}

// // temporal al presionar el boton ctrl se llama a endGame(true)
// document.addEventListener("keydown", (event) => {
//     if (event.ctrlKey)
//         endGame(true);
// });