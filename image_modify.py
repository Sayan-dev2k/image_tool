import os
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
def set_wh_(im,width_):
    global w,h
    width,height=im.size
    ratio=height/width
    w=int(width_.get())
    h=int(w*ratio)
    
    resized_image=im.resize((w,h))
    return resized_image
def set_wh():
    global w,h,img
    width,height=img.size
    ratio=height/width
    w=int(width_.get())
    h=int(w*ratio)
    height_.config(text=h)
    
    

def bulk_resize():
    global filepath,width_
    files=os.listdir(filepath)
    extensions=['jpg','jpeg','png','jfif']
    fl=filepath.split('/')[-1]
    for f in files:
        ext=f.split('.')[-1]
        if ext in extensions:
            
            im=Image.open(fl+'/'+f)
            img_resized=set_wh_(im,width_)
            filep=f"im/{f}"
            img_resized.save(filep)
    lbl=Label(root,text='IMAGES RESIZED SUCCESSFULLY!!',bg='#FF4500',fg='white',font=('times new roman',15,'bold'))
    lbl.place(x=950,y=450)
def upload_folder():
    global filepath,width_,height_
    filepath=filedialog.askdirectory(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',title='Open a folder')
    wlabel=Label(root,text='Width',font=('times new roman',25,'bold'),bg='#EADDCA')
    wlabel.place(x=530,y=300)
    hlabel=Label(root,text='Height',font=('times new roman',25,'bold'),bg='#EADDCA')
    hlabel.place(x=530,y=350)
    width_=Entry(root,width=10,font=('times new roman',20))
    width_.focus_set()
    width_.place(x=630,y=300)
    height_=Label(root,text='Height will be adjusted according to aspect ratio',bg='white',fg='red',font=('times new roman',20))
    height_.place(x=640,y=350)
    
  
def crop_():
    global img,filepath
    x=int(x_.get())
    y=int(y_.get())
    w=int(width_.get())+x
    h=int(height_.get())+y
    ext=filepath.split('.')[-1]
    img=img.crop(box=(x,y,w,h))
    if(ext=='jpg'):
        file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.jpg')
        img.save(file)    
    else:
        file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.png')
        img.save(file)
    lbl=Label(root,text='IMAGE CROPPED SUCCESSFULLY!!',bg='#FF4500',fg='white',font=('times new roman',15,'bold'))
    lbl.place(x=950,y=450)

def upload_im():
    global img,x_,y_,width_,height_,filepath
    filepath=filedialog.askopenfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',title='Open a file',filetypes=(('image files','*.png'),('all files','*.*')))
    img=Image.open(filepath)
    xlabel=Label(root,text='Position X',font=('times new roman',25,'bold'),bg='#EADDCA')
    xlabel.place(x=300,y=300)
    x_=Entry(root,width=10,font=('times new roman',20))
    x_.focus_set()
    x_.place(x=500,y=300)
    ylabel=Label(root,text='Position Y',font=('times new roman',25,'bold'),bg='#EADDCA')
    ylabel.place(x=700,y=300)
    y_=Entry(root,width=10,font=('times new roman',20))
    y_.focus_set()
    y_.place(x=900,y=300)
    wlabel=Label(root,text='Width',font=('times new roman',25,'bold'),bg='#EADDCA')
    wlabel.place(x=300,y=400)
    width_=Entry(root,width=10,font=('times new roman',20))
    width_.focus_set()
    width_.place(x=500,y=400)
    hlabel=Label(root,text='Height',font=('times new roman',25,'bold'),bg='#EADDCA')
    hlabel.place(x=700,y=400)
    height_=Entry(root,width=10,font=('times new roman',20))
    height_.focus_set()
    height_.place(x=900,y=400)

def upload_img():
    global img,width_,height_,filepath
    filepath=filedialog.askopenfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',title='Open a file',filetypes=(('image files','*.png'),('all files','*.*')))
    img=Image.open(filepath)
    wlabel=Label(root,text='Width',font=('times new roman',25,'bold'),bg='#EADDCA')
    wlabel.place(x=530,y=300)
    hlabel=Label(root,text='Height',font=('times new roman',25,'bold'),bg='#EADDCA')
    hlabel.place(x=530,y=350)
    width_=Entry(root,width=10,font=('times new roman',20))
    width_.focus_set()
    width_.place(x=630,y=300)
    height_=Label(root,width=10,bg='white',font=('times new roman',20))
    height_.place(x=640,y=350)
    setbtn=Button(root,text='SET',font=('times new roman',15),command=set_wh)
    setbtn.place(x=630,y=400)
def resize_():
    global w,h,img,filepath
    ext=filepath.split('.')[-1]
    img=img.resize((w,h),Image.ANTIALIAS)
    if(ext=='jpg'):
        file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.jpg')
        img.save(file)    
    else:
        file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.png')
        img.save(file)
    lbl=Label(root,text='IMAGE RESIZED SUCCESSFULLY!!',bg='#FF4500',fg='white',font=('times new roman',15,'bold'))
    lbl.place(x=950,y=450)
def upload_jpg():
    global img
    filepath=filedialog.askopenfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',title='Open a file',filetypes=(('image files','*.jpg'),('all files','*.*')))
    img=Image.open(filepath)
    
def upload_png():
    global img
    filepath=filedialog.askopenfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',title='Open a file',filetypes=(('image files','*.png'),('all files','*.*')))
    img=Image.open(filepath)
def png_to_jpg():
    global img
    p=img.convert('RGB')
    file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.jpg')
    p.save(file)
    lbl=Label(root,text='CONVERTED TO JPG SUCCESSFULLY!!',bg='#FF4500',fg='white',font=('times new roman',15,'bold'))
    lbl.place(x=950,y=450)
def jpg_to_png():
    global img
    file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.png')
    img.save(file)
    lbl=Label(root,text='CONVERTED TO PNG SUCCESSFULLY!!',bg='#FF4500',fg='white',font=('times new roman',15,'bold'))
    lbl.place(x=950,y=450)
def fun1():
   
    
    title.destroy()
    lbl1.destroy()
    resize.destroy()
    resize_bulk.destroy()
    crop.destroy()
    png_jpg.destroy()
    jpg_png.destroy()
    label.destroy()
    label1.destroy()
    titl=Label(root,text='IMAGE RESIZE',font=('times new roman',25,'bold'),bg='#FFBF00').place(x=0,y=20,relwidth=1)
    upload=Button(root,text='UPLOAD IMAGE',font=('times new roman',20,'bold'),bg='#90EE90',command=upload_img)
    upload.pack(pady=120)
    convert=Button(root,text='RESIZE IMAGE',font=('times new roman',20,'bold'),bg='#90EE90',command=resize_)
    convert.place(x=630,y=200)
    labl1=Label(root,height=300,width=300,bg='white')
    labl1.place(x=630,y=450)
    icon=Image.new("RGB",(400,400),('white'))
    bg1=Image.open('resize_icon.png')
    bg1=bg1.resize((300,300),Image.ANTIALIAS)
    icon.paste(bg1,(50,50))
    icon.save('rsize_icon.png')
    img=ImageTk.PhotoImage(file='rsize_icon.png')
    labl1.config(image=img)
    labl1.image=img

def fun2():
    title.destroy()
    lbl1.destroy()
    resize.destroy()
    resize_bulk.destroy()
    crop.destroy()
    png_jpg.destroy()
    jpg_png.destroy()
    label.destroy()
    label1.destroy()
    titl=Label(root,text='IMAGE RESIZE IN BULK',font=('times new roman',25,'bold'),bg='#FFBF00').place(x=0,y=20,relwidth=1)
    upload=Button(root,text='UPLOAD FOLDER ',font=('times new roman',20,'bold'),bg='#90EE90',command=upload_folder)
    upload.pack(pady=120)
    convert=Button(root,text='RESIZE IMAGES',font=('times new roman',20,'bold'),bg='#90EE90',command=bulk_resize)
    convert.place(x=630,y=200)
    labl1=Label(root,height=300,width=300,bg='white')
    labl1.place(x=630,y=450)
    icon=Image.new("RGB",(400,400),('white'))
    bg1=Image.open('resize_icon.png')
    bg1=bg1.resize((300,300),Image.ANTIALIAS)
    icon.paste(bg1,(50,50))
    icon.save('rsize_icon.png')
    img=ImageTk.PhotoImage(file='rsize_icon.png')
    labl1.config(image=img)
    labl1.image=img
def fun3():
    title.destroy()
    lbl1.destroy()
    resize.destroy()
    resize_bulk.destroy()
    crop.destroy()
    png_jpg.destroy()
    jpg_png.destroy()
    label.destroy()
    label1.destroy()
    titl=Label(root,text='CROP IMAGE',font=('times new roman',25,'bold'),bg='#FFBF00').place(x=0,y=20,relwidth=1)
    upload=Button(root,text='UPLOAD IMAGE',font=('times new roman',20,'bold'),bg='#90EE90',command=upload_im)
    upload.pack(pady=120)
    convert=Button(root,text='CROP',font=('times new roman',20,'bold'),bg='#90EE90',command=crop_)
    convert.place(x=650,y=200)
    labl1=Label(root,height=300,width=300,bg='white')
    labl1.place(x=630,y=450)
    icon=Image.new("RGB",(400,400),('white'))
    bg1=Image.open('crop_icon.png')
    bg1=bg1.resize((300,300),Image.ANTIALIAS)
    icon.paste(bg1,(50,50))
    icon.save('cr_icon.png')
    img=ImageTk.PhotoImage(file='cr_icon.png')
    labl1.config(image=img)
    labl1.image=img
def fun4():
    
    title.destroy()
    lbl1.destroy()
    resize.destroy()
    resize_bulk.destroy()
    crop.destroy()
    png_jpg.destroy()
    jpg_png.destroy()
    label.destroy()
    label1.destroy()
    titl=Label(root,text='CONVERT PNG TO JPG',font=('times new roman',25,'bold'),bg='#FFBF00').place(x=0,y=20,relwidth=1)
    upload=Button(root,text='UPLOAD PNG IMAGE',font=('times new roman',20,'bold'),bg='#90EE90',command=upload_png)
    upload.pack(pady=120)
    convert=Button(root,text='CONVERT TO JPG',font=('times new roman',20,'bold'),bg='#90EE90',command=png_to_jpg)
    convert.place(x=600,y=200)
    frame = Frame(root, width=1000, height=500,bg='yellow',bd=2,relief='solid')
    frame.place(x=250, y=280)
    labl1=Label(frame,height=300,width=300,bg='white')
    labl1.place(x=350,y=100)
    icon=Image.new("RGB",(400,400),('white'))
    bg1=Image.open('pngtjpg.jpg')
    bg1=bg1.resize((300,300),Image.ANTIALIAS)
    icon.paste(bg1,(50,50))
    icon.save('ptj.png')
    img=ImageTk.PhotoImage(file='ptj.png')
    labl1.config(image=img)
    labl1.image=img
def fun5():
    title.destroy()
    lbl1.destroy()
    resize.destroy()
    resize_bulk.destroy()
    crop.destroy()
    png_jpg.destroy()
    jpg_png.destroy()
    label.destroy()
    label1.destroy()
    titl=Label(root,text='CONVERT JPG TO PNG',font=('times new roman',25,'bold'),bg='#FFBF00').place(x=0,y=20,relwidth=1)
    upload=Button(root,text='UPLOAD JPG IMAGE',font=('times new roman',20,'bold'),bg='#90EE90',command=upload_jpg)
    upload.pack(pady=120)
    convert=Button(root,text='CONVERT TO PNG',font=('times new roman',20,'bold'),bg='#90EE90',command=jpg_to_png)
    convert.place(x=600,y=200)
    frame = Frame(root, width=1000, height=500,bg='yellow',bd=2,relief='solid')
    frame.place(x=250, y=280)
    labl1=Label(frame,height=300,width=300,bg='white')
    labl1.place(x=350,y=100)
    icon=Image.new("RGB",(400,400),('white'))
    bg1=Image.open('jpgtpng.png')
    bg1=bg1.resize((300,300),Image.ANTIALIAS)
    icon.paste(bg1,(50,50))
    icon.save('jtp.png')
    img=ImageTk.PhotoImage(file='jtp.png')
    labl1.config(image=img)
    labl1.image=img
    

root=Tk()
root.geometry("1500x800")
root.title("Image modifier")
title=Label(root,text='IMAGE MODIFY TOOL',font=('times new roman',50,'bold'),bg='blue',fg='white',bd=5,relief='solid')
title.place(x=0,y=20,relwidth=1)
root.config(bg='#EADDCA')
lbl1=Label(root,text='CHOOSE AN OPTION',font=('times new roman',25,'bold'),bg='red',fg='white')
lbl1.pack(pady=120)
resize=Button(root,text='RESIZE IMAGE',font=('times new roman',20,'bold'),bg='yellow',command=fun1)
resize.place(x=50,y=200)
resize_bulk=Button(root,text='RESIZE IMAGE IN BULK',font=('times new roman',20,'bold'),bg='yellow',command=fun2)
resize_bulk.place(x=300,y=200)
crop=Button(root,text='CROP IMAGE',font=('times new roman',20,'bold'),bg='yellow',command=fun3)
crop.place(x=700,y=200)
png_jpg=Button(root,text='PNG TO JPG',font=('times new roman',20,'bold'),bg='yellow',command=fun4)
png_jpg.place(x=980,y=200)
jpg_png=Button(root,text='JPG TO PNG',font=('times new roman',20,'bold'),bg='yellow',command=fun5)
jpg_png.place(x=1250,y=200)
# frame = Frame(root, width=600, height=500,bg='violet',bd=2,relief='solid')
# frame.place(x=395, y=270)
label=Label(root,height=300,width=300,bg='white')
label.place(x=350,y=400)
icon=Image.new("RGB",(400,400),('white'))
# draw=ImageDraw.Draw(icon)
bg=Image.open('img.png')
bg=bg.resize((300,300),Image.ANTIALIAS)
icon.paste(bg,(50,50))
icon.save('icon.png')
img=ImageTk.PhotoImage(file='icon.png')
label.config(image=img)
label.image=img
label1=Label(root,height=300,width=300,bg='white')
label1.place(x=850,y=400)
icon=Image.new("RGB",(400,400),('white'))
bg1=Image.open('tool.png')
bg1=bg1.resize((300,300),Image.ANTIALIAS)
icon.paste(bg1,(50,50))
icon.save('ticon.png')
img=ImageTk.PhotoImage(file='ticon.png')
label1.config(image=img)
label1.image=img
root.mainloop()

