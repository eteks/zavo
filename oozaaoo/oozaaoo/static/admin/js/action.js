$(document).ready(function(){
	$('#id_booking_id').blur(function(){
		$('#id_total_amount').val("100");
		var myurl = "/total_amount_generation/"
		$.ajax({
            type: "POST",
            url: myurl,
            data: "selected=" + selected,
            success: function(response) {
                window.location.reload(true);
            },
        });
	});
});