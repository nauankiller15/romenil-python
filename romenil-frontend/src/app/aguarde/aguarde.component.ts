import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'app-aguarde',
  templateUrl: './aguarde.component.html',
  styleUrls: ['./aguarde.component.css']
})
export class AguardeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    $('#fecharBtAguarde').on('click', function () {
      $('#aguarde').fadeOut('100');
      $('body').removeClass('noborder');
    });
    $('body').addClass('noborder');
  }

}
