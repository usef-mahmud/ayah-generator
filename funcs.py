import requests
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import ffmpeg
from bidi.algorithm import get_display
import arabic_reshaper

# muhammadjibreel
# shaatree
# alafasy


def get_data(surah, ayah, recruiter_id):
    res = requests.get(
        f'http://api.alquran.cloud/v1/ayah/{surah}:{ayah}/ar.{recruiter_id}').json()

    return {
        'audio': res['data']['audio'],
        'text': res['data']['text'].replace('ا۟', 'ا'),
        'surah': res['data']['surah']['name']
    }


def create_image(text, ayah_id):
    font = ImageFont.truetype('data/fonts/UthmanicHafs.ttf', 70)

    lines = textwrap.wrap(text, width=115)
    lines_h = 0
    for line in lines:
        h = font.getbbox(line)[3]

        lines_h += h

    img = Image.new('RGB', (1920, lines_h+300+((len(lines))*20)))
    draw = ImageDraw.Draw(img)

    font_top = 170
    for line in lines:
        w = font.getbbox(line)[2]
        h = font.getbbox(line)[3]

        unicode_text_reshaped = arabic_reshaper.reshape(u'{line}')
        unicode_text_reshaped_RTL = get_display(unicode_text_reshaped , base_dir='R')

        draw.text(((img.width-w)/2, font_top), unicode_text_reshaped_RTL, font=font, align='center')
        font_top += (h+20)

    img.save(f'data/images/ayah_{ayah_id}.png')


def download_audio(url, ayah_id):
    res = requests.get(url)
    open(f'data/audio/ayah_{ayah_id}.mp3', 'wb').write(res.content)


def combine_audio_image(audio_path, image_path, output_file):

    a = ffmpeg.input(audio_path)
    b = ffmpeg.input(image_path)

    stream = ffmpeg.concat(b, a, v=1, a=1)
    stream = ffmpeg.output(stream, f'data/output/{output_file}.mp4')
    ffmpeg.run(stream, overwrite_output=True)

    os.remove(audio_path)
    os.remove(image_path)
