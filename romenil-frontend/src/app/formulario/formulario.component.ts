import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { ApiService } from '../shared/api-service/api.service';
import { Erro } from '../shared/erros';
import { Formulario } from './models';
declare var $: any;

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
})
export class FormularioComponent implements OnInit {
  conta = new Conta();
  formulario = new Formulario();
  editavel = true;

  constructor(
    private apiService: ApiService,
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router
  ) {
    this.verificarDados();
  }

  ngOnInit(): void {
    $(document).ready(function () {
      $('.loader-wrapper').fadeIn(250).delay(2000).fadeOut(450);
    });
    $('#fecharBtForm').on('click', function () {
      $('#formulario').fadeOut('100');
      $('body').removeClass('noborder');

    });

    // BOTÃO DE ABRIR TELA DE CONFIRMAÇÃO DE GERAR CARDÁPIO
    $('#gerarCardap').on('click', function () {
      $('#generateCard').slideDown(550);
    });
    // BOTÃO DE FECHAR TELA DE CONFIRMAÇÃO DE GERAR CARDÁPIO
    $('#closeGenerate').on('click', function () {
      $('#generateCard').slideUp(650);
    });
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
        if (data.user) {
          if (data.ativo) {
            this.getConta();
            this.getFormulario();
          } else {
            this.router.navigate(['conversao']);
          }
        } else {
          this.router.navigate(['/criar-usuario']);
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
          this.formulario = data;

          let data_form = new Date(this.formulario.modificado_em);
          data_form.setDate(data_form.getDate() + 20);
          let agora = new Date();

          this.editavel = agora >= data_form;
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

  salvarFormulario() {
    this.apiService.salvar('formulario', this.formulario).subscribe(
      (data) => {
        this.router.navigate(['aguarde']);
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
