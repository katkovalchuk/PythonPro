# float
a = 6.7
print(type(a))
# str
b = "this is my string"
print(type(b))
# List[float]
my_list = [1.2, 3, 4, 5.6]
print(type(my_list))
# Tuple[str,float]
my_tuple = ("this is my string", 6.7)
print(type(my_tuple))
# Dict[float, float]
my_dict = {"first_float": 23.9, "second_float": 56.8}
print(type(my_dict))
# Set[str]
my_set = {"this is my string"}
print(type(my_set))
# bool
c = bool(5 > 2)  # True
print(type(c))
# Set[bool]
my_set2 = {False}
print(type(my_set2))
# Set[Tuple[float,int,str]]
my_set3 = {(34.5, 2, "this is my string")}
print(type(my_set3))
# int
d = 8
print(type(d))
# List[str]
my_list2 = ["this is my string"]
print(type(my_list2))
# Dict[float, Set[Tuple[str]]]
my_dict2 = {27.0: {("this is my string", )}}
print(type(my_dict2))
# Dict[Tuple[float,bool,str], bool]
my_dict3 = {(34.5, True, "this is my string"): False}
print(type(my_dict3))
# Dict[str, str]
my_dict4 = {"first_str": "this is my string", "second_str": "this is my other string"}
print(type(my_dict4))
# Tuple[int]
my_tuple2 = (5, )
print(type(my_tuple2))
# Dict[Tuple[float,float], List[bool]]
my_dict5 = {(56.4, 23.6): [True]}
print(type(my_dict5))
# List[bool]
my_list3 = [False]
print(type(my_list3))
# Set[Any]
my_set4 = {"this is my string", "this is my other string"}
print(type(my_set4))
# List[int]
my_list4 = [4]
print(type(my_list4))
# List[Any]
my_list5 = ["this is my string", "this is my other string"]
print(type(my_list5))
# Dict[int, List[Any]]
my_dict6 = {8: ["this is my string", "this is my other string"]}
print(type(my_dict6))
# Tuple[int,bool]
my_tuple3 = (5, False)
print(type(my_tuple3))
# Tuple[float,str]
my_tuple4 = (5.7, "this is my string")
print(type(my_tuple4))
# Tuple[bool]
my_tuple5 = (True, )
print(type(my_tuple5))
# Tuple[str,str]
my_tuple6 = ("this is my string", "this is my other string")
print(type(my_tuple6))
# Tuple[int,bool,float]
my_tuple7 = (9, False, 7.4)
print(type(my_tuple7))
# Dict[int, Set[str]]
my_dict7 = {7: {"this is my string"}}
print(type(my_dict7))
# Tuple[float,float]
my_tuple8 = (9.3, 0.2)
print(type(my_tuple8))
# Set[int]
my_set5 = {5}
print(type(my_set5))
# Dict[Tuple[bool,int,int], float]
my_dict8 = {(False, 3, 7): 9.2}
print(type(my_dict8))
# Dict[float, int]
my_dict9 = {0.5: 4}
print(type(my_dict9))
# Tuple[bool,float]
my_tuple9 = (True, 8.5)
print(type(my_tuple9))
# List[Tuple[bool,float]]
my_list6 = [(False, 3.5)]
print(type(my_list6))
# List[Tuple[int]]
my_list7 = [(5, )]
print(type(my_list7))
# Tuple[bool,str]
my_tuple10 = (True, "this is my string")
print(type(my_tuple10))
# Tuple[float]
my_tuple11 = (6.4, )
print(type(my_tuple11))