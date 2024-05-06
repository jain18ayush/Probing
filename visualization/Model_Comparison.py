import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
with open('./statistics/statistics.txt', 'r') as file:
    data = [line.strip().split(': ') for line in file]

# Extract model-prompt combinations, values, and layers
model_prompts = []
value1 = []
value2 = []
layers = []

for row in data:
    model_prompt = row[0].split('/')[1]
    if "prompt" not in model_prompt:  # Filter out data containing "prompt"
        # Split by "_", keep everything after the first occurrence
        split_parts = model_prompt.split('_')
        model_name = split_parts[0]  # Base model name
        suffix_to_keep = '_'.join(split_parts[2:])  # Join remaining parts for suffix

        # Combine model name and suffix (if any)
        displayed_name = model_name
        if suffix_to_keep:
            displayed_name += f'_{suffix_to_keep}'

        model_prompts.append(displayed_name)
        values = row[1].split()
        value1.append(float(values[0]))
        value2.append(float(values[1]))
        layers.append(model_prompt.split('_')[-1])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Create bars for the first value
bar1 = np.arange(len(model_prompts))
ax.bar(bar1, value1, label='Loss')

# Create bars for the second value, slightly offset
bar_width = 0.35
bar2 = [x + bar_width for x in bar1]
ax.bar(bar2, value2, bar_width, label='Accuracy')

# Add labels and title
ax.set_xlabel('Model-Prompt Combinations', fontsize=12)
ax.set_ylabel('Values', fontsize=12)
ax.set_title('Bar Plot of Model-Prompt Combinations with Discrete Sentences', fontsize=14)

# Set x-axis ticks with processed model names
ax.set_xticks([r + bar_width / 2 for r in range(len(model_prompts))], model_prompts, rotation=90)
ax.legend()

# Show the plot
plt.show()
