
#========The beginning of the class=========
from tabulate import tabulate

class Shoe(dict):

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return int(self.quantity) 
    
    def __str__(self):
        #here I return a string of the attributes for ease of reading.
        #return f'Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}  '
        return f'{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'            

        
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = [] #object list
data_list = [] #string 2D list
#==========Functions outside the class==============
def open_file():
    file_list = []
    try:
        with open('inventory.txt', 'r') as f:
            file = f.readlines()[1:] #skip the first line which are the column names
        for line in file:
            content = line.replace('\n', '')
            content = content.split(',')
            temp_list = []
            for item in content:
                item = item.strip()
                temp_list.append(item)
            file_list.append(temp_list)
    except FileNotFoundError: #setting an exception incase the file does not exist
        print('File could not be found, make sure you are in the correct directory. ')   
    return file_list #returning the list for later use.

def read_shoes_data():
    #here I open the text file and write it to a list for later use
    inventory_data = open_file()
    for line in inventory_data:
        line = Shoe(line[0], line[1], line[2], line[3], line[4])
        shoe_list.append(line)

def tabular_data():
    #here I itterate through the shoe list of objects. Since an object cannot be itterated through
    #I have taken the display of the class object and put it into a list
    #I split and strip accordingly and then append that into its own list, from there I append that list
    #to the main list I will use for the table of the shoes
    for line in shoe_list:
        line = Shoe.__str__(line)
        content = line.split(',')
        temp_data = [] #temporary list to append to main list
        for item in content:
            x = item.strip().lower()
            temp_data.append(x)
        data_list.append(temp_data)
    return data_list    

def capture_shoes():
    while True:
        #Here I initiate the variables and assign values to later test are true for error handling
        cost = 0
        quantity = 0
        country = '1'
        code = '1'
        product = '1'
        
        #for the following lines of code I have used 'isnumeric()' to test if the input is being enter as a number
        #if it is a number it will ask again until only  a string is entered as the following three variables cannot be numbers
        while country.isnumeric():
            country = input('What is the country of the shoe: ').lower()
        
        while code.isnumeric():   
            code = input('What is the code of the shoe: ').lower()
        
        while product.isnumeric():
            product = input('What is the product name: ').lower()
        
        #here I check if the following two vairables are being entered as numbers with the Try/except error handling
        #if they are not numbers then the user will be required to re enter until the cost and quanitity are inputed as numbers
        while True:
            try:
                cost = int(input('What is the cost of the shoe: '))
                break
            except ValueError:
                print('You have not enter a number. ')
            
        while True:    
            try:    
                quantity = int(input('What is the quantity of the shoe: '))
                break
            except ValueError:
                print('You have not enter a number. ')
        
        #Here I display the new item that the user wants to add and give them an option to verify if the information is correct or not and the option
        #to reenter the information. If the user says the the information is correct it is appended into the 'show_list'
        #if no is entered the whole function will run again asking for the information again    
        print(f'''New Item:
Country:  {country} 
Code:     {code}
Product:  {product}
Cost:     {cost}
Quantity: {quantity}''')
        choice = input('Is the new item correct? Enter Yes to add to the system or No to re-enter the details: ').lower()

        if choice == "yes":
            new_shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(new_shoe)
            #here I write the new shoes to the file as well as adding it to the shoe_list objects
            with open('inventory.txt', 'a') as f:
                f.write('\n')
                f.write(str(new_shoe))
                return menu
        elif choice == "no":
            capture_shoes()
        elif choice == '-1':
            return menu
    
        overwrite()
         


def view_all():
    table = tabulate(data_list, headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity'], tablefmt= 'simple_grid' )
    print(table)
        

def re_stock():
      
    '''
    Below is my code for the compulsory requirment where I itirate through the object list and compare the quantities 
    I update the quantity with the choice that the users chooses and adds them together
    Lastly I convert the change back to strings so that they can be written back into the text file.
    
    min_object = min(shoe_list, key = Shoe.get_quantity)
    print(min_object)
    update_quantity = int(input('How many shoes would you like to re-order: '))
    min_object.quantity = update_quantity + int(min_object.quantity)
    str(min_object.quantity) 
    '''
    
    choice = int(input('What minimum quantity are you looking for? '))
    for count, line in enumerate(shoe_list, 1):
        if int(line.quantity) <= choice:
            print(count, '-', line)
        
    count_choice = int(input('Enter the number of the shoe you would like re-stock: '))
    for count, line in enumerate(shoe_list, 1):
        if count_choice == count:
            print(line)
            update_quantity = int(input('How many shoes would you like to re-order: '))
            line.quantity = update_quantity + int(line.quantity)
            str(line.quantity)
            print('Re-order placed. SUCCESS!')
            
            overwrite()
    

def seach_shoe():     
    #here I give my user choices on how they would like to search. They have options to search by all the columns and not only by code 
    #as I feel that this is more relevant  
    search_choice = input('''How would you like to search: 
Enter 'Country' if you want to search by Country: 
Enter 'Code' if you want to search by Code: 
Enter 'Product' if you want to search by Product:
Enter 'Cost' if you want to search by Cost: 
Enter 'Quantity' if you want to search by Quantity:
:''').lower()
    
    #once the user makes a choice the choice is compared with the objects to search for what the user has stated
    if search_choice == 'country':
        choice = input('What country shoe are you looking for: ')
        for line in shoe_list:
            if line.country.lower() == choice:
                print(line)
    elif search_choice == 'code':
        choice = input('What code shoe are you looking for: ')
        for line in shoe_list:
            if line.code.lower() == choice:
                print(line)
    elif search_choice == 'product':
        choice = input('What product name are you looking for: ')
        for line in shoe_list:
            if line.product.lower() == choice:
                print(line)
    elif search_choice == 'cost':
        choice = input('What cost of the shoe are you looking for: ')
        for line in shoe_list:
            if line.cost == choice:
                print(line)
    elif search_choice == 'quantity':
        choice = input('What quantity of shoe are you looking for: ')
        for line in shoe_list:
            if line.quantity == choice:
                print(line)
    elif search_choice == '-1':
        return menu
            

def value_per_item():
    #Here I use the tabulated data as I want to display it as a table
    #I append the value into the new column 
    total_value_table = []
    for line in data_list:
        total_value = int(line[3]) * int(line[4])
        line.append(total_value)
        total_value_table.append(line)
               
    print(tabulate(total_value_table, headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity', 'Total Value'], tablefmt= 'simple_grid' ))


def highest_qty():
    #Here I check for the max quantity like I did for the re_stock function
    #To make it more presentable I have included a function that prints the output into a box
    max_object = max(shoe_list, key = Shoe.get_quantity)
    x = max_object.code, max_object.product, 'is on SALE!!!'
    print_boxed_output(x)


def print_boxed_output(output):
    #Here I create a function that prints an output into a box to make certain outputs more presentable
    length = len(output) + 50  # Account for the box border

    horizontal_line = '+' + '-' * length + '+'
    empty_line = '|' + ' ' * length + '|'

    print(horizontal_line)
    print(empty_line)
    print('|  ', output, '     |')
    print(empty_line)
    print(horizontal_line)

def overwrite():
    with open('inventory.txt', 'w') as f:
        f.writelines('Country,Code,Product,Cost,Quantity' + '\n')
        for obj in shoe_list:
            f.writelines(str(obj) + '\n')
#==========Main Menu=============

read_shoes_data() #at start up of program so that it populates the shoe_list
tabular_data() #at start up to populate the table data list
while True:
    menu = input('''_________________________________________________
Enter the number you wish to proceed with
Enter -1 at anytime to return to the main menu:
1 - View all shoes
2 - Capture a new shoe
3 - Re-Stock shoes 
4 - Search shoes 
5 - Total cost of the shoes
6 - Shoe that is on sale
7 - Exit program
: ''').lower()

    if menu == '1':
        read_shoes_data()
        tabular_data()
        view_all()
    elif menu == '2':
        capture_shoes()
    elif menu == '3':
        re_stock()
    elif menu == '4':
        seach_shoe()
    elif menu == '5':
        value_per_item()
    elif menu == '6':
        highest_qty()
    elif menu == '7':
        exit()

    