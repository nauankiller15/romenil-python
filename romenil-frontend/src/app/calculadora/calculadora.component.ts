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
    $('#fecharBtCalc').on('click', function () {
      $('#calculadora').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');

    $('#calculated').on('click', function () {
      $('#calculadoraForm').slideUp('100');
    });
  }
}
