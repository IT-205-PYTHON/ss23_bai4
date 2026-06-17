# Module: utils/string_utils.py
# Vai trò: Chuẩn hóa chuỗi tên sinh viên
import re


def normalize_name(name):
    """
    Chuẩn hóa một chuỗi tên:
    - Xóa khoảng trắng đầu/cuối
    - Rút gọn nhiều khoảng trắng giữa từ thành một
    - Viết hoa chữ cái đầu mỗi từ
    Input:  name (str)
    Output: str - tên đã chuẩn hóa
    """
    name = name.strip()
    name = re.sub(r'\s+', ' ', name)
    name = name.title()
    return name


def normalize_student_names(records):
    """
    Chuẩn hóa tên toàn bộ sinh viên trong danh sách.
    Input:  records (list) - danh sách dict sinh viên
    Output: None (cập nhật trực tiếp và in kết quả ra terminal)
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for student in records:
        student["name"] = normalize_name(student["name"])
        print(f"{student['student_id']}: {student['name']}")

    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")
