import math

import basic_attribute as ba
import random as r



# common event
# standard value is 5


def crisis_trigger(faction_stability, resource, resource_growth_rate, corruption,
                  troops_point, troops_point_Growth_rate, stability_status, game_turn):
    fs = faction_stability
    re = resource
    rgr = resource_growth_rate
    rc = corruption
    tp = troops_point
    tpgr = troops_point_Growth_rate
    status = stability_status
    gt = game_turn

    # crisis
    print()
    print('Event 001: The country enters a state of crisis. It needs to be dealt with immediately.')
    tp_cost = max((rc//10) * 5, 10)
    print('Using troop to deal with crises at once')
    fs = ba.check_stability(fs)
    if tp < tp_cost:
        gt = 20
        print('game over')
        return fs, re, rgr, rc, tp, tpgr, status, gt
    else:
        tp -= tp_cost
        print('The first step in crisis management is over.')
        fs += 1
        fs = ba.check_stability(fs)
        status1 = ba.faction_stable_status(fs)
        if status1 == 'Unrest':
            print('Event 002: Continuing crisis')
            tp_cost = max((rc//10) * 5, 10)
            if tp < tp_cost:
                gt = 20
                print('game over')
                return fs, re, rgr, rc, tp, tpgr, status1, gt
            print('1.Using troop to deal with crises as well')
            print('2.Using resources to deal with the crisis')
            a = input('your choice: ')
            if a == '1':
                tp -= tp_cost
                rc -= tp_cost
                rc = max(0, rc)
                fs += 1
            elif a == '2':
                cost = (r.uniform(6, 9)/10)
                rgr -= cost
                rc -= int(cost * 5)
                rc = max(0, rc)
                fs += 1
            status1 = ba.faction_stable_status(fs)
            return fs, re, rgr, rc, tp, tpgr, status1, gt
        else:
            return fs, re, rgr, rc, tp, tpgr, status1, gt

def event_trigger(faction_stability, resource, resource_growth_rate, corruption,
                  troops_point, troops_point_Growth_rate, stability_status, game_turn):
    fs = faction_stability
    re = resource
    rgr = resource_growth_rate
    rc = corruption
    tp = troops_point
    tpgr = troops_point_Growth_rate
    status = stability_status
    gt = game_turn
    if rc > int(rgr * 10):
        # Ability to remove corruption
        # 0 - 100 randan int
        # if value is in [0 to difference], bad event
        # (difference, 100], good event
        # difference increase, bad event probability increase
        difference = rc - int(rgr * 5)
        v = r.uniform(0, 100)
        if 0 <= v <= difference:
            print('Event 003: Too much corruption in faction')
            re -= int(rgr * 5)
            rgr -= 0.15
            tpgr -= 0.1
            fs -= 1
            return fs, re, rgr, rc, tp, tpgr, status, gt
        else:
            print('Event 004: Cleaning up corruption')
            rc -= r.uniform(1, 2+int(rgr))
            rgr -= 0.1
            tpgr -= 0.07
            return fs, re, rgr, rc, tp, tpgr, status, gt
    else:
        v = r.uniform(0, 100)
        if 0 <= v <= (3 - fs//3)*10:
            # bad event
            print("Event 005: Not Gaining popular support")
            re -= r.uniform(0, 2+10-fs)
            rgr -= 0.07
            tpgr -= 0.05
            fs -= 1
            return fs, re, rgr, rc, tp, tpgr, status, gt
        else:
            # good event
            print("Event 006: Gaining popular support")
            print('1. gain long-term benefits')
            print('2. direct access to resources')
            choice = input('your choice is: ')
            if choice == '1':
                rgr += 0.08
                tpgr += 0.06
                return fs, re, rgr, rc, tp, tpgr, status, gt
            elif choice == '2':
                re += 2 * rgr
                tp += 1 * tpgr
                rc += r.uniform(1, 2+int(rgr*2))
                return fs, re, rgr, rc, tp, tpgr, status, gt










