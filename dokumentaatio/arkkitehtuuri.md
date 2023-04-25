```mermaid

classDiagram
  GameLoop <|-- StartScreen
  GameLoop <|-- PlatformJumpingGame
  PlatformJumpingGame <|-- Player

```


Sekvenssikaavio alotusnäytöstä pelin lattiaraon kautta lopetukseen. (erilainen luokkakuvaukseen verrattuna, johtuen uusista muutoksista):

```mermaid
sequenceDiagram
  actor User
  participant StartScreen
  participant PlatformJumpingGame
  participant Player
  participant StopScreen
  User->>StartScreen: StartScreen
  StartScreen->>PlatformJumpingGame: press "Enter"
  PlatformJumpingGame->>Player: events("right")
  Player-->>PlatformJumpingGame: 
  PlatformJumpingGame->>Player: events("right")
  Player->>StopScreen: last_loop()
   
```
 
