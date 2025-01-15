import os
import subprocess
from datetime import datetime, timedelta

# Define the pixel art for "RVORINE"
art = [
    "  RRR  V   V  OOO  RRR  III N   N  EEE ",
    "  R  R V   V O   O R  R  I  NN  N  E   ",
    "  RRR  V   V O   O RRR   I  N N N  EEE ",
    "  R R  V   V O   O R R   I  N  NN  E   ",
    "  R  R  VVV   OOO  R  R III N   N  EEE ",
]

# Start date for commits
start_date = datetime(2025, 1, 15)

# Repository directory
repo_dir = os.getcwd()

# Function to execute shell commands
def run_command(command):
    subprocess.run(command, shell=True, check=True, cwd=repo_dir)

# Generate commits for each pixel
for y, row in enumerate(art):
    for x, char in enumerate(row):
        if char != " ":
            commit_date = start_date + timedelta(days=x + y * 7)
            run_command(f"echo 'Commit ({x}, {y})' > art.txt")
            run_command("git add art.txt")
            run_command(
                f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "Pixel ({x}, {y})"'
            )

print("Contribution art generated successfully!")
