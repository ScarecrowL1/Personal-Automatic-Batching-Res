import os


def open_app(app_dir):
    os.startfile(app_dir)


if __name__ == "__main__":
    obs = r'C:\Users\li\Desktop\BiliBili\OBS Studio.lnk'
    blive = r'D:\Program Files\bililive\livehime\livehime.exe'
    blive_chat = r'C:\Users\li\Desktop\BiliBili\blivechat.lnk'
    cat_mover = r'C:\Users\li\Desktop\BiliBili\Bongo Cat Mver.lnk'
    open_app(obs)
    open_app(blive)
    open_app(blive_chat)
    open_app(cat_mover)
