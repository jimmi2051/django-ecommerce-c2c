$(document).ready(function(){
    var check_url = $(location).attr('pathname').split('/');
    var id_attribute = check_url[check_url.length - 1]

    // Load data in attribute
    $.ajax({
        url: 'http://localhost:8000/admin/attribute/' + id_attribute,
        method: 'GET',
        contentType: 'application/json',
        success: function(response){
            console.log(response);
            attribute = response[0]['fields']

            $('#inputLabel').val(attribute.label);
            var option_active = ''
            if(attribute.is_active == true){
                option_active += '<option value="1" selected >Kích hoạt</option>'
                option_active += '<option value="0">Đang khoá</option>'
            }else{
                option_active += '<option value="1">Kích hoạt</option>'
                option_active += '<option value="0" selected >Đang khoá</option>'
            }
            $('#inputIsActive').append(option_active)
            
        }
    })

    // Edit Category

    $('#edit').click(function(){
        data = {
            'inputLabel': $('#inputLabel').val(),
            'inputIsActive': $('#inputIsActive').val(),   
        }

        $.ajax({
            url: 'http://localhost:8000/admin/attribute/' + id_attribute,
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                console.log(response);
                if(response == 1){
                    setTimeout("pageRedirect('/admin/manager_attribute')", 3000);
                    alert('Da sua thanh cong!\nBan se duoc dieu huong den danh sach thuoc tinh sau 3 giay!');
                }
                else
                    alert('ERROR')
            }
        })
    });

    $('#delete').click(function(){
        $.ajax({
            url: 'http://localhost:8000/admin/attribute/' + id_attribute,
            method: 'DETELE',
            success: function(response){
                console.log(response);
                if(response == 1){
                    setTimeout("pageRedirect('/admin/manager_attribute')", 3000);
                    alert('Thuoc tinh da bi xoa!\nBan se duoc dieu huong den danh sach thuoc tinh sau 3 giay!');
                }
                else
                    alert('ERROR')
            }
        })
    });
});
