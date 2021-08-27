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
      $('#calculadoraForm').fadeOut(250);
      $('.cardBtn').slideDown(250);
    });
  }
}
