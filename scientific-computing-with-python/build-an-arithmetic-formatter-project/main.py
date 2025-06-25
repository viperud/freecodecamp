def arithmetic_arranger(problems, show_answers=False):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    final = ''
    if len(problems) > 5:
        return('Error: Too many problems.')

    for problem in problems:
        problem_split = problem.split()
        digit1 = problem_split[0]
        digit2 = problem_split[2]
        oprt = problem_split[1]
        
        if not oprt == "-" and not oprt == '+':
            return("Error: Operator must be '+' or '-'.")

        if not digit1.isdigit() or not digit2.isdigit():
            return('Error: Numbers must only contain digits.')

        if len(digit1) > 4 or len(digit2) > 4:
            return('Error: Numbers cannot be more than four digits.')

        if oprt == '+':
            answer = str(int(digit1) + int(digit2))
        elif oprt == '-':
            answer = str(int(digit1) - int(digit2))

        maximum = max(len(digit1), len(digit2))

        total_len = maximum + 2

        line1 += (' ' * (total_len - len(digit1))) + digit1 + '    '
        line2 += oprt + (' ' * (total_len - len(digit2) - 1)) + digit2 + '    '

        line3 += '-' * total_len + '    '

        line4 += (' ' * (total_len - len(answer))) + answer + '    '

    final = line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4]
    if show_answers:
        final += '\n' + line4[:-4]

    return final

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')