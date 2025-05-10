from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def create_histograms():
    # Load iris dataset 
    iris = load_iris()

    # Create a dictionary storing feature names and their corresponding data
    features = {
        'sepal_length': iris.data[:, 0],
        'sepal_width': iris.data[:, 1],
        'petal_length': iris.data[:, 2],
        'petal_width': iris.data[:, 3]
    }

    # Define colors
    colors = ['seagreen', 'lightgreen', 'darkorchid', 'plum']
    edgecolors = ['mediumseagreen', 'palegreen', 'mediumorchid', 'thistle']

    # Generate plots and store them in a list
    plots = []
    for i, (feature, values) in enumerate(features.items()):
        fig, ax = plt.subplots()
        ax.hist(values, color=colors[i], edgecolor=edgecolors[i])
        ax.set_xlabel('Dimensions (in cm)')
        ax.set_ylabel('N. in the dataset')
        ax.set_title(feature.replace('_', ' ').capitalize())
        plots.append((feature, fig))
    
    return plots

def save_histograms( plot_path):
    plots = create_histograms()
    for feature, fig in plots:
        fig.savefig(f'{plot_path}_{feature}.png', dpi=300, bbox_inches='tight')
        plt.close(fig)

if __name__ == '__main__':
    plots = create_histograms()
    for feature, fig in plots:
        plt.show()  # Display each plot
        
    