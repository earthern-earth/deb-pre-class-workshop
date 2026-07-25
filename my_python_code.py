print("1. สร้าง List ชื่อ temperatures มีค่าอุณหภูมิ 7 วัน [35, 25, 26, 25, 29, 27, 38] คำนวณค่าเฉลี่ยออกมา\n")
temperatures = [35, 25, 26, 25, 29, 27, 38] 

total = sum(temperatures)
average = total/len(temperatures)

print(f"average_temperature: {average}\n")
print("--- --- --- ---\n")

print("2. เขียน loop พิมพ์ค่าแต่ละวัน เช่น “วันที่ 1 มีค่า 35 องศา\n")
i = 1
for temperature in temperatures:
    print(f"วันที่ {i} มีค่า {temperature} องศา")
    i = i + 1
print("--- --- --- ---\n")

print("3. เขียนฟังก์ชัน classify_temp(t, avg) คืนค่า \"ร้อน\" ถ้าเกินค่าเฉลี่ย และ \"เย็น\" ถ้าต่ำกว่าหรือเท่ากับค่าเฉลี่ย\n")
def classify_temp(t, avg):
    result = "ร้อน" if t > avg else "เย็น"
    return result


for temperature in temperatures:
    print(f"Tempearture = {temperature} >> {classify_temp(temperature, average)}")
print("--- --- --- ---\n")

classify_temp_lambda = (lambda t, avg: f"Tempearture = {t} >> ร้อน" if t > avg else f"Tempearture = {t} >> เย็น")

for temperature in temperatures:
    print(f"{classify_temp_lambda(temperature, average)}")
print("--- --- --- ---\n")

print("4. ลองใช้ pandas อ่านไฟล์ CSV pokemon.csv แล้วสั่ง print ค่า df.head() ออกมา\n")
import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df.head(5))
print("--- --- --- ---\n")