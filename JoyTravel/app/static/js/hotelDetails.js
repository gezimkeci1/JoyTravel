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

    if(window.scrollY > 100){
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

function showAlertAndRefresh() {
    alert('Hotel booked successfully! You will be contacted by our team about payment and any questions you may have.');
    location.reload();
}