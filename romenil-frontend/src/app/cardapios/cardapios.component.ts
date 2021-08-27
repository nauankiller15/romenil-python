import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'app-cardapios',
  templateUrl: './cardapios.component.html',
  styleUrls: ['./cardapios.component.css'],
})
export class CardapiosComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {
    $('#fecharBtCardp').on('click', function () {
      $('#cardapio').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }
}
