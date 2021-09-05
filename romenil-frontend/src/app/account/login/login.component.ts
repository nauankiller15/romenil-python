import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService } from '../shared/account.service';
import { Login } from './models';

declare var $: any;

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  login = new Login;
  carregando = false;
  
  constructor(private accountService: AccountService, private router: Router) {}

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
      data => {
        // navego para a rota vazia novamente
        this.router.navigate(['']);
      }, 
     
      error => {
        this.carregando = false;
        console.log(error.error)
      }
    );
  }
}
