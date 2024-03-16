import subprocess
import os
import re


def main():
    path = '../../video' + input("enter path: ")
    title = input("enter title: ")
    for root, dirs, files in os.walk(path, topdown=False):
        print(root, dirs, files)
        for file in files:
            input_path = os.path.join(root, file)
            number = re.findall(r'\d+', str(file))[0]
            file_name = f'{title}-{number}.mp4'
            output_path = os.path.join(root, file_name)
            subprocess.run([
                "ffmpeg",
                "-y",
                "-i", input_path,
                "-metadata", f"title={title}",
                "-codec", "copy",
                output_path
            ])
        for file in files:
            input_path = os.path.join(root, file)
            if str(file).find('Scene') != '-1':
                os.remove(input_path)


if __name__ == '__main__':
    main()