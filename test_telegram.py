import requests

# 1. ข้อมูลของbot
TOKEN = '8220444201:AAHig8BTsCcurclOyVDGOIXgYzct8ITp50I'  
CHAT_ID = '8696330483'    

# 2. ฟังก์ชันสำหรับส่งข้อความ
def send_telegram_message(message_text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message_text
    }
    
    # สั่งยิงข้อมูลไปที่ Telegram
    response = requests.post(url, data=payload)
    
    # เช็คว่าส่งสำเร็จไหม
    if response.status_code == 200:
        print("ส่งข้อความเข้า Telegram สำเร็จแล้ว!")
    else:
        print(f"ส่งไม่สำเร็จ โค้ดแจ้งเตือน: {response.text}")

# 3. ลองเรียกใช้งานฟังก์ชัน
send_telegram_message("สวัสดีนี่คือข้อความทดสอบแจ้งเตือนจากระบบ")