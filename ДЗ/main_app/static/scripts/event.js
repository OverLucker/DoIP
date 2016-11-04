$('#header_login').click ( function (){
    alert("logged");
    $('#header_sign_up').hide();
    $('#header_login').hide();
    $('#header_user_page').show();
    $('#header_logout').show();
});

$('#header_logout').click( function () {
    alert("logout");
    $('#header_user_page').hide();
    $('#header_logout').hide();
    $('#header_sign_up').show();
    $('#header_login').show();
});

$('#join').click( function() {
    // i should submit here that i'm going to participate
});

$('#leave').click( function() {
    // i should submit here that i'm NOT going to participate
});

$( document ).ready( function() {
    $('body').show();
});

window.onload = function() {
    if ($('.item_view').attr('is_part') == "True")
        $('#join').hide();
    else
        $('#leave').hide();
};
