// function startListening() {
//     const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
//     recognition.lang = 'en-US';
//     recognition.interimResults = false;

//     recognition.start();

//     recognition.onresult = function(event) {
//         const command = event.results[0][0].transcript;
//         document.getElementById('output').innerText = `You said: "${command}"`;
//         sendCommandToBackend(command);
//     };

//     recognition.onerror = function(event) {
//         document.getElementById('output').innerHTML = `<strong>Error occurred during speech recognition: ${event.error}</strong>`;
//         console.error('Speech recognition error:', event.error);
//     };

//     recognition.onspeechend = function() {
//         recognition.stop();
//     };

//     recognition.onend = function() {
//         console.log("Speech recognition ended");
//     };
// }

// function sendCommandToBackend(command) {
//     fetch('http://localhost:8000/analyze-symptoms/', {   // <- Correct endpoint
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify({symptom: command})   // <- Send symptom (not command) since we are diagnosing symptoms
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }
//         return response.json();
//     })
//     .then(data => {
//         document.getElementById('output').innerHTML += `<br><br><strong>Diagnosis: ${data.diagnosis}</strong>`;
//         speakText(`Based on your symptom, the diagnosis is: ${data.diagnosis}`);
//     })
//     .catch(error => {
//         document.getElementById('output').innerHTML += `<br><br><strong>Error contacting Health Assistant.</strong>`;
//         console.error('Backend error:', error);
//     });
// }

// function speakText(text) {
//     const utterance = new SpeechSynthesisUtterance(text);
//     utterance.lang = 'en-US';
//     speechSynthesis.speak(utterance);
// }
 


//-------------------------------------------------


function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;

    recognition.start();

    recognition.onresult = function(event) {
        const command = event.results[0][0].transcript;
        document.getElementById('output').innerText = `You said: "${command}"`;
        sendCommandToBackend(command);
    };

    recognition.onerror = function(event) {
        document.getElementById('output').innerHTML = `<strong>Error occurred during speech recognition: ${event.error}</strong>`;
        console.error('Speech recognition error:', event.error);
    };

    recognition.onspeechend = function() {
        recognition.stop();
    };

    recognition.onend = function() {
        console.log("Speech recognition ended");
    };
}

function sendCommandToBackend(command) {
    fetch('https://smart-health-ai.onrender.com/api/process', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({symptom: command})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        let diagnosisText = '';
        let remediesText = '';

        if (data.diagnosis && data.diagnosis.length > 0) {
            diagnosisText = '<strong>Diagnosis:</strong><br>' + data.diagnosis.join('<br>');
            speakText(`Based on your symptom, the diagnosis is: ${data.diagnosis.join(', ')}`);
        } else {
            diagnosisText = '<strong>Diagnosis:</strong> No diagnosis available.';
            speakText('No diagnosis is available.');
        }

        if (data.remedies && data.remedies.length > 0) {
            remediesText = '<br><br><strong>Remedies:</strong><br>' + data.remedies.join('<br>');
            speakText(` ${data.remedies.join(', ')}`);
        } else {
            remediesText = '<br><br><strong>Remedies:</strong> No remedies available.';
            speakText('No remedies are available.');
        }

        document.getElementById('output').innerHTML += `<br><br>${diagnosisText}${remediesText}`;

    })
    .catch(error => {
        document.getElementById('output').innerHTML += `<br><br><strong>Error contacting Health Assistant.</strong>`;
        console.error('Backend error:', error);
    });
}

function speakText(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    speechSynthesis.speak(utterance);
}
