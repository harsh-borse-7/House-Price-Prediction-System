
function form_handler(event) {
    event.preventDefault();
}
function send_data()
{
    document.querySelector('form').addEventListener("submit",form_handler);

    var fd=new FormData(document.querySelector('form'));

    var xhr= new XMLHttpRequest({mozSystem: true});

   console.log(34);
    xhr.open('POST','/predict',true);

    xhr.onreadystatechange = function(){
    console.log(xhr.readyState)
        if(xhr.readyState == XMLHttpRequest.DONE){

            document.getElementById('prediction').innerHTML="Price: ₹"+xhr.responseText;

        }
    };

    xhr.onload= function(){};

    xhr.send(fd);
}