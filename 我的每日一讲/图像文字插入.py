from PIL import Image,ImageDraw,ImageFont
old_img = Image.open(r"C:\Users\Administrator\Desktop\ll\56\1.png")
X,Y = old_img.size # 输出图片的大小
new_image = old_img.resize((240,240),Image.ANTIALIAS).transpose(Image.ROTATE_90) # 图片旋转
draw = ImageDraw.Draw(new_image)
newfont=ImageFont.truetype('simkai.ttf',40) # 设置图片文字，字体类型，以及字体大小
draw.text((40,150),"我来了",font=newfont,fill="black")#draw.txt：向图片中写入文字，x,y是确定写入文字的位置，font文字大小，file字体颜色
new_image.show()
