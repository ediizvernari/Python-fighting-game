from FighterClass import*


def turndisplay(fighter):
    print(fighter.getname() + "s turn")


def windisplay(fighter):
    print(fighter.getname() + " won")


def nofightererror():
    print("WE DON'T HAVE 2 FIGHTERS, EXITING FIGHT")


def turn(fighter):
    print(fighter.getname() + "'s turn")
    print()
    print(str(fighter.getstamina()) + " Stamina left")


def pressinput():
    inp = None

    print("press any button!")

    while inp != "":
        inp = input()


def costprint(fighter):
    print("costs: light attack= " + str(fighter.getlstm()) + ", medium attack= " + str(fighter.getstm()) +
          ", heavy attack= " + str(fighter.gethstm()) + ", potions left: " + str(fighter.getpotions()))


def optionselect(fighter, target):
    option = None
    options = ["1", "2", "3", "4", "5"]

    print("select option: 1=light attack, 2=medium attack, 3=heavy attack, 4=heal, 5=rest")
    costprint(fighter)

    while option not in options:
        option = input("select a proper option: ")

    match option:
        case "1": fighter.attack(target, fighter.getldmg(), fighter.getlstm())
        case "2": fighter.attack(target, fighter.getdmg(), fighter.getstm())
        case "3": fighter.attack(target, fighter.gethdmg(), fighter.gethstm())
        case "4": fighter.heal(target)
        case "5": fighter.rest(target)


def fightsimulation(fighter1, fighter2):

    if (not isinstance(fighter1, Fighter)) or (not isinstance(fighter2, Fighter)):
        nofightererror()
    else:

        while fighter1.getalive() and fighter2.getalive():
            print()

            fighter1.printdetails()

            turndisplay(fighter1)
            optionselect(fighter1, fighter2)

            if not fighter2.getalive():
                windisplay(fighter1)
            else:
                print()
                fighter2.printdetails()
                turndisplay(fighter2)
                optionselect(fighter2, fighter1)

                if not fighter1.getalive():
                    windisplay(fighter2)
