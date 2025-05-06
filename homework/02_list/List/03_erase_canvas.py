"""Implement an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white."""
import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()
        
        self.eraser = None
        self.cells = []  # Keep track of blue cells

        self.create_grid()
        self.canvas.bind("<Button-1>", self.create_eraser)

        # Mouse tracking
        self.canvas.bind("<Motion>", self.track_mouse)
        self.mouse_x = 0
        self.mouse_y = 0

    def create_grid(self):
        rows = CANVAS_HEIGHT // CELL_SIZE
        cols = CANVAS_WIDTH // CELL_SIZE

        for row in range(rows):
            for col in range(cols):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                self.cells.append(cell)

    def create_eraser(self, event):
        if self.eraser is not None:
            return  # Only one eraser

        x1 = event.x
        y1 = event.y
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE
        self.eraser = self.canvas.create_rectangle(x1, y1, x2, y2, fill="pink", outline="black")
        self.update_eraser()

    def track_mouse(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def update_eraser(self):
        if self.eraser is None:
            return

        while True:
            # Move eraser to current mouse position
            self.canvas.coords(self.eraser, self.mouse_x, self.mouse_y,
                               self.mouse_x + ERASER_SIZE, self.mouse_y + ERASER_SIZE)

            # Detect overlap with blue cells
            overlapping = self.canvas.find_overlapping(self.mouse_x, self.mouse_y,
                                                       self.mouse_x + ERASER_SIZE,
                                                       self.mouse_y + ERASER_SIZE)

            for item in overlapping:
                if item != self.eraser and item in self.cells:
                    self.canvas.itemconfig(item, fill="white")

            self.canvas.update()
            time.sleep(0.05)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
