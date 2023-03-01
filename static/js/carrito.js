
class Carrito{

    //AÑADIR EL PRODUCTO AL CARRITO
    comprarProducto(e){
        e.preventDefault();
        if(e.target.classList.contains('agregar-carrito')){
            const producto= e.target.parentElement.parentElement;
             this.leerDatosProducto(producto);
             
        }
    }

    leerDatosProducto(producto){
        const infoProducto = {
            imagen : producto.querySelector('img').src,
            titulo : producto.querySelector('h5').textContent,
            precio : producto.querySelector('.precio').textContent,
            id : producto.querySelector('a').getAttribute('data-id'),
            cantidad : 1
        }
        this.insertarCarrito(infoProducto);
    }

    insertarCarrito(producto){
        const row = document.createElement('tr');
        row.innerHTML = `
          <td> 
             <img src="${producto.imagen}" width=100> 
          </td>
          <td>${producto.titulo}</td>
          <td>${producto.precio}</td>
          <td>
             <a href="#" class"btn-close borrar-producto" data-id="${producto.id}"></a>
          </td>
        `;
        listaProductos.appendChild(row);
        this.guardarProductosLocalStorage(producto);
    }

    eliminarProducto(e){
        e.preventDefault();
        let producto, productoID;
        if(e.target.classList.contains('borrar-producto')){
        e.target.parentElement.parentElement.remove();
        producto = e.target.parentElement.parentElement;
        productoID = producto.querySelector('a').getAttribute('data-id');
    }
    this.eliminarProductoLocalStorage(productoID);
}

    vaciarCarrito(e){
        e.preventDefault();
        while(listaProductos.firstChild){
            listaProductos.removeChild(listaProductos.firstChild);
        }

        return false;
    }

    guardarProductosLocalStorage(producto){
        let productos;
        productos = this.obtenerProductosLocalStorage();
        productos.push(producto);
        localStorage.setItem('productos', JSON.stringify(productos));
    }

    obtenerProductosLocalStorage(){
        let productosLS;

        if(localStorage.getItem('productos') === null){
            productosLS = [];
        }

        else {
            productosLS = JSON.parse(localStorage.getItem('productos'));
        }
        return productosLS;
    }

    eliminarProductoLocalStorage(productoID){
        let productosLS;
        productosLS = this.obtenerProductosLocalStorage();
        productosLS.forEach(function(productosLS, tienda){
            if(productosLS.id === productoID){
                productosLS.splice(tienda, 1);
            }
    
    });

    localStorage.setItem('productos', JSON.stringify(productosLS));

    

    }

}

