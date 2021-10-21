import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { Erro } from 'src/app/shared/erros';
import { Login } from '../models';

declare var $: any;

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  login = new Login();
  carregando = false;
  mask = ''
  
  documento_correto = true;

  constructor(
    private toastrService: ToastrService,
    private accountService: AccountService,
    private router: Router
  ) { 
    if (this.accountService.autenticado()) {
      this.router.navigate(['/welcome']);
    }
  }

  ngOnInit(): void {
    $('body').addClass('noborder');

    $('#fecharBtLogin').on('click', function () {
      $('#login').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('#abrirConta').on('click', function () {
      $('#criarconta').fadeIn('100');
      $('#login').fadeOut('100');
    });
  }

  removeMask() {
    this.mask = ''
  }

  getMask() {
    
    console.log(this.login.email_cpf_cnpj);
    if (this.login.email_cpf_cnpj.match(/^\d{11}$|^\d{14}$|^(\d{3}.){2}\d{3}\-\d{2}$|^\d{2}.\d{3}.\d{3}\/\d{4}\-\d{2}$/)) {
      if (isNaN(Number((this.login.email_cpf_cnpj)))) {
        this.login.email_cpf_cnpj = this.login.email_cpf_cnpj.replace(/\./g, '').replace('-', '').replace('/', '');
        this.mask = 'CPF_CNPJ'
        this.documento_correto = true;
      }
    } else if (this.login.email_cpf_cnpj.match(/^\w+\@\w+(\.\w+){1,2}$/)) {
      this.documento_correto = true;
    } else {
      this.documento_correto = false;
    }
  }

  onSubmit() {
    this.carregando = true;
    this.accountService.login(this.login).subscribe(
      (data) => {
        window.localStorage.setItem('token', data.token);
        this.toastrService.success('Login efetuado com sucesso!');
        this.router.navigate(['/welcome']);
      },

      (error) => {
        this.carregando = false;
        const erro = new Erro(this.toastrService, error);
        erro.exibir()        
      }
    );
  }
}
