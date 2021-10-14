import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModeloCardapioComponent } from './modelo-cardapio.component';

describe('ModeloCardapioComponent', () => {
  let component: ModeloCardapioComponent;
  let fixture: ComponentFixture<ModeloCardapioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ModeloCardapioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ModeloCardapioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
