import textract

file = r'C:\Users\supachai\Desktop\daily\daily Gold 651226.docx'

text = textract.process(filename = file)
text2 = text.decode('utf-8')

start_date = text2.index("วัน")
end_date = text2.index("Daily")

datedoc = str(text2[(start_date-3):(end_date)]).strip()

print(datedoc)