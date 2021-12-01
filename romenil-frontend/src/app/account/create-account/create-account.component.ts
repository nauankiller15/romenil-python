import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { MustMatch } from './must-match.service';

import { Conta } from '../models';

import { Erro } from 'src/app/shared/erros';

declare var $: any;

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css'],
})
export class CreateAccountComponent implements OnInit {
  conta = new Conta();
  loading = false;

  constructor(
    private toastrService: ToastrService,
    private accountService: AccountService,
    private router: Router
  ) {
    if (this.accountService.autenticado()) {
      this.accountService.usuario().subscribe(
        (data) => {
          if (data.user) {
            if (data.ativo == true) {
              this.router.navigate(['/welcome_exclusive']);
            } else {
              this.router.navigate(['/welcome']);
            }
          }
        },
        (error) => {
          this.loading = false;
          const erro = new Erro(this.toastrService, error);
          erro.exibir();
        }
      );
    }
  }

  ngOnInit(): void {
    $('body').addClass('noborder');

    $('#closeGenerate').on('click', function () {
      $('#generateCard').slideUp(350);
    });
    
  }

  onSubmit() {
    $('#generateCard').slideDown(450);
  }
    
  criarConta() {
    this.loading = true;
    this.accountService.createAccount(this.conta).subscribe(
      (data) => {
        this.conta = data;
        this.toastrService.success('Conta criada com sucesso');
        this.loading = false;
        this.router.navigate(['/login']);
      },
      (error) => {
        this.loading = false;
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
