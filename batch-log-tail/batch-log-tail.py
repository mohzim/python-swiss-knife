import os
import time

def monitor_logs(directory, lines=10, interval=2):
    """Monitor all log files in a directory for updates."""
    log_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.log')]
    file_positions = {file: 0 for file in log_files}

    # print(f"\nPrinting file: {log_files}\n")

    print(f"Monitoring logs in directory: {directory}")
    while True:
        for file in log_files:
            try:
                with open(file, 'r') as f:
                    f.seek(file_positions[file])
                    new_data = f.read()
                    if new_data:
                        print(f"\n--- New data in {file} ---")  
                        print(new_data, end='')
                        file_positions[file] = f.tell()
            except FileNotFoundError:
                print(f"File {file} not found. Skipping...")
        time.sleep(interval)


if __name__ == "__main__": # If script is being run as main, then name = main
    log_directory = input("Enter the directory with containing log files: ").strip()
    if not os.path.isdir(log_directory): # Check if directory exists in Unix or Windows
        print("Invalid directory. Please provide a valid path.")
    else:
        lines_to_tail = int(input("Enter the number of lines to tail (default 10): ") or 10)
        monitor_logs(log_directory, lines=lines_to_tail)