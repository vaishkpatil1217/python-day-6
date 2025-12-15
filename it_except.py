list=["vaish","rohit","aaru","hrishi","palu"]

it=iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("stop iteration")
        break