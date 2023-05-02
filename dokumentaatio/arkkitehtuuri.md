# Arkkitehtuurikaavio  
```mermaid
classDiagram
    devices_db -- database_connection
    device_repository --> database_connection
    index <-- initialize_database
    initialize_database <-- "1" devices_db
    index <-- ui
    main_window <-- new_device
    main_window <-- edit_device
    main_window --> ui
    main_window <-- add_project_device
    device_repository --> new_device
    device_repository --> edit_device
    device_repository --> add_project_device
    project_device_maker --> add_project_device
    project_device_maker -- device_repository
    project_data_service --> main_window
    project_data_service --> add_project_device
    
    Project "1" --> main_window
    ProjectDevice "*" --> Project
    ProjectPoint "0-4" --> ProjectDevice
    project_device_maker <-- ProjectDevice
```  
  
# Rakenne ja toiminnallisuus yleisesti.
Ohjelman rakenteessa on kolme tasoa.  
- UI: Käyttöliittymän koodi.  
- Services: Sovelluslogiikan koodi.  
- Entities: Sovelluksen käyttämät tietoa sisältävät luokat.  
- Repositories: Tietojen tallennus ja haku tietokannasta.  
  
# Käyttöliittymästä  
Ohjelmassa on tällä hetkellä seuraavat ikkunat:  
Päänäkymä - Sisältää projektiin lisätyt laitteet ja pisteet.  
Uuden laitteen lisäys tietokantaan - Mahdollistaa laitteiden tallennuksen pysyvästi.  
Tietokannan laitteen muokkaus - Tästä ikkunasta käsin voi muokata tietokantaan tallennettua tietoa.  
Lisää laite projektiin - Täältä voi valita mitä tietokantaan tallennettuja laitteita halutaan lisätä projektiin. Pisteet lisätään automaattisesti.  
  
Jokainen ikkuna on oma luokkansa, joiden näyttämisestä vastaa UI-luokka. Käyttöliittymä on pääosin erillinen sovelluslogiikasta. Muutamia sovelluslogiikan osia on kuitenkin vielä käyttöliittymän luokissa.  
  
# Sovelluslogiikka  
Sovelluksen tietoja hallinnoi project_data_service -luokka. Sinne lisätään projektiin lisätyt laitteet. project_device -luokka kuvaa projektin laitteita. Jokaisen project_device -luokan alla on project_point -pisteitä, jotka kuvaavat lisättyjen laitteiden pisteitä.  
  
project_device_maker -luokka tarjoaa metodit project_device -olioiden ja niiden alla olevien project_point -olioiden luomiseen.  
  
# Projektin tietojen tallennus  
Projektin tiedot on tarkoitus tallentaa csv muodossa tiedostoon. Tätä ei vielä ole toteutettu.

