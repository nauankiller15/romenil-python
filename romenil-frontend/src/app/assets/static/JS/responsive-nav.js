$('div.burger').on('click', function() {

    if (!$(this).hasClass('open')) { openMenu(); } else { closeMenu(); }

});


$('div.menu-mobile li').on('click', function() {
    closeMenu();
});


function openMenu() {

    $('div.circle').addClass('expand');

    $('div.burger').addClass('open');
    $('div.x, div.y, div.z').addClass('collapse');
    $('.menu-mobile li').addClass('animate');

    setTimeout(function() {
        $('div.y').hide();
        $('div.x').addClass('rotate30');
        $('div.z').addClass('rotate150');
    }, 70);
    setTimeout(function() {
        $('div.x').addClass('rotate45');
        $('div.z').addClass('rotate135');
    }, 120);



}

function closeMenu() {

    $('div.burger').removeClass('open');
    $('div.x').removeClass('rotate45').addClass('rotate30');
    $('div.z').removeClass('rotate135').addClass('rotate150');
    $('div.circle').removeClass('expand');
    $('.menu-mobile li').removeClass('animate');

    setTimeout(function() {
        $('div.x').removeClass('rotate30');
        $('div.z').removeClass('rotate150');
    }, 50);
    setTimeout(function() {
        $('div.y').show();
        $('div.x, div.y, div.z').removeClass('collapse');
    }, 70);

}


// // 
// // 
// // //  
// // //  
// // Função boolean para evento touch mobile
// // 


let stopScrolling = false;

window.addEventListener("touchmove", handleTouchMove, {
    passive: false

});


function handleTouchMove(e) {
    if (!stopScrolling) {
        return;
    }
    e.preventDefault();
}

function onTouchStart() {
    stopScrolling = true;
}

function onTouchEnd() {
    stopScrolling = false;
}

//
//