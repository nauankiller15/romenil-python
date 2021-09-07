import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';
import { CreateAccountComponent } from './account/create-account/create-account.component';
import { LoginComponent } from './account/login/login.component';
import { CardapiosComponent } from './cardapios/cardapios.component';
import { FormularioComponent } from './formulario/formulario.component';
import { WelcomeComponent } from './welcome/welcome.component';

const routes: Routes = [
  {
    path: '',
    component: AppComponent,
    children: [
      { path: 'login', component: LoginComponent },
      { path: 'create-account', component: CreateAccountComponent },
      //
      { path: 'welcome', component: WelcomeComponent },
      { path: 'calculadora', component: CalculadoraComponent },
      { path: 'cardapios', component: CardapiosComponent },
      { path: 'formulario', component: FormularioComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
