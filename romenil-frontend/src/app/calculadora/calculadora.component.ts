import { Component, OnInit } from '@angular/core';

declare var $: any;

@Component({
  selector: 'app-calculadora',
  templateUrl: './calculadora.component.html',
  styleUrls: ['./calculadora.component.css'],
})
export class CalculadoraComponent implements OnInit {
  calculadora = {
    sexo: '',
    idade: null,
    peso: null,
    altura: null,
    nivel_atividade: '',
  };

  constructor() {}

  ngOnInit(): void {
    $('#fecharBtCardp').on('click', function () {
      $('#calculadora').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
    //
    $('#calculated').on('click', function () {
      $('#calculadoraForm').fadeOut(350);
      $('#resultados').slideDown(350);
      $('.cardBtn').slideDown(250);
    });
    $('#refazerIMC').on('click', function () {
      $('#calculadoraForm').slideDown(450);
      $('#resultados').slideUp(450);
      $('.cardBtn').slideDown(250);
    });
  }
}
