export class Cardapios {
    desjejum: Cardapio[] = [];   
    cafeManha: Cardapio[] = [];   
    refeicao2: Cardapio[] = [];   
    almoco: Cardapio[] = []; 
    refeicao4: Cardapio[] = [];   
    janta: Cardapio[] = [];   
    refeicao6: Cardapio[] = []; 
}

export class Cardapio {
    refeicao: number = 0;
    prato: string = '';
}


export class CardapiosCompletos {
    desjejum: CardapioCompleto[] = [];   
    cafeManha: CardapioCompleto[] = [];   
    refeicao2: CardapioCompleto[] = [];   
    almoco: CardapioCompleto[] = []; 
    refeicao4: CardapioCompleto[] = [];   
    janta: CardapioCompleto[] = [];   
    refeicao6: CardapioCompleto[] = []; 
}

export class CardapioCompleto {
    id: number = 0;
    refeicao: number = 0;
    prato: string = '';
    principal : string = '';
    secundaria : string = '';
}