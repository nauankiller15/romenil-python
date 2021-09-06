import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
// import jwtDecode from 'jwt-decode';
// import { ToastrService } from 'ngx-toastr';
import { environment } from 'src/environments/environment';
import { Conta, Login, Usuario } from '../models';


// @Injectable({
//   providedIn: 'root'
// })
// export class AuthService {
  
//   
  
//   constructor() {}
  
//   async autenticar

//   autenticado() {
//     const token = this.getAuthorizationToken();
    
//     if (token) {
//       const expirado = this.tokenExpirado(token);
//       if (!expirado) {
//         return true;
//       } else {
//         localStorage.removeItem('token');
//       }
//     }
//     localStorage.removeItem('token');
//     return false;
//   }

//   getAuthorizationToken() {
//     const token = localStorage.getItem('token');
//     return token;
//   }

//   tokenExpirado(token: string) {
//     const tokenDecode = jwtDecode(token);
    
//     if (tokenDecode['exp']) {
//       const expiracao = tokenDecode['exp']
//       const dataExpiracao = new Date(0);
//       dataExpiracao.setUTCSeconds(expiracao);

//       if ( dataExpiracao.valueOf() < new Date().valueOf()) {
//         return true;
//       } else {
//         return false
//       }
//     }
//   }

//   getUserId() {
//     const token = this.getAuthorizationToken()
//     const tokenDecode = jwtDecode(token);

//     return tokenDecode['user_id']
//   }
// }




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
}
