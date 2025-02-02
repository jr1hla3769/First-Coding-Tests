import tkinter as tk
from tkinter import ttk, font
import math

class ValentineCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Valentine's Card")
        
        # Set window size and background
        self.root.geometry("500x700")
        self.root.configure(bg='#FFE4E8')
        
        # Create main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(expand=True, fill='both')
        
        # Create front and back frames
        self.front_frame = ttk.Frame(self.main_frame)
        self.back_frame = ttk.Frame(self.main_frame)
        
        # Configure custom styles
        self.setup_styles()
        self.setup_front_page()
        self.setup_back_page()
        
        # Show front page initially
        self.show_front_page()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#FFE4E8')
        self.style.configure('TLabel', background='#FFE4E8', font=('Palatino', 12))
        self.style.configure('Title.TLabel', font=('Palatino', 24, 'bold'))
        self.style.configure('Message.TLabel', font=('Palatino', 14))
        self.style.configure('Signature.TLabel', font=('Palatino', 14, 'italic'))
        
    def setup_front_page(self):
        self.front_frame.configure(style='TFrame')
        
        # Create canvas for heart
        self.canvas = tk.Canvas(self.front_frame, width=300, height=300, 
                              bg='#FFE4E8', highlightthickness=0)
        self.canvas.pack(pady=20)
        
        # Draw 3D heart
        self.draw_3d_heart()
        
        # Add title
        title = ttk.Label(self.front_frame, 
                         text="Happy Valentine's Day!",
                         style='Title.TLabel')
        title.pack(pady=10)
        
        # Add instruction
        instruction = ttk.Label(self.front_frame,
                              text="Click anywhere to open ❤️",
                              style='TLabel')
        instruction.pack(pady=5)
        
        # Bind click event
        self.front_frame.bind('<Button-1>', lambda e: self.show_back_page())
        self.canvas.bind('<Button-1>', lambda e: self.show_back_page())
        
    def setup_back_page(self):
        self.back_frame.configure(style='TFrame')
        
        # Container for message
        message_frame = ttk.Frame(self.back_frame)
        message_frame.pack(expand=True, fill='both', padx=40, pady=40)
        
        # Dear message
        dear = ttk.Label(message_frame, 
                        text="Querida Silvana,",
                        style='Message.TLabel')
        dear.pack(anchor='w', pady=(0, 20))
        
        # Main message
        message = ttk.Label(message_frame, 
                          text="""Te quiero cada dia mas. Jamas pensé que 
podría ser tan afortunado o feliz en mi 
vida. Pero contigo siento que nada es 
imposible.

Espero que disfrutes de este dia y que 
lo pasemos bien juntitos.

Te adoro mija bonita.""",
                          style='Message.TLabel',
                          justify='left')
        message.pack(pady=10)
        
        # Signature
        signature = ttk.Label(message_frame,
                            text="\nTuyo,\nJacobito",
                            style='Signature.TLabel',
                            justify='left')
        signature.pack(anchor='w', pady=(20, 0))
        
        # Close button
        close_btn = ttk.Button(self.back_frame, text="Close",
                              command=self.show_front_page)
        close_btn.pack(pady=20)
        
    def draw_3d_heart(self):
        # Enhanced 3D effect with more layers for fuller shape
        colors = ['#FF9999', '#FF8080', '#FF6666', '#FF4D4D', '#FF3333', '#FF1A1A', '#FF0000']
        offsets = [(6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)]
        
        # Draw shadow layers
        for offset, color in zip(offsets, colors):
            points = self.calculate_heart_points(90, offset)
            self.canvas.create_polygon(points, fill=color, outline=color)
            
        # Draw highlight
        highlight_points = self.calculate_heart_points(80, (-2, -2))
        self.canvas.create_polygon(highlight_points, fill='#FF6666', outline='#FF6666')
        
    def calculate_heart_points(self, size, offset=(0, 0)):
        points = []
        center_x = 150 + offset[0]
        center_y = 150 + offset[1]
        
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            # Modified equations for fuller heart shape
            x = size * (16 * math.sin(rad) ** 3) / 16
            y = -size * (13 * math.cos(rad) - 5 * math.cos(2*rad) - 2 * math.cos(3*rad) - math.cos(4*rad)) / 16
            points.extend([center_x + x, center_y + y])
            
        return points
        
    def show_front_page(self):
        self.back_frame.pack_forget()
        self.front_frame.pack(expand=True, fill='both')
        
    def show_back_page(self):
        self.front_frame.pack_forget()
        self.back_frame.pack(expand=True, fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    app = ValentineCard(root)
    root.mainloop()
    