import subprocess

channels = [
    {"name": "Live Của Tôi", "url": "https://m.youtube.com/live/LDivJzkSTXY"}
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for ch in channels:
        print(f"Đang lấy link cho: {ch['name']}")
        try:
            # Đã đổi '-f', 'best' thành '-f', 'b'
            result = subprocess.run(
                ['yt-dlp', '-f', 'b', '-g', ch['url']], 
                capture_output=True, text=True, check=True
            )
            m3u8_url = result.stdout.strip()
            
            if m3u8_url:
                f.write(f'#EXTINF:-1 tvg-name="{ch["name"]}",{ch["name"]}\n')
                f.write(f"{m3u8_url}\n")
                print("-> Thành công!")
        except subprocess.CalledProcessError as e:
            print(f"-> Lỗi chi tiết từ YouTube: {e.stderr.strip()}")
        except Exception as e:
            print(f"-> Lỗi hệ thống: {e}")
