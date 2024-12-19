import tkinter as tk
from typing import Optional, Any

class PaintApp:
    def __init__(self, window: tk.Tk) -> None:
        self.window: tk.Tk = window
        self.window.title("ペイントツール")
        
        # キャンバスの作成
        self.canvas: tk.Canvas = tk.Canvas(self.window, width=600, height=400, bg='white')
        self.canvas.pack(expand=True, fill='both')
        
        # マウスイベントのバインド
        self.canvas.bind('<B1-Motion>', self.paint)  # マウスドラッグ時
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        
        # 前回の座標を保存する変数
        self.prev_x: Optional[int] = None
        self.prev_y: Optional[int] = None
    
    def paint(self, event: tk.Event) -> None:
        if self.prev_x is not None and self.prev_y is not None:
            # 前回の座標から現在の座標まで線を引く
            self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y,
                                  width=2, fill='black', smooth=True)
        self.prev_x = event.x
        self.prev_y = event.y
    
    def reset(self, event: tk.Event) -> None:
        # マウスボタンを離したときに座標をリセット
        self.prev_x = None
        self.prev_y = None

def main() -> None:
    window: tk.Tk = tk.Tk()
    app: PaintApp = PaintApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()