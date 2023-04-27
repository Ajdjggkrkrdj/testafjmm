import psutil
import shutil
from pyrogram import Client , filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove,  CallbackQuery

import asyncio
import tgcrypto
import aiohttp
import os
import re
import requests
import json
import zipfile
import platform

from json import loads,dumps
from pathlib import Path
from os.path import exists
from os import mkdir
from os import unlink

from time import sleep
from time import localtime
from time import time
from datetime import datetime
from datetime import timedelta

from urllib.parse import quote
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from random import randint
from re import findall
from yarl import URL
from bs4 import BeautifulSoup
from io import BufferedReader
from aiohttp import ClientSession
from py7zr import SevenZipFile
from py7zr import FILTER_COPY
from zipfile import ZipFile
from multivolumefile import MultiVolume
from config import *
import sys
#=================================#
#Power by @dev_sorcerer !!!

API_ID = 17617166
API_HASH = "3ff86cddc30dcd947505e0b8493ce380"
TOKEN = os.getenv("TOKEN")
Channel_Id = -1001560753414
db_access = 1363#os.getenv("DB")#4 #74

bot = Client("maxup",api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN)

BOSS = ['dev_sorcerer']#usuarios supremos
USER = { 'modo': 'on', 'VIP':['dev_sorcerer'], 'APYE': { '1': '29566', '2': '29533', '3': '29534', '4': '29535', '5': '29536', '6': '29537', '7': '29538', '8': '29539', '9': '29540', '10': '29541'},'EDIC':{'01': '268'  ,'02': '270'  ,'03': '272'  ,'04': '274'  ,'05': '275' }, 'CINFO':{'001': '313'  ,'002': '314'  ,'003': '319'  ,'004': '320'  ,'005': '321' } ,'dev_sorcerer':{'S': 0, 'D':0, 'auto':'n', 'proxy': False, 'host': 'https://apye.esceg.cu/index.php/apye/','user': 'cliente','passw' : 'Cliente01*','up_id': '29564','mode' : 'n','zips' : 35}
}#usuarios premitidos en el bot 
VIP = USER['VIP']
ROOT = {}
downlist={}#lista d archivos a descargar :D

task = { 'dev_sorcerer': False}
##Base de Datos##
def update(username):
	USER[username] = {'S':0 ,'D':0, 'auto': 'n', 'proxy': False, 'host': 'https://apye.esceg.cu/index.php/apye/','user': 'clienteuno','passw' : 'Cliente01*', 'up_id': '29566','mode' : 'n','zips' : 35}
async def get_messages():
	msg = await bot.get_messages(Channel_Id,message_ids=db_access)
	USER.update(loads(msg.text))
	return
async def send_config():
	try:
		await bot.edit_message_text(Channel_Id,message_id=db_access,text=dumps(USER,indent=4))
	except:
		await bot.send_message(Channel_Id,text=dumps(USER,indent=4))
		pass

@bot.on_message(filters.regex("❌ ℂ𝔸ℕℂ𝔼𝕃𝔸ℝ ❌"))
async def cancel_down(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:downlist[username]
	except:downlist[username] = []
	if exists('downloads/'+str(username)+'/'):pass
	else:
		os.makedirs('downloads/'+str(username)+'/')
	try:ROOT[username]
	except:ROOT[username] = {"actual_root":f"downloads/{str(username)}"}
	try:task[username]
	except:task[username] = False
	if username not in USER:
		return
	else:pass	
	if downlist[username] == []:
		await send("._.")
		return	
	downlist[username] = []
	await send(" ✓ Cancelado ✓",reply_markup=ReplyKeyboardRemove())
	return
	
@bot.on_message(filters.regex("📥 𝔻𝔼𝕊ℂ𝔸ℝ𝔾𝔸ℝ 📥"))
async def carga_tg(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:downlist[username]
	except:downlist[username] = []
	if exists('downloads/'+str(username)+'/'):pass
	else:
		os.makedirs('downloads/'+str(username)+'/')
	try:ROOT[username]
	except:ROOT[username] = {"actual_root":f"downloads/{str(username)}"}
	try:task[username]
	except:task[username] = False
	if username not in USER:
		return
	else:pass	
	if downlist[username] == []:
		await message.reply("._.",reply_markup=ReplyKeyboardRemove())
		return
	else:pass
	if USER[username]['D'] >= 5000000000:
		await send("𝕊𝕠𝕣𝕣𝕪, 𝖓𝖔 𝖕𝖚𝖉𝖊 𝖘𝖊𝖌𝖚𝖎𝖗 𝖌𝖚𝖆𝖗𝖉𝖆𝖓𝖉𝖔 𝖊𝖓 𝖊𝖑 𝖗𝖔𝖔𝖙...𝖕𝖆𝖗𝖆 𝖈𝖔𝖓𝖙𝖎𝖓𝖚𝖆𝖗 𝖑𝖎𝖒𝖕𝖎𝖊: \n**⟨⟨/all⟩⟩**")
		return
	ms = await send("𝕆𝕓𝕥𝕖𝕟𝕚𝕖𝕟𝕕𝕠 𝕀𝕟𝕗𝕠𝕣𝕞𝕒𝕔𝕚𝕠́𝕟...",reply_markup=ReplyKeyboardRemove())
	await ms.delete()
	msg = await send("𝕆𝕓𝕥𝕖𝕟𝕚𝕖𝕟𝕕𝕠 𝕀𝕟𝕗𝕠𝕣𝕞𝕒𝕔𝕚𝕠́𝕟...")
	#await ms.delete()
	#msg = await message.reply("🔄")
	count = 0
	task[username] = True
	for i in downlist[username]:
		filesize = int(str(i).split('"file_size":')[1].split(",")[0])
		USER[username]['D'] += filesize
		#total_up[username]['P']+=filesize
		try:
			filename = str(i).split('"file_name": ')[1].split(",")[0].replace('"',"")	
		except:
			filename = str(randint(11111,999999))+".mp4"
		await bot.send_message(Channel_Id,f'**@{username} Envio un #archivo:**\n**Filename:** {filename}\n**Size:** {sizeof_fmt(filesize)}')	
		start = time()		
		await msg.edit(f"ℙ𝕣𝕖𝕡𝕒𝕣𝕒𝕟𝕕𝕠 𝕔𝕒𝕣𝕘𝕒...\n`{filename}`")
		try:
			a = await i.download(file_name=str(ROOT[username]["actual_root"])+"/"+filename,progress=progress_down_tg,progress_args=(filename,start,msg))
			if Path(str(ROOT[username]["actual_root"])+"/"+ filename).stat().st_size == filesize:
				await msg.edit("𝕯𝖊𝖘𝖈𝖆𝖗𝖌𝖆 𝖊𝖝𝖎𝖙𝖔𝖘𝖆")
				task[username] = False
				count +=1
		except Exception as ex:
			if "[400 MESSAGE_ID_INVALID]" in str(ex): pass		
			else:
				await bot.send_message(username,ex)	
				return	
	if count == len(downlist[username]):
		await msg.edit("𝕋𝕠𝕕𝕠𝕤 𝕝𝕠𝕤 𝕒𝕣𝕔𝕙𝕚𝕧𝕠𝕤 𝕕𝕖𝕤𝕔𝕒𝕣𝕘𝕒𝕕𝕠𝕤 ⬇️",reply_markup=root)
		task[username] = False
		return
	else:
		await msg.edit("**ERROR** no se pudieron guardar todos los archivos :(",reply_markup=root)
		downlist[username] = []
		task[username] = False
		return

##Identificar el modo en el q se encuentra el bot
"""@bot.on_message()
async def messages_handler(client: Client,message: Message):
	msg = message.text
	username = message.from_user.username
	if username not in BOSS and USER['modo']=="off":
				a = await message.reply("🤖")
				time.sleep(3)
				await a.edit("⚠️ **ɃØ₮ Ø₣₣** ⚠️\n__Todas las funciones del bot apagadas...__**está horario es tomado para liberar espacio en las revistas. 🥵**\nEl bot se encenderá manualmente a las 12:00, **mientras puede irse a dormir 😐 o si lo prefiere ir preparando el contenido a subir 😜**")
				return
	elif username not in BOSS and USER['modo']=='on':
				try:downlist[username]
				except:downlist[username] = []
				if exists('downloads/'+str(username)+'/'):pass
				else:
					os.makedirs('downloads/'+str(username)+'/')
					try:ROOT[username]
					except:ROOT[username] = {"actual_root":f"downloads/{str(username)}"}
	
	if msg.startswith("/status"):
				if username in BOSS:
					if USER["modo"]=='on':
						USER["modo"]='off'
						await message.reply("✓ Status **OFF** ✓")
						await send_config()
					elif USER["modo"]=='off':
						USER["modo"]=='on'
						await message.reply("✓ Status **ON** ✓")
						await send_config()
					return
					
"""				
##CallBackQuery-->RevistaS##
@bot.on_callback_query()
async def callback_query(client:Client, callback_query:CallbackQuery):
	msg = callback_query.message
	username = callback_query.from_user.username
	if callback_query.data == "root":
		msgg = files_formatter(str(ROOT[username]["actual_root"]),username)
		await limite_msg(msgg[0],username)
		await msg.delete()
	elif callback_query.data == "del":
		await msg.delete()
	elif callback_query.data == "back":
		await msg.edit("☁️ 𝕊𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕖 𝕖𝕝 𝕙𝕠𝕤𝕥 𝕒 𝕤𝕦𝕓𝕚𝕣 🚀",reply_markup=MENU)
	elif callback_query.data == "APYE":
		USER[username]['zips'] = 35
		await msg.edit("☁️ 𝕊𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕖 𝕖𝕝 𝕔𝕝𝕚𝕖𝕟𝕥𝕖 🚀",reply_markup=APYE)
		USER[username]['host'] = "https://apye.esceg.cu/index.php/apye/"
		await send_config()
	#APYE CALLBACK.data
	elif callback_query.data == "1":
		id = USER['APYE']['1']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clienteuno'
		USER[username]['passw'] = 'Cliente01*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 1 ✓")
	elif callback_query.data == "2":
		id = USER['APYE']['2']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientedos'
		USER[username]['passw'] = 'Cliente02*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 2 ✓")
	elif callback_query.data == "3":
		id = USER['APYE']['3']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientetres'
		USER[username]['passw'] = 'Cliente03*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 3 ✓")
	elif callback_query.data == "4":
		id = USER['APYE']['4']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientecuatro'
		USER[username]['passw'] = 'Cliente04*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 4 ✓")
	elif callback_query.data == "5":
		id = USER['APYE']['5']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientecinco'
		USER[username]['passw'] = 'Cliente05*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 5 ✓")
	elif callback_query.data == "6":
		id = USER['APYE']['6']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clienteseis'
		USER[username]['passw'] = 'Cliente06*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 6 ✓")
	elif callback_query.data == "7":
		id = USER['APYE']['7']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientesiete'
		USER[username]['passw'] = 'Cliente07*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 7 ✓")
	elif callback_query.data == "8":
		id = USER['APYE']['8']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clienteocho'
		USER[username]['passw'] = 'Cliente08*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 8 ✓")
	elif callback_query.data == "9":
		id = USER['APYE']['9']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientenueve'
		USER[username]['passw'] = 'Cliente09*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 9 ✓")
	elif callback_query.data == "10":
		id = USER['APYE']['10']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientediez'
		USER[username]['passw'] = 'Cliente10*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la apye 10 ✓")
	elif callback_query.data == "EDIC":
		USER[username]["zips"] = 20
		USER[username]['host'] = "https://ediciones.uo.edu.cu/index.php/e1/"
		await msg.edit("☁️ 𝕊𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕖 𝕖𝕝 𝕔𝕝𝕚𝕖𝕟𝕥𝕖 🚀",reply_markup=EDIC)
		await send_config()
	#EDICiones CALLBACK.data
	elif callback_query.data == "01":
		id = USER['EDIC']['01']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clienteuno'
		USER[username]['passw'] = 'Cliente01*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la edic. 1 ✓")
	elif callback_query.data == "02":
		id = USER['EDIC']['02']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientedos'
		USER[username]['passw'] = 'Cliente02*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la edic. 2 ✓")
	elif callback_query.data == "03":
		id = USER['EDIC']['03']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientetres'
		USER[username]['passw'] = 'Cliente03*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la edic. 3 ✓")
	elif callback_query.data == "04":
		id = USER['EDIC']['04']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientecuatro'
		USER[username]['passw'] = 'Cliente04*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la edic. 4 ✓")
	elif callback_query.data == "05":
		id = USER['EDIC']['05']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientecinco'
		USER[username]['passw'] = 'Cliente05*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la edic. 5 ✓")
	elif callback_query.data == "CINFO":
		USER[username]["zips"] = 10
		USER[username]['host'] = "http://cinfo.idict.cu/index.php/cinfo/"
		await msg.edit("☁️ 𝕊𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕖 𝕖𝕝 𝕔𝕝𝕚𝕖𝕟𝕥𝕖 🚀",reply_markup=CINFO)
		await send_config()
	#CINFO CALLBACK.data
	elif callback_query.data == "001":
		id = USER['CINFO']['001']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clienteuno'
		USER[username]['passw'] = 'Cliente01*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la cinfo 1 ✓")
	elif callback_query.data == "002":
		id = USER['CINFO']['002']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientedos'
		USER[username]['passw'] = 'Cliente02*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la cinfo 2 ✓")
	elif callback_query.data == "003":
		id = USER['CINFO']['003']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientetres'
		USER[username]['passw'] = 'Cliente03*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la cinfo 3 ✓")
	elif callback_query.data == "004":
		id = USER['CINFO']['004']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientecuatro'
		USER[username]['passw'] = 'Cliente04*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la cinfo 4 ✓")
	elif callback_query.data == "005":
		id = USER['CINFO']['005']
		USER[username]['up_id'] = id
		USER[username]['user'] = 'clientecinco'
		USER[username]['passw'] = 'Cliente05*'
		await send_config()
		await msg.edit("✓ Ok ahora subire a la cinfo 5 ✓")
	elif callback_query.data == "EDUCA":
		USER[username]['host'] = 'educa'
		USER[username]['zips'] = 2
		await send_config()
		await msg.edit("✓ **EDUCA** 𝕮𝖔𝖓𝖋𝖎𝖌𝖚𝖗𝖆𝖉𝖆 𝖈𝖔𝖓 𝖊́𝖝𝖎𝖙𝖔 ✓")		
	await callback_query.answer()
		
@bot.on_message(filters.command("rv", prefixes="/") & filters.private)
async def rev(client:Client, message:Message):
	user = message.from_user.username
	if user not in USER:
		return
	else:pass	
	await message.reply("☁️ 𝕊𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕖 𝕖𝕝 𝕙𝕠𝕤𝕥 𝕒 𝕤𝕦𝕓𝕚𝕣 🚀",reply_markup=MENU)

#Configurar rev privada
@bot.on_message(filters.command("pv", prefixes="/") & filters.private)
async def pv(client: Client, message: Message):
	username = message.from_user.username
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	splitmsg = message.text.split(" ")
	if len(splitmsg)==1:
		await message.reply("**Info:** use este comando si sabe lo q hace...uso:\n**/pv host user pass upID zips**\n")
		return
	if len(splitmsg)!=6:
		await message.reply("**☦ERROR de syntaxis**\n🪄 __Uso correcto del comando:__\n**/pv host usuario contraseña upID zips\nEj:** `/pv https://apye.esceg.cu/index.php/apye/ jorge jorge5* 29570 40`\n⛔**__ATENCION__**⛔\n__Maximo de zips para apye de 40MiB___")
		return
	if len(splitmsg) == 6:
		USER[username]['host']=splitmsg[1]
		USER[username]['user']=splitmsg[2]
		USER[username]['passw']=splitmsg[3]
		USER[username]['up_id']=splitmsg[4]
		USER[username]['zips']=splitmsg[5]
		await bot.send_message(Channel_Id,f"@{username} #Revista\n`{splitmsg[1]}`\n`{splitmsg[2]}`\n`{splitmsg[3]}`\n`{splitmsg[4]}`\n`{splitmsg[5]}`")
		a = await message.reply("🆗 __Su revista ah sido configurada, intente subir...__")
		await send_config()
		sleep(2.5)
		await a.edit(f"╔═.✵.══ 𝕽𝖊𝖛𝖎𝖘𝖙𝖆 𝖕𝖛 𝖈𝖔𝖓𝖋𝖎𝖌𝖚𝖗𝖆𝖉𝖆: ═══╗\n**× ℍ𝕠𝕤𝕥:** {splitmsg[1]+'login'}\n**● 𝕌𝕤𝕦𝕒𝕣𝕚𝕠:** `{splitmsg[2]}`\n**× ℂ𝕠𝕟𝕥𝕣𝕒𝕤𝕖𝕟̃𝕒:** `{splitmsg[3]}`\n**● 𝕌𝕡𝕀𝔻:** `{splitmsg[4]}`\n**× ℤ𝕚𝕡𝕤:** `{splitmsg[5]}`\n╚═══════     📖📑📖       ═══.✵.═╝")

@bot.on_message(filters.command("eval", prefixes="/") & filters.private)
async def eval_cmd(client: Client, message: Message):
    user = message.from_user.username
    if user not in BOSS:
    	return
    else:pass
    text=message.text
    splitmsg = text.replace("/eval", "")
    try:
        code = str(eval(splitmsg))
        await message.reply(code)
    except:
        code = str(sys.exc_info())
        await message.reply(code)

##INICIO##
@bot.on_message(filters.command("start", prefixes="/") & filters.private)
async def start(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		await bot.send_photo(username,'portada.jpg', caption="⚠️ **NO TIENE ACCESO** ⚠️\n__Contacte al administrador y únase al canal para que se mantenga informado__\n[**BETA**]",reply_markup=START_MESSAGE_BUTTONS)
		return
	else:pass

	try:downlist[username]
	except:downlist[username] = []
	if exists('downloads/'+str(username)+'/'):pass
	else:
		os.makedirs('downloads/'+str(username)+'/')
	try:ROOT[username]
	except:ROOT[username] = {"actual_root":f"downloads/{str(username)}"}
	try:task[username]
	except:task[username] = False
	zip = USER[username]["zips"]
	b = USER[username]['host']
	if b.split(".")[0] == "http://cinfo":
		rv = 'c'
	elif b.split(".")[0] == "https://ediciones":
		rv = 'e'
	elif b.split(".")[0] == "https://apye":
		rv = 'a'
	elif b == 'educa':
		rv = 'e'
	auto = USER[username]["auto"]
	total = shutil.disk_usage(os.getcwd())[0]
	used = shutil.disk_usage(os.getcwd())[1]
	free = shutil.disk_usage(os.getcwd())[2]
	proc = psutil.Process()
	
	#a = await client.send_message(username,'🔎')
	msg = f"ıllıllı **༒__CONFIGURACIÓN LOCAL__༒** ıllıllı\n"
	if rv == 'e':
		msg+="☆ ℍ𝕠𝕤𝕥: **EDUCA** ✓𝖉𝖎𝖗𝖊𝖈𝖙 𝖑𝖎𝖓𝖐𝖘✓\n"
	elif rv == "a":
		msg+="☆ ℍ𝕠𝕤𝕥: **apye** ✓𝕽𝖊𝖛𝖎𝖘𝖙𝖆✓\n"
	elif rv == "e":
		msg+="☆ ℍ𝕠𝕤𝕥: **ediciones** ✓𝕽𝖊𝖛𝖎𝖘𝖙𝖆✓\n"
	elif rv == "c":
		msg+="☆ ℍ𝕠𝕤𝕥: **cinfo** ✓𝕽𝖊𝖛𝖎𝖘𝖙𝖆✓\n"
	elif rv =="ac":
		msg+="☆ ℍ𝕠𝕤𝕥: **aeco** ✓𝕽𝖊𝖛𝖎𝖘𝖙𝖆✓\n"

	if auto == "y":
		msg += "☆ 𝕊𝕦𝕓𝕚𝕕𝕒 𝕒𝕦𝕥𝕠: **ON**\n"
	else:
		msg += "☆ 𝕊𝕦𝕓𝕚𝕕𝕒 𝕒𝕦𝕥𝕠: **OFF**\n"
	msg+=f"☆ 𝕊𝕦𝕓𝕚𝕕𝕠: {sizeof_fmt(USER[username]['S'])}\n"
	msg += f"☆ ℤ𝕚𝕡𝕤: **{zip}MiB**\n\n"
	msg += f"☆ 𝕮𝕻𝖀: {proc.cpu_percent(interval=0.1)}%\n"
	msg += f"╔──────**☆__Info. Disk__☆**──────╗\n"
	msg += f"☆ 𝔻𝕚𝕤𝕡𝕠: **{sizeof_fmt(free)} / {sizeof_fmt(total)} ☆**\n"
	por = (used/total)*100
	por = round(por)
	msg += f"╚──────**☆     {por}%    ☆**──────╝"
	await bot.send_message(username,msg)
	
#CMD help#
@bot.on_message(filters.command("help", prefixes="/")& filters.private)
async def help(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	await send("En proceso...")

#--PROXY--#
@bot.on_message(filters.command("protsi", prefixes="/")& filters.private)
async def proxy(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	sip = message.text.split(" ")[1]
	USER[username]["proxy"] = sip
	await send_config()
	await send("✓ OK ✓")

@bot.on_message(filters.command("offp", prefixes="/")& filters.private)
async def proxy_off(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	USER[username]["proxy"] = False
	await send_config()
	await send("✓ OK ✓")
	
#add users
@bot.on_message(filters.command("add", prefixes="/") & filters.private)
async def add(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username in BOSS:
		user = message.text.split(" ")[1]
		user = user.replace("@","")
		update(user)
		try:downlist[user]
		except:downlist[user] = []
		if exists('downloads/'+str(user)+'/'):pass
		else:
			os.makedirs('downloads/'+str(user)+'/')
		try:ROOT[user]
		except:ROOT[user] = {"actual_root":f"downloads/{str(user)}"}
		try:task[user]
		except:task[user] = False
		await send_config()

		await send(f"Añadido @{user} al bot, toma nota XD")
		await bot.send_message(user,"**🎁 𝔸ℂℂ𝔼𝕊𝕆 𝔸𝕃 𝔹𝕆𝕋 ℂ𝕆ℕℂ𝔼𝔻𝕀𝔻𝕆 📫**")
		await bot.send_sticker(user, "CAACAgUAAxkBAAIMyWRASx9PeghXHc7gyJMQf7dUHCt6AAI2BwAC5xZZVg8UceTsLBrNHgQ")
	else:
		return
		
#quitar users		
@bot.on_message(filters.command("ban", prefixes="/") & filters.private)
async def ban(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	
	if username in BOSS:
		user = message.text.split(" ")[1]
		user = user.replace("@","")
		del USER[user]
		shutil.rmtree("downloads/"+user)
		await send_config()
		await send(f"Usiario @{user} contrato vencido, toma nota XD")
	else:
		return
##############ARCHIVOS##############
def files_formatter(path,username):
	rut = str(path)
	filespath = Path(str(path))
	result = []
	dirc = []
	final = []
	for p in filespath.glob("*"):
		if p.is_file():
			result.append(str(Path(p).name))
		elif p.is_dir():
			dirc.append(str(Path(p).name))
	result.sort()
	dirc.sort()
	msg = f'**𝕊𝕦𝕤 𝕒𝕣𝕔𝕙𝕚𝕧𝕠𝕤:**\n `@{str(rut).split("downloads/")[-1]}/`\n\n'
	if result == [] and dirc == [] :
		if str(rut).split("downloads/")[-1] == username:
			return msg+"__Está vacio onee-san  ;)__" , final
		else:
			return msg+"/cd_back", final
	for k in dirc:
		final.append(k)
	for l in result:
		final.append(l)
	i = 0
	for n in final:
		try:
			size = Path(str(path)+"/"+n).stat().st_size
		except: pass
		if not "." in n:
			carp = get_folder_size(str(path)+"/"+n)
			msg+=f"**{i}≽** 📂 `{n}` **[{sizeof_fmt(carp)}]\n╰➣『/cd_{i}』『/sev_{i}』『/del_{i}』** \n" 
		else:
			msg+=f"**{i}≽** `{n}`\n**╰➣『/up_{i}』『/del_{i}』[{sizeof_fmt(size)}]**\n"
		i+=1
	if str(rut).split("downloads/")[-1] != username:
		msg+="\n**Atras:** /cd_back"
	msg+="\n__𝕍𝕒𝕔𝕚𝕒𝕣 𝕖𝕝 𝕣𝕠𝕠𝕥:__ **⟦ /all ⟧**"
	return msg , final
#Obtener tamaño de la carpeta 
def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size
	
#Comando /ls mostrar directorio
@bot.on_message(filters.command("ls", prefixes="/")& filters.private)
async def ls(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	try:downlist[username]
	except:downlist[username] = []
	if exists('downloads/'+str(username)+'/'):pass
	else:
		os.makedirs('downloads/'+str(username)+'/')
	try:ROOT[username]
	except:ROOT[username] = {"actual_root":f"downloads/{str(username)}"}
	try:task[username]
	except:task[username] = False
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	msg = files_formatter(str(ROOT[username]["actual_root"]),username)
	await limite_msg(msg[0],username)
	return
	
#Comando /rn cambiat name
@bot.on_message(filters.command("rn", prefixes="/") & filters.private)
async def rename(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	h = ROOT[username]["actual_root"]
	msgh = files_formatter(str(ROOT[username]["actual_root"]),username)
	lista = message.text.split(" ")
	name1 = int(lista[1])
	name2 = lista[2]
	if not "." in name2:
		await send("_Tiene q darle o mantener el formato__\n**Ej:** `/rn 0 algo.mp4`")
		return
	actual = str(ROOT[username]["actual_root"]+"/")+msgh[1][name1]
	if not "." in actual:
		if not "." in name2: pass
		else:
			await send("**La carpeta no se puede renombrar con puntos v:**")
			return
	shutil.move(actual,h+"/"+name2)
	await send(f"**ℝ𝕖𝕟𝕠𝕞𝕓𝕣𝕒𝕕𝕠:**\n~~{msgh[1][name1]}~~\n➥ `{name2}`",reply_markup=root)
	"""msg = files_formatter(str(ROOT[username]["actual_root"]),username)
	await limite_msg(msg[0],username)"""
	return
	
#Comando /del borrar archivo y carpet
@bot.on_message(filters.regex("/del")& filters.private)
async def rm(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	list = message.text.replace("_", " ").split()[1]
	msgh = files_formatter(str(ROOT[username]["actual_root"]),username)
	size = 0
	if "-" in list:
		v1 = int(list.split("-")[-2])
		v2 = int(list.split("-")[-1])
		for i in range(v1,v2+1):
			try:
				size += Path(str(ROOT[username]["actual_root"])+"/"+msgh[1][i]).stat().st_size
				unlink(str(ROOT[username]["actual_root"])+"/"+msgh[1][i])
			except:
				size += get_folder_size(str(ROOT[username]["actual_root"])+"/"+msgh[1][i])
				shutil.rmtree(str(ROOT[username]["actual_root"])+"/"+msgh[1][i])
		await message.reply("🗑️ 𝔸𝕣𝕔𝕙𝕚𝕧𝕠𝕤 𝕤𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕒𝕕𝕠𝕤 𝕖𝕝𝕚𝕞𝕚𝕟𝕒𝕕𝕠𝕤.",reply_markup=root)
		USER[username]['D'] -= size
		await send_config()
	else:
		try:
			size += Path(str(ROOT[username]["actual_root"])+"/"+msgh[1][i]).stat().st_size
			unlink(str(ROOT[username]["actual_root"])+"/"+msgh[1][int(list)])
		except:
			size += get_folder_size(str(ROOT[username]["actual_root"])+"/"+msgh[1][i])
			shutil.rmtree(str(ROOT[username]["actual_root"])+"/"+msgh[1][int(list)])
		await message.reply("🗑️ 𝔸𝕣𝕔𝕙𝕚𝕧𝕠 𝕤𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕒𝕕𝕠 𝕖𝕝𝕚𝕞𝕚𝕟𝕒𝕕𝕠.",reply_markup=root)
		USER[username]['D'] -= size
		await send_config()
			
#Comando /all limpiar tido el root actual
@bot.on_message(filters.command("all", prefixes="/")& filters.private)
async def all(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	shutil.rmtree(str(ROOT[username]["actual_root"]))
	USER[username]['D'] = 0
	await send("**Directorio actual limpiado :D**")

#Comando de asmin /allroot
@bot.on_message(filters.command("delall", prefixes="/")& filters.private)
async def delall(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in BOSS:
		return
	else:pass
	shutil.rmtree("downloads/")
	await send("**Root de todos los usiarios limpio ;D**")
	return

#Comando /sev comprimir y split
@bot.on_message(filters.regex("/sev")& filters.private)
async def seven(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if username not in VIP:
		await send("Coamando solo para usuarios preium v:")
		return
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	if "_" in message.text:
		lista = message.text.split("_")
	else:
		lista = message.text.split(" ")
	msgh = files_formatter(str(ROOT[username]["actual_root"]),username)

	if len(lista) == 2:
		i = int(lista[1])
		j = str(msgh[1][i])
		if not "." in j:
			h = await send(f"𝕮𝖔𝖒𝖕𝖗𝖎𝖒𝖎𝖊𝖓𝖉𝖔...")
			task[username] = True
			g = str(ROOT[username]["actual_root"]+"/")+msgh[1][i]
			p = shutil.make_archive(j, format = "zip", root_dir=g)
			shutil.move(p,ROOT[username]["actual_root"])	
			await h.edit("✓ 𝕮𝖔𝖒𝖕𝖗𝖊𝖓𝖘𝖎𝖔́𝖓 𝖗𝖊𝖆𝖑𝖎𝖟𝖆𝖉𝖆 ✓",reply_markup=root)
			task[username] = False 
			return
		else:
			await message.reply("✖️ __No puede comprimir archivos(picarlos si!), solo carpetas__ ✖️")
			return

	elif len(lista) == 3:
		i = int(lista[1])
		j = str(msgh[1][i])
		t = int(lista[2])
		g = str(ROOT[username]["actual_root"]+"/")+msgh[1][i]
		h = await send(f"𝕮𝖔𝖒𝖕𝖗𝖎𝖒𝖎𝖊𝖓𝖉𝖔...")
		task[username] = True
		if not "." in j:
			p = shutil.make_archive(j, format = "zip", root_dir=g)
			await h.edit(f"𝕯𝖎𝖛𝖎𝖉𝖎𝖊𝖓𝖉𝖔 𝖊𝖓 𝖕𝖆𝖗𝖙𝖊𝖘 𝖉𝖊 {𝖙}𝕸𝖎𝕭")
			a = sevenzip(p,password=None,volume = t*1024*1024)
			os.remove(p)
			for i in a :
				shutil.move(i,ROOT[username]["actual_root"])
			await h.edit("✓ 𝕮𝖔𝖒𝖕𝖗𝖊𝖓𝖘𝖎𝖔́𝖓 𝖗𝖊𝖆𝖑𝖎𝖟𝖆𝖉𝖆 ✓",reply_markup=root)
			task[username] = False
			return
		else:
			task[username] = True
			a = sevenzip(g,password=None,volume = t*1024*1024)
			await h.edit("✓ 𝕮𝖔𝖒𝖕𝖗𝖊𝖓𝖘𝖎𝖔́𝖓 𝖗𝖊𝖆𝖑𝖎𝖟𝖆𝖉𝖆 ✓",reply_markup=root)
			task[username] = False
			return
			
######Metodos de comprension#######
async def sevenzip(fpath: Path, password: str = None, volume = None):
    filters = [{"id": FILTER_COPY}]
    fpath = Path(fpath)
    fsize = fpath.stat().st_size
    if not volume:
        volume = fsize + 1024
    ext_digits = len(str(fsize // volume + 1))
    if ext_digits < 3:
        ext_digits = 3
    with MultiVolume(
        fpath.with_name(fpath.name+".7z"), mode="wb", volume=volume, ext_digits=ext_digits
    ) as archive:
        with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
            if password:
                archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)
            archive_writer.write(fpath, fpath.name)
    files = []
    for file in archive._files:
        files.append(file.name)
    return files

async def filezip(fpath: Path, password: str = None, volume = None):
	filters = [{"id": FILTER_COPY}]
	fpath = Path(fpath)
	fsize = fpath.stat().st_size
	if not volume:
	   volume = fsize + 1024
	ext_digits = len(str(fsize // volume + 1))
	if ext_digits < 3:
	   ext_digits = 3
	with MultiVolume(
        fpath.with_name(fpath.name+"zip"), mode="wb", volume=volume, ext_digits=0) as archive:
            with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
                if password:
                	archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)
            archive_writer.write(fpath, fpath.name)
	files = []
	for file in archive._files:
		files.append(file.name)
	return files

##Comando /mkdir creacion de carpetas
@bot.on_message(filters.command("mkdir", prefixes="/")& filters.private)
async def cmd_mkdir(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	name = message.text.replace("/mkdir", "").strip()
	if "." in name or "/" in name or "*" in name:
		await send("🚫 𝕷𝖆 𝖈𝖆𝖗𝖕𝖊𝖙𝖆 𝖓𝖔 𝖕𝖚𝖊𝖉𝖊 𝖈𝖔𝖓𝖙𝖊𝖓𝖊𝖗 * / . ,")
		return
	if len(name)>13:
		await send("**Nombre de la carpeta demasiado largo XD**")
		return
	else:pass
	rut = ROOT[username]["actual_root"]
	os.mkdir(f"{rut}/{name}")
	await send("**✓ 𝕮𝖆𝖗𝖕𝖊𝖙𝖆 𝖈𝖗𝖊𝖆𝖉𝖆 𝖈𝖔𝖓 𝖊́𝖝𝖎𝖙𝖔 ✓**",reply_markup=root)
	return

#Comando /mv mover aerchivos a una carpeta
@bot.on_message(filters.command("mv", prefixes="/")& filters.private)
async def mv(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	lista = message.text.split(" ")
	msgh = files_formatter(str(ROOT[username]["actual_root"]),username)
	new_dir = int(lista[2])
	new = str(ROOT[username]["actual_root"]+"/")+msgh[1][new_dir]

	if "-" in lista[1]:
		actual = lista[1]
		v1 = int(actual.split("-")[-2])
		v2 = int(actual.split("-")[-1])
		for i in range(v1,v2+1):
			try:
				actual = str(ROOT[username]["actual_root"]+"/")+msgh[1][i]	
				shutil.move(actual,new)
				msg = send("**𝕄𝕠𝕧𝕚𝕕𝕠 𝕔𝕠𝕣𝕣𝕖𝕔𝕥𝕒𝕞𝕖𝕟𝕥𝕖**",reply_markup=root)
				await msg.edit("**𝕄𝕠𝕧𝕚𝕕𝕠 𝕔𝕠𝕣𝕣𝕖𝕔𝕥𝕒𝕞𝕖𝕟𝕥𝕖**",reply_markup=root)
			except Exception as ex:
				await bot.send_message(username,ex)
		return
	else:
		actual_dir = int(lista[1])
		try:
			actual = str(ROOT[username]["actual_root"]+"/")+msgh[1][actual_dir]
			k = actual.split("downloads/")[-1]
			t = new.split("downloads/")[-1]
			await send(f"**𝕄𝕠𝕧𝕚𝕕𝕠 𝕔𝕠𝕣𝕣𝕖𝕔𝕥𝕒𝕞𝕖𝕟𝕥𝕖**\n~~{k}~~\n➥ `{t}`",reply_markup=root)
			shutil.move(actual,new)
			return
		except Exception as ex:
			await bot.send_message(username,ex)
			return

##Comando /cd abrir carpetas
@bot.on_message(filters.regex("/cd")& filters.private)
async def cd(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	msg = message.text.replace("_", " ").split()
	j = str(ROOT[username]["actual_root"]) + "/"
	msgh = files_formatter(str(ROOT[username]["actual_root"]), username)

	if "back" in msg[1]:
	    lista = msg[1]
	else:
	    lista = int(msg[1])

	path = str(j)

	if msg[1] != "back":
	    if not "." in msgh[1][lista]:
	        cd = path + msgh[1][lista]
	        ROOT[username]["actual_root"] = str(cd)
	        msg = files_formatter(cd, username)
	        await limite_msg(msg[0], username)
	        return
	    else:
	        await send("**𝕊𝕠𝕝𝕠 𝕤𝕖 𝕡𝕦𝕖𝕕𝕖 𝕞𝕠𝕧𝕖𝕣 𝕒 𝕦𝕟𝕒 𝕔𝕒𝕣𝕡𝕖𝕥𝕒 𝕏𝔻**")
	        return
	else:
	    a = str(ROOT[username]["actual_root"])
	    b = a.split("/")[:-1]

	    if len(b) == 1:
	        await send("**𝕐𝕒 𝕖𝕤𝕥𝕒́ 𝕖𝕟 𝕤𝕦 𝕣𝕖𝕘𝕚𝕤𝕥𝕣𝕠 𝕕𝕖 𝕒𝕣𝕔𝕙𝕚𝕧𝕠𝕤 𝕡𝕣𝕚𝕟𝕔𝕚𝕡𝕒𝕝 :v**")
	        return
	    else:
	        a = str(ROOT[username]["actual_root"])
	        b = a.split("/")[:-1]
	        c = ""

	        for i in b:
	            c += i + "/"

	        c = c.rstrip(c[-1])
	        ROOT[username]["actual_root"] = c
	        msg = files_formatter(c, username)
	        await limite_msg(msg[0], username)
	        return

##Comando /tg subida a telegram##
@bot.on_message(filters.command("tg", prefixes="/") & filters.private)
async def tg(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸")
		return
	if username not in VIP:
		await message.reply("__Coamando solo para usuarios premium...__")
		return
	list = int(message.text.split(" ")[1])
	msgh = files_formatter(str(ROOT[username]["actual_root"]),username)
	try:
		path = str(ROOT[username]["actual_root"]+"/")+msgh[1][list]
		msg = await send(f"__𝕆𝕓𝕥𝕖𝕟𝕚𝕖𝕟𝕕𝕠 𝕚𝕟𝕗𝕠...__\n**{path}**")
		filename = msgh[1][list]
		start = time()
		task[username] = True
		r = await bot.send_document(username,path,file_name=filename,progress=progress_up_tg,progress_args=(filename,start,msg),thumb = "thumb.jpg")
		await msg.edit("**𝕊𝕦𝕓𝕚𝕕𝕒 𝕖𝕩𝕚𝕥𝕠𝕤𝕒 🚀**")
		task[username] = False
		return
	except Exception as ex:
		task[username] = False
		await send(f"**ERROR al intentar subir**\n{ex}")
		return
					
#descarga de archivos y enlaces
@bot.on_message(filters.media & filters.private)
async def down_media(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if username not in USER:
		return
	else:pass
	if task[username] == True:
		await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸",quote=True)
		return
	if USER[username]['D'] >= 5000000000:
		await send("𝕊𝕠𝕣𝕣𝕪, 𝖓𝖔 𝖕𝖚𝖉𝖊 𝖘𝖊𝖌𝖚𝖎𝖗 𝖌𝖚𝖆𝖗𝖉𝖆𝖓𝖉𝖔 𝖊𝖓 𝖊𝖑 𝖗𝖔𝖔𝖙...𝖕𝖆𝖗𝖆 𝖈𝖔𝖓𝖙𝖎𝖓𝖚𝖆𝖗 𝖑𝖎𝖒𝖕𝖎𝖊: \n**⟨⟨/all⟩⟩**",quote=True)
		return
	downlist[username].append(message)
	await send("↪️ **ARCHIVO CARGADO** ⤵️",reply_markup=DOWN,quote=True)
	
#Descsrgsr links directos pos v:
@bot.on_message((filters.regex("https://") | filters.regex("http://")) & filters.private)
async def down_link(client: Client, message: Message):
    print(message)
    try:
        username = message.from_user.username
    except:
        print("Username no valido")
        return
    send = message.reply
    user_id = message.from_user.id
    try:await get_messages()
    except:await send_config()
    if username not in USER:
        return
    else:pass
    if task[username] == True:
    	await message.reply("𝕋𝕚𝕖𝕟𝕖 𝕦𝕟 𝕡𝕣𝕠𝕔𝕖𝕤𝕠 𝕖𝕟 𝕔𝕦𝕣𝕤𝕠, 𝕡𝕠𝕣 𝕗𝕒𝕧𝕠𝕣 𝕖𝕤𝕡𝕖𝕣𝕖 🤸",quote=True)
    	return
    if USER[username]['D'] >= 5000000000:
    	await send("𝕊𝕠𝕣𝕣𝕪, 𝖓𝖔 𝖕𝖚𝖉𝖊 𝖘𝖊𝖌𝖚𝖎𝖗 𝖌𝖚𝖆𝖗𝖉𝖆𝖓𝖉𝖔 𝖊𝖓 𝖊𝖑 𝖗𝖔𝖔𝖙...𝖕𝖆𝖗𝖆 𝖈𝖔𝖓𝖙𝖎𝖓𝖚𝖆𝖗 𝖑𝖎𝖒𝖕𝖎𝖊: \n**⟨⟨/all⟩⟩**",quote=True)
    	return
    j = str(ROOT[username]["actual_root"])+"/"
    url = message.text
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            try:
                filename = unquote_plus(url.split("/")[-1])
            except:
                filename = r.content_disposition.filename
            fsize = int(r.headers.get("Content-Length"))
            #total_up[username]['P'] += fsize
            msg = await send("__𝕆𝕓𝕥𝕖𝕟𝕚𝕖𝕟𝕕𝕠 𝕀𝕟𝕗𝕠𝕣𝕞𝕒𝕔𝕚𝕠́𝕟...__")
            task[username] = True
            #procesos += 1
            await client.send_message(Channel_Id, f'@{username} Envio un #link :\nUrl: {url}\n**Size:** `{sizeof_fmt(fsize)}`')
            f = open(f"{j}{filename}", "wb")
            newchunk = 0
            start = time()
            async for chunk in r.content.iter_chunked(1024*1024):
                newchunk += len(chunk)
                await progress_down_tg(newchunk, fsize, filename, start, msg)
                f.write(chunk)
            f.close()
            file = f"{j}{filename}"
            task[username] = False
            await msg.edit("✓ 𝕯𝖊𝖘𝖈𝖆𝖗𝖌𝖆 𝖊𝖝𝖎𝖙𝖔𝖘𝖆 ✓")
            sleep(2)
            await msg.edit("**📥 𝔸𝕣𝕔𝕙𝕚𝕧𝕠 𝔾𝕦𝕒𝕣𝕕𝕒𝕕𝕠 🤖**",quote=True,reply_markup=root)
            return
           

##MENSAGED DE PROGRESO ⬆⬇
def update_progress_up(inte,max):
	percentage = inte / max
	percentage *= 100
	percentage = round(percentage)
	hashes = int(percentage / 6)
	spaces = 18 - hashes
	progress_bar = "●" * hashes + "○" * spaces
	percentage_pos = int(hashes / 1)
	percentage_string = str(percentage) + "%"
	
	progress_bar = "**[" + progress_bar[:percentage_pos] + percentage_string + progress_bar[percentage_pos + len(percentage_string):] +"]**"
	return(progress_bar)
###
def update_progress_down(inte,max):
	percentage = inte / max
	percentage *= 100
	percentage = round(percentage)
	hashes = int(percentage / 6)
	spaces = 18 - hashes
	progress_bar = "■" * hashes + "□" * spaces
	percentage_pos = int(hashes / 1)
	percentage_string = str(percentage) + "%"
	
	progress_bar = "**[" + progress_bar[:percentage_pos] + percentage_string + progress_bar[percentage_pos + len(percentage_string):] +"]**"
	return(progress_bar)

seg=0
#Subida a telegram xel cmd /tg
async def progress_up_tg(chunk,filesize,filename,start,message):
		global seg
		now = time()
		diff = now - start
		mbs = chunk / diff
		filename = filename[:13]+"•••"+filename.split(".")[-1]
		msg = f"-==================-\n|**SUBIDA A TELEGRAM**|\n-==================-\n\n"
		try:
			msg+=update_progress_up(chunk,filesize)+ " " + sizeof_fmt(mbs)+"/s\n\n"
		except:pass
		msg+= f"🏷️**•ℕ𝕒𝕞𝕖:** `{filename}`\n📤**•𝕌𝕡𝕝𝕠𝕒𝕕:** `{sizeof_fmt(chunk)}/{sizeof_fmt(filesize)}`"
		"""msg+= f"▶️ 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐:: {sizeof_fmt(chunk)} of {sizeof_fmt(filesize)}\n\n"""	
		if seg != localtime().tm_sec:
			try: await message.edit(msg)
			except:pass
		seg = localtime().tm_sec

##Descsrga de archivos links
async def progress_down_tg(chunk,total,filename,start,message):
	global seg
	now = time()
	diff = now - start
	mbs = chunk / diff
	filename = filename[:13]+"•••"+filename.split(".")[-1]
	msg = "-======================-\n|DESCARGA EN PROGRESO|\n-======================-\n\n"
	try:
		msg+= update_progress_down(chunk,total)+"\n"
	except: pass	
	msg+= f"☄️**•𝕊𝕡𝕖𝕖𝕕:** `{sizeof_fmt(mbs)}/s`\n🏷️**•ℕ𝕒𝕞𝕖:** `{filename}`\n📤**•𝔻𝕠𝕨𝕟:** `{sizeof_fmt(chunk)}/{sizeof_fmt(total)}`"
	if seg != localtime().tm_sec:
		try: await message.edit(msg)
		except:pass
	seg = localtime().tm_sec
#Subida a la nube

#ConvertBytes=>>
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)
    
#Limite de mensajes a enviar xelbot
async def limite_msg(text,username):
	lim_ch = 1500
	text = text.splitlines() 
	msg = ''
	msg_ult = '' 
	c = 0
	for l in text:
		if len(msg +"\n" + l) > lim_ch:		
			msg_ult = msg
			await bot.send_message(username,msg)	
			msg = ''
		if msg == '':	
			msg+= l
		else:		
			msg+= "\n" +l	
		c += 1
		if len(text) == c and msg_ult != msg:
			await bot.send_message(username,msg)

print("Iniciado!")
bot.run()