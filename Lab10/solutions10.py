def q01():
    """Create a function that receives a collection of elements (e.g., list, set, tuple), if the collection is mutable,
    convert the collection into an immutable collection, otherwise return the original collection. Note the values of the
    elements should not be changes. """
    def return_tuple(coll):
        if type(coll) in (set, list):
            print(f"Converting {type(coll).__name__} to tuple")
            return tuple(coll)
        else:
            print("already a tuple)")
            return coll

    set1 = {1, 2, 3}
    list1 = [1, 2, 3]
    tuple1 = (1, 2, 3)

    print(type(return_tuple(set1)))
    print(type(return_tuple(list1)))
    print(type(return_tuple(tuple1)))


import random
def q02():
    outer_list = []
    for o in range(10):
        inner_list = []
        for i in range(10):
            inner_list.append(random.randint(1,100))

        outer_list.append(inner_list)

    print(len(outer_list))
    for i in outer_list:
        print(i)
    print()
    print(outer_list[6])

q02()