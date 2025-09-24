import tkinter as tk
from PIL import Image, ImageTk

class ScreenSelection:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.config(bg="black")
        self.root.attributes("-topmost", True)

        self.start_x = None
        self.start_y = None
        self.rect = None
        self.result = None

        self.canvas = tk.Canvas(self.root, cursor="cross", bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("<Button-3>", lambda e: self.root.destroy())

        self.root.mainloop()

    def on_button_press(self, event):
        self.start_x = int(self.canvas.canvasx(event.x))
        self.start_y = int(self.canvas.canvasy(event.y))

        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline="white", width=2
        )

    def on_move_press(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = (int(self.canvas.canvasx(event.x)), int(self.canvas.canvasy(event.y)))
        self.result = (self.start_x, self.start_y, end_x, end_y)
        self.root.destroy()

    def get_region(self) -> tuple[int,int,int,int]:
        return self.result

class ImageRegion:
    def __init__(self, region: tuple[int, int, int, int], image: Image.Image):
        self.region = region
        self.image_path = image

        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        x1, y1, x2, y2 = self.region
        width = abs(x2 - x1)
        height = abs(y2 - y1)

        self.root.geometry(f"{width}x{height}+{x1}+{y1}")

        image = image.resize((width, height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(image)

        label = tk.Label(self.root, image=self.tk_image, borderwidth=0, highlightthickness=0)
        label.pack(fill=tk.BOTH, expand=True)

        self.root.bind("<Button-1>", lambda e: self.root.destroy())

        self.root.mainloop()

class ImageTopRight:
    def __init__(self, image: Image.Image):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        self.original_image = image
        self.current_image = image
        self.tk_image = ImageTk.PhotoImage(self.current_image)

        self.width, self.height = self.current_image.size
        screen_width = self.root.winfo_screenwidth()
        x = screen_width - self.width
        y = 0
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

        self.label = tk.Label(self.root, image=self.tk_image, borderwidth=0, highlightthickness=0)
        self.label.pack(fill=tk.BOTH, expand=True)

        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)

        self.label.bind("<MouseWheel>", self.zoom)

        self.label.bind("<Double-Button-1>", lambda e: self.root.destroy())

        self.offset_x = 0
        self.offset_y = 0

        self.root.mainloop()

    def start_move(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def do_move(self, event):
        x = self.root.winfo_x() + (event.x - self.offset_x)
        y = self.root.winfo_y() + (event.y - self.offset_y)
        self.root.geometry(f"+{x}+{y}")

    def zoom(self, event):
        scale = 1.1 if event.delta > 0 else 0.9
        new_width = int(self.current_image.width * scale)
        new_height = int(self.current_image.height * scale)
        self.current_image = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.current_image)
        self.label.config(image=self.tk_image)
        self.width, self.height = self.current_image.size
        self.root.geometry(f"{self.width}x{self.height}+{self.root.winfo_x()}+{self.root.winfo_y()}")

