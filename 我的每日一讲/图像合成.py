import imageio
import glob
import re
def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))#将图片保存为gif的帧
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.3) #设置格式 速度
    return
def find_all_png():
    png_filenames = glob.glob(r"C:\Users\Administrator\Desktop\我的每日一讲\2\*.png")
    buf = []
    for png_file in png_filenames:
        buf.append(png_file)
    return buf
if __name__ == '__main__':
    buff = find_all_png()
    create_gif(buff, '2.gif')