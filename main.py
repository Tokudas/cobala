import requests
import datetime

def fetch_tv360_link():
    channel_id = '32'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Referer': f'https://m.tv360.vn/tv/hitv?ch={channel_id}'
    }
    api_url = "https://api.tv360.vn/public/v1/vod/play-info"
    params = {'id': channel_id, 'content_type': '0', 'quality': 'HD', 'platform': 'web'}
    
    try:
        res = requests.get(api_url, headers=headers, params=params, timeout=10)
        if res.status_code == 200:
            data = res.json()
            return data.get('data', {}).get('stream_url', '')
    except Exception as e:
        print(f"Lỗi kết nối API: {e}")
    return None

def update_playlist():
    link = fetch_tv360_link()
    
    # Luôn luôn tạo file playlist.m3u để sửa lỗi Git tuyệt đối
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        if link:
            f.write(f'#EXTINF:-1 tvg-id="HiTV" tvg-name="HiTV" group-title="TV360",HiTV (Cập nhật: {datetime.datetime.now().strftime("%H:%M:%S")})\n')
            f.write(link + "\n")
            print("Đã lấy được key và cập nhật link thành công!")
        else:
            # Nếu hệ thống bận, ghi link tạm thời để file không bị trống
            f.write('#EXTINF:-1 group-title="Bảo trì",Kênh HiTV đang chờ làm mới key\n')
            f.write("https://example.com/temporary.m3u8\n")
            print("Tạm thời không lấy được key, đã tạo file dự phòng.")

if __name__ == "__main__":
    update_playlist()
