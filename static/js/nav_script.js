document.addEventListener("DOMContentLoaded", function() {

    const profile = document.getElementById('profile')

    if (profile) {

        const width = document.getElementById('profile-part').offsetWidth;

        profile_menu = document.getElementById('profile-menu');
        
        profile_menu.style.width = width + 'px';

        
        profile.addEventListener('click', function (e) {
            profile_menu.classList.toggle('show');
            document.getElementById('triangle').classList.toggle('transform-180');
            // console.log(profile_menu.classList);
        });
    }

    

});