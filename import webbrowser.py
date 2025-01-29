<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nosso Amor</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background: #ffebee;
            overflow: hidden;
            position: relative;
        }

        .hearts {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        .hearts span {
            position: absolute;
            display: block;
            width: 20px;
            height: 20px;
            background: #ff4d4d;
            clip-path: polygon(50% 0%, 100% 38%, 82% 100%, 50% 75%, 18% 100%, 0% 38%);
            animation: animate 10s linear infinite;
            bottom: -150px;
        }

        .hearts span:nth-child(1) {
            left: 25%;
            animation-delay: 0s;
        }

        .hearts span:nth-child(2) {
            left: 10%;
            animation-delay: 2s;
        }

        .hearts span:nth-child(3) {
            left: 70%;
            animation-delay: 4s;
        }

        .hearts span:nth-child(4) {
            left: 50%;
            animation-delay: 6s;
        }

        .hearts span:nth-child(5) {
            left: 85%;
            animation-delay: 8s;
        }

        @keyframes animate {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translateY(-1000px) rotate(720deg);
                opacity: 0;
            }
        }

        .container {
            position: relative;
            z-index: 1;
            text-align: center;
            color: #ff4d4d;
            padding-top: 50px;
        }

        .counter {
            font-size: 3em;
            margin-bottom: 20px;
        }

        .images {
            margin-top: 20px;
        }

        .images img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 10px;
            border: 5px solid #ff4d4d;
        }

        .quotes {
            margin-top: 20px;
            font-size: 1.5em;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="hearts">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </div>

    <div class="container">
        <div class="counter">
            <span id="days">00</span> Dias <span id="hours">00</span> Horas <span id="minutes">00</span> Minutos <span id="seconds">00</span> Segundos
        </div>

        <div class="images">
            <img src="sua-foto1.jpg" alt="Foto 1">
            <img src="sua-foto2.jpg" alt="Foto 2">
        </div>

        <div class="quotes">
            <p>"Eu te amo mais que tudo nesse mundo!"</p>
            <p>"Você é a razão do meu sorriso."</p>
        </div>
    </div>

    <script>
        const startDate = new Date("2023-01-01"); // Coloque a data que começaram a namorar

        function updateCounter() {
            const now = new Date();
            const diff = now - startDate;

            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((diff % (1000 * 60)) / 1000);

            document.getElementById('days').innerText = days;
            document.getElementById('hours').innerText = hours;
            document.getElementById('minutes').innerText = minutes;
            document.getElementById('seconds').innerText = seconds;
        }

        setInterval(updateCounter, 1000);
        updateCounter();
    </script>
</body>
</html>