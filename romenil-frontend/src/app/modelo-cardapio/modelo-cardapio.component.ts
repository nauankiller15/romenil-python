import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-modelo-cardapio',
  templateUrl: './modelo-cardapio.component.html',
  styleUrls: ['./modelo-cardapio.component.css']
})
export class ModeloCardapioComponent implements OnInit {

  @Input() cardapio: string = '';

  constructor() { }

  ngOnInit(): void {
  }

}
