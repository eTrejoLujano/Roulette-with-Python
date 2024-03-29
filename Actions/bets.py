def straight_up(bigrisk):
    if bigrisk == "37":
        return "00"
    else:
        return bigrisk


def splits1(split1):
    splitone = {"00": "null", "0": "null", "1": "1,2", "2": "1,2", "3": "2,3", "4": "1,4", "5": "4,5",
                "6": "5,6", "7": "4,7", "8": "7,8", "9": "8,9", "10": "7,10", "11": "10,11", "12": "11,12",
                "13": "10,13", "14": "13,14", "15": "14,15", "16": "13,16", "17": "16,17", "18": "17,18", "19": "16,19",
                "20": "19,20", "21": "20,21", "22": "19,22", "23": "22,23", "24": "23,24", "25": "22,25", "26": "25,26",
                "27": "26,27", "28": "25,28", "29": "28,29", "30": "29,30", "31": "28,31", "32": "31,32", "33": "32,33",
                "34": "31,34", "35": "34,35", "36": "35,36"}
    return splitone[split1]


def splits2(split2):
    splittwo = {"00": "null", "0": "null", "1": "1,4", "2": "2,3", "3": "3,6", "4": "4,4", "5": "2,5",
                "6": "3,6", "7": "7,8", "8": "5,8", "9": "6,9", "10": "10,11", "11": "8,11", "12": "9,12",
                "13": "13,14", "14": "11,14", "15": "12,15", "16": "16,17", "17": "14,17", "18": "15,18", "19": "19,20",
                "20": "17,20", "21": "18,21", "22": "22,23", "23": "20,23", "24": "21,24", "25": "25,26", "26": "23,26",
                "27": "24,27", "28": "28,29", "29": "26,29", "30": "27,30", "31": "31,32", "32": "29,32", "33": "30,33",
                "34": "34,35", "35": "32,35", "36": "33,36"}
    return splittwo[split2]


def splits3(split3):
    splitthree = {"00": "null", "0": "null", "1": "null", "2": "2,5", "3": "null", "4": "4,7", "5": "5,6",
                  "6": "6,9", "7": "7,10", "8": "8,9", "9": "9,12", "10": "10,13", "11": "11,12", "12": "12,15",
                  "13": "13,16", "14": "14,15", "15": "15,18", "16": "16,19", "17": "17,18", "18": "18,21", "19": "19,22",
                  "20": "20,21", "21": "21,24", "22": "22,25", "23": "23,24", "24": "24,27", "25": "25,28", "26": "26,27",
                  "27": "27,30", "28": "28,31", "29": "29,30", "30": "30,33", "31": "31,34", "32": "32,33", "33": "33,36",
                  "34": "null", "35": "35,36", "36": "3null"}
    return splitthree[split3]


def splits4(split4):
    splitfour = {"00": "null", "0": "null", "1": "null", "2": "null", "3": "null", "4": "null", "5": "5,8",
                 "6": "null", "7": "null", "8": "8,11", "9": "null", "10": "null", "11": "11,14", "12": "null",
                 "13": "null", "14": "14,17", "15": "null", "16": "null", "17": "17,20", "18": "null", "19": "null",
                 "20": "20,23", "21": "null", "22": "null", "23": "23,26", "24": "null", "25": "null", "26": "26,29",
                 "27": "null", "28": "null", "29": "29,32", "30": "null", "31": "null", "32": "32,35", "33": "null",
                 "34": "null", "35": "null", "36": "null"}
    return splitfour[split4]


def black_red(blackred):
    colors = {"00": "green", "0": "green", "1": "red", "2": "black", "3": "red", "4": "black", "5": "red",
              "6": "black", "7": "red", "8": "black", "9": "red", "10": "black", "11": "black", "12": "red",
              "13": "black", "14": "red", "15": "black", "16": "red", "17": "black", "18": "red", "19": "red",
              "20": "black", "21": "red", "22": "black", "23": "red", "24": "black", "25": "red", "26": "black",
              "27": "red", "28": "black", "29": "black", "30": "red", "31": "black", "32": "red", "33": "black",
              "34": "red", "35": "black", "36": "red"}
    return colors[blackred]


def odd_even(oddeven):
    if (int(oddeven) % 2) == 0:
        return "even"
    else:
        return "odd"


def columns123(spinb):
    columns = {"00": "null", "0": "null", "1": "1", "2": "2", "3": "3", "4": "1", "5": "2",
               "6": "3", "7": "1", "8": "2", "9": "3", "10": "1", "11": "2", "12": "3",
               "13": "1", "14": "2", "15": "3", "16": "1", "17": "2", "18": "3", "19": "1",
               "20": "2", "21": "3", "22": "1", "23": "2", "24": "3", "25": "1", "26": "2",
               "27": "3", "28": "1", "29": "2", "30": "3", "31": "1", "32": "2", "33": "3",
               "34": "1", "35": "2", "36": "3"}
    return columns[spinb]


def dozens123(dozen):
    thedozen = {"00": "null", "0": "null", "1": "1", "2": "1", "3": "1", "4": "1", "5": "1",
                "6": "1", "7": "1", "8": "1", "9": "1", "10": "1", "11": "1", "12": "1",
                "13": "2", "14": "2", "15": "2", "16": "2", "17": "2", "18": "2", "19": "2",
                "20": "2", "21": "2", "22": "2", "23": "2", "24": "2", "25": "3", "26": "3",
                "27": "3", "28": "3", "29": "3", "30": "3", "31": "3", "32": "3", "33": "3",
                "34": "3", "35": "3", "36": "3"}
    return thedozen[dozen]


def bothhalves(half):
    halfs = {"00": "null", "0": "null", "1": "1", "2": "1", "3": "1", "4": "1", "5": "1",
             "6": "1", "7": "1", "8": "1", "9": "1", "10": "1", "11": "1", "12": "1",
             "13": "1", "14": "1", "15": "1", "16": "1", "17": "1", "18": "1", "19": "2",
             "20": "2", "21": "2", "22": "2", "23": "2", "24": "2", "25": "2", "26": "2",
             "27": "2", "28": "2", "29": "2", "30": "2", "31": "2", "32": "2", "33": "2",
             "34": "2", "35": "2", "36": "2"}
    return halfs[half]


def street(stree):
    streets = {"00": "null", "0": "null", "1": "1,2,3", "2": "1,2,3", "3": "1,2,3", "4": "4,5,6", "5": "4,5,6",
               "6": "4,5,6", "7": "7,8,9", "8": "7,8,9", "9": "7,8,9", "10": "10,11,12", "11": "10,11,12", "12": "10,11,12",
               "13": "13,14,15", "14": "13,14,15", "15": "13,14,15", "16": "16,17,18", "17": "16,17,18", "18": "16,17,18", "19": "19,20,21",
               "20": "19,20,21", "21": "19,20,21", "22": "22,23,24", "23": "22,23,24", "24": "22,23,24", "25": "25,26,27", "26": "25,26,27",
               "27": "25,26,27", "28": "28,29,30", "29": "28,29,30", "30": "28,29,30", "31": "31,32,33", "32": "31,32,33", "33": "31,32,33",
               "34": "34,35,36", "35": "34,35,36", "36": "34,35,36"}
    return streets[stree]


def lines1(line1):
    lineone = {"00": "null", "0": "null", "1": "1-6", "2": "1-6", "3": "1-6", "4": "1-6", "5": "1-6",
               "6": "1-6", "7": "7-12", "8": "7-12", "9": "7-12", "10": "7-12", "11": "7-12", "12": "7-12",
               "13": "13-18", "14": "13-18", "15": "13-18", "16": "13-18", "17": "13-18", "18": "13-18", "19": "19-24",
               "20": "19-24", "21": "19-24", "22": "19-24", "23": "19-24", "24": "19-24", "25": "25-30", "26": "25-30",
               "27": "25-30", "28": "25-30", "29": "25-30", "30": "25-30", "31": "31-36", "32": "31-36", "33": "31-36",
               "34": "31-36", "35": "31-36", "36": "31-36"}
    return lineone[line1]


def lines2(line2):
    linetwo = {"00": "null", "0": "null", "1": "null", "2": "null", "3": "null", "4": "4-9", "5": "4-9",
               "6": "4-9", "7": "4-9", "8": "4-9", "9": "4-9", "10": "10-15", "11": "10-15", "12": "10-15",
               "13": "10-15", "14": "10-15", "15": "10-15", "16": "16-21", "17": "16-21", "18": "16-21", "19": "16-21",
               "20": "16-21", "21": "16-21", "22": "22-27", "23": "22-27", "24": "22-27", "25": "22-27", "26": "22-27",
               "27": "22-27", "28": "28-33", "29": "28-33", "30": "28-33", "31": "28-33", "32": "28-33", "33": "28-33",
               "34": "null", "35": "null", "36": "null"}
    return linetwo[line2]


def corner(corn):
    corners = {"00": "null", "0": "null", "1": "1,2,4,5", "2": "1,2,4,5", "3": "2,3,5,6", "4": "1,2,4,5", "5": "1,2,4,5",
               "6": "2,3,5,6", "7": "4,5,7,8", "8": "4,5,7,8", "9": "5,6,8,9", "10": "7,8,10,11", "11": "7,8,10,11", "12": "8,9,11,12",
               "13": "10,11,13,14", "14": "10,11,13,14", "15": "11,12,14,15", "16": "13,14,16,17", "17": "13,14,16,17", "18": "14,15,17,18", "19": "16,17,19,20",
               "20": "16,17,19,20", "21": "17,18,20,21", "22": "19,20,22,23", "23": "19,20,22,23", "24": "20,21,23,24", "25": "22,23,25,26", "26": "22,23,25,26",
               "27": "23,24,26,27", "28": "25,26,28,29", "29": "25,26,28,29", "30": "26,27,29,30", "31": "28,29,31,32", "32": "28,29,31,32", "33": "29,30,32,33",
               "34": "31,32,34,35", "35": "31,32,34,35", "36": "32,33,35,36"}
    return corners[corn]


def corner2(corn2):
    cornerstwo = {"00": "null", "0": "null", "1": "null", "2": "2,3,5,6", "3": "null", "4": "4,5,7,8", "5": "2,3,5,6",
                  "6": "5,6,8,9", "7": "7,8,10,11", "8": "5,6,8,9", "9": "8,9,11,12", "10": "10,11,13,14", "11": "8,9,11,12", "12": "11,12,14,15",
                  "13": "13,14,16,17", "14": "11,12,14,15", "15": "14,15,17,18", "16": "16,17,19,20", "17": "14,15,17,18", "18": "17,18,20,21", "19": "19,20,22,23",
                  "20": "17,18,20,21", "21": "20,21,23,24", "22": "22,23,25,26", "23": "20,21,23,24", "24": "23,24,26,27", "25": "25,26,28,29", "26": "23,24,26,27",
                  "27": "26,27,29,30", "28": "28,29,31,32", "29": "26,27,29,30", "30": "29,30,32,33", "31": "31,32,34,35", "32": "29,30,32,33", "33": "32,33,35,36",
                  "34": "null", "35": "32,33,35,36", "36": "null"}
    return cornerstwo[corn2]


def corner3(corn3):
    cornersthree = {"00": "null", "0": "null", "1": "null", "2": "null", "3": "null", "4": "null", "5": "4,5,7,8",
                    "6": "null", "7": "null", "8": "7,8,10,11", "9": "null", "10": "null", "11": "10,11,13,14", "12": "null",
                    "13": "null", "14": "13,14,16,17", "15": "null", "16": "null", "17": "16,17,19,20", "18": "null", "19": "null",
                    "20": "19,20,22,23", "21": "null", "22": "null", "23": "22,23,25,26", "24": "null", "25": "null", "26": "25,26,28,29",
                    "27": "null", "28": "null", "29": "28,29,31,32", "30": "null", "31": "null", "32": "31,32,34,35", "33": "null",
                    "34": "null", "35": "null", "36": "null"}
    return cornersthree[corn3]


def corner4(corn4):
    cornersfour = {"00": "null", "0": "null", "1": "null", "2": "null", "3": "null", "4": "null", "5": "5,6,8,9",
                   "6": "null", "7": "null", "8": "8,9,11,12", "9": "null", "10": "null", "11": "11,12,14,15", "12": "null",
                   "13": "null", "14": "14,15,17,18", "15": "null", "16": "null", "17": "17,18,20,21", "18": "null", "19": "null",
                   "20": "20,21,23,24", "21": "null", "22": "null", "23": "23,24,26,27", "24": "null", "25": "null", "26": "26,27,29,30",
                   "27": "null", "28 ": "null", "29": "29,30,32,33", "30": "null", "31": "null", "32": "32,33,35,36", "33": "null",
                   "34": "null", "35": "null", "36": "null"}
    return cornersfour[corn4]


def topline(basket):
    baskets = {"00": "yes", "0": "yes", "1": "yes", "2": "yes", "3": "yes", "4": "null", "5": "null",
               "6": "null", "7": "null", "8": "null", "9": "null", "10": "null", "11": "null", "12": "null",
               "13": "null", "14": "null", "15": "null", "16": "null", "17": "null", "18": "null", "19": "null",
               "20": "null", "21": "null", "22": "null", "23": "null", "24": "null", "25": "null", "26": "null",
               "27": "null", "28": "null", "29": "null", "30": "null", "31": "null", "32": "null", "33": "null",
               "34": "null", "35": "null", "36": "null"}
    return baskets[basket]
