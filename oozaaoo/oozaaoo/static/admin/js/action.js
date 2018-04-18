$(document).ready(function(){
	$('#id_booking_id').blur(function(){
        booking_id = $(this).val();
		var myurl = "/total_amount_generation/"
		$.ajax({
            type: "POST",
            url: myurl,
            // data: ""selected=" + selected",
            data: "booking_id="+booking_id,
            success: function(response) {
                $('#id_total_amount').val(response.total_cost);
                $('#id_balance_amount').val(response.balance_amount);
            },
        });
	});

    $('#id_package').change(function(){
        // alert($(this).find('option:selected').val());
        package_id = $(this).find('option:selected').val();
        adult = $('#id_no_of_adult').val();
        children = $('#id_no_of_children').val();
        infant = $('#id_no_of_infant').val();
        // alert(adult);
        // alert(children);
        // alert(infant);
        var myurl = "/get_package_details/"
        $.ajax({
            type: "POST",
            url: myurl,
            // data: ""selected=" + selected",
            data: "package_id="+package_id+"&adult="+adult+"&children="+children+"&infant="+infant,
            success: function(response) {
                // alert(JSON.stringify(response));
                $('#id_package_cost').val(response.package_cost);
                // $('#id_balance_amount').val(response.balance_amount);
            },
        });
    });

    $('#id_discount').blur(function(){
        discount_val = $(this).val();
        package_cost = $('#id_package_cost').val();
        var myurl = "/caculate_booking_cost/"
        $.ajax({
            type: "POST",
            url: myurl,
            // data: ""selected=" + selected",
            data: "discount_val="+discount_val+"&package_cost="+package_cost,
            success: function(response) {
                $('#id_total_cost').val(response.total_cost);
            },
        });
    });
});