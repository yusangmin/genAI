import tkinter as tk
from tkinter import messagebox
import random

# 로또 번호 생성 함수
def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)

# 버튼 클릭 이벤트 핸들러 함수
def generate_numbers():
    lotto_numbers = generate_lotto_numbers()
    messagebox.showinfo("로또 번호", "생성된 로또 번호는 {} 입니다.".format(lotto_numbers))

# tkinter 윈도우 생성
window = tk.Tk()
window.title("로또 번호 생성기")

# 버튼 생성
button = tk.Button(window, text="로또 번호 생성", command=generate_numbers)
button.pack(pady=10)

# 윈도우 실행
window.mainloop()