import os
import time

# Function to tail log files in a directory
def monitor_logs(directory, lines, interval):

    # Get File List
    log_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.log')]
    file_cursor = {f:0 for f in log_files}

    # Iterate through each file
    print(f"Monitoring logs in directory {directory}")
    read_counter = 0

    while True:
        for file in log_files:
            try:
                with open(file,'r') as f:
                    f.seek(file_cursor[file])
                    new_data = f.read()
                    if new_data:
                        print(f"\nNew lines in {f.name} \n")
                        print(new_data, end=' ')
                        file_cursor[file] = f.tell() # return current stream position
                        read_counter += 1
                        print(f"\nRead Counter: {read_counter}")
            except FileNotFoundError:
                print(f'Unable to open file {f.name}. Skipping')
        time.sleep(interval)

if __name__ == "__main__":
    # Get log directory and lines to tail
    log_directory = input("Enter directory location: ").strip()

    if not os.path.isdir(log_directory):
        print("Invalid path. Please provide a valid path", end='')
    else:
        log_lines = int(input("Enter number of lines to tail (Default:10)") or 10)
        monitor_logs(log_directory, log_lines, 2)

