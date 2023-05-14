# RAU laite ja pistetyökalu

Työkalulla on mahdollista pitää kirjaa projektiin tarvittavista laitteista ja niiden tarvitsemista pisteistä.  

Ohjelma on vielä aika raakile, viikko on mennyt isoksi osaksi opettelussa ja erinäisten ongelmien selvittelyssä.  

Käyttöohjeessa on lisää tietoa ohjelman käytöstä.

*Linkit:* [Changelog](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)  
[Vaatimusmäärittely](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
[Työaikakirjanpito](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)  
[Arkkitehtuurikaavio](https://github.com/attesan/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  
[Viimeisin julkaisu](https://github.com/attesan/ot-harjoitustyo/releases/tag/loppupalautus)  
  
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
Voit halutessasi lisätä tässä ikkunassa useamman laitteen peräkkäin. Kun olet valmis, paina: Peruuta -painiketta.  
Jos haluat muokata jotain lisäämääsi laitetta, valitse Tietokanta -pudotusvalikosta: Muokkaa tietokannan laitetta.  
Klikkaa haluamaasi laitetta ja muokkaa sen tietoja oikean reunan kentissä. Lopuksi tallenna muutokset painamalla: Tallenna -painiketta.  
Laitteiden lisäys projektiin onnistuu valitsemalla Lisää -pudotusvalikosta: Laite projektiin.  
Avautuvassa ikkunassa näet kaikkien tietokantaan lisäämiesi laitteiden perustiedot. Positio kenttään kirjoitetaan laitteen tarkoitusta tai järjestelmäsijaintia kuvaava lyhenne. Laitteen voi lisätä klikkaamalla "Lisää projektiin" -painiketta. Position on oltava uniikki projektissa.  
Pertuuta -painikkeella pääset takaisin päänäkymään.  
Jos lisäsit laitteen, se näkyy nyt päänäkymän laitelistassa. Ohjelma on myös lisännyt laitteen vaatimat pisteet pääikkunan pistelistaan.  
Voit halutessasi poistaa laitteen laitelistasta valitsemalla ensin poistettavan laitteen, ja klikkaamalla sen jälkeen "Poista laite projektista" -painiketta.  
Ohjelma poistaa automaattisesti laitteen pisteet pistelistasta.  
Jos haluat tallentaa projektin tiedot, voit tehdä niin Projekti-pudotusvalikosta. Valitse pudotusvalikosta "Vie CSV". Avautuvassa ikkunassa voit valita tiedoston tallennuspaikan ja tiedostonimen. Ohjelma lisää tiedostopäätteen automaattisesti. Lopuksi tallenna tiedot painamalla Tallenna-painiketta.  
Tässä on sovelluksen tämän hetkinen toiminnallisuus.

# Komennot komentoriville 
Suorita ohjelma: poetry run invoke start  
Suorita testit: poetry run invoke test  
Luo testikattavuusraportti: poetry run invoke coverage-report  
Aja pylint testit: poetry run invoke lint  
