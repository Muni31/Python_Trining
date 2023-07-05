# Separate the classes made in task 2 into different files.
# Implement __init__.py, __version__.py which prints applicable details of the contents of this module.
from my_module.citys import city
from my_module.countrys import country
a=city()
b=country()
print(f"{a.town}- city defined in citys.py")
print(f"{b.county}- country defined in countrys.py")