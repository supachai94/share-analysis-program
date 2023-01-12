from win32com import client as wc
import textract
import os
from create_img import img_price_daily, img_price_glitter, img_daily, img_glitter

file = r'C:\Users\supachai\Desktop\daily\img\daily Gold 651226.docx'

def thaidate():
    import datetime
    date = datetime.datetime.now()
    day = date.strftime("%A")
    day_num = date.strftime("%d")
    month = date.strftime("%B")
    month_num = date.strftime("%m")
    year = date.strftime("%Y")
    thaiyear = int(year)+543
    time_h = date.strftime("%H")
    time_m = date.strftime("%M")

    if day == "Monday":
        day = "วันจันทร์"
    elif day == "Tuesday":
        day = "วันอังคาร"
    elif day == "Wednesday":
        day = "วันพุธ"
    elif day == "Thursday":
        day = "วันพฤหัสบดี"
    elif day == "Friday":
        day = "วันศุกร์"


    if month == "January":
        month = "มกราคม"
    elif month == "February":
        month = "กุมภาพันธ์"
    elif month == "March":
        month = "มีนาคม"
    elif month == "April":
        month = "เมษายน"
    elif month == "May":
        month = "พฤษภาคม"
    elif month == "June":
        month = "มิถุนายน"
    elif month == "July":
        month = "กรกฎาคม"
    elif month == "August":
        month = "สิงหาคม"
    elif month == "September":
        month = "กันยายน"
    elif month == "October":
        month = "ตุลาคม"
    elif month == "November":
        month = "พฤศจิกายน"
    elif month == "December":
        month = "ธันวาคม"

    return day, day_num, month, month_num, str(thaiyear), time_h, time_m

def doc2docx(filename, part, name):
    w = wc.Dispatch('Word.Application')
    doc = w.Documents.Open(os.path.abspath(filename))
    doc.SaveAs(part+'/'+name+'.docx',16)
    doc.Close()
    return

def input_daily(filename):
    text = textract.process(filename = filename)
    text2 = text.decode('utf-8')

    resistance = text2.index("Resistance")
    support = text2.index("Support")

    start_recommend = text2.index("แนะนำ")
    end_recommend = text2.index("ปัจจัยที่ต้องติดตาม")

    start_analysis = text2.index("วิเคราะห์ราคาทองคำ")
    end_analysis = text2.index("แนะนำ")

    start_strategy = text2.index("Today Strategy")
    end_strategy = text2.index("วิเคราะห์ราคาทองคำ")

    price_gold_res = str(text2[(resistance+12):(resistance+23)]).replace(" ","").strip()
    price_gold965_res = str(text2[(resistance+24):(resistance+41)]).replace(" ","").strip()
    price_money_res = str(text2[(resistance+41):(resistance+52)]).replace(" ","").strip()

    price_gold_sup = str(text2[(support+7):(support+20)]).replace(" ","").strip()
    price_gold965_sup = str(text2[(support+20):(support+35)]).replace(" ","").strip()
    price_money_sup = str(text2[(support+37):(support+48)]).replace(" ","").strip()

    recommend = str(text2[(start_recommend+7):(end_recommend)]).strip()
    analysis = str(text2[(start_analysis+20):(end_analysis)]).strip()
    strategy = str(text2[(start_strategy):(end_strategy)]).strip()
    select_strategy = strategy.split() 

    return(price_gold_res,price_gold965_res,price_money_res,price_gold_sup,price_gold965_sup,price_money_sup,recommend,analysis,select_strategy[2])

def input_glitter(filename):
    text = textract.process(filename = filename)
    text2 = text.decode('utf-8')

    start_recommend = text2.rfind("แนะนำ")
    end_recommend = text2.index("หัวข้อข่าวที่น่าสนใจ")

    start_header = text2.rfind("วิเคราะห์ราคาทองคำ")
    end_header = text2.index("แนะนำ")

    recommend = str(text2[(start_recommend+6):(end_recommend)]).strip()

    header = str(text2[(start_header+20):(end_header)]).strip()

    resistance = text2.rfind("Resistance")
    support = text2.rfind("Support")
    price_gold_res = str(text2[(resistance+12):(resistance+26)]).replace(" ","").strip()
    price_gold965_res = str(text2[(resistance+25):(resistance+42)]).replace(" ","").strip()
    price_money_res = str(text2[(resistance+42):(resistance+57)]).replace(" ","").strip()
    price_gold_sup = str(text2[(support+7):(support+22)]).replace(" ","").strip()
    price_gold965_sup = str(text2[(support+22):(support+39)]).replace(" ","").strip()
    price_money_sup = str(text2[(support+39):(support+55)]).replace(" ","").strip()

    return (price_gold_res, price_gold965_res, price_money_res, price_gold_sup, price_gold965_sup, price_money_sup, recommend, header)

def create_msg_daily(filename):
    x = input_daily(filename=filename)
    y = thaidate()
    recommend = x[6]
    analysis = x[7]
    select_strategy = x[8]
    date_str = "วันที่ "+y[1]+" "+y[2]+" "+y[4]
    url = "http://www.classicgold.co.th/image/strategy_analysis/filestrategy141120221131016777.pdf"
    daily = "บทวิเคราะห์ Daily Comment\n"
    day_session = "ประจำช่วง Day Session\n"

    comment_message = daily+day_session+date_str+"\n"+"\n"+select_strategy+"\n\n"+analysis+"\n\nแนะนำ : "+recommend+"\n\nสามารถติดตามบทวิเคราะห์ทั้งหมดได้ที่\n"+url+"\nสนใจลงทุนทองคำกับ Classic Gold\nทองคำแท่ง : 02-225-7770\nเว็บไซต์ : www.classicgold.co.th"+"\n#เจียบเซ่งเฮง #classicgold #ทองคำ #ทองคำแท้ #ค่ากำเน็จราคาถูก #ทองรูปพรรณ #ทองคำแท่ง #gold #ทองดีมีคุณภาพ #ออมทองออนไลน์ #tradinggold #ของขวัญ #ราคาทองวันนี้ #ราคาทองประจำวัน"

    price_message = "แนวรับ แนวต้าน\n"+date_str+"\nให้เพื่อนๆ ติดตามมาแล้วครับ\n"+"ติดตามข่าวสารข้อมูลเกี่ยวกับทองคำและสัญญาซื้อขายล่วงหน้าในผลิตภัณฑ์อื่นๆ ได้ที่\n"+"www.classicgold.co.th\n"+"__________________________\n"+"สนใจลงทุนทองคำกับ Classic Gold\n"+"ทองคำแท่ง : 02-225-7770"+"\n#เจียบเซ่งเฮง #classicgold #ทองคำ #ทองคำแท้ #ค่ากำเน็จราคาถูก #ทองรูปพรรณ #ทองคำแท่ง #gold #ทองดีมีคุณภาพ #ออมทองออนไลน์ #tradinggold #ของขวัญ #ราคาทองวันนี้ #ราคาทองประจำวัน"

    return comment_message, price_message

def create_msg_glitter(filename):
    x = input_glitter(filename=filename)
    y = thaidate()
    recommend = x[6]
    analysis = x[7]
    date_str = "วันที่ "+y[1]+" "+y[2]+" "+y[4]
    url = "http://www.classicgold.co.th/image/strategy_analysis/filestrategy141120221131016777.pdf"
    glitter = "บทวิเคราะห์ Glitter Gold\n"
    night_session= "ประจำช่วง Night Session\n"

    glitter_message = glitter+night_session+date_str+"\n\n"+analysis+"\n\nแนะนำ : "+recommend+"\n\nสามารถติดตามบทวิเคราะห์ทั้งหมดได้ที่\n"+url+"\nสนใจลงทุนทองคำกับ Classic Gold\nทองคำแท่ง : 02-225-7770\nเว็บไซต์ : www.classicgold.co.th"+"\n#เจียบเซ่งเฮง #classicgold #ทองคำ #ทองคำแท้ #ค่ากำเน็จราคาถูก #ทองรูปพรรณ #ทองคำแท่ง #gold #ทองดีมีคุณภาพ #ออมทองออนไลน์ #tradinggold #ของขวัญ #ราคาทองวันนี้ #ราคาทองประจำวัน"

    price_message = "แนวรับ แนวต้าน\n"+date_str+"\nให้เพื่อนๆ ติดตามมาแล้วครับ\n"+"ติดตามข่าวสารข้อมูลเกี่ยวกับทองคำและสัญญาซื้อขายล่วงหน้าในผลิตภัณฑ์อื่นๆ ได้ที่\n"+"www.classicgold.co.th\n"+"__________________________\n"+"สนใจลงทุนทองคำกับ Classic Gold\n"+"ทองคำแท่ง : 02-225-7770"+"\n#เจียบเซ่งเฮง #classicgold #ทองคำ #ทองคำแท้ #ค่ากำเน็จราคาถูก #ทองรูปพรรณ #ทองคำแท่ง #gold #ทองดีมีคุณภาพ #ออมทองออนไลน์ #tradinggold #ของขวัญ #ราคาทองวันนี้ #ราคาทองประจำวัน"


    return glitter_message, price_message

def create_contents(filename):
    name = os.path.basename(filename)
    splifilename = os.path.splitext(name)
    name = splifilename[0]
    get_status = name.split()
    status = get_status[0]
    
    if status == "daily":
        get_date = thaidate()
        date = get_date[1]+" "+get_date[2]+" "+str(get_date[4])
        x = input_daily(filename = filename)
        img_price_daily(money_a=x[5], money_b=x[2], gold_a=x[3], gold_b=x[0], gold965_a=x[4], gold965_b=x[1], date=date)

        img_daily(header="", content="")
        getdata = create_msg_daily(filename=filename)
        comment_message = getdata[0]
        price_message = getdata[1]

    elif status == "evening":
        get_date = thaidate()
        date = get_date[1]+" "+get_date[2]+" "+str(get_date[4])
        x = input_glitter(filename = filename)
        img_price_glitter(money_a=x[5], money_b=x[2], gold_a=x[3], gold_b=x[0], gold965_a=x[4], gold965_b=x[1], date=date)

        img_glitter(header="", content="")
        getdata = create_msg_glitter(filename=filename)
        comment_message = getdata[0]
        price_message = getdata[1]

    else:
        print("เกิดข้อผิดพลาดในขั้นตอนการสร้างเนื้อหา")
        print(status)

    return comment_message, price_message, status


datenow = thaidate()
date = datenow[0]+"ที่ "+datenow[1]+" "+datenow[2]+" พ.ศ. "+str(datenow[4])
now = date.split()
day_now = now[0]
day_num_now = now[1]
month_now = now[2]
year_now = now[4]

file = r'C:\Users\supachai\Desktop\daily\daily Gold 651226.docx'

text = textract.process(filename = file)
text2 = text.decode('utf-8')

start_date = text2.index("วัน")
end_date = text2.index("Daily")

datedoc = str(text2[(start_date):(end_date)]).strip()
select_datedoc = datedoc.split()
day_doc = select_datedoc[0]
day_num = select_datedoc[1]
month_doc = select_datedoc[2]
year_doc = select_datedoc[4]

if day_now == day_doc and day_num_now == day_num and month_now == month_doc and year_now == year_doc:
    print("000")

else:
    print("888")


#print(select_datedoc,now)
    