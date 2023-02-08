import vlc
import pathlib

MEDIA_DIR = pathlib.Path(__file__).parent / "rsc/default"
RFID_DIR = pathlib.Path(__file__).parent / "rsc/rfid"


def get_rfid():
    # return rfid id if rfid is detected, otherwise return None
    # TODO: implement this
    return None


def main():
    default_media = [x for x in MEDIA_DIR.glob("*") if x.is_file()]
    current_media_playing = 0

    player = vlc.MediaPlayer()
    player.set_fullscreen(True)

    player.set_media(vlc.Media(default_media[current_media_playing]))
    player.play()

    while True:
        rfid = get_rfid()
        if rfid is not None:
            print(f"RFID detected: {rfid}")
            media = RFID_DIR / f"{rfid}.mp4"
            if media.exists():
                current_media_playing = 0
                player.set_media(vlc.Media(media))
                player.play()
                continue

        if player.get_state() == vlc.State.Ended:
            current_media_playing += 1
            if current_media_playing >= len(default_media):
                current_media_playing = 0
            player.set_media(vlc.Media(default_media[current_media_playing]))
            player.play()


if __name__ == '__main__':
    main()
