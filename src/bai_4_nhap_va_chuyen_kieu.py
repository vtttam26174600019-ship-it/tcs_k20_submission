# 4.1. Nhập ba trường dữ liệu
ma_quan_sat = input("Nhap ma quan sat: ")
so_lan_do = int(input("Nhap so lan do: "))
gia_tri_do = float(input("Nhap gia tri do: "))
don_vi_do = input("Nhap don vi do: ")

# 4.2. Tính giá trị dẫn xuất
gia_tri_f = gia_tri_do * 9 / 5 + 32
print("Ma quan sat:", ma_quan_sat)
print("So lan do:", so_lan_do)
print("Gia tri C:", gia_tri_do, don_vi_do)
print("Gia tri F:", gia_tri_f, "F")

print("Kieu cua so_lan_do:", type(so_lan_do))
print("Kieu cua gia_tri_do:", type(gia_tri_do))

so_lan_do_text = str(so_lan_do)
print("Gia tri so_lan_do_text:", so_lan_do_text)
print("Kieu cua so_lan_do_text:", type(so_lan_do_text))

# GIẢI THÍCH LỖI 
# Khi người dùng nhập chuỗi chữ như 'abc' vào int() hoặc float(),
# Python không thể chuyển đổi chữ cái thành số được nên sẽ báo lỗi ValueError