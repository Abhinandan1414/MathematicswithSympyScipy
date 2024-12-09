import numpy as np
import pandas as pd

# Comeup with Impact_Probability_Matrix from given data frame

#Row is impact and column is probability

Impapact_probability_matrx = {
    'Probability_0': [4, 5, 6,7],
    'Probability_1': [7, 8, 9,10], 
    'Probability_2': [10, 11, 12,13],
    'Probability_3': [10, 11, 12,13]
}

# Creating Datafarme from given dictionary
df = pd.DataFrame(Impapact_probability_matrx)
#Display the DataFrame
print("DataFrame with row and column headers:")
print(df)

#Converting the DataFrame to a NumPy Matrix
data_frame_to_matrix = df.to_numpy()

#Sub Matrix starting from 2nd row and 2nd column
#For the time being hard code it to 2. Hard coding is not best sofware practice. Here focus is demonstration
starting_row_column_value = 2

#Sliced Impact_likelyhood_matrix containing high impact and high probability values

sliced_impact_probability_matrix = data_frame_to_matrix[starting_row_column_value:,starting_row_column_value:]
print(sliced_impact_probability_matrix)


#Come up with Macro and Micro Economic representation of business environment
#Each row is micro and column is macro

#Intentionally retain the exact same values as in first data frame. 
# Because final values are easy to verfy after the process
Economic_Business_Environment_for_various_micros = {
    'given_macro_0':[4, 5, 6,7],
    'given_macro_1': [7, 8, 9,10],
    'given_macro_2': [10, 11, 12,13],
    'given_macro_3': [10, 11, 12,13]
}

# Creating Impact_Weight_Matric
df = pd.DataFrame(Economic_Business_Environment_for_various_micros)
#Display the DataFrame
print("DataFrame with row and column headers:")
print(df)


#Converting the DataFrame to a NumPy Matrix
data_frame_to_matrix = df.to_numpy()

#Sub Matrix starting from 2nd row and 2nd column
#For the time being hard code it to 2. Hard coding is not best sofware practice. Here focus is demonstration
starting_row_column_value = 2

sliced_Economic_Business_Environment_for_various_micros_macro = data_frame_to_matrix[starting_row_column_value:,starting_row_column_value:]
print(sliced_Economic_Business_Environment_for_various_micros_macro)


#Convert sliced impact_probability matrix into vector using flatten

sliced_impact_probability_vector = sliced_impact_probability_matrix.flatten()

#Convert sliced_Economic_Business_Environment_for_various_micros_macro using flatten

sliced_Economic_Business_Environment_for_various_micros_macro_vector = sliced_Economic_Business_Environment_for_various_micros_macro.flatten()

#We converted the sliced_impact_probability_matrix to 1D array and sliced_Economic_Business_Environment_for_various_micros_macro to 1D array
#Now come up with Matrix of Impact_Probability_Matrix * Economic_Business_Environment_for_various_micros

final_impact_probability_micro_macro_matrix = np.outer(sliced_impact_probability_vector,sliced_Economic_Business_Environment_for_various_micros_macro_vector)
print(final_impact_probability_micro_macro_matrix)

#If needed it can be sliced further. But we should NOT do that.