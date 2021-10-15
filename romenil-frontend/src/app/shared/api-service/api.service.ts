import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private readonly baseUrl = environment.baseUrl;
  private httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json'});
  private httpHeaders2 = new HttpHeaders({ 'Content-Type': 'text/html'});
  

  constructor(private httpClient: HttpClient) {}

  listar(url: string): Observable<any> {
    return this.httpClient.get(this.baseUrl + url +'/', {
      headers: this.httpHeaders,
    });
  }

  getHtml(url: string): Observable<any> {
    return this.httpClient.get(this.baseUrl + url +'/', {
      responseType: 'text',
      headers: this.httpHeaders2,
    });
  }

  salvar(url: string, dados: any): Observable<any> {
    return this.httpClient.post(this.baseUrl + url +'/', dados, {
      headers: this.httpHeaders,
    });
  }
}
