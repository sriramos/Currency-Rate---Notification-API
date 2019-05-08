# Currency-Rate---Notification-API


Currency Price Monitoring System

Problem Description
The goal is to build a system that notifies the user when a currency pair rate reaches the target rate. User configures the currency pair and target rate

Implementation

The program is implemented in Python.  We have used different layers of classes and functions to implement the design as per the requirements.

XMLParser – Gets the input data from the url in XML format and reads the input till it identifies the currency pair given.

CurrencyTree– Reads the updated input continuously and the target and bid rate of the pair.

CurrencyComparator –  Reads the XML input pair and the rate from the URL given and compares it with the existing database.

Main – Used for integrating all the functionalities of the design

Functional Description
When the program is executed, it initially sets the default values to have a currency pair of ‘EURUSD’ with a target value of 1.381 and periodically checks if the current value drops below the default target value. If the condition is achieved, the program stops indicating the user, else, if runs a loop till the condition satisfies for every 10 seconds. The user can configure the currency pair and the target rate once one set of conditions are satisfied. The program then executes according to the new conditions and variables set by the user.

Conclusion
The program is developed and executed successfully according to the requirements of the user. The development process included performing and implementing various software design practices and methodologies which helped carry out the development process efficiently.
