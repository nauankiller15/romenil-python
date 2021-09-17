import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { Erro } from '../shared/erros';
declare var $: any;

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
})
export class FormularioComponent implements OnInit {

  conta = new Conta();

  constructor(
    private router: Router, 
    private accountService: AccountService,
    private toastrService: ToastrService,
  ) {
    this.verificarDados();
  }

  ngOnInit(): void {
    $('#fecharBtForm').on('click', function () {
      $('#formulario').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }

  verificarDados() {
    if (this.accountService.autenticado()) {
      this.getConta();
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
        this.getUsuario();
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}