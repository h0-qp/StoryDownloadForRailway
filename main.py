import requests,os,re,random,asyncio,json
import threading
from flask import Flask
from pyrogram import Client, filters ,enums,idle
from pyrogram.types import InlineKeyboardMarkup as mk, InlineKeyboardButton as btn
from pyrogram.errors import FloodWait
from pyromod import listen 
from sqldb import db
db.autocommit = True
import config
import datetime
import time

# --- إعداد السيرفر الوهمي (Flask) لضمان بقاء البوت شغال ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "AliBot is Running!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = threading.Thread(target=run_web)
    t.start()
# --------------------------------------------------------

token = config.token 
ch_user = config.ch_id 
ch_name = "أنا بغدادي" 
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
	api_id = 28142751,  
	api_hash = "b687bb41ce8938f0535819f9ae46a075", 
	phone_number = "+212783223178",
	session_string = "BAGtbJ8AMXkVFHoLb91vUZR82EQpIIMb2P2hLwxGD8oNAKmcZQMu_IPVbtjohHcq_u36ugXZSu7WqVnTgzQD4gFGYAufgeTV2M-6XedYUmkdfAJgxH9dhJlwhJlEz5FsDzj99o_jk57BNq6inozoxem5U1J7DH71RBfh-3Uy1tUCqK-fH54eGMWM1mIuE0t8PuTx5_gMM7L-xgIDw5xJEwV94S7VK4akb35LYxgL-8zaSV7SmFwF0E6NlCNk5AX4jjjEWlhJdUnLrx4BG3_jRfN0scL7nZP5cV1KPlVSVoOlLcVcYQ97uW_tHj2OLsy00JuS1nVkMPxssSgVPzE03TgAVN_KiwAAAAGEyRG4AA"
)
app4 = Client(
	"botalimhamood9",
	api_id = 22266096,  
	api_hash = "249920fba6117b3d90a779135172fe09", 
	phone_number = "+201206612729",
	session_string = "BAFTwPAAC8CgOnLuSi46hAEzfc97dppcNTq15bYNBiGKjPktebuzEvlWsulA34V2PdmBkeFmclLes8ciYxiHbel_S7MLcoNYho90q3ZDvI-QKTu-Olf2cp7K6uNtHKCUgfshzE_oxFOgy1UqEzUzQ-hGuyK_MgeA6aJ4CN47h2zIC-kHF5sNgypipMj3bCPes9XZRS_7fMONURcMt5FlWPodrN6FdrFXkmaWzc16Ey38i16csKhNw01_dMi6jn5JfLIc0Cc66svibtbHdLFtxgnccI0bumJkiUx09DR5aEQLeYws5jgGC9csec7LRmk79WTSQiH1TRSPcj_N1vPvRQ2qHoG-kwAAAAFyAB6sAA"
)
app3 = Client(
	"botalimhamood10",
	api_id = 27013572,  
	api_hash = "3b802c362e53fabf54a6ed91708f8241", 
	phone_number = "+212630334721",
	session_string = "BAGcMcQAJIKtBHDWdtjoL8dbPF3Hso0alxoPCb7YGN1Ft03yox2x0NMg0CPBxnnF3WgHo3CR1pbtRsXafunTeczHgd78hJjU_JUy3AcsnzVLSzQWFET1wj80f5iUdyTd9fZQd5hJPY1PEXEHdmn-HEPRA09RcAg78rmG47pHnzOmGJ6_3pKfRTrg_qBQX2sM55BnG_E4VZewd61cRGPOY8wpJuCtUh-Y-MA3htTdxFPsjtwXu59W38DUk7h3U4DYjL1a5EaQaMS5Uh_Xe-PQCKKOoOlS2TIF4yba2leSpt3xPG0_VrmVcb5-yHkR37p0yzoSGernlHI8HcbhGWZXSgr2X73-AQAAAAG-VpZGAA"
)

stories_viewer = Client(
	"stories_viewer_test_ali",
	api_id = 25334168,  
	api_hash = "be0b107d3369166c4333317e95047404",
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

what = {
	"adaa": "False",
	"replace_channel": "False",
	"replace_startMSG": "False"
}

async def daily_delete():
	while True:
		now = datetime.datetime.now()
		if now.day in [1,2,3,4,5,6,7]:
			msg_for_subs = f"""مرحبا بك عزيزي المطور 😇👋، هذه الرسالة هي تذكير لفترة الإشتراك والمقدرة يوم 1 من الشهر واليوم هو {now.day}، في حال لم يتم وان قمت بالدفع فقم بالتجاهل فقط."""
			await bot.send_message("@alimhamood",msg_for_subs)
		os.system("rm -rf downloads")
		await asyncio.sleep(86400)
		db.set(f"daily_join",0)
		db.set(f"daily_uses",0)

async def weekly_delete():
	while True:
		await asyncio.sleep(604800)
		db.set(f"weekly_join",0)
		db.set(f"weekly_uses",0)

# --- دالة التنظيف كل ساعتين لضمان عدم امتلاء المساحة ---
async def cleanup_files():
	while True:
		await asyncio.sleep(7200) # 7200 ثانية = ساعتين
		try:
			# مسح اي ملف ميديا متراكم بالمسار الرئيسي
			for file in os.listdir():
				if file.endswith(('.jpg', '.png', '.jpeg', '.mp4', '.webp')):
					os.remove(file)
			os.system("rm -rf downloads")
		except Exception as e:
			print(f"Cleanup error: {e}")
# --------------------------------------------------------

def number_to_string(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return str(round(number / 1000, 1)).replace('.0', '') + 'k'
    else:
        return str(int(number / 1000000)) + 'm'

def is_member(user_id):
	get = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id={ch_user}&user_id={user_id}").json()
	if get["result"]["status"] == "left":
		return False
	else:
		return True

ch_user = "@iBaghdady"
ch_btn = mk([
	[btn(ch_name,url=f"https://t.me/{ch_user.replace('@','')}")]
])

# إعدادات قاعدة البيانات
if not db.exists(f"daily_uses"): db.set(f"daily_uses",0)
if not db.exists(f"weekly_uses"): db.set(f"weekly_uses",0)
if not db.exists(f"total_uses"): db.set(f"total_uses",0)
if not db.exists(f"daily_join"): db.set(f"daily_join",0)
if not db.exists(f"weekly_join"): db.set(f"weekly_join",0)
if not db.exists(f"subs"): db.set(f"subs","False")
if not db.exists(f"startMSG"): db.set(f"startMSG", '''مرحبا بك في بوت تحميل ستوريات التيليجرام فقط ارسل معرف/ايدي/رابط للتحميل.''')

os.system("rm -rf AliBot.session AliBot.session-journal")

@bot.on_message(filters.command("start") & filters.private)
async def welcome(bot,message):
	user = message.from_user
	name = user.mention
	username = user.username
	id = user.id
	startMSG = db.get(f"startMSG")
	
	members = db.get("users")
	if not members: members = []
	
	if not id in members:
		daily_join = int(db.get(f"daily_join") or 0) +1
		weekly_join = int(db.get(f"weekly_join") or 0) +1
		db.set(f"daily_join",daily_join)
		db.set(f"weekly_join",weekly_join)
		members.append(id)
		db.set("users",members)
		await bot.send_message(dev,in_msg.format(name,id,username,len(members)))
	
	if message.from_user.id in [dev,435009958,1160471152]:
		subs = "❌" if db.get(f"subs") in ["False",0,None] else "✅"
		buttons = mk([
				[btn("الاحصائيات.",callback_data="status")],
				[btn("اذاعة.",callback_data="adaa")],
				[btn(f"الاشتراك الاجباري {subs}",callback_data="subs"), btn(text="رسالة start.",callback_data="startMSG")]
			])
		await message.reply(startMSG,reply_markup=ch_btn)
		await message.reply("مرحبا بك عزيزي الادمن في قائمة الاوامر.",reply_markup=buttons)
	
	elif not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول.\n\nCH: {ch_user}",reply_markup=ch_btn)
		else:
			await message.reply(startMSG,reply_markup=ch_btn)
	else:
		await message.reply(startMSG,reply_markup=ch_btn)

@bot.on_message(filters.regex("^(نسخة احتياطية|نسخه احتياطيه|/database)$") & filters.private)
async def get_database(bot,message):
	id = message.from_user.id
	if id in [dev,435009958,1160471152]:
		members = db.get(f"users")
		num = len(members)
		for user_id in members:
			open("members.txt","a").write(f"{user_id}\n")
		await message.reply_document(open("members.txt","rb"), caption=f"نسخة الاعضاء الاحتياطية.\nالعدد: {num}")
		os.remove("members.txt")
		try: await message.reply_document(open(f"{bot_name}.sqlite-shm","rb"), caption="ملف التخزين الاحتياطي.")
		except: pass
		try: await message.reply_document(open(f"{bot_name}.sqlite-wal","rb"), caption="ملف الفهرسة.")
		except: pass
		await message.reply_document(open(f"{bot_name}.sqlite","rb"), caption="هذه هي نسخة البوت بالكامل.")

@bot.on_message(filters.regex("^https://t.me/") & filters.private)
async def get_stories_from_link(bot,message):
	id = message.from_user.id
	user_id = message.from_user.id
	name = message.from_user.first_name
	username = message.from_user.username
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك في قناة البوت رجاءا أشتراك بالاول.\n\nCH: {ch_user}",reply_markup=ch_btn)
	
	if not "/s/" in message.text:
		return await message.reply("ارسل رابط ستوري صحيح.")
	text = message.text.replace("https://t.me/","").replace("t.me/","")
	id,number = text.split("/s/")
	msg = await message.reply("**جاري البحث عن استوريات التليجرام لهذا الشخص عادة مايستغرق الامر 30 ثانية لغرض منع الحظر...**")
	try:
		if what_account[0] == 4:
			story = await app1.get_stories(id,int(number))
			what_account[0] = 1
		elif what_account[0] == 1:
			story = await app2.get_stories(id,int(number))
			what_account[0] = 2
		elif what_account[0] == 2:
			story = await app3.get_stories(id,int(number))
			what_account[0] = 3
		elif what_account[0] == 3:
			story = await app4.get_stories(id,int(number))
			what_account[0] = 4
			
		file_name = await story.download()
		if file_name.endswith(('.jpg', '.png', '.jpeg')):
			await bot.send_photo(message.chat.id,open(file_name,"rb"))
		else:
			await bot.send_video(message.chat.id,open(file_name,"rb"))
		await asyncio.sleep(1.5)
		try:
			await stories_viewer.view_stories(id,number)
			if "@" in id: id = id.replace("@","")
			user = await stories_viewer.get_users(id)
			viewer_msg = f"هذا الشخص:\nالاسم: {name}\nاليوزر: @{username}\nالايدي: {user_id}\n\nشاهد ستوري هذا الشخص:\nالاسم: {user.first_name}\nاليوزر: @{id}\nالايدي: {user.id}"
			try: await stories_viewer.send_message("me",viewer_msg)
			except: pass
		except: pass
		
		os.remove(file_name)
		
		db.set(f"daily_uses", int(db.get(f"daily_uses")) +1)
		db.set(f"weekly_uses", int(db.get(f"weekly_uses")) +1)
		db.set(f"total_uses", int(db.get(f"total_uses")) +1)
		
	except Exception as error:
		await bot.send_message("alimhamood",f"رسالة الخطأ: {str(error)}")
		return await msg.edit("لا يمكن للبوت جلب ستوريات هذا الشخص.")
	await msg.delete()
	

@bot.on_message(filters.regex("^(@|[a-zA-Z0-9_]+$)") & filters.private)
async def get_stories_from_user(bot,message):
	id = message.from_user.id
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك في قناة البوت.\n\nCH: {ch_user}",reply_markup=ch_btn)
	user = message.text.split("@")[1] if "@" in message.text else message.text
	if not re.match(r'^[a-zA-Z0-9_]+$', user): return
	return await message.reply("**أختر ماذا تريد؟:**",reply_markup=mk([
			[btn(text="ستوريات اليوم 🔰",callback_data=f"today:{user}")],
			[btn(text="الاستوريات المثبتة 🗓",callback_data=f"archive:{user}")]
		]))

@bot.on_message(filters.regex("^\d+") & filters.private)
async def get_stories_from_user_id(bot,message):
	id = message.from_user.id
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك.\n\nCH: {ch_user}",reply_markup=ch_btn)
	user = message.text
	if not re.match(r'^\d+', user): return
	return await message.reply("**أختر ماذا تريد؟:**",reply_markup=mk([
			[btn(text="ستوريات اليوم 🔰",callback_data=f"today:{user}")],
			[btn(text="الاستوريات المثبتة 🗓",callback_data=f"archive:{user}")]
		]))

@bot.on_message(filters.all & filters.private)
async def get_all_messages_from_user(bot,message):
	id = message.from_user.id
	if not db.get(f"subs") in ["False",0,None]:
		if is_member(id) == False:
			return await message.reply(f"أنت غير مشترك.\n\nCH: {ch_user}",reply_markup=ch_btn)
	msg = f"""هذا البوت مخصص فقط لتحميل ستوريات التيليجرام، اذا أردت تحميل من مواقع التواصل الاجتماعي عليك تجربة بوتنا الاخر:\n**• @M4S1bot •**"""
	if message.text:
		if not re.match(r"^https://t\.me/.+/s/.*$", message.text):
			await message.reply(msg)
	else:
		try: await message.forward("forwoa")
		except: pass

@bot.on_callback_query(filters.regex("^(today:(.*?)|archive:(.*?))$"))
async def downloaderStory(bot, query):
	method,user = query.data.split(":")
	name = query.from_user.first_name
	username = query.from_user.username
	user_id = query.from_user.id
	
	await query.message.edit("**جاري البحث والتحميل (سيتم إرسال الستوريات على دفعات لضمان السرعة)...**")
	
	try:
		if method == "today":
			if what_account[0] == 4:
				story = app1.get_chat_stories(user)
				what_account[0] = 1
			elif what_account[0] == 1:
				story = app2.get_chat_stories(user)
				what_account[0] = 2
			elif what_account[0] == 2:
				story = app3.get_chat_stories(user)
				what_account[0] = 3
			elif what_account[0] == 3:
				story = app4.get_chat_stories(user)
				what_account[0] = 4
		else:
			if what_account[0] == 4:
				story = app1.get_pinned_stories(user)
				what_account[0] = 1
			elif what_account[0] == 1:
				story = app2.get_pinned_stories(user)
				what_account[0] = 2
			elif what_account[0] == 2:
				story = app3.get_pinned_stories(user)
				what_account[0] = 3
			elif what_account[0] == 3:
				story = app4.get_pinned_stories(user)
				what_account[0] = 4

		storiesID = []
		batch = [] # مصفوفة الدفعة
		total_sent = 0
		
		async for s in story:
			storiesID.append(s.id)
			file_name = await s.download()
			batch.append({"file_name": file_name, "date": s.date})
			
			# 🔥 نظام الدفعات: إذا وصل العدد 10 ستوريات، أرسلها وامسحها فوراً
			if len(batch) >= 10:
				for file in batch:
					if file["file_name"].endswith(('.jpg', '.png', '.jpeg')):
						await bot.send_photo(query.message.chat.id, open(file["file_name"], "rb"), caption=f"🗓 {file['date']} .")
					else:
						await bot.send_video(query.message.chat.id, open(file["file_name"], "rb"), caption=f"🗓 {file['date']} .")
					os.remove(file["file_name"]) # مسح الملف فورا بعد الارسال
				batch.clear() # تفريغ الدفعة لاستقبال الـ 10 اللي بعدها
				total_sent += 10
				
		# إرسال ما تبقى من الستوريات (إذا كان العدد المتبقي أقل من 10)
		if len(batch) > 0:
			for file in batch:
				if file["file_name"].endswith(('.jpg', '.png', '.jpeg')):
					await bot.send_photo(query.message.chat.id, open(file["file_name"], "rb"), caption=f"🗓 {file['date']} .")
				else:
					await bot.send_video(query.message.chat.id, open(file["file_name"], "rb"), caption=f"🗓 {file['date']} .")
				os.remove(file["file_name"])
			total_sent += len(batch)
			batch.clear()

		if total_sent == 0:
			return await query.message.edit("الحساب لا يوجد به ستوريات.")
			
		await query.message.delete()

		# تسجيل المشاهدة
		try:
			if len(storiesID) > 0:
				await stories_viewer.view_stories(user,storiesID[0])
				userInfo = await stories_viewer.get_users(user)
				viewer_msg = f"الاسم: {name}\nاليوزر: @{username}\nالايدي: {user_id}\n\nشاهد ستوري:\nالاسم: {userInfo.first_name}\nاليوزر: @{user}\nالايدي: {userInfo.id}"
				try: await stories_viewer.send_message("me",viewer_msg)
				except: pass
		except: pass

		# تحديث الإحصائيات
		db.set(f"daily_uses", int(db.get(f"daily_uses")) +1)
		db.set(f"weekly_uses", int(db.get(f"weekly_uses")) +1)
		db.set(f"total_uses", int(db.get(f"total_uses")) +1)

	except Exception as error:
		print(error)
		return await query.message.edit("لا يمكن للبوت جلب ستوريات هذا الشخص.")

@bot.on_callback_query(filters.regex("^(status|adaa|startMSG|replace_startMSG|back|subs|delete)$"))
async def settings(bot, query):
	id = query.from_user.id
	back = mk([[btn("رجوع",callback_data="back")]])
	subs_status = "❌" if db.get(f"subs") in ["False",0,None] else "✅"
	buttons = mk([
			[btn("الاحصائيات.",callback_data="status")],
			[btn("اذاعة.",callback_data="adaa")],
			[btn(f"الاشتراك الاجباري {subs_status}",callback_data="subs"), btn(text="رسالة start.",callback_data="startMSG")]
		])
	replace_startMSG = mk([[btn(text="تغيير رسالة ستارت",callback_data="replace_startMSG")], [btn(text="رجوع",callback_data="back")]])
	
	if query.data == "back":
		await query.message.edit("مرحبا بك عزيزي الادمن في قائمة الاوامر.",reply_markup=buttons)
	
	elif query.data == "status":
		members_list = db.get(f"users")
		members = len(members_list) if members_list else 0
		weekly_join = number_to_string(int(db.get(f"weekly_join") or 0))
		daily_join = number_to_string(int(db.get(f"daily_join") or 0))
		total_uses = number_to_string(int(db.get(f"total_uses") or 0))
		weekly_uses = number_to_string(int(db.get(f"weekly_uses") or 0))
		daily_uses = number_to_string(int(db.get(f"daily_uses") or 0))
		
		msg = f"**عدد الأعضاء الكلي: {members}**\n**الدخول اخر 7 أيام: {weekly_join}**\n**الدخول اخر 24 ساعة: {daily_join}**\n__ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ__\n**عدد التحميلات الكلي: {total_uses}**\n**التحميلات اخر 7 أيام: {weekly_uses}**\n**التحميلات اخر 24 ساعة: {daily_uses}**"
		await query.message.edit(msg,reply_markup=back)
	
	elif query.data == "adaa":
		msg = await query.message.chat.ask('الان ارسل المراد ارساله\n\n اذا اردت الالغاء فقط ارسل `الغاء`.', filters=filters.all)
		if msg.text == "الغاء": return await msg.reply("تم الالغاء.")
		true, false, numofdone = [], [], []
		members = db.get(f"users") or []
		progressMSG = await bot.send_message(chat_id=id, text="جاري الإرسال... النسبة المئوية: 0%")
		for idx, user in enumerate(members):
			try:
				await msg.copy(user)
				true.append(user)
				await asyncio.sleep(1.5)
			except FloodWait as e:
				await asyncio.sleep(e.value)
			except Exception as e:
				false.append(user)
			numofdone.append(user)
			if len(numofdone) >= 100:
				progress = (idx / len(members)) * 100
				await progressMSG.edit(f"جاري الإرسال... النسبة المئوية: {progress:.2f}%")
				numofdone.clear()
		await msg.reply(f"تمت الاذاعة الى {len(true)}\n\nالذين حظروا البوت {len(false)}")

	elif query.data == "subs":
		if db.get(f"subs") in ["False",None,0]:
			db.set(f"subs", "True")
			await query.answer("تم التفعيل.")
		else:
			db.set(f"subs", "False")
			await query.answer("تم التعطيل.")
		subs_status = "❌" if db.get(f"subs") in ["False",0,None] else "✅"
		new_buttons = mk([
			[btn("الاحصائيات.",callback_data="status")],
			[btn("اذاعة.",callback_data="adaa")],
			[btn(f"الاشتراك الاجباري {subs_status}",callback_data="subs"), btn(text="رسالة start.",callback_data="startMSG")]
		])
		await query.message.edit("مرحبا بك عزيزي الادمن في قائمة الاوامر.",reply_markup=new_buttons)

	elif query.data == "startMSG":
		my_msg = db.get(f"startMSG")
		await query.message.edit(f"الرسالة: {my_msg}",reply_markup=replace_startMSG)

	elif query.data == "replace_startMSG":
		await query.message.delete()
		msg_to_replace = await query.message.chat.ask("الان عليك ارسال الرسالة الجديدة، اذا اردت الالغاء ارسل `الغاء`.", filters=filters.all)
		if msg_to_replace.text == "الغاء": return await msg.reply("تم الالغاء.")
		db.set(f"startMSG",msg_to_replace.text)
		await query.message.reply("**تم اضافة الرسالة الجديدة**")
		
	if query.data == "delete":
		await query.message.delete()

@stories_viewer.on_message(filters.all & filters.private)
async def the_user_viewer_have_message(bot,message):
	msg = "هذا الحساب يُستخدم من اجل تنزيل ستوريات الحسابات من التليجرام وجوده في قائمة المشاهدين لا يعني انك شخص مهم \nمجرد شخص قام بمشاهدة الستوري الخاص بك 🤗\n\nيمكنك ايضا تنزيل ستوريات الاشخاص عن طريق البوت الموجود في البايو🫡"
	try: await message.reply(msg)
	except: pass

if __name__ == "__main__":
    async def init():
        keep_alive() # تشغيل السيرفر الوهمي
        await bot.start()
        await app1.start()
        await app2.start()
        await app3.start()
        await app4.start()
        await stories_viewer.start()
        
        # تشغيل دوال التنظيف بالخلفية
        asyncio.create_task(daily_delete())
 
