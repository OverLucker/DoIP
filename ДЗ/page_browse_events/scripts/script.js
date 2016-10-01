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

$('#click_me').click( function () {
    $.get ("../cgi-bin/form.py").done (function (data) { 
        alert("data : " + data);
    });
});

