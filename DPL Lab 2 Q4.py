#student ID:1201200987#
#student Name:Loh Joo Sheng#
BNN=1.5
GRPS=5.6

comb=int(input("Enter the quantity (comb) of bananas bought : "))
kg=float(input("Enter the amount (kg) of hrape bought : "))

pbanana = comb * BNN
pgrape = kg * GRPS
total=pbanana+pgrape

print("Invoice for Fruits Purchase")
print("---------------------------------")
print("Item\t          Qty\t  Price\t       Total ")
print("Banana(combs)\t  {:.2f}\t  RM1.50\t RM{:.2f}".format(comb,pbanana))
print("Banana(combs)\t  {:.2f}\t  RM1.50\t RM{:.2f}".format(kg,pgrape))
print("Total = RM{}".format(total))