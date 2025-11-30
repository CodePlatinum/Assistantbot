from telegram.ext import Updater, CommandHandler

TOKEN = "8438299884:AAHQg5xLTto1bZvCcR4ygmeHcnYk2GmSD6M"

# Replace this later with your actual link
YOUR_LINK = "https://example.com"

def start(update, context):
    update.message.reply_text(f"Here is your link:\n{YOUR_LINK}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
