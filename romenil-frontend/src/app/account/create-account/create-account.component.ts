import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';

import { Conta, Usuario } from '../models';

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
  ) {
    if (this.accountService.autenticado()) {
      this.accountService.usuario().subscribe((data) => {
        if (data.usuario) {
          this.router.navigate(['/welcome']);
        } else {
          this.pagina = 'usuario';
        }
      });
    }
  }

  ngOnInit(): void {
    $('body').addClass('noborder');
  }

  voltar() {
    this.pagina = 'conta';
  }
  
  onSubmit() {
    this.loading = true;
    this.accountService.createAccount(this.conta).subscribe(
      (data) => {
        this.conta = data;
        this.toastr.success('Conta criada com sucesso');
        this.router.navigate(['/login']);
      },
      (error) => {
        this.loading = false;
        this.toastr.error('Erro na criação da conta');
      }
    );
  }

  onSubmitUsuario() {
    this.loading = true;
    this.accountService.createUser(this.usuario).subscribe(
      (data) => {
        this.toastr.success('Dados cadastrados com sucesso!');
        this.router.navigate(['/welcome']);
      },
      (error) => {
        this.loading = false;
        this.toastr.error('Erro no complemento dos dados');
      }
    );
  }
}
