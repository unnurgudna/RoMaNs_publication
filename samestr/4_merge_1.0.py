import subprocess
from pathlib import Path

# --- CONFIGURATION ---
base_dir = Path("out_convert")
marker_dir = "samestr_db/"
nprocs = "30"
output_base = Path("out_merge")
dry_run = False 
# ----------------------

# Ensure output directory exists
output_base.mkdir(parents=True, exist_ok=True)

# Loop through all subdirectories 
for subdir in base_dir.iterdir():
    if subdir.is_dir():
        
        if not any(subdir.glob("*.npz")):
            print(f"No .npz files found in {subdir}. Skipping.")
            continue

        # Build the glob pattern string
        input_files_glob = f"{subdir}/*.npz"

	# Create output directory specific to this subdir
        output_dir = output_base / subdir.name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Build the full shell command string
        cmd = (
            f"samestr merge "
            f"--input-files {input_files_glob} "
            f"--marker-dir {marker_dir} "
            f"--nprocs {nprocs} "
            f"--output-dir {output_dir}"
        )

        print(f"Command for {subdir.name}:\n{cmd}")

        if not dry_run:
            try:
                subprocess.run(cmd, shell=True, check=True)
                print(f"Completed: {subdir.name}")
            except subprocess.CalledProcessError as e:
                print(f"Error in {subdir.name} (exit code {e.returncode})")
        else:
            print("Dry run mode command not executed.")
