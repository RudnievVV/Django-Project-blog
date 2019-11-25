// Reset profile image function
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

// Post rating function
$(document).ready(function(){
    $("#starGet").click(function (){
        window.location.replace(
            window.location.pathname + $("input:radio[name=rating]:checked").val() + "/rate"
        );
    });
});

// Top navigation categories search function
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

// Post details user image popup function
$(document).ready(function(){
    // Get the modal
    var modal, img, modalImg, captionText, span
    modal = document.getElementById("user_image_popup");

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    img = document.getElementById("user_image_post_details");
    modalImg = document.getElementById("img01");
    captionText = document.getElementById("user_image_popup_caption");
    img.onclick = function(){
      modal.style.display = "block";
      modalImg.src = this.src;
      captionText.innerHTML = this.alt;
    };

    // Get the <span> element that closes the modal
    span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
      modal.style.display = "none";
    };
});