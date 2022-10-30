# initial basic attribute setting

# faction statue list
buff_list = []

# stability part
faction_stability = 10
def check_stability(faction_stability):
    if faction_stability > 10:
        stability = 10
    elif faction_stability < 0:
        stability = 0
    else:
        stability = faction_stability
    return stability

def faction_stable_status(faction_stability):
    if faction_stability < 2:
        return "Unrest"
    elif 2 <= faction_stability < 9:
        return "Normal"
    else:
        return "Stable"

#############################
# resource part

resource = 10
resource_growth_rate = 1
corruption = 0
def gain_resource(resource, resourse_growth_rate):
    new_resource = resource + resourse_growth_rate * 5
    return new_resource

#############################
# troops point part
troops_point = 5
troops_point_Growth_rate = 1
def gain_trooppoint(troopspoint, troops_point_Growth_rate):
    new_troopspoint = troopspoint + troops_point_Growth_rate
    return new_troopspoint



###########################
# faction focus part
start_turn = 1
focus_demand = 0
focus_select = False
focus_type = 'N'
focus_name = 'N'

## init number
def init_number(resource, troop_point, fasction_stability, corruption):
    return int(resource), int(troop_point), int(fasction_stability), int(corruption)





