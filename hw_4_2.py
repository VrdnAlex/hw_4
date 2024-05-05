def get_cats_info(path):
    cats_list = list()

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                cat_info = line.strip().split(',')
                cat = {
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": cat_info[2]
                }
                cats_list.append(cat)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cats_list
