import xml.etree.ElementTree as ET
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import time
import requests



def getChoiceNumber():
    while (True):
        try:
            choice = input("Please enter the number of your selection [1-2]: ")
            choiceNum = int(choice)
            if (choiceNum >= 1 and choiceNum <= 2):
                return choiceNum
            else:
                print("Enter Valid Choices.")

        except ValueError:
            print("Enter Valid Integer")


def getString(text="Please enter a string: "):
    while (True):
        try:
            choice = input(text)
            return choice

        except:
            print("Enter Valid Input")


def getFloat(text="Please enter a decimal number"):
    while (True):
        try:
            choice = input(text)
            floatNum = float(choice)
            return floatNum

        except ValueError:
            print("YEnter Valid Floating Point Value.")

def getXMLValue(url):
    example_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    req = urllib2.Request(url, None, example_headers)

    #r = requests.get(url, headers=example_headers)

    response = urllib2.urlopen(req)

    xmlFile = response.read()
    return xmlFile;


class CurrencyTree:
    def __init__(self, string):
        self.tree = ET.fromstring(string)

    def getCurrentRate(self, symbol):
        for child in self.tree:
            if (child.attrib['Symbol'].lower() == symbol.lower()):
                return float(child[0].text)

    def checkSymbolExists(self, symbol):
        for child in self.tree:
            if (child.attrib['Symbol'].lower() == symbol.lower()):
                return True
        return False


class CurrencyComparator:
    def __init__(self, tree, currency, target, direction):
        self.currency = currency
        self.targetRate = target
        self.direction = direction

    def compareValues(self, tree):
        currentRate=tree.getCurrentRate(self.currency)
        if (self.targetRate >= currentRate):
            flagValue = 1
        else:
            flagValue = -1
        if (flagValue != self.direction):
            return True,flagValue
        else:
            return False,flagValue





def mainLoop():
    val = time.time()
    checkRate = 10
    CurrencyURL="https://rates.fxcm.com/RatesXML"
    tree = CurrencyTree(getXMLValue(CurrencyURL))
    test = CurrencyComparator(tree, 'EURUSD', 1.38355, 0)
    print("Currency Taken as Input " + test.currency)
    print(" when it reaches target rate " + str(test.targetRate) )
    print(" checking every " + str(checkRate) + " seconds.")

    while True:
        timeComparer=time.time()
        if ( timeComparer - val > checkRate):
            tree = CurrencyTree(getXMLValue(CurrencyURL))
            val,compareValue=test.compareValues(tree)
            print(compareValue)
            if (compareValue == -1):
                print("Currency Taken as Input "+test.currency )
                print("it is Above target rate " + str(test.targetRate) )
                print("current rate " + str(tree.getCurrentRate(test.currency)))
            elif (compareValue == 1):
                print("Currency Taken as Input " + test.currency)
                print("it is below target rate " + str(test.targetRate))
                print("current rate " + str(tree.getCurrentRate(test.currency)))
            val = time.time()
            if (val):
                break;

        time.sleep(0.1)
    while True:
        print("What would you like to do?")
        print("""
                    [1] Change my currency configuration.
                    [2] Exit the program.
                                        """)
        step1 = False
        choiceNum=0
        while (not step1):
            try:
                choice = input("Please enter the number of your selection [1-2]: ")
                choiceNum = int(choice)
                if (choiceNum >= 1 and choiceNum <= 2):
                    choiceNum=choiceNum
                else:
                    print("Invalid selection, try again.")
                step1 = True
            except:
                print("please try again.")

        selection = choiceNum

        if (selection == 1):
            step1 = False
            while (not step1):
                currencyName = getString("Currency to be cheked: ")
                if (tree.checkSymbolExists(currencyName)):
                    step1 = True
                else:
                    print("Invalid Currency")

            targetRate = getFloat("Please enter the target rate: ")

            print(
                "Would you like to be notified when the target rate is above [1] or below [2] the previously entered value?")
            choiceAboveOrBelow = getChoiceNumber()
            if (choiceAboveOrBelow == 1):
                test = CurrencyComparator(tree, currencyName, targetRate, 1)
            else:
                test = CurrencyComparator(tree, currencyName, targetRate, -1)

            print("Currently looking at currency " + test.currency + " when it reaches target rate " + str(
                test.targetRate) + " checking every " + str(checkRate) + " seconds.")
            while True:
                timeComparer = time.time()
                if (timeComparer - val > checkRate):
                    tree = CurrencyTree(getXMLValue(CurrencyURL))
                    val, compareValue = test.compareValues(tree)
                    print(compareValue)
                    if (compareValue == -1):
                        print("Currency Taken as Input " + test.currency)
                        print("it is Above target rate " + str(test.targetRate))
                        print("current rate " + str(tree.getCurrentRate(test.currency)))
                    elif (compareValue == 1):
                        print("Currency Taken as Input " + test.currency)
                        print("it is below target rate " + str(test.targetRate))
                        print("current rate " + str(tree.getCurrentRate(test.currency)))
                    val = time.time()
                    if (val):
                        break;
        elif (selection == 2):
            break



mainLoop()



