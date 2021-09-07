import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Erro } from 'src/app/shared/erros';
import { AccountService } from '../../shared/account.service';

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

  onSubmit() {
    this.carregando = true;
    this.accountService.login(this.login).subscribe(
      (data) => {
        window.localStorage.setItem('token', data.token);
        // navego para a rota vazia novamente
        this.router.navigate(['/welcome']);
        this.toastrService.success('Login efetuado com sucesso!');
      },

      (error) => {
        this.carregando = false;
        const erro = new Erro(this.toastrService, error);
        erro.exibir()        
      }
    );
  }
}
