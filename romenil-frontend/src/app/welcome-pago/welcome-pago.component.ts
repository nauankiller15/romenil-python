import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Conta } from '../account/models';
import { AccountService } from '../shared/account-service/account.service';
import { Erro } from '../shared/erros';
declare var $: any;

@Component({
  selector: 'app-welcome-pago',
  templateUrl: './welcome-pago.component.html',
  styleUrls: ['./welcome-pago.component.css'],
})
export class WelcomePagoComponent implements OnInit {

  constructor(
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router
  ) {}

  ngOnInit(): void {
    $('#fecharBtWelcomePago').on('click', function () {
      $('#bemvindo-pago').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }
}
