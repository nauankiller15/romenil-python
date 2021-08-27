$(function() {
    $(document).scroll(function() {
        var $nav = $(".menu");
        $nav.toggleClass('menu-back', $(this).scrollTop() > $nav.height());
    });
});

function MenuAtivo() {
    $('.menuItems li a').on('click', function() {
        $(this).addClass('active');
        $(this).siblings().removeClass('active');
    });
}