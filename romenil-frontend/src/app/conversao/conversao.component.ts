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
  styleUrls: ['./conversao.component.css']
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
    $('#fecharBtConversao').on('click', function () {
      $('#conversao').fadeOut('100');
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

  getConta() {
    this.accountService.conta().subscribe(
      (data) => {
        this.conta = data;
        console.log(this.conta)
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

}
