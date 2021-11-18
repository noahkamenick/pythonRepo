from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
import challenge2 as c

button = widgets.Button(description="Emergency Shutdown")
output = widgets.Output()
display(button, output)

# Button Callback (action)
def on_button_clicked(b):
    with output:
        print("Emergency Shutdown")
        c.shutdown_int('Loopback0')

button.on_click(on_button_clicked)