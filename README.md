# garden.matplotlib

`garden.matplotlib` is a Kivy garden package that provides a simple way to embed Matplotlib plots and charts in Kivy applications. This package makes it easy to integrate powerful data visualization tools into your Kivy apps, allowing you to create interactive, high-quality data visualizations with ease.

## Installation

This repository uses the legacy kivy garden flower format. To install `garden.matplotlib`, simply add it to your Kivy garden using the most up-to-date [legacy garden tool instructions](https://kivy.org/doc/stable/api-kivy.garden.html#legacy-garden-tool-instructions).

```cmd
pip install garden
garden install matplotlib
```

## Usage

Using `garden.matplotlib` is simple. To embed a Matplotlib plot in your Kivy app, simply create a `FigureCanvasKivyAgg` widget and add it to your app as you would any other Kivy widget:

```python
import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class MyPlotApp(App):
    def build(self):
        # Create a box layout for the app
        layout = BoxLayout(orientation='vertical')

        # Create a Matplotlib figure and canvas
        fig, ax = plt.subplots()
        canvas = FigureCanvasKivyAgg(fig)

        # Add the canvas to the app layout
        layout.add_widget(canvas)

        # Plot the data
        ax.plot([1, 2, 3, 4])

        # Redraw the canvas
        canvas.draw_idle()

        return layout

MyPlotApp().run()
```

## Contributing

If you find a bug or have an idea for a new feature, we welcome contributions from the community. To contribute to `garden.matplotlib`, simply fork the repository, make your changes, and submit a pull request. We'll review your changes and merge them into the repository if they meet our standards and requirements.

## License

`garden.matplotlib` is released under the MIT license. See the `LICENSE` file for more information.
