
                # Big Calculation               (comments.py)
'''                        
Python stores a small value integer in 32 bits or 64 bits
depends on the cpu word size. But the storage may increase
as needed as long as memory still available.
'''
##print(123**1234)                        #   (print_input.py)
                                          # **  (operators.py)
# Python integers can be as big as the memory available.       (types.py)
# A Python statement does not need a semicolon(;) at the end.  (print_input.py)

# 2**64 seconds is equal to how many billion(10**9) years?
seconds = 2**64	                       # assignement (variables.py)
minutes = seconds / 60              # 1 minute = 60 seconds
hours = minutes / 60                # 1 hour = 60 minutes
days = hours / 24                   # 1 day = 24 hours
years = days / 365.25               # 365.25 day = 1 year
billion_years = years / 1_000_000_000   # 1_000_000_000 years = 1 billion year
                              # embedded underscore (numbers.py)                           
##print(billion_years)   

                                    # string formatting  (strings.py)
##print('2**64 = %.2f billion_years' % billion_years)
                                  
                                    # function string    (strings.py)
##print(f'2**64 = {billion_years:.2f} billion_year')
                                                   
#---------------------------------------------------------

'''                                   multiple lines (comments.py)
กระดานหมากรุกขนาด 8x8 มี 64 ช่อง
        วางเมล็ดข้าว  1 เมล็ดลงบนช่องที่ 1
                  2 เมล็ดลงบนช่องที่ 2
                  4 เมล็ดลงบนช่องที่ 3
                  8 เมล็ดลงบนช่องที่ 4
                     ..............
                  2**n เมล็ดลงบนช่องที่ n
        ต้องใช้ช้าวทั้งหมด 2**64 - 1 เมล็ด
หากประเทศหนึ่งผลิตข้าวได้ 1000 ล้านตัน ต่อปี สมมติว่าข้าว 1 ตันมี 10 ล้านเมล็ด
      ประเทศนี้ต้องใช้เวลากี่ปีจึงจะผลิตข้าวจำนวนนี้ได้
'''
grains = 2**64 - 1
tons = grains / (10 * 1_000_000)
years = tons / (1000 * 1_000_000)
##print('%.2f years' % (years))

'''
Exercise:
1. บริษัท Google มีชื่อมาจากคำว่า googol ซึ่งเท่ากับ 10 ยกกำลัง 100 คือ 10**100
       จงคำนวณ 1 googol วินาทีเท่ากับกี่พันล้าน(10**9) ปี

2. ชาวตะวันตกเชื่อว่าเลข 6 เป็นเลขอาถรรพ์ และ 666 คือเลขชั่วร้ายสุดๆ
       จงคำนวณว่า ระหว่าง 666**666 กับ 6**(6**6) ค่าใดมากกว่ากัน

3. ในทวีปยุโรป 1 billion มีค่าเท่ากับ 1 ล้านล้าน (คือ 10**12)
   แต่ในอเมริกา 1 billion มีค่าเท่ากับ 1 พันล้าน (คือ 10**9)
กำหนดให้ 1 นาทีมี 60 วินาที 1 ชั่วโมงมี 60 นาที 1 วันมี 24 ชั่วโมง และ 1 ปีมี 365.25 วัน
สมมติว่า คนทุกคนหายใจหนึ่งครั้งทุกวินาที ตั้งแต่เกิดและไม่หยุดหายใจจนตาย
คนยุโรปจะไม่สามารถมีอายุอยู่ถึงตอนที่หายใจครั้งที่ 1 billion (10**12)
     แต่คนอเมริกันจะหายใจครั้งที่ 1 billion (10**9) ตอนอายุประมาณกี่ปี

4. Alpha Centauri คือกลุ่มดาวที่อยู่ห่างจากโลกประมาณ 4.37 ปีแสง (light year)
   1 ปีแสง คือระยะทางที่แสงเดินทางหนึ่งปี มีค่าประมาณ 9.4605284 × 10**12 กิโลเมตร
เครื่องบินเจ็ท MIG-25 ทำความเร็วได้ 3,089 กิโลเมตร/ชั่วโมง
จงคำนวณว่า MIG-25 ต้องใช้เวลากี่ปี จึงจะไปถึง Alpha Centauri โดยสมมติว่าสามารถใช้
ความเร็วสูงสุดออกจากโลกไปได้ตลอดเส้นทาง และน้ำมันไม่หมด 
'''
