import csv
from datetime import *

class Info:
    def __init__(self):
        self.client = input("Please enter a client's name: ")
        self.text = input("Please enter the required text: ")
        self.height = int(input("Please enter the height of wood: "))
        self.width = int(input("PLease enter the width of the wood: "))
        self.length = int(input("Please enter the length of the wood: "))
        self.woodPrice = float(input("Please enter the price for the material: "))
    
    def priceCalculator(self):
        workerSalary = 15
        Tax = 21
        productPrice = (len(self.text))*1.2 + (self.width/100 * self.length/100 * self.height/100) * 3 * self.woodPrice
        taxSum = (productPrice + workerSalary)*Tax/100
        finalPrice = (productPrice + workerSalary + taxSum)
        return finalPrice
    
    def Export(self, price):
        mydate = datetime.now()
        cheque = open("Cheque.txt", "w")
        writing = mydate.strftime("Date and Time of printing: %d.%m.%Y %H : %M") + "\n Client name: " + self.client + "\n Ordered text: " + self.text + "\n Price in total: " + str(price) + "EUR"
        cheque.write(writing)
        with open('CSVCheque.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Date and Time of printing:", mydate])
            writer.writerow(["Client name:", self.client])
            writer.writerow(["Ordered text:", self.text])
            writer.writerow(["Price in total:", str(price) + " EUR"])
        
woodThing = Info()
totalSum = woodThing.priceCalculator()
woodThing.Export(totalSum)