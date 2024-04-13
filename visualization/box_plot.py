import os
import matplotlib.pyplot as plt

# Set the directory where your files are located
directory = "./statistics/Layer_Data/merged"

# Create a dictionary to store accuracy values for each file
all_accuracies = {}
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
    
    # Store accuracy values for the current file under its filename as key
    all_accuracies[filename] = accuracies
    file_names.append(filename.split('_')[0] + '_' + filename.split('_')[1])  # Store the filename

# Create a figure and axis object
fig, ax = plt.subplots()

# Create a box plot for each file's accuracy data
bp = ax.boxplot(all_accuracies.values(), notch=True, vert=True, patch_artist=True, 
               labels=file_names)  # Adjust notch and other parameters as needed

# Customize box plot appearance (optional)
for box, color in zip(bp['boxes'], ['blue', 'green', 'red', 'purple', 'orange']):  # Adjust colors for more files
    box.set_facecolor(color)

# Add labels and title
ax.set_xlabel("Model")
ax.set_ylabel("Accuracy")
ax.set_title("Distribution of Accuracy Across Models with Combined Sentences")
ax.set_xticks([i + 1 for i, _ in enumerate(file_names)])  # Adjust x-axis tick positions

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Display the plot
plt.show()
