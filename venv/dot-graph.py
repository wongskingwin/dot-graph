import matplotlib.pyplot as plt

# Generate reflection points on a horizontal axis
def reflect_points_on_horizontal_axis(x_values, y_values, reflection_y_intercept):
    i = 0
    number_of_starting_values = len(x_values)
    reflected_y_values = []
    while i < number_of_starting_values:
        reflected_y_values.append((reflection_y_intercept - y_values[i]) + reflection_y_intercept)
        i+=1
    return(x_values, reflected_y_values) # X values don't change when reflecting on a horizontal axis

# Plot a set of points and various transforms on them
def plot_points():

    # Initialize starting x/y values
    base_x_values = [1, 4, 9, 16, 25, -10]
    base_y_values = [1, 0, 3, 4, 5, -20]
    base_graph_label = "base graph"
    base_graph_color = "black"

    # Get reflected values
    (reflected_x_values, reflected_y_values) = reflect_points_on_horizontal_axis(base_x_values, base_y_values, 2)
    reflected_graph_name = "reflected graph"
    reflected_graph_color = "orange"

    # Generate scatter graph based on above x/y numbers
    plt.scatter(base_x_values, base_y_values, color = base_graph_color)
    plt.scatter(reflected_x_values, reflected_y_values, color = reflected_graph_color)

    # Set graph title and legend
    plt.title("Scatter Graph")
    plt.legend([base_graph_color + " - " + base_graph_label, reflected_graph_color + " - " + reflected_graph_name])

    # Format x/y axes
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.axhline(0)
    plt.axvline(0)

    # Show graph
    plt.show()

if __name__ == '__main__':
    plot_points()
