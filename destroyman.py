import os
import tkinter as tk

# Declare window
window = tk.Tk()

# Some variables
taskbarHeight = 48

windowSize = [200, 200]
windowSizeString = str(windowSize[0]) + 'x' + str(windowSize[1])

windowPosition = [100, window.winfo_screenheight() - windowSize[1] - taskbarHeight]
windowPositionString = str(windowPosition[0]) + '+' + str(windowPosition[1])

path = os.getcwd() + '\\'


# Window stuff
window.geometry(windowSizeString + '+' + windowPositionString)
window.overrideredirect(True)
window.lift()
window.attributes('-topmost', True)
window.attributes('-transparentcolor', '#F0F0F0')

# Frame stuff
frame = tk.Frame(window, bg='#F0F0F0')
frame.pack(fill='both', expand=True)


# Call action .gif to an array
idle = [tk.PhotoImage(file = path + 'idle.gif', format = 'gif -index %i' %(i)).subsample(3) for i in range(2)]
talking = [tk.PhotoImage(file = path + 'talking.gif', format = 'gif -index %i' %(i)).subsample(3) for i in range(2)]
walking = [tk.PhotoImage(file = path + 'walking.gif', format = 'gif -index %i' %(i)).subsample(3) for i in range(2)]

# Init images
sprite = tk.Label(window, image = idle[0]).pack()

window.mainloop()