#!/usr/bin/env python3
import os
import time
import shutil

def purgeDir(dir, age):
    print("Scanning:", dir)
    age = age * 86400  # Convert days to seconds
    now = time.time()

    for f in os.listdir(dir):
        filepath = os.path.join(dir, f)
        try:
            modified = os.stat(filepath).st_mtime
            print(f'Inspecting: {f} ({modified}) - Current: {now}')

            if (now - modified) > age:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                    print(f'Deleted file: {f} ({modified})')
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
                    print(f'Deleted directory: {f} ({modified})')
        except Exception as e:
            print(f"Error handling {filepath}: {e}")

# Example usage:
# Replace '/home/test' with the directory you want to scan
# and 30 with the age in days
purgeDir('/home/test', 30)
