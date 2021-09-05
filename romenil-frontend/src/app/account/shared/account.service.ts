import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
// import jwtDecode from 'jwt-decode';
// import { ToastrService } from 'ngx-toastr';
import { environment } from 'src/environments/environment';
import { Login } from '../login/models';


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

  async login(usuario: Login) {
    const resp = this.httpClient.post(this.baseUrl + 'login/', usuario).subscribe(
      data => {
        console.log('success', data);
        return data;
      },
      error => {
        console.log('oops', error);
        return error;
      }
    );

    // const resp = await this.http.post(this.baseUrl + 'login/', usuario, {
    //   headers: this.httpHeaders,
    // }).toPromise();
    
    // if (resp && resp.token) {
    //   localStorage.setItem('token', resp['token']);
    //   return true;
    // }
    // return false;
    return resp
  }

  createAccount(account: any) {
    return new Promise((resolve) => {
      resolve(true);
    });
  }
}
