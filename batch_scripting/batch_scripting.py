import os
import subprocess

def batch_process(directory, command_template):
    """
    Batch process files in a directory using a specified command template.

    Args:
        directory (str): Path to the directory containing files to process.
        command_template (str): Command template with a placeholder for the file name.
                                Example: "cat {file}" or "python process.py {file}"
    """
    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid path.")
        return

    # List all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print(f"Found {len(files)} files in directory: {directory}")

    for file in files:
        # Replace the placeholder with the actual file name
        command = command_template.format(file=file)
        print(f"Executing: {command}")

        try:
            # Execute the command
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"Output:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing file {file}: {e.stderr}")

if __name__ == "__main__":
    # Get directory and command template from the user
    directory = input("Enter the directory containing files to process: ").strip()
    command_template = input("Enter the command template (use {file} as a placeholder for file names): ").strip()

    batch_process(directory, command_template)
