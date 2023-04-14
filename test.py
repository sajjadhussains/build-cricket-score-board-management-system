import random

class T20Cup:
    allTeams=[]
    def entry_team(self,teamObj):
        self.allTeams.append(teamObj)

class Team(T20Cup):
    def __init__(self,name) -> None:
        self.teamName=name
        self.playersListOfObject=[]
        super().entry_team(self)
    def entry_player(self,player):
        self.playersListOfObject.append(player)
    def __repr__(self) -> str:
        return f'from object team name: {self.teamName}'

class Player:
    def __init__(self,name,teamObj) -> None:
        self.playerName=name
        self.strikRate=0.0
        self.runBat=0
        self.ballUsed=0
        self.fours=0
        self.sixes=0
        self.runBall=0
        self.wicketsTaken=0
        self.ballsBowled=0
        teamObj.playersListOfObject.append(self)
    def __repr__(self) -> str:
        return f'player name: {self.playerName}'

class Innings:
    def __init__(self,team1,team2,battingTeam,bowlingTeam) -> None:
        self.teamOneObj=team1
        self.teamTwoObj=team2
        self.battingTeam=battingTeam
        self.bowlingTeam=bowlingTeam
        self.totalRun=0
        self.totalWickets=0
        self.totalOver=0
        self.currentBall=0
        self.currentBattingList=[battingTeam.playersListOfObject[0],battingTeam.playersListOfObject[1]]
        self.striker=battingTeam.playersListOfObject[0]
        self.currentBowler=None
        self.currentOverStatus=[]
        self.allOverStatus=[]
    def sohw_score_board(self):
        print(f"*{self.currentBattingList[0].playerName} - {self.currentBattingList[0].runBat}({self.currentBattingList[0].ballUsed})")
        print(f" {self.currentBattingList[1].playerName} - {self.currentBattingList[1].runBat}({self.currentBattingList[1].ballUsed})")
        print(f'{self.battingTeam.teamName[:3].upper()} || {self.totalRun}-{self.totalWickets}')
        print(f"Overs:{self.totalOver}.{self.currentBall}")
        if self.currentBowler is not None:
            print(f"{self.currentBowler.playerName}- {self.currentBowler.runBall}/{self.currentBowler.wicketsTaken}")
    def set_bowler(self,bowlerObj):
        self.currentBowler=bowlerObj
    def bowl(self,status):
        self.totalRun+=status
        self.striker.runBat+=status
        self.striker.ballUsed+=1
        self.currentBowler.runBall+=status
        self.currentBowler.ballsBowled+=1
        self.currentBall+=1



cup = T20Cup()
bangladesh=Team('Bangladesh')
india=Team('India')
tamim=Player('Tamim Iqbal',bangladesh)
sakib=Player('Sakib al hasan',bangladesh)
mushfiq=Player('Mushfiqur Rahim',bangladesh)
kohli=Player('Virat Kohli',india)
rohit=Player('Rohit Sharma',india)
bumrah=Player('Jasprit Bumrah',india)

while True:
    print('selected teams to be played')
    for i,val in enumerate(cup.allTeams):
        print(f'{i+1}. {val.teamName}')
    
    teamOneIndex,teamTwoIndex=map(int,input("Enter two team indexes: ").split(" "))
    teamOneIndex-=1
    teamTwoIndex-=1
    teamOneObj=cup.allTeams[teamOneIndex]
    teamTwoObj=cup.allTeams[teamTwoIndex]
    tossWin = random.choice([teamOneIndex,teamTwoIndex])
    print(f'{cup.allTeams[tossWin].teamName} have won the toss')
    rand=random.choice([0,1])
    if tossWin==teamOneIndex:
        tossLoss=teamTwoIndex
    else:
        tossWin=teamTwoIndex
        tossLoss=teamOneIndex
    if rand==0:
        # winner team choose bowling
        print(f'{cup.allTeams[tossWin].teamName} elected to bowl first')
        battingTeamObj=cup.allTeams[tossLoss]
        bowlingTeamObj=cup.allTeams[tossWin]
        
    else:
        print(f'{cup.allTeams[tossWin].teamName} elected to bat first')
        # winner team choose batting
        battingTeamObj=cup.allTeams[tossWin]
        bowlingTeamObj=cup.allTeams[tossLoss]
    innings1=Innings(teamOneObj,teamTwoObj,battingTeamObj,bowlingTeamObj)
    innings1.sohw_score_board()
    print('Choose bowler: ')
    for i,val in enumerate(bowlingTeamObj.playersListOfObject):
        print(f"{i+1}.{val.playerName}")
    bowlerIndex=int(input("Enter bowler index: "))
    bowlerIndex-=1
    bowlerObj=bowlingTeamObj.playersListOfObject[bowlerIndex]
    innings1.set_bowler(bowlerObj)
    innings1.sohw_score_board()
    innings1.bowl(6)
    innings1.sohw_score_board()
    break