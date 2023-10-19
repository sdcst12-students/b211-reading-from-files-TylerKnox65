"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""
import csv
def main(stock = None):
    numStock = 0
    found = None
    with open('task5.csv', newline='') as csvfile:
        readdata = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for i in readdata:
            data = ', '.join(i)
            data = data.split(",")
            
            try:
                if  stock == data[0]:
                    print(data)
                    found = data
                elif stock in data[0]:
                    numStock += 1
            except:
                pass
        if found != None:
            print(f"The company for the stock {stock} is {found[1]}")
        elif numStock > 0:
            print(f"There are {numStock} stocks with that name")
            



if __name__ == "__main__":
    main(input("Enter the stock: "))