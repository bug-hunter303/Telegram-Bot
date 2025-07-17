from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final

TOKEN: Final = '8154824294:AAFhf6GaTYI2RBWdi_8cBhV413FX-Oy4w9o'
BOT_USERNAME: Final = '@AanKubot'


# COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Oho bhai, kaam paenau ma sanga chat garna aatexau ta !')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Thukka babu , I am a CHATBOT idiot . Type smth so I can respond.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ankit bhanne manxe le banako ho yo tara I am under development , for now just type hi , hello , how are you , thankyou ")
    

# RESPONSE HANDLER

def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hi babu, pada yr kaam xaina berojgar bot sanga kura garxa'
    
    if 'how are you' in processed:
        return 'Not good , I am broke AF bro paisa haldeu esewa ma : 9745692024'
    
    if 'hi' in processed:
        return 'Hyaa mula , lame ass padna ja , BOLNA MAANXAINA MALAI'
    
    if 'thankyou' in processed:
        return "You're welcome bro , thank you for using me future updates coming soon !"
    
    if 'nai' in processed:
        return 'Bujnu paryo ni ta FUCCHE'
    
    return "Ae bhai i am still under development , only use 'hi','hello','thankyou','how are you'. BUJEU? / TYPE nai"
    
    
async def handle_message(update: Update,context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: {text}')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
            
        else:
            return
    else:
        response: str = handle_response(text)
        
    print('Bot:',response)
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
if __name__ == '__main__':
    print('STARTING BOT.....')
    app = Application.builder().token(TOKEN).build()
    
    # COMMANDS
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    
    # MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # ERRORS
    app.add_error_handler(error)
    
    # POLLING THE BOT
    print('POLLING....')
    app.run_polling(poll_interval=2)
    
    
    
