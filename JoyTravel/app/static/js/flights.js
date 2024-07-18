// Show and hide sidebar

function showSidebar(){
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.width = "250px";
}

function hideSidebar(){
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.width = "0px";
}

// Give navbar background color when scroll

document.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');

    if(window.scrollY > 200){
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert');
    if (alerts.length > 0) {
        setTimeout(() => {
            alerts.forEach(alert => {
                alert.style.display = 'none';
            });
        }, 10000);
    }
});