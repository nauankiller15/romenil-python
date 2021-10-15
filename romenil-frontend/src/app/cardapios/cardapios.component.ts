import { Component, OnInit, ViewChild, ViewContainerRef } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { ApiService } from '../shared/api-service/api.service';
import { Erro } from '../shared/erros';
declare var $: any;

@Component({
  selector: 'app-cardapios',
  templateUrl: './cardapios.component.html',
  styleUrls: ['./cardapios.component.css'],
})
export class CardapiosComponent implements OnInit {

  conta = new Conta();
  cardapio = ''
 
  constructor(
    private accountService: AccountService,
    private apiService: ApiService, 
    private toastrService: ToastrService
  ) {
    this.getConta();
    this.getCardapio();
  }

  ngOnInit(): void {
    $('#fecharBtCardp').on('click', function () {
      $('#cardapio').fadeOut('100');
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

  getCardapio() {
    this.apiService.listar('cardapio').subscribe(
      (data) => {
        this.cardapio = data.cardapio;
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
