$('.list-group-item .custom-control-label').on('click', function(){
    var checkBox = $(this).prev('input');

    console.log(checkBox);

    if($(checkBox).attr('checked'))
  	    $(checkBox).removeAttr('checked');
    else
  	    $(checkBox).attr('checked', 'checked');

    return false;

})
