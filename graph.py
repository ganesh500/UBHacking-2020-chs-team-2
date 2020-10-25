def graph():
  import pandas as pd
  import matplotlib.pyplot as plt
  df = pd.read_csv('all_states_history.csv')
  plt.barh(df.state.head(25), df.positive.head(25), align="center", color="green")
  plt.ylabel('U.S. States')
  plt.xlabel('Positive Cases')
  plt.title('Positive COVID-19 cases in each state')
  plt.show()

  plt.barh(df.state.tail(25), df.positive.tail(25), align="center", color="green")
  plt.style.use("fivethirtyeight")
  plt.ylabel('U.S. States')
  plt.xlabel('Positive Cases')
  plt.title('Positive COVID-19 cases in each state cont')
  plt.show()

  plt.barh(df.state.head(25), df.death.head(25),align="center", color="red")
  plt.style.use("fivethirtyeight")
  plt.ylabel('U.S. States')
  plt.xlabel('Deaths')
  plt.title('Deaths Due to COVID-19')
  plt.show()

  plt.barh(df.state.tail(25), df.death.tail(25),align="center", color="red")
  plt.style.use("fivethirtyeight")
  plt.ylabel('U.S. States')
  plt.xlabel('Deaths')
  plt.title('Deaths Due to COVID-19')
  plt.show()
  return graph()