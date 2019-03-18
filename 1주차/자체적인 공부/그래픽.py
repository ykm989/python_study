import tkinter

window = tkinter.Tk()#window 말고ㅗ 다른 이름도 가능

window.title("킹왕짱 헤헤")#타이틀 이름 말 그대로
window.geometry("640x500")#창의 크기
window.resizable(True, True)#상하, 좌우 크기 조절 가능 여

label = tkinter.Label(window, text = "Hello", width=10, height = 5, fg="red", relief = "solid")#윈도우 창에 라벨 위젯을 설정 할 수 있음
#text = 라벨에 표시할 문자열, textvariable = 라벨에 표시할 문자열을 가져올 변수, anchor = 라벨안의 문자열 또는 이미지의 위치
#justify = 라벨의 문자열이 여러 줄 일 경우 정렬 방법(center, left, right) wraplength = 자동 줄내림 설정 너
label.pack()#위젯을 배치할 수 있

window.mainloop()
