import numpy as np
from Actions.spin import spin_ball
from Actions.table import show_table
from Actions.bets import straight_up
from Actions.bets import splits1, splits2, splits3, splits4
from Actions.bets import black_red, odd_even
from Actions.bets import columns123, dozens123, bothhalves
from Actions.bets import street, topline
from Actions.bets import lines1, lines2
from Actions.bets import corner, corner2, corner3, corner4

while True:
    print("ROULETTE\n")
    print("1) Lets Play")
    print("2) No I don't take risks")

    winnings_su = 0
    winnings_sp = 0
    winnings_rb = 0
    winnings_oe = 0
    winnings_c = 0
    winnings_d = 0
    winnings_h = 0
    winnings_st = 0
    winnings_l = 0
    winnings_cor = 0
    winnings_b = 0

    finalstraight = 0
    finalsplits = 0
    finalcolors = 0
    finalevenodd = 0
    finalcolumns = 0
    finaldozens = 0
    finalhalves = 0
    finalstreets = 0
    finallines = 0
    finalcorners = 0
    finalBaskets = 0

    straightup = []
    splits = []
    red_black = []
    even_odd = []
    columns = []
    dozens = []
    halves = []
    streets = []
    lines = []
    corners = []
    Baskets = []

    straightup_bet = []
    splits_bet = []
    red_black_bet = []
    even_odd_bet = []
    columns_bet = []
    dozens_bet = []
    halves_bet = []
    streets_bet = []
    lines_bet = []
    corners_bet = []
    Baskets_bet = []

    straightup_bet_dict = {}
    splits_bet_dict = {}
    red_black_bet_dict = {}
    even_odd_bet_dict = {}
    columns_bet_dict = {}
    dozens_bet_dict = {}
    halves_bet_dict = {}
    streets_bet_dict = {}
    lines_bet_dict = {}
    corners_bet_dict = {}
    Baskets_bet_dict = {}

    choice = int(input("Make your decision: \n "))

    if choice == 1:
        print("TIME TO PLAY")
        # show_table()
        while True:
            straight = input(
                "Straight up (Single Number)?\n Enter your choices one at a time and enter 'Done' when finished.\n ").lower()

            straightup.append(straight)

            if straight == "done":
                break

            straightb = input(" How much would you like to bet?\n ")

            straightup_bet.append(straightb)

        while True:
            split = input(
                "Splits?\n Enter your choice one at a time and enter 'Done' when finished.\n Enter your choices by listing both numbers from least to greatest with a comma seperating them.\n Examples of choices: '1,2' '10,11' '17,20' '26,27'.\n ").lower()

            splits.append(split)

            if split == "done":
                break

            splitb = input(" How much would you like to bet?\n ")

            splits_bet.append(splitb)

        while True:
            color = input(
                "Red or Black?\n Enter your choices one at a time and enter 'Done' when finished.\n ").lower()

            red_black.append(color)

            if color == "done":
                break

            colorb = input(" How much would you like to bet?\n ")

            red_black_bet.append(colorb)

        while True:
            oddeven = input(
                "Odd or Even?\n Enter your choice one at a time and enter 'Done' when finished.\n ").lower()

            even_odd.append(oddeven)

            if oddeven == "done":
                break

            oddevenb = input(" How much would you like to bet?\n ")

            even_odd_bet.append(oddevenb)

        while True:
            column = input(
                "Columns?\n Enter your choice one at a time and enter 'Done' when finished.\n Choices: '1' for column 1, '2' for column 2, or '3' for column 3.\n ").lower()

            columns.append(column)

            if column == "done":
                break

            columnsb = input(" How much would you like to bet?\n ")

            columns_bet.append(columnsb)

        while True:
            dozen = input(
                "Dozens?\n Enter your choice one at a time and enter 'Done' when finished.\n Choices: '1' for 1-12, '2' for 13-24, or '3' for 25-36.\n ").lower()

            dozens.append(dozen)

            if dozen == "done":
                break

            dozenb = input(" How much would you like to bet?\n ")

            dozens_bet.append(dozenb)

        while True:
            half = input(
                "Halves (High/Low)?\n Enter your choice one at a time and enter 'Done' when finished.\n Choices: '1' for 1-18 and '2' for 19-36.\n ").lower()

            halves.append(half)

            if half == "done":
                break

            halfb = input(" How much would you like to bet?\n ")

            halves_bet.append(halfb)

        while True:
            streetz = input(
                "Streets?\n Enter your choice one at a time and enter 'Done' when finished.\n Enter your choices by listing all numbers in that row from least to greatest with commas seperating each integer.\n For example, '1,2,3' for the first row.\n ").lower()

            streets.append(streetz)

            if streetz == "done":
                break

            streetb = input(" How much would you like to bet?\n ")

            streets_bet.append(streetb)

        while True:
            line = input(
                "Lines (Double Streets)?\n Enter your choice one at a time and enter 'Done' when finished.\n Examples of choices: '1-6' '4-9' '13-18'.\n ").lower()

            lines.append(line)

            if line == "done":
                break

            lineb = input(" How much would you like to bet?\n ")

            lines_bet.append(lineb)

        while True:
            corna = input(
                "Corners (Squares)?\n Enter your choice one at a time and enter 'Done' when finished.\n Enter your choices by listing the four numbers involved in each corner from least to greatest with commas seperating each integer.\n For example, '1,2,4,5'.\n ").lower()

            corners.append(corna)

            if corna == "done":
                break

            cornersb = input(" How much would you like to bet?\n ")

            corners_bet.append(cornersb)

        while True:
            basket = input(
                "Backet (Top Line)? Enter 'Yes' to place a bet or 'No' to continue. Enter 'Done' when finished.\n ").lower()

            Baskets.append(basket)

            if basket == "done" or basket == "no":
                break

            Basketb = input(" How much would you like to bet?\n ")

            Baskets_bet.append(Basketb)

        spin_b = spin_ball()

        straight_up(straightup)
        straightup.pop()
        straightup_bet_dict = {
            straightup[i]: straightup_bet[i] for i in range(len(straightup))}

        s1 = splits1(spin_b)
        s2 = splits2(spin_b)
        s3 = splits3(spin_b)
        s4 = splits4(spin_b)
        splits.pop()
        splits_bet_dict = {
            splits[i]: splits_bet[i] for i in range(len(splits))}

        br = black_red(spin_b)
        red_black.pop()
        red_black_bet_dict = {
            red_black[i]: red_black_bet[i] for i in range(len(red_black))}

        oe = odd_even(spin_b)
        even_odd.pop()
        even_odd_bet_dict = {
            even_odd[i]: even_odd_bet[i] for i in range(len(even_odd))}

        c = columns123(spin_b)
        columns.pop()
        columns_bet_dict = {
            columns[i]: columns_bet[i] for i in range(len(columns))}

        d = dozens123(spin_b)
        dozens.pop()
        dozens_bet_dict = {
            dozens[i]: dozens_bet[i] for i in range(len(dozens))}

        h = bothhalves(spin_b)
        halves.pop()
        halves_bet_dict = {
            halves[i]: halves_bet[i] for i in range(len(halves))}

        st = street(spin_b)
        streets.pop()
        streets_bet_dict = {
            streets[i]: streets_bet[i] for i in range(len(streets))}

        l1 = lines1(spin_b)
        l2 = lines2(spin_b)
        lines.pop()
        lines_bet_dict = {
            lines[i]: lines_bet[i] for i in range(len(lines))}

        cor = corner(spin_b)
        cor2 = corner2(spin_b)
        cor3 = corner3(spin_b)
        cor4 = corner4(spin_b)
        corners.pop()
        corners_bet_dict = {
            corners[i]: corners_bet[i] for i in range(len(corners))}

        bask = topline(spin_b)
        Baskets.pop()
        Baskets_bet_dict = {
            Baskets[i]: Baskets_bet[i] for i in range(len(Baskets))}

        print(f"Your choices were {straightup} for straight up,\n {splits} for splits,\n {red_black} for red or black,\n {even_odd} for odd or even,\n {columns} for columns,\n {dozens} for dozens,\n {streets} for streets,\n {lines} for lines (double streets),\n {corners} for corners (squares),\n and {Baskets} was entered for Basket. ")

        if spin_b in straightup:
            winnings_su += 35
            finalstraight = float(
                straightup_bet_dict[spin_b]) * float(winnings_su)
            print(f"You've won ${finalstraight} from straight up. ")

        if s1 in splits:
            winnings_sp += 17
            finalsplits = float(
                splits_bet_dict[s1]) * float(winnings_sp)
            print(f"You've won ${finalsplits} from splits. ")

        if s2 in splits:
            winnings_sp += 17
            finalsplits = float(
                splits_bet_dict[s2]) * float(winnings_sp)
            print(f"You've won ${finalsplits} from splits. ")

        if s3 in splits:
            winnings_sp += 17
            finalsplits = float(
                splits_bet_dict[s3]) * float(winnings_sp)
            print(f"You've won ${finalsplits} from splits. ")

        if s4 in splits:
            winnings_sp += 17
            finalsplits = float(
                splits_bet_dict[s4]) * float(winnings_sp)
            print(f"You've won ${finalsplits} from splits. ")

        if br in red_black:
            winnings_rb += 2
            finalcolors = float(
                red_black_bet_dict[br]) * float(winnings_rb)
            print(f"You've won ${finalcolors} from red or black. ")

        if oe in even_odd:
            winnings_oe += 2
            finalevenodd = float(
                even_odd_bet_dict[oe]) * float(winnings_oe)
            print(f"You've won ${finalevenodd} from even or odd. ")

        if c in columns:
            winnings_c += 3
            finalcolumns = float(
                columns_bet_dict[c]) * float(winnings_c)
            print(f"You've won ${finalcolumns} from columns. ")

        if d in dozens:
            winnings_d += 3
            finaldozens = float(
                dozens_bet_dict[d]) * float(winnings_d)
            print(f"You've won ${finaldozens} from dozens. ")

        if h in halves:
            winnings_h += 3
            finalhalves = float(
                halves_bet_dict[h]) * float(winnings_h)
            print(f"You've won ${finalhalves} from dozens. ")

        if st in streets:
            winnings_st += 11
            finalstreets = float(
                streets_bet_dict[st]) * float(winnings_st)
            print(f"You've won ${finalstreets} from streets. ")

        if l1 in lines:
            winnings_l += 5
            finallines = float(
                lines_bet_dict[l1]) * float(winnings_l)
            print(f"You've won ${finallines} from lines. ")

        if l2 in lines:
            winnings_l += 5
            finallines = float(
                lines_bet_dict[l2]) * float(winnings_l)
            print(f"You've won ${finallines} from lines. ")

        if cor in corners:
            winnings_cor += 8
            finalcorners = float(
                corners_bet_dict[cor]) * float(winnings_cor)
            print(f"You've won ${finalcorners} from corners. ")

        if cor2 in corners:
            winnings_cor += 8
            finalcorners = float(
                corners_bet_dict[cor2]) * float(winnings_cor)
            print(f"You've won ${finalcorners} from corners. ")

        if cor3 in corners:
            winnings_cor += 8
            finalcorners = float(
                corners_bet_dict[cor3]) * float(winnings_cor)
            print(f"You've won ${finalcorners} from corners. ")

        if cor4 in corners:
            winnings_cor += 8
            finalcorners = float(
                corners_bet_dict[cor4]) * float(winnings_cor)
            print(f"You've won ${finalcorners} from corners. ")

        if bask in Baskets:
            winnings_b += 6
            finalBaskets = float(
                Baskets_bet_dict[bask]) * float(winnings_b)
            print(f"You've won ${finalBaskets} from Basket. ")

        total = [finalstraight, finalsplits, finalcolors,
                 finalevenodd, finalcolumns, finaldozens, finalhalves, finalstreets, finallines, finalcorners, finalBaskets]
        winningstotal = sum(total)
        print(f"You won a total of ${winningstotal}!")

    elif choice == 2:
        break

    else:
        print("INVALID ENTRY\n")
