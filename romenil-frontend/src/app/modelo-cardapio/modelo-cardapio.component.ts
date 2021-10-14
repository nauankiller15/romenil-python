import { Component, Input, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'app-modelo-cardapio',
  templateUrl: './modelo-cardapio.component.html',
  styleUrls: ['./modelo-cardapio.component.css'],
})
export class ModeloCardapioComponent implements OnInit {
  @Input() cardapio: string = '';
  eulaContent = '';

  constructor() {}
  ngOnInit(): void {
    $(document).ready(function () {
      $('.date').load('a.html');
    });
  }
}
