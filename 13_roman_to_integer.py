def romanToInt(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    
    # วนลูปจากซ้ายไปขวาถึงตัวสุดท้าย
    for i in range(len(s) - 1):
        # ถ้าค่าตัวอักษรปัจจุบันน้อยกว่าตัวถัดไป แสดงว่าเป็นการลบ
        if roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        # ถ้าไม่ใช่อย่างนั้น ก็ให้บวกเพิ่มปกติ
        else:
            total += roman_map[s[i]]
            
    # เพิ่มค่าของตัวอักษรตัวสุดท้ายเข้าไป
    total += roman_map[s[-1]]
    
    return total

print(romanToInt("X"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))