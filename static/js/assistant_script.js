const scrollable = document.querySelector('.content');

const voice = document.getElementById('voice');
const text_area = document.getElementById('text_area');
const text_placeholder = text_area.getAttribute('placeholder');

let mediaRecorder;
let chunks = [];
let audioElement;


function scrollBottom () {
    scrollable.scrollTop = scrollable.scrollHeight;
}

function getCSRFToken() {
    const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];
    return cookieValue;
}

function playAudio(audioUrl) {
    audioElement = new Audio(audioUrl);
    audioElement.play();
    document.getElementById("stop-sound").style.cursor = 'pointer';
    audioElement.addEventListener('ended', function () {
        document.getElementById('stop-sound').style.cursor = 'not-allowed';
    });
}

function sendAudioToServer(audioBlob) {
    let formData = new FormData();
    formData.append('audio', audioBlob);
    formData.append('api_token', document.getElementById("api_token").textContent)

    fetch('/voice-assistant/recognize-audio/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then(data => {
        sendTextToServer(data["text"]);
    }).catch(error => {
        console.error(error);
        alert("Щось пішло не так");
    })
}

function sendTextToServer(text) {
    let formData = new FormData();
    formData.append('text', text);
    formData.append('api_token', document.getElementById("api_token").textContent);

    fetch('/voice-assistant/exec-command/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    }).then(respones => {
        if (!respones.ok) {
            throw new Error('Network response was not ok');
        }
        return respones.json();
    }).then(data => {
        document.getElementById("content").insertAdjacentHTML('beforeend', data["text"]);
        scrollBottom();
        playAudio(data['audio_path']);
    }).catch(error => {
        console.error(error);
        alert("Щось пішло не так");
    });
}

scrollable.addEventListener('resize', scrollBottom);

window.onload = scrollBottom;

navigator.mediaDevices.getUserMedia({ audio: true }).then(function(stream) {
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = function(event) {
        chunks.push(event.data);
    };

    mediaRecorder.onstop = function() {
        let audioBlob = new Blob(chunks, {'type' : 'audio/vnd.wave;'});
    
        sendAudioToServer(audioBlob);
    };

}).catch(function(err) {
    console.error('Error accessing microphone: ', err);
    alert('Помилка доступу до мікрофону');
});

document.getElementById("stop-sound").addEventListener('click', function() {
    if (audioElement) {
        audioElement.pause();
        audioElement.currentTime = 0;
        document.getElementById('stop-sound').style.cursor = 'not-allowed';
    }
});

document.getElementById('send').addEventListener('click', function() {
    const text = text_area.value;
    if (!text) {
        alert("Ви відправляєте пустий запит");
        return;
    }
    text_area.value = "";
    sendTextToServer(text);
});

voice.addEventListener('click', function(e) {
    if (text_area.getAttribute('placeholder') == text_placeholder) {
        if (mediaRecorder) {
            text_area.setAttribute('placeholder', 'Слухаю вас');
            text_area.setAttribute('readonly', true);
            text_area.value = '';
            
            chunks = [];
            mediaRecorder.start();
        } else {
            console.error('MediaRecorder is not initialized');
            alert('Сталася помилка. Спробуйте перезавантажити сторінку');
        }
    } else {
        text_area.setAttribute('placeholder', text_placeholder);
        text_area.removeAttribute('readonly');
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            mediaRecorder.stop();
        } else {
            console.error('MediaRecorder is not initialized or already stopped.');
            alert('Сталася помилка. Спробуйте перезавантажити сторінку');
        }
    }
});

text_area.addEventListener('keydown', function(event) {
    if (event.key == 'Enter') {
        event.preventDefault();
        document.getElementById('send').click();
    }
});
