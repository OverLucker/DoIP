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

var last_page = 1;

function getCurHeight()
{
    return  $(document).height() - 100;
}

var started = false;

$(document).ready( function() {
    $(window).scroll( function () {
        if (started)
            return;
        if($(window).scrollTop() + $(window).height() >= getCurHeight() ) {
            started = true;
            $.ajax({
                url:'page='+last_page,
                type:'get',
                success: function(response, status) {  
                    $('.item_container').append(response);
                    last_page++;
                }
            }).done (function() { started = false;});
        }    
    })
})
