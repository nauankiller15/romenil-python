import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { MustMatch } from './must-match.service';

import { Conta, Usuario } from '../models';

import { Erro } from 'src/app/shared/erros';

declare var $: any;

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css'],
})
export class CreateAccountComponent implements OnInit {
  conta = new Conta();
  usuario = new Usuario();
  pagina = 'conta';
  loading = false;

  constructor(
    private toastrService: ToastrService,
    private accountService: AccountService,
    private router: Router
  ) {
    if (this.accountService.autenticado()) {
      this.accountService.usuario().subscribe((data) => {
        if (data.usuario) {
          this.router.navigate(['/formulario']);
        } else {
          this.pagina = 'usuario';
        }
      });
    }
  }

  ngOnInit(): void {
    $(document).ready(() => {
      $('.celular').mask('(00) 00000-0000');
      $('.cpf').mask('000.000.000-00', { reverse: false });
    });
    $('body').addClass('noborder');
  }

  voltar() {
    this.pagina = 'conta';
  }

  validarDocumento() {

  }
  
  onSubmit() {
    this.loading = true;
    this.accountService.createAccount(this.conta).subscribe(
      (data) => {
        this.conta = data;
        this.toastrService.success('Conta criada com sucesso');
        this.router.navigate(['/login']);
      },
      (error) => {
        this.loading = false;
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  onSubmitUsuario() {
    this.loading = true;
    this.accountService.createUser(this.usuario).subscribe(
      (data) => {
        this.toastrService.success('Dados cadastrados com sucesso!');
        this.router.navigate(['/formulario']);
      },
      (error) => {
        this.loading = false;
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
