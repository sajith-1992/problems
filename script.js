function show(val){
     document.getElementById("screen_value").value+= val
}
function minus(){
  var  minus_oldval = document.getElementById("screen_value").value
    document.getElementById("screen_value").value=""
    
    eql(minus_oldval,calculator)
    

  
    
}
function eql(){
     var new_value=document.getElementById("screen_value").value
     console.log(new_value)
    switch (calculator){
        case 1:
           var result= new_value-minus_oldval
    }
    document.getElementById("screen_value").value=result
}
