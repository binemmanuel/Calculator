import re
import tkinter as tk

root = tk.Tk()

HEIGHT = 500
WIDTH = 400

lf_bg_color = '#505050'
lr_bg_color = lf_bg_color

lf_btn_bg_color = '#808080'
rf_btn_bg_color = '#353535'

rf_btn_color = '#fff'
lf_btn_color = '#fff'


def get_btn(btn, input_field):
    if input_field['text'] == '':
        input_field['text'] = btn
    else:
        if str(input_field['text'])[-1] != '.' or btn != '.':
            input_field['text'] = str(input_field['text']) + str(btn)


def back_space(input_field):
    result = str(input_field['text'])
    input_field['text'] = result[0: -1]


def clear(input_field):
    input_field['text'] = ''


def sub(f_operand, s_operand):
    return f_operand - s_operand


def multiply(f_operand, s_operand):
    return f_operand * s_operand


def div(f_operand, s_operand):
    return f_operand / s_operand


def cal(input_field):
    try:
        if len(str(input_field['text'])) > 1:
            result = ''

            match = re.search(r'(\+)|(\-)|(\*)|(/)', str(input_field['text']))

            operator = match.group()

            print(operator)

            operands = input_field['text'].split(operator)

            f_operand = float(operands[0])
            s_operand = float(operands[1])

            if operator == '+':
                result = sum([f_operand, s_operand])

            elif operator == '-':
                result = sub(f_operand, s_operand)

            elif operator == '*':
                result = multiply(f_operand, s_operand)

            elif operator == '/':
                result = div(f_operand, s_operand)

            str_result = str(result)

            # Display just the first 11 numbers if the number is > 12
            if len(str(result)) > 12:
                result = str_result[0:11]

            # Display the result
            if str(result)[-1] == '0':
                input_field['text'] = int(result)
            else:
                input_field['text'] = result
    except:
        input_field['text'] = 'Syntax Error'


canvas = tk.Canvas(height=HEIGHT, width=WIDTH)
canvas.pack()

# Upper frame contains the input field.
upper_frame = tk.Frame(root, bg='#969696', bd=3)
upper_frame.place(relx=0.01, rely=0.04, relwidth=0.98, relheight=0.17)

input_field = tk.Label(upper_frame, bg='#fff', font=('Courier', 40), bd=0, anchor='e', justify='right')
input_field.place(relheight='1', relwidth='1')

# Lower frame contains the cal buttons.
lower_left_frame = tk.Frame(root, bg=lf_bg_color, bd=3)
lower_left_frame.place(relx=0.40, rely=0.25, relwidth=0.79, relheight=0.7, anchor='n')

# Cal buttons.
# First Row.
btn = tk.Button(lower_left_frame, font=50, bg=rf_btn_bg_color, fg=rf_btn_color, text='CL', bd=0,
                command=lambda: clear(input_field))
btn.place(rely=0.001, relheight=0.08, relwidth=1)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='7',
                command=lambda: get_btn(7, input_field))
btn.place(relx=0.01, rely=0.09, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='8',
                command=lambda: get_btn(8, input_field))
btn.place(relx=0.34, rely=0.09, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='9',
                command=lambda: get_btn(9, input_field))
btn.place(relx=0.67, rely=0.09, relheight=0.2, relwidth=0.32)

# Second Row.
btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='4',
                command=lambda: get_btn(4, input_field))
btn.place(relx=0.01, rely=0.3, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='5',
                command=lambda: get_btn(5, input_field))
btn.place(relx=0.34, rely=0.3, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='6',
                command=lambda: get_btn(6, input_field))
btn.place(relx=0.67, rely=0.3, relheight=0.2, relwidth=0.32)

# Third Row.
btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='1',
                command=lambda: get_btn(1, input_field))
btn.place(relx=0.01, rely=0.51, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='2',
                command=lambda: get_btn(2, input_field))
btn.place(relx=0.34, rely=0.51, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='3',
                command=lambda: get_btn(3, input_field))
btn.place(relx=0.67, rely=0.51, relheight=0.2, relwidth=0.32)

# Fourth Row.
btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='.',
                command=lambda: get_btn('.', input_field))
btn.place(relx=0.01, rely=0.719, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='0',
                command=lambda: get_btn(0, input_field))
btn.place(relx=0.34, rely=0.719, relheight=0.2, relwidth=0.32)

btn = tk.Button(lower_left_frame, bg=lf_btn_bg_color, fg=lf_btn_color, bd=0, font=50, text='=',
                command=lambda: cal(input_field))
btn.place(relx=0.67, rely=0.719, relheight=0.2, relwidth=0.32)

# Right Fame
lower_right_frame = tk.Frame(root, bg=lr_bg_color, bd=3)
lower_right_frame.place(relx=0.89, rely=0.25, relwidth=0.20, relheight=0.7, anchor='n')

btn = tk.Button(lower_right_frame, font=50, bg=rf_btn_bg_color, fg=rf_btn_color, text='C', bd=0,
                command=lambda: back_space(input_field))
btn.place(rely=0.001, relheight=0.20, relwidth=1)

btn = tk.Button(lower_right_frame, font=50, bg=rf_btn_bg_color, fg=rf_btn_color, text='/', bd=0,
                command=lambda: get_btn('/', input_field))
btn.place(rely=0.209, relheight=0.19, relwidth=1)

btn = tk.Button(lower_right_frame, font=50, bg=rf_btn_bg_color, fg=rf_btn_color, text='*', bd=0,
                command=lambda: get_btn('*', input_field))
btn.place(rely=0.409, relheight=0.19, relwidth=1)

btn = tk.Button(lower_right_frame, font=50, bg=rf_btn_bg_color, fg=rf_btn_color, text='-', bd=0,
                command=lambda: get_btn('-', input_field))
btn.place(rely=0.609, relheight=0.19, relwidth=1)

btn = tk.Button(lower_right_frame, font=50, bg=rf_btn_bg_color, fg=rf_btn_color, text='+', bd=0,
                command=lambda: get_btn('+', input_field))
btn.place(rely=0.81, relheight=0.19, relwidth=1)

root.mainloop()
