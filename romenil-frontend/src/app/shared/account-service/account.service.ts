import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import jwtDecode from 'jwt-decode';
import { environment } from 'src/environments/environment';
import { Conta, Login, Usuario } from 'src/app/account/models';


@Injectable({
  providedIn: 'root',
})
export class AccountService {

  private readonly baseUrl = environment.baseUrl + 'conta/';
  private httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json'});
  

  constructor(private httpClient: HttpClient, private router: Router) {}

  login(dados: Login): Observable<any> {
    return this.httpClient.post(this.baseUrl + 'login/', dados, {
      headers: this.httpHeaders,
    });
  }
     
  createAccount(dados: Conta): Observable<any> {
    return this.httpClient.post(this.baseUrl + 'criar-conta/', dados, {
      headers: this.httpHeaders,
    });
  }

  createUser(dados: Usuario): Observable<any> {
    return this.httpClient.post(this.baseUrl + 'criar-usuario/', dados, {
      headers: this.httpHeaders,
    });
  }

  conta(): Observable<any> {
    return this.httpClient.get(this.baseUrl + 'dados/', {
      headers: this.httpHeaders,
    });
  }

  usuario(): Observable<any> {
    return this.httpClient.get(this.baseUrl + 'usuario/', {
      headers: this.httpHeaders,
    });
  }

  private getAuthorizationToken() {
    const token = localStorage.getItem('token');
    if (token) {
      return token;
    } else {
      return ''
    }
  }

  private getDataToken(token: string): Token {
    let dataToken: Token = jwtDecode(token);
    return dataToken;
  }

  private tokenValido(token: string) {
    let dataToken = this.getDataToken(token);
    if (dataToken.exp) {
      const expiracao = dataToken.exp;
      const dataExpiracao = new Date(0);
      dataExpiracao.setUTCSeconds(expiracao);

      if ( dataExpiracao.valueOf() > new Date().valueOf()) {
        return true;
      }
    }
    return false;
  }    

  autenticado() {
    const token = this.getAuthorizationToken();
    
    if (token) {
      const tokenValido = this.tokenValido(token);
      if (tokenValido) {
        return true;
      } else {
        localStorage.removeItem('token');
      }
    }
    return false;
  }

  getId() {
    const token = this.getAuthorizationToken();
    if (token) {
      const dataToken = this.getDataToken(token);
      return dataToken.user_id;
    }
    return 0;
  }
}

interface Token {
  token: string;
  exp: number;
  user_id: number;
}