# create function that extracts integers from a string
# and returns 0 if no integers found


def extract_int(string):
    try:
        return int(''.join([ch for ch in string if ch.isdigit()]))
    except:
        return 0


# open the file with text to read the lines to a list subj_lines
with open('task_6_file.txt', 'r', encoding='utf-8') as my_file:
    subj_lines = [line.strip().split(': ') for line in my_file]
print(subj_lines)

dict_keys = [el[0] for el in subj_lines]

dict_vals = [sum(list(map(extract_int, el[1].split()))) for el in subj_lines]

res_dict = {key: value for key, value in zip(dict_keys, dict_vals)}
print(res_dict)