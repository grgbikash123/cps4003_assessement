import matplotlib.pyplot as plt

def visualize_pie_chart(data):
    labels = data.keys()
    sizes = data.values()

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90 )

    # Adding legend
    ax.legend(wedges, labels, title="Departments", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Display the plot
    plt.show()


def visualize_histogram(data):
    # Assuming data is a list of distances
    plt.hist(data, bins=20, color='blue', edgecolor='black')
    plt.xlabel('Distance from Home')
    plt.ylabel('Frequency')
    plt.title('Histogram of Distance from Home')
    plt.grid(True)
    plt.show()
