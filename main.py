from funcs import *
import time

surah_id = int(input('enter surah number: \n'))
ayahs = input('enter ayahs number: \n')
ayah_start = int(ayahs.split('-')[0])
ayah_end= int(ayahs.split('-')[1])

concat_file = open('concat.txt', 'w')


for id in range(ayah_start, ayah_end+1):
    ayah = get_data(surah_id, id)

    download_audio(ayah['audio'], id)
    craete_image(ayah['text'], id)

    combine_audio_image(
        f'data/audio/ayah_{id}.mp3',
        f'data/images/ayah_{id}.png',
        f'video_ayah_{id}',
        
    )

    concat_file.write('file %s\n' % f"'./data/output/video_ayah_{id}.mp4'")

concat_file.close()

if ayah_start == ayah_end:
    os.rename(
        f'data/output/video_ayah_{ayah_start}.mp4',
        f'data/output/output.mp4'
    )
else:
    ffmpeg.input('concat.txt', format='concat', safe=0).output('data/output/output.mp4').run(overwrite_output=True)

    for i in range(ayah_start, ayah_end+1):
        os.remove(f'data/output/video_ayah_{i}.mp4')
os.remove('concat.txt')

print('\n\n\n\nSUCCEED!!\n\n\n\n')