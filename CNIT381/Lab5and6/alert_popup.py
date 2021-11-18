import tkinter as tk


def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = tk.Tk()
    root.title(title)
    w = 400
    h = 200
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w,h,x,y))
    m = message 
    m += '\n'
    m += path
    w = tk.Label(root, text=m, width=120, height=10)
    w.pack()
    b = tk.Button(root, text="Ok", command=root.destroy, width=10)
    b.pack()
    tk.mainloop()