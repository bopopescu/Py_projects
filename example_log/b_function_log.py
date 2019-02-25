#python function pass argument as reference, but
#only mutable argument can be modified by function
def test_id(items):
    items.append({"wifi":4})

def main():
    items = [{"11AC":1},{"11ax:2"},{"BT":3} ]
    test_id(items)
    print("test id {}".format(items))
#test id[{'11AC': 1}, {'11ax:2'}, {'BT': 3}, {'wifi': 4}]
if __name__ == "__main__":
    main()

def try_to_change_list_reference(the_list):
    the_list = ["BRCM", "QCA","MRVL"]

outer_list = ["QTNA","INTL"]
print('outer_list =', outer_list)           #outer_list = ['QTNA', 'INTL']
try_to_change_list_reference(outer_list)
print('outer_list =', outer_list)           #outer_list = ['QTNA', 'INTL']



