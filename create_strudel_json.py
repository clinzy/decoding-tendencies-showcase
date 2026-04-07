import os
import json

def create_individual_strudel_json(directory="."):
    # Supported audio extensions in Strudel
    valid_extensions = ('.wav', '.mp3', '.ogg', '.m4a', '.flac')
    sample_map = {}

    # Get all files in the current directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            # Use the filename without extension as the key
            sample_name = os.path.splitext(filename)[0]
            # Map the name to a list containing the file path
            sample_map[sample_name] = [filename]

    # Write the formatted JSON
    with open("strudel.json", "w") as f:
        json.dump(sample_map, f, indent=2)

    print(f"Done! Created strudel.json with {len(sample_map)} unique categories.")

if __name__ == "__main__":
    create_individual_strudel_json()