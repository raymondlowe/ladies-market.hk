$(document).ready(function () {
    $('.slideshowClass').cycle({
        fx: 'scrollLeft',
        pause: true,
        timeout: 5000
    });

    $('#logo').click(function () {
        window.location.href = 'https://www.ladies-market.hk/';
    });



    bg_color_tween();

});


var colors = Array('#FFD700', '#1f1616', '#ac4620', '#2c4f6c', '#ab7967', '#544948', '#6104a4', '#8c06eb'); //List the hex codes you want to loop through here.


var color_index = 0;
var interval = 1000; //How long the color blend transition lasts. (in milliseconds, 1000 = 1 second)

function bg_color_tween() {
    $('#logo').delay(5000).animate({
        backgroundColor: colors[color_index]
    }, interval, 'linear', function () {
        if (color_index == colors.length) {
            color_index = 0;
        } //If we are at the end of the colors array go back to the beginning.
        else {
            color_index++;
        } //Lets move to the next color in the colors array.s

        bg_color_tween();
    });
}


$(document).ready(function () {
    if ($('#mobile-menu-button').is(":visible")) {
        $('#mobile-menu-button').bigSlide({ menu: '#nav-menu', side: 'left', easyClose: true, push: '.push' });
    }
});
