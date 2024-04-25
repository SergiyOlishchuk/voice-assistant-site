
document.getElementById('registrate').addEventListener('click', (e) => {
    const url = e.target.attributes.target-url.value; 
    window.location.href = url;
});