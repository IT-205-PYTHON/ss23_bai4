# Module: reports/report_generator.py
# Vai trò: Hiển thị danh sách điểm sinh viên và xuất báo cáo học tập
import datetime
from colorama import init, Fore, Style

from utils.score_utils import calculate_average, classify_student

# Khởi tạo colorama (tự động reset màu sau mỗi lần in)
init(autoreset=True)


def display_student_scores(records):
    """
    Hiển thị danh sách điểm và điểm trung bình của từng sinh viên.
    Input:  records (list) - danh sách dict sinh viên
    Output: None (in kết quả ra terminal)
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for idx, student in enumerate(records, start=1):
        avg = calculate_average(student["scores"])
        classification = classify_student(avg)
        print(
            f"{idx}. [{student['student_id']}] {student['name']:<15} "
            f"| Điểm: {student['scores']} "
            f"| ĐTB: {avg:.2f} - {classification}"
        )
    print("---------------------------------")


def export_learning_report(records):
    """
    Xuất báo cáo học tập ra file .txt, hiển thị thống kê và thông báo thành công.
    Input:  records (list) - danh sách dict sinh viên
    Output: None (ghi file và in kết quả ra terminal)
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    passed = sum(1 for s in records if calculate_average(s["scores"]) >= 5.0)
    need_improve = total - passed

    now = datetime.datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    report_filename = "learning_report.txt"

    # Nội dung báo cáo ghi ra file
    lines = [
        "===== BÁO CÁO HỌC TẬP RIKKEI ACADEMY =====",
        f"Thời gian tạo: {timestamp}",
        "--------------------------------------------",
        f"Tổng số sinh viên     : {total}",
        f"Số SV đạt yêu cầu    : {passed}",
        f"Số SV cần cải thiện  : {need_improve}",
        "--------------------------------------------",
        "Chi tiết từng sinh viên:",
    ]

    for student in records:
        avg = calculate_average(student["scores"])
        classification = classify_student(avg)
        lines.append(
            f"  [{student['student_id']}] {student['name']} "
            f"- ĐTB: {avg:.2f} - {classification}"
        )

    lines.append("============================================")

    with open(report_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Hiển thị thống kê trên terminal
    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số sinh viên đạt yêu cầu: {passed}")
    print(f"Số sinh viên cần cải thiện: {need_improve}")

    # Thông báo thành công bằng màu xanh lá (colorama)
    print(Fore.GREEN + f">> Đã xuất báo cáo ra file {report_filename}")
