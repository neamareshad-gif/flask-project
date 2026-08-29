










function startVoice() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US"; // ቀጣይ እንቀይራለን

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById("input").value = text;
        send();
    };

    recognition.start();
}













































function send() {
    const text = document.getElementById("input").value;

    fetch("/api/ai", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("response").innerText =
            "AI: " + data.response + " | Tokens: " + data.tokens;

        let historyHTML = "";
        data.history.forEach(item => {
            historyHTML += `
            <p>👤 ${item.user}</p>
            <p>🤖 ${item.ai}</p>
            <hr>
            `;
        });
        document.getElementById("history").innerHTML = historyHTML;
    });
}

// chart
const ctx = document.getElementById('chart');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{ label: 'Users', data: [] }]
    }
});

function fetchData() {
    fetch("/api/live-data")
    .then(res => res.json())
    .then(data => {
        chart.data.labels.push(data.time);
        chart.data.datasets[0].data.push(data.users);

        // keep last 10 only (fix crowded issue)
        if (chart.data.labels.length > 10) {
            chart.data.labels.shift();
            chart.data.datasets[0].data.shift();
        }

        chart.update();
        document.getElementById("users").innerText = data.users;
    });
}

setInterval(fetchData, 5000);




























function startVoice() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US"; // ቀጣይ እንቀይራለን

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById("input").value = text;
        send();
    };

    recognition.start();
}


















