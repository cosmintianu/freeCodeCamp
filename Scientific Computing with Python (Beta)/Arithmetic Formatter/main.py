def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems :
        parts = problem.split()

        if parts[1] not in ('+','-'):
            return "Error: Operator must be '+' or '-'."
        
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        width = max(len(parts[0]),len(parts[2])) + 2

        first_line.append(parts[0].rjust(width))
        second_line.append(parts[1] + " " + parts[2].rjust(width - 2))
        dashes.append("-" * width)

        if show_answers:
            if parts[1] == '+':
                answer = str(int(parts[0]) + int(parts[2]))
            else:
                answer = str(int(parts[0]) - int(parts[2]))
            answers.append(answer.rjust(width))
        
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes) 
    )

    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)

    print (arranged_problems)    

    return arranged_problems


# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)

arithmetic_arranger(["3801 - 2", "123 + 49"],False)

print("  3801      123\n-    2    +  49\n------    -----")
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')