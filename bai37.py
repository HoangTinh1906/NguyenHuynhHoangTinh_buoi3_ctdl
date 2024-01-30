danh_sach_tu = ["táo", "chuối", "cam", "táo", "chuối", "nho", "táo"]
def dem_tan_suat_tu(danh_sach_tu):
    tan_suat_tu = {}
    for i in range(len(danh_sach_tu)):
        tu = danh_sach_tu[i]
        if tu in tan_suat_tu:
            tan_suat_tu[tu] += 1
        else:
            tan_suat_tu[tu] = 1
    return tan_suat_tu
ket_qua = dem_tan_suat_tu(danh_sach_tu)
print(ket_qua)
