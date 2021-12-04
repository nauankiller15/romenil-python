import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { ApiService } from 'src/app/shared/api-service/api.service';
import { Erro } from 'src/app/shared/erros';

@Component({
  selector: 'app-trocar-senha',
  templateUrl: './trocar-senha.component.html',
  styleUrls: ['./trocar-senha.component.css']
})
export class TrocarSenhaComponent implements OnInit {

  dados = {
    id: 0,
    old_password: '',
    password1: '',
    password2: '',
  }

  constructor(
    private accountService: AccountService,
    private apiService: ApiService,
    private toastrService: ToastrService,
    private router: Router
    ) { }

  ngOnInit(): void {
  }

  mudarSenha() {
    this.dados.id = this.accountService.getId();
    this.apiService.atualizar('conta/mudar-senha', this.dados).subscribe(
      (data) => {
        window.localStorage.removeItem('token');
        this.toastrService.success('Dados atualizados com sucesso.');
        this.router.navigate(['/login']);
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
