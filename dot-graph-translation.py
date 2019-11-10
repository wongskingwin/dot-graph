import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Label data points
def label_data_points(x_values, y_values, ax, base_point_labels):
    i = 0
    for xy in zip(x_values, y_values):
        ax.annotate('{}({},{})'.format(base_point_labels[i], xy[0], xy[1]), xy=xy, textcoords='data')
        i += 1

# Translate points
def translate_points(x_values, y_values, scale_factor):
    i = 0
    number_of_starting_values = len(x_values)
    translated_x_values = []
    translated_y_values = []
    while i < number_of_starting_values:
        translated_x_values.append(x_values[i]*scale_factor)
        translated_y_values.append(y_values[i]*scale_factor)
        i+=1
    return(translated_x_values, translated_y_values)

# Plot a set of points and various transforms on them
def plot_points():
    # To graph another transform:
    #   1. Populate another set of x/y arrays.  Define new variables for the label and color
    #   2. Use the ax variable to make a new call to the scatter function, passing in your new x/y arrays, color, and label
    #   3. Add a call to label_data_points function, passing in your new x/y arrays

    # Set base x/y values
    base_x_values = [2,0,0,1,3,6,9,12,15,4,7,11,14,16,1,3,4,6,8,8,8,11,11,11,13,13,15,15,17,17,15,17]
    base_y_values = [13,11,10,9,9,9,10,12,14,11,12,13,14,15,4,7,4,7,4,7,8,7,3,5,6,4,7,4,4,6,6,7]
    base_point_labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","AB","AC","AD","AE", "AF"]
    base_graph_color = "black"

    # Get translated x/y values
    scale_factor = 2
    (translated_x_values, translated_y_values) = translate_points(base_x_values, base_y_values, scale_factor)
    translated_graph_color = "red"

    # Generate scatter graphs based on above x/y numbers
    fig, (ax, ax2) = plt.subplots(1, 2, sharex='all', sharey='all')
    ax.scatter(base_x_values, base_y_values, color = base_graph_color)
    ax2.scatter(translated_x_values, translated_y_values, color = translated_graph_color)

    # Label data points
    # Note base point labels are used for all points
    label_data_points(base_x_values, base_y_values, ax, base_point_labels)
    label_data_points(translated_x_values, translated_y_values, ax2, base_point_labels)

    # Set graph title
    ax.set_title("Base Dot Graph")
    ax2.set_title("Translated Dot Graph")

    # Format x/y axes and legend
    ax.axhline(0)
    ax.axvline(0)
    tick_interval = 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
    ax.legend()
    ax2.axhline(0)
    ax2.axvline(0)
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
    ax2.yaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
    ax2.legend()


    # Show graph
    plt.show()

if __name__ == '__main__':
    plot_points()
