import requests
import re

ten_kenh = "Giọng Ca Để Đời"
url_nguon = "https://www.youtube.com/live/LDivJzkSTXY"

try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url_nguon, headers=headers, timeout=10)
    noi_dung = response.text
    match = re.search(r'https?://[^\s"\'<>]*\.m3u8\?[^\s"\'<>]*token=[a-zA-Z0-9]+', noi_dung)
    
    if match:
        link = match.group(0)
        m3u = f"#EXTM3U\n#EXTINF:-1, {ten_kenh}\n{link}\n"
        with open("list-kenh.m3u", "w", encoding="utf-8") as f:
            f.write(m3u)
        print("OK")
    else:
        print("Khong tim thay link")
except Exception as e:
    print(f"Loi: {e}")
    
