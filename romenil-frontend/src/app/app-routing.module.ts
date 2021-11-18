import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';
import { CreateAccountComponent } from './account/create-account/create-account.component';
import { LoginComponent } from './account/login/login.component';
import { CardapiosComponent } from './cardapios/cardapios.component';
import { FormularioComponent } from './formulario/formulario.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { AuthGuardService } from './shared/guards/auth-guard/auth.guard';
import { ConversaoComponent } from './conversao/conversao.component';
import { AguardeComponent } from './aguarde/aguarde.component';
import { WelcomePagoComponent } from './welcome-pago/welcome-pago.component';
import { DashboardComponent } from './dashboard/dashboard/dashboard.component';
import { DashboardCardapiosComponent } from './dashboard/dashboard-cardapios/dashboard-cardapios.component';
import { PermissoesComponent } from './dashboard/permissoes/permissoes.component';
import { NaoAutorizadoComponent } from './dashboard/nao-autorizado/nao-autorizado.component';
import { UsuarioComponent } from './account/usuario/usuario.component';
import { ProfileComponent } from './account/profile/profile.component';
import { TrocarSenhaComponent } from './account/trocar-senha/trocar-senha.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'create-account', component: CreateAccountComponent },
  {
    path: 'dashboard',
    canActivate: [AuthGuardService],
    children: [
      { path: '', component: DashboardComponent },
      { path: 'cardapios', component: DashboardCardapiosComponent },
      { path: 'permissoes', component: PermissoesComponent },
      { path: 'nao-autorizado', component: NaoAutorizadoComponent },
    ],
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
      { path: 'criar-usuario', component: UsuarioComponent },
      { path: 'perfil', component: ProfileComponent },
      { path: 'trocar_senha', component: TrocarSenhaComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
