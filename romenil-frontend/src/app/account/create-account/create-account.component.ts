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
    passwordvalid: '',
    cpf: '',
    cnpj: '',
    celular: '',
  }

  constructor() { }

  ngOnInit(): void {

  }

  onSubmit(){

  }

}
