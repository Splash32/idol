def divider(a, b):

   try:

       return a / b

   except ZeroDivisionError:

       print("Ви не можете ділити на нуль!")

       return 0

   except TypeError:

       print("Ви не можете ділити нечислові значення!")

       return 0

   except ValueError:

       print("Ви не можете ділити нечислові значення!")

       return 0

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

result = []

for key in data:

   res = divider(key, data[key])

   result.append(res)

print(result)