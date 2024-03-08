$(document).ready(function(){
    $("#signup-form").validate({
        rules:{
           email:{
            required:true,
            email:true


           },
           psw:{
            required:true,
            minlength:4
           }


        }

        
    })
})