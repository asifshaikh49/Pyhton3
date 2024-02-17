# Task: List vs. Tuple vs. Set

# Create a List
my_list = [1, 'hello', 3.14, True]

# Create a Tuple
my_tuple = (1, 'world', 2.71, False)

# Create a Set
my_set = {1, 2, 3, 4, 5}

# Print initial state
print("Original List:", my_list)
print("Original Tuple:", my_tuple)
print("Original Set:", my_set)

# Modify List
my_list.append('new_item')
my_list.remove(1)

# Modify Tuple (Tuples are immutable, so we create a new one)
my_tuple = my_tuple + (42,)

# Modify Set
my_set.add(6)
my_set.remove(3)

# Print modified state
print("\nModified List:", my_list)
print("Modified Tuple:", my_tuple)
print("Modified Set:", my_set)

# Task: Working with Dictionaries

# Your Favorite DevOps Tools
fav_tools = {
  1: "Linux",
  2: "Git",
  3: "Docker",
  4: "Kubernetes",
  5: "Terraform",
  6: "Ansible",
  7: "Chef"
}

# Print your favorite tool using keys
tool_key = 3
print("\nYour Favorite DevOps Tool:", fav_tools.get(tool_key, "Tool not found"))

# Managing Cloud Service Providers

# Initial list of cloud providers
cloud_providers = ["AWS", "GCP", "Azure"]

# Add "Digital Ocean" to the list
cloud_providers.append("Digital Ocean")

# Sort the list alphabetically
cloud_providers.sort()

# Print the updated list
print("\nUpdated Cloud Providers List:", cloud_providers)
