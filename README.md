# EE160 Final Project — How to run the game

This README explains common ways to run the game from this repository on a Linux machine (tested on Ubuntu).

## 1. Open the project folder
In a terminal:
```
cd {repo_name}
```

## 2. Common run instructions

### A. Python (pygame or similar)
1. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
2. Install dependencies (if present):
```
pip install -r requirements.txt
```
3. Run the game (common entry names: `main.py`, `game.py`, `run.py`):
```
python3 main.py
```
Replace `main.py` with the actual entry file name.

## 4. Controls
(Replace with your game's actual controls)
- Arrow keys / WASD — move
- Space — jump / action
- Esc — pause / quit

## 5. Troubleshooting
- Missing dependencies: check `requirements.txt` or `package.json`.
- Permission issues when running: try `chmod +x ./script` or ensure python/node binaries are installed.
- If `import pygame` fails: `pip install pygame` inside the virtualenv.
- For web CORS/static resource problems, use the simple HTTP server (`python3 -m http.server`).

## 6. Tests (if any)
Run tests with pytest:
```
pip install -r requirements.txt   # if tests require packages
pytest
```

## 7. Contact / Notes
If something is unclear, provide the project files list or the main entry filename and I can give exact commands.
