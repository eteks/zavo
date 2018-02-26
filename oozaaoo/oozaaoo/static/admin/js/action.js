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
        adult = $('#id_no_of_adult').text();
        children = $('#id_no_of_children').text();
        infant = $('#id_no_of_infant').text();
        var myurl = "/get_package_details/"
        $.ajax({
            type: "POST",
            url: myurl,
            // data: ""selected=" + selected",
            data: "package_id="+package_id+"&adult="+adult+"&children="+children+"&infant="+infant,
            success: function(response) {
                // $('#id_total_amount').val(response.total_cost);
                // $('#id_balance_amount').val(response.balance_amount);
            },
        });
    });
});