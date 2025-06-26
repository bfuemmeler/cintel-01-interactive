from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt
#
# Data for the histogram

rng = np.random.default_rng(seed=2025)
data = rng.normal(loc=0, scale=1, size=1000)

app_ui = ui.page_navbar(
    ui.nav_panel(
        "Histogram",
        ui.input_slider(
            "selected_number_of_bins",
            "Number of Bins",
            min=0,
            max=100,
            value=20
        ),
        ui.output_plot("histogram"),
    ),
    title="Exploring Distribution"
)

def server(input,output, session):

    @output
    @render.plot(alt="Normalized histogram of the data")
    def histogram():
        """Reactive plot: redraws when the slider value changes."""
        n_bins = max(input.selected_number_of_bins(), 1)

        plt.figure()
        plt.hist(data, bins=n_bins, density=True)
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.title(f"Histogram with {n_bins} bins")
        plt.tight_layout()

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
