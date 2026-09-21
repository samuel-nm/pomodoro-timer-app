import tkinter as tk
from tkinter import messagebox
from config import STAGES

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
        self.current_stage_idx = 0
        self.time_left = 0
        self.running = False
        self.timer_id = None
        
        self.lbl_status = tk.Label(root, text="", font=("Helvetica", 14, "bold"), fg="#333333")
        self.lbl_status.pack(pady=20)
        
        self.lbl_timer = tk.Label(root, text="00:00", font=("Helvetica", 48, "bold"), fg="#e74c3c")
        self.lbl_timer.pack(pady=10)
        
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=20)
        
        self.btn_start = tk.Button(self.btn_frame, text="Start", width=10, command=self.start_timer)
        self.btn_start.grid(row=0, column=0, padx=5)
        
        self.btn_pause = tk.Button(self.btn_frame, text="Pause", width=10, command=self.pause_timer, state="disabled")
        self.btn_pause.grid(row=0, column=1, padx=5)
        
        self.btn_skip = tk.Button(self.btn_frame, text="Skip", width=10, command=self.next_stage)
        self.btn_skip.grid(row=0, column=2, padx=5)
        
        self.load_stage()

    def load_stage(self):
        if self.current_stage_idx >= len(STAGES):
            messagebox.showinfo("Done!", "All stages completed successfully!")
            self.current_stage_idx = 0
            
        stage = STAGES[self.current_stage_idx]
        self.lbl_status.config(text=stage["label"])
        self.time_left = stage["duration"] * 60
        self.update_timer_display()

    def update_timer_display(self):
        mins, secs = divmod(self.time_left, 60)
        self.lbl_timer.config(text=f"{mins:02d}:{secs:02d}")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.btn_start.config(state="disabled")
            self.btn_pause.config(state="normal")
            self.tick()

    def pause_timer(self):
        if self.running:
            self.running = False
            self.btn_start.config(state="normal")
            self.btn_pause.config(state="disabled")
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

    def next_stage(self):
        self.pause_timer()
        self.current_stage_idx = (self.current_stage_idx + 1) % len(STAGES)
        self.load_stage()

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer_display()
            self.timer_id = self.root.after(1000, self.tick)
        else:
            self.running = False
            self.btn_start.config(state="normal")
            self.btn_pause.config(state="disabled")
            messagebox.showinfo("Stage Finished", "Time is up!")
            self.next_stage()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
