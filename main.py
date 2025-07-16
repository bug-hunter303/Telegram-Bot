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
    await update.message.reply_text("...... It's a custom command")
    

# RESPONSE HANDLER

def handle_response(text: str) -> str:
    
    
    
