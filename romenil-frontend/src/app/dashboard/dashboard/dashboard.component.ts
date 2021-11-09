import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { Erro } from 'src/app/shared/erros';
import { Conta } from '../models';

declare var $: any;

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  pagina = 'dashboard';
  conta = new Conta

  constructor(
    private accountService: AccountService,
    private router: Router,
    private toastrService: ToastrService
  ) {
    this.getConta();
  }

  ngOnInit(): void {
    $('body').addClass('noborder');
  }

  getConta() {
    this.accountService.conta().subscribe(
      (data) => {
        this.conta = data;
        if (!(['desenvolvedor','administrador'].includes(this.conta.perfil))) {
          this.router.navigate(['dashboard/nao-autorizado']);
        } else {
          console.log(this.conta.perfil)
        }
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
