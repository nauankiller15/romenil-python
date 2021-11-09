import { Component, OnInit } from '@angular/core';
import { Usuario } from './models';

declare var $: any;

@Component({
  selector: 'app-permissoes',
  templateUrl: './permissoes.component.html',
  styleUrls: ['./permissoes.component.css']
})
export class PermissoesComponent implements OnInit {

  pagina = 'permissoes';
  usuarios: Usuario[] = [
    {
      id: 1,
      first_name: 'João guilherme',
      last_name: 'matos',
      email: 'email',
      cargo: 'desenvolvedor',
    },
    {
      id: 2,
      first_name: 'maria vitoria',
      last_name: 'matos',
      email: 'email',
      cargo: 'administrador',
    },
  ];
  selectedUsuario: Usuario = new Usuario;


  constructor() { }

  ngOnInit(): void {
    $('body').addClass('noborder');
  }

  editar(usuario: Usuario) {
    console.log(usuario);
  }

  excluir(usuario: Usuario) {
    console.log(usuario);
  }
}
