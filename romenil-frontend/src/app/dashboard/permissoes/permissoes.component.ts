import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { ApiService } from 'src/app/shared/api-service/api.service';
import { Erro } from 'src/app/shared/erros';
import { Conta } from '../models';
import { Cargo, Usuario } from './models';

declare var $: any;

@Component({
  selector: 'app-permissoes',
  templateUrl: './permissoes.component.html',
  styleUrls: ['./permissoes.component.css']
})
export class PermissoesComponent implements OnInit {

  pagina = 'permissoes';
  conta = new Conta;
  cargos: Cargo[] = [];
  usuarios: Usuario[] = [
    {
      id: 1,
      first_name: 'João guilherme',
      last_name: 'matos',
      email: 'email',
    },
    {
      id: 2,
      first_name: 'maria vitoria',
      last_name: 'matos',
      email: 'email',
    },
  ];
  selectedUsuario: Usuario = new Usuario;


  constructor(
    private accountService: AccountService,
    private apiService: ApiService,
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
          this.getCargos();
        }
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  getCargos() {
    this.apiService.listar('permissoes/listar').subscribe(
      (data) => {
        this.cargos = data;
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  editar(usuario: Usuario) {
    console.log(usuario);
  }

  excluir(usuario: Usuario) {
    console.log(usuario);
  }
}
