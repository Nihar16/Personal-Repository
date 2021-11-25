def attendancesheet(my_list):
    print("inside fn",my_list)
    my_list.extend([1,'anuja'])
    return my_list

new_list=[2,'python']
print("outside fn",new_list)
print("return object",attendancesheet(new_list))
print("outside fn again",new_list)
