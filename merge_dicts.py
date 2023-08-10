def merge_dicts_list(dicts_list):
    merged_dict = {}
    
    for dictionary in dicts_list:
        for key, value in dictionary.items():
            merged_dict.setdefault(key, []).append(value)
    
    return merged_dict

employee1 = {'first_name': 'Ali', 'age': 23, 'salary': 4000}
employee2 = {'first_name': 'Mohamed', 'age': 24, 'salary': 8000}
employee3 = {'first_name': 'Khaled', 'age': 25, 'salary': 1000}
employee4 = {'first_name': 'Ibrahim', 'age': 27, 'salary': 7000}
employee5 = {'first_name': 'Zaid', 'age': 30, 'salary': 9000}

employees_list = [employee1, employee2, employee3, employee4, employee5]
merged_data = merge_dicts_list(employees_list)
print(merged_data)