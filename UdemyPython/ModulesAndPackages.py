# PyPi is a respository for open-source third-party Python packages.
# its similar to RubyGems in the Ruby world, PHP's Packagist, CSPAN for Perl, and NPM for node.js 

from colorama import init 
init()
from colorama import Fore
print(Fore.RED + "some red text")

# how to create your own modules and packages. 
# modules are just.py scripts that you call in another .py script 
# packages are a collection of modules 

#! example: im just doing it in one .py because i want to see it together.
#! normally you would have more than one .py so you can call it in differnt places 

def my_func():
    print("this would be in a different .py") 

#! now to call it in a differnt .py 

#*    from otherpy import my_func

my_func() 

#! this is the file layout example: this gives you access to other files inside other folders. 
#* Folder MainPackage
#?  inside of MainPackage is Folder Subpackage and __init__.py and you can put a main .py file in here. 
# you dont need anything in __init__.py but you need it so that when it runs it knows its a pacakge 
#?   inside of Subpackage Folder you also have a __init__.py for the same reasons. you can have any other files you want in here too. 

#! to import it!!!

#*   from MyMainPackage import some_mine_script 
#? and to get file inside that folder you use a . to get that file  
#* from MyMainPackage.SubPackage import mysubscript 
#? you can can call that function inside the folder 
#*  some_main_script.report_main() 

