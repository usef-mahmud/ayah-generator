from funcs import *
import ffmpeg
import moviepy.editor as mp

surah_id = int(input('enter surah number: \n'))
ayahs = input('enter ayahs number: \n')
ayah_start = int(ayahs.split('-')[0])
ayah_end= int(ayahs.split('-')[1])

for id in range(ayah_start, ayah_end+1):
    ayah = get_data(surah_id, id)

    download_audio(ayah['audio'], id)
    craete_image(ayah['text'], id)

    combine_audio_image(
        f'data/audio/ayah_{id}.mp3',
        f'data/images/ayah_{id}.png',
        f'video_ayah_{id}',
        
    )


if ayah_start == ayah_end:
    os.rename(
        f'data/output/video_ayah_{ayah_start}.mp4',
        f'data/output/output.mp4'
    )
else:

    concat_clip = mp.concatenate_videoclips([mp.VideoFileClip(name).crossfadein(2.0).crossfadeout(2.0) for name in [f'data/output/video_ayah_{i}.mp4' for i in range(ayah_start, ayah_end+1)]], method='compose')
    concat_clip.write_videofile('data/output/output.mp4', fps=24, threads=8)

    for i in range(ayah_start, ayah_end+1):
        os.remove(f'data/output/video_ayah_{i}.mp4')

print('\n\n\n\nSUCCEED!!\n\n\n\n')


