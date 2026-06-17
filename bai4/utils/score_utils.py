# Module: utils/score_utils.py
# Vai trò: Tính toán điểm trung bình và phân loại học lực sinh viên


def calculate_average(scores):
    """
    Tính điểm trung bình từ danh sách điểm.
    Input:  scores (list) - danh sách điểm (có thể rỗng hoặc chứa giá trị không hợp lệ)
    Output: float - điểm trung bình, trả về 0.0 nếu không có điểm hợp lệ
    """
    # Lọc chỉ lấy các giá trị là số hợp lệ (int hoặc float)
    valid_scores = [s for s in scores if isinstance(s, (int, float))]

    if not valid_scores:
        return 0.0

    return sum(valid_scores) / len(valid_scores)


def classify_student(average):
    """
    Phân loại học lực dựa trên điểm trung bình.
    Input:  average (float) - điểm trung bình
    Output: str - xếp loại học lực
    """
    if average >= 8.0:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"
