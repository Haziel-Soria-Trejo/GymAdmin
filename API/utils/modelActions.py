from base.utils.notice import notice
from .setModel import addGroup, addItem, deleteTask, setClient, setClientPay, \
    setClientPay, setTask, setItemSell, updateGroup, updateItem, upgradeStaff


class Actions:
    def __init__(self, body, by, to,):
        self.body = body
        self.subject = body['subject']
        self.by = by
        self.to = to

        self.subjects = {
            'setClient': self.setClient,
            'setClientPay': self.setClientPay,
            'setTask': self.setTask,
            'setItemSell': self.setItemSell,
            'deleteTask': self.deleteTask,
            'addItem': self.addItem,
            'addGroup': self.addGroup,
            'updateItem': self.updateItem,
            'updateGroup': self.updateGroup,
            'addDisp':self.addDisp,
            'upgradeStaff':self.upgradeStaff
        }

    def switchSubject(self):
        return self.subjects[self.subject]()

    def setClient(self):
        body = self.body
        setClient(body['name'], body['membership'],
                  self.by, body['fee'], body['inscription'],body['advice'])

        return None

    def setClientPay(self):
        body = self.body

        res = setClientPay(body['name'], body['id'],
                           float(body['total']), self.by)

        return res

    def setTask(self):
        body = self.body

        setTask(body['name'], body['descr'],
                self.by, self.to(username=body['to']),
                body['duration'], int(body['importance']))

        return None

    def setItemSell(self):
        body = self.body
        res = setItemSell(body['name'], body['id'],
                          self.by, body['total'])

        return res

    def deleteTask(self):
        body = self.body
        deleteTask(
            deleteTask(int(body['id']))
        )

        return None

    def addItem(self):
        body = self.body
        addItem(body['name'], self.by, body['clusterName'], body['price'])

        return None

    def addDisp(self):
        body = self.body
        notice(body['text'],self.by.username,[body['staff_to']],'comunicado')
        #addDisp(body['text'],self.by.username,body['staff_to'])
        
        return None
    
    def upgradeStaff(self):
        body = self.body
        upgradeStaff(body['staff'],body['rank'])

    def addGroup(self):
        body = self.body
        addGroup(body['name'])

        return None

    def updateItem(self):
        body = self.body
        delete = body['action'] == 'delete'
        name = body['name'] if 'name' in body else None
        cluster = body['cluster'] if 'cluster' in body else None
        price = body['price'] if 'price' in body else None

        updateItem(body['id'],name,cluster,price,delete)
        return None

    def updateGroup(self):
        body = self.body
        delete = body['action'] == 'delete'
        name = body['name'] if 'name' in body else None

        updateGroup(body['id'],name,delete)
        return None
