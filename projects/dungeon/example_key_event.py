# %%
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import patches

# %%
# Disable the default 's' shortcut
plt.rcParams['keymap.save'] = ['ctrl+s']

# %%
class PressKeySimulator:
    def __init__(self):
        
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_title("Simulator showing the key letter", fontsize=16)
        self.ax.set_aspect('equal')
        self.ax.set_xlim(0, 16)
        self.ax.set_ylim(0, 16)

        rect_patch = patches.Rectangle(xy=(2, 2), width=12, height=12, 
                                       edgecolor='blue', facecolor='#dcdcdc',
                                       linewidth=2.5)
        self.ax.add_patch(rect_patch)

        self.letter = self.ax.text(8, 8, f"NOTHING", 
                                   fontsize=36, color='red',
                                   horizontalalignment='center', verticalalignment='center',
                                   transform=self.ax.transData)
        self.instruction = self.ax.text(8, 11, f"Press Arrow keys or 'a', 's', 'w', 'd'\n\n" +
                                        f"Press 'x' to exit", 
                                        fontsize=18, horizontalalignment='center', 
                                        transform=self.ax.transData)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)

        print(f"Simulator started. Press any key to show the letter")
        plt.show()

    def on_key(self, event):
        
        # This code can be refactored to be shorter. But I deliberately write this long
        # so that you can understand event.key is a string.
        if event.key == 'left':
            self.letter.set_text('A')
        elif event.key == 'right':
            self.letter.set_text('D')
        elif event.key == 'up':
            self.letter.set_text('W')
        elif event.key == 'down':
            self.letter.set_text('S')
        elif event.key == 'a' or event.key == 'A':
            self.letter.set_text("LEFT")
        elif event.key == 'd' or event.key == 'D':
            self.letter.set_text("RIGHT")
        elif event.key == 's' or event.key == 'S':
            self.letter.set_text("DOWN")
        elif event.key == 'w' or event.key == 'W':
            self.letter.set_text('UP')
        elif event.key == 'x' or event.key == 'X':
            print("Exit the simulator")
            plt.close(self.fig)
            return
        else:
            print("Other keys are ignored")
            self.letter.set_text("Other keys are ignored")
            return  # ignore other keys

        self.fig.canvas.draw()

PressKeySimulator()