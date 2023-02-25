const carro = new Carrito();
const carrito = document.getElementById('carrito');
const productos = document.getElementById('lista-productos');
const listaProductos = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

cargarEventos();

function cargarEventos(){

    //AGREGAR AL CARRITO
    productos.addEventListener('click', (e)=>{carro.comprarProducto(e)});


    //ELIMINAR PRODUCTOS DEL CARRITO
    carrito.addEventListener('click', (e)=>{carro.eliminarProducto(e)});


    //VACIAR CARRITO 
    vaciarCarritoBtn.addEventListener('click', (e)=>{carro.vaciarCarrito(e)});
}