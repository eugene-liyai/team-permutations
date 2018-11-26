def generateXArray(team, arr):
    arrayTeamX = []
    for val in arr:
        if val != team:
            arrayTeamX.append(team + '.' + val)
    return arrayTeamX
