import pandas as pd

data_file = pd.read_csv("./2018_Central_Park_Squirrel_Census.csv")
df = pd.DataFrame(data_file)

fur_colors = df["Primary Fur Color"]

list_colors = fur_colors.to_list()

colored_squirrel = []

total_gray = "Gray", list_colors.count("Gray")
total_red = "Red", list_colors.count("Cinnamon")
total_black = "Black", list_colors.count("Black")

colored_squirrel.append(total_gray)
colored_squirrel.append(total_red)
colored_squirrel.append(total_black)

df_squirrel = pd.DataFrame(colored_squirrel)
cleaned_colors = df_squirrel.rename(columns={0: "Fur Color", 1: "Count"})

cleaned_colors.to_csv("squirrel_count.csv")