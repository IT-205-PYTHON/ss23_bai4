# main.py - Điểm khởi động chương trình Hệ Thống Tiện Ích Học Tập Rikkei Academy

from data.students import student_records
from utils import normalize_student_names, generate_assignment_code
from reports import display_student_scores, export_learning_report


def show_menu():
    """Hiển thị menu chính của chương trình."""
    print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
    print("1. Xem danh sách sinh viên và điểm trung bình")
    print("2. Chuẩn hóa tên sinh viên")
    print("3. Sinh mã bài tập ngẫu nhiên")
    print("4. Xuất báo cáo học tập")
    print("5. Thoát chương trình")
    print("====================================================")


def main():
    """
    Hàm chính điều phối toàn bộ chương trình.
    Sử dụng vòng lặp while True để hiển thị menu liên tục đến khi người dùng thoát.
    """
    while True:
        show_menu()

        try:
            choice = input("Chọn chức năng (1-5): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nCảm ơn bạn đã sử dụng hệ thống!")
            break

        if choice == "1":
            display_student_scores(student_records)

        elif choice == "2":
            normalize_student_names(student_records)

        elif choice == "3":
            code = generate_assignment_code()
            print("\n--- SINH MÃ BÀI TẬP ---")
            print(f"Mã bài tập của bạn là: {code}")

        elif choice == "4":
            export_learning_report(student_records)

        elif choice == "5":
            print("\nCảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("\nChức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()
