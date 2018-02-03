import tkinter as tk
import tkinter.messagebox as MB
import firstrun
import subprocess


class gooeybread:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.wm_title("Gooey Bread - Linux, Nvidia, CCMiner")
        self.main_window.geometry("500x100")
        self.top_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        self.middle_frame = tk.Frame()
        self.second_middle = tk.Frame()
        self.prompt_label = tk.Label(self.top_frame,
                                     text="Enter your preferred pool and your address. ")
        self.pool = tk.Entry(self.middle_frame,
                             width=20)
        self.pool_id = tk.Label(self.middle_frame,
                                text="Pool: ")
        self.address_id = tk.Label(self.second_middle,
                                   text="Address: ")
        self.address = tk.Entry(self.second_middle,
                                width=20)
        self.prompt_label.pack(side="left")
        self.pool_id.pack(side="left")
        self.pool.pack(side="right")
        self.address_id.pack(side="left")
        self.address.pack(side="right")
        self.first_run = tk.Button(self.bottom_frame,
                                   text="First run?",
                                   command=self.check_install)

        self.start_mining = tk.Button(self.bottom_frame,
                                      text="Start mining",
                                      command=self.start_mining)
        self.quit_button = tk.Button(self.bottom_frame,
                                     text="Quit",
                                     command=self.main_window.destroy)

        self.first_run.pack(side="left")
        self.start_mining.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.second_middle.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def check_install(self):
        if MB.askyesno("Install", "Do you want Gooey Bread to automatically configure the miner?"):
            firstrun.prereq()

    def start_mining(self):
        MB.showinfo("Mining in progress...", "Now mining! Click 'quit' to stop. ")
        runMine = subprocess.run(['./ccminer', '--algo=scrypt:10', '-o', str(
            self.pool.get()), '-u', str(self.address.get()), '--max_temp=85'])


gooeybread = gooeybread()
