import telebot, json, os, time
from telebot import types
from funcs import *
import moviepy.editor as mp

TOKEN = '6015624747:AAHqMKfm2yn3CiCFPAoAl0L2B2Jdze0D-YM'
bot = telebot.TeleBot(TOKEN)
f = open('data/users.json')
data = json.load(f)

chat_status = {
    "active": True
}

surahs = [
    {"surah": 1, "name": "الفاتحة", "ayahs": 7},
    {"surah": 2, "name": "البقرة", "ayahs": 286},
    {"surah": 3, "name": "آل عمران", "ayahs": 200},
    {"surah": 4, "name": "النساء", "ayahs": 176},
    {"surah": 5, "name": "المائدة", "ayahs": 120},
    {"surah": 6, "name": "الأنعام", "ayahs": 165},
    {"surah": 7, "name": "الأعراف", "ayahs": 206},
    {"surah": 8, "name": "الأنفال", "ayahs": 75},
    {"surah": 9, "name": "التوبة", "ayahs": 129},
    {"surah": 10, "name": "يونس", "ayahs": 109},
    {"surah": 11, "name": "هود", "ayahs": 123},
    {"surah": 12, "name": "يوسف", "ayahs": 111},
    {"surah": 13, "name": "الرعد", "ayahs": 43},
    {"surah": 14, "name": "ابراهيم", "ayahs": 52},
    {"surah": 15, "name": "الحجر", "ayahs": 99},
    {"surah": 16, "name": "النحل", "ayahs": 128},
    {"surah": 17, "name": "الإسراء", "ayahs": 111},
    {"surah": 18, "name": "الكهف", "ayahs": 110},
    {"surah": 19, "name": "مريم", "ayahs": 98},
    {"surah": 20, "name": "طه", "ayahs": 135},
    {"surah": 21, "name": "الأنبياء",  "ayahs": 112},
    {"surah": 22, "name": "الحج", "ayahs": 78},
    {"surah": 23, "name": "المؤمنون", "ayahs": 118},
    {"surah": 24, "name": "النور",  "ayahs":  64},
    {"surah": 25, "name": "الفرقان", "ayahs": 77},
    {"surah": 26, "name": "الشعراء", "ayahs": 227},
    {"surah": 27, "name": "النمل", "ayahs": 96},
    {"surah": 28, "name": "القصص", "ayahs": 88},
    {"surah": 29, "name": "العنكبوت", "ayahs": 69},
    {"surah": 30, "name": "الروم", "ayahs": 60},
    {"surah": 31, "name": "لقمان", "ayahs": 34},
    {"surah": 32, "name": "السجدة", "ayahs": 30},
    {"surah": 33, "name": "الأحزاب", "ayahs": 73},
    {"surah": 34, "name": "سبإ", "ayahs": 54},
    {"surah": 35, "name": "فاطر", "ayahs": 45},
    {"surah": 36, "name": "يس", "ayahs": 83},
    {"surah": 37, "name": "الصافات", "ayahs": 182},
    {"surah": 38, "name": "ص", "ayahs": 88},
    {"surah": 39, "name": "الزمر", "ayahs": 75},
    {"surah": 40, "name": "غافر", "ayahs": 85},
    {"surah": 41, "name": "فصلت", "ayahs": 54},
    {"surah": 42, "name": "الشورى", "ayahs": 53},
    {"surah": 43, "name": "الزخرف", "ayahs": 89},
    {"surah": 44, "name": "الدخان", "ayahs": 59},
    {"surah": 45, "name": "الجاثية", "ayahs": 37},
    {"surah": 46, "name": "الأحقاف", "ayahs": 35},
    {"surah": 47, "name": "محمد", "ayahs": 38},
    {"surah": 48, "name": "الفتح", "ayahs": 29},
    {"surah": 49, "name": "الحجرات", "ayahs": 18},
    {"surah": 50, "name": "ق", "ayahs": 45},
    {"surah": 51, "name": "الذاريات", "ayahs": 60},
    {"surah": 52, "name": "الطور", "ayahs": 49},
    {"surah": 53, "name": "النجم", "ayahs": 62},
    {"surah": 54, "name": "القمر", "ayahs": 55},
    {"surah": 55, "name": "الرحمن", "ayahs": 78},
    {"surah": 56, "name": "الواقعة", "ayahs": 96},
    {"surah": 57, "name": "الحديد", "ayahs": 29},
    {"surah": 58, "name": "المجادلة", "ayahs": 22},
    {"surah": 59, "name": "الحشر", "ayahs": 24},
    {"surah": 60, "name": "الممتحنة", "ayahs": 13},
    {"surah": 61, "name": "الصف", "ayahs": 14},
    {"surah": 62, "name": "الجمعة", "ayahs": 11},
    {"surah": 63, "name": "المنافقون", "ayahs": 11},
    {"surah": 64, "name": "التغابن", "ayahs": 18},
    {"surah": 65, "name": "الطلاق", "ayahs": 12},
    {"surah": 66, "name": "التحريم", "ayahs": 12},
    {"surah": 67, "name": "الملك", "ayahs": 30},
    {"surah": 68, "name": "القلم", "ayahs": 52},
    {"surah": 69, "name": "الحاقة", "ayahs": 52},
    {"surah": 70, "name": "المعارج", "ayahs": 44},
    {"surah": 71, "name": "نوح", "ayahs": 28},
    {"surah": 72, "name": "الجن", "ayahs": 28},
    {"surah": 73, "name": "المزمل", "ayahs": 20},
    {"surah": 74, "name": "المدثر", "ayahs": 56},
    {"surah": 75, "name": "القيامة", "ayahs": 40},
    {"surah": 76, "name": "الانسان", "ayahs": 31},
    {"surah": 77, "name": "المرسلات", "ayahs": 50},
    {"surah": 78, "name": "النبإ", "ayahs": 40},
    {"surah": 79, "name": "النازعات", "ayahs": 46},
    {"surah": 80, "name": "عبس", "ayahs": 42},
    {"surah": 81, "name": "التكوير", "ayahs": 29},
    {"surah": 82, "name": "الإنفطار", "ayahs": 19},
    {"surah": 83, "name": "المطففين", "ayahs": 36},
    {"surah": 84, "name": "الإنشقاق", "ayahs": 25},
    {"surah": 85, "name": "البروج", "ayahs": 22},
    {"surah": 86, "name": "الطارق", "ayahs": 17},
    {"surah": 87, "name": "الأعلى", "ayahs": 19},
    {"surah": 88, "name": "الغاشية", "ayahs": 26},
    {"surah": 89, "name": "الفجر", "ayahs": 30},
    {"surah": 90, "name": "البلد", "ayahs": 20},
    {"surah": 91, "name": "الشمس", "ayahs": 15},
    {"surah": 92, "name": "الليل", "ayahs": 21},
    {"surah": 93, "name": "الضحى", "ayahs": 11},
    {"surah": 94, "name": "الشرح", "ayahs": 8},
    {"surah": 95, "name": "التين", "ayahs": 8},
    {"surah": 96, "name": "العلق", "ayahs": 19},
    {"surah": 97, "name": "القدر", "ayahs": 5},
    {"surah": 98, "name": "البينة", "ayahs": 8},
    {"surah": 99, "name": "الزلزلة", "ayahs": 8},
    {"surah": 100, "name": "العاديات", "ayahs": 11},
    {"surah": 101, "name": "القارعة", "ayahs": 11},
    {"surah": 102, "name": "التكاثر", "ayahs": 8},
    {"surah": 103, "name": "العصر", "ayahs": 3},
    {"surah": 104, "name": "الهمزة", "ayahs": 9},
    {"surah": 105, "name": "الفيل", "ayahs": 5},
    {"surah": 106, "name": "قريش", "ayahs": 4},
    {"surah": 107, "name": "الماعون", "ayahs": 7},
    {"surah": 108, "name": "الكوثر", "ayahs": 3},
    {"surah": 109, "name": "الكافرون", "ayahs": 6},
    {"surah": 110, "name": "النصر", "ayahs": 3},
    {"surah": 111, "name": "المسد", "ayahs": 5},
    {"surah": 112, "name": "الإخلاص", "ayahs": 4},
    {"surah": 113, "name": "الفلق", "ayahs": 5},
    {"surah": 114, "name": "الناس", "ayahs": 6}
]

recruiters = [
    {
        'name': 'عبدالرحمن السديس',
        'id': 'abdurrahmaansudais'
    },{
        'name': 'أبو بكر الشاطري',
        'id': 'shaatree'
    },{
        'name': 'أحمد بن علي العجمي',
        'id': 'ahmedajamy'
    },{
        'name': 'مشاري العفاسي',
        'id': 'alafasy'
    },{
        'name': 'الحصري',
        'id': 'husary'
    },{
        'name': 'ماهر المعيقلي',
        'id': 'mahermuaiqly'
    },{
        'name': 'محمد جبريل',
        'id': 'muhammadjibreel'
    },{
        'name': 'ماهر المعيقلي',
        'id': 'mahermuaiqly'
    },
]

@bot.message_handler(commands=['start'])
def send_message(msg):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add(types.KeyboardButton('اختر السورة'))
    bot.send_message(
        msg.chat.id, 'أهلا بك\nيمكنك البدء في تصميم الفيديوهات عن طريق هذا الزر', reply_markup=markup)


@bot.message_handler()
def keyboard_res(msg):
    if msg.text == 'اختر السورة':
        if chat_status['active']:
            data.append({
                "chat": msg.chat.id
            })
            markup = types.InlineKeyboardMarkup(row_width=2)
            for i in range(0, len(surahs)):
                if i % 2 == 0 and i != 0:
                    markup.row(
                        types.InlineKeyboardButton(
                            surahs[i-1]['name'], callback_data=f'surah_{surahs[i-1]["surah"]}'),
                        types.InlineKeyboardButton(
                            surahs[i]['name'], callback_data=f'surah_{surahs[i]["surah"]}')
                    )
            bot.send_message(
                msg.chat.id, 'قم باختيار سورة من القائمة', reply_markup=markup)
        else:
            bot.send_message(msg.chat.id, 'هناك شخص آخر يستخدم البرنامج في الوقت الحالي، يرجى المحاولة لاحقا')

def get_start_ayah(msg):
    chats_id = [i for i, e in enumerate(data) if e['chat'] == msg.chat.id]
    data[chats_id[len(chats_id)-1]]['start_ayah'] = int(msg.text)
    next_msg = bot.send_message(msg.chat.id, 'أدخل نهاية الآيات')
    bot.register_next_step_handler(next_msg, get_end_ayah)


def get_end_ayah(msg):
    chats_id = [i for i, e in enumerate(data) if e['chat'] == msg.chat.id]
    data[chats_id[len(chats_id)-1]]['end_ayah'] = int(msg.text)

    markup = types.InlineKeyboardMarkup(row_width=2)
    for recruiter in recruiters:
        markup.add(types.InlineKeyboardButton(recruiter['name'], callback_data=f'recruiter_{recruiter["id"]}'))
    bot.send_message(
        msg.chat.id, 'اختر اسم القارئ', reply_markup=markup)

    
@bot.callback_query_handler(lambda call:True)
def callback_recruiter(call):
    if call.message:

        if 'recruiter' in call.data:
            print(call.data)
            chats_id = [i for i, e in enumerate(data) if e['chat'] == call.message.chat.id]
            data[chats_id[len(chats_id)-1]]['recruiter'] = call.data.split('_')[1]
            with open('data/users.json', 'w') as f:
                f.write(json.dumps(data))
            bot.send_message(call.message.chat.id, 'سيتم تجهيز الفيديو خلال لحظات')
            
            loading_msg = bot.send_message(call.message.chat.id, 'جاري تصميم الفيديو....')

            current = data[chats_id[len(chats_id)-1]]
            try:
                chat_status['active'] = False
                for id in range(current['start_ayah'], current['end_ayah']+1):
                    ayah = get_data(current['surah'], id, current['recruiter'])
                    print(ayah)
                    create_image(ayah['text'], id)
                    download_audio(ayah['audio'], id)

                    combine_audio_image(
                        f'data/audio/ayah_{id}.mp3',
                        f'data/images/ayah_{id}.png',
                        f'video_ayah_{id}',
                    )

                if current['start_ayah'] == current['end_ayah']:
                    concat_clip = mp.concatenate_videoclips([mp.VideoFileClip(f'data/output/video_ayah_{str(current["start_ayah"])}.mp4').crossfadein(1.0).crossfadeout(1.0)], method='compose')
                    concat_clip.write_videofile('data/output/output.mp4', fps=24, threads=8)

                    os.remove(f'data/output/video_ayah_{current["start_ayah"]}.mp4')
                else:
                    concat_clip = mp.concatenate_videoclips([mp.VideoFileClip(name).crossfadein(2.0).crossfadeout(2.0) for name in [f'data/output/video_ayah_{str(i)}.mp4' for i in range(current['start_ayah'], current['end_ayah']+1)]], method='compose')
                    concat_clip.write_videofile('data/output/output.mp4', fps=24, threads=8)

                    time.sleep(1)
                    for i in range(current["start_ayah"], current["end_ayah"]+1):
                        os.remove(f'data/output/video_ayah_{i}.mp4')

                bot.delete_message(call.message.chat.id, loading_msg.message_id)
                bot.send_video(call.message.chat.id, open('data/output/output.mp4', 'rb'))
                chat_status['active'] = True

            except Exception as e:
                print(e)
                bot.delete_message(call.message.chat.id, loading_msg.message_id)
                bot.send_message(call.message.chat.id, 'تعذر تحميل الفيديو\nيمكنك اعادة المحاولة لاحقا')
                chat_status['active'] = True

        elif 'surah' in call.data:
            if chat_status['active']:
                surah_num = int(call.data.split('_')[1])
                chats_id = [i for i, e in enumerate(
                    data) if e['chat'] == call.message.chat.id]
                data[chats_id[len(chats_id)-1]]['surah'] = surah_num
                next_msg = bot.send_message(call.message.chat.id, f"أدخل الآيات من 1 إلى {surahs[surah_num-1]['ayahs']}")
                bot.register_next_step_handler(next_msg, get_start_ayah)
            else:
                bot.send_message(call.message.chat.id, 'هناك شخص آخر يستخدم البرنامج في الوقت الحالي، يرجى المحاولة لاحقا')
    
    

        


print('POLLING....')
while True:
    bot.infinity_polling()
