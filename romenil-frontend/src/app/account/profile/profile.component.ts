import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { ApiService } from 'src/app/shared/api-service/api.service';
import { Erro } from 'src/app/shared/erros';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  conta = {
    id: 0,
    first_name: '',
    last_name: '',
    email: '',
    username: '',
  }

  usuario = {
    cpf_ou_cnpj: '',
  }

  constructor(
    private accountService: AccountService,
    private apiService: ApiService,
    private toastrService: ToastrService,
  ) { 
    this.getUsuario();
    this.getConta();
  }

  ngOnInit(): void {
  }

  getUsuario() {
    this.apiService.listar('conta/usuario').subscribe(
      (data) => {
        if (data.user) {
          this.usuario = data;
        } else {
          this.usuario.cpf_ou_cnpj = 'Não cadastrado';
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

  atualizarDados() {
    this.conta.username = this.conta.email;
    this.apiService.atualizar('conta/atualizar', this.conta).subscribe(
      (data) => {
        this.toastrService.success('Dados atualizados com sucesso.');
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
