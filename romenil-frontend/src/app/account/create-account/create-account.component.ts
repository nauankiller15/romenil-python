import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

import { Conta, Usuario } from '../models';
import { AccountService } from '../shared/account.service';

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
    private toastr: ToastrService,
    private accountService: AccountService,
    private router: Router
  ) {}

  ngOnInit(): void {
    $('body').addClass('noborder');
  }

  onSubmit() {
    this.loading = true;
    this.accountService.createAccount(this.conta).subscribe(
      (data) => {
        this.conta = data;
        console.log(this.conta);
        this.usuario.usuario = this.conta.id;
        this.pagina = 'usuario';
        this.loading = false;
      },
      (error) => {
        this.toastr.error('Erro na criação da conta');
      }
    );
  }

  onSubmitUsuario() {
    this.loading = true;
    this.accountService.createUser(this.usuario).subscribe(
      (data) => {
        this.loading = false;
        this.router.navigate(['/login']);
        this.toastr.success('Dados cadastrados com sucesso!')
      },
      (error) => {
        this.toastr.error('Erro no complemento dos dados');
      }
    );
  }
}
