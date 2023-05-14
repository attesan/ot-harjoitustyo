#Testausdokumentti  
  
Ohjelmaa on testattu sekä yksikkö-, integraatio- sekä manuaalisin testein. Toiminnallisuutta on testattu laajasti käsin järjestelmätasolla.  
  
#Yksikkö- ja integraatiotestaus  
  
#Sovelluslogiikka  
  
Sovelluslogiikkaa testataan seuraavasti:  
project_data_service -luokkaa testataan project_data_service_test-testiluokalla.  
project_device_maker -luokkaa testataan project_device_maker_test-testiluokalla.  
  
#Repositoriot  
  
device_repository -luokkaa testataan device_repository_test-testiluokalla.  
  
#Testauskattavuus  
Testauskattavuus on 71% mutta se saattaa kasvaa mikäli loppupalautusta ennen ehtii vielä muutaman testin lisäämään.  
Tällä hetkellä file_service -luokkaa ei testata automaattisesti. Luokan toiminta on testattu manuaalisesti käyttöliittymän kautta.  
Käyttöliittymän luokat on jätetty automaattisen testauksen ulkopuolelle kurssin vaatimusten seurauksena. Käyttöliittymää on testattu manuaalisesti.  
  
#Järjestelmätestaus  
  
Järjestelmätestaus on suoritettu manuaalisesti.  
  
#Asennus ja konfigurointi  
Asennusta ja konfigurointia on testattu readme.md -tiedoston käynnistysohjeen mukaisesti. Myös Käyttöohjeen käynnistysohjeen mukainen asennus on testattu.  
Sovelluksessa ei tällä hetkellä ole mahdollisuutta konfiguroida ympäristömuuttujia. Tiedoston tallennussijainti  
on käyttäjän valittavissa. Tallennusta on testattu tilanteessa jossa päällekirjoitetaan olemassa oleva tiedosto tai luodaan kokonaan uusi tiedosto.  
  
#Toiminnallisuus  
  
Kaikki määrittelydokumentin ja käyttöohjeen toteutettu toiminnallisuus on testattu.  
Testauksen yhteydessä on pyritty käymään läpi erilaisia virhetilanteita, kuten virheellisiä tai puuttuvia käyttäjän syöttämiä merkkijonoja.  
Suuressa osassa näistä virhetilanteista käyttäjä saa näkyviin virheilmoituksen ja ohjelma jatkaa toimintaa normaalisti.  
  
#Sovellukseen jääneet laatuongelmat  
  
Sovelluksessa saattaa ilmetä joitain virhetilanteita, joihin ei ole vielä lisätty käyttäjälle selkeää virheilmoitusta.  
Suurimmassa osassa näitä tilanteita ohjelma jatkaa kuitenkin normaalia toimintaa.  
Tiedostoa tallennettaessa käyttäjälle annetaan vain yleisluontoinen virheilmoitus, mikäli jotain menee vikaan.  
Tämä virheviesti ei välttämättä ole hyvä apu jokaiseen ongelmatilanteeseen.  
  
Mikäli ohjelmalla ei ole kirjoitusoikeutta tietokantaansa tai projektin tallennuspaikkaan, käyttäjä ei välttämättä saa järkevää virheilmoitusta.  
SQLite tietokantaa ei ole alustettu. Eli python -m poetry run invoke build-komnetoa ei ole suoritettu.  
  
