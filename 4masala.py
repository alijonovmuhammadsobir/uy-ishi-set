ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}

umumiy = ali.intersection(vali)
faqat_ali = ali.difference(vali)

print("umumiy:", umumiy)
print("faqat Ali:", faqat_ali)