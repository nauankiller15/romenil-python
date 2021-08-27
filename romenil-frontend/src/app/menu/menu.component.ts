import { Component, OnInit } from '@angular/core';

declare var $: any;

@Component({
  selector: 'menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
})
export class MenuComponent implements OnInit {
  constructor() {
    this.MenuAtivo();
  }
  MenuAtivo() {
    $('.menuItems li a').on('click', () => {
      $(this).addClass('active');
      $(this).siblings().removeClass('active');
    });
  }

  ngOnInit(): void {
    
    // Animação Login Abrir

    $('#loginBt').on('click', function () {
      $('#login').fadeIn('100');
    });

    $('#fecharBt').on('click', function () {
      $('#login').fadeOut('100');
    });

    // MENU RESPONSIVO
    $('div.burger').on('click', () => {
      if (!$(this).hasClass('open')) {
        openMenu();
      } else {
        closeMenu();
      }
    });

    $('div.menu-mobile li').on('click', function () {
      closeMenu();
    });

    function openMenu() {
      $('div.circle').addClass('expand');

      $('div.burger').addClass('open');
      $('div.x, div.y, div.z').addClass('collapse');
      $('.menu-mobile li').addClass('animate');

      setTimeout(function () {
        $('div.y').hide();
        $('div.x').addClass('rotate30');
        $('div.z').addClass('rotate150');
      }, 70);
      setTimeout(function () {
        $('div.x').addClass('rotate45');
        $('div.z').addClass('rotate135');
      }, 120);
    }

    function closeMenu() {
      $('div.burger').removeClass('open');
      $('div.x').removeClass('rotate45').addClass('rotate30');
      $('div.z').removeClass('rotate135').addClass('rotate150');
      $('div.circle').removeClass('expand');
      $('.menu-mobile li').removeClass('animate');

      setTimeout(function () {
        $('div.x').removeClass('rotate30');
        $('div.z').removeClass('rotate150');
      }, 50);
      setTimeout(function () {
        $('div.y').show();
        $('div.x, div.y, div.z').removeClass('collapse');
      }, 70);
    }
    // //
    // //
    // // //
    // // //
    // // Função boolean para evento touch mobile
    // //

    let stopScrolling = false;

    window.addEventListener('touchmove', handleTouchMove, {
      passive: false,
    });

    function handleTouchMove(e: { preventDefault: () => void }) {
      if (!stopScrolling) {
        return;
      }
      e.preventDefault();
    }

    function onTouchStart() {
      stopScrolling = true;
    }

    function onTouchEnd() {
      stopScrolling = false;
    }

    //
    //
  }
}
