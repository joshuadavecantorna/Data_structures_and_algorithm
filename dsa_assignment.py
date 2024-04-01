import matplotlib.pyplot as plt
from functions import all_expressions

x_values = []

def functions_result_write(y_values_dict):
    with open("output_results.txt", "w") as file:
        for name_of_expression, values in y_values_dict.items():
            file.write(f"Result of the Expression ({name_of_expression}):\n[")
            for value in values:
                file.write(f"{int(round(value))},")# nag gamit ako ng int tapos round para ma round off yung result kasi marami yung decimals
            file.write("]\n\n\n")

with open("x_val.txt", 'r') as file:# i read nya yung file ko na x_val na may int na 1 to 50
    data = file.readlines()
    for d in data:
        x_values.extend([int(value) for value in d.split(',')])

def solving_expression(x_values, expression):
    y_values = [expression(x) for x in x_values]
    return y_values

def graph_expression(x_values, y_values, name_of_expression):#dito yung graph ng individual expressions 
    plt.plot(x_values, y_values, label=name_of_expression, linewidth=2)
    plt.title(f"Graph of {name_of_expression}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def graph_all_expressions(x_values, y_values_dict):# dito naman yung graph if lahat i solve
    for name_of_expression, y_values in y_values_dict.items():
        plt.plot(x_values, y_values, label=name_of_expression, linewidth=2)
    
    plt.title("Graph of All Expressions")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

functions_result_write({})

try:
    choice = int(input("\nEnter the number of the expression you want to solve: "))#pipili ang user kung ano na equation ang kanyang i solve
    
    if choice == 11:
        y_values_dict = {}
        for expression_name, expression in all_expressions.expressions.items():
            y_values = solving_expression(x_values, expression)
            y_values_dict[expression_name] = y_values
        
        graph_all_expressions(x_values, y_values_dict)

        functions_result_write(x_values, y_values_dict)
        
    elif 1 <= choice <= len(all_expressions.expressions):
        expression_name = list(all_expressions.expressions.keys())[choice - 1]
        expression = all_expressions.expressions[expression_name]
        
        # i solve nya dito at i graph
        y_values = solving_expression(x_values, expression)
        graph_expression(x_values, y_values, expression_name)

        functions_result_write({expression_name: y_values})#after ma solve is i write nya na sa file
        
    else:
        print("Invalid choice. Please enter a number from 1 to 11")
        
except ValueError:
    print("Invalid input. Please enter a number.")