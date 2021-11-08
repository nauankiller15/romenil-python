import { Component, OnInit } from '@angular/core';

declare var $: any;

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  ativo = 'dashboard';

  constructor() { }

  ngOnInit(): void {
    $('body').addClass('noborder');
  }
}
