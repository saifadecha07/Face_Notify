import requests

# 1. ข้อมูลของbot
TOKEN = '8220444201:AAHig8xxxxxxxxxxxxx'  
CHAT_ID = '869xxxxxxxx'    

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
        print("Message sent")
    else:
        print(f"Message unsent: {response.text}")

# 3. ลองเรียกใช้งานฟังก์ชัน
send_telegram_message("Hello")