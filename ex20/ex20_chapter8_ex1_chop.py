lst = list()
lst = [1,2,3,4,5,6]

def chop(passed_lst):
    if len(passed_lst) >= 2:
        result = delete_head(passed_lst)
        # print(passed_lst)
        result = tail(passed_lst)
        # print(passed_lst)
        return result

def delete_head(pass_lst):
    del pass_lst[0]

def tail(pass_lst):
    del pass_lst[-1]

def middle(passed_lst):
    result = passed_lst[1:(len(passed_lst) - 1)]
    return result

result_lst = middle(lst)
print(result_lst)
result_lst = chop(lst)
print(result_lst)