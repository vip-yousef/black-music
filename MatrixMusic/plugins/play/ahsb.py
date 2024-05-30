from pyrogram import Client, filters
from pyrogram.types import Message
from MatrixMusic import app
from strings.filters import command
from config import OWNER_ID

@app.on_message(command("احسب"))
def A1RTR(client, message):   
    atari = message.text.split("احسب ", 1)[1]
    
    try:        
        result = eval(atari.replace("×", "*").replace("÷", "/"))  #Rsexs
        response = f"≭︰الناتج هو : {result}"
    except:
        response = "≭︰اكتب بالصيغة الصحيحة مثل: احسب 4 + 10 * 14"
        
    message.reply(response)
