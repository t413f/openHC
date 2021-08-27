import filetype
import os
from loguru import logger

class suffix_file():
    video = '.avi'
    audio = '.mp3'
    image = '.jpg'
    archive = '.zip'

def check_type(filepath) -> str:
    if filetype.is_image(filepath):
        return suffix_file.image
    elif filetype.is_video(filepath):
        return suffix_file.video
    elif filetype.is_audio(filepath):
        return suffix_file.audio
    elif filetype.is_archive(filepath):
        return suffix_file.archive

def start_recover(directorypath):
    for root, dirs, files in os.walk(directorypath):
        for file in files:
            if str(file).find('password') == 1:
                continue
            if not os.path.join(root, file).endswith(check_type(os.path.join(root,file))):
                logger.info(os.path.join(root, file))
                logger.info(str(os.path.join(root, file))[:str(os.path.join(root,file)).index('.', 1)] + check_type(os.path.join(root, file)))
                os.rename(os.path.join(root, file), str(os.path.join(root, file))[:str(os.path.join(root,file)).index('.', 1)] + check_type(os.path.join(root, file)))

def main():
    directory_of_hidden_cabinet = ".\\temp"
    start_recover(directory_of_hidden_cabinet)

if __name__ == '__main__':
    main()