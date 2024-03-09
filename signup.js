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


        },
        messages:{
            email:{
                required : "Please enter a valid email address"
            },
            psw:{
                required:"This field cannot be empty",
                minlength:"There should be a minimum of 4 characters"
            }
        }

        
    })
})