import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';
import { CreateAccountComponent } from './account/create-account/create-account.component';
import { LoginComponent } from './account/login/login.component';
import { CardapiosComponent } from './cardapios/cardapios.component';
import { FormularioComponent } from './formulario/formulario.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { AuthGuardService } from './shared/auth-guard/auth.guard';
import { ConversaoComponent } from './conversao/conversao.component';
import { AguardeComponent } from './aguarde/aguarde.component';
import { WelcomePagoComponent } from './welcome-pago/welcome-pago.component';
import { DashboardComponent } from './dashboard/dashboard/dashboard.component';
import { DashboardCardapiosComponent } from './dashboard/dashboard-cardapios/dashboard-cardapios.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'create-account', component: CreateAccountComponent },
  {
    path: 'dashboard',
    children: [
      {
        path: '', component: DashboardComponent, 
      },
      {
        path: 'cardapios', component: DashboardCardapiosComponent, 
      },
    ]
  },
    
  { path: '', component: AppComponent },
  {
    path: '',
    component: AppComponent,
    canActivate: [AuthGuardService],
    children: [
      { path: 'welcome', component: WelcomeComponent },
      { path: 'welcome_exclusive', component: WelcomePagoComponent },
      { path: 'calculadora', component: CalculadoraComponent },
      { path: 'cardapios', component: CardapiosComponent },
      { path: 'formulario', component: FormularioComponent },
      { path: 'conversao', component: ConversaoComponent },
      { path: 'aguarde', component: AguardeComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
