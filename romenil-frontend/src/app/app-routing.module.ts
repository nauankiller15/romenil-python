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
import { AdminComponent } from './account/admin/admin.component';
import { AguardeComponent } from './aguarde/aguarde.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'create-account', component: CreateAccountComponent },
  {
    path: 'admin',
    component: AdminComponent,
    // canActivate: [AuthGuardService],
  },
  { path: '', component: AppComponent },
  {
    path: '',
    component: AppComponent,
    canActivate: [AuthGuardService],
    children: [
      { path: 'welcome', component: WelcomeComponent },
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
