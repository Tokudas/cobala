import subprocess

# Link YouTube Live bạn yêu cầu
url_youtube = "https://www.youtube.com/live/LDivJzkSTXY"
ten_kenh = "YouTube Live"

try:
    # Lệnh lấy link trực tiếp từ YouTube
    # --get-url -f "best" giúp lấy link m3u8 chất lượng tốt nhất
    command = f'yt-dlp --get-url -f "best" {url_youtube}'
    result = subprocess.check_output(command, shell=True, text=True).strip()
    
    # Tạo file m3u
    m3u_content = f"#EXTM3U\n#EXTINF:-1, {ten_kenh}\n{result}\n"
    with open("list-kenh.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Lay link thanh cong!")
except Exception as e:
    print(f"Loi: {e}")
