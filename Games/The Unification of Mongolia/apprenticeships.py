def apprenticeships(p, apprenticeship):

    if apprenticeship == "apothecary":
        health_bonus = 60
        attack_bonus = 0
        defense_bonus = 0
        p.health += health_bonus
        p.attack += attack_bonus
        p.defense += defense_bonus

    elif apprenticeship == "blacksmith":
        health_bonus = 0
        attack_bonus = 0
        defense_bonus = 60
        p.health += health_bonus
        p.attack += attack_bonus
        p.defense += defense_bonus
    elif apprenticeship == "farmer":
        health_bonus = 40
        attack_bonus = 0
        defense_bonus = 20
        p.health += health_bonus
        p.attack += attack_bonus
        p.defense += defense_bonus
    elif apprenticeship == "laborer":
        health_bonus = 20
        attack_bonus = 20
        defense_bonus = 20
        p.health += health_bonus
        p.attack += attack_bonus
        p.defense += defense_bonus
    elif apprenticeship == "steppe bandit":
        health_bonus = 0
        attack_bonus = 60
        defense_bonus = 0
        p.health += health_bonus
        p.attack += attack_bonus
        p.defense += defense_bonus
    elif apprenticeship == "woodsman":
        health_bonus = 20
        attack_bonus = 40
        defense_bonus = 0
        p.health += health_bonus
        p.attack += attack_bonus
        p.defense += defense_bonus
