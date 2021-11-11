import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { ApiService } from '../shared/api-service/api.service';
import { Erro } from '../shared/erros';

declare var $: any;

@Component({
  selector: 'app-aguarde',
  templateUrl: './aguarde.component.html',
  styleUrls: ['./aguarde.component.css'],
})
export class AguardeComponent implements OnInit {
  conta = new Conta();
  data_form = new Date();
  timer = { horas: 0, minutos: 0, segundos: 0 };
  time = 0;
  intervalo: any = null;

  constructor(
    private apiService: ApiService,
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router
  ) {
    this.getUsuario();
  }

  ngOnInit(): void {
    $(document).ready(function () {
      $('.loader-wrapper').fadeIn(250).delay(1000).fadeOut(250);
    });
    $('#fecharBtAguarde').on('click', function () {
      $('#aguarde').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }

  getUsuario() {
    this.accountService.usuario().subscribe(
      (data) => {
        if (!data.usuario) {
          this.router.navigate(['/create-account']);
        } else if (data.ativo) {
          this.getConta();
          this.getFormulario();
        } else {
          this.router.navigate(['conversao']);
        }
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  getFormulario() {
    this.apiService.listar('formulario').subscribe(
      (data) => {
        if (data) {
          let agora = new Date();
          this.data_form = new Date(data.modificado_em);
          let atualizacao = new Date(data.modificado_em);
          this.time =
            2 * 3600 - (agora.valueOf() - atualizacao.valueOf()) / 1000 + 1;
          this.intervalo = setInterval(() => {
            this.getTimer();
          }, 1000);
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

  getTimer() {
    this.time--;
    console.log(this.time);
    this.timer.horas = Math.floor(this.time / 3600);
    this.timer.minutos = Math.floor((this.time % 3600) / 60);
    this.timer.segundos = Math.floor((this.time % 3600) % 60);

    if (this.time <= 1) {
      this.router.navigate(['cardapios']);
    }
  }
}
