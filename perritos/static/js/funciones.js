
//función que valida un formulario
 $(function(){
    $("#mi-formulario").validate({
        rules:{
            nom:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            pass:{
                required:true
            },
            fono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:pass
            }
        },//rules
        messages:{
            nom:{
                required:'Ingrese nombre del usuario',
                minlength:'Caracteres insuficientes (3)'
            },
            correo:{
                required:'Ingrese correo del usuario',
                email:'Formato incorrecto del correo'
            },
            pass:{
                required:'Ingrese una contraseña',
                minlength: 'Caracteres insuficientes(8)'
            },
            fono:{
                required:'Ingrese un teléfono válido',
                minlength: 'Cantidad de digitos insuficientes'
            },
            fecha:{
                required:'Seleccione una fecha válida',
                min:'Fecha no corresponde'
            },
            pass2:{
                required:'Ingrese una contraseña',
                minlength: 'Caracteres insuficientes(8)',
                equalTo:'Contraseñas no coinciden'
            },
        }//messages
    });
});