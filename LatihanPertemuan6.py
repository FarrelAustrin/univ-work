list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang=2
for i in range(ulang):
  print ("data Ke - " + str(i+1))
  list_nim.append(input("Masukkan Nim anda : "))
  list_uts.append(int(input("Masukkan Nilai UTS anda :")))
  list_uas.append(int(input("Masukkan Nilai UAS : ")))

for i in range(ulang):
  list_total.append((list_uas[i] + list_uts[i]) / 2)

print("")
print("===============================================================")
print("Nim              Nilai Uts       Nilai UAS               Total")
print("===============================================================")

for i in range(ulang):
  print ("%s \t %i \t\t %i \t\t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))

print("===============================================================")