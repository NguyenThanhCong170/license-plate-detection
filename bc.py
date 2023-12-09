import easyocr
import csv
import os

def OCR_va_CSV(image):
  reader = easyocr.Reader(['en'], gpu=False)
  result = reader.readtext(image, detail = 0)
  output = "".join(result)
  output = output.upper().replace(' ',"-").replace('*',"-")
  print(result)
  
  #nhớ điều chỉnh file mình muốn ở đâu
  filepath = ".\detect.csv"
  if not os.path.isfile(filepath):
  
      file = open('detect.csv', 'w', newline='')
      csv_writer = csv.writer(file)
      csv_writer.writerow([f'output'])
      file.close()
  else:
      file = open('detect.csv', 'a', newline='')
      csv_writer = csv.writer(file)
      csv_writer.writerow([f'output'])
      file.close()
    
