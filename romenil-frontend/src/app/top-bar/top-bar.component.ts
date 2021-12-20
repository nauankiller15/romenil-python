import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Conta } from '../account/models';
import { LoaderService } from '../loader/loader.service';

declare var $: any;

@Component({
  selector: 'app-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.css'],
})
export class TopBarComponent implements OnInit {
  @Input() conta = new Conta();

  constructor(private router: Router,
    public loaderService:LoaderService) {}

  ngOnInit(): void {
    
    $('.menu-box').on('click', function () {
      $('.box-menu').toggle(200);
    });
    $(document).ready(function () {
      // MENU TOP BAR
      const menu = document.querySelector('#mobile-menu');
      const menuLinks = document.querySelector('.nav-menu');

      menu!.addEventListener('click', function () {
        menu!.classList.toggle('is-active');
        menuLinks!.classList.toggle('active');
      });

      // MENU DROP DOWN
      const drop_btn = document.querySelector('.drop-btn');
      const menu_wrapper = document.querySelector('.wrapper');
      const menu_bar = <HTMLElement>document.querySelector('.menu-bar');
      const setting_drop = <HTMLElement>document.querySelector('.setting-drop');
      const setting_item = <HTMLElement>document.querySelector('.setting-item');
      const back_setting_btn = <HTMLElement>(
        document.querySelector('.back-setting-btn')
      );

      drop_btn!.addEventListener('click', function () {
        menu_wrapper!.classList.toggle('show');
      });
      // setting_item!.addEventListener('click', function () {
      //   menu_bar!.style.marginLeft = '-300px';
      //   setTimeout(() => {
      //     setting_drop!.style.display = 'block';
      //   }, 100);
      // });
      back_setting_btn!.addEventListener('click', function () {
        menu_bar!.style.marginLeft = '0px';
        setting_drop!.style.display = 'none';
      });
    });
  }

  sair() {
    localStorage.removeItem('token');
  }
}
