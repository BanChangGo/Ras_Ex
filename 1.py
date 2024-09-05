import subprocess

# libcamera-still 명령을 통해 10초 동안 미리보기
try:
    subprocess.run(["libcamera-still", "-t", "10000"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
