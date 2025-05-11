# Analyse
# Main program for the project. This script carries out the full analysis of the Iris dataset and saves the outputs to a folder named 'plots'.

# import custom modules and packages required to run the program 
from modules.read_dataset import read
from modules.summary import summary
from modules.histograms import save_histograms
from modules.scatter import save_scatter
from modules.boxplots import save_boxplots 
from modules.heatmap import save_heatmap, save_correlation_matrix
from modules.linear_regression import save_regression
from modules.pairplot import save_pairplot
import os 
import logging

# Setup logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Helper function to safely run modules
# This function will log the start and end of each module execution, as well as any errors that occur. source: https://chatgpt.com/share/6820be4d-57b0-800f-8b38-03913e815e8b
def run_module(name, func, *args, **kwargs):
    logger.info(f"Running module: {name}")
    try:
        func(*args, **kwargs)
        logger.info(f"Completed module: {name}")
    except Exception as e:
        logger.error(f"Error in module '{name}': {e}", exc_info=True)

# Create the directory to save the plots
try: 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plot_dir = os.path.join(script_dir, 'plots')
    os.makedirs(plot_dir, exist_ok=True)
    logger.info(f"'plots' directory ready at: {plot_dir}")
except Exception as e:
    logger.critical(f"Fatal error creating 'plots' directory: {e}", exc_info=True)
    exit(1)

# 1. Read and explore dataset
run_module("Read Dataset", read)

# 2. Save summary
summary_path = os.path.join(plot_dir, '02_summary.txt')
run_module("Summary", summary, summary_path)

# 3. Save histograms
hist_path = os.path.join(plot_dir, '03')
run_module("Histograms", save_histograms, hist_path)

# 4. Save boxplots
boxplot_path = os.path.join(plot_dir, '04')
run_module("Boxplots", save_boxplots, boxplot_path)

# 5. Save scatter plots
scatter_path = os.path.join(plot_dir, '05')
run_module("Scatter Plots", save_scatter, scatter_path)

# 6. Save linear regression plots
regression_path = os.path.join(plot_dir, '06')
run_module("Linear Regression", save_regression, regression_path)

# 7. Save heatmap and correlation matrix
corr_path = os.path.join(plot_dir, '07')
run_module("Heatmap", save_heatmap, corr_path)
run_module("Correlation Matrix", save_correlation_matrix, corr_path)

# 8. Save pairplot
pairplot_path = os.path.join(plot_dir, '08')
run_module("Pairplot", save_pairplot, pairplot_path)