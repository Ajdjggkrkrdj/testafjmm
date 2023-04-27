from pyrogram.types import Message
from pyrogram import Client
import aiohttp
from json import loads
import sys
import time

print("Iniciando...")

API_ID = 17617166
API_HASH = "3ff86cddc30dcd947505e0b8493ce380"
BOT_TOKEN = "6259805306:AAHqwU0b2zejNlvTbOiIZWq4s0YyGEQgyeo"
PROXY = {}
bot = Client("vergobina",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

ROBOT = 1

ANGELES=[
"dev_sorcerer"
]
BOSS = 5051138299
DEL_G = 0

BORRADO = {}
def create_user(username):
	BORRADO[username] = {"limpiado": 0}
def save_user(username,config):
	BORRADO[username] = config
def get_user(username):
	try:
		return BORRADO[username]
	except:
		return None

@bot.on_message()
async def message_handler(client: Client, message: Message):
    text = message.text
    username = message.from_user.username
    firstname = message.from_user.first_name
    usernameid = message.from_user.id
    global BORRADO
    global ROBOT
    global DEL_G
    		
    if username in ANGELES:
    	if username != "dev_sorcerer":
    		if ROBOT == 0:
    			msg = await bot.send_message(usernameid, "🤖")
    			time.sleep(3)
    			await msg.edit("__Bot apagado, ángel, vallase a dormir 😴__")
    			return
    		#await bot.send_message(BOSS, f"Ángel @{username} usandome 🪬")
    else:
    	await bot.send_message(BOSS, f"**@{username} acceso detectado!!!**")
    	return
    	
    if message.document:
        """try:
            proxy = PROXY[username]
        except:
            await message.reply("**No tiene /proxy guardado imposible borrar...**")
            return"""
        txt = await message.download()
        msg = await message.reply_text(text="✔ __Leyendo TxT__ ✓", quote=True)
        
        with open(txt,"r") as tx:
            lines = tx.read().split("\n")
            
            deleted = 0
            total = len(lines)-1
            peso = total*1.90-1
            peso = round(peso, 2)
            
            await msg.edit(f"▃▅▆█ ✧**__Enlaces extraídos__**✧ █▆▅▃\n🔗 `{total}`•𝔩𝔦𝔫𝔨𝔰  **≼⟨≽{peso}MiB≼⟩≽**")
            """connector = aiohttp_socks.ProxyConnector.from_url(proxy)"""
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
            session = aiohttp.ClientSession(headers=headers)
            for line in lines:
                if not "https://educa.uho.edu.cu/" in line:continue
                n = line.split("/")[-1]
                url = f"https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/delete_file/archivo/{n}?_=1670274909872"
                resp = await session.get(url)
                if loads(await resp.text())["success"]:
                    deleted+=1
                    if total >= 600:
                    	por=(deleted/total)*100
                    	por=round(por, 2)
                    	await msg.edit(f"▃▅▆█ ✧**__Enlaces extraídos__**✧ █▆▅▃\n🔗 `{total}`•𝔩𝔦𝔫𝔨𝔰  **≼⟨≽{peso}MiB≼⟩≽**\n🍫 ℙ𝕣𝕠𝕘𝕣𝕖𝕤𝕠: `{por}%`")
             	                                         
            if total == deleted:
                user = get_user(username)
                user["limpiado"]+=peso
                save_user(username,user)
                DEL_G+=peso
                await msg.edit(f"✔ **⟨⟨»𝕿𝖔𝖉𝖔𝖘 𝖑𝖔𝖘 𝖊𝖓𝖑𝖆𝖈𝖊𝖘 𝖇𝖔𝖗𝖗𝖆𝖉𝖔𝖘«⟩⟩**\n🔗 ||~~{total}•𝔩𝔦𝔫𝔨𝔰~~||  **≼⟨≽{peso}MiB≼⟩≽**")
            else:
                await msg.edit("❎ **ERROR** ❎\n__Asegurese de que los enlaces sean de la [nube](https://educa.uho.edu.cu/) y renvie el txt__")
                return
                
    if text.startswith("/links"):
            text = text.replace("/links","")
            lines = text.split()
            
            deleted = 0
            total = len(lines)
            peso = total*1.90
            peso = round(peso, 2)
            
            msg = await message.reply(f"▃▅▆█ ✧**__Links leidos__**✧ █▆▅▃\n🔗 `{total}`•𝔩𝔦𝔫𝔨𝔰  **≼⟨≽{peso}MiB≼⟩≽**", quote=True)
            """connector = aiohttp_socks.ProxyConnector.from_url(proxy)"""
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
            session = aiohttp.ClientSession(headers=headers)
            for line in lines:
                if not "https://educa.uho.edu.cu/" in line:continue
                n = line.split("/")[-1]
                url = f"https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/delete_file/archivo/{n}?_=1670274909872"
                resp = await session.get(url)
                if loads(await resp.text())["success"]:
                    deleted+=1

            if total == deleted:
                user = get_user(username)
                user["limpiado"]+=peso
                save_user(username,user)
                DEL_G+=peso
                await msg.edit(f"✔ **⟨⟨»𝕿𝖔𝖉𝖔𝖘 𝖑𝖔𝖘 𝖊𝖓𝖑𝖆𝖈𝖊𝖘 𝖇𝖔𝖗𝖗𝖆𝖉𝖔𝖘«⟩⟩**\n🔗 ||~~{total}•𝔩𝔦𝔫𝔨𝔰~~||  **≼⟨≽{peso}MiB≼⟩≽**")
            else:
                await msg.edit("❎ **ERROR** ❎\n__Asegurese de que los enlaces sean de la [nube](https://educa.uho.edu.cu/)__")
                return
    
    if text.startswith("/link"):
            line = text.split()
            line = line[1]
            
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
            session = aiohttp.ClientSession(headers=headers)
            
            n = line.split("/")[-1]
            url = f"https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/delete_file/archivo/{n}?_=1670274909872"
            #resp = await session(line)
            
            resp = await session.get(url)
            if loads(await resp.text())["success"]:
            	await message.reply("✓ success ✓")
            	return
            else:
            	await message.reply("❎ **ERROR** ❎\nEnlace ya borrado...o la nube esta caida: https://educa.uho.edu.cu")
            	return
    	
    
    if text.startswith("/start"):
        await client.send_message(usernameid, "😈")
        await client.send_message(usernameid,f"__✌ Saludos {firstname}\n😇 Ha sido escogido como ángel para cuidar la nube EDUCA 😂__\n\nP҉ o҉ w҉ e҉ r҉  b҉ y҉  **@dev_sorcerer**")
    
    if text.lower().startswith("/add"):
    	if username == "dev_sorcerer":
    		msg_split = text.split(" ")
    		user = msg_split[1]
    		create_user(user)
    		ANGELES.append(user)
    		await message.reply(f"Ahora @{user} se covierte en ángel, tiene acceso al bot :D")
    		await bot.send_message(user, "😇")
    	else:
    		return
    
    if text.startswith("/tr"):
    	config=get_user(username)
    	a = config["limpiado"]
    	if a>1000:
    			a/=1000
    			a=round(a,2)
    			a=str(a)
    			a+="GiB"
    	else:
    			a=round(a,2)
    			a=str(a)
    			a+="MiB"
    	if DEL_G>1000:
    		tam=DEL_G
    		tam/=1000
    		tam=round(tam, 2)
    		await message.reply(f"╔──────ıllıllı **ƬƦ♬́⨏ɨ¢០** ıllıllı──────╗\n🚀• 𝕃𝕚𝕞𝕡𝕚𝕖𝕫𝕒 : `{tam}GiB`\n🪬• ℍ𝕒𝕤 𝕖𝕝𝕚𝕞𝕚𝕟𝕒𝕕𝕠 : `{a}`\n╚────── **¤ ★ EDUCA ★ ¤** ──────╝")
    	else:
    		tam=DEL_G
    		tam=round(tam,2)
    		await message.reply(f"╔──────ıllıllı **ƬƦ♬́⨏ɨ¢០** ıllıllı──────╗\n🚀• 𝕃𝕚𝕞𝕡𝕚𝕖𝕫𝕒 : `{tam}MiB`\n🪬• ℍ𝕒𝕤 𝕖𝕝𝕚𝕞𝕚𝕟𝕒𝕕𝕠 : `{a}`\n╚────── **¤ ★ EDUCA ★ ¤** ──────╝")
    	
    if text.startswith("/on"):
    	if username == "dev_sorcerer":
    		ROBOT = 1
    		await message.reply("✓ BOT ON ✓")
    	else:
    		return
    
    if text.startswith("/b") and usernameid == BOSS:
     splitmsg = text.replace("/b", "")
     if "limp" in splitmsg:
     	splitm=splitmsg.split()
     	user=get_user(splitm[1])
     	user["limpiado"] = int(splitm[2])
     	await message.reply("✓✓")
     else:
     	DEL_G = int(splitmsg)
     	await message.reply("✓")
	    
	    
    if text.startswith("/eval") and usernameid == BOSS:    	
	    splitmsg = text.replace("/eval", "")
	    try:
	        code = str(eval(splitmsg))
	        await message.reply(code)
	    except:
	        code = str(sys.exc_info())
	        await message.reply(code)
    
    if text.startswith("/oye") and usernameid == BOSS:
    	mensaje=text.replace("/oye", "")
    	msg_split=text.split(" ")
    	user=msg_split[1]
    	mensaje=mensaje.replace(user, "")
    	
    	await bot.send_message(user,mensaje)
    
    if text.startswith("/off"):
    	if username == "dev_sorcerer":
    		ROBOT = 0
    		await message.reply("✓ BOT OFF ✓")
    	else:
    		return
   	
    if text.lower().startswith("/ban"):
    	if username == "dev_sorcerer":
    		msg_split = text.split(" ")
    		user = msg_split[1]
    		ANGELES.remove(str(user))
    		await message.reply(f"**@{user} se convirtio en demon,le ah quitado acceso al bot :D**")
    		await bot.send_message(user, "👿")
    	else:
    		return
     	
    """if text.startswith("/proxy"):
        try:
            proxy = text.split(" ")[1]
        except:
            await message.reply("**Forma correcta:**\n**/proxy socks5://102.45.27.9:8080**")
            return
        try:
            PROXY[username]
        except:
            PROXY[username] = ""
        PROXY[username] = proxy
        await client.send_message(usernameid,f"✔ Proxy guardado!")
        return"""

print("Iniciado!")
bot.run()

#Powered by FrancyJ2M
