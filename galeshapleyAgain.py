def stable_matches(women_prefs,men_prefs):
    free_men=list(men_prefs.keys())
    engagements={}
    while free_men:
        man=free_men.pop(0)
        man_pref=men_prefs[man]
        woman=man_pref.pop(0)
        fiance=engagements.get(woman)
        if not fiance:
            engagements[woman]=man
        else:
            if women_prefs[woman].index(man)<women_prefs[woman].index(fiance):
                engagements[woman]=man
                free_men.append(fiance)
            else:
                free_men.append(man)
    return engagements
n=int(input("Enter the number of men and women:"))
men_prefs={}
women_prefs={}
print("Enter men's preferences:")
for i in range(n):
    man=input(f"Enter name of man {i+1}:")
    prefs=input(f"Enter the {man}'s preferences(space seperated):").split()
    men_prefs[man]=prefs
print("Enter women's preferences:")
for i in range(n):
    woman=input(f"Enter name of woman {i+1}:")
    prefs=input(f"Enter the {woman}'s preferences(space seperated):").split()
    women_prefs[woman]=prefs
stableMatches=stable_matches(women_prefs,men_prefs)
print("Stable matches:")
for woman,man in stableMatches.items():
    print(f"{man} is engaged to {woman}")


