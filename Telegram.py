from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

TOKEN = "6222671703:AAEhmTR3O_6ETRJyfvJUybKxoCc2kURg6CI"
ADMIN_USERNAME = "716752339"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! How can I assist you? 🗿')

def echo(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=ADMIN_USERNAME, text=f"From @{update.effective_user.username}: {update.message.text}")
    # Send the "thanks" message and provide a custom inline keyboard with the "New case" button.
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("New case", callback_data="new_case")]])
    update.message.reply_text('Thanks for contacting, we will contact you in direct message ASAP 🫡', reply_markup=reply_markup)

def handle_new_case(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'new_case':
        query.message.reply_text('Hello! How can I assist you today?')

def reply_to_user(update: Update, context: CallbackContext) -> None:
    target_user, msg = update.message.text.split(maxsplit=1)
    context.bot.send_message(chat_id=target_user, text=f"Reply from {ADMIN_USERNAME}: {msg}")

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(CallbackQueryHandler(handle_new_case))
    dispatcher.add_handler(MessageHandler(Filters.user(username=ADMIN_USERNAME) & Filters.reply, reply_to_user))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
