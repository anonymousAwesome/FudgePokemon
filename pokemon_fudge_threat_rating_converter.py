import csv

threat_rating_limits=[25,79,132,185,238,291,344,397,450,503,556,609]
hp_limits=[0,20,40,60,80,120,180,256,256,256,256,256]
spd_limits=[0,20,40,60,80,110,150,200,256,256,256,256]


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
    elif stat_value<limit_list[8]:
        return "Fair Superhuman (Legendary)"
    elif stat_value<limit_list[9]:
        return "Good Superhuman (Legendary+1)"
    elif stat_value<limit_list[10]:
        return "Great Superhuman (Legendary+2)"
    elif stat_value<limit_list[11]:
        return "Superb Superhuman (Legendary+3)"
    else:
        return "Legendary Superhuman (Legendary+4)"


with open('pokemon_base_stats.csv', newline='') as pokemon_file:
    pokemon_reader=csv.reader(pokemon_file)
    with open('pokemon_threat_converted.txt', 'w') as f:
        for x in pokemon_reader:
            summed_stats=sum([int(y) for y in x[4:8]])
            f.write("{}: \n".format(x[2].strip()))
            f.write("HP: {}\n".format(poke_convert(hp_limits, int(x[3]))))
            f.write("Threat Rating: {}\n".format(poke_convert(threat_rating_limits,summed_stats)))
            f.write("Initiative: {}\n\n".format(poke_convert(spd_limits, int(x[8]))))
