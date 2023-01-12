from PIL import ImageFont, ImageDraw, Image
from PIL import Image, ImageTk
import cv2  
import numpy as np

def img_price_daily(gold_a,gold_b,gold965_a,gold965_b,money_a,money_b,date):
    date_x = 155
    date_y = 375

    golda_x = 240
    golda_y = 1050

    goldb_x = 250
    goldb_y = 1310

    gold965a_x = 760
    gold965a_y = 1050

    gold965b_x = 760
    gold965b_y = 1310

    moneya_x = 1330
    moneya_y = 1050

    moneyb_x = 1330
    moneyb_y = 1310

    image = cv2.imread(r'C:\Users\supachai\Desktop\daily\img\image2.png')  
    cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
    pil_im = Image.fromarray(cv2_im_rgb)  
    draw = ImageDraw.Draw(pil_im)
    fontpartmilktea = (r'C:\Users\supachai\Desktop\daily\font\milktea-normal.ttf')

    font1 = ImageFont.truetype(fontpartmilktea, 58)
    font2 = ImageFont.truetype(fontpartmilktea, 85)
    
    draw.text((date_x, date_y), date, font=font2, fill=(0,0,0,0))
    
    draw.text((golda_x, golda_y), gold_a, font=font1, fill=(0,0,0,0))
    draw.text((goldb_x, goldb_y), gold_b, font=font1, fill=(0,0,0,0))

    draw.text((gold965a_x, gold965a_y), gold965_a, font=font1, fill=(0,0,0,0))
    draw.text((gold965b_x, gold965b_y), gold965_b, font=font1, fill=(0,0,0,0))

    draw.text((moneya_x, moneya_y), money_a, font=font1, fill=(0,0,0,0))
    draw.text((moneyb_x, moneyb_y), money_b, font=font1, fill=(0,0,0,0))
    
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    width = 1040
    height = 1040
    dim = (width, height)
    resized = cv2.resize(cv2_im_processed, dim, interpolation = cv2.INTER_AREA)

    #cv2.imshow(resized)
    cv2.imwrite('C:/Users/supachai/Desktop/daily/img/daily_price_img.png', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return

def img_price_glitter(gold_a,gold_b,gold965_a,gold965_b,money_a,money_b,date):
    date_x = 155
    date_y = 420

    golda_x = 220#240
    golda_y = 1000#1050

    goldb_x = 220
    goldb_y = 1240

    gold965a_x = 652
    gold965a_y = 1000

    gold965b_x = 652
    gold965b_y = 1240

    moneya_x = 1170
    moneya_y = 1000

    moneyb_x = 1170
    moneyb_y = 1240

    image = cv2.imread(r'C:\Users\supachai\Desktop\daily\img\image4.png')  
    cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
    pil_im = Image.fromarray(cv2_im_rgb)  
    draw = ImageDraw.Draw(pil_im)
    fontpart = (r'C:\Users\supachai\Desktop\daily\font\milktea-normal.ttf')
    font1 = ImageFont.truetype(fontpart, 58)
    font2 = ImageFont.truetype(fontpart, 80)
    
    draw.text((date_x, date_y), date, font=font2, fill=(0,0,0,0))
    
    draw.text((golda_x, golda_y), gold_a, font=font1, fill=(0,0,0,0))
    draw.text((goldb_x, goldb_y), gold_b, font=font1, fill=(0,0,0,0))

    draw.text((gold965a_x, gold965a_y), gold965_a, font=font1, fill=(0,0,0,0))
    draw.text((gold965b_x, gold965b_y), gold965_b, font=font1, fill=(0,0,0,0))

    draw.text((moneya_x, moneya_y), money_a, font=font1, fill=(0,0,0,0))
    draw.text((moneyb_x, moneyb_y), money_b, font=font1, fill=(0,0,0,0))
    
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    width = 1040
    height = 1040
    dim = (width, height)
    resized = cv2.resize(cv2_im_processed, dim, interpolation = cv2.INTER_AREA)

    cv2.imwrite('C:/Users/supachai/Desktop/daily/img/glitter_price_img.png', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return

def img_daily(header, content,):

    text_size1 = 50
    text_size2 = 50
    header_x = 50
    header_y = 230
    content_x = 280
    content_y = 370

    image = cv2.imread(r'C:\Users\supachai\Desktop\daily\img\daily_3.png')  
    cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
    pil_im = Image.fromarray(cv2_im_rgb)  
    draw = ImageDraw.Draw(pil_im)
    fontparTHSarabunNew = (r'C:\Users\supachai\Desktop\daily\font\THSarabunNew Bold.ttf')
    fontpartFC = (r'C:\Users\supachai\Desktop\daily\font\FC Subject Rounded Bold [Non-commercial use].ttf')
    font1 = ImageFont.truetype(fontpartFC, text_size1)
    font2 = ImageFont.truetype(fontparTHSarabunNew, text_size2)

    draw.text((header_x, header_y), header, font=font1, fill=(255,255,255,0))
    draw.text((content_x, content_y), content, font=font2, fill=(255,255,255,0))
    
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    width = 1040
    height = 1040
    dim = (width, height)
    resized = cv2.resize(cv2_im_processed, dim, interpolation = cv2.INTER_AREA)

    #cv2.imshow(resized)
    cv2.imwrite('C:/Users/supachai/Desktop/daily/img/daily_img.png', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return

def img_glitter(header, content):

    text_size1 = 50
    text_size2 = 50
    header_x = 50
    header_y = 230
    content_x = 280
    content_y = 370
    image = cv2.imread(r'C:\Users\supachai\Desktop\daily\img\glitter_3.png')  
    cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
    pil_im = Image.fromarray(cv2_im_rgb)  
    draw = ImageDraw.Draw(pil_im)
    fontparTHSarabunNew = (r'C:\Users\supachai\Desktop\daily\font\THSarabunNew Bold.ttf')
    fontpartFC = (r'C:\Users\supachai\Desktop\daily\font\FC Subject Rounded Bold [Non-commercial use].ttf')
    font1 = ImageFont.truetype(fontpartFC, text_size1)
    font2 = ImageFont.truetype(fontparTHSarabunNew, text_size2)

    draw.text((header_x, header_y), header, font=font1, fill=(255,255,255,0))
    draw.text((content_x, content_y), content, font=font2, fill=(255,255,255,0))
    
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    width = 1040
    height = 1040
    dim = (width, height)
    resized = cv2.resize(cv2_im_processed, dim, interpolation = cv2.INTER_AREA)

    cv2.imwrite('C:/Users/supachai/Desktop/daily/img/glitter_img.png', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return


