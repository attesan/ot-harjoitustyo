---  
Monopoli  
---  
classDiagram  
    pelinappula "1" <-- "1" pelaaja  
    pelaaja "2..8" -- "1" peli  
    pelinappula ..> ruutu  
    noppa "2" <-- "1" peli  
    peli "1" --> "40" ruutu  
    ruutu -- "1" aloitusruutu  
    peli -- aloitusruutu  
    ruutu -- "1" vankila  
    peli -- vankila  
    ruutu -- "1" sattuma  
    ruutu -- "1" yhteismaa  
    sattuma --> "*" kortti  
    yhteismaa --> "*" kortti  
    ruutu -- "*" Asemat_ja_laitokset  
    ruutu -- "*" Normaalit_kadut  
    Normaalit_kadut --> "0..4" talo  
    Normaalit_kadut --> "0..1" hotelli  
    Normaalit_kadut "0..*" <-- pelaaja  
  
class pelaaja{  
    +rahaa  
}  
  
class Normaalit_kadut{  
    +nimi  
}  

class kortti{  
    +toiminto()  
}  

class ruutu{  
    +seuraava_ruutu  
}  
