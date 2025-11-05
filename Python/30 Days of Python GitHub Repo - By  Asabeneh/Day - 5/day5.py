#Q1 
emp_list = list()
print(emp_list)

#Q2 - Q4
five_items = ["item1", "item2", "item3", "item4", "item5"]
len_five_items = len(five_items)
print(len_five_items)

items_five_items = five_items[0], five_items[2], five_items[-1]
print(items_five_items)

#Q5
mixed_data_types = ["Abenese", 23, 5.11, False, "Jiaog Nag 20th Road Gzb"]

#Q6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

num_companies = len(it_companies)
print(num_companies)

company_positions = it_companies[0], it_companies[3], it_companies[-1]
print(company_positions)

it_companies[1] = "Samsung"
print(it_companies)

it_companies.insert(-1, "IT")
print(it_companies)

it_companies.insert(3, "panasonic")
print(it_companies)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
uperr = it_companies[3].upper()
print(uperr)

check_company = "Google" in it_companies
print(check_company)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
slice_list = it_companies[3:]
print(slice_list)

slice_last = it_companies[:-3]
print(slice_last)

slice_mid = it_companies[0:3] + it_companies[4:]
print(slice_mid)

it_companies.pop(0)
print(it_companies)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(3)
print(it_companies)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(6)
print(it_companies)

it_companies.clear()
print(it_companies)

#Q26 >
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

join_list = front_end + back_end
print(join_list)

full_stack = join_list.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)