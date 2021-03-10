#step 8-8
def make_album(singer, album, track=''):
    if track:
        album = {'singer': singer, 'album': album, 'track': track}
    else:
        album = {'singer': singer, 'album': album}

    return album

while True:
    print('Создайте свой альбом')
    print('Введите \'q\' для выхода')
    singer = input('Введите имя певца: ')
    if singer.lowe() == 'q':
        break

    album = input('Введите название альбома: ')
    if album.lower() == 'q':
        break

    track = input('Введите количество дорожек: ')
    if track.lower() == 'q':
        break

    print(make_album(singer, album, track))
    print('\n')