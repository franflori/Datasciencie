class pasajero():
    PassengerId=""
    survived=""
    pclass=""
    nName=""
    sex=""
    age=0
    sibsp=0
    parch=0
    ticket=""
    fare=""
    cabin=""
    embarked=""
    
    def __init__(self, PassengerId,survived,pclass,nName,sex,
                age,sibsp,parch,ticket,fare,cabin,embarked) :
        self.PassengerId=PassengerId
        self.survived=survived
        self.pclass=pclass
        self.nName=nName
        self.sex=sex
        self.age=age
        self.sibsp=sibsp
        self.parch=parch
        self.ticket=ticket
        self.fare=fare
        self.cabin=cabin
        self.embarked=embarked


    def setSuvived(self,survived):
        self.survived=survived
