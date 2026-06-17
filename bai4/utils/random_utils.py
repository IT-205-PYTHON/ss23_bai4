# Module: utils/random_utils.py
# Vai trò: Sinh mã bài tập ngẫu nhiên
import random
import string


def generate_assignment_code():
    """
    Sinh mã bài tập ngẫu nhiên theo định dạng: PY-[4 ký tự chữ hoa hoặc số]
    Input:  Không có
    Output: str - mã bài tập, ví dụ: PY-A8K2
    """
    characters = string.ascii_uppercase + string.digits
    suffix = ''.join(random.choices(characters, k=4))
    return f"PY-{suffix}"
