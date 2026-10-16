# 3.1. Khởi tạo một bản quan sát
ma_quan_sat = "OBS025"
so_lan_do = 4
gia_tri_do = 31.5
hop_le = True
ghi_chu = None
# In giá trị và kiểu của từng biến bằng print() và type()
print("ma_quan_sat:", ma_quan_sat, "| Kieu:", type(ma_quan_sat))
print("so_lan_do:", so_lan_do, "| Kieu:", type(so_lan_do))
print("gia_tri_do:", gia_tri_do, "| Kieu:", type(gia_tri_do))
print("hop_le:", hop_le, "| Kieu:", type(hop_le))
print("ghi_chu:", ghi_chu, "| Kieu:", type(ghi_chu))

# 3.2. Gán lại giá trị
gia_tri_do = 31.5
print("Lan 1:", gia_tri_do)
gia_tri_do = 29.8
print("Lan 2:", gia_tri_do)
# GIAI THICH: Sau phép gán thứ hai, tên gia_tri_do sẽ truy cập
# vào giá trị mới là 29.8 (giá trị cũ 31.5 đã bị ghi đè/thay thế).

# 3.3. None và các giá trị khác
# DU DOAN: Tất cả 3 phép so sánh dưới đây đều trả về False
# vì None biểu thị giá trị rỗng/không có gì, hoàn toàn khác với 0, chuỗi rỗng "" hay False.
print("None == 0   ->", None == 0)
print("None == ''  ->", None == "")
print("None == False ->", None == False)