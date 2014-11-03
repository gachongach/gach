$(function() {
    var $window = $(window);

    

    $window.keydown(function(event) {
        // When the client hits ENTER on their keyboard
        if (event.which === 13) {

            if (name) {
                alert(name)
            }else{
                alert("fail!")
            
            }
        }
    })
})