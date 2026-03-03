
# TEST CASE-1

import re

username = input("enter username:")
password = input("enter password:")

username_pattern = r'^(?=.{1,20}$)[a-zA-Z0-9._]+@(gmail\.com|outlook\.in)$'
password_pattern = r'^[A-Z][a-zA-Z@]{7}$'

if re.match(username_pattern,username):
    print("valid username")
else:
    print("Invalid username")

if re.match(password_pattern,password):
    print("valid password")

else:
    print("Invalid password")

# OUTPUT:
# =======
# enter username:Manasa01@gmail.com                       
# enter password:Manasa@@
# valid username
# valid password

# ====================================================================

# TESTCASE-2

import re

username = input("enter username:")
password = input("enter password:")

username_pattern = r'^([A-Z][A-Za-z0-9]{10})$'
password_pattern = r'^[0-9]{5}$'

if re.match(username_pattern,username):
    print("valid username")
else:
    print("Invalid username")

if re.match(password_pattern,password):
    print("valid password")

else:
    print("Invalid password")

# # OUTPUT:
# # ========
# # enter username:Manasa1234
# # enter password:12345
# # Invalid username
# # valid password

# =======================================================================

# # TESTCASE-3
# # ==========

import re

username = input("enter username:")
password = input("enter password:")

username_pattern = r'^([A-Za-z]{5})$'
password_pattern = r'^[A-Z0-9]@#{5}$'

if re.match(username_pattern,username):
    print("valid username")
else:
    print("Invalid username")

if re.match(password_pattern,password):
    print("valid password")

else:
    print("Invalid password")

# OUTPUT:
# ========
# enter username:Manas
# enter password:M12@#
# valid username
# Invalid password

# ======================================================================================

# TESTCASE-4
# ===========

import re

username = input("enter username:")
password = input("enter password:")

username_pattern = r'^([A-Za-z0-9]{10})$'
password_pattern = r'^[A-Za-z0-9]{5}$'

if re.match(username_pattern,username):
    print("valid username")
else:
    print("Invalid username")

if re.match(password_pattern,password):
    print("valid password")

else:
    print("Invalid password")

# OUTPUT:
# ========
# enter username:Manasa1234
# enter password:Manu0
# valid username
# valid password