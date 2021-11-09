import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard-base',
  templateUrl: './dashboard-base.component.html',
  styleUrls: ['./dashboard-base.component.css']
})
export class DashboardBaseComponent implements OnInit {
  @Input() pagina = '';
  
  constructor() { }

  ngOnInit(): void {
  }

}
