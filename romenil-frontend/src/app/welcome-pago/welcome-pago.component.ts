import { Component, OnInit } from '@angular/core';
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
  ) { 
    this.getConta();
  }

  ngOnInit(): void {
    $('#fecharBtWelcomePago').on('click', function () {
      $('#bemvindo-pago').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
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
