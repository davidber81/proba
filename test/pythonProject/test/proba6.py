def add_element_to_list(element1, list_to_add=None):
  if list_to_add is None:
    list_to_add = []
  list_to_add.append(element1)
  return list_to_add

values_list_2 = add_element_to_list(element1=42)
print(values_list_2)
add_element_to_list(element1=1, list_to_add=values_list_2)
print(values_list_2)

