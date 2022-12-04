import webbrowser
def stock_crawler():
    x=str((input("Enter  be dorked  ")))
    y=("//.......Searching "+x+" in defined places.........//")
    print(y)
    z=(input("Open chrome   Y/N "))
    
    if z == 'y':
        webbrowser.open("https://www.google.co.in/advanced_search")
        webbrowser.open_new_tab("https://www.screener.in/company/"+x)
        webbrowser.open_new_tab("https://in.tradingview.com/chart/?symbol=NSE%3A"+x)
        webbrowser.open_new_tab("https://chartink.com/stocks/"+x+".html")
        webbrowser.open_new_tab("https://nseguide.com/stock.php?"+x)
        webbrowser.open_new_tab("https://www.google.com/finance/quote/"+x+":NSE")
        

    
   
    else:
        print("Nothing ")
        
        
        

print(stock_crawler())
