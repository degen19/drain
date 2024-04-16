import random
import math

elder_acc = 35872
elder_max = 66

ralos_VQ_acc = 30576
ralos_VQ_max = 24

ralos_AVQ_acc = 32916
ralos_AVQ_max = 24

ralos_AQM_acc = 36068
ralos_AQM_max = 23

bgs_acc = 69434
bgs_max = 77

def defRoll(defence, type): 
    roll = (defence + 9) * (type + 64)
    return roll

def did_i_hit(attackRoll, defenseRoll):
    hitchance = 0
    if attackRoll > defenseRoll:
        hitchance = 1 - ((defenseRoll + 2)/(2*(attackRoll + 1)))
    else: 
        hitchance = attackRoll/(2*(defenseRoll + 1))
    if random.random() < hitchance:
        return True
    else:
        return False
    
def maidenDrain(num_elder, num_ralos, num_bgs, VQ, AVQ, AQM):
    defence = 200
    crush = 0
    slash = 0
    ranged = 0
    crush_roll = defRoll(defence, crush)
    range_roll = defRoll(defence, ranged)
    slash_roll = defRoll(defence, slash)

    # Elder
    for _ in range(num_elder):
        if did_i_hit(elder_acc, crush_roll):
            drain = math.floor(defence * 0.35)
            defence -= drain
            defence = max(defence, 0)
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    # Ralos 
    for _ in range(num_ralos*2):
        if VQ:
            attackRoll = ralos_VQ_acc
        elif AVQ:
            attackRoll = ralos_AVQ_acc
        elif AQM:
            attackRoll = ralos_AQM_acc
        
        if did_i_hit(attackRoll, range_roll):
            drain = 35
            defence -= drain
            defence = max(defence, 0)
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    # BGS
    for _ in range(num_bgs):
        if did_i_hit(bgs_acc, slash_roll):
            damage = random.randint(1, bgs_max)
            defence -= damage
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    return defence

def sotetsegDrain(num_elder, num_ralos, num_bgs, VQ, AVQ, AQM):
    defence = 200
    crush = 70
    slash = 70
    ranged = 150
    crush_roll = defRoll(defence, crush)
    range_roll = defRoll(defence, ranged)
    slash_roll = defRoll(defence, slash)

    # Elder
    for _ in range(num_elder):
        if did_i_hit(elder_acc, crush_roll):
            drain = math.floor(defence * 0.35)
            defence -= drain
            defence = max(defence, 100)
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    # Ralos 
    for _ in range(num_ralos * 2):
        if VQ:
            attackRoll = ralos_VQ_acc
        elif AVQ:
            attackRoll = ralos_AVQ_acc
        elif AQM:
            attackRoll = ralos_AQM_acc
        
        if did_i_hit(attackRoll, range_roll):
            drain = 25
            defence -= drain
            defence = max(defence, 100)
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    # BGS
    for _ in range(num_bgs):
        if did_i_hit(bgs_acc, slash_roll):
            damage = random.randint(1, bgs_max)
            defence -= damage
            defence = max(defence, 100)
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    return defence

def xarpusDrain(num_elder, num_ralos, num_bgs, VQ, AVQ, AQM):
    defence = 250
    crush = 0
    slash = 0
    ranged = 160
    crush_roll = defRoll(defence, crush)
    range_roll = defRoll(defence, ranged)
    slash_roll = defRoll(defence, slash)

    # Elder
    for _ in range(num_elder):
        if did_i_hit(elder_acc, crush_roll):
            drain = math.floor(defence * 0.35)
            defence -= drain
            defence = max(defence, 0)
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    # Ralos 
    for _ in range(num_ralos * 2):
        if VQ:
            attackRoll = ralos_VQ_acc
        elif AVQ:
            attackRoll = ralos_AVQ_acc
        elif AQM:
            attackRoll = ralos_AQM_acc
        
        if did_i_hit(attackRoll, range_roll):
            drain = 22
            defence -= drain
            defence = max(defence, 0)
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    # BGS
    for _ in range(num_bgs):
        if did_i_hit(bgs_acc, slash_roll):
            damage = random.randint(1, bgs_max)
            defence -= damage
            crush_roll = defRoll(defence, crush)
            range_roll = defRoll(defence, ranged)
            slash_roll = defRoll(defence, slash)

    return defence

def count_defense_below_threshold(threshold, num_elder, num_ralos, num_bgs, VQ, AVQ, AQM, target, runs=1000000):
    count = 0
    for _ in range(runs):
        if target == "maiden":
            final_defense = maidenDrain(num_elder, num_ralos, num_bgs, VQ, AVQ, AQM)
        elif target == "xarpus":
            final_defense = xarpusDrain(num_elder, num_ralos, num_bgs, VQ, AVQ, AQM)
        elif target == "sotetseg":
            final_defense = sotetsegDrain(num_elder, num_ralos, num_bgs, VQ, AVQ, AQM)
        else:
            raise ValueError("Invalid target. Choose 'maiden', 'xarpus', or 'sotetseg'.")

        if final_defense <= threshold:  # Update the condition to final_defense < threshold
            count += 1

    ratio = count / runs
    percentage = round(ratio * 100, 2)
    return f"{percentage}%"



VQ = True #void quiver
AVQ = False #void quiver anguish
AQM = False #anguish quiver masori(top)
num_elder = 2
num_ralos = 2 #number of attacks, the number of reduction attempts is double this number
num_bgs = 0
threshold = 0 #defence threshold
target = "maiden" #maiden sotetseg or xarpus
count_below_threshold = count_defense_below_threshold(threshold, num_elder, num_ralos, num_bgs, VQ, AVQ, AQM, target)

print(f"Elder Maul: {num_elder} | Ralos: {num_ralos} | BGS: {num_bgs}\n{count_below_threshold} chance to reduce {target} to or below {threshold} defense")