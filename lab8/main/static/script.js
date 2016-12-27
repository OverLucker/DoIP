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

    $.plot(
        $('#display'), 
        [{
            label: func, 
            data:func_arr,
            color: "#000000"
        }], 
        {}
    );

})