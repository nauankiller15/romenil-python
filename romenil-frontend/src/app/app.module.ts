import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { NgxLoadingModule } from 'ngx-loading';
import { NgxMaskModule } from 'ngx-mask';
import { ToastrModule } from 'ngx-toastr';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';

import { LoginComponent } from './account/login/login.component';
import { CreateAccountComponent } from './account/create-account/create-account.component';
import { CardapiosComponent } from './cardapios/cardapios.component';
import { FormularioComponent } from './formulario/formulario.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { AguardeComponent } from './aguarde/aguarde.component';
import { ConversaoComponent } from './conversao/conversao.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { WelcomePagoComponent } from './welcome-pago/welcome-pago.component';

import { AuthTokenInterceptor } from './shared/http-interceptor/auth-token.interceptor';
import { AuthGuardService } from './shared/guards/auth-guard/auth.guard';
import { EscapeHtmlPipe } from './shared/pipes/keep-html.pipe';

import { DashboardBaseComponent } from './dashboard/base/dashboard-base/dashboard-base.component';
import { SidebarComponent } from './dashboard/base/sidebar/sidebar.component';
import { DashboardComponent } from './dashboard/dashboard/dashboard.component';
import { DashboardCardapiosComponent } from './dashboard/dashboard-cardapios/dashboard-cardapios.component';
import { PermissoesComponent } from './dashboard/permissoes/permissoes.component';
import { NaoAutorizadoComponent } from './dashboard/nao-autorizado/nao-autorizado.component';
import { UsuarioComponent } from './account/usuario/usuario.component';
import { ProfileComponent } from './account/profile/profile.component';
import { TrocarSenhaComponent } from './account/trocar-senha/trocar-senha.component';

import { NgxSkeletonLoaderModule } from 'ngx-skeleton-loader';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    CalculadoraComponent,
    LoginComponent,
    CreateAccountComponent,
    CardapiosComponent,
    FormularioComponent,
    WelcomeComponent,
    TopBarComponent,
    ConversaoComponent,
    EscapeHtmlPipe,
    AguardeComponent,
    WelcomePagoComponent,
    DashboardComponent,
    SidebarComponent,
    DashboardBaseComponent,
    DashboardCardapiosComponent,
    PermissoesComponent,
    NaoAutorizadoComponent,
    UsuarioComponent,
    ProfileComponent,
    TrocarSenhaComponent,
  ],
  imports: [
    NgxSkeletonLoaderModule.forRoot(),
    MatProgressBarModule,
    BrowserAnimationsModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    ToastrModule.forRoot({
      timeOut: 3800,
      extendedTimeOut: 3500,
      closeButton: true,
      positionClass: 'toast-top-center',
      enableHtml: true,
      progressBar: true,
    }),
    NgxLoadingModule.forRoot({}),
    NgxMaskModule.forRoot(),
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthTokenInterceptor, multi: true },
    AuthGuardService,
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
