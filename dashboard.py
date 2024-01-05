import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def show_home(data, root):
    # Chart 1: Bar chart of Age Distribution
    ages = [int(staff["Age"]) for staff in data]
    age_distribution = {age: ages.count(age) for age in set(ages)}

    fig1, ax1 = plt.subplots()
    ax1.bar(age_distribution.keys(), age_distribution.values())
    ax1.set_title("Age Distribution")
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Count")

    # --------------------------------------------------------------------------

    # Chart 2: Pie chart of Gender Distribution
    genders = [staff["Gender"] for staff in data]
    gender_distribution = {gender: genders.count(gender) for gender in set(genders)}

    fig2, ax2 = plt.subplots()
    ax2.pie(
        gender_distribution.values(),
        labels=gender_distribution.keys(),
        autopct="%1.1f%%",
        startangle=90,
    )
    ax2.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title("Gender Distribution")

    # --------------------------------------------------------------------------

    # Chart 3: Bar chart of Department Distribution
    departments = [staff["Department"] for staff in data]
    department_distribution = {
        department: departments.count(department) for department in set(departments)
    }

    fig3, ax3 = plt.subplots()
    ax3.bar(department_distribution.keys(), department_distribution.values())
    ax3.set_title("Department Distribution")
    ax3.set_xlabel("Department")
    ax3.set_ylabel("Count")

    # --------------------------------------------------------------------------

    # Chart 4: Box plot for Hourly Rate Distribution
    hourly_rates = [float(row["HourlyRate"]) for row in data]
    fig4, ax4 = plt.subplots()
    boxprops = dict(facecolor="lightblue", color="black")
    ax4.boxplot(hourly_rates, patch_artist=True, boxprops=boxprops)
    ax4.set_title("Hourly Rate Distribution (Box Plot)")
    ax4.set_ylabel("Hourly Rate")

    # --------------------------------------------------------------------------

    # Chart 5: Box plot for Attrition Rate

    attrition = [row["Attrition"] for row in data]

    # Calculate attrition rate over time
    attrition_rate = [
        attrition[: i + 1].count("Yes") / (i + 1) * 100 for i in range(len(attrition))
    ]
    fig5, ax5 = plt.subplots()
    ax5.plot(range(1, len(attrition_rate) + 1), attrition_rate, marker="o")
    ax5.set_title("Attrition Rate Over Time")
    ax5.set_xlabel("Number of Employees")
    ax5.set_ylabel("Attrition Rate (%)")

    charts_frame = tk.Frame(root)
    charts_frame.pack()

    # --------------------------------------------------------------------------
    # Number of male female and total Employees
    # --------------------------------------------------------------------------
    genders = [row["Gender"] for row in data]
    num_males = genders.count("Male")
    num_females = genders.count("Female")

    # ---------------------------------------------------------------------------------------------------------------------

    upper_frame = tk.Frame(charts_frame)
    upper_frame.pack(pady=10, expand=True)

    canvas = tk.Canvas(upper_frame, width=550, height=550, bg="white")
    center_x = canvas.winfo_reqwidth() / 2
    center_y = canvas.winfo_reqheight() / 6
    canvas.pack(padx=5, side=tk.LEFT)
    canvas.create_text(
        center_x,
        center_y,
        text=f"\n\n\n\n\n\n\n\n\n\n\n\n\n\nMale Employees   : {num_males}\nFemale Employees : {num_females}\nTotal Employees  : {num_males + num_females}",
        fill="black",
        font=("JetBrains Mono", 15),
    )

    canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT, fill="both", expand=True, padx=5)

    canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left", fill="both", expand=True, padx=5)

    # ---------------------------------------------------------------------------------------------------------------------
    lower_frame = tk.Frame(charts_frame)
    lower_frame.pack(pady=10, fill="both", expand=True)

    canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side="left", fill="both", expand=True, padx=5)

    canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
    canvas4.draw()
    canvas4.get_tk_widget().pack(side="left", expand=True, padx=5)

    canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
    canvas5.draw()
    canvas5.get_tk_widget().pack(side="left", fill="both", expand=True, padx=5)


def display_dashboard(retriever):
    root = tk.Tk()
    root.title("Dashboard")
    # root.state("zoomed")                     # uncomment if below doesn't work, this doesn't work for linux X11

    data = retriever.data

    # -----------------------------------------------------------------------------------------------------------
    #                       Dashboard at top_frame
    # -----------------------------------------------------------------------------------------------------------
    top_frame = tk.Frame(root, bg="#4C2A85")
    top_frame.pack(fill="x")
    label1 = tk.Label(
        top_frame,
        text="\tCPS4003 – Programming Principles and Techniques : Nurse Attrition data",
        bg="#4C2A85",
        fg="#FFF",
        font=("JetBrainsMono Nerd Font Propo", 25),
    )
    label1.pack(side="left")

    ## HOME button
    show_home(data, root)

    exit_button = tk.Button(
        top_frame,
        text="Exit",
        bg="#4C2A85",
        fg="#FFF",
        font=("JetBrainsMono Nerd Font Propo", 15),
        command=lambda: root.destroy(),
        padx=92,
        pady=20,
    )
    exit_button.pack()

    root.mainloop()