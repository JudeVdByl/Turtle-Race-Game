# Turtle Race Game

A lightweight graphical racing game built with Python's **turtle** module. Place a bet, watch six colorful turtles sprint to the finish, and see if your pick comes out on top.

## Features

* Six distinct turtle racers in classic rainbow colors
* User prompt to bet on the winning color
* Randomized movement for each turn keeps every race unpredictable
* Popup message announces the winner and whether your bet was correct
* "Race again" prompt lets you restart instantly without closing the window

## Requirements

* Python 3.8 or newer
* Standard library modules only (`turtle`, `tkinter`, `random`)

  * On some Linux distributions you may need to install `python3-tk`.

## Installation

```bash
git clone https://github.com/your‑username/turtle‑race.git
cd turtle‑race
```

No additional packages are needed.

## Running the Game

```bash
python turtle_race.py
```

1. Enter a color when prompted (red, orange, yellow, green, blue, or purple).
2. Watch the turtles race across the screen.
3. A dialog shows the winning color and your result.
4. Choose **yes** to run another race or close the window to quit.

## File Reference

| File             | Purpose          |
| ---------------- | ---------------- |
| `turtle_race.py` | Main game script |

## Contributing

Feel free to open issues or submit pull requests for improvements such as sound effects, score tracking, or difficulty tweaks.

## License

This project is released under the MIT License.
