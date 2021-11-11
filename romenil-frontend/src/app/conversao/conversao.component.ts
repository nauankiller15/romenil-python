import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { Erro } from '../shared/erros';
declare var $: any;

@Component({
  selector: 'app-conversao',
  templateUrl: './conversao.component.html',
  styleUrls: ['./conversao.component.css'],
})
export class ConversaoComponent implements OnInit {
  conta = new Conta();

  constructor(
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router
  ) {
    this.verificarDados();
  }

  ngOnInit(): void {
    $(document).ready(function () {
      $('.loader-wrapper').fadeIn(250).delay(1000).fadeOut(250);
    });
    $('body').addClass('noborder');

  }
  

  verificarDados() {
    if (this.accountService.autenticado()) {
      this.getUsuario();
    } else {
      this.router.navigate(['/login']);
    }
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
  getUsuario() {
    this.accountService.usuario().subscribe(
      (data) => {
        if (!data.usuario) {
          this.router.navigate(['/create-account']);
        } else if (data.ativo) {
          this.router.navigate(['formulario']);
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
}
