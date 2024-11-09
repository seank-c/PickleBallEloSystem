from datetime import date
# ==== CLASSES ====

class Player:
    # Data fields:
        # - name: string
        # - elo: int
        # - subbed: int
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
        self.subbed = 0

    def recalculateElo(self, result):
        """ 
        # Calculates this player's new elo based on the game they played

        # Parameters:
        # result (bool): the result of the match; True if win, False if loss
        """
        if (result):
            self.elo += 10
        else:
            self.elo -= 10


class Session:
    # Data fields:    
        # - playerList: [Player]
        # - date: Date
        # - location: string
    def __init__(self, playerList, date, location):
        self.playerList = playerList
        self.date = date
        self.location = location

class Match:
    # Data fields
        # team1: (Player, Player)
        # team2: (Player, Player)
        # averageElo: int

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2 


# memberList - csv file

global currentSession = createSession("Auburn Tennis Courts")

# ==== FUNCTIONS ====
def createSession(location):
    return Session([], date.today(), location)

def addPlayer(name):
    """
    Adds a player to the current session. If their name matches a name in the database, extract their elo, else default their elo to 1000.
    """

    with open("playerList.csv", mode="r") as csvfile:
        csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        if name == row["name"]:
            currentSession.playerList.append(Player(name, row["elo"]))
            return
    
    currentSession.playerList.append(Player(name, 1000))



def generateBracket(voluntarySubs): 
    """
    Creates a bracket of players based on the current session
    
    Parameters:
        voluntarySubs ([Player]): list of players who have chosen to sub for the next round voluntarily

    Returns:
        bracket ([Match]): list of Matches
    """

    playerList = currentSession.playerList

    # remove all players that would like to sub voluntarily
    for player in voluntarySubs:
        playerList.remove(player)

    # find the minimum number of times anybody has subbed during this session
    minSubs = min()
    

    match option:
        case 1:
        # generate bracket for round 1
        bracket = []
        j = 1
        for i in range(0, 32, 4):
            # create pairs of players in groups of 4, matching the top player with the bottom player as one pair and the middle two players as a second pair
            bracket.append({
                f'Team {j}': [sliced_player_list[i], sliced_player_list[i + 3]],
                f'Team {j+1}':
                [sliced_player_list[i + 1], sliced_player_list[i + 2]]
            })
            j += 2
        return bracket



def resolveMatch(match, winner)
    """
    Resolves match data by updating the elos of all the players involved

    Parameters:
        match (Match): the match to be resolved
        winner ((Player, Player)): pair of players who won the match

    Raises:
        Exception
    """

def resolveBracket(): 
    """
    Resolves all bracket data,

    Parameters:
        bracket ([Match]): list of Matches to be resolved

    Raises:
        Exception
    """


def resolveSession():
    """
    Resolves all post-session data
    
    Parameters:
        session (Session): the session to be resolved 
    """

# setupSession()
#     # Creates a session 

#     # Parameters:
#     #    

#     # Returns:
#     #    reverse(str1):The string which gets reversed.   

# addPlayer()

# createBracket()
#     -

if __name__ == "__main__":
