import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { Usuario } from '../models';
import { Erro } from 'src/app/shared/erros';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.css']
})
export class UsuarioComponent implements OnInit {

  usuario = new Usuario();
  loading = false;
  
  constructor(
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router
  ) {
    if (this.accountService.autenticado()) {
      this.accountService.usuario().subscribe((data) => {
        if (data.user) {
          if (data.ativo == true) {
            this.router.navigate(['/welcome_exclusive']);
          } else {
            this.router.navigate(['/welcome']);
          }
        }
      });
    }
  }

  ngOnInit(): void {
  }


  onSubmitUsuario() {
    this.loading = true;
    this.accountService.createUser(this.usuario).subscribe(
      (data) => {
        localStorage.removeItem('next')
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
