import subprocess
import os

url_youtube = "https://www.youtube.com/live/LDivJzkSTXY"
ten_kenh = "YouTube Live"

try:
    command = f'yt-dlp --get-url -f "best" {url_youtube}'
    result = subprocess.check_output(command, shell=True, text=True).strip()
    
    with open("list-kenh.m3u", "w", encoding="utf-8") as f:
        f.write(f"#EXTM3U\n#EXTINF:-1, {ten_kenh}\n{result}\n")
    print("Tao file thanh cong!")
except Exception as e:
    print(f"Loi chi tiet: {e}")
    with open("list-kenh.m3u", "w") as f:
        f.write("# Lỗi lấy link")
        
