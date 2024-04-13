import os
import matplotlib.pyplot as plt

# Set the directory where your files are located
directory = "./statistics/Layer_Data/simple"

# Create lists to store accuracy values and file names
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
            # Split the line and parse accuracy
            parts = line.strip().split(':')
            accuracy = float(parts[1].split()[1])  # Assuming accuracy is the second value
            
            accuracies.append(accuracy)
    
    # Truncate accuracy list to first 10 layers
    accuracies = accuracies  # Select only the first 10 elements
    
    # Append data for this file
    all_accuracies.append(accuracies)
    file_names.append(os.path.basename(filename).split('_')[0] + '_' + os.path.basename(filename).split('_')[1])  # Store filename

# Create the plot
fig, ax = plt.subplots()

# Plot accuracy for each file (first 10 layers)
for i, (accuracies, file_name) in enumerate(zip(all_accuracies, file_names)):
    ax.plot(accuracies, label=f"{file_name} Accuracy")

# Add labels and legend
ax.set_xlabel("Layer")
ax.set_ylabel("Accuracy")
ax.legend()

# Display the plot
plt.show()
