import numpy as np
import math

# maze_cost_array = np.zeros((9,9))

# print(maze_cost_array)

# test comment

class Maze:
    def __init__(self, set_grid_size = 3):
        self.gridsize = set_grid_size
        # Sets the goal coord to the middle of the maze
        self.goal_coords = (math.floor(set_grid_size / 2),math.floor(set_grid_size / 2))

        self.initial_costgrid = self.intialise_costgrid()

    def intialise_costgrid(self):
        self.empty_costgrid = np.zeros((self.gridsize,self.gridsize))

        # manhattandistance
        for idx in range()

        return self.empty_costgrid



class DataProcessor:
    """
    A class to process and analyze data from various sources.
    
    This class provides functionality for loading, cleaning, transforming,
    and analyzing data. It supports multiple file formats and offers
    various analysis methods.
    """
    
    def __init__(self, source_path=None):
        """
        Initialize the DataProcessor with an optional data source.
        
        Parameters:
        -----------
        source_path : str, optional
            Path to the data source file. If not provided, data must be
            loaded separately using the load_data method.
        """
        # Will store the source file path
        # Will initialize empty data container
        # Will set up configuration parameters
        pass
    
    def load_data(self, file_path, file_type=None):
        """
        Load data from the specified file path.
        
        Parameters:
        -----------
        file_path : str
            Path to the data file to be loaded.
        file_type : str, optional
            Type of file ('csv', 'json', 'excel', etc.). If not provided,
            will be inferred from the file extension.
            
        Returns:
        --------
        bool
            True if data loaded successfully, False otherwise.
        """
        # Will detect file type if not provided
        # Will use appropriate reader based on file type
        # Will validate that data was loaded correctly
        # Will store data in internal data structure
        pass
    
    def clean_data(self, columns=None):
        """
        Clean the loaded data by handling missing values, outliers, etc.
        
        Parameters:
        -----------
        columns : list, optional
            List of column names to clean. If None, all columns will be processed.
            
        Returns:
        --------
        dict
            Statistics about the cleaning process (e.g., number of removed rows)
        """
        # Will check if data is loaded
        # Will handle missing values (delete or impute)
        # Will remove duplicates
        # Will handle outliers
        # Will track and return cleaning statistics
        pass
    
    def transform_data(self, transformations):
        """
        Apply specified transformations to the data.
        
        Parameters:
        -----------
        transformations : dict
            Dictionary mapping column names to transformation functions.
            
        Returns:
        --------
        bool
            True if transformations were applied successfully.
        """
        # Will apply each transformation to specified columns
        # Will validate results of transformations
        # Will update internal data with transformed values
        pass
    
    def analyze(self, method, parameters=None):
        """
        Perform analysis on the data using the specified method.
        
        Parameters:
        -----------
        method : str
            Name of the analysis method to use.
        parameters : dict, optional
            Parameters for the analysis method.
            
        Returns:
        --------
        dict
            Results of the analysis.
        """
        # Will validate that requested method exists
        # Will perform the requested analysis with given parameters
        # Will format and return results
        pass
    
    def export_results(self, output_path, format_type='csv'):
        """
        Export the processed data to the specified format.
        
        Parameters:
        -----------
        output_path : str
            Path where the output file should be saved.
        format_type : str, optional
            Format of the output file (default: 'csv').
            
        Returns:
        --------
        bool
            True if export was successful, False otherwise.
        """
        # Will validate that data exists to export
        # Will convert data to requested format
        # Will save data to specified path
        # Will handle potential errors during export
        pass

class Calculator:
    def __init__(self, initial_value=0):
        """Initialize the calculator with a starting value."""
        self.value = initial_value
        self.history = []
    
    def add(self, number):
        """Add a number to the current value."""
        self.value += number
        self.history.append(f"Added {number}")
        return self.value
    
    def subtract(self, number):
        """Subtract a number from the current value."""
        self.value -= number
        self.history.append(f"Subtracted {number}")
        return self.value
    
    def multiply(self, number):
        """Multiply the current value by a number."""
        self.value *= number
        self.history.append(f"Multiplied by {number}")
        return self.value
    
    def get_history(self):
        """Return the history of operations."""
        return self.history

"""
# # Creating an instance of the Calculator class
# my_calc = Calculator(10)  # Initialize with value 10

# # Using the methods of the class
# result1 = my_calc.add(5)      # Adds 5 to 10
# print(f"After adding 5: {result1}")

# result2 = my_calc.multiply(2)  # Multiplies 15 by 2
# print(f"After multiplying by 2: {result2}")

# result3 = my_calc.subtract(7)  # Subtracts 7 from 30
# print(f"After subtracting 7: {result3}")

# # Getting the history of operations
# print("\nOperation history:")
# for operation in my_calc.get_history():
#     print(f"- {operation}")

# # You can create another instance with different values
# another_calc = Calculator(100)
# another_calc.subtract(50)
# print(f"\nSecond calculator value: {another_calc.value}")"
"""

test_maze = Maze(3)

print(test_maze.initial_costgrid)
print(test_maze.goal_coords)