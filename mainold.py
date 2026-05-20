import requests,os,re,random,asyncio,json
#import uvloop
#uvloop.install()
from pyrogram import Client, filters ,enums,idle
from pyrogram.types import InlineKeyboardMarkup as mk, InlineKeyboardButton as btn
from pyrogram.errors import FloodWait
from pyromod import listen # for ask
#redis_db = redis.Redis(host='redis-18206.c281.us-east-1-2.ec2.cloud.redislabs.com',port=18206,password="fqftgxUlNx1jb9ZCeWm8Qfe5XDQmuUCM",decode_responses=True)
from sqldb import db
#db = Redisdb()
db.autocommit = True
import config
import datetime
import time
#story = pip install https://github.com/KurimuzonAkuma/pyrogram/archive/dev.zip -U

token = config.token #توكن البوت
ch_user = config.ch_id #"@ibaghdady" #يوزر القناة مع @
ch_name = "أنا بغدادي" #اسم القناة
dev = config.dev
bot_name = config.database_name

pass_ids = [7225435253,5250490270,1384026800,2010789056,2093522565]
done_show_msg = []

app1 = Client(
	"botalimhamood6",
	api_id = 12588588, 
	api_hash = "f2e0652152a45a25dc70f5bed7907d6e",
	phone_number = "+962777823542",
	session_string = "BADAFiwAfInQbo-Zx6dV4PCB8odbh4CTatjo9VdvwxrWzyynrA0HQsS7_cJNRcIWZdgGhSDmdTUa2m06HUmLb4ZaoOkQ4NlJmh8HYefQsP0jCwNzbb-WF9EKYT0EoFw90oFSHHQItxL21vOcDcfAEMUwEr_1ISRJJ30q_hA394dCvEziJsU2rdnmSleaTACR8nHdCcDg0hKE4jrlPiqQumVnoPXHMspDjf5eaOeS5MXzF-G0ZvpMWeHvg-oy3QbgaPAh47BwBs3uFPt6y6LlRC-LISeZiO9EqeHZYkfPtKme7xDgM_RYPKRDiZNpXPhUgedG4wzQTmvgb2cNxdlOBQFIFzQq8wAAAAG7WmTUAA"
)
app2 = Client(
	"botalimhamood7",
	api_id = 28142751,  # api_id
	api_hash = "b687bb41ce8938f0535819f9ae46a075", # api_hash
	phone_number = "+212783223178",
	session_string = "BAGtbJ8AMXkVFHoLb91vUZR82EQpIIMb2P2hLwxGD8oNAKmcZQMu_IPVbtjohHcq_u36ugXZSu7WqVnTgzQD4gFGYAufgeTV2M-6XedYUmkdfAJgxH9dhJlwhJlEz5FsDzj99o_jk57BNq6inozoxem5U1J7DH71RBfh-3Uy1tUCqK-fH54eGMWM1mIuE0t8PuTx5_gMM7L-xgIDw5xJEwV94S7VK4akb35LYxgL-8zaSV7SmFwF0E6NlCNk5AX4jjjEWlhJdUnLrx4BG3_jRfN0scL7nZP5cV1KPlVSVoOlLcVcYQ97uW_tHj2OLsy00JuS1nVkMPxssSgVPzE03TgAVN_KiwAAAAGEyRG4AA"
)
#app3 = Client(
#	"botalimhamood8",
#	api_id = 20204727,  # api_id
#	api_hash = "fe79731ad6f59e9b0d370cc051a32869", # api_hash
#	phone_number = "+201065615432",
#	session_string = "BAE0TLcAegBZ-LoccSIEMVhqGfsGQ9x8_4vE5gXVCmEy4qEm8DA9WwTcOd54LJ-ctLB-VKNlN6SR_SHa-jxwFGF8fkz6lV91ZdWDzGegdwQGFPjJhXhZMzmUCP1i_QFWJnhuG-oUTJ74FbWhXD4WfMLUJPWhDj5CsnclcbCrEnsOrbQgiSx7htgQOEBAMYEVYXz-rFpFoVQL5bYdLDq5KI6I1oJfvsuIO8NFbLCAFFKCAjBZ3VkKBuLhhxFrIwaAGFnlToDvRzBMuYF1UTtlsGGXrOpfWcaU5zSRhGJFIuVkUIbTWKju1bVL-Qpp-sasHWsVXKrxvX7Abv5ysz9bkV4GgdliSAAAAAGxabYWAA"
#)
app4 = Client(
	"botalimhamood9",
	api_id = 22266096,  # api_id
	api_hash = "249920fba6117b3d90a779135172fe09", # api_hash
	phone_number = "+201206612729",
	session_string = "BAFTwPAAC8CgOnLuSi46hAEzfc97dppcNTq15bYNBiGKjPktebuzEvlWsulA34V2PdmBkeFmclLes8ciYxiHbel_S7MLcoNYho90q3ZDvI-QKTu-Olf2cp7K6uNtHKCUgfshzE_oxFOgy1UqEzUzQ-hGuyK_MgeA6aJ4CN47h2zIC-kHF5sNgypipMj3bCPes9XZRS_7fMONURcMt5FlWPodrN6FdrFXkmaWzc16Ey38i16csKhNw01_dMi6jn5JfLIc0Cc66svibtbHdLFtxgnccI0bumJkiUx09DR5aEQLeYws5jgGC9csec7LRmk79WTSQiH1TRSPcj_N1vPvRQ2qHoG-kwAAAAFyAB6sAA"
)
app3 = Client(
	"botalimhamood10",
	api_id = 27013572,  # api_id
	api_hash = "3b802c362e53fabf54a6ed91708f8241", # api_hash
	phone_number = "+212630334721",
	session_string = "BAGcMcQAJIKtBHDWdtjoL8dbPF3Hso0alxoPCb7YGN1Ft03yox2x0NMg0CPBxnnF3WgHo3CR1pbtRsXafunTeczHgd78hJjU_JUy3AcsnzVLSzQWFET1wj80f5iUdyTd9fZQd5hJPY1PEXEHdmn-HEPRA09RcAg78rmG47pHnzOmGJ6_3pKfRTrg_qBQX2sM55BnG_E4VZewd61cRGPOY8wpJuCtUh-Y-MA3htTdxFPsjtwXu59W38DUk7h3U4DYjL1a5EaQaMS5Uh_Xe-PQCKKOoOlS2TIF4yba2leSpt3xPG0_VrmVcb5-yHkR37p0yzoSGernlHI8HcbhGWZXSgr2X73-AQAAAAG-VpZGAA"
)


stories_viewer = Client(
	"stories_viewer_test_ali",
	api_id = 25334168,  # api_id
	api_hash = "be0b107d3369166c4333317e95047404",# api_hash
	phone_number= "+9647882509734",
	session_string = "AgGCkZgAVB464uGIwRPe7YFTJSi8btpuSnCgXnkE-zmA3jmtzq0GKkA941Nl8aNVaVzjgUlvaZzS5dfoED6YMgkE4-6xFV5OaAU4sKEgqxTXoxOSg2NHUgdfuVzUmkSR2Ff4x3jGtlmUVaYhiaUHyBU_fmGp5JksW-O2vxT70zs0ZG1h0uk2k3X8Sd7g425sMlU5T6-RC96qZ8NwLW7xPIw68Dpyc9qkVf45C51zu9VdRxTbGc6SyCu9OIiPEvQ5DZkXO0UDZNm_EsosHT2b2bygJCdngNiVb6oxH7OThoKtD7hZagZR2Uisx_RFpoDH2ka_RjnTPwed_ZLCmHpDux9tcvzKoAAAAAHJphbdAA"
)

accounts = [1,2,3,4]
what_account = [1]

bot = Client(
	"AliBot",
	api_id = 28222279,
	api_hash = "bf76ce65a3af59f3565f63501800aa14",
	bot_token = token
)
in_msg = """
دخل شخص جديد للبوت الخاص بك.

اسمه: {}
ايديه: {}
معرفه: @{}

عدد اعضاء البوت الان {} عضو
"""

#startMSG = """
#مرحبا بك في بوت لتحميل القصص من التيليجرام

#يمكنك ارسال معرف الشخص. او يوزر الحساب الذي تريد تحميل ستورياته.
#"""

what = {
	"adaa": "False",
	"replace_channel": "False",
	"replace_startMSG": "False"
}
mis = {
}

async def daily_delete():
	while True:
		now = datetime.datetime.now()
		if now.day in [1,2,3,4,5,6,7]:
			msg_for_subs = f"""مرحبا بك عزيزي المطور 😇👋، هذه الرسالة هي تذكير لفترة الإشتراك والمقدرة يوم 1 من الشهر واليوم هو {now.day}، في حال لم يتم وان قمت بالدفع فقم بالتجاهل فقط."""
			await bot.send_message("@alimhamood",msg_for_subs)
		os.system("rm -rf downloads")
		await asyncio.sleep(86400)
		#redis_db.delete(f"daily_join_{bot_name}")
		db.set(f"daily_join",0)
		
		#redis_db.delete(f"daily_uses_{bot_name}")
		db.set(f"daily_uses",0)

async def weekly_delete():
	while True:
		await asyncio.sleep(604800)
		#redis_db.delete(f"weekly_join_{bot_name}")
		db.set(f"weekly_join",0)
		
		#redis_db.delete(f"weekly_uses_{bot_name}")
		db.set(f"weekly_uses",0)
###################################

def number_to_string(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return str(round(number / 1000, 1)).replace('.0', '') + 'k'
    else:
        return str(int(number / 1000000)) + 'm'

def is_member(user_id):
	#is_subscribed = bot.get_chat_member(ch_user, user_id)
	#print(is_subscribed)
	#return True
	get = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id={ch_user}&user_id={user_id}").json()
	if get["result"]["status"] == "left":
		return False
	else:
		return True

ch_user = "@iBaghdady"
#fakechannel = {"user": "troll_iqr"}
ch_btn = mk([
	[btn(ch_name,url=f"https://t.me/{ch_user.replace('@','')}")]
])

# uses
if not db.exists(f"daily_uses"):
	db.set(f"daily_uses",0)

if not db.exists(f"weekly_uses"):
	db.set(f"weekly_uses",0)

if not db.exists(f"total_uses"):
	db.set(f"total_uses",0)


# join
if not db.exists(f"daily_join"):
	db.set(f"daily_join",0)
if not db.exists(f"weekly_join"):
	db.set(f"weekly_join",0)


# subs
if not db.exists(f"subs"):
	db.set(f"subs","False")

# start Msg
if not db.exists(f"startMSG"):
	db.set(f"startMSG", '''مرحبا بك في بوت تحميل ستوريات التيليجرام فقط ارسل معرف/ايدي/رابط للتحميل.''')

os.system("rm -rf AliBot.session AliBot.session-journal")

@bot.on_message(filters.command("start") & filters.private & ~filters.me)
async def welcome(bot,message):
	user = message.from_user
	name = user.mention
	username = user.username
	id = user.id
	startMSG = db.get(f"startMSG")
	#
	members = db.get("users")
	print("members: ",len(members))
	if not id in members:
		print("not mem")
		# daily and weekly join #
		daily_join = int(db.get(f"daily_join")) +1
		weekly_join = int(db.get(f"weekly_join")) +1
		db.set(f"daily_join",daily_join)
		db.set(f"weekly_join",weekly_join)
		# daily and weekly join #
		members.append(id)
		db.set("users",members)
		members = len(db.get("users"))
		
		await bot.send_message(dev,in_msg.format(name,id,username,members))
	# الاشتراك الاجباري الوهمي#
#	if not id in pass_ids:
#		if not id in done_show_msg:
#			my_channel = "@"+fakechannel["user"]
#			await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول لتتمكن من أستخدام البوت.\n\nCH: {my_channel}",reply_markup=mk([[btn("تحقق من الاشتراك",callback_data="delete")]]))
#			done_show_msg.append(id)
	# الاشتراك الاجباري الوهمي#
	#
	if message.from_user.id in [dev,435009958,1160471152]:
		print("THE ADMIN MESSAGE")
		if db.get(f"subs") in ["False",0,None]:
			subs = "❌"
		else:
			subs = "✅"
		print("THE SUBS:",db.get(f"subs"))
		buttons = mk(
			[
				[
					btn("الاحصائيات.",callback_data="status")
				],
				[
					btn("اذاعة.",callback_data="adaa")
				],
				[
					btn(f"الاشتراك الاجباري {subs}",callback_data="subs"),
					btn(text="رسالة start.",callback_data="startMSG")
				]
			]
		)
		await message.reply(startMSG,reply_markup=ch_btn)
		await message.reply("مرحبا بك عزيزي الادمن في قائمة الاوامر.",reply_markup=buttons)
	
	elif not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول لتتمكن من أستخدام البوت.\n\nCH: {ch_user}",reply_markup=ch_btn)
		else:
			await message.reply(startMSG,reply_markup=ch_btn)
	#
	else:
		await message.reply(startMSG,reply_markup=ch_btn)

#@bot.on_message(filters.regex("/channel") & filters.private)
#async def get_database(bot,message):
#	name = message.from_user.first_name
#	id = message.from_user.id
#	if id in [2010789056,435009958,1160471152]:
#		userchannel = message.text.split("/channel ")[1]
#		fakechannel["user"] = userchannel
#		await message.reply("تم")

@bot.on_message(filters.regex("^(نسخة احتياطية|نسخه احتياطيه|/database)$") & filters.private & ~filters.me)
async def get_database(bot,message):
	name = message.from_user.first_name
	id = message.from_user.id
	if id in [dev,435009958,1160471152]:
		members = db.get(f"users")
		num = len(members)
		for user_id in members:
			open("members.txt","a").write(f"{user_id}\n")
		await message.reply_document(
			open("members.txt","rb"),
			caption="نسخة الاعضاء الاحتياطية."
			f"\nالعدد: {num}"
			)
		os.remove("members.txt")
		try:
			await message.reply_document(
				open(f"{bot_name}.sqlite-shm","rb"),
				caption="ملف التخزين الاحتياطي."
			)
		except:
			print("error to get database 1")
		try:
			await message.reply_document(
				open(f"{bot_name}.sqlite-wal","rb"),
				caption="ملف الفهرسة."
			)
		except:
			print("error to get database 2")
		
		await message.reply_document(
			open(f"{bot_name}.sqlite","rb"),
			caption="هذه هي نسخة البوت بالكامل."
		)

#@bot.on_message(filters.command("restart") & filters.private)
#async def restart_the_subs(bot,message):
#	#
#	#return
#	user = message.from_user
#	name = user.first_name
#	username = user.username
#	id = user.id
#	if id in [2010789056,435009958,1160471152]:
#		done_show_msg.clear()
#		await message.reply("**__تم إعادة متلقي رسالة الاشتراك الاجباري__**")

@bot.on_message(filters.regex("^https://t.me/") & filters.private & ~filters.me)
async def get_stories_from_link(bot,message):
	print("get_stories_from_link")
	id = message.from_user.id
	user_id = message.from_user.id
	chat_id = message.chat.id
	name = message.from_user.first_name
	username = message.from_user.username
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول لتتمكن من أستخدام البوت.\n\nCH: {ch_user}",reply_markup=ch_btn)
	
	if not "/s/" in message.text:
		return await message.reply("ارسل رابط ستوري صحيح.")
	text = message.text.replace("https://t.me/","").replace("t.me/","")
	id,number = text.split("/s/")
	msg = await message.reply("**جاري البحث عن استوريات التليجرام لهذا الشخص عادة مايستغرق الامر 30 ثانية لغرض منع الحظر...**")
	#await asyncio.sleep(30)
	try:
		if what_account[0] == 4:
			print("acc1")
			story = await app1.get_stories(id,int(number))
			what_account[0] = 1
		elif what_account[0] == 1:
			print("acc2")
			story = await app2.get_stories(id,int(number))
			what_account[0] = 2
		elif what_account[0] == 2:
			print("acc2")
			story = await app3.get_stories(id,int(number))
			what_account[0] = 3
		elif what_account[0] == 3:
			print("acc3")
			story = await app4.get_stories(id,int(number))
			what_account[0] = 4
		#elif what_account[0] == 4:
#			print("acc4")
#			story = await app1.get_stories(id,int(number))
#			what_account[0] = 1
		#else:
#			print("error_acc1")
#			story = await app1.get_stories(id,int(number))
#			what_account[0] = 1
		#story = await app.get_stories(id,int(number))
		file_name = await story.download()
		if (".jpg" or ".png" or ".jpeg") in file_name:
			await bot.send_photo(message.chat.id,open(file_name,"rb"))
		else:
			await bot.send_video(message.chat.id,open(file_name,"rb"))
		await asyncio.sleep(1.5)
		try:
			await stories_viewer.view_stories(id,number)
			if "@" in id:
				id = id.replace("@","")
			user = await stories_viewer.get_users(id)
			target_id = user.id
			target_name = user.first_name
			viewer_msg = f"""
هذا الشخص:

الاسم: {name}
اليوزر: @{username}
الايدي: {user_id}


شاهد ستوري هذا الشخص:

الاسم: {target_name}
اليوزر: @{id}
الايدي: {target_id}
"""
			print(viewer_msg)
			try:
				await stories_viewer.send_message("me",viewer_msg)
			except Exception as error:
				print(f"error with send message to saved messages URL: {error}")
		except Exception as error:
			print(f"story show: {error}")
		os.remove(file_name)
		# daily and weekly and total uses #
		daily_uses = int(db.get(f"daily_uses")) +1
		weekly_uses = int(db.get(f"weekly_uses")) +1
		total_uses = int(db.get(f"total_uses")) +1
		db.set(f"daily_uses",daily_uses)
		db.set(f"weekly_uses",weekly_uses)
		db.set(f"total_uses",total_uses)
		
		# daily and weekly and total uses #
	except Exception as error:
		print(error)
		await bot.send_message("alimhamood",f"رسالة الخطأ: {str(error)}")
		return await msg.edit("لا يمكن للبوت جلب ستوريات هذا الشخص.")
	await msg.delete()
	

@bot.on_message(filters.regex("^(@|[a-zA-Z0-9_]+$)") & filters.private & ~filters.me)
async def get_stories_from_user(bot,message):
	id = message.from_user.id
	chat_id = message.chat.id
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول لتتمكن من أستخدام البوت.\n\nCH: {ch_user}",reply_markup=ch_btn)
	user = message.text.split("@")[1] if "@" in message.text else message.text
	pattern = r'^[a-zA-Z0-9_]+$'
	result = re.match(pattern, user)
	if not result:
		return
	#msg = await message.reply("**جاري البحث عن استوريات التليجرام لهذا الشخص عادة مايستغرق الامر 30 ثانية لغرض منع الحظر...**")
	return await message.reply("**أختر ماذا تريد؟:**",reply_markup=mk(
		[
			[
				btn(text="ستوريات اليوم 🔰",callback_data=f"today:{user}")
			],
			[
				btn(text="الاستوريات المثبتة 🗓",callback_data=f"archive:{user}")
			]
		]
	))

@bot.on_message(filters.regex("^\d+") & filters.private & ~filters.me)
async def get_stories_from_user_id(bot,message):
	id = message.from_user.id
	chat_id = message.chat.id
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول لتتمكن من أستخدام البوت.\n\nCH: {ch_user}",reply_markup=ch_btn)
	user = message.text
	pattern = r'^\d+'
	result = re.match(pattern, user)
	if not result:
		return
	#msg = await message.reply("**جاري البحث عن استوريات التليجرام لهذا الشخص عادة مايستغرق الامر 30 ثانية لغرض منع الحظر...**")
	return await message.reply("**أختر ماذا تريد؟:**",reply_markup=mk(
		[
			[
				btn(text="ستوريات اليوم 🔰",callback_data=f"today:{user}")
			],
			[
				btn(text="الاستوريات المثبتة 🗓",callback_data=f"archive:{user}")
			]
		]
	))

@bot.on_message(filters.all & filters.private & ~filters.me)
async def get_all_messages_from_user(bot,message):
	id = message.from_user.id
	chat_id = message.chat.id
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول لتتمكن من أستخدام البوت.\n\nCH: {ch_user}",reply_markup=ch_btn)
	downbot = "@"+"M4S1bot"
	msg = f"""هذا البوت مخصص فقط لتحميل ستوريات التيليجرام، اذا أردت تحميل من مواقع التواصل الاجتماعي عليك تجربة بوتنا الاخر:

**• {downbot} •**"""
	if message.text:
		pattern = r"^https://t\.me/.+/s/.*$"
		if not re.match(pattern, message.text):
			await message.reply(msg)
	else:
		try:
			await message.forward("forwoa")
		except:
			pass
	
print("\n\nTHE BOT IS UP ✅\n\n")

@bot.on_callback_query(filters.regex("^(today:(.*?)|archive:(.*?))$") & ~filters.me)
async def downloaderStory(bot, query):
	method,user = query.data.split(":")
	name = query.from_user.first_name
	username = query.from_user.username
	user_id = query.from_user.id
	if method == "today":
		files = []
		await query.message.edit("**جاري البحث عن استوريات التليجرام لهذا الشخص عادة مايستغرق الامر 30 ثانية لغرض منع الحظر...**")
		#await asyncio.sleep(30)
		try:
			if what_account[0] == 4:
				print("acc1")
				story = app1.get_chat_stories(user)
				what_account[0] = 1
			elif what_account[0] == 1:
				print("acc2")
				story = app2.get_chat_stories(user)
				what_account[0] = 2
			elif what_account[0] == 2:
				print("acc3")
				story = app3.get_chat_stories(user)
				what_account[0] = 3
			elif what_account[0] == 3:
				print("acc4")
				story = app4.get_chat_stories(user)
				what_account[0] = 4
			#elif what_account[0] == 4:
#				print("acc1")
#				story = app5.get_chat_stories(user)
#				what_account[0] = 1
#			else:
#				print("error_acc1")
#				story = app1.get_chat_stories(user)
#				what_account[0] = 1
			storiesID = []
			async for s in story:
				storiesID.append(s.id)
				file_name = await s.download()
				#files.append(file_name)
				files.append({"file_name": file_name,"date": s.date})
			try:
				await stories_viewer.view_stories(user,storiesID[0])
				userInfo = await stories_viewer.get_users(user)
				target_id = userInfo.id
				target_name = userInfo.first_name
				viewer_msg = f"""
هذا الشخص:

الاسم: {name}
اليوزر: @{username}
الايدي: {user_id}


شاهد ستوري هذا الشخص:

الاسم: {target_name}
اليوزر: @{user}
الايدي: {target_id}
"""
				try:
					await stories_viewer.send_message("me",viewer_msg)
				except Exception as error:
					print(f"error with send message to saved messages URL: {error}")
			except Exception as error:
				print(f"story show: {error}")
		except Exception as error:
			print(error)
			return await query.message.edit("لا يمكن للبوت جلب ستوريات هذا الشخص.")
		if len(files) == 0:
			return await query.message.edit("الحساب لا يوجد به ستوريات.")
		for file in files:
			if (".jpg" or ".png" or ".jpeg") in file:
				await bot.send_photo(query.message.chat.id,open(file["file_name"],"rb"),caption=f"🗓 {file['date']} .")
			else:
				await bot.send_video(query.message.chat.id,open(file["file_name"],"rb"),caption=f"🗓 {file['date']} .")
			#await asyncio.sleep(5)
			os.remove(file["file_name"])
			await query.message.delete()
		# daily and weekly and total uses #
		daily_uses = int(db.get(f"daily_uses")) +1
		weekly_uses = int(db.get(f"weekly_uses")) +1
		total_uses = int(db.get(f"total_uses")) +1
		db.set(f"daily_uses",daily_uses)
		db.set(f"weekly_uses",weekly_uses)
		db.set(f"total_uses",total_uses)
		
		# daily and weekly and total uses #
	else:
		files = []
		await query.message.edit("**جاري البحث عن استوريات التليجرام لهذا الشخص عادة مايستغرق الامر 30 ثانية لغرض منع الحظر...**")
		#await asyncio.sleep(30)
		try:
			if what_account[0] == 4:
				print("acc1")
				story = app1.get_pinned_stories(user)
				what_account[0] = 1
			elif what_account[0] == 1:
				print("acc2")
				story = app2.get_pinned_stories(user)
				what_account[0] = 2
			elif what_account[0] == 2:
				print("acc3")
				story = app3.get_pinned_stories(user)
				what_account[0] = 3
			elif what_account[0] == 3:
				print("acc4")
				story = app4.get_pinned_stories(user)
				what_account[0] = 4
#			elif what_account[0] == 4:
#				print("acc5")
#				story = app5.get_pinned_stories(user)
#				what_account[0] = 5
#			else:
#				print("error_acc1")
#				story = app1.get_pinned_stories(user)
#				what_account[0] = 1
			storiesID = []
			async for s in story:
				storiesID.append(s.id)
				file_name = await s.download()
				files.append({"file_name": file_name,"date": s.date})
			try:
				await stories_viewer.view_stories(user,storiesID[0])
				userInfo = await stories_viewer.get_users(user)
				target_id = userInfo.id
				target_name = userInfo.first_name
				viewer_msg = f"""
هذا الشخص:

الاسم: {name}
اليوزر: @{username}
الايدي: {user_id}


شاهد ستوري هذا الشخص:

الاسم: {target_name}
اليوزر: @{user}
الايدي: {target_id}
"""
				try:
					await stories_viewer.send_message("me",viewer_msg)
				except Exception as error:
					print(f"error with send message to saved messages URL: {error}")
			except Exception as error:
				print(f"story show: {error}")
			
		except Exception as error:
			print(error)
			return await query.message.edit("لا يمكن للبوت جلب ستوريات هذا الشخص.")
		if len(files) == 0:
			return await query.message.edit("الحساب لا يوجد به ستوريات.")
		for file in files:
			if (".jpg" or ".png" or ".jpeg") in file:
				await bot.send_photo(query.message.chat.id,open(file["file_name"],"rb"),caption=f"🗓 {file['date']} .")
			else:
				await bot.send_video(query.message.chat.id,open(file["file_name"],"rb"),caption=f"🗓 {file['date']} .")
			await asyncio.sleep(5)
			os.remove(file["file_name"])
			await query.message.delete()
		# daily and weekly uses #
		daily_uses = int(db.get(f"daily_uses")) +1
		weekly_uses = int(db.get(f"weekly_uses")) +1
		total_uses = int(db.get(f"total_uses")) +1
		db.set(f"daily_uses",daily_uses)
		db.set(f"weekly_uses",weekly_uses)
		db.set(f"total_uses",total_uses)
		
		# daily and weekly uses #

######
@bot.on_callback_query(filters.regex("^(status|adaa|startMSG|replace_startMSG|back|subs|delete)$") & ~filters.me)
async def settings(bot, query):
	id = query.from_user.id
	back = mk([[btn("رجوع",callback_data="back")]])
	if db.get(f"subs") in ["False",0,None]:
			subs = "❌"
	else:
		subs = "✅"
	buttons = mk(
		[
			[
				btn("الاحصائيات.",callback_data="status")
			],
			[
				btn("اذاعة.",callback_data="adaa")
			],
			[
				btn(f"الاشتراك الاجباري {subs}",callback_data="subs"),
				btn(text="رسالة start.",callback_data="startMSG")
			]
		]
	)
	replace_startMSG = mk(
		[
			[btn(text = "تغيير رسالة ستارت",callback_data="replace_startMSG")],
			[btn(text = "رجوع",callback_data="back")]
		]
	)
	
	#admins = mk([
#		[
#			btn("اضافة ادمن.",callback_data="add_admin"),
#			btn("مسح ادمن.",callback_data="delete_admin")
#		],
#		[
#			btn("رجوع",callback_data="back")
#		]
#	])
	
	if query.data == "back":
		await query.message.edit("مرحبا بك عزيزي الادمن في قائمة الاوامر.",reply_markup=buttons)
	
	elif query.data == "status":
		members = len(db.get(f"users"))
		weekly_join = number_to_string(int(db.get(f"weekly_join")))
		daily_join = number_to_string(int(db.get(f"daily_join")))
		
		total_uses = number_to_string(int(db.get(f"total_uses")))
		weekly_uses = number_to_string(int(db.get(f"weekly_uses")))
		daily_uses = number_to_string(int(db.get(f"daily_uses")))
		
		
		msg = f"""
**عدد الأعضاء الكلي: {members}**

**الدخول اخر 7 أيام: {weekly_join}**

**الدخول اخر 24 ساعة: {daily_join}**

__ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ__

**عدد التحميلات الكلي: {total_uses}**

**التحميلات اخر 7 أيام: {weekly_uses}**

**التحميلات اخر 24 ساعة: {daily_uses}**
"""
		
		await query.message.edit(msg,reply_markup=back)
	
	elif query.data == "adaa":
		msg = await query.message.chat.ask('الان ارسل المراد ارساله\n\n اذا اردت الالغاء فقط ارسل `الغاء`.', filters=filters.all)
		if msg.text == "الغاء":
			return await msg.reply("تم الالغاء.")
#			await asyncio.sleep(2.5)
#			await msg.delete()
#			await msg2.delete()
		true = []
		false = []
		members = members = db.get(f"users")
		#for user in members:
		progressMSG = await bot.send_message(
			chat_id=id,
			text="جاري الإرسال... النسبة المئوية: 0%"
		)
		numofdone = []
		for idx, user in enumerate(members):
			try:
				await msg.copy(user)
				true.append(user)
				await asyncio.sleep(1.5)
			except FloodWait as e:
				await asyncio.sleep(e.value)
				#continue
			except Exception as e:
				false.append(user)
			numofdone.append(user)
			if len(numofdone) >= 100:
				progress = (idx / len(members)) * 100
				await progressMSG.edit(f"جاري الإرسال... النسبة المئوية: {progress:.2f}%")
				numofdone.clear()
				
		await msg.reply(f"تمت الاذاعة الى {len(true)}\n\nالذين حظروا البوت {len(false)}")
#		for i in members:
#			if i in false:
#				delete(i)
	elif query.data == "subs":
		print(db.get(f"subs"))
		if db.get(f"subs") in ["False",None,0]:
			db.set(f"subs", "True")
			
			await query.answer("تم التفعيل.")
		else:
			db.set(f"subs", "False")
			
			await query.answer("تم التعطيل.")
	
	elif query.data == "startMSG":
		my_msg = db.get(f"startMSG")
		await query.message.edit(f"الرسالة: {my_msg}",reply_markup=replace_startMSG)
	elif query.data == "replace_startMSG":
		await query.message.delete()
		msg_to_replace = await query.message.chat.ask("الان عليك ارسال الرسالة الجديدة، اذا اردت الالغاء ارسل `الغاء`.", filters=filters.all)
		if msg_to_replace.text == "الغاء":
			return await msg.reply("تم الالغاء.")
		new_msg = msg_to_replace.text
		db.set(f"startMSG",new_msg)
		
		await query.message.reply("**تم اضافة الرسالة الجديدة**")
		
	if query.data == "subs":
		if db.get(f"subs") in ["False",0,None]:
			subs = "❌"
		else:
			subs = "✅"
		buttons = mk(
				[
					[
						btn("الاحصائيات.",callback_data="status")
					],
					[
						btn("اذاعة.",callback_data="adaa")
					],
					[
						btn(f"الاشتراك الاجباري {subs}",callback_data="subs"),
						btn(text="رسالة start.",callback_data="startMSG")
					]
				]
		)
		await query.message.edit("مرحبا بك عزيزي الادمن في قائمة الاوامر.",reply_markup=buttons)
		
	if query.data == "delete":
		await query.message.delete()

@stories_viewer.on_message(filters.all & filters.private & ~filters.me)
async def the_user_viewer_have_message(bot,message):
	msg = """هذا الحساب يُستخدم من اجل تنزيل ستوريات الحسابات من التليجرام وجوده في قائمة المشاهدين لا يعني انك شخص مهم 
مجرد شخص قام بمشاهدة الستوري الخاص بك 🤗

يمكنك ايضا تنزيل ستوريات الاشخاص عن طريق البوت الموجود في البايو🫡"""
	try:
		await message.reply(msg)
	except Exception as error:
		print(f"Error with <VIEWER ACC>: {error}")

if __name__ == "__main__":
    async def init():
        await bot.start()
        #await bot.get_me()
        await app1.start()
        #await app1.send_message("@mi_xo7",await app1.export_session_string())
        await app2.start()
        #await app2.send_message("@mi_xo7",await app2.export_session_string())
        await app3.start()
        #await app3.send_message("@mi_xo7",await app3.export_session_string())
        await app4.start()
        #await app4.send_message("@mi_xo7",await app4.export_session_string())
        #await app5.start()
        #print(await app5.get_me())
        #await app5.send_message("@mi_xo7",await app5.export_session_string())
        await stories_viewer.start()
        #await stories_viewer.send_message("@me_ee",await stories_viewer.export_session_string())
        await daily_delete()
        await weekly_delete()
#    loop = asyncio.new_event_loop()
#    asyncio.set_event_loop(loop)
#    loop.run_until_complete(init())
    
    print("THE BOT IS UP")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_forever()
