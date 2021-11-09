import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { AccountService } from '../../account-service/account.service';
@Injectable()
export class AuthGuardService implements CanActivate {
  constructor(
    private accountService: AccountService, 
    private router: Router
  ) {}
  canActivate(): boolean {

    if (this.accountService.autenticado()) {
      return true
    } else {
      this.router.navigate(['login']);
      return false;
    }
  }
}
