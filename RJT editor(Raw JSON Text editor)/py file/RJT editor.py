# coding:UTF-8
import os
from turtle import title
try:
    import tkinter as tk
    from tkinter import Checkbutton, font as tkFont
    from tkinter import ttk
    from tkinter.colorchooser import askcolor
    from tkinter import messagebox
except:
    os.system('pip install tkinter')
    import tkinter as tk
    from tkinter import Checkbutton, font as tkFont
    from tkinter import ttk
    from tkinter.colorchooser import askcolor
    from tkinter import messagebox
import json
try:
    import pyperclip
except:
    os.system('pip install pyperclip')
    import pyperclip


text = ''
color = ''
font_ = ''
bold = False
italic = False
underlined = False
strikethrough = False
obfuscated = False
clickEvent = {'action': '', 'value': ''}
hoverEvent = {'action': '', 'contents': ''}
outPut = {}


def setEmpty(row_, column_, width_=10, height_=10, sep_=True):
    empty = tk.Canvas(width=width_, height=height_)
    empty.grid(row=row_, column=column_)
    if sep_ == True:
        sep = tk.Canvas(bg="dark gray", height=1)
        sep.grid(row=row_, column=column_, columnspan=3, sticky='we')


def choose_color_(event):
    global choose_color, color_get
    if choose_color.get() == '-[自定义颜色]-':
        color_get = str(askcolor(title='颜色选择')[1])
        if '#' not in str(color_get):
            choose_color.set('白色')
            color_get = 'white'
        else:
            choose_color.set('-[自定义颜色]-:'+color_get)
    else:
        color_get = {'黑色': 'black', '白色': 'white', '深蓝色': 'dark_blue', '浅蓝色': 'blue', '深绿色': 'dark_green', '浅绿色': 'green', '深青色': 'dard_aqua', '浅青色': 'aqua',
                     '深红色': 'dark_red', '浅红色': 'red', '深紫色': 'purple', '浅紫色': 'light_purple', '金色': 'gold', '灰色': 'gray', '深灰色': 'dark_gray', '黄色': 'yellow'}[choose_color.get()]


def choose_font_(event):
    global choose_font, font_get
    font_get = {'默认字体': 'minecraft:default', '强制unicode字体': 'minecraft:uniform',
                '标准银河字母': 'minecraft:alt', 'Dungeons符文字体': 'minecraft:illageralt'}[choose_font.get()]


def required_(event):
    required.post(event.x_root, event.y_root)


def setDefault():
    bold_.set(0)
    underlined_.set(0)
    italic_.set(0)
    obfuscated_.set(0)
    strikethrough_.set(0)


def undoDefault():
    if str(bold_.get()) == '1' or str(underlined_.get()) == '1' or str(italic_.get()) == '1' or str(obfuscated_.get()) == '1' or str(strikethrough_.get()) == '1':
        default_.set(0)
        obfuscated_.set(0)


def undoObfuscated():
    bold_.set(0)
    underlined_.set(0)
    italic_.set(0)
    strikethrough_.set(0)
    default_.set(0)


def choose_click_press(*args):
    helpText = {'跳转到[数值]的超链接': '超链接的url', '运行命令(无权限限制)': '运行的命令', '打开聊天页面并输入[数值]': '要输入的文本',
                '跳转第[数值]页(仅成书有效)': '要跳转的页数', '将[数值]复制到剪贴板': '要复制的文本'}[ClickEventTypeChoose.get()]
    if helpText == '运行的命令':
        tipClick.config(text='数值:  '+helpText)
        ClickEventValue.insert(0, '/')
    else:
        tipClick.config(text='数值:  '+helpText)
        if ClickEventValue.get()[0:1] == '/':
            ClickEventValue.delete(0)


def clickEvent_press():
    if str(useClick.get()) == '0':
        ClickEventTypeChoose['state'] = 'disabled'
        tipClick['state'] = 'disabled'
        ClickEventValue['state'] = 'disabled'
        tipClickEventType['state'] = 'disabled'
    else:
        ClickEventTypeChoose['state'] = 'readonly'
        tipClick['state'] = 'abled'
        ClickEventValue['state'] = 'abled'
        tipClickEventType['state'] = 'abled'


def HoverEvent_press():
    if str(useHover.get()) == '0':
        HoverEventTypeChoose['state'] = 'disables'
        tipHover['state'] = 'disabled'
        HoverEventValue['state'] = 'disabled'
        tipHoverEventType['state'] = 'disabled'
    else:
        HoverEventTypeChoose['state'] = 'readonly'
        tipHover['state'] = 'abled'
        HoverEventValue['state'] = 'abled'
        tipHoverEventType['state'] = 'abled'


def Spawn():
    global text, color, font_, bold, italic, underlined, strikethrough, obfuscated, clickEvent, hoverEvent, outPut
    raw_font = choose_font.get()
    text = rawString.get()
    color = color_get
    font_ = font_get
    if str(default_.get()) != 'default':
        if str(bold_.get()) == '1':
            bold = True
        if str(italic_.get()) == '1':
            italic = True
        if str(underlined_.get()) == '1':
            underlined = True
        if str(strikethrough_.get()) == '1':
            strikethrough = True
        if str(obfuscated_.get()) == '1':
            obfuscated = True
        outPut = {'text': text, 'color': color, 'font': font_, 'bold': bold, 'italic': italic,
                  'underlined': underlined, 'strikethrough': strikethrough, 'obfuscated': obfuscated}
    else:
        outPut = {'text': text, 'color': color}
    if str(useClick.get()) == '1':
        clickEvent['action'] = {'跳转到[数值]的超链接': 'open_url', '运行命令(无权限限制)': 'run_command', '打开聊天页面并输入[数值]': 'suggest_command',
                                '跳转第[数值]页(仅成书有效)': 'change_page', '将[数值]复制到剪贴板': 'copy_to_clipboard'}[ClickEventTypeChoose.get()]
        clickEvent['value'] = ClickEventValue.get()
        outPut.update({'clickEvent': clickEvent})
    if str(useHover.get()) == '1':
        hoverEvent['action'] = {'显示文本': 'show_text'}[
            HoverEventTypeChoose.get()]
        hoverEvent['contents'] = HoverEventValue.get()
        outPut.update({'hoverEvent': hoverEvent})
    outPutJson = json.dumps(outPut)
    try:
        pyperclip.copy(outPutJson)
        messagebox.showinfo(title='提示', message='复制成功!')
    except:
        messagebox.showerror(title='错误', message='未知错误,复制不成功!')
    choose_font.set(raw_font)


root = tk.Tk()
root.resizable(False, False)
root.title('RJT editor for Minecraft Java Edition')
root.iconbitmap('icon.ico')

tipFont = tkFont.Font(family='等线', size=13)
entryFont = tkFont.Font(family='等线', size=20)

required = tk.Menu(root, tearoff='off')
required.add_command(label='这是一个必选标签', font=tipFont)


setEmpty(0, 0, sep_=False)

tipClickEventType = ttk.Label(text='原始字符串*:', font=tipFont)
tipClickEventType.grid(row=1, column=1, sticky='w')
tipClickEventType.bind('<Enter><Button-3>', required_)

rawString = ttk.Entry(width=31, font=entryFont)
rawString.grid(row=2, column=1, sticky='w,e')

setEmpty(3, 0)
setEmpty(1, 2, sep_=False)

tipClickEventType = ttk.Label(text='颜色选择*:', font=tipFont)
tipClickEventType.grid(row=4, column=1, sticky='w')
tipClickEventType.bind('<Enter><Button-3>', required_)

colors = tk.StringVar()  # 窗体自带的文本，新建一个值
choose_color = ttk.Combobox(
    width=30, textvariable=colors, state='readonly', font=entryFont)  # 初始化
choose_color["values"] = ('白色', '黑色', '深蓝色', '浅蓝色', '深绿色',
                          '浅绿色', '深青色', '浅青色', '深红色', '浅红色', '深紫色', '浅紫色', '金色', '灰色', '深灰色', '黄色', '-[自定义颜色]-')
choose_color.current(0)
choose_color.bind('<<ComboboxSelected>>', choose_color_)
choose_color.set('白色')
color_get = 'black'
choose_color.grid(row=5, column=1, sticky='w,e')

setEmpty(6, 0)

tipClickEventType = ttk.Label(text='字体选择*:', font=tipFont)
tipClickEventType.grid(row=7, column=1, sticky='w')
tipClickEventType.bind('<Enter><Button-3>', required_)

font_ = tk.StringVar()  # 窗体自带的文本，新建一个值
choose_font = ttk.Combobox(width=30, textvariable=font_,
                           state='readonly', font=entryFont)  # 初始化
choose_font["values"] = ('默认字体', '强制unicode字体', '标准银河字母', 'Dungeons符文字体')
choose_font.current(1)
choose_font.bind('<<ComboboxSelected>>', choose_font_)
choose_font.set('默认字体')
font_get = 'minecraft:default'
choose_font.grid(row=8, column=1, sticky='w,e')

setEmpty(9, 0)

default_ = tk.StringVar()
default_.set(0)
choose_default = tk.Radiobutton(
    text='正常', font=tipFont, variable=default_, value='default', command=setDefault)
choose_default.grid(row=10, column=1, sticky='w')
default_.set('default')

italic_ = tk.StringVar()
italic_.set(0)
choose_italic = tk.Checkbutton(
    text='斜体', font=tipFont, variable=italic_, onvalue=True, offvalue=False, command=undoDefault)
choose_italic.grid(row=10, column=1)

underlined_ = tk.StringVar()
underlined_.set(0)
choose_underlined = tk.Checkbutton(
    text='下划线', font=tipFont, variable=underlined_, onvalue=True, offvalue=False, command=undoDefault)
choose_underlined.grid(row=10, column=1, sticky='e')

strikethrough_ = tk.StringVar()
strikethrough_.set(0)
choose_strikethrough = tk.Checkbutton(
    text='删除线', font=tipFont, variable=strikethrough_, onvalue=True, offvalue=False, command=undoDefault)
choose_strikethrough.grid(row=11, column=1, sticky='e')

bold_ = tk.StringVar()
bold_.set(0)
choose_bold = tk.Checkbutton(
    text='加粗', font=tipFont, variable=bold_, onvalue=True, offvalue=False, command=undoDefault)
choose_bold.grid(row=11, column=1)

obfuscated_ = tk.StringVar()
obfuscated_.set(0)
choose_obfuscated = tk.Radiobutton(
    text='混淆处理', font=tipFont, variable=obfuscated_, value=1, command=undoObfuscated)
choose_obfuscated.grid(row=11, column=1, sticky='w')

setEmpty(12, 0)

useClick = tk.StringVar()
choose_click = Checkbutton(
    text='启用点击文本事件', font=tipFont, variable=useClick, onvalue=True, offvalue=False, command=clickEvent_press)
choose_click.grid(row=13, column=1, sticky='w')
useClick.set(0)

tipClickEventType = ttk.Label(text='点击事件类型选择:', font=tipFont)
tipClickEventType.grid(row=14, column=1, sticky='w')
tipClickEventType['state'] = 'disabled'

ClickEventType = tk.StringVar()
ClickEventTypeChoose = ttk.Combobox(
    width=30, textvariable=ClickEventType, state='readonly', font=entryFont)
ClickEventTypeChoose['values'] = (
    '跳转到[数值]的超链接', '运行命令(无权限限制)', '打开聊天页面并输入[数值]', '跳转到第[数值]页(仅在成书中生效)', '将[数值]复制到剪贴板')
choose_font.current(0)
ClickEventTypeChoose.bind('<<ComboboxSelected>>', choose_click_press)
ClickEventType.set('')
ClickEventTypeChoose['state'] = 'disabled'
ClickEventTypeChoose.set('')
ClickEventTypeChoose.grid(row=15, column=1, sticky='w,e')

tipClick = ttk.Label(text='数值:', font=tipFont)
tipClick.grid(row=16, column=1, sticky='w')
tipClick['state'] = 'disabled'

ClickEventValue = ttk.Entry(width=31, font=entryFont)
ClickEventValue.grid(row=17, column=1, sticky='w,e')
ClickEventValue['state'] = 'disabled'

setEmpty(18, 0)

useHover = tk.StringVar()
choose_Hover = Checkbutton(
    text='启用鼠标悬停显示', font=tipFont, variable=useHover, onvalue=True, offvalue=False, command=HoverEvent_press)
choose_Hover.grid(row=19, column=1, sticky='w')
useHover.set(0)

tipHoverEventType = ttk.Label(text='点击显示类型选择:', font=tipFont)
tipHoverEventType.grid(row=20, column=1, sticky='w')
tipHoverEventType['state'] = 'disabled'

HoverEventType = tk.StringVar()
HoverEventTypeChoose = ttk.Combobox(
    width=30, textvariable=HoverEventType, state='disabled', font=entryFont)
HoverEventTypeChoose['values'] = ('显示文本')
HoverEventTypeChoose.grid(row=21, column=1, sticky='w,e')
HoverEventType.set('')

tipHover = ttk.Label(text='文本:', font=tipFont)
tipHover.grid(row=22, column=1, sticky='w')
tipHover['state'] = 'disabled'

HoverEventValue = ttk.Entry(width=31, font=entryFont)
HoverEventValue.grid(row=23, column=1, sticky='w,e')
HoverEventValue['state'] = 'disabled'

setEmpty(24, 0)

Spawn = tk.Button(font=entryFont, text='生成并复制', height=2, command=Spawn)
Spawn.grid(row=25, column=1, sticky='we')

setEmpty(26, 0, sep_=False)

root.mainloop()
