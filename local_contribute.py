#!/usr/bin/env python
import os
from datetime import datetime, timedelta
from random import randint
import subprocess
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
import threading
import sys

def main():
    # Get user input for date range
    try:
        # Get start date
        start_input = input("Enter start date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_input, "%Y-%m-%d")
        
        # Get end date
        end_input = input("Enter end date (YYYY-MM-DD): ")
        end_date = datetime.strptime(end_input, "%Y-%m-%d")
        end_date = end_date.replace(hour=23, minute=59, second=59)
        
        # Validate dates
        if end_date < start_date:
            raise ValueError("End date must be after start date")
        
        # Get commit range
        min_commits = int(input("Enter minimum commits per day (8-100): "))
        max_commits = int(input("Enter maximum commits per day (must be >= minimum): "))
        
        if min_commits < 1 or min_commits > 100:
            min_commits = 50  # Default if invalid
        if max_commits < min_commits or max_commits > 100:
            max_commits = 99  # Default if invalid
            
    except ValueError as e:
        print(f"Error with input: {e}")
        print("Using default values instead.")
        start_date = datetime(2024, 1, 1, 0, 0, 0)
        end_date = datetime(2024, 5, 31, 23, 59, 59)
        min_commits = 50
        max_commits = 99
    
    # Create header for contributions file
    date_range = f"{start_date.strftime('%B %Y')} - {end_date.strftime('%B %Y')}"
    with open('CONTRIBUTIONS.md', 'w', encoding='utf-8') as f:
        f.write(f'# Activity Log ({date_range})\n\n')

    # Pre-generate all commit dates
    all_commits = []
    current_date = start_date
    while current_date <= end_date:
        # Generate commits per day based on user input
        num_commits = randint(min_commits, max_commits)
        day_commits = sorted([
            current_date + timedelta(minutes=randint(0, 1439))
            for _ in range(num_commits)
        ])
        all_commits.extend(day_commits)
        current_date += timedelta(days=1)

    total_commits = len(all_commits)
    print(f"Generating {total_commits} commits for {date_range}...")

    # Process in chunks
    chunk_size = 500
    chunks = [all_commits[i:i + chunk_size] for i in range(0, len(all_commits), chunk_size)]
    
    max_workers = mp.cpu_count() * 4
    
    commits_done = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for chunk in chunks:
            process_chunk(chunk)
            commits_done += len(chunk)
            progress = (commits_done / total_commits) * 100
            print(f'Progress: {progress:.2f}% - {commits_done}/{total_commits}')
    
    print(f"\nContribution generation completed successfully!")
    print(f"Created {total_commits} commits from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print(f"Use 'git push -f origin main' to push the changes to GitHub")

def process_chunk(dates):
    for date in dates:
        try:
            contribute(date)
        except Exception as e:
            print(f"Error on {date}: {e}")
            continue

def contribute(date):
    file_lock = threading.Lock()
    with file_lock:
        with open('CONTRIBUTIONS.md', 'a', encoding='utf-8') as file:
            file.write(f'Contribution: {date.strftime("%Y-%m-%d %H:%M")}\n\n')
    
    date_str = date.strftime('%Y-%m-%d %H:%M:%S')
    env = dict(os.environ)
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    git_lock = threading.Lock()
    with git_lock:
        subprocess.run(['git', 'add', 'CONTRIBUTIONS.md'], check=True, capture_output=True)
        subprocess.run(
            ['git', 'commit', '-m', f'Contribution: {date.strftime("%Y-%m-%d %H:%M")}'],
            env=env,
            check=True,
            capture_output=True
        )

if __name__ == "__main__":
    main()