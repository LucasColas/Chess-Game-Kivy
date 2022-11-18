chess game with AI
===

* Jeu d'échecs 1v1
* IA (mélange Machine Learning + Minimax Alpha Beta)
* Images SVG
* Python + Django

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
@enduml
```



[Dataset chess Top 12 Players](https://www.kaggle.com/datasets/liury123/chess-game-from-12-top-players)