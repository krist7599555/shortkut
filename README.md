<div align="center">
  <img src="./icon-sqcl.png" width="150" alt="ShortKut Icon" />
  <br />
  <br />
  <img src="https://img.shields.io/badge/Mac_M1-Compatible-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Mac M1 Compatible" />
  <br />
  <a href="https://github.com/krist7599555/shotkut/raw/main/ShortKut.dmg">
    <img src="https://img.shields.io/badge/Download-ShortKut.dmg-blue?style=for-the-badge&logo=apple" alt="Download ShortKut.dmg" />
  </a>
</div>

# 🚀 ShortKut

**ShortKut** = **Short**cut + **Kut** (Krist)

ShortKut is a macOS productivity tool designed to streamline your workflow by detecting custom key sequences to launch applications instantly.

**ShortKut** คือเครื่องมือช่วยเพิ่มความโปรดักทีฟบน macOS ที่ออกแบบมาเพื่อช่วยให้ workflow ของคุณลื่นไหลยิ่งขึ้น โดยการตรวจจับการกดปุ่มตามลำดับเพื่อเปิดแอปพลิเคชันได้ทันที

## ✨ Features

- ⚡ **Quick App Launching**: Trigger applications using simple key sequences.
- ⌨️ **Right Shift Detection**: Uses `<shift_r>` sequences for ergonomic access.
- 👻 **Background Operation**: Runs quietly in the background with a system tray icon (GUI).

## 🎹 Shortcuts

ShortKut listens for specific key sequences (last 3 keys pressed). The primary trigger involves double-tapping the **Right Shift** key followed by a letter.

| Sequence | Action |
| :--- | :--- |
| `<shift_r>` + `<shift_r>` + `b` | Open **Helium** |
| `<shift_r>` + `<shift_r>` + `t` | Open **Ghostty** |
| `<shift_r>` + `<shift_r>` + `c` | Open **Antigravity** |

*Note: Also supports `F3` or `:` as alternative triggers for the same actions.*

## 🛠️ Installation & Development

### 📋 Prerequisites

- Python 3.x
- `mise` (for environment management)
- `brew` (for system dependencies)

### ⚙️ Setup

1.  **Install Dependencies**:
    ```bash
    mise run install
    # Or manually:
    # brew install python-tk
    # pip install -r requirements.txt
    ```

2.  **Run Locally**:
    ```bash
    python lib.py
    ```

3.  **Build for Distribution**:
    Create a standalone executable using PyInstaller:
    ```bash
    mise run build
    # Or manually:
    # pyinstaller --windowed --onefile --name ShortKut --icon ./icon-sqcl.png --add-data 'icon-1024.png:.' ./lib.py
    ```

## 💻 Technology

- 🐍 **Python**: Core logic.
- 🎮 **pynput**: Keyboard monitoring and hotkey detection.
- 🖼️ **Tkinter**: GUI and system presence.
- 📦 **PyInstaller**: Packaging for macOS.

## 🚧 Current Status & Warning

⚠️ **Current Version**: This application is currently built using **Python**. It is in active development.

## 🗺️ Roadmap / TODO (Next Beta)

- [ ] 💎 **Migrate to Ruby**: Explore using Ruby for the core logic in the next beta version.
- [ ] 🔧 **Customizable Shortcuts**: Allow users to define their own key sequences and actions.
- [ ] 🖥️ **GUI Interaction**: Enable configuration and interaction directly through the GUI window.

