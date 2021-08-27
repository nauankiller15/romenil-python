jQuery(document).ready(function() {

    jQuery(".botaobottom").hide();

    jQuery(window).scroll(function() {
        if (jQuery(this).scrollTop() > 300) {
            jQuery('.botaobottom').fadeIn('200');
        } else {
            jQuery('.botaobottom').fadeOut('100');
        }
    });
});