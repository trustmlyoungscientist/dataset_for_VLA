file_path = "./libero/libero/bddl_files/libero_object/pick_up_the_alphabet_soup_and_place_it_in_the_basket.bddl"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print(content)

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  

