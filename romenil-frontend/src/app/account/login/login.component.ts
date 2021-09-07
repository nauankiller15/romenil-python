import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService } from '../shared/account.service';
import { ToastrService } from 'ngx-toastr';

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
    private toastr: ToastrService,
    private accountService: AccountService,
    private router: Router
  ) { console.log(this.accountService.autenticado())}

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
        this.toastr.success('Login efetuado com sucesso!');
      },

      (error) => {
        this.carregando = false;
        this.toastr.error(error.error);
      }
    );
  }
}
