def clean_requirements_file(input_file, output_file):
    """
    Cleans a requirements.txt file by removing lines that contain spaces.

    Args:
        input_file (str): Path to the input requirements.txt file.
        output_file (str): Path to save the cleaned requirements.txt file.
    """
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Filter out lines that contain spaces
        cleaned_lines = [line for line in lines if ' ' not in line.strip()]

        with open(output_file, 'w') as outfile:
            outfile.writelines(cleaned_lines)

        print(f"Cleaned requirements file saved to: {output_file}")

    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "requirements.txt"  # Input requirements file
    output_file = "cleaned_requirements.txt"  # Output cleaned file
    clean_requirements_file(input_file, output_file)