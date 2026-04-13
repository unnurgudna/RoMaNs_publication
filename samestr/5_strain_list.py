import os
import csv

def list_files_to_csv(root_folder, output_csv):
    file_data = []

    # Go through all subdirectories
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Get relative subdirectory name
        subdirectory = os.path.relpath(dirpath, root_folder)
        for filename in filenames:
            file_data.append([filename, subdirectory])

    # Write data to CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Name", "Subdirectory"])
        writer.writerows(file_data)

    print(f"CSV file created: {output_csv}")


# Replace this with folder path
folder_a_path = r"out_merge"
output_csv_path = r"out_strain_list.csv"

list_files_to_csv(folder_a_path, output_csv_path)
