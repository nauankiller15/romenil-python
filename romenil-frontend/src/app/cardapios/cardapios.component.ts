import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { ApiService } from '../shared/api-service/api.service';
import { Erro } from '../shared/erros';
import { Cardapio, Cardapios } from './modelos';
declare var $: any;

@Component({
  selector: 'app-cardapios',
  templateUrl: './cardapios.component.html',
  styleUrls: ['./cardapios.component.css'],
})
export class CardapiosComponent implements OnInit {
  conta = new Conta();
  cardapios = new Cardapios();

  constructor(
    private accountService: AccountService,
    private apiService: ApiService,
    private toastrService: ToastrService,
    private router: Router
  ) {
    this.getDados();
  }

  ngOnInit(): void {
    $('#fecharBtCardp').on('click', function () {
      $('#cardapio').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');

    // BOTÃO DE PRINTAR A PÁGINA DE CARDÁPIO
    $('#printer').on('click', () => {
      var conteudo = document.getElementById('print')!.innerHTML;
      const tela_impressao = window.open('about:blank');
      var myStyle =
        '<link rel="stylesheet" href="./assets/static/CSS/cardapio.css" />';
      tela_impressao!.document.write(myStyle + '#print');
      tela_impressao!.document.write(conteudo);
      tela_impressao!.document.write(
        '<link rel="stylesheet" href="./assets/static/CSS/cardapio.css" type="text/css" />'
      );
      tela_impressao!.window.print();
      tela_impressao!.window.close();
    });
    //
  }

  getDados() {
    this.apiService.listar('conta/usuario').subscribe(
      (data) => {
        if (data && data.ativo) {
            this.getConta();
            this.getCardapios();
        } else {
          this.router.navigate(['conversao'])
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

  getCardapios() {
    this.apiService.listar('cardapio').subscribe(
      (data) => {
        if (data) {
          for (let cardapio in data) {
            if (data[cardapio].refeicao == 0) {
              this.cardapios.desjejum.push(data[cardapio].prato);
            } else if (data[cardapio].refeicao == 1) {
              this.cardapios.cafeManha.push(data[cardapio].prato);
            } else if (data[cardapio].refeicao == 2) {
              this.cardapios.refeicao2.push(data[cardapio].prato);
            } else if (data[cardapio].refeicao == 3) {
              this.cardapios.almoco.push(data[cardapio].prato);
            } else if (data[cardapio].refeicao == 4) {
              this.cardapios.refeicao4.push(data[cardapio].prato);
            } else if (data[cardapio].refeicao == 5) {
              this.cardapios.janta.push(data[cardapio].prato);
            } else if (data[cardapio].refeicao == 6) {
              this.cardapios.refeicao6.push(data[cardapio].prato);
            }
          }
        } else {
          this.router.navigate(['formulario'])
        }
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
