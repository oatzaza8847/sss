import tkinter as tk

def khawoat():
    Wi_Wi = int(W_input.get())
    H = int(H_input.get())
    A = int(A_input.get())
    S = str(S_input.get())

    water = ''
    water = 'นำ้ที่ควรได้รับต่อวัน : '+str((Wi_Wi * 2.2 *30/2)/1000) + ' ลิตร'
    output_label_1.configure(text=water,fg='#FFF',bg='#7f9a8b')

    if S == 'ชาย':
        cal = ''
        cal = 'พลังงานที่ควรได้รับต่อวัน : '+str(66+(13.7 * Wi_Wi)+(5 * H) - (6.8 * A)) + ' กิโลแคลอรี่'
        output_label_2.configure(text=cal,fg='#FFF',bg='#7f9a8b')
    if S == 'หญิง':
        cal = ''
        cal = 'พลังงานที่ควรได้รับต่อวัน : ' + str(665 + (9.6 * Wi_Wi) + (1.8 * H) - (4.7 * A)) + ' กิโลแคลอรี่'
        output_label_2.configure(text=cal,fg='#FFF',bg='#7f9a8b')



window = tk.Tk()
window.title('KHAWOAT')
window.minsize(width=500, height=500)

top_label = tk.Label(master=window, text='CALORIE AND WATER',font=('Times','30','bold'))
top_label.pack(pady=20)

W_label = tk.Label(master=window, text='นำ้หนัก')
W_label.pack(fill=tk.Y)
W_input = tk.Entry(master=window)
W_input.pack(fill=tk.Y)

H = tk.Label(master=window, text='ส่วนสูง')
H.pack()
H_input = tk.Entry(master=window)
H_input.pack()

A_label = tk.Label(master=window, text='อายุ')
A_label.pack()
A_input = tk.Entry(master=window)
A_input.pack()

S_label = tk.Label(master=window, text='ชาย/หญิง')
S_label.pack()
S_input = tk.Entry(master=window)
S_input.pack()
image = tk.PhotoImage(file='click.png')
button = tk.Button(
    master=window, text='CLICK',
    command=khawoat,width=300, height=100,pady=5,image=image
)
button.pack(pady=10)

output_label_1= tk.Label(master=window,font=('','15'))
output_label_1.pack(pady=5)
output_label_2= tk.Label(master=window,font=('','15'))
output_label_2.pack()


window.mainloop()