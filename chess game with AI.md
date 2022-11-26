chess game with AI
===

* Chess Game (1V1)
* AI (Mix of Machine Learning and Minimax)
* Python + Kivy 
* Play with your phone
* Convert to Windows / Mac 
* Kivy Mob

## Todo

```plantuml
@startuml
abstract class Piece {
    color: integer
    alive: bool
    x : integer
    y : integer
    +move()
    +availabe_moves()
    
    
}

class Game {
    
    +check_checkmate()
    +check_draw()
    +check_move()
    
}

class Window {
    Width: int
    Height: int 
    Chronometer : Date
    Turn: int
    +display_game()
    +display_availabe_moves()
    +change_player_turn()
    +get_position()
    
}

class Pawn {
    
}

class Knight {
    
}

class Bishop {
    
}

class Queen {
    
}

class King {
    
}

class Rook {
    
}

Piece <|-down- Pawn
Piece <|-down- Knight
Piece <|-down- Bishop
Piece <|-down- Queen
Piece <|-down- King
Piece <|-down- Rook

Game --down- Piece
Window --left- Game
@enduml
```



[Dataset chess Top 12 Players](https://www.kaggle.com/datasets/liury123/chess-game-from-12-top-players)

