import telebot
from telebot import types

TOKEN = '5864755813:AAGtAx1aYMJGUCPuMWt0wiSjbZ_5FiaEZ5A'
bot = telebot.TeleBot(TOKEN)

surahs = [
	{"surah":1, "name": "الفاتحة"},
	{"surah":2, "name": "البقرة"},
	{"surah":3, "name": "آل عمران"},
	{"surah":4, "name": "النساء"},
	{"surah":5, "name": "المائدة"},
	{"surah":6, "name": "الأنعام"},
	{"surah":7, "name": "الأنفال"},
	{"surah":9, "name": "التوبة"},
	{"surah":10, "name": "يونس"},
	{"surah":11, "name": "هود"},
	{"surah":12, "name": "يوسف"},
	{"surah":13, "name": "الرعد"},
	{"surah":14, "name": "ابراهيم"},
	{"surah":15, "name": "الحجر"},
	{"surah":16, "name": "النحل"},
	{"surah":17, "name": "الإسراء"},
	{"surah":18, "name": "الكهف"},
	{"surah":19, "name": "مريم"},
	{"surah":20, "name": "طه"},
	{"surah":21, "name": "الأنبياء"},
	{"surah":22, "name": "الحج"},
	{"surah":23, "name": "المؤمنون"},
	{"surah":24, "name": "النور"},
	{"surah":25, "name": "الفرقان"},
	{"surah":26, "name": "الشعراء"},
	{"surah":27, "name": "النمل"},
	{"surah":28, "name": "القصص"},
	{"surah":29, "name": "العنكبوت"},
	{"surah":30, "name": "الروم"},
	{"surah":31, "name": "لقمان"},
	{"surah":32, "name": "السجدة"},
	{"surah":33, "name": "الأحزاب"},
	{"surah":34, "name": "سبإ"},
	{"surah":35, "name": "فاطر"},
	{"surah":36, "name": "يس"},
	{"surah":37, "name": "الصافات"},
	{"surah":38, "name": "ص"},
	{"surah":39, "name": "الزمر"},
	{"surah":40, "name": "غافر"},
	{"surah":41, "name": "فصلت"},
	{"surah":42, "name": "الشورى"},
	{"surah":43, "name": "الزخرف"},
	{"surah":44, "name": "الدخان"},
	{"surah":45, "name": "الجاثية"},
	{"surah":46, "name": "الأحقاف"},
	{"surah":47, "name": "محمد"},
	{"surah":48, "name": "الفتح"},
	{"surah":49, "name": "الحجرات"},
	{"surah":50, "name": "ق"},
	{"surah":51, "name": "الذاريات"},
	{"surah":52, "name": "الطور"},
	{"surah":53, "name": "النجم"},
	{"surah":54, "name": "القمر"},
	{"surah":55, "name": "الرحمن"},
	{"surah":56, "name": "الواقعة"},
	{"surah":57, "name": "الحديد"},
	{"surah":58, "name": "المجادلة"},
	{"surah":59, "name": "الحشر"},
	{"surah":60, "name": "الممتحنة"},
	{"surah":61, "name": "الصف"},
	{"surah":62, "name": "الجمعة"},
	{"surah":63, "name": "المنافقون"},
	{"surah":64, "name": "التغابن"},
	{"surah":65, "name": "الطلاق"},
	{"surah":66, "name": "التحريم"},
	{"surah":67, "name": "الملك"},
	{"surah":68, "name": "القلم"},
	{"surah":69, "name": "الحاقة"},
	{"surah":70, "name": "المعارج"},
	{"surah":71, "name": "نوح"},
	{"surah":72, "name": "الجن"},
	{"surah":73, "name": "المزمل"},
	{"surah":74, "name": "المدثر"},
	{"surah":75, "name": "القيامة"},
	{"surah":76, "name": "الانسان"},
	{"surah":77, "name": "المرسلات"},
	{"surah":78, "name": "النبإ"},
	{"surah":79, "name": "النازعات"},
	{"surah":80, "name": "عبس"},
	{"surah":81, "name": "التكوير"},
	{"surah":82, "name": "الإنفطار"},
	{"surah":83, "name": "المطففين"},
	{"surah":84, "name": "الإنشقاق"},
	{"surah":85, "name": "البروج"},
	{"surah":86, "name": "الطارق"},
	{"surah":87, "name": "الأعلى"},
	{"surah":88, "name": "الغاشية"},
	{"surah":89, "name": "الفجر"},
	{"surah":90, "name": "البلد"},
	{"surah":91, "name": "الشمس"},
	{"surah":92, "name": "الليل"},
	{"surah":93, "name": "الضحى"},
	{"surah":94, "name": "الشرح"},
	{"surah":95, "name": "التين"},
	{"surah":96, "name": "العلق"},
	{"surah":97, "name": "القدر"},
	{"surah":98, "name": "البينة"},
	{"surah":99, "name": "الزلزلة"},
	{"surah":100, "name": "العاديات"},
	{"surah":101, "name": "القارعة"},
	{"surah":102, "name": "التكاثر"},
	{"surah":103, "name": "العصر"},
	{"surah":104, "name": "الهمزة"},
	{"surah":105, "name": "الفيل"},
	{"surah":106, "name": "قريش"},
	{"surah":107, "name": "الماعون"},
	{"surah":108, "name": "الكوثر"},
	{"surah":109, "name": "الكافرون"},
	{"surah":110, "name": "النصر"},
	{"surah":111, "name": "المسد"},
	{"surah":112, "name": "الإخلاص"},
	{"surah":113, "name": "الفلق"},
	{"surah":114, "name": "الناس"}
]

@bot.message_handler(commands=['start'])
def send_message(msg):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('اختر السورة'))
    bot.send_message(msg.chat.id, 'أهلا بك\nيمكنك البدء في تصميم الفيديوهات عن طريق هذا الزر', reply_markup=markup)


@bot.message_handler()
def keyboard_res(msg):
    if msg.text == 'اختر السورة':
        markup = types.InlineKeyboardMarkup(row_width=2)
        for surah in surahs:
            markup.add(types.InlineKeyboardButton(surah['name'], callback_data=f'surah_{surah["surah"]}'))

        bot.send_message(msg.chat.id, 'قم باختيار سورة من القائمة', reply_markup=markup)

@bot.callback_query_handler(lambda call: True)
def callback_data(call):
    if call.message:
        if call.data in [f'surah_{id}' for id in range(1, 115)]:
            surah_id = call.data.split('_')[1]
            bot.reply_to(call.message, text=surah_id)
        

bot.infinity_polling()