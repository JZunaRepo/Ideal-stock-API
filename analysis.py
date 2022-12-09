import statistics as stats
import matplotlib.pyplot as plt
import csv

SBUX_data = []
with open ("SBUX.csv", "r") as infile:
  reader = csv.DictReader(infile)
  for row in reader:
    SBUX_data.append(row)

i=0
SBUX_stdev_data = []
while i <len(SBUX_data):
  if i + 1 >= len(SBUX_data) or i + 2 >= len(SBUX_data) or i + 3 >= len(SBUX_data) or i + 4 >= len(SBUX_data):
    break
  Day_1 = float(SBUX_data[i]["Closing_Price"])
  Day_2 = float(SBUX_data[i+1]["Closing_Price"])
  Day_3 = float(SBUX_data[i+2]["Closing_Price"])
  Day_4 = float(SBUX_data[i+3]["Closing_Price"])
  Day_5 = float(SBUX_data[i+4]["Closing_Price"])

  pop_stdev = stats.pstdev([Day_1,Day_2,Day_3,Day_4,Day_5])
  SBUX_stdev_data.append(pop_stdev)
  i += 5

week = 0 

for stdev in SBUX_stdev_data:
  week += 1 
  print(f"SBUX Week {week} Stdv is: {stdev}")

plt.plot(SBUX_stdev_data)
plt.title("Stock Weekly Standar Deviation")
plt.ylabel("STDV of Closing Price")
plt.show()