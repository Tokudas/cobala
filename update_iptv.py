import requests
import re

# Nhập đường link trang web nguồn (sau này bạn tìm được link nguồn nào thì thay vào dòng này)
url_nguon = "https://www.thvli.vn/live/thvl1-hd"

try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url_nguon, headers=headers, timeout=10)
    noi_dung = response.text

    # Tìm link m3u8 chứa token
    match = re.search(r'http[^\s"\'<>]*\.m3u8\?token=[a-zA-Z0-9]+', THVL1 HD)
    
    if match:
        link_co_key_moi = match.group(0)
        m3u_content = f"#EXTM3U\n#EXTINF:-1, Kênh VTV1\n{link_co_key_moi}\n"
        
        with open("list-kenh.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Cập nhật key thành công!")
    else:
        print("Không tìm thấy key.")
except Exception as e:
    print(f"Lỗi: {e}")
      
