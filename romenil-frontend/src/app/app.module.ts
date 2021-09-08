import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { LoginComponent } from './account/login/login.component';
import { CreateAccountComponent } from './account/create-account/create-account.component';
import { AuthenticationComponent } from './account/authentication/authentication.component';
import { CardapiosComponent } from './cardapios/cardapios.component';
import { FormularioComponent } from './formulario/formulario.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { AuthTokenInterceptor } from './shared/http-interceptor/auth-token.interceptor';

import { NgxLoadingModule } from 'ngx-loading';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    CalculadoraComponent,
    LoginComponent,
    CreateAccountComponent,
    AuthenticationComponent,
    CardapiosComponent,
    FormularioComponent,
    WelcomeComponent,
    TopBarComponent,
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    NgxLoadingModule.forRoot({}),
    ToastrModule.forRoot({
      timeOut: 3800,
      extendedTimeOut: 3500,
      closeButton: true,
      positionClass: 'toast-bottom-right',
      enableHtml: true,
      progressBar: true,
    }),
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthTokenInterceptor, multi: true },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
