from operator import add, sub, mul, truediv, floordiv

def evaluate_s_expression(key, expression_dictionary):
    expression = expression_dictionary[key]
    if not isinstance(expression, list):
        return expression
    else:
        return expression[1](evaluate_s_expression(expression[0], expression_dictionary), 
                             evaluate_s_expression(expression[2], expression_dictionary))


monkey_business = {}
with open("day_21.txt", "r") as input_data:
    for line in input_data:
        line = line.strip().split(": ")
        if line[1].isnumeric():
            monkey_business[line[0]] = int(line[1])
        else:
            op_er_ation = line[1].split(" ")
            if op_er_ation[1] == "+":
                op_er_ation[1] = add
            if op_er_ation[1] == "-":
                op_er_ation[1] = sub
            if op_er_ation[1] == "*":
                op_er_ation[1] = mul
            if op_er_ation[1] == "/":
                op_er_ation[1] = floordiv
            monkey_business[line[0]] = op_er_ation

print(evaluate_s_expression("root", monkey_business))            
