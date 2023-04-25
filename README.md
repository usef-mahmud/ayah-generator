## Ayah Generator
A python script that generates cool videos for some selected ayahs from **holy quran**. Then I make new version of this script as a telegram bot to be more easier for user than terminal

## How it works
It takes 2 inputs from user **surah number** and **ayahs range**, and use it in making API requests to [Alquran Cloud](https://alquran.cloud/api) and get ayah in text and mp3 audio file.\
It uses this text and make it in black background with PIL library, then uses ffmpeg to combine images and audio in mp4 video file.\
The last step is concatenate all video files to one output file and some transisions using Moviepy.\

In the telegram bot user be also able to choose the recruiter.

#### [**Bot Live Demo**](https://t.me/AyahGeneratorBot)

## Usage
At first clone this repository to your machine:\
&emsp; `git clone https://github.com/usef-mahmud/ayah-generator.git`

then run the `main.py` file form terminal\
at the end it will ask for some inputs like **surah number** that between 1 and 114. after entered the surah number you will be asked for the ayahs range in this form **1-100**. If you want to choose one ayah just enter its number like this **13-13**.\
It will take some time in concatenating videos of ayahs based on the wide of range.
