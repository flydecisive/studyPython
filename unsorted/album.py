#step 8-7
def make_album(singer_name, album_name, track=''):
    if track:
        album = {'singer': singer_name, 'album': album_name, 'track': track}
    else:
        album = {'singer': singer_name, 'album': album_name}
    return album

first = make_album('Sting', 'Shape')
for key, value in first.items():
    print(key + ' - ' + str(value))

second = make_album('Mettalica', 'Enter Sadman')
for key, value in second.items():
    print(key + ' - ' + str(value))

third = make_album('Anacondaz', 'Выходи за меня', 17)
for key, value in third.items():
    print(key + ' - ' + str(value))