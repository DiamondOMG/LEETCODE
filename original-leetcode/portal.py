"""
    เกม หาจำนวนก้าวที่น้อยที่สุด ในการไปถึงเป้าหมาย 
    เริ่มจาก 1 ก้าวได้ไกลสุด 11 ช่อง เป้าหมายอยู่ที่ ช่อง 200 
    ให้ portal มา ชุดนึง ถ้าก้าวลงช่องนั้น จะสามารถวาปไปอีก ช่องได้
    เช่น portal {35:100, 150:200}
"""
def warp(portal: dict[int, int]) -> int:
    position = 1
    step = 0
    target = 200

    while position < target:
        # ถ้าเดินถึงเป้าภายใน 1 ก้าว
        if target - position <= 11:
            step += 1
            return step

        # เช็คว่ามี portal อยู่ในระยะ 11 ช่องข้างหน้ามั้ย
        jumped = False
        for offset in range(1, 12):
            key = position + offset
            if key in portal:
                position = portal[key]
                step += 1
                jumped = True
                break

        # ถ้าไม่เจอ portal เลย → เดิน 11 ช่องตามปกติ
        if not jumped:
            position += 11
            step += 1

    return step


print(warp({35:100, 150:199}))