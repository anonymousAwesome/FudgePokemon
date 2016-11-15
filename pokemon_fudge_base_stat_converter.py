import csv

hp_limits=[0,20,40,60,80,120,180,256]
atk_limits=[0,15,30,50,70,90,120,150]
sp_atk_limits=[0,15,30,50,70,90,120,150]
def_limits=[0,20,40,60,80,110,150,200]
sp_def_limits=[0,20,40,60,80,110,150,200]
spd_limits=[0,20,40,60,80,110,150,200]

def poke_convert(limit_list, stat_value):
    if stat_value<limit_list[0]:
        return "Abysmal"
    elif stat_value<limit_list[1]:
        return "Terrible"
    elif stat_value<limit_list[2]:
        return "Poor"
    elif stat_value<limit_list[3]:
        return "Mediocre"
    elif stat_value<limit_list[4]:
        return "Fair"
    elif stat_value<limit_list[5]:
        return "Good"
    elif stat_value<limit_list[6]:
        return "Great"
    elif stat_value<limit_list[7]:
        return "Superb"
    return "Legendary"

with open('pokemon_base_stats.csv', newline='') as pokemon_file:
    pokemon_reader=csv.reader(pokemon_file)
    with open('pokemon_converted.txt', 'w') as f:
        for x in pokemon_reader:
            f.write (x[2].strip()+": \n")
            f.write ("HP: "+poke_convert(hp_limits,int(x[3]))+"\n")
            f.write ("Melee Attack: "+poke_convert(atk_limits,int(x[4]))+"\n")
            f.write ("Melee Defense: "+poke_convert(def_limits,int(x[5]))+"\n")
            f.write ("Ranged Attack: "+poke_convert(sp_atk_limits,int(x[6]))+"\n")
            f.write ("Ranged Defense: "+poke_convert(sp_def_limits,int(x[7]))+"\n")
            f.write ("Initiative: "+poke_convert(spd_limits,int(x[8]))+"\n\n")
