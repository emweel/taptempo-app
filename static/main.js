$(document).ready(function() {
    console.log("ready!");

    $("form").submit(function(){
        //console.log("tap!")
        $.ajax({
            type: "POST",
            url: "/",
            success: function(tempo) {
                //console.log(tempo);
                $("#tempo").html(tempo.tempo)
            },
            error: function(error) {
                console.log(error);
            }
        });
    
    });

});
