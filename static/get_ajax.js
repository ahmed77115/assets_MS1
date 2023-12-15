


window.django = { jQuery: jQuery.noConflict(false) };
(function($) {

    $(document).on('input', '#id_last_name', function() {
        alert("jkjfkjkjkjkj")
            // e.preventDefault();


        $.ajax({
            url: '/ahmed/',
            data: { "id": 1 },
            method: 'GET',
            success: function(data) {
                alert("kjkjffffffff")
                console.log(data)
                $.each(data.data, function(i, value) {
                    if (!$('#id' + i).is(":checkbox")) {
                        $(`input[name="${i}"]`).val(value);

                    }
                    if ($('#id' + i).is(":checkbox")) {
                        if (value === true) {
                            $(`input[name="${i}"][type="checkbox"]`).val(value);
                            $(`input[name="${i}"][typ   e="checkbox"]`).prop('checked', 'checked');
                        } else {
                            $(`input[name="${i}"][type="checkbox"]`).prop('checked', false);

                        }
                    }
                    $(`textarea[name="${i}"]`).text(value);
                    $(`select[name="${i}"]option`).each(function() {
                        if ($(this).val() == value) {
                            $(this).prop("selected", true);
                            // $(this).val(value);

                        }
                    });
                    // $("#modalform")..show()
                    // table.ajax.reloadd();
                });
                // console.log(data);
                // alert("jdkfjdkjfkdfffffff");
                // console.log(data);
                $('span[class="text-danger"]').remove();
                if (data.status == 1) {
                    $("#form_id1")[0].reset();
                    alert(data.massage)
                        // $('#modelform').hide()
                    table.ajax.reload();


                } else {
                    if (data.status == 0) {
                        alert(data.massage)

                    } else {
                        if (data.status == 2) {
                            alert(data.massage)
                            let error = JSON.parse(data.error);
                            $.each(error, function(i, value) {
                                let div = '<span class="text-danger" >';
                                $.each(value, function(j, message) {
                                    div += `${message.message} <br>`;

                                });

                                $(`#div_id_${i}`).append(div);
                                // $('#div_id_'+i).append(div);
                            });

                        }
                    }

                }
            },
            error: function(data) {
                alert("jdkfjooooooooooooooooooff");

                alert('error');
            }

        });

    });


})(django.jQuery);