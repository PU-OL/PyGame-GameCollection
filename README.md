# Games with PyGame

> ## Table of Contents
>
> 1. [Project description](#project-description)
> 2. [License](#license)
> 3. [Requirements](#requirements)
> 4. [How to start](#how-to-start)
> 5. [Found a bug?](#found-a-bug)
> 6. [Included games](#included-games)
>    1. [Pac-Man](#pac-man)
> 7. [Install games yourself](#install-games-yourself)
>

## Project description

This project include games made with PyGame in Python.

## License

This code is licensed under GNU GENERAL PUBLIC LICENSE.

More information [here](../../LICENSE).

## Requirements

- Python 3.12 or older
- PyGame

## How to start

- Install all the requirements
- Open main.py
- Select one of the Games
- Play the Game

## Found a bug?

If you found a bug you can report it [here](../../issues).

## Included games

- Pac-Man

---

### Pac-Man

With the number of point you get more ghosts will spawn. 

| Points | Number of Ghosts |
|--------|------------------|
| 10     | 1                |
| 20     | 2                |
| 30     | 3                |
| 40     | 4                |

You can control Pac-Man via w,a,s and d or the arrow keys

---

## Install Games yourself

1. Put your game in a class
2. Add a ``` def yourname(self, screen, clock):```<br>
``self.screen = screen``<br>
``self.clock = clock``<br>
``self.name = "yourname"``
3. Add a methode ``def start(self):`` where you put your main code
4. Import this class to ``main.py``
5. Add ``yourgame = yourgame(screen, clock)`` in ``main.py`` after line 13
6. Add ``games.append(yourgame)`` also in ``main.py``
7. Now start ``main.py`` and enjoy your game

---
©2026 PU-OL