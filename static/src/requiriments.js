// En tu archivo tu-script.js
document.addEventListener('DOMContentLoaded', function() {
    $('.selectpicker').selectpicker();

    handleGetImagesList();
    

});


function handleGetImagesList(){


    let html = "<option value='0' selected >--Seleccione una opcion--</option>";
    $.ajax({
        type: 'GET',
        url: "/getImages/",
        async: true,
        dataType: "JSON"
        , success: function (data) {
           console.log(data);

            $.each( data.folders, function(i, item){
                console.log(item);
                html += "<option value='" + item + "' >" + item + "</option>";
            } );
           
            if( data.folders.length == 0 ){
                $("#folder-select").html("<option value='0'>No hay carpetas</option>");
            }


           $('#folder-select').html(html);


        }
    });

}



function handlegetImageFromSelect( imgPathFolder ){

    console.log(imgPathFolder);

    $.ajax({
        type: 'GET',
        url: "/getImagesPath/",
        async: true,
        data : { 'folder': imgPathFolder },
        dataType: "JSON"
        , success: function (data) {
           console.log(data);

           const images = data.images;
           const imageContainer = $('#images');

           imageContainer.empty();
           images.forEach(function(imagePath) {
               const imgElement = $('<img>').attr('src', imagePath).attr('alt', 'Image');
               imageContainer.append(imgElement);
           });


        }
    });
}

// Función para obtener el token CSRF
function obtenerCSRFToken() {
    const csrfCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfCookie) {
        return csrfCookie.split('=')[1];
    }
    return null;
}