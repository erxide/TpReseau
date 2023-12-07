5-12-2023 10:54 
URL : https://bakerstreet.fun

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baker Street</title>
    <link rel="stylesheet" href="./assets/commingsoon.css">
    <link rel="icon" href="./assets/logo.png" type="image/x-icon">
</head>
<body>
    <div id="logo-container">
        <img id="logo" src="./assets/logo2.png" alt="Logo">
    </div>

    <div id="content">
        <div id="coming-soon">Coming Soon</div>
        <div id="loading-dots"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const loadingDots = document.getElementById('loading-dots');
            
            function animateDots() {
                loadingDots.innerHTML = '';
                
                for (let i = 0; i < 3; i++) {
                    setTimeout(() => {
                        loadingDots.innerHTML += '.';
                    }, i * 500);
                }

                
                setTimeout(() => {
                    loadingDots.innerHTML = '';
                    animateDots();  
                }, 2000);
            }

            setTimeout(() => {
                animateDots();
            }, 1000);
        });
    </script>
</body>
</html>
