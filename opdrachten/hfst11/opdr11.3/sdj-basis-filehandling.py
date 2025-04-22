'''Programma voor Basis Filehandling'''
__author__ = "Stefan de Jong"
__email__ = "370661@student.firda.nl"
__copyright__ = "Copyright 2024 (C) Stefan de Jong. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Stefan de Jong"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.

import os
import shutil 

with open('opdrachten\hfst11\opdr11.3\lorem-ipsum.txt', 'w') as file:
    file.write('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aeneanvulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. \n')

with open('opdrachten\hfst11\opdr11.3\lorem-ipsum.txt', 'r') as file:
    for line in file:
        print(line)

os.rename("opdrachten\hfst11\opdr11.3\lorem-ipsum.txt", "opdrachten\hfst11\opdr11.3\lorem-ipsum-copy.txt")
os.system('copy opdrachten\hfst11\opdr11.3\lorem-ipsum-copy.txt opdrachten\hfst11\opdr11.3')

with open('opdrachten\hfst11\opdr11.3\lorem-ipsum.txt', 'w') as file:
    file.write('Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodalessagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id,metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia.')

os.remove('opdrachten\hfst11\opdr11.3\lorem-ipsum.txt')
os.rename("opdrachten\hfst11\opdr11.3\lorem-ipsum-copy.txt", "opdrachten\hfst11\opdr11.3\lorem-ipsum.txt")

with open("opdrachten\hfst11\opdr11.3\lorem-ipsum.txt", 'r') as f:
    for line in f:
        for word in line.split():
            print(word, "")
        print("", "")