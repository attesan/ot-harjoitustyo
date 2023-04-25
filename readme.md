# RAU laite ja pistetyökalu

Työkalulla on mahdollista pitää kirjaa projektiin tarvittavista laitteista ja niiden tarvitsemista pisteistä.  

Ohjelma on vielä aika raakile, viikko on mennyt isoksi osaksi opettelussa ja erinäisten ongelmien selvittelyssä.  

*Linkit:* [Changelog](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)  
[Vaatimusmäärittely](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
[Työaikakirjanpito](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)  
[Arkkitehtuurikaavio](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  
[Viimeisin julkaisu](https://github.com/attesan/ot-harjoitustyo/releases/tag/Viikko5)  
  
# Ohjelman suorittaminen  
1 Pura lataamasi kansio.  
2 Avaa kansio: ot-harjoitustyo-viikko5\src\  
3 Tuplaklikkaa: index.py  

Ohjelma käynnistyy suoraan pääikkunaan.  
Viimeisin toiminnallisuus löytyy changelog -dokumentista.  
  
# Käyttö lyhyesti  
Avaa Tietokanta -pudotusvalikosta: lisää laite tietokantaan.  
Laitteen tiedot syötetään tämän ikkunan kenttiin ja tallennetaan painamalla: Tallenna -painiketta.  
Laitteen perustiedot löytyvät ensimmäiseltä riviltä.  
Pisteet kuvaavat laitteen fyysisiä kytkentöjä.  
Voit halutessasi lisätä useamman laitteen peräkkäin. Kun olet valmis, paina: Peruuta -painiketta.  
Jos haluat muokata jotain lisäämääsi laitetta, valitse Tietokanta -pudotusvalikosta: Muokkaa tietokannan laitetta.  
Klikkaa haluamaasi laitetta ja muokkaa sen tietoja oikean reunan kentissä. Lopuksi tallenna muutokset painamalla: Tallenna -painiketta.  
Laitteiden lisäys onnistuisi mikäli kyseinen toiminnallisuus olisi olemassa. Jos haluat kuitenkin fiilistellä tätä kokemusta, valitse Lisää -pudotusvalikosta: Laite projektiin.  
Avautuvassa ikkunassa näet kaikkien lisäämiesi laitteiden perustiedot. Positio kenttään kirjoitetaan laitteen tarkoitusta kuvaava lyhenne. Laitteen lisäystä voi harjoitella klikkaimella: Lisää projektiin -painiketta. Se ei tee mitään.  
Tässä kaikki tällä hetkellä viimeisimpään julkaisuun toteutettu toiminnallisuus. Ensi viikolla laitteiden ja pisteiden lisääminen lienee mahdollista. Myös ainakin laiteposition muokkaaminen onnistunee. Myös CSV muotoinen tiedoston tallennus olisi tavoitteena saada toteutettua ensi viikolla.  
  
# Komennot komentoriville 
Suorita ohjelma: poetry run invoke start  
Suorita testit: poetry run invoke test  
Luo testikattavuusraportti: poetry run invoke coverage-report  
Aja pylint testit: poetry run invoke lint  
