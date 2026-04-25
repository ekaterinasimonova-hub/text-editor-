import tkinter as tk
from tkinter import filedialog, messagebox, font, scrolledtext
import os

class ModernNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Notepad")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a1a')
        
        # File tracking
        self.current_file = None
        self.is_saved = True
        
        # Configure custom fonts
        self.title_font = font.Font(family="Segoe UI", size=12, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=10)
        
        # Font configuration for text formatting
        self.base_font_family = "Consolas"
        self.preset_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 24, 28, 32, 36, 48, 72]
        self.current_font_size = 12
        
        self.setup_ui()
        self.setup_syntax_highlighting()
        self.setup_text_formatting()
        
    def setup_ui(self):
        # Configure root window properties
        self.root.resizable(True, True)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title bar
        title_frame = tk.Frame(main_frame, bg='#2d2d2d', height=50)
        title_frame.pack(fill=tk.X, pady=(0, 10))
        title_frame.pack_propagate(False)
        
        # File name display
        self.file_label = tk.Label(
            title_frame, 
            text="Untitled - Modern Notepad", 
            font=self.title_font,
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.file_label.pack(side=tk.LEFT, padx=15, pady=15)
        
        # Status label
        self.status_label = tk.Label(
            title_frame,
            text="Ready",
            font=("Segoe UI", 9),
            fg='#888888',
            bg='#2d2d2d'
        )
        self.status_label.pack(side=tk.RIGHT, padx=15, pady=15)
        
        # Toolbar
        toolbar_frame = tk.Frame(main_frame, bg='#2d2d2d', height=45)
        toolbar_frame.pack(fill=tk.X, pady=(0, 10))
        toolbar_frame.pack_propagate(False)
        
        # Toolbar buttons - File/Edit operations
        buttons = [
            ('📁 New', self.new_file),
            ('📄 Open', self.open_file),
            ('💾 Save', self.save_file),
            ('💾 Save As', self.save_as_file),
            ('✂️ Cut', self.cut),
            ('📋 Copy', self.copy),
            ('📌 Paste', self.paste),
            ('🔍 Find', self.find_text)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(
                toolbar_frame,
                text=text,
                font=self.button_font,
                bg='#3d3d3d',
                fg='#ffffff',
                activebackground='#4d4d4d',
                activeforeground='#ffffff',
                relief='flat',
                bd=0,
                padx=15,
                pady=8,
                cursor='hand2',
                command=command
            )
            btn.pack(side=tk.LEFT, padx=(0 if i == 0 else 5, 0))
        
        # Formatting toolbar section
        format_frame = tk.Frame(toolbar_frame, bg='#2d2d2d')
        format_frame.pack(side=tk.RIGHT)
        
        format_buttons = [
            ('𝐁', self.apply_bold, 'Bold (Ctrl+B)'),
            ('𝐈', self.apply_italic, 'Italic (Ctrl+I)'),
            ('𝐔', self.apply_underline, 'Underline (Ctrl+U)'),
            ('𝑺', self.apply_strikethrough, 'Strikethrough (Ctrl+T)')
        ]
        
        for text, command, tooltip in format_buttons:
            btn = tk.Button(
                format_frame,
                text=text,
                font=("Segoe UI", 11, "bold"),
                bg='#3d3d3d',
                fg='#ffffff',
                activebackground='#4d4d4d',
                activeforeground='#ffffff',
                relief='flat',
                bd=0,
                padx=12,
                pady=8,
                cursor='hand2',
                command=command
            )
            btn.pack(side=tk.LEFT, padx=2)
            btn.bind("<Enter>", lambda e, t=tooltip: self.show_tooltip(t))
            btn.bind("<Leave>", lambda e: self.hide_tooltip())
        
        # NEW: Font size dropdown section
        font_size_frame = tk.Frame(toolbar_frame, bg='#2d2d2d')
        font_size_frame.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Font size label
        self.font_size_label = tk.Label(
            font_size_frame,
            text="Size:",
            font=self.button_font,
            fg='#ffffff',
            bg='#2d2d2d'
        )
        self.font_size_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Font size dropdown
        self.font_size_var = tk.StringVar(value="12")
        self.font_size_menu = tk.OptionMenu(
            font_size_frame,
            self.font_size_var,
            *map(str, self.preset_sizes),
            command=self.on_font_size_change
        )
        self.font_size_menu.config(
            font=self.button_font,
            bg='#3d3d3d',
            fg='#ffffff',
            activebackground='#4d4d4d',
            activeforeground='#ffffff',
            relief='flat',
            bd=0,
            padx=10,
            pady=5,
            width=4,
            cursor='hand2'
        )
        self.font_size_menu["menu"].config(
            bg='#3d3d3d',
            fg='#ffffff',
            activebackground='#4d4d4d',
            activeforeground='#ffffff',
            font=self.button_font
        )
        self.font_size_menu.pack(side=tk.LEFT)
        
        # Text editor
        self.text_area = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            font=(self.base_font_family, self.current_font_size),
            bg='#1e1e1e',
            fg='#d4d4d4',
            insertbackground='#ffffff',
            selectbackground='#264f78',
            selectforeground='#ffffff',
            spacing1=4,
            spacing3=4,
            padx=15,
            pady=15
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Bind events
        self.text_area.bind('<KeyRelease>', self.on_text_change)
        self.text_area.bind('<Control-s>', lambda e: self.save_file())
        self.text_area.bind('<Control-n>', lambda e: self.new_file())
        self.text_area.bind('<Control-o>', lambda e: self.open_file())
        self.text_area.focus_set()
        
        # Auto-save timer
        self.auto_save()
    
    # NEW: Font size dropdown handler
    def on_font_size_change(self, selected_size):
        """Handle font size dropdown selection."""
        try:
            new_size = int(selected_size)
            if new_size != self.current_font_size:
                self.current_font_size = new_size
                self.update_font_size()
                self.update_status(f"Font size changed to {self.current_font_size}")
        except ValueError:
            pass
    
    def setup_text_formatting(self):
        """Configure text formatting tags and bind keyboard shortcuts."""
        self.configure_formatting_tags()
        self.text_area.bind('<Control-b>', lambda e: self.apply_bold())
        self.text_area.bind('<Control-i>', lambda e: self.apply_italic())
        self.text_area.bind('<Control-u>', lambda e: self.apply_underline())
        self.text_area.bind('<Control-t>', lambda e: self.apply_strikethrough())
    
    def update_font_size(self):
        """Update the text area font size and refresh formatting tags."""
        # Update main text area font
        font_tuple = (self.base_font_family, self.current_font_size)
        self.text_area.configure(font=font_tuple)
        
        # Update dropdown selection
        self.font_size_var.set(str(self.current_font_size))
        
        # Reconfigure all formatting tags with new base size
        self.configure_formatting_tags()
    
    def configure_formatting_tags(self):
        """Configure font-based formatting tags with current font size."""
        # Base font for modifications
        base_font = font.Font(family=self.base_font_family, size=self.current_font_size)
        
        # Bold tag
        bold_font = font.Font(family=base_font['family'], size=base_font['size'], weight='bold')
        self.text_area.tag_configure('bold', font=bold_font)
        
        # Italic tag
        italic_font = font.Font(family=base_font['family'], size=base_font['size'], slant='italic')
        self.text_area.tag_configure('italic', font=italic_font)
        
        # Underline tag
        underline_font = font.Font(family=base_font['family'], size=base_font['size'], underline=True)
        self.text_area.tag_configure('underline', font=underline_font)
        
        # Strikethrough tag (using overstrike)
        strike_font = font.Font(family=base_font['family'], size=base_font['size'], overstrike=True)
        self.text_area.tag_configure('strikethrough', font=strike_font)
    
    def _toggle_formatting(self, tag_name):
        """Toggle the specified formatting tag on selected text."""
        try:
            start = self.text_area.index('sel.first')
            end = self.text_area.index('sel.last')
        except tk.TclError:
            messagebox.showwarning("No Selection", "Please select text to format.")
            return
        
        # Check if tag is already applied to the entire selection
        has_tag = self.text_area.tag_ranges(f'{tag_name}_temp') or \
                  self.text_area.tag_ranges(tag_name)
        
        if has_tag:
            # Remove tag
            self.text_area.tag_remove(tag_name, start, end)
            self.text_area.tag_remove(f'{tag_name}_temp', start, end)
            self.update_status(f"Removed {tag_name}")
        else:
            # Apply tag
            self.text_area.tag_add(tag_name, start, end)
            self.update_status(f"Applied {tag_name}")
    
    # Formatting methods
    def apply_bold(self):
        """Apply or toggle bold formatting to selected text."""
        self._toggle_formatting('bold')
    
    def apply_italic(self):
        """Apply or toggle italic formatting to selected text."""
        self._toggle_formatting('italic')
    
    def apply_underline(self):
        """Apply or toggle underline formatting to selected text."""
        self._toggle_formatting('underline')
    
    def apply_strikethrough(self):
        """Apply or toggle strikethrough formatting to selected text."""
        self._toggle_formatting('strikethrough')
    
    def show_tooltip(self, text):
        """Show tooltip for buttons."""
        x = self.root.winfo_pointerx() + 10
        y = self.root.winfo_pointery() + 10
        self.tooltip = tk.Toplevel(self.root)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=text, background="#ffffe1", 
                        relief="solid", borderwidth=1, font=("Segoe UI", 9))
        label.pack()
    
    def hide_tooltip(self):
        """Hide tooltip."""
        if hasattr(self, 'tooltip'):
            self.tooltip.destroy()
    
    def setup_syntax_highlighting(self):
        self.text_area.tag_configure('keyword', foreground='#569cd6')
        self.text_area.tag_configure('string', foreground='#ce9178')
        self.text_area.tag_configure('comment', foreground='#6a9955')
        self.text_area.tag_configure('number', foreground='#b5cea8')
    
    def on_text_change(self, event=None):
        if self.current_file:
            self.file_label.config(text=f"{os.path.basename(self.current_file)}* - Modern Notepad")
        else:
            self.file_label.config(text="Untitled* - Modern Notepad")
        self.is_saved = False
        self.status_label.config(text=f"Modified | {len(self.text_area.get('1.0', tk.END).split())} words | Size: {self.current_font_size}")
    
    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.after(2000, lambda: self.status_label.config(
            text=f"Ready | {len(self.text_area.get('1.0', tk.END).split())} words | Size: {self.current_font_size}"
        ))
    
    def new_file(self):
        if not self.is_saved and self.text_area.get('1.0', tk.END).strip():
            if not messagebox.askyesno("Unsaved Changes", "Save changes before creating new file?"):
                return
            self.save_file()
        
        self.current_file = None
        self.text_area.delete('1.0', END)
        for tag in ['bold', 'italic', 'underline', 'strikethrough']:
            self.text_area.tag_remove(tag, '1.0', tk.END)
        self.file_label.config(text="Untitled - Modern Notepad")
        self.is_saved = True
        self.status_label.config(text=f"New file created | Size: {self.current_font_size}")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.text_area.delete('1.0', tk.END)
                for tag in ['bold', 'italic', 'underline', 'strikethrough']:
                    self.text_area.tag_remove(tag, '1.0', tk.END)
                self.text_area.insert('1.0', content)
                self.current_file = file_path
                self.file_label.config(text=f"{os.path.basename(file_path)} - Modern Notepad")
                self.is_saved = True
                self.update_status(f"Opened: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
    
    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    content = self.text_area.get('1.0', tk.END + '-1c')
                    file.write(content)
                self.is_saved = True
                self.file_label.config(text=f"{os.path.basename(self.current_file)} - Modern Notepad")
                self.update_status("Saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
        else:
            self.save_as_file()
    
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
        )
        if file_path:
            self.current_file = file_path
            self.save_file()
    
    def cut(self):
        self.text_area.event_generate('<<Cut>>')
    
    def copy(self):
        self.text_area.event_generate('<<Copy>>')
    
    def paste(self):
        self.text_area.event_generate('<<Paste>>')
    
    def find_text(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Find")
        search_window.geometry("300x120")
        search_window.configure(bg='#2d2d2d')
        search_window.transient(self.root)
        search_window.grab_set()
        
        tk.Label(search_window, text="Find:", bg='#2d2d2d', fg='#ffffff', font=self.button_font).pack(pady=10)
        
        search_var = tk.StringVar()
        entry = tk.Entry(search_window, textvariable=search_var, font=("Segoe UI", 10), bg='#3d3d3d', fg='#ffffff', insertbackground='#ffffff')
        entry.pack(pady=5, padx=20, fill=tk.X)
        entry.focus_set()
        
        def find():
            search_text = search_var.get()
            if search_text:
                content = self.text_area.get('1.0', tk.END)
                start = '1.0'
                self.text_area.tag_remove('highlight', '1.0', tk.END)
                pos = 0
                while True:
                    pos = content.find(search_text, pos)
                    if pos == -1:
                        break
                    end_pos = f"1.0+{pos + len(search_text)}c"
                    self.text_area.tag_add('highlight', f"1.0+{pos}c", end_pos)
                    self.text_area.tag_config('highlight', background='#264f78', foreground='#ffffff')
                    pos += 1
                if pos > 0:
                    self.text_area.see(f"1.0+{pos-1}c")
        
        tk.Button(search_window, text="Find Next", command=find, bg='#3d3d3d', fg='#ffffff', font=self.button_font).pack(pady=10)
    
    def auto_save(self):
        if not self.is_saved and self.current_file:
            # Auto-save to backup
            backup_path = self.current_file + ".autosave"
            try:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(self.text_area.get('1.0', tk.END + '-1c'))
            except:
                pass
        self.root.after(30000, self.auto_save)  # Every 30 seconds

def main():
    root = tk.Tk()
    app = ModernNotepad(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
