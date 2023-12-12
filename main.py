def main menu():
    menu =  """
    Welcome ro Nurses Program
    Pick an Option:
    
    [1] Load the data
    [2] Process the data
    [3] Visualize the data
    [4] Export the data
    
    
    Enter the selection:"""


    response =int(input(menu))
    # validation
    return response



def run():
    response = main_menu()
    if response ==1:
        load_data()

