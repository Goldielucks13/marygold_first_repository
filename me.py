import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

#personal_information
name = "Mary Gold Balusada"
age = 19
address = "Poblacion Aurora, Zamboanga del Sur"
school = "Zamboanga del Sur Provincial Government College-Aurora"
course = "Bachelor of Science in Information System"
blood_type = "pass"
religion = "Roman Catholic"
sex = "Female"
status = "single"

#colored string
c_name = Fore.GREEN + Style. BRIGHT + name
c_age = Fore.RED + Style. BRIGHT + str(age)
c_address = Fore.CYAN + Style. BRIGHT + address
c_school = Fore.BLUE + Style. BRIGHT + school
c_course = Fore.LIGHTMAGENTA_EX + Style. BRIGHT + course
c_blood_type = Fore.LIGHTCYAN_EX + Style. BRIGHT + blood_type
c_religion = Fore.LIGHTBLUE_EX + Style. BRIGHT + religion
c_sex = Fore.MAGENTA + Style. BRIGHT + sex
c_status = Fore.GREEN + Style.BRIGHT + status

color_name = Fore.LIGHTWHITE_EX + Style.BRIGHT + "Name: "
color_age = Fore.LIGHTWHITE_EX + Style.BRIGHT + "Age: "
color_address = Fore.LIGHTWHITE_EX + Style.BRIGHT + "Address: "
color_school = Fore.LIGHTWHITE_EX + Style.BRIGHT + "School: "
color_course = Fore.LIGHTWHITE_EX + Style.BRIGHT + "course: "
color_blood_type = Fore.LIGHTWHITE_EX + Style.BRIGHT + "Blood Type: "
color_religion = Fore.LIGHTWHITE_EX + Style.BRIGHT + "Religion: "
color_sex = Fore.LIGHTWHITE_EX + Style.BRIGHT + "Sex: "
color_status = Fore.LIGHTWHITE_EX + Style.BRIGHT + "Status"
#
print(color_name + c_name)
print(color_age + c_age)
print(color_address + c_address)
print(color_school + c_school)
print(color_course + c_course)
print(color_blood_type + c_blood_type)
print(color_religion + c_religion)
print(color_sex, c_sex)
print(color_status, c_status)