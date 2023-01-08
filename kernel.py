import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numba
import sklearn.linear_model

@numba.jit
def medical_language(dataset):
  commands = {
    "line_chart": line_chart,
    "histogram": histogram,
    "scatterplot": scatterplot,
    "query": query,
    "barplot": barplot,
    "linear_regression": linear_regression
  }

  for line in dataset:
    parts = line.split(" ")
    cmd = parts[0]
    args = parts[1:]

    if cmd in commands:
      commands[cmd](args)
    else:
        print("Invalid Query")

def line_chart(args):
  x = args[0]
  y = args[1]

  plt.plot(dataset[x], dataset[y])
  plt.show()

def histogram(args):
  for col in args:
    plt.hist(dataset[col])
    plt.show()

def scatterplot(args):
  x = args[0]
  y = args[1]

  plt.scatter(dataset[x], dataset[y])
  plt.show()

def query(args):
  query = " & ".join(args)

  filtered_data = dataset.query(query)
  print(filtered_data)

def barplot(args):
  for col in args:
    plt.bar(dataset[col], dataset.index)
    plt.show()

def linear_regression(args):
  x = args[0]
  y = args[1]

  model = sklearn.linear_model.LinearRegression()

  model.fit(dataset[[x]], dataset[y])

  print("Coefficients:", model.coef_)
  print("Intercept:", model.intercept_)

dataset = pd.read_csv(input("What is the path to the dataset your working on? "))

'''commands = [
  "scatterplot AGE RACE",
  "query AGE>14",
  "barplot FEMALE",
  "query AGE>13 APRDRG>700,
  "linear_regression AGE LOS
]'''

command_chain = []
history = []

i = 1
while i > 0:
    line = input(f"Command [{i}]: ")

    if line == "view history":
        if len(history) > 0:
            for v in history:
                print(v)
        else:
            print("You havent written any queries yet!")

    command_chain.append(line)
    try:    
        medical_language(command_chain)
    except:
        print("Error Occured: Try again with the right syntax")
    i+=1
    history.append(command_chain[0])
    command_chain.pop()
    

'''input_str = 'survey.csv --plot bar Age treatment'
execute(input_str)'''
