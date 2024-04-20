try:
    # Open the file in read mode
    with open("offensive.txt", "r") as file:
        # Read and print the content
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'offensive.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
