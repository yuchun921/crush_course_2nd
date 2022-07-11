# Function

Learn to write functions.  
Learn ways to pass information to functions.

- Learn how to write certain functions whose primary job is to display information
- Other functions designed to process data and return a value or set of values
- Learn to store functions in separate files called modules

---

## Defining a Function

- keyword `def` to define a function. : def
- passing information in the parentheses of function. : name

```python
def say_hello(name):
    print(f"Hello, {name}")
```

<hr style="border-bottom: 1px double" />

## Arguments and Parameters 實參和形參

- 實參(Arguments): 實際存在的參數  
  (An argument is a piece of information that’s passed from a function call to a function.)
- 形參(Parameters): 形式上的參數, 沒有實際的值, 通過別人給值後才有意義  
  (A piece of information the function needs to do its job.)

```python
# name => parameters
def say_hello(name):
    print(f"Hello, {name}")


# "Peggy" => Arguments
say_hello("Peggy")
```

## Passing Arguments

A function definition can have multiple parameters, a function call may need multiple arguments.  
So can pass arguments to your functions in a number of ways.

- positional arguments 位置實參
- keyword arguments 關鍵字實參

### Positional Arguments

實參的傳入順序需與定義形參時的順序相同  
Need to be in the same order the parameters were written.

```python
# 形參順序 name, age
def introducing(name: str, age: int):
    print(f"Hi, my name is {name}, I'm {age} years old.")


# 實參傳入順序: name: Peggy, age: 27
introducing("Peggy", 27)  # Hi, my name is Peggy, I'm 27 years old.
```

#### Multiple Function Calls

可以根據需求多次call function, 要再介紹一個人時, 只要再調用 introducing() 就好了

### Keyword Arguments

將名稱和值一起傳給方法, 所以不會像位置形參一樣有搞錯傳入順序的可能  
Pass name-value pair to a function, so there's no confusion like positional arguments.

```python
# 形參順序 name, age
def introducing(name: str, age: int):
    print(f"Hi, my name is {name}, I'm {age} years old.")


# 以 name-value 傳入, 因此無需考慮順序
introducing(name="Peggy", age=27)  # Hi, my name is Peggy, I'm 27 years old.
introducing(age=44, name="Fiona")  # # Hi, my name is Fiona, I'm 44 years old.
```

<hr style="border-bottom: 1px double" />

## Default Values
定義方法時可以替形參指定預設值, 調用方法時若有提供實參給形參, 則方法會使用提供的實參值, 否則使用形參預設值.  
When writing a function, can define default values for each parameter, if argument provide values for parameter in the function call, use argument value, else use parameter default value.

定義方法時, 需要先列出沒有預設值的形參, 再列出有預設值的形參, python才能夠正確解讀形參位置  
When define function, any parameter with a default value needs to be  listed after all the parameters that don’t have default values.  
So Python to continue interpreting positional arguments correctly.

```python
# 形參順序 name, age
def introducing(age: int, name = "Someone"):
    print(f"Hi, my name is {name}, I'm {age} years old.")


# name, age都有傳入值, 因此會使用傳入的值
introducing(name="Peggy", age=27)  # Hi, my name is Peggy, I'm 27 years old.

# 只傳入age, 因此name會用形參default值
introducing(age=44)  # Hi, my name is Someone, I'm 44 years old.
```

<hr style="border-bottom: 1px double" />

## Return Values
可以使用`return`將值回傳給調用方法的一行程式, 將較重的工作移到方法中完成再傳回去  
Use `return` statement takes value from function call and sends it back, allow to move heavier program's to functon.

```python
def format_name(first_name, last_name):
    return f"{first_name} {last_name}".title()

full_name = format_name("Peggy", "chen")
print(f"My name is {full_name}") # My name is Peggy Chen
```