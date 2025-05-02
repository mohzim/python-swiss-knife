Here’s an example of a Python script for batch scripting. This script demonstrates how to execute multiple commands or tasks in sequence, such as processing files in a directory or automating repetitive tasks.

How It Works:
batch_process Function:

Takes a directory path and a command template as input.
Iterates through all files in the directory.
Replaces {file} in the command template with the actual file path.
Executes the command using subprocess.run.
Command Template:

The user provides a command template, such as cat {file} or python process.py {file}.
{file} is replaced with the actual file path during execution.
Error Handling:

If a command fails, the error is caught and displayed.
Example Usage:
Place some files in a directory, e.g., /path/to/files.
Run the script:
Input the directory path and a command template:
The script will process each file in the directory using the specified command.
Output:
For each file, the script will display the command being executed and its output.