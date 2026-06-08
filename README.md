# ECommerce Mock Data Project
Data Analytics project utilizing Pandas, NumPy, MatPlotLib and Jupyter to manipulate a mock data set for visualization and analysis

## Functionality
A csv file containing the data is loaded into a DataFrame using Pandas in load_data.py. Here, the file is formatted using regular expressions to make date and dollar amounts consistent. Following this formatting change, the dataset is used to create a Database file.

The query_data.py file is where we utilize SQL queries to get an aggregate of each online merchants total revenue and average transaction value per month, as well as the number of unique customers for each merchant.
