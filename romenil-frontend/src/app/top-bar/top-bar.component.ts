import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.css'],
})
export class TopBarComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {
    window.onload = function () {
      // MENU TOP BAR
      const menu = document.querySelector("#mobile-menu");
      const menuLinks = document.querySelector(".nav-menu");
    
      menu!.addEventListener("click", function () {
        menu!.classList.toggle("is-active");
        menuLinks!.classList.toggle("active");
      });
    };
    
  }
}
