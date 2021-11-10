import { Component, OnInit } from '@angular/core';
import { RouteConfigLoadEnd, RouteConfigLoadStart, Router, RouterEvent } from '@angular/router';

declare var $: any;
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  template: '<menu></menu><router-outlet></router-outlet>',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title(title: any) {
    throw new Error('Method not implemented.');
  }
  loading: boolean;

  constructor(private router: Router) {

    this.loading = false;

    // router.events.subscribe((event: RouterEvent) => {
    //   if (event instanceof RouteConfigLoadStart) {
    //     this.loading = true;        
    //   }
    //   else if (event instanceof RouteConfigLoadEnd) {
    //     this.loading = false;
    //   }
    // }

  }

  ngOnInit(): void {
    $('#entrarprog').on('click', function () {

      $('.dashFundo').fadeIn(250);

    });
  }
}
