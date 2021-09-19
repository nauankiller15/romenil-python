import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { Erro } from '../shared/erros';
import { Calculadora } from '../calculadora/models';

declare var $: any;

@Component({
  selector: 'app-calculadora',
  templateUrl: './calculadora.component.html',
  styleUrls: ['./calculadora.component.css'],
})
export class CalculadoraComponent implements OnInit {

  conta = new Conta();
  calculadora = {} as Calculadora;
  imc = 0;
  diagnostico = '';
  maintenance = 0;
  loseWeight = 0;
  gainWeight = 0;

  constructor(private accountService: AccountService, private toastrService:ToastrService) { 
    this.getConta();
  }

  ngOnInit(): void {
    $('#fecharBtCalc').on('click', function () {
      $('#calculadora').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
    //
    $('#calculated').on('click', function () {
      $('#calculadoraForm').fadeOut(350);
      $('#resultados').slideDown(350);
      $('.cardBtn').slideDown(250);
    });
    $('#refazerIMC').on('click', function () {
      $('#calculadoraForm').slideDown(450);
      $('#resultados').slideUp(450);
      $('.cardBtn').slideDown(250);
    });
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

  calcularIMC() {
    this.imc = this.calculadora.peso / (this.calculadora.altura * this.calculadora.altura/10000);

    if (this.imc < 18.5) {
      this.diagnostico = 'abaixo do peso';
    } else if (this.imc >= 18.5 && this.imc < 25) {
      this.diagnostico = 'peso ideal';
    } else if (this.imc >= 25 && this.imc < 30) {
      this.diagnostico = 'sobrepeso';
    } else if (this.imc >= 30 && this.imc < 35) {
      this.diagnostico = 'obesidade leve';
    } else if (this.imc >= 35 && this.imc < 40) {
      this.diagnostico = 'obesidade severa';
    } else {
      this.diagnostico = 'obesidade mórbida';
    }
  }

  calcularTMB() {
    const tmb = Math.round(
      this.calculadora.sexo == 'male'
      ? 66 + (13.8 * this.calculadora.peso) + (5 * this.calculadora.altura) - (6.8 * this.calculadora.idade)
      : 655 + (9.6 * this.calculadora.peso) + (1.8 * this.calculadora.altura) - (4.7 * this.calculadora.idade)
    );
          
    this.maintenance = Math.round(tmb * Number(this.calculadora.nivel_atividade));
    this.loseWeight = this.maintenance - 450;
    this.gainWeight = this.maintenance + 450;
}

  submit() {
    this.calcularIMC();
    this.calcularTMB();
    $('#resultados').fadeIn(250);
  }
}
