
// window.onload = function(){ alert('asd'); }

$('#plot').click(function(){
    low = parseFloat($('input[name=low]').val());
    high = parseFloat($('input[name=high]').val());
    func = $('input[name=function]').val();
    
    func_arr = []
    for(var i = low; i < high; i+=.1)
    {
        const x = i;
        const y = eval(func)
        func_arr.push([x, y]);
    }
    // alert(func_arr);
    // func_arr = [[0,1], [0,2], [0,3] ];
    $.plot(
        $('#display'), 
        [{
            label: func, 
            data:func_arr,
            color: "#000000"
        }], 
        {}
    );
    // alert(low + ' ' + high + ' ' + func);
})