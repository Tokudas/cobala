import requests
import datetime

def fetch_tv360_link():
    channel_id = '32' # ID của kênh HiTV
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
        print(f"Lỗi khi cào dữ liệu: {e}")
    return None

def update_playlist():
    link = fetch_tv360_link()
    if link:
        # Ghi đè file playlist.m3u bằng link có chứa key mới nhất
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write(f'#EXTINF:-1 tvg-id="HiTV" tvg-name="HiTV" group-title="TV360",HiTV (Cập nhật: {datetime.datetime.now().strftime("%H:%M")})\n')
            f.write(link + "\n")
        print("Cập nhật key thành công!")
    else:
        print("Không lấy được link/key từ TV360.")

if __name__ == "__main__":
    update_playlist()
