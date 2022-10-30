import GameEvent as GE
import basic_attribute as ba
import math
import matplotlib.pyplot as plt
import action as ac

# game_turn < 10: game_turn**2 + 10
# game_turn > 10: int(math.log(game_turn-9, 1.1) + 9**2 + 15)
# mission only respect to resource, try to gain more resource in a game turn
# arrange troop is important
x = []
y = []
y1 = []
faction_stability = ba.faction_stability
resource = ba.resource
resource_growth_rate = ba.resource_growth_rate
corruption = ba.corruption
troops_point = ba.troops_point
troops_point_Growth_rate = ba.troops_point_Growth_rate
game_turn = ba.start_turn
start_turn = ba.start_turn
focus_demand = ba.focus_demand
focus_select = ba.focus_select
focus_type = ba.focus_type
focus_name = ba.focus_name


run = True

while run:
    print()
    ## crisis check phase
    faction_stability = ba.check_stability(faction_stability)
    status = ba.faction_stable_status(faction_stability)
    if status == 'Unrest':
        if corruption <= 0:
            corruption = 0
        faction_stability, resource, resource_growth_rate, corruption, troops_point, troops_point_Growth_rate, status, game_turn \
            = GE.crisis_trigger(faction_stability, resource, resource_growth_rate, corruption, troops_point, troops_point_Growth_rate,
                               status, game_turn)

        faction_stability = ba.check_stability(faction_stability)
        resource, troops_point, faction_stability, corruption = ba.init_number(resource, troops_point, faction_stability, corruption)

    else:
        # focus part
        if focus_select == False:
            if game_turn < 12:
                focus_demand = game_turn**2 + 10
            else:
                focus_demand = int(math.log(game_turn-1, 1.1) + 11**2 + 15)
            print('choose focus')
            print('Next mission is: {}'.format(focus_demand))
            print('1. domestic policy')
            print('2. foreign policy')
            choice = input('your choice: ')

            if choice == '1':
                start_turn = game_turn
                focus_type = 'domestic'
                focus_select = True
                focus_name = 'domestic policy'

            elif choice == '2':
                start_turn = game_turn
                focus_type = 'foreign'
                focus_select = True
                focus_name = 'foreign policy'
            print()

        else:
            if game_turn - start_turn == 3:
                if resource >= focus_demand:
                    print('mission complete')
                    focus_select = False
                else:
                    print('mission failed')
                    print('the end')
                    game_turn = 20

            print('Task requirements: the number of resources is greater than or equal to', focus_demand)
            print('recent focus type is ', focus_type)

        ## action phase
        if corruption <= 0:
            corruption = 0
        print()
        print('choose one action: 1.construction 2.conscription 3.Trade 4.Threat')
        action = input('Turn{}, your action: '.format(game_turn))
        if action == '1':
            resource, troops_point, corruption, faction_stability, resource_growth_rate \
                = ac.construction(resource, resource_growth_rate, focus_type, troops_point, corruption, faction_stability, game_turn)
        elif action == '2':
            troops_point, faction_stability, troops_point_Growth_rate \
                = ac.conscription(troops_point, troops_point_Growth_rate, faction_stability, focus_type)
        elif action == '3':
            resource, troops_point, resource_growth_rate, corruption \
                = ac.Trade(focus_type, troops_point, resource, corruption, resource_growth_rate)
        elif action == '4':
            troops_point_Growth_rate, resource_growth_rate, faction_stability \
                = ac.Threat(focus_type, troops_point_Growth_rate, faction_stability, resource_growth_rate)

        faction_stability = ba.check_stability(faction_stability)
        resource, troops_point, faction_stability, corruption = ba.init_number(resource, troops_point, faction_stability, corruption)

        # event phase
        print()
        faction_stability, resource, resource_growth_rate, corruption, troops_point, troops_point_Growth_rate, status, game_turn \
            = GE.event_trigger(faction_stability, resource, resource_growth_rate, corruption, troops_point, troops_point_Growth_rate,
                               status, game_turn)

        faction_stability = ba.check_stability(faction_stability)
        resource, troops_point, faction_stability, corruption = ba.init_number(resource, troops_point, faction_stability, corruption)

        # gain resource & gain troop points phase
        resource = ba.gain_resource(resource, resource_growth_rate)
        troops_point = ba.gain_trooppoint(troops_point, troops_point_Growth_rate)


    if game_turn >= 20:
        print('the end')
        run = False



    x.append(game_turn)
    y.append(resource)
    y1.append(focus_demand)
    game_turn += 1

    resource, troops_point, faction_stability, corruption = ba.init_number(resource, troops_point, faction_stability, corruption)
    print()
    print('resource: ', resource)
    print('stability: ', faction_stability)
    print('troop point: ', troops_point)
    print('Number of resources gained per turn(5*rgr): ', 5*resource_growth_rate)
    print('Number of Troop point gained per turn(1*tpgr): ', troops_point_Growth_rate)
    print('Corruption: ', corruption)

plt.plot(x, y)
plt.plot(x, y1)
plt.show()
