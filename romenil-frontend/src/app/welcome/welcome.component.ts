import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { Erro } from '../shared/erros';
declare var $: any;

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css'],
})
export class WelcomeComponent implements OnInit {
  conta = new Conta();

  constructor(
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router
  ) {
    this.verificarDados();
  }

  ngOnInit(): void {
    $('#fecharBtWelcome').on('click', function () {
      $('#bemvindo').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }

  verificarDados() {
    if (this.accountService.autenticado()) {
      this.getUsuario();
    } else {
      this.router.navigate(['/login']);
    }
  }

  getUsuario() {
    this.accountService.usuario().subscribe(
      (data) => {
        if (!data.usuario) {
          this.router.navigate(['/create-account']);
        } else {
          this.getConta();
        }
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  getConta() {
    this.accountService.conta().subscribe(
      (data) => {
        this.conta = data;
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
