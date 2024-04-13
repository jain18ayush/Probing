import os
import matplotlib.pyplot as plt

# Set the directory where your files are located
directory = "./statistics/Layer_Data/simple"

# Create a list to store accuracy values from all files
all_accuracies = []
file_names = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    # Initialize a list to store accuracy values for the current file
    accuracies = []
    
    # Open the file and read the data
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by ':' to separate the label (layer number) and values
            parts = line.strip().split(':')
            
            # Parse the accuracy value
            accuracy = float(parts[1].split()[1])  # Assuming accuracy is the second value
            
            accuracies.append(accuracy)
    
    # Append the accuracy values for the current file to the master list
    all_accuracies.append(accuracies)
    file_names.append(os.path.basename(filename))  # Store the filename without the directory path

# Create a figure and axis object
fig, ax = plt.subplots()

# Scatter plot the accuracy values for each file with different markers
markers = ['o', 's', '^', 'P', 'D']  # Adjust markers as needed for more files
for i, (accuracies, file_name) in enumerate(zip(all_accuracies, file_names)):
    ax.scatter(range(len(accuracies)), accuracies, label=f"{file_name}", marker=markers[i % len(markers)])

# Add labels and legend
ax.set_xlabel("Layer")
ax.set_ylabel("Accuracy")
ax.legend()

# Display the plot
plt.show()
