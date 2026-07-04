import subprocess

url_youtube = "https://www.youtube.com/live/LDivJzkSTXY"
ten_kenh = "YouTube Live"

try:
    # Lệnh yt-dlp để lấy link stream m3u8 trực tiếp
    # --get-url giúp lấy link trần, -f "best" lấy chất lượng cao nhất
    command = f'yt-dlp --get-url -f "best" {url_youtube}'
    result = subprocess.check_output(command, shell=True, text=True).strip()
    
    # Tạo nội dung file m3u
    m3u_content = f"#EXTM3U\n#EXTINF:-1, {ten_kenh}\n{result}\n"
    
    with open("list-kenh.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Tao file list-kenh.m3u thanh cong!")
except Exception as e:
    print(f"Khong the lay link, loi: {e}")
