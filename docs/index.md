# UW Foundation of Programming: Python
# Assignment 7
---
Kevin Wong<br/>
November 18, 2019<br/>
Foundations of Programming: Python<br/>
University of Washington<br/>
Professor: Randal Root<br/>
Assignment 07<br/>

**Introduction**<br/>
For this assignment 7, we are to use the web to research good examples of websites for pickling and error handling in python. We are then to explain the subject and why we feel these websites are good. We are then to post our assignment on GitHub, create a GitHub webpage, and take the text, images, and links from your Word document and put them into the GitHub webpage.

**Assignment**<br/>
For this assignment, I use the web to research Exception Handling and Error Handling in Python. I have organized this paper to showcase the few webpages that provide good example to learn these topics. And to explain why I chose them. I also added examples that I have learn from these websites to explain the topic. 

**Research Exception Handling in Python**<br/>
I found these three webpages below on except handling exceptionally good. To me, what is a good website for teaching anything, let alone programming, is to start with the very extreme basic. A good website will not confuse the student with additional information that is unnecessary at the beginning. They will use as minimal of information as possible to get their point across. A good website will also use multiple simple examples to augment their point. A good website must also go through each step carefully because skipping a step may confuse the student. Therefore, I found these websites to be good, especially the first one on the list from w3wschools.com. What is exceptionally good about w3wschool.com is that they also format their webpages so that they are very easy to read, with lots of white spaces and large fonts and good use of background color to separate the different examples:

[w3wschools.com - Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

[PythonForBegineers - Exception Handling in Python](https://www.pythonforbeginners.com/error-handling/exception-handling-in-python)

[DataCamp - Exception and Error Handling in Python](https://www.datacamp.com/community/tutorials/exception-handling-python)

**Exception Handling Example**<br/>
According to the website pythonforbeginners.com in the 2nd link above, if describes an exception, “as an error that happens during execution of a program. When that
error occurs, Python generate an exception that can be handled, which avoids your
program to crash.” The website goes to say that, “exceptions are convenient in many ways for handling errors and special conditions in a program. When you think that you have a code which can produce an error then you can use exception handling.”

Let’s look at an extremely simple example the benefit of structured error handling. Figure 1 is code that will result in an error when ran. This error is shown in Figure 2.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure1.jpg "Figure 1")<br/>
**Figure 1. Screenshot of a simple code to demonstrate an error.**<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure2.png "Figure 2")<br/>
**Figure 2. Screenshot of result from running the code.**<br/>

The error shown in Figure 2 is useful to the software developer but not too useful to the user of the program. If the error is expected, the developer can add some code to handle the error in a much more elegant way. Here, in Figure 3, is the modification to the code to solve this problem.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure3.png "Figure 3")<br/>
**Figure 3. Screenshot of modified code to handle errors.**<br/>

The resulting output from running the program, as shown in Figure 4, is much more palatable to the user. The output can be written in plain simple English as oppose to the gibberish that the user sees from the earlier output in Figure 2.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure4.png "Figure 4")<br/>
**Figure 4. Screenshot of resulting output from the modified code to handle errors.**<br/>

**Built-in Exceptions**<br/>
Python provides some basic exception classes which are already defined and can be used in generic cases. A list of Built-in exceptions is shown Figure 5 from the datacamp.com website.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure5.png "Figure 5")<br/>
**Figure 5. Screenshot of a list of Built-in exceptions from https://www.datacamp.com/community/tutorials/exception-handling-python**

**Exception Handling Example: ValueError**<br/>
Now look at the code as shown in Figure 6. It’s asking the user to enter an integer. When the user does that, the program should display a sentence that the user has successful entered an integer.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure6.png "Figure 6")<br/>
**Figure 6. Screenshot of code that ask user to input an integer.**<br/>

However, as you shall see in Figure 7, if the user does not enter an integer, but instead enter a letter “a”, a long and confusing error message appears.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure7.png "Figure 7")<br/>
**Figure 7. Screenshot of the error message output when user enters letter “a”.**<br/>

In order to handle this error more appropriately, we can use one of the python’s Built-in exception called “ValueError”. Look at Figure 8 for the modified code.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure8.png "Figure 8")<br/>
**Figure 8. Screenshot of the modified code from Figure 6 to handle the exception error.**<br/>

Now, when the user runs the program and enters the letter “a”, it will display, “No valid integer!” and to, “Please try again…” See Figure 9. The program will continuously display the same error message until the user enters an integer, then it will display, “Awesome, you successfully entered an integer!” This way of handling the error is much more user friendly.<br/>

![alt text](https://raw.githubusercontent.com/mynameiswong/IntroToProg-Python-Mod07/master/docs/Figure8.png "Figure 8")<br/>
**Figure 9. Screenshot of the output from running the code in Figure 8.**<br/>





