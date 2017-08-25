# BomberMan

## Usage
python3 game.py

## Gameplay
The player must navigate Bomberman through a maze by destroying bricks(for which the player gets 20 points) and enemies(for which the player gets 100 points) with his bombs. After killing all the enemies in a level, the player advances to the next level by standing on the door, which is hidden under a random brick. There are 3 levels in total. On each level, we can get one powerup like Huge Bomb, Xtra Life or Immortal that will spawn on a random loaction after we press the p key and will stay there for 10 seconds.

The controls for the game are:

`w`: Move up one step

`a`: Move left one step

`s`: Move down one step

`d`: Move right one step

`b`: Drop bomb on current location

`q`: End the Game

`p`: Spawn a powerup

## Board Objects

```
Bomberman
[^^]
 ][
 ```

```
Wall
####
####
```

```
Bricks
////
////
```


```
Bomb(with a timer)
3333
3333
```

```
Explosion
eeee
eeee
```

```
Enemy 1(Slowest)
EEEE
EEEE
```

```
Enemy 2(Faster)
/==\
\==/
```

```
Enemy 3(Fastest and requires 2 bombs)
(--)
====
```




## Game Implementation and Design

### Modularity
The game has a very modular design and each component has been decomposed into small units and methods.

### Inheritence
Each object on the board inherits from a single class BoardObject and the Bomberman and Enemy classes inherit from the Person class which in turn inherits from BoardObject class.


### Polymorphism
The code also has functions which behave differently according to the object it acts upon.

### Encapsulation
The code has been encapsulated well into classes and only the required functions are public in each class otherwise every variable and function is private.
