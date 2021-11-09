// TELA DE CARREGAMENTO
$(window).on("load", function () {
  
    $(".loader-wrapper").fadeOut("slow");
  $('form').each(function () {
    this.reset();
  });
});

$(document).ajaxStart(function () {
  $(".loader-wrapper").fadeIn(250);
});

$(document).ajaxStop(function () {
  $(".loader-wrapper").fadeOut(250);
});