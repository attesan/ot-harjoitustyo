```markdown
sequenceDiagram
    main ->> laitehallinto: HKLLaitehallinto()
    laitehallinto -->> main: None
    main ->> rautatientori: Lataajalaite()
    rautatientori -->> main: None
    main ->> ratikka6: Lukijalaite()
    ratikka6 ->> main: None
    main ->> bussi244: Lukijalaite()
    bussi244 -->> main: None
    main ->> lippu_luukku: Kioski()
    lippu_luukku -->> main: None
    main ->> lippu_luukku: osta_matkakortti("Kalle")
    lippu_luukku ->> Matkakortti: Matkakortti("Kalle")
    Matkakortti -->> lippu_luukku: None
    lippu_luukku -->> main: uusi_kortti
    main ->> kallen_kortti: uusi_kortti
    main ->> rautatientori: lataa_arvoa(kallen_kortti, 3)
    rautatientori ->> kallen_kortti: kasvata_arvoa(3)
    activate kallen_kortti
    kallen_kortti -->> rautatientori: None
    deactivate kallen_kortti
    rautatientori -->> main: None
    main ->> ratikka6: aosta_lippu(kallen_kortti, 0)
    ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
    activate kallen_kortti
    kallen_kortti -->> ratikka6: None
    deactivate kallen_kortti
    ratikka6 -->> main: True
    main ->> bussi244: osta_lippu(kallen_kortti, 2)
    bussi244 -->> main: False
```
