class user:

    def __init__(self,ID,username,name,password,permitions):
        self._ID = ID
        self._Username = username
        self._name = name
        self._password = password
        self._permitions = permitions

    #--- getters ---

    def getID(self):
        return self._ID

    def getusername(self):
        return self._Username

    def getname(self):
        return self._name

    def getpassword(self):
        return self._password

    def getpermitions(self):
        return self._permitions

    #--- setters ---

    def setID(self,ID):
        self._ID = ID

    def setusername(self,username):
        self._Username = username

    def setname(self,name):
        self._name = name

    def setpassword(self,password):
        self._password = password

    def setpermitions(self,permitions):
        self._permitions = permitions

    def __str__(self):
        return str(self._ID+' ,'+ self._Username+' ,'+ self._name+' ,'+ self._password+' ,'+ self._permitions)

#--------------------------------------------------#

class tarefa:

    def __init__(self,TarefaID,name,timestart,timeend,ProjectID,user):
        self._ProjectID = ProjectID
        self._TarefaID = TarefaID
        self._name = name
        self._timestart = timestart
        self._timeend = timeend
        self._user = user


    #--- getters ---

    def getProjectID(self):
        return self._ProjectID

    def getTarefaID(self):
        return self._TarefaID

    def getname(self):
        return self._name

    def gettimestart(self):
        return self._timestart

    def gettimeend(self):
        return self._timeend

    def getuser(self):
        return self._user

    #--- setters ---

    def setProjectID(self,ProjectID):
        self._ProjectID =ProjectID

    def setTarefaID(self,TarefaID):
        self._TarefaID = TarefaID

    def setname(self,name):
        self._name = name

    def settimestart(self,timestart):
        self._timestart = timestart

    def settimeend(self,timeend):
        self._timeend = timeend

    def setuser(self, user):
        self._user =  user

    def __str__(self):
        return str(self._ProjectID+' ,'+ self._TarefaID+' ,'+ self._name+' ,'+ self._timestart+' ,'+ self._timeend+' ,'+ self._user)

#--------------------------------------------------#

class projeto:

    def __init__(self,ProjectID,GroupID,timestart,timeend):
        self._ProjectID = ProjectID
        self._GroupID = GroupID
        self._timestart = timestart
        self._timeend = timeend

    #--- getters ---

    def getProjectID(self):
        return self._ProjectID

    def getGroupID(self):
        return self._GroupID

    def gettimestart(self):
        return self._timestart

    def gettimeend(self):
        return self._timeend

    #--- setters ---

    def setProjectID(self,ProjectID):
        self._ProjectID = ProjectID

    def setGroupID(self,GroupID):
        self._GroupID = GroupID

    def settimestart(self,timestart):
        self._timestart = timestart

    def settimeend(self,timeend):
        self._timeend = timeend

    def __str__(self):
        return str(self._ProjectID+' ,'+ self._GroupID+' ,'+ self._timestart+' ,'+ self._timeend)
