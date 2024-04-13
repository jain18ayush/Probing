import os
import matplotlib.pyplot as plt

# Set the directory where your files are located
directory = "./statistics/Layer_Data/simple"

# Create lists to store loss and accuracy values from all files
all_losses = []
all_accuracies = []
file_names = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    # Initialize lists to store loss and accuracy values for the current file
    losses = []
    accuracies = []
    
    # Open the file and read the data
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by ':' to separate the label (layer number) and values
            parts = line.strip().split(':')
            
            # Parse the loss and accuracy values
            loss, accuracy = map(float, parts[1].split())
            
            losses.append(loss)
            accuracies.append(accuracy)
    
    # Append the loss and accuracy values for the current file to the master lists
    all_losses.append(losses)
    all_accuracies.append(accuracies)
    file_names.append(os.path.basename(filename))  # Store the filename without the directory path

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the loss and accuracy values for each file as separate lines
for i, (losses, accuracies, file_name) in enumerate(zip(all_losses, all_accuracies, file_names)):
    ax.plot(losses, label=f"{file_name} Loss")
    ax.plot(accuracies, label=f"{file_name} Accuracy")

# Add labels and legend
ax.set_xlabel("Layer")
ax.set_ylabel("Loss / Accuracy")
ax.legend()

# Display the plot
plt.show()