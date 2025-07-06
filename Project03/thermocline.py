"""
thermocline.py

Svita Kiran
Fall 2023
10/01/23
CS152 Lab 3

This program will compute the thermocline.

python3 thermocline.py

"""

def density(temps):
    # finds and prints the density of the temperatures given
    list = []
    for t in temps:
        rho = 1000 * (1 - (t + 288.9414) * (t - 3.9863)**2 / (508929.2*(t + 68.12963)))
        list.append(rho)
    ans = ['{:.2f}'.format(t) for t in list]
    print(ans)
    return ans

def thermocline_depth(temps, depths):
    # finds and returns the depth of the thermocline after given temperatures and depths
    rhos = density(temps)
    drho_dz = []
    for i in range(len(rhos) - 1):
        x = (float(rhos[i + 1]) - float(rhos[i])) / (depths[i + 1] - depths[i])
        drho_dz.append(x)
    max_drho_dz = -1.0
    maxindex = -1
    for i in range(len(drho_dz)):
        if drho_dz[i] > max_drho_dz:
            max_drho_dz = drho_dz[i]
            maxindex = i
            thermoDepth = (depths[maxindex] + depths[maxindex + 1])/2
    return thermoDepth

def main():
     # prints the day and corresponding thermocline depth from 12:03:00PM into a new file
     fields = [10, 11, 16, 17, 15, 14, 13, 12]
     depths = [1, 3, 5, 7, 9, 11, 13, 15]

     file = open('GoldieJuly2019.csv', 'r')
     file.readline()
     day = 0

     newfile = open('ThermoclineData.csv', 'w')
     for line in file:
          words = line.split(',')
          if '12:03:00 PM' in words[0]:
               day += 1
               temps = []
               for i in range(len(depths)):
                    temps.append(float(words[fields[i]]))
               thermo_depth = thermocline_depth(temps, depths)
               print(str(day) + "," + str(thermo_depth))
               newfile.write(str(day) + "," + str(thermo_depth) + '\n')
     return

if __name__ == "__main__":
	main()
