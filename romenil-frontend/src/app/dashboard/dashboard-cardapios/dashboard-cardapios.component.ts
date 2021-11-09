import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { CardapioCompleto, Cardapios, CardapiosCompletos } from 'src/app/cardapios/modelos';
import { ApiService } from 'src/app/shared/api-service/api.service';
import { Erro } from 'src/app/shared/erros';

declare var $: any;

@Component({
  selector: 'app-dashboard-cardapios',
  templateUrl: './dashboard-cardapios.component.html',
  styleUrls: ['./dashboard-cardapios.component.css']
})
export class DashboardCardapiosComponent implements OnInit {

  pagina = 'cardapios';
  todosCardapios: CardapioCompleto[] = [];
  cardapios = new CardapiosCompletos();
  principais = [['DI', 'Diabetes'], ['HI', 'Hipertensao'], ['NP', 'Nenhuma Patologia principal']];
  secundarias = [['ML', 'Metabolismo Lento'], ['CO', 'Constipação'], ['IN', 'Insônia'], ['CE', 'Colesterol Elevado'], ['AN', 'Ansiedade'], ['RL', 'Retensão Liquida'], ['CL', 'Celíaco'], ['NP', 'Nenhuma Patologia secundária']];
  patologiaPrincipal = 'DI';
  patologiaSecundaria = "ML"
  
  constructor(
    private apiService: ApiService,
    private toastrService: ToastrService,
  ) { 
    this.getCardapios();
  }

  ngOnInit(): void {
    $('body').addClass('noborder');
  }

  getCardapios() {
    this.apiService.listar('dashboard/cardapios').subscribe(
      (data) => {
        this.todosCardapios = data;
        this.setCardapio();
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }

  selectPrincipal(codigo: string) {
    console.log('selectPrincipal', codigo)
    this.patologiaPrincipal = codigo;
    this.setCardapio();
  }

  selectSecundaria(codigo: string) {
    console.log('selectSecundaria', codigo)
    this.patologiaSecundaria = codigo;
    this.setCardapio();
  }

  setCardapio() {
    let principal = this.patologiaPrincipal;
    let secundaria = this.patologiaSecundaria;
    if (principal != 'NP' && secundaria == 'RL') {
      secundaria = 'NP'
    }

    this.cardapios = new CardapiosCompletos;
    for (let cardapio in this.todosCardapios) {
      if (this.todosCardapios[cardapio].principal == principal && this.todosCardapios[cardapio].secundaria == secundaria) {
        if (this.todosCardapios[cardapio].refeicao == 0) {
          this.cardapios.desjejum.push(this.todosCardapios[cardapio]);
        } else if (this.todosCardapios[cardapio].refeicao == 1) {
          this.cardapios.cafeManha.push(this.todosCardapios[cardapio]);
        } else if (this.todosCardapios[cardapio].refeicao == 2) {
          this.cardapios.refeicao2.push(this.todosCardapios[cardapio]);
        } else if (this.todosCardapios[cardapio].refeicao == 3) {
          this.cardapios.almoco.push(this.todosCardapios[cardapio]);
        } else if (this.todosCardapios[cardapio].refeicao == 4) {
          this.cardapios.refeicao4.push(this.todosCardapios[cardapio]);
        } else if (this.todosCardapios[cardapio].refeicao == 5) {
          this.cardapios.janta.push(this.todosCardapios[cardapio]);
        } else if (this.todosCardapios[cardapio].refeicao == 6) {
          this.cardapios.refeicao6.push(this.todosCardapios[cardapio]);
        }
      }
    }
    console.log(this.cardapios);
  }
}
