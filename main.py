import vlc
import pathlib


def main():
    # Create a new instance of vlc media player
    player = vlc.MediaPlayer()
    player.toggle_fullscreen()

    media = vlc.Media(pathlib.Path(__file__).parent / "rsc/test.mp4")
    player.set_media(media)
    player.play()

    start_time = player.get_time()

    while True:
        pass


if __name__ == '__main__':
    main()
