from subprocess import Popen
import os

FFMPEG_PATH = "./ffmpeg/bin/ffmpeg.exe"


def compress_video():
    input_path = "./video/"
    output_path = "./compressed/"

    i = 1
    for file in os.listdir(input_path):
        print(file)
        video_path = input_path + file
        out = output_path + '{}.mp4'.format(i)

        ffmpeg_process = Popen([FFMPEG_PATH, "-hide_banner", "-loglevel", "panic", "-y", "-i", video_path,
                                "-vcodec", "h264", "-acodec", "mp3", out],
                               start_new_session=True)

        ffmpeg_process.wait()

        i += 1

        print("chiamata a ffmpeg finita")


if __name__ == '__main__':
    compress_video()
    print("Done")
