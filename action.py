import random as r
import math
# domestic action

def construction(original_resource, growth_rate, focus_type, trooppoint, corruption, stability, game_turn):
    # Direct access to resources
    # improve stability
    # improve resource growth rate
    # corruption will increase potential cost
    rc = corruption
    new_tp = trooppoint
    fs = stability
    if rc <= 0:
        rc = 0
    if new_tp < 0:
        re = original_resource + new_tp * 5
        return re, trooppoint, rc, fs, growth_rate
    if focus_type == 'domestic':
        new_tp -= 1
        cost = r.uniform(game_turn, int(game_turn+rc+1)) + (3 - fs//3) + 3
    else:
        new_tp -= 1
        cost = 5 + r.uniform(game_turn, game_turn+rc) + (3 - fs//3)
    rc += r.uniform(1, 2+int(growth_rate*2))
    fs += 1
    resource = original_resource - cost
    new_resource = resource + growth_rate * 5
    gr = growth_rate + 0.15

    return new_resource, new_tp, rc, fs, gr

def conscription(original_trooppoint, growth_rate, stability, focus_type):
    # Direct access to manpower
    # decrease stability
    # improve tp growth rate
    if focus_type == 'domestic':
        cost = 0 + r.uniform(0, 1+3-(stability//3))
    else:
        cost = 1 + r.uniform(1, 2+3-(stability//3))

    troop_point = original_trooppoint - cost
    new_troop_point = troop_point + growth_rate * (stability//3)
    new_stability = stability - 1
    gr = growth_rate + 0.1

    return new_troop_point, new_stability, gr

# foreign action
def Trade(focus_type, trooppoint, resource, corruption, resource_growth_rate):
    rc = corruption
    tp = trooppoint
    new_resource = resource + rc
    new_rc = max(0, rc-(math.floor(resource_growth_rate)*5))
    new_tp = tp - new_rc
    if new_tp < 0:
        return resource, new_tp, resource_growth_rate, corruption
    if focus_type == 'foreign':
        new_gr = resource_growth_rate - (r.uniform(3, 6)/10)
    else:
        new_gr = resource_growth_rate - (r.uniform(6, 9)/10)

    return new_resource, new_tp, new_gr, new_rc

def Threat(focus_type, tp_growth_rate, stability, resource_growth_rate):
    new_tp_gr = tp_growth_rate
    fs = stability - 3
    if focus_type == 'foreign':
        new_tp_gr -= r.uniform(2, 4)/10
    else:
        new_tp_gr -= r.uniform(4, 7)/10
    new_r_gr = resource_growth_rate + (r.uniform(4, 7)/10)
    return new_tp_gr, new_r_gr, fs


