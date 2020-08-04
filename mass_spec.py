#John Tucker
import copy

class Solution:
    def __init__(self):
        self.weight = float(input("Enter Mass Spectrometer Weight: "))
        self.ligand_weight = float(input("Enter Weight of Ligand: "))
        self.charge_input = int(input("Enter Charge (e.g. -2 or 1): "))
        self. accuracy_range = float(input("Enter Accuracy Range: "))
        self.count = 0
        ## Basic Weights
        Ligand = [self.ligand_weight, "Ligand", -2]
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

        self.out_order = dict()
        # list starting with heaviest elements first (optimization)
        self.particles = [OAc, MeOH, Ligand, Copper, Iodine, Bromine, Calcium, Potassium, Chlorine, Magnesium, Sodium,
                     Fluorine, Lithium, Hydrogen]
        self.answer(self.weight)
        self.print_answers()


    # the actual weight may be a multiple of the input weight and charge
    def answer(self, weight):
        for i in range(1,6):

            self.adjusted_weight = weight * i
            self.adjusted_charge = self.charge_input * i
            self.multiple = i
            self.combination(0, 0,0, [0] * (len(self.particles)))

    def combination(self, curr_weight, charge, index, arr):

        difference = abs(self.adjusted_weight - curr_weight)

        if difference < self.accuracy_range and self.adjusted_charge == charge:
            self.out_order[str(arr)] = ((copy.copy(arr), charge, difference))

        for i in range(6):
            if index == len(self.particles):
                return False

            weight = curr_weight + i * self.particles[index][0]
            curr_charge =  charge + i* self.particles[index][2]
            arr[index] = i
            if weight > self.adjusted_weight + self.accuracy_range:
                arr[index] = 0
                return False

            self.combination(weight,curr_charge,index+1, arr)
        arr[index] = 0




    def print_answers(self):
        # How many combinations
        how_many = len(self.out_order)

        # Creates a list of tuples in order
        sorted_elems = sorted(self.out_order.items(), key=lambda x: x[1][2], reverse = True)
        in_order = []

        # Iterate over the sorted sequence
        for elem in sorted_elems:
            final = ""
            charge = ""
            if elem[1][1] > 0:
                charge += "+"

            temp = ""
            for i in range(len(elem[1][0])):
                if elem[1][0][i] != 0:
                    if not temp:
                        temp+= str(elem[1][0][i]) + " " + self.particles[i][1]
                    else:
                        temp += ","  + " " + str(elem[1][0][i]) + " " + self.particles[i][1]

            charge += str(elem[1][1])
            final += "(difference: {}) charge: {} combination: {}"
            final = final.format(round(elem[1][2], 5),charge, temp)
            in_order.append(final)
        for elem in in_order:
            print(elem)

        bottom_message = "\n\n{} combinations found \nPrinted with increasing accuracy"
        print(bottom_message.format(how_many))

Master = Solution()