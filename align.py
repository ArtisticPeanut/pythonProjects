# Given data
data = {
    'Student ID': [1, 2, 3, 4, 5, 6, 7],
    'English': [90, 55, 80, 45, 95, 81, 99],
    'Science': [50, 73, 85, 90, 45, 70, 80],
    'Pass in Math': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No']
}

# Function to calculate Gini index
def calculate_gini_index(left_counts, right_counts):
    total_samples = sum(left_counts) + sum(right_counts)
    gini_left = 1 - sum((count / sum(left_counts))**2 for count in left_counts)
    gini_right = 1 - sum((count / sum(right_counts))**2 for count in right_counts)
    gini_index = (sum(left_counts) / total_samples) * gini_left + (sum(right_counts) / total_samples) * gini_right
    return gini_index

# Example calculation for Split 1 and Split 2
split1_left_counts = [1, 1]  # Replace with your actual counts
split1_right_counts = [1, 1]  # Replace with your actual counts
gini_index_split1 = calculate_gini_index(split1_left_counts, split1_right_counts)

split2_left_counts = [1, 1]  # Replace with your actual counts
split2_right_counts = [1, 1]  # Replace with your actual counts
gini_index_split2 = calculate_gini_index(split2_left_counts, split2_right_counts)

# Compare Gini indices
if gini_index_split1 < gini_index_split2:
    best_split = "Split 1"
else:
    best_split = "Split 2"

print(f"The best split is: {best_split}")
