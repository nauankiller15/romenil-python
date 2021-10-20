import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { ApiService } from '../shared/api-service/api.service';
import { Erro } from '../shared/erros';
import { Alergia, Patologia, EstiloVida } from './models';
declare var $: any;

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
})
export class FormularioComponent implements OnInit {

  conta = new Conta();
  patologia = new Patologia; 
  alergia = new Alergia; 
  estiloVida = new EstiloVida; 

  constructor(
    private apiService: ApiService,
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router, 
  ) {
    this.verificarDados();
  }

  ngOnInit(): void {
    $('#fecharBtForm').on('click', function () {
      $('#formulario').fadeOut('100');
      $('body').removeClass('noborder');
    });

    // BOTÃO DE ABRIR TELA DE CONFIRMAÇÃO DE GERAR CARDÁPIO
    $('#gerarCardap').on('click', function () {
      $('#generateCard').fadeIn(250);
    });
      // BOTÃO DE FECHAR TELA DE CONFIRMAÇÃO DE GERAR CARDÁPIO
      $('#closeGenerate').on('click', function () {
        $('#generateCard').fadeOut(250);
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
        if (!data.usuario) {
          this.router.navigate(['/create-account']);
        } else if (data.ativo) {
          this.getConta();
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

  salvarFormulario() {
    this.apiService.salvar('formulario/patologia', this.patologia).subscribe(
      (data) => {
        this.router.navigate(['cardapios'])
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}