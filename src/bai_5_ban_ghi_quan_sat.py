# 5.1. Thiết kế dữ liệu nhập
ma_quan_sat = input("Nhap ma quan sat (str): ")
ten_dai_luong = input("Nhap ten dai luong (str): ")
gia_tri_do = float(input("Nhap gia tri do (float): "))
don_vi = input("Nhap don vi (str): ")

# 5.2. Gắn thời điểm hiện tại
from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

# 5.3. Xuất bản ghi bằng f-string
print(f"Ma quan sat : {ma_quan_sat}")
print(f"Dai luong : {ten_dai_luong}")
print(f"Gia tri : {gia_tri_do:.2f} {don_vi}")
print(f"Thoi diem : {thoi_diem_text}")