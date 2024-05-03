
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('btn-link').addEventListener('click', (e) => {
        window.location.href = e.target.attributes.target_url.value;
    });
    
    let message = document.getElementById('message');
    if (message) {
        setTimeout(() => {
            message.classList.add('hidden');
        }, 3000);
    }
});