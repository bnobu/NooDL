import os
import requests
import subprocess

# Function to download .ts files
def download_ts_files():
    base_url = input("Input GoNoodle url. Remember to replace the TS numbers with {}. ")
    ts_files = []
    for i in range(1, 1000):  # Assuming the range of possible file numbers
        file_url = base_url.format(i)
        response = requests.head(file_url)
        if response.status_code == 200:
            print(f"Downloading {file_url}")
            ts_file_name = f"video_{i}.ts"
            with open(ts_file_name, "wb") as f:
                f.write(requests.get(file_url).content)
            ts_files.append(ts_file_name)
        else:
            print(f"File not found: {file_url}")
            break
    return ts_files

# Function to merge .ts files into .mp4
def merge_ts_files(ts_files):
    output_file = "merged_video.mp4"
    input_files = "|".join(ts_files)
    command = f"ffmpeg -i 'concat:{input_files}' -c copy {output_file}"
    subprocess.call(command, shell=True)
    return output_file

# Main function
def main():
    ts_files = download_ts_files()
    if ts_files:
        merged_file = merge_ts_files(ts_files)
        print(f"Merged video file: {merged_file}")
        # Clean up downloaded .ts files
        for ts_file in ts_files:
            os.remove(ts_file)

if __name__ == "__main__":
    main()

