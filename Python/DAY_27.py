print("===== OPERATOR BOOLEAN DAN ARITMATIKA ===== \n")

x=int(input("Masukkan nilai x:"))
y=int(input("Masukkan nilai y:"))

operator_1 = x < y
operator_2 = x > y
operator_3 = x <= y
operator_4 = x >= y
operator_5 = x == y
operator_6 = x != y

print ('nilai {} lebih kecil dari {} adalah {}'. format (x,y, operator_1))
print ('nilai {} lebih besar dari {} adalah {}'. format (x,y,operator_2))
print ('nilai {} kurang dari atau sama dengan {} adalah {}'. format (x,y, operator_3))
print ('nilai {} lebih dari atau sama dengan {} adalah {}'. format (x,y, operator_4))
print ('nilai {} sama dengan  {} adalah {} '. format (x,y, operator_5))
print ('nilai {} tidak sama dengan {} adalah {}'. format (x,y, operator_6))