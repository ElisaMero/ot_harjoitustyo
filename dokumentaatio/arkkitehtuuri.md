```mermaid

classDiagram
  GameLoop <|-- StartScreen
  GameLoop <|-- PlatformJumpingGame
  PlatformJumpingGame <|-- Player

```


Sekvenssikaavio (erilainen luokkakuvaukseen verrattuna, johtuen uusista muutoksista):

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant TodoService
  participant UserRepository
  User->>UI: click "Login" button
  UI->>TodoService: login("kalle", "kalle123")
  TodoService->>UserRepository: find_by_username("kalle")
  UserRepository-->>TodoService: user
  TodoService-->>UI: user
  UI->UI: show_todos_view()
```
