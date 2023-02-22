const nav = document.querySelector('.navegacion');

window.addEventListener('scroll', function(){
    nav.classList.toggle('active', this.window.scrollY >0)
})