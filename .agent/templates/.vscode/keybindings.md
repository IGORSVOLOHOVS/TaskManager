# Professional C++ Keybindings

Since VS Code does not support project-local keyboard shortcuts, please add the following to your global `keybindings.json` (Open with `Ctrl+Shift+P` -> `Open Keyboard Shortcuts (JSON)`).

## Essential Mappings

```json
[
    {
        "key": "alt+o",
        "command": "clangd.switchheadersource",
        "when": "editorTextFocus && editorLangId == 'cpp'"
    },
    {
        "key": "ctrl+alt+s",
        "command": "header-source-switcher.switchSideBySide",
        "when": "editorTextFocus && (editorLangId == 'cpp' || editorLangId == 'c')"
    },
    {
        "key": "ctrl+f7",
        "command": "workbench.action.tasks.runTask",
        "args": "CMake: Build"
    },
    {
        "key": "ctrl+alt+c",
        "command": "cmake.configure"
    },
    {
        "key": "ctrl+alt+t",
        "command": "workbench.action.tasks.runTask"
    },
    {
        "key": "ctrl+alt+i",
        "command": "editor.action.toggleInlayHints"
    }
]
```

## Summary of shortcuts

| Shortcut | Action | Extension |
| :--- | :--- | :--- |
| `Alt + O` | Switch between Header/Source | Clangd |
| `Ctrl + Alt + S` | Switch Header/Source (Side by Side) | Header Switcher |
| `Ctrl + F7` | Build with CMake | Core Tasks |
| `Ctrl + Alt + C` | Configure CMake | CMake Tools |
| `Ctrl + Alt + T` | Run any Task | Core Tasks |
| `Ctrl + Alt + I` | Toggle Inlay Hints | Core Editor |
| `F5` | Start Debugging | Core Debug |
| `F2` | Rename Symbol | Clangd |
| `Shift + F12` | Find All References | Clangd |
