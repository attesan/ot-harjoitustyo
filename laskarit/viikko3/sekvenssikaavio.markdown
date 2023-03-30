```mermaid
sequenceDiagram
    main ->> kone: Machine()
    kone ->> __tank: FuelTank()
    __tank -->> kone: None
    kone ->> __tank: fill(40)
    activate __tank
    __tank -->> kone: None
    deactivate __tank
    kone ->> __engine: Engine(self.__tank)
    __engine -->> kone: None
    kone -->> main: None
    main ->> kone: drive()
    kone ->> __engine: start()
    __engine ->> __tank: consume()
    activate __tank
    __tank -->> __engine: None
    deactivate __tank
    __engine -->> kone: None
    kone ->> __engine: is_running()
    __engine -->> kone: True
    kone ->> __engine: use_energy()
    __engine ->> __tank: consume(10)
    activate __tank
    __tank -->> __engine: None
    deactivate __tank
    __engine -->> kone: None
    kone -->> main: None
```
