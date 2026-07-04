import requests
import re

# Nhập đường link trang web nguồn (sau này bạn tìm được link nguồn nào thì thay vào dòng này)
url_nguon = "https://www.thvli.vn/live/thvl1-hd"

try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url_nguon, headers=headers, timeout=10)
    noi_dung = response.text

    # Tìm link m3u8 chứa token
            if match:
            link_co_key_moi = match.group(0)
            m3u_content += f'#EXTINF:-1 tvg-name="{ten_kenh}", {ten_kenh}\n{link_co_key_moi}\n'
            print(f"[OK] {ten_kenh}")
        else:
            # Ghi thông báo ra để bạn dễ kiểm tra trong tab Actions
            print(f"[FAIL] Khong tim thay link cho {ten_kenh}")
    except Exception as e:
        print(f"[ERROR] Loi {ten_kenh}: {str(e)}")

# Thêm điều kiện để không báo lỗi nếu không có kênh nào được lấy
if m3u_content != "#EXTM3U\n":
    with open("list-kenh.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
else:
    print("Khong co kenh nao duoc lay, bo qua viec ghi file.")

            f.write(m3u_content)
        print("Cập nhật key thành công!")
    else:
        print("Không tìm thấy key.")
except Exception as e:
    print(f"Lỗi: {e}")
      
