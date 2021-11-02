import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WelcomePagoComponent } from './welcome-pago.component';

describe('WelcomePagoComponent', () => {
  let component: WelcomePagoComponent;
  let fixture: ComponentFixture<WelcomePagoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WelcomePagoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(WelcomePagoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
