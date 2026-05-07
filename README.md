<h1 align="center">Python-Tetris</h1>

<p align="center">
  A classic Tetris game built using Python and the Pygame library.
</p>

## 📸 Screenshot

![tetris](screenshot/1.png "Tetris")

## ✨ Features

- **Classic Gameplay**: Experience the traditional Tetris mechanics you know and love.
- **Score Tracking**: Points are awarded based on the number of lines cleared simultaneously.
- **High Score Persistence**: The game remembers your highest score across sessions (saved in the `record` file).
- **Dynamic Window Scaling**: Automatically scales the game to fit your screen height while maintaining the aspect ratio.
- **Executable Ready**: Pre-configured to easily build into a standalone executable using PyInstaller.

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| `Left Arrow` | Move piece left |
| `Right Arrow` | Move piece right |
| `Up Arrow` | Rotate piece |
| `Down Arrow` | Accelerate drop speed |

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame-ce

### Installation & Running

1. Clone the repository:
   ```bash
   git clone https://github.com/ShivamKR12/Python-Tetris.git
   cd Python-Tetris
   ```
2. Install the required dependencies:
   ```bash
   pip install pygame-ce
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## 📦 Packaging (Standalone Executable)

To build the game into a single executable file that can be shared without requiring Python to be installed:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the build command (Windows):
   ```bash
   pyinstaller --noconsole --onefile --add-data "img;img" --add-data "font;font" main.py
   ```
   *(For macOS/Linux, use `:` instead of `;` in the `--add-data` flags)*

The compiled executable will be located in the `dist/` directory.

## 📝 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
