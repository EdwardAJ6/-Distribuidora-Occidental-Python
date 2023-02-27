const formulario = document.getElementById('FormRegistro');
const inputs = document.querySelectorAll('#FormRegistro input');

const expresiones = {
    numdocumen: /\d{10,12}/,

	nombres: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, 

    apellidos: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,

    telefono: /^\d{10}$/ ,

    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,

	contra: /^[a-zA-Z0-9\_\-]{4,16}$/
	
}

const campos = {
    numdocumen: false,
    nombres: false,
    apellidos: false,
    telefono: false,
    correo: false,
    contra: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "numdoc":
            if(expresiones.numdocumen.test(e.target.value)){
                document.getElementById('grupo_doc').classList.remove('formnumdoc-incorrecto');
                document.getElementById('grupo_doc').classList.add('formnumdoc-correcto');
                document.querySelector('#grupo_doc i').classList.add('fa-check-circle');
                document.querySelector('#grupo_doc i').classList.remove('fa-times-circle');
                document.querySelector('#grupo_doc .error').classList.remove('error-activo');
                campos['numdocumen'] =true;
            }
            else{
                document.getElementById('grupo_doc').classList.add('formnumdoc-incorrecto');
                document.getElementById('grupo_doc').classList.add('formnumdoc-correcto');
                document.querySelector('#grupo_doc i').classList.add('fa-times-circle');
                document.querySelector('#grupo_doc i').classList.remove('fa-check-circle');
                document.querySelector('#grupo_doc .error').classList.add('error-activo');
                campos['numdocumen'] =false;
            }

        break;

        case "nombres":
            if(expresiones.nombres.test(e.target.value)){
                document.getElementById('grupo_nombres').classList.remove('formnombres-incorrecto');
                document.getElementById('grupo_nombres').classList.add('formnombres-correcto');
                document.querySelector('#grupo_nombres i').classList.add('fa-check-circle');
                document.querySelector('#grupo_nombres i').classList.remove('fa-times-circle');
                document.querySelector('#grupo_nombres .error').classList.remove('error-activo');
                campos['nombres'] =true;
            }
            else{
                document.getElementById('grupo_nombres').classList.add('formnombres-incorrecto');
                document.getElementById('grupo_nombres').classList.add('formnombres-correcto');
                document.querySelector('#grupo_nombres i').classList.add('fa-times-circle');
                document.querySelector('#grupo_nombres i').classList.remove('fa-check-circle');
                document.querySelector('#grupo_nombres .error').classList.add('error-activo');
                campos['nombres'] =false;
                
            }
            
            
        break;

        case "apellidos":
            if(expresiones.apellidos.test(e.target.value)){
                document.getElementById('grupo_apellidos').classList.remove('formapellidos-incorrecto');
                document.getElementById('grupo_apellidos').classList.add('formapellidos-correcto');
                document.querySelector('#grupo_apellidos i').classList.add('fa-check-circle');
                document.querySelector('#grupo_apellidos i').classList.remove('fa-times-circle');
                document.querySelector('#grupo_apellidos .error').classList.remove('error-activo');
                campos['apellidos'] =true;
            }
            else{
                document.getElementById('grupo_apellidos').classList.add('formapellidos-incorrecto');
                document.getElementById('grupo_apellidos').classList.add('formapellidos-correcto');
                document.querySelector('#grupo_apellidos i').classList.add('fa-times-circle');
                document.querySelector('#grupo_apellidos i').classList.remove('fa-check-circle');
                document.querySelector('#grupo_apellidos .error').classList.add('error-activo');
                campos['apellidos'] =false;
            }
            
        break;

        case "telefono":
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('grupo_telefono').classList.remove('formtelefono-incorrecto');
                document.getElementById('grupo_telefono').classList.add('formtelefono-correcto');
                document.querySelector('#grupo_telefono i').classList.add('fa-check-circle');
                document.querySelector('#grupo_telefono i').classList.remove('fa-times-circle');
                document.querySelector('#grupo_telefono .error').classList.remove('error-activo');
                campos['telefono'] =true;
            }
            else{
                document.getElementById('grupo_telefono').classList.add('formtelefono-incorrecto');
                document.getElementById('grupo_telefono').classList.add('formtelefono-correcto');
                document.querySelector('#grupo_telefono i').classList.add('fa-times-circle');
                document.querySelector('#grupo_telefono i').classList.remove('fa-check-circle');
                document.querySelector('#grupo_telefono .error').classList.add('error-activo');
                campos['telefono'] =false;
            }
            
        break;

        case "contra":
            if(expresiones.contra.test(e.target.value)){
                document.getElementById('grupo_contra').classList.remove('formcontra-incorrecto');
                document.getElementById('grupo_contra').classList.add('formcontra-correcto');
                document.querySelector('#grupo_contra i').classList.add('fa-check-circle');
                document.querySelector('#grupo_contra i').classList.remove('fa-times-circle');
                campos['contra'] =true;
            }
            else{
                
                document.getElementById('grupo_contra').classList.add('formcontra-incorrecto');
                document.getElementById('grupo_contra').classList.add('formcontra-correcto');
                document.querySelector('#grupo_contra i').classList.add('fa-times-circle');
                document.querySelector('#grupo_contra i').classList.remove('fa-check-circle');
                campos['contra'] =false;
            }
            
        break;

        case "correo":
            if(expresiones.correo.test(e.target.value)){
                document.getElementById('grupo_correo').classList.remove('formcorreo-incorrecto');
                document.getElementById('grupo_correo').classList.add('formcorreo-correcto');
                document.querySelector('#grupo_correo i').classList.add('fa-check-circle');
                document.querySelector('#grupo_correo i').classList.remove('fa-times-circle');
                campos['correo'] =true;
            }
            else{
                document.getElementById('grupo_correo').classList.add('formcorreo-incorrecto');
                document.getElementById('grupo_correo').classList.add('formcorreo-correcto');
                document.querySelector('#grupo_correo i').classList.add('fa-times-circle');
                document.querySelector('#grupo_correo i').classList.remove('fa-check-circle');
                document.querySelector('#grupo_correo .error').classList.add('error-activo');
                campos['correo'] =false;
            }
            
        break;

    }

}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
    
    });


formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    if(campos.numdocumen && campos.nombres && campos.apellidos && campos.telefono && campos.correo && campos.contra){

        document.getElementById('mensajeExito').classList.add('mensajeExito-activo');
        setTimeout(() =>{
            document.getElementById('mensajeExito').classList.remove('mensajeExito-activo');

        }, 5000);
    }
    
        else{
            document.getElementById('mensajeError').classList.add('mensajeError-activo');
            
        }
     
});


