import subprocess


try:
    subprocess.run(["libcamera-still", "-t", "10000"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
