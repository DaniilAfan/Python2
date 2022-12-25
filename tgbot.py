from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg=update.message.text
    items=msg.split()
    x=int(items[1])
    y=int(items[2])
    await update.message.reply_text(f' {x}+ {y}={x+y}')

app = ApplicationBuilder().token("5947199515:AAHzlejtuN5x0wQnV2Z-4hjVCa5L5Btz-pQ").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_command))
print('server started')
app.run_polling()