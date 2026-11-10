BUFFER_SIZE = 8

def lab(data, check_size=False):
    # บัฟเฟอร์ 8 ไบต์ ตามด้วยข้อมูลข้างเคียง 4 ไบต์
    memory = bytearray(b"........KEEP")

    if len(data) > len(memory):
        raise ValueError("เกินพื้นที่ของแบบจำลอง")

    if check_size and len(data) > BUFFER_SIZE:
        raise ValueError("ปฏิเสธ: ข้อมูลใหญ่กว่าบัฟเฟอร์")

    # ทุกการเขียนยังอยู่ภายในอาร์เรย์ที่จัดสรรไว้
    memory[:len(data)] = data

    print("Buffer :", bytes(memory[:BUFFER_SIZE]))
    print("ข้างเคียง:", bytes(memory[BUFFER_SIZE:]))

data = b"ABCDEFGHIJKL"

lab(data)  # ข้อมูลข้างเคียงเปลี่ยนจาก KEEP เป็น IJKL

try:
    lab(data, check_size=True)
except ValueError as error:
    print(error)