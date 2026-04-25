### Modern Notepad: a sleek dark‑theme text editor

A clean, modern text editor built with Python and tkinter — perfect for coding, note‑taking, or just jotting down ideas. Dark theme, rich formatting, and auto‑save keep your workflow smooth and distraction‑free.


**What it does:**

* edit text with a beautiful dark interface;
* format text: **bold**, *italic*, underline, ~~strikethrough~~;
* change font size on the fly (8–72 pt);
* open and save `.txt` and `.py` files (UTF‑8);
* search for text with highlighting;
* auto‑saves every 30 seconds (creates `.autosave` backups);
* shows file status and word count in the status bar;
* supports keyboard shortcuts for faster work.


**What I learned:**

* **tkinter GUI:** built a full interface with frames, labels, buttons, dropdowns, and a scrollable text area.
* **Dark styling:** used dark colours (`#1a1a1a`, `#2d2d2d`) and smooth hover effects for a professional look.
* **Text formatting:** implemented bold, italic, underline, and strikethrough with tags and keyboard shortcuts (`Ctrl+B`, `Ctrl+I`, `Ctrl+U`, `Ctrl+T`).
* **File handling:** added New, Open, Save, and Save As functions with UTF‑8 encoding.
* **Search tool:** created a popup window to find and highlight text.
* **Auto‑save:** set up periodic backups to prevent data loss.
* **Event binding:** linked keyboard and mouse actions to app functions (e.g., `Ctrl+S` to save).
* **State management:** tracked file status (saved/unsaved), current file path, and font size.
* **Tooltips:** added hover hints for formatting buttons to improve UX.
* **Syntax highlighting:** basic colouring for Python‑like code (keywords, strings, comments, numbers).


🚀 **How to use it**

1. Run `code.py` in Python.
2. The «Modern Notepad» window opens (1000×700 px, dark theme).
3. Start typing in the main text area.
4. Format your text:
   * Use **𝐁**, **𝐈**, **𝐔**, **𝑺** buttons or `Ctrl+B` / `Ctrl+I` / `Ctrl+U` / `Ctrl+T`.
   * Pick a font size from the dropdown menu (Size: 12 by default).
5. Manage files:
   * **📁 New** — start a fresh document.
   * **📄 Open** — load a `.txt` or `.py` file.
   * **💾 Save** — save current file.
   * **💾 Save As** — save with a new name.
6. Edit and search:
   * **✂️ Cut**, **📋 Copy**, **📌 Paste** — standard clipboard actions.
   * **🔍 Find** — open search dialog, type text, click **Find Next** to highlight matches.
7. Watch the status bar:
   * Shows «Modified» when unsaved changes exist.
   * Displays word count and current font size.
8. Relax — your work auto‑saves every 30 seconds.

🔍 **A few things to know**

* Font size resets when you restart (no persistent settings).
* Syntax highlighting is basic (works best with Python).
* Search is case‑sensitive and doesn’t support regex.
* Tooltips may appear slightly off‑screen.
* Large files could slow down the search or auto‑save.
* Auto‑saved backups (`file.txt.autosave`) aren’t restored automatically.


🛫 **Try it yourself!**

1. Download `code.py`.
2. Open it in your favourite Python environment (IDLE, VS Code, PyCharm).
3. Run the script — the sleek dark window appears instantly.
4. Test it:
   * Type a sentence and make a word **bold** with the button or `Ctrl+B`.
   * Select text and apply *italic* or ~~strikethrough~~.
   * Change the font size — watch the text update in real time.
   * Open a Python file — see keywords (blue), strings (orange), comments (green) highlighted.
   * Click **🔍 Find**, type a word, and click **Find Next** — matches light up.
   * Make a change — notice the title bar adds a `*` and the status says «Modified».
   * Press `Ctrl+S` to save — the `*` disappears and status shows «Saved successfully».
   * Close and reopen to test auto‑saved backup (if enabled).


It’s simple, it’s dark, and it just works. Perfect for quick notes, light coding, or learning tkinter! Give it a go — and feel free to tweak it to your taste! 😊
