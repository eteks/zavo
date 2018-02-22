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
});