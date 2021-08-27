// 
// 
// 
// Animação Login Abrir

$('#loginBt').on('click', function() {
    console.log('Teste');
    $('#login').fadeIn('500');
})

$('#fecharBt').on('click', function() {
    $('#login').fadeOut('500');
})

// 
// 
// 
// 

// 
// 
// 
// ---------------------------------------
// ANIMAÇÃO MENU TOPO
// ----------------------------------------
// 
// Animação Inicio Abrir
// 
$('#inicioAbrir').on('click', function() {
    $(window).scrollTop(0);
    $("#inicio").fadeIn('600');
    $('#contato').fadeOut('600');
    $('#time').fadeOut("700");
    $('#sobre').fadeOut('600');

})

// 
// 
// 
// 
// 
// Animação Sobre Abrir
// 
$('#sobreAbrir').on('click', function() {
    $(window).scrollTop(0);
    $('#sobre').fadeIn('600');
    $("#inicio").fadeOut('600');
    $('#contato').fadeOut('600');
    $('#time').fadeOut("700");
})


// Animação Contato Abrir
$('#contatoAbrir').on('click', function() {
    $(window).scrollTop(0);
    $('#contato').fadeIn("700");
    $('#sobre').fadeOut('600');
    $("#inicio").fadeOut('600');
    $("#time").fadeOut('600');
})

// 
// 
// --------------------------------
// ANIMAÇÃO FOOTER
// --------------------------------
//
// 
// 
// Animação Inicio Abrir
// 
$('#inicioAbrirBottom').on('click', function() {
    $('#inicioAbrir').trigger('click');

})

// 
// 
// 
// 
// Animação Sobre Abrir
// 
$('#sobreAbrirBottom').on('click', function() {
    $('#sobreAbrir').trigger('click');
})

// 
// 
// 
// 
// Animação Contato Abrir
// 
$('#contatoAbrirBottom').on('click', function() {
    $('#contatoAbrir').trigger('click');
})

// 
// 
// 
// 
// 
// ---------------------------------------
// ANIMAÇÃO MENU RESPONSIVO
// ----------------------------------------
// 
// Animação Inicio Abrir
// 
$('#inicioAbrirResponsv').on('click', function() {
    $(window).scrollTop(0);
    $('.header').trigger('click');
    $("#inicio").fadeIn('600');
    $('#contato').fadeOut('600');
    $('#time').fadeOut("700");
    $('#sobre').fadeOut('600');

})

// 
// 
// 
// 
// 
// Animação Sobre Abrir
// 
$('#sobreAbrirResponsv').on('click', function() {
    $(window).scrollTop(0);
    $('.header').trigger('click');
    $('#sobre').fadeIn('600');
    $("#inicio").fadeOut('600');
    $('#contato').fadeOut('600');
    $('#time').fadeOut("700");
})

// 
// 
// 
// Animação Contato Abrir
$('#contatoAbrirResponsv').on('click', function() {
    $(window).scrollTop(0);
    $('.header').trigger('click');
    $('#contato').fadeIn("700");
    $('#sobre').fadeOut('600');
    $("#inicio").fadeOut('600');
    $('#time').fadeOut('600');
})





// 
// 
// --------------------------------
// ANIMAÇÃO PÁGINA SOBRE PARA IR PRA PÁGINA DE CONTATO
// --------------------------------
//
// 
// 
// Animação BOTÃO CONTATO Abrir
// 
$('#sobreContato').on('click', function() {
    $('#contatoAbrir').trigger('click');

})

// 
//



