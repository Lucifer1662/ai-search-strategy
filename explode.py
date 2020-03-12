from util import print_board 

def tokensToDic(tokens):
    board = set()
    for token in tokens:
        x = token[1]
        y = token[2]
        board.add((x,y))
    return board



def recurseIslands(id, pos, board, islands):
    islands[pos] = id
    for x in range(-1,2):
        for y in range(-1,2):
            neighborPos = (pos[0]+x,pos[1]+y)
            if(neighborPos in board and not neighborPos in islands):
                recurseIslands(id, neighborPos, board, islands)


def boardToIslands(board):
    islands = {}
    id = 0
    for key in board:
        if(not key in islands):
            recurseIslands(id, key, board, islands)
            id +=1
    return islands

def isLandsToids(islands):
    idToIslandPos = {}
    for islandsPos in islands:
        id = islands(islandsPos)
        if(id in idToIslandPos):
            idToIslandPos[id].append(islandsPos)  
        else:
            idToIslandPos[id] = [islandsPos]


def islandsNearby(pos, islands):
    nerbyIslands = set()
    for x in range(-1,2):
        for y in range(-1,2):
            neighborPos = (pos[0]+x,pos[1]+y)
            if(neighborPos in islands):
                nerbyIslands.add(islands[neighborPos])
    return nerbyIslands

def amountOfDamage(islands):
    damage = {}
    for middlePos in islands:
        for x in range(-1,2):
            for y in range(-1,2):
                pos = (middlePos[0]+x,middlePos[1]+y)
                if(not pos in islands ):
                    damage[pos] = islandsNearby(pos, islands)
    return damage
    
def pickLocation(amountOfDamage):
    maxDamage = 0
    location = None
    for damagePos in amountOfDamage:
        damage = len(amountOfDamage[damagePos])
        if(maxDamage < damage):
            maxDamage = damage
            location = damagePos
    return location

def sortAmountofDamage(amountOfDamage):
    listOfDamage = []
    for pos in amountOfDamage:
        listOfDamage.append((pos, amountOfDamage[pos]))
    return sorted(listOfDamage, key=lambda x: len(x[1]), reverse=True)


def func():
    pass

def pickLocations(index, sortedIslandsThatWillBeBlowUpAt, numTokens, targets, targetss):
    (pos, islands) = sortedIslandsThatWillBeBlowUpAt[index]
    targets.append(pos)
    
    sortedIslandsThatWillBeBlowUpAt = list(filter(lambda x: x[1].union(islands) != islands, sortedIslandsThatWillBeBlowUpAt))
    print(islands)
    print(sortedIslandsThatWillBeBlowUpAt)
    print("---------------------")
    if(len(sortedIslandsThatWillBeBlowUpAt) == 0):
        targetss.append(targets)
        return
    
    if(numTokens <= 1):
        return

  
    targetss = []
    for i in range(len(sortedIslandsThatWillBeBlowUpAt)):
        pickLocations(i, sortedIslandsThatWillBeBlowUpAt, numTokens -1, targets.copy(), targetss)


def PossibleWinningExplosions(blackPieces, numWhite):
    print(set([0,1]).union(set([2])) == set([2]))
    board1 = tokensToDic(blackPieces)
    islands = boardToIslands(board1)
    islandsThatWillBlowUpAt = amountOfDamage(islands)
    print_board(islandsThatWillBlowUpAt)
    sortedIslands = sortAmountofDamage(islandsThatWillBlowUpAt)
    print(sortedIslands)
    targetss = []
    pickLocations(0, sortedIslands, numWhite, [], targetss)
    #for i in range(len(sortedIslands)):
    #    pickLocations(i, sortedIslands, numWhite, [], targetss)
    return targetss