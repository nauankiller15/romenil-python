import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AccountService } from 'src/app/shared/account-service/account.service';
import { Erro } from 'src/app/shared/erros';
import { Conta } from '../../models';

@Component({
  selector: 'app-dashboard-base',
  templateUrl: './dashboard-base.component.html',
  styleUrls: ['./dashboard-base.component.css']
})
export class DashboardBaseComponent implements OnInit {
  @Input() pagina = '';
  
  constructor(
    private accountService: AccountService,
    private toastrService: ToastrService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }
}
