jQuery('document').ready(function(){
	jQuery("#reset-image").on("click", function(){
		var image_reset
		image_reset = confirm("Do you confirm image reset?");
		if (image_reset) {
			window.location.replace("/profile/reset-image/")
		} else {
			return false;
		}
	});

});

$(document).ready(function(){
    $("#starGet").click(function (){
        window.location.replace(
            window.location.pathname + $("input:radio[name=rating]:checked").val() + "/rate"
        );
    });
});

$(document).ready(function(){
    $("#categories_dropbtn_search").on("keyup", function(){
        var input, filter, ul, li, a, i;
        input = document.getElementById("categories_dropbtn_search");
        filter = input.value.toUpperCase();
        div = document.getElementById("nav_dropdown_categories");
        a = div.getElementsByTagName("a");
        for (i = 0; i < a.length; i++) {
            txtValue = a[i].textContent || a[i].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                a[i].style.display = "";
            } else {
                a[i].style.display = "none";
            };
      };
    });
});