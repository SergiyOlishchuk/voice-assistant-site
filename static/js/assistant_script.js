document.addEventListener("DOMContentLoaded", function() {
    const scrollable = document.querySelector('.content');

    function scrollBottom () {
        scrollable.scrollTop = scrollable.scrollHeight;
    }

    scrollable.addEventListener('resize', scrollBottom);

    window.onload = scrollBottom;

    const voice = document.getElementById('voice');
    const text_area = document.querySelector('.field');
    const text_placeholder = text_area.getAttribute('placeholder');

    voice.addEventListener('click', function(e) {
        if (text_area.getAttribute('placeholder') == text_placeholder) {
            text_area.setAttribute('placeholder', 'Слухаю вас');
            text_area.setAttribute('readonly', true);
            text_area.value = '';
        } else {
            text_area.setAttribute('placeholder', text_placeholder);
            text_area.removeAttribute('readonly');
        }
    });
});