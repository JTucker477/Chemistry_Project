#John Tucker

weight = float(input("Enter Mass Spectrometer Weight: "))
ligand_weight = float(input("Enter Weight of Ligand: "))
charge_input = int(input("Enter Charge : "))
accuracy_range = float(input("Enter Accuracy Range: "))

## Basic Weights
Ligand = [ligand_weight, "Ligand", -2]
Copper = [63.54, "Copper", 2]

OAc = [3758, "OAc", 2]
MeOH = [3707, "MeOH", 2]

## atomic mass of 1st column
Hydrogen = [1.008, "Hydrogen", 1]
Lithium = [6.941, "Lithium", 1]
Sodium = [22.98977, "Sodium", 1]
Potassium = [39.0983, "Potassium", 1]



## atomic mass of 2nd column
Magnesium = [24.305, "Magnesium", 2]
Calcium = [40.078, "Calcium", 2]


## atomic mass of halogens
Fluorine = [18.998, "Fluorine", -1]
Chlorine = [35.45, "Chlorine", -1]
Bromine = [79.904, "Bromine", -1]
Iodine = [126.90, "Iodine", -1]

out_order = dict()
count = 0
for aa in range(1, 6):
    # Prints how complete
    Percentage = (17 * (aa - 1))
    Percentage_final = "{}% complete"
    print(Percentage_final.format(Percentage))
    # Different types of adjusted weight
    adjusted_weight = weight * aa
    for a in range(6):
        difference_a = adjusted_weight - a * OAc[0]
        print(a, "OAc", difference_a)
        if difference_a < -1:
            break

        for b in range(6):
            difference_b = difference_a - b * MeOH[0]
            print(b, "MeOH", difference_b)
            if difference_b < -1:
                break
            # 1st column elements
            for c in range(6):
                difference_c = difference_b - c * Ligand[0]
                print(c, "Ligand", difference_c)
                if difference_c < -1:
                    break
                for d in range(6):
                    difference_d = difference_c - d * Copper[0]
                    print(d, "copper", difference_d)
                    if difference_d < -1:
                        break
                    for e in range(6):
                        #Checks to make sure there's at least 1 ligand or at least 1 copper
                        if (c == 0) and (d == 0):
                            break
                        difference_e = difference_d - e * Iodine[0]
                        print(e, "Iodine", difference_e)
                        if difference_e < -1:
                            break
                        overall_charge = a * OAc[2] + b * MeOH[2] + c * Ligand[2] + d * Copper[2] + e * Iodine[2]
                        count += 1

                        if (abs(difference_e) < accuracy_range) and (
                                charge_input * aa == overall_charge):
                            print('true?')
                            # Adds a plus sign if positive
                            overall_charge_present = ""
                            if overall_charge > 0:
                                overall_charge_present = "+" + str(
                                    overall_charge)
                            else:
                                overall_charge_present = str(overall_charge)
                            name = "{} charge: {} {}, {} {}, {} {}, {} {}, {} {},"
                            name = name.format(overall_charge_present, c, Ligand[1], d, Copper[1], a, OAc[1], b, MeOH[1], e, Iodine[1])
                            out_order[name] = difference_e

print("100% complete\n")
print('count', count)

#Prints how many combinations were made
how_many = len(out_order)
top_message = "{} combinations found\n\nIn order list of combinations:"
print(top_message.format(how_many))


# Creates a list of tuples in order
listofTuples = sorted(out_order.items() ,  key=lambda x: abs(x[1]))

in_order =[]
# Iterate over the sorted sequence
for elem in listofTuples :
    stringboi = "{}         difference = {}"
    stringboi = stringboi.format(elem[0] , elem[1])
    in_order.append(stringboi)

for elem in range(len(in_order)):
    print(in_order[elem])
