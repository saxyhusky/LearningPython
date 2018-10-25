#Task 1
start = (2, 123.4567, 1000, 12345.67)
print("file_{:0>3d} :   {:.2f}, {:.2e}, {:.3g}".format(start[0],start[1],start[2],start[3]))

#Task 2
print (f"file_{start[0]:0>3d} :   {start[1]:.2f}, {start[2]:.2e}, {start[3]:.3g}")

#Task 3
def formatter(in_tuple):
    l=len(in_tuple)
    print(("the {} numbers are: " + ",".join(["{}"]*l)).format(l, *in_tuple))

#Task 4
list=(4,30,2017,2,27)
print(f"{list[3]:0>2d} {list[4]} {list[2]} {list[0]:0>2d} {list[1]}")

#Task 5
fruit = ["oranges", 1.3, "lemons", 1.1]
print(f"the weight of an {fruit[0][:-1].upper()} is {fruit[1]*1.2} and the weight of a {fruit[2][:-1].upper()} is {fruit[3]*1.2}")

#Task 6
rows=(("bob", 27,"$99.88"),("Sally", 100, "$10000.00"),("Laura", 1, "$0.00"))
for row in rows:
    print("{:10} {:^10} {:<10} ".format(*row))