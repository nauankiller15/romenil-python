import { Component, OnInit, ViewChild, ViewContainerRef } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { ApiService } from '../shared/api-service/api.service';
import { Erro } from '../shared/erros';
declare var $: any;

@Component({
  selector: 'app-cardapios',
  templateUrl: './cardapios.component.html',
  styleUrls: ['./cardapios.component.css'],
})
export class CardapiosComponent implements OnInit {

  cardapio = ''
 
  constructor(private apiService: ApiService, private toastrService: ToastrService) {
    this.getCardapio()
  }

  ngOnInit(): void {
    $('#fecharBtCardp').on('click', function () {
      $('#cardapio').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }

  getCardapio() {
    this.apiService.listar('cardapio').subscribe(
      (data) => {
        this.cardapio = data.cardapio;
      },
      (error) => {
        const erro = new Erro(this.toastrService, error);
        erro.exibir();
      }
    );
  }
}
