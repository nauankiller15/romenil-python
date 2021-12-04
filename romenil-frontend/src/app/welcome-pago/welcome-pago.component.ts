import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { Erro } from '../shared/erros';
declare var $: any;

@Component({
  selector: 'app-welcome-pago',
  templateUrl: './welcome-pago.component.html',
  styleUrls: ['./welcome-pago.component.css'],
})
export class WelcomePagoComponent implements OnInit {

  conta = new Conta;

  constructor(
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router
  ) { 
    this.getUsuario();
  }

  ngOnInit(): void {
    $(document).ready(function () {
      $('.loader-wrapper').fadeIn(250).delay(1200).fadeOut(250);
    });
    $('#fecharBtWelcomePago').on('click', function () {
      $('#bemvindo-pago').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }

  getUsuario() {
    this.accountService.usuario().subscribe(
      (data) => {
        if (data.user) {
          if (data.ativo) {
            this.getConta();
          } else {
            this.router.navigate(['/conversao']);
          }
        } else {
          this.router.navigate(['/welcome']);
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
