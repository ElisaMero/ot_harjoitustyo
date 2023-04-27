**Arkkitehtuurikuvaus**
##
Kuvaus kansioista:
- src:ssä sijaitsee käyttöliittymät ja pelin pyöritys
- objects-kansiossa sijaitsee pelin elementit: pelaaja, hyppytasot sekä karkit
- repositories-kansiossa sijaitsee tietokannan luominen. Tietokanta on toteutettu SQL-kielellä. Tietokantataulun nimi on Highscores.
Tauluun tallennetaan jokaisen pelin jälkeen tulos kerätyistä karkeista. Viisi suurinta tulosta näkyy src-kansion highscoreboard-tiedostossa.
##

**Luokkakaavio:**

```mermaid

classDiagram
  GameLoop <|-- StartScreen
  GameLoop <|-- PlatformJumpingGame
  PlatformJumpingGame <|-- Player
  PlatformJumpingGame <|-- Candies
  PlatformJumpingGame <|-- Shelves
  PlatformJumpingGame <|-- StopScreen
  SaveData <|-- Board
  PlatformJumpingGame <|-- SaveData  
```


**Sekvenssikaaviot:**

Alotusnäytöstä pelin lattiaraon kautta lopetukseen. (erilainen luokkakuvaukseen verrattuna, johtuen uusista muutoksista):

```mermaid
sequenceDiagram
  actor User
  participant StartScreen
  participant GameLoop
  participant PlatformJumpingGame
  participant Player
  participant StopScreen
  User->>GameLoop: GameLoop
  GameLoop->>StartScreen: StartScreen
  StartScreen->>PlatformJumpingGame: press "Enter"
  PlatformJumpingGame->>Player: events("right")
  Player-->>PlatformJumpingGame: 
  PlatformJumpingGame->>Player: events("right")
  Player-->>PlatformJumpingGame: 
  PlatformJumpingGame->>StopScreen: last_loop()
   
```
 









