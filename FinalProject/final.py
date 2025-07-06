"""
Svita Kiran

CS152A
Final Project: Simulation of the Rescorla-Wagner Model with Python
12/8/23

This program implements a GUI simulation of the Rescorla-Wagner learning model, a classical conditioning model
used to estimate associative strength between a conditioned stimulus (CS) and an unconditioned stimulus (US).
The simulation allows users to adjust parameters such as the learning rate and unconditioned stimulus
intensity to change their impact on the associative strength through many trials.

python3 final.py

"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RescorlaWagnerSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Rescorla-Wagner Model Simulation")

        # Parameters
        self.alpha = tk.DoubleVar(value=0.1)
        self.beta = tk.DoubleVar(value=1.0)
        self.lambda_val = tk.DoubleVar(value=0.5)

        # Simulation variables
        self.trials = 50
        self.associative_strength = [0.0]

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Learning Rate Slider
        ttk.Label(self.root, text="Learning Rate (α):").pack()
        alpha_slider = ttk.Scale(self.root, from_=0.01, to=1.0, variable=self.alpha, orient=tk.HORIZONTAL)
        alpha_slider.pack()

        # US Intensity Slider
        ttk.Label(self.root, text="US Intensity (λ):").pack()
        lambda_slider = ttk.Scale(self.root, from_=0.01, to=1.0, variable=self.lambda_val, orient=tk.HORIZONTAL)
        lambda_slider.pack()

        # Run Simulation Button
        run_button = ttk.Button(self.root, text="Run Simulation", command=self.run_simulation)
        run_button.pack()

        # Matplotlib Figure for Plot
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    def run_simulation(self):
        self.associative_strength = [0.0]
        for _ in range(1, self.trials + 1):
            delta_v = self.alpha.get() * self.beta.get() * (self.lambda_val.get() - self.associative_strength[-1])
            new_strength = self.associative_strength[-1] + delta_v
            self.associative_strength.append(new_strength)

        # Update Matplotlib Plot
        self.ax.clear()
        self.ax.plot(range(self.trials + 1), self.associative_strength, marker='o')
        self.ax.set_xlabel('Trials')
        self.ax.set_ylabel('Associative Strength')
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = RescorlaWagnerSimulator(root)
    root.mainloop()
