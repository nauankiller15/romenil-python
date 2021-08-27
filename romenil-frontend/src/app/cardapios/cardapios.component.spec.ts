import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardapiosComponent } from './cardapios.component';

describe('CardapiosComponent', () => {
  let component: CardapiosComponent;
  let fixture: ComponentFixture<CardapiosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CardapiosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CardapiosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
