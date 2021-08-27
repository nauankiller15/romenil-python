import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
})
export class FormularioComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {
    $('#fecharBtCardp').on('click', function () {
      $('#formulario').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }
}