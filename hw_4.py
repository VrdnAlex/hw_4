def total_salary(path):
    salary = list()

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_developers = len(lines)

            for line in lines:
                salary.append(int(line.strip().split(',')[1]))

            total_salary = sum(salary)

            average_salary = total_salary / num_developers
            return total_salary, average_salary

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

