jQuery('document').ready(function(){
	jQuery("#reset-image").on("click", function() {
		var image_reset
		image_reset = confirm("Do you confirm image reset?");
		if (image_reset) {
			window.location.replace("/profile/reset-image/")
		} else {
			return false;
		}
	});

});