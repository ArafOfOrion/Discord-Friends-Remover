# Discord Friends Remover
This is a Python automation script which helps you to remove all of your discord friends and pending friend requests. This is basically an autoclicker, have a look into usage guide to know further about how to use it.

## Installation
In order to use this script, you need to have a Python interpreter installed in your computer, and to easily edit the script you need to have a code editor installed. Lets have a closer look into them, if you already have these installed then you can skip this section.

#### Python Interpreter
Having a Python interpreter installed is a must for running the script. You can easily download and install a Python interpreter from https://www.python.org/downloads/.  For a detailed installation guide, have a closer look into https://docs.python.org/3/using/.

#### Code Editor
If you are already a programmer then you should have a code editor installed in your computer. It is not a must to have a code editor installed, you need to install it so that you can easily edit the scripts. You can use notepad or any other text editor anyways. We recommend you using Sublime Text, if you are a programmer or willing to become one then get started with Visual Studio Code or PyCharm. You are actually free to use any editor you want. Here are the links for some useful code editing software:-
- [Sublime Text](https://www.sublimetext.com/ "Sublime Text")
- [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code")
- [PyCharm](https://www.jetbrains.com/pycharm/ "PyCharm")

## Usage Guide
Now let's see how can you use the scripts.  First of all download the scripts or clone this GitHub repository, then open the file you want to use, `pending_requests.py` is for removing pending requests and `friends.py` is for removing friends. Now let's see how to use them. 

### Pending Requests
Using this script is easy, first of all open the file. In line 6 you will see
```py
pending_requests = 203
``` 
Enter the number of pending friend requests you have here. Then open up discord (either web version or desktop version). Go to `Friends -> Pending` and then run the script. After you run the script immidiate put your mouse cursor on the reject button, remember you have 5 seconds to do this. You can increase the waiting time by editing line 7 which is,
```
time.sleep(5)
```
here you can put a valid number of seconds to be waited after running the script. Soon the script will start its work and you will get desired result.

### Friends
Using this script is a bit complex, there are two methods to do it. First method is recommended for everyone, and the second method is still workable but not recommended for non-programmers.

#### Recommended way
First of all open discord desktop app and zoom in the window, the window size should be `110%`.  After that open the script and go to line 16, which is:-
```
friends = 475
```
here input the number of friends you have. Right below this line, you will see,
```
time.sleep(5)
```
this works exactly the same as we described above in removing pending requests section. However, after that in your discord desktop app go to `Friends -> All` and then run the script. You will get your desried output (hopefully). If you don't get what you expected, move to the second way.

#### Second way
This way is a bit complex, in this way first of all you have to get the x and y coordinates of buttons in your discord app and then run the script. First of all either open the discord desktop app or open in website. Go to `Friends -> All` and put your mouse cursor on the three dots. Then open up your terminal and run this command:-
```
Python
```
> Note: This command might not work if you don't have Python in your path. in case of that, refer to https://www.javatpoint.com/how-to-set-python-path.

After that, in the terminal write the following lines of codes:-
```
import pyautogui
pyautogui.position()
```
You will get an output like
```
Point(x=484, y=307)
```
Now open `friends.py` and go to line 6 and set "x" to the value of x you got in your terminal. Do the same with the "y" value in line 7. Don't close the terminal, minimize it.
Now, click on the three dots in your discord app and put your mouse on `Remove Friend` button. Then again open your terminal, you can easily do it by pressing `alt + tab` since you didn't close it. Now run the following lines of code:-
```
pyautogui.position()
```
Yes, you don't have to run those extra codes because you didn't close the terminal. You will get a similiar output as you got before. Now do the same process in line 11 and line 12. Done, now just run the script and you will get the output you expect.

## Conclusion
The process might be slow if you have too many friends, please have patience. If this helped you, then consider starring the repository.