from assignment3 import ConfigDict     # you can put class ConfigDict 
                                       # in assignment3.py, or just put the 
                                       # class code in the same file as this
                                       # calling code; then this import 
                                       # statement is not needed

cc = ConfigDict('config_file.txt')

print(cc['query'])                     # SELECT this FROM that WHERE condition
print(cc['email_to'])                  # me@mydomain.com
cc['database'] = 'mysql_managed'       # [ this writes to the config file ]