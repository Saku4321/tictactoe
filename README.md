# ❌🟢 Tic Tac Toe (Kółko i Krzyżyk)

A modular Python implementation of the classic **Tic Tac Toe** game, playable in the console.  
Supports both **single-player (vs computer opponent)** and **two-player (local)** modes.

Modularna implementacja klasycznej gry **Kółko i Krzyżyk** w języku Python, działająca w konsoli.  
Obsługuje tryb **jednoosobowy (z przeciwnikiem komputerowym)** oraz **dwuosobowy (na jednym komputerze)**.

---

## 🧩 Project Structure / Struktura projektu

```
tictactoe/
├── tictactoe.py           # Main game file – controls game flow and mode
├── player_movement.py     # Handles player input and mode selection
├── ai_movement.py         # Computer opponent decision logic (rule-based)
├── movement_check.py      # Board evaluation and win/draw checking
└── PyCharmMiscProject.iml # IDE config file (optional)
```

---

## 🎮 Game Overview / Opis gry

- Classic 3×3 Tic Tac Toe grid represented with Python lists  
- Player **X** always moves first  
- Computer or second player plays as **O**  
- Game ends automatically when:
  - one player wins, or  
  - the board is full (draw)

---

## 🧠 Computer Opponent Logic (ai_movement.py)

The opponent logic is **rule-based** — it doesn’t use machine learning or search algorithms,  
but instead follows a set of predefined conditions and priorities to simulate an intelligent player.

Logika przeciwnika komputerowego opiera się na **zestawie ustalonych reguł (rule-based)**.  
Nie jest to algorytm uczący się ani oparty na przeszukiwaniu (np. minimax),  
lecz system prostych zasad decyzyjnych symulujących „inteligentne” zachowanie gracza.

### Decision hierarchy / Hierarchia decyzji:
1. **Winning move** – if two “O” in a row, play the third.
2. **Blocking move** – if two “X” in a row, block the player.
3. **Attacking move** – expand partial lines containing “O”.
4. **Defensive move** – prevent player advantage when possible.

The AI checks all **rows, columns, and diagonals** each turn using helper functions from `movement_check.py`.

---

## 👤 Player Input (player_movement.py)

- Allows selecting game mode: `1player` or `2player`
- Prompts the user for:
  - **row (1–3)**
  - **column (1–3)** within that row
- Clears the console between moves for readability
- Prevents placing a mark in an already occupied cell

---

## ⚙️ Game Logic (movement_check.py)

Handles all game evaluation:
- `checking_row`, `checking_column`, `checking_diagonal1/2` — count symbols in each line  
- `check_if_movement_is_possible()` — finds first available position  
- `winner()` — determines if "X" or "O" has won  
- `board_full()` — detects a draw  
- `wincheck()` — prints results and stops the game  

---

## 🕹️ Main Game Loop (tictactoe.py)

1. Displays the current board state  
2. Prompts the player(s) for moves  
3. In 1-player mode, triggers computer move via `ai_move()`  
4. Uses `wincheck()` to check for win/draw conditions  
5. Ends the game automatically when a result is found  

Example gameplay:
```
Select game mode: 1player / 2player
X moves
Please select row: 1,2,3
Pick place in row: 1,2,3
O moves
...
X wins! or Draw
```

---

## ▶️ How to Run / Jak uruchomić

Run the main file in your terminal:
```bash
python tictactoe.py
```
Then follow the on-screen instructions to play in **single-player** or **two-player** mode.

---

## 🧩 Technical Details / Szczegóły techniczne

- **Language:** Python 3  
- **Libraries:** Only built-in (`os`, `random`)  
- **Design:** Modular, procedural OOP  
- **Interface:** Text-based (console I/O)

---

## 🚀 Possible Improvements / Możliwe ulepszenia
- Implement a smarter AI (e.g. Minimax algorithm with alpha-beta pruning)  
- Add replay and scoring system  
- Create GUI version (Tkinter or Pygame)  
- Save game statistics or move history  

---

## 👨‍💻 Author / Autor

Developed as an early programming project focused on:
- modular program design,  
- implementation of turn-based game logic,  
- and building a rule-based computer opponent in Python.

Stworzono jako wczesny projekt uczący:
- projektowania programów modułowych,  
- implementacji logiki gier turowych,  
- oraz tworzenia **systemów decyzyjnych przeciwnika komputerowego** w Pythonie.
