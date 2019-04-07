# ----* to set system variable use preferences->project structure->add content root *----
import antigravity
# import my_module #for importing complete file
import sys
# sys.path.append('/Users/utkarshshende/Desktop/importTest') # to accessing file when its in different location
from my_module import find_index, test    #for importing specific module(function,varaible)


courses = ['History', 'Math', 'Physics', 'CompSci']
# index = my_module.find_index(courses, 'Math') #we need to specify file_name.function() if importing complete file
index = find_index(courses, 'Math') #we can directly define module name when importing specific module
print(index)
print(test)
print(sys.path)