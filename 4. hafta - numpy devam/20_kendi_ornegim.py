import cv2
import numpy as np
import tkinter as tk
from tkinter import colorchooser, ttk
from PIL import Image, ImageTk


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Benzeri Renk Paleti")
        self.root.geometry("1000x600")

        # Ana pencereyi yapılandır
        self.canvas_frame = tk.Frame(root, bg="white")
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Kontrol paneli
        self.control_panel = tk.Frame(root, bg="#f0f0f0", width=200)
        self.control_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Canvas oluştur
        self.canvas_width, self.canvas_height = 700, 500
        self.canvas = tk.Canvas(self.canvas_frame, bg="white", width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # OpenCV için boş bir resim oluştur
        self.image = np.ones((self.canvas_height, self.canvas_width, 3), dtype=np.uint8) * 255
        self.display_image()

        # Değişkenler
        self.current_color = (0, 0, 0)  # Varsayılan siyah
        self.brush_size = 5
        self.last_x, self.last_y = None, None

        # Renk paleti
        self.create_color_palette()

        # Fırça boyutu ayarı
        self.create_brush_size_slider()

        # Canvas olayları
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        # Temizle düğmesi
        self.clear_button = tk.Button(self.control_panel, text="Temizle", command=self.clear_canvas)
        self.clear_button.pack(pady=10, fill=tk.X)

        # Kaydet düğmesi
        self.save_button = tk.Button(self.control_panel, text="Kaydet", command=self.save_image)
        self.save_button.pack(pady=10, fill=tk.X)

    def create_color_palette(self):
        # Renk paleti etiketi
        tk.Label(self.control_panel, text="Renk Paleti").pack(pady=5)

        # Temel renkler çerçevesi
        colors_frame = tk.Frame(self.control_panel)
        colors_frame.pack(pady=5)

        # Temel renkler
        basic_colors = [
            "#000000", "#808080", "#800000", "#808000", "#008000",
            "#008080", "#000080", "#800080", "#ff0000", "#00ff00",
            "#0000ff", "#ffff00", "#00ffff", "#ff00ff", "#ffffff"
        ]

        # Renk düğmeleri oluştur
        row, col = 0, 0
        for color in basic_colors:
            tk.Button(
                colors_frame,
                bg=color,
                width=2,
                height=1,
                command=lambda c=color: self.select_color(c)
            ).grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Özel renk seçici düğmesi
        tk.Button(
            self.control_panel,
            text="Özel Renk Seç",
            command=self.choose_custom_color
        ).pack(pady=10, fill=tk.X)

        # Mevcut renk göstergesi
        self.current_color_display = tk.Canvas(self.control_panel, width=80, height=30, bg="#000000")
        self.current_color_display.pack(pady=5)

    def create_brush_size_slider(self):
        # Fırça boyutu etiketi
        tk.Label(self.control_panel, text="Fırça Boyutu").pack(pady=5)

        # Fırça boyutu kaydırıcısı
        self.brush_slider = ttk.Scale(
            self.control_panel,
            from_=1,
            to=50,
            orient=tk.HORIZONTAL,
            value=self.brush_size,
            command=self.update_brush_size
        )
        self.brush_slider.pack(fill=tk.X, pady=5)

        # Fırça boyutu değeri göstergesi
        self.brush_size_label = tk.Label(self.control_panel, text=f"Boyut: {self.brush_size}")
        self.brush_size_label.pack(pady=5)

    def update_brush_size(self, value):
        self.brush_size = int(float(value))
        self.brush_size_label.config(text=f"Boyut: {self.brush_size}")

    def select_color(self, color):
        # HEX rengini RGB'ye dönüştür
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        self.current_color = (b, g, r)  # OpenCV BGR formatı
        self.current_color_display.config(bg=color)

    def choose_custom_color(self):
        color = colorchooser.askcolor(title="Özel Renk Seç")
        if color[1]:  # Eğer bir renk seçildiyse
            self.select_color(color[1])

    def display_image(self):
        # OpenCV görüntüsünü Tkinter'da göster
        self.img = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        self.photo = ImageTk.PhotoImage(image=self.img)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            # OpenCV kullanarak çizim yap
            cv2.line(
                self.image,
                (self.last_x, self.last_y),
                (event.x, event.y),
                self.current_color,
                self.brush_size
            )
            # Görüntüyü güncelle
            self.display_image()
            self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        # Temizle
        self.image = np.ones((self.canvas_height, self.canvas_width, 3), dtype=np.uint8) * 255
        self.display_image()

    def save_image(self):
        # Görüntüyü kaydet
        filename = 'paint_resim.png'
        cv2.imwrite(filename, self.image)
        tk.messagebox.showinfo("Bilgi", f"Resim {filename} olarak kaydedildi!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()