document.addEventListener("DOMContentLoaded", function() {
    const btn_open_modal = document.getElementById('change-password');
    const modal = document.getElementById('modal')

    btn_open_modal.onclick = function () {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }

    modal.onclick = function(e) {
        if (e.target == modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }
});