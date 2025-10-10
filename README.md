# 🚀 Asteroids

A classic Asteroids clone built with Python and Pygame.

## ✨ Features

- Classic arcade gameplay
- Smooth 60 FPS rendering
- Asteroid spawning and collision detection
- Player shooting mechanics with cooldown

## 📋 Requirements

- Python 3.11+ (see `.python-version`)
- uv (recommended) or pip for dependency management

## 🛠️ Setup

### Using uv (Recommended)

```bash
uv sync
uv run main.py
```

### Using pip

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 🎮 Controls

- **W** - Move forward
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **Space** - Shoot

## 📁 Project Structure

```
├── main.py              # Game entry point and main loop
├── player.py            # Player ship class
├── asteroid.py          # Asteroid entity
├── shot.py              # Projectile class
├── asteroidfield.py     # Asteroid spawning manager
├── circleshape.py       # Base class for circular entities
├── constants.py         # Game constants and settings
├── pyproject.toml       # Project configuration
└── uv.lock             # Dependency lockfile
```

## 🔧 Development

- Use `uv.lock` for reproducible installations
- Check `.gitignore` for excluded build artifacts
- Format and lint with your preferred tools

## 📝 License

Educational project from [Boot.dev](https://boot.dev)

---
