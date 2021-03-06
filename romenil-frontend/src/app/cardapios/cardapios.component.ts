import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { ApiService } from '../shared/api-service/api.service';
import { Erro } from '../shared/erros';
import { Cardapios } from './modelos';
declare var $: any;

@Component({
  selector: 'app-cardapios',
  templateUrl: './cardapios.component.html',
  styleUrls: ['./cardapios.component.css'],
})
export class CardapiosComponent implements OnInit {
  conta = new Conta();
  cardapios = new Cardapios();
  public loading = false;

  // CARREGADOR NG SKELETON
  animation = 'pulse';
  contentLoaded = false;
  contentLoadedPerfil = false;
  count = 10;
  widthHeightSizeInPixels = 50;

  intervalId: number | null = null;
  //

  constructor(
    private accountService: AccountService,
    private apiService: ApiService,
    private toastrService: ToastrService,
    private router: Router
  ) {
    this.getDados();
  }

  ngOnInit(): void {
    // SKELETON LOADER
    this.intervalId = window.setInterval(() => {
      this.animation = this.animation === 'pulse' ? 'progress-dark' : 'pulse';
      this.count = this.count === 4 ? 5 : 4;
      this.widthHeightSizeInPixels =
        this.widthHeightSizeInPixels === 50 ? 100 : 50;
    }, 5000);
    //---------------

    $(document).ready(function () {
      $('.loader-wrapper').fadeIn(250).delay(1200).fadeOut(250);
    });
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
        if (data.user) {
          if (data.ativo) {
            this.getConta();
            this.getCardapios();
          } else {
            this.router.navigate(['conversao']);
          }
        } else {
          this.router.navigate(['criar-usuario']);
        }
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  getConta() {
    this.contentLoadedPerfil = true;
    this.accountService.conta().subscribe(
      (data) => {
        this.conta = data;
      },
      (error) => {
        this.contentLoadedPerfil = false;
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  getCardapios() {
    this.apiService.listar('cardapio').subscribe(
      (data) => {
        if (data.pronto == true) {
          this.contentLoaded = true;
          let dados = data.dados;
          for (let cardapio in dados) {
            if (dados[cardapio].refeicao == 0) {
              this.cardapios.desjejum.push(dados[cardapio].prato);
            } else if (dados[cardapio].refeicao == 1) {
              this.cardapios.cafeManha.push(dados[cardapio].prato);
            } else if (dados[cardapio].refeicao == 2) {
              this.cardapios.refeicao2.push(dados[cardapio].prato);
            } else if (dados[cardapio].refeicao == 3) {
              this.cardapios.almoco.push(dados[cardapio].prato);
            } else if (dados[cardapio].refeicao == 4) {
              this.cardapios.refeicao4.push(dados[cardapio].prato);
            } else if (dados[cardapio].refeicao == 5) {
              this.cardapios.janta.push(dados[cardapio].prato);
            } else if (dados[cardapio].refeicao == 6) {
              this.cardapios.refeicao6.push(dados[cardapio].prato);
            }
          }
        } else {
          if (data.completed_form == true) {
            this.router.navigate(['aguarde']);
          } else {
            this.router.navigate(['formulario']);
          }
        }
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  enviarEmail() {
    $('.loaderBtn').fadeIn(200);
    this.loading = true;
    this.apiService.salvar('cardapio/via-email', null).subscribe(
      (data) => {
        $('.loaderBtn').fadeOut(200);
        this.loading = false;
        console.log(data);
        this.toastrService.success('Cardápio enviado para o seu Email!');
      },
      (error) => {
        $('.loaderBtn').fadeOut(200);
        this.loading = false;
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
