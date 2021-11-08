import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardCardapiosComponent } from './dashboard-cardapios.component';

describe('DashboardCardapiosComponent', () => {
  let component: DashboardCardapiosComponent;
  let fixture: ComponentFixture<DashboardCardapiosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DashboardCardapiosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DashboardCardapiosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
