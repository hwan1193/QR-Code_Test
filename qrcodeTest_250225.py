import tkinter  # as Tk 로 별칭 사용 가능. 
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

#################################################################
# tkiner : 표준 라이브러리 사용
# messagebox : 경고 메시지나 알림을 띄우기 위한 tkiner 서브 모듈 사용
# qrcode : qr 코드를 생성하는 외부 라이브러리 사용
# PIL : 이미지 처리 라이브러리 , 생성된 qr코드를 tkiner에서 사용할 수 있도록 변환하는데 사용.
#################################################################

# QR 코드 생성 함수
def generate_qr_code():
    input_text = text_entry.get()  # 텍스트 입력 받기 # 사용자가 입력한 텍스트를 가져옴.
    if not input_text:
        messagebox.showwarning("경고", "QR 코드를 생성할 텍스트를 입력하세요!")     # 텍스트 입력란에 아무것도 기입하지 않을 경우 경고 메시지 띄우고 함수 종료 시킴.
        return

    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )                           # qrcode 라이브러리의 qrcode 객체를 생성함. # version : qr코드 크기 # error_correction : qr 코드 오류 수정 레벨을 말하며, error_correct_l은 오류 수정 비율이 가장 낮음.
                                # box_size : qr코드 내 각 작은 사각형 크기 사용 # border : qr코드의 외부 여백 크기 사용
    qr.add_data(input_text)     # qr.add_data(input_text) 사용자로부터 받은 텍스트를 qr코드에 추가함.
    qr.make(fit=True)           # qr.make(fit=True) qr 코드의 데이터를 맞추어 최적화함.

    # 이미지를 생성하고 PIL 형식으로 변환
    img = qr.make_image(fill='black', back_color='white')   # qr.make_image : 생성된 qr코드를 이미지로 변환함. qr 코드의 색상과 배경 색상을 지정하였음. 
    img.save("qrcode.png")      # img.save("qrcode.png") : 생성된 qr코드를 "qrcode.png"라는 이름으로 저장시킴.

    # 이미지를 Tkinter에서 사용할 수 있게 변환
    img_tk = ImageTk.PhotoImage(img)            # ImageTk.PhotoImage(img) : PIL 이미지 tkniter에서 사용할 수 있는 이미지 객체로 변환 함.
    qr_label.config(image=img_tk)               # 변환된 이미지를 qr_label 위젯에 설정하여 화면에 표시.
    qr_label.image = img_tk  # 이미지를 메모리에 유지해야 합니다.

# Tkinter 윈도우 설정
window = tkinter.Tk()                #tkinter 윈도우 생성함.
window.title("QR 코드 생성기")   # 윈도우의 제목을 "qr코드 생성기"로 설정
window.geometry("400x400")      # 윈도우 크기를 400x400으로 크기 설정함.
window.resizable(False, False)  # 윈도우 크기를 고정하여 사용자가 크기를 조정 못 하도록 설정.

# 입력 텍스트 박스
label = tkinter.Label(window, text="QR 코드로 변환할 텍스트를 입력하세요:", font=("Arial", 12))  #텍스트를 사용자에게 안내하는 역할
label.pack(pady=10) #pady=10을 통해 위아래로 여백을 추가함.

text_entry = tkinter.Entry(window, width=30, font=("Arial", 14))    #tkinter.Entry() : 텍스트를 입력 받을 수 있는 입력란을 생성함. width와 font 크기 조절.
text_entry.pack(pady=10)    #pady=10을 통해 위아래로 여백을 추가함.

# QR 코드 생성 버튼
generate_button = tkinter.Button(window, text="QR 코드 생성", command=generate_qr_code, font=("Arial", 12))
generate_button.pack(pady=20)

#### tk.Button() : qr코드 생성 버튼을 생성 / 버튼 클릭 시 generate_qr_code() 함수를 호출함.

# QR 코드 이미지를 표시할 라벨
qr_label = tkinter.Label(window)
qr_label.pack(pady=10)

# 실행
window.mainloop()