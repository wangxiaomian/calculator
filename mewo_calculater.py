import tkinter as tk
window = tk.Tk()
window.title('小猫猫的计算器')
window.geometry('500x500')

text = '喜欢'
iCnt = 0
def print_text():
	global iCnt
	iCnt += 1
	print(text+iCnt*'!')

a = tk.Button(window,text = '请戳我',command = print_text)


#######
'''
e = tk.Entry(window)
e.pack()

def insert_point():
	var = e.get()
	t1.insert('insert',var)

def insert_end():
	var = e.get()
	t1.insert('end',var)

b1 = tk.Button(window,text = 'insert point',command = insert_point)
b1.pack()

b2 = tk.Button(window,text = 'insert end',command = insert_end)
b2.pack()

t1 = tk.Text(window,height = 2)
t1.pack()
'''
#####

numStr = ''
float_sig = False
num1 = None
num2 = None
opt = None

def f0():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '0'
	t1.insert('end','0')

def f1():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '1'
	t1.insert('end','1')


def f2():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '2'
	t1.insert('end','2')

def f3():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '3'
	t1.insert('end','3')

def f4():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '4'
	t1.insert('end','4')

def f5():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '5'
	t1.insert('end','5')

def f6():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '6'
	t1.insert('end','6')

def f7():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '7'
	t1.insert('end','7')

def f8():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '8'
	t1.insert('end','8')

def f9():
	global numStr
	if num1 is not None and not numStr:
		float_sig = False
		t1.delete('1.0','end')
	numStr += '9'
	t1.insert('end','9')

def f_point():
	global numStr
	global float_sig
	if num1 is not None and not numStr:
		t1.delete('1.0','end')
	numStr += '.'
	float_sig = True
	t1.insert('end','.')







def opt_plus():
	global num1
	global num2
	global numStr
	global opt

	if numStr:
		if num1:
			if float_sig:
				num2 = float(numStr)
			else:
				num2 = int(numStr)
			numStr = ''
		else:
			if float_sig:
				num1 = float(numStr)
			else:
				num1 = int(numStr)
			numStr = ''
	if num1 and num2:
		opt_equal()
	opt = '+'

	

def opt_minus():
	global num1
	global num2
	global numStr
	global opt

	if numStr:
		if num1:
			if float_sig:
				num2 = float(numStr)
			else:
				num2 = int(numStr)
			numStr = ''
		else:
			if float_sig:
				num1 = float(numStr)
			else:
				num1 = int(numStr)
			numStr = ''
	if num1 and num2:
		opt_equal()
	opt = '-'
	

def opt_mult():
	global num1
	global num2
	global numStr
	global opt

	if numStr:
		if num1:
			if float_sig:
				num2 = float(numStr)
			else:
				num2 = int(numStr)
			numStr = ''
		else:
			if float_sig:
				num1 = float(numStr)
			else:
				num1 = int(numStr)
			numStr = ''
	if num1 and num2:
		opt_equal()
	opt = '*'
	

def opt_divi():
	global num1
	global num2
	global numStr
	global opt

	if numStr:
		if num1:
			if float_sig:
				num2 = float(numStr)
			else:
				num2 = int(numStr)
			numStr = ''
		else:
			if float_sig:
				num1 = float(numStr)
			else:
				num1 = int(numStr)
			numStr = ''
	if num1 and num2:
		opt_equal()
	opt = '/'

def opt_mod():
	global num1
	global num2
	global numStr
	global opt

	if numStr:
		if num1:
			if float_sig:
				num2 = float(numStr)
			else:
				num2 = int(numStr)
			numStr = ''
		else:
			if float_sig:
				num1 = float(numStr)
			else:
				num1 = int(numStr)
			numStr = ''
	if num1 and num2:
		opt_equal()
	opt = '%'


def opt_equal():
	global num1
	global num2
	global numStr
	global float_sig
	# 如果nusStr有数字，放到num2中
	if numStr:
		if not num1:
			if float_sig:
				num1 = float(numStr)
			else:
				num1 = int(numStr)
		else:
			if float_sig:
				num2 = float(numStr)
			else:
				num2 = int(numStr)
		numStr = ''

	# 如果numstr没数字，归零
	elif not num1 or not num2:
		opt_ac()


	if num1 and num2:
		t1.delete('1.0','end')
		x = None

		if opt == '+':
			x = num1+num2
			t1.insert('insert',x)

		elif opt == '-':
			x = num1 - num2
			t1.insert('insert',x)

		elif opt == '*':
			x = num1 * num2
			t1.insert('insert',x)

		elif opt == '/':

			if num1 % num2 == 0:
				x = num1 // num2
			else:
				x = num1 / num2
			t1.insert('insert',x)

		elif opt == '%':
			x = num1 % num2
			t1.insert('insert',x)
		num1 = x 
		num2 = None


def opt_ac():
	global num1
	global num2
	global numStr
	global float_sig
	numStr = ''
	num1 = None
	num2 = None
	float_sig = False
	t1.delete('1.0','end')


b_point = tk.Button(window,text = '.',width = 2,height = 2,command = f_point)
b_point.pack()
b_point.place(x = 150,y = 400)


b0 = tk.Button(window,text = '0',width = 7,height = 2,command = f0)
b0.pack()
b0.place(x=50,y=400)

b1 = tk.Button(window,text = '1',width = 2,height = 2,command = f1)
b1.pack()
b1.place(x=50,y=350)

b2 = tk.Button(window,text = '2',width = 2,height = 2,command = f2)
b2.pack()
b2.place(x=100,y=350)

b3 = tk.Button(window,text = '3',width = 2,height = 2,command = f3)
b3.pack()
b3.place(x = 150,y = 350)


b4 = tk.Button(window,text = '4',width = 2,height = 2,command = f4)
b4.pack()
b4.place(x = 50,y=300)

b5 = tk.Button(window,text = '5',width = 2,height = 2,command = f5)
b5.pack()
b5.place(x = 100,y = 300)

b6 = tk.Button(window,text = '6',width = 2,height = 2,command = f6)
b6.pack()
b6.place(x = 150,y = 300)

b7 = tk.Button(window,text = '7',width = 2,height = 2,command = f7)
b7.pack()
b7.place(x = 50,y = 250)

b8 = tk.Button(window,text = '8',width = 2,height = 2,command = f8)
b8.pack()
b8.place(x = 100,y = 250)

b9 = tk.Button(window,text = '9',width = 2,height = 2,command = f9)
b9.pack()
b9.place(x = 150,y = 250)


opt_plus_button = tk.Button(window,text = '+',width = 2,height = 2,command = opt_plus)
opt_plus_button.pack()
opt_plus_button.place(x = 200,y = 350)

opt_minus_button = tk.Button(window,text = '-',width = 2,height = 2,command = opt_minus)
opt_minus_button.pack()
opt_minus_button.place(x = 200,y = 300)

opt_mult_button = tk.Button(window,text = '*',width = 2,height = 2,command = opt_mult)
opt_mult_button.pack()
opt_mult_button.place(x = 200,y = 250)

opt_divi_button = tk.Button(window,text = '/',width = 2,height = 2,command = opt_divi)
opt_divi_button.pack()
opt_divi_button.place(x = 200,y = 200)

opt_mod_button = tk.Button(window,text = '%',width = 2,height = 2,command = opt_mod)
opt_mod_button.pack()
opt_mod_button.place(x = 150,y = 200)


opt_equal_button = tk.Button(window,text = '=',width = 2,height = 2,command = opt_equal)
opt_equal_button.pack()
opt_equal_button.place(x = 200,y = 400)

opt_ac_button = tk.Button(window,text = 'AC',width = 7,height = 2,command = opt_ac)
opt_ac_button.pack()
opt_ac_button.place(x = 50,y = 200)


t1 = tk.Text(window,height = 3)
t1.pack()
t1.place(x = 50,y = 100)





window.mainloop()