import { Component, OnInit } from '@angular/core';

declare var $: any;

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})
export class CreateAccountComponent implements OnInit {

  criarconta = {
    nome: '',
    email: '',
    password: '',
  }

  constructor() { }

  ngOnInit(): void {
    $('#fecharBtCriar').on('click', function () {
      $('#criarconta').fadeOut('100');
    });
    $('#voltarLogin').on('click', function () {
      $('#criarconta').fadeOut('100');
      $('#login').fadeIn('100');
    });
  }

  onSubmit(){

  }

}
