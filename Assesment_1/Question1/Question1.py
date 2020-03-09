import json
example = {"data": [
                [1,2,3],
                [4,5,6],
                [7,8,9]]}

def dict_sum(dictionary):
    total = 0
    jsondict = {}
    for i in dictionary['data']:
        each = sum(i)
        total += each
    jsondict['sum'] = total
    with open('answer.json', 'w') as file_obj:
        json.dump(jsondict, file_obj, indent=4)


if __name__ == '__main__':
    dict_sum(example)