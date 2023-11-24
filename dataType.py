# int type data
hablu = 420;
print(type(hablu));

# float type data
gablu = 34.6;
print(type(gablu));

# complex type data
kodu = 420j;
print(type(kodu));

# string type data
yourName = 'hablu';
myName = 'Robin';
print(type(yourName));
print('My name is'+' '+myName);

# bool type data
Bool = True;
print(type(Bool));



x = 5;
y = 3;

print(x<y);

# binary type data
habluList = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 12,255];

habluByte = bytes(habluList);
print(habluByte);


# Binary type data byteArray

gabluList = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 12,255];

gabluByte = bytearray(gabluList);
gabluByte[1] = 100;
print(gabluByte[1]);


# None type data

x= None;
print(type(x));


# List type data
li = ['apple', 'mango', 'orange', 'banana']
print(li)
print(type(li))


# tuple data type

tup = (5, 10, 24, 45,68)
print(tup);
print(type(tup))



# Range type data

ran = range(10)
print(ran);
print(type(ran))

for i in ran:
    print(i)