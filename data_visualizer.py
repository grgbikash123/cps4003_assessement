import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def create_chart_window(fig, title):
    """
    Create a new Tkinter window for a chart.

    Parameters:
        fig (matplotlib.figure.Figure): The Matplotlib figure object.
        title (str): The title of the chart.
    """
    chart_window = tk.Tk()
    chart_window.title(title)
    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Start the Tkinter main loop
    chart_window.mainloop()


def generate_pie_chart(data, title):
    """
    Generate a Pie Chart based on the given data.

    Parameters:
        data (dict): A dictionary where keys represent categories and values represent counts.
        title (str): The title of the pie chart.
    """
    fig, ax = plt.subplots()
    ax.pie(data.values(), labels=data.keys(), autopct="%1.1f%%")
    ax.set_title(title)

    create_chart_window(fig, title)


def generate_histogram(data, xlabel, ylabel, title):
    """
    Generate a histogram based on the given data.

    Parameters:
        data (list): A list of values for the histogram.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        title (str): The title of the histogram.
    """
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="blue", edgecolor="black")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)

    create_chart_window(fig, title)
