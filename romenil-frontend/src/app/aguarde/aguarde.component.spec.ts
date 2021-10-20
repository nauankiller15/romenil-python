import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AguardeComponent } from './aguarde.component';

describe('AguardeComponent', () => {
  let component: AguardeComponent;
  let fixture: ComponentFixture<AguardeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AguardeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AguardeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
