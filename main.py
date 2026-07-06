import requests
import datetime
import random

def fetch_tv360_link():
    channel_id = '32'
    
    # Giả lập dải IP dân dụng của mạng Viettel khu vực Hà Nội (115.79.x.x)
    fake_hanoi_viettel_ip = f"115.79.{random.randint(1, 255)}.{random.randint(1, 255)}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Referer': f'https://m.tv360.vn/tv/hitv?ch={channel_id}',
        'Origin': 'https://m.tv360.vn',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Chèn IP Hà Nội vào tất cả các cổng header có thể có
        'X-Forwarded-For': fake_hanoi_viettel_ip,
        'X-Real-IP': fake_hanoi_viettel_ip,
        'Client-IP': fake_hanoi_viettel_ip,
        'X-Client-IP': fake_hanoi_viettel_ip
    }
    
    api_url = "https://api.tv360.vn/public/v1/vod/play-info"
    params = {'id': channel_id, 'content_type': '0', 'quality': 'HD', 'platform': 'web'}
    
    try:
        # Sử dụng Session để giữ trạng thái kết nối
        session = requests.Session()
        res = session.get(api_url, headers=headers, params=params, timeout=10)
        if res.status_code == 200:
            data = res.json()
            return data.get('data', {}).get('stream_url', '')
    except Exception as e:
        print(f"Lỗi kết nối API: {e}")
    return None

def update_playlist():
    link = fetch_tv360_link()
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        if link:
            f.write(f'#EXTINF:-1 tvg-id="HiTV" tvg-name="HiTV" group-title="TV360",HiTV (Cập nhật: {datetime.datetime.now().strftime("%H:%M:%S")})\n')
            f.write(link + "\n")
            print("Tuyệt vời! Đã vượt rào thành công và lấy được key bằng IP Hà Nội!")
        else:
            f.write('#EXTINF:-1 group-title="Bảo trì",Kênh HiTV đang chờ làm mới key\n')
            f.write("https://example.com/temporary.m3u8\n")
            print("Tường lửa Viettel vẫn chặn IP của GitHub.")

if __name__ == "__main__":
    update_playlist()
