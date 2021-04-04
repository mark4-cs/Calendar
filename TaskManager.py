import numpy as np
from User import User
numDays, numSectionsDay = 7, 288


class TaskManager:
    def __init__(self, tasksArr=[], user = User()):
        self.user = user
        self.tasksArr = tasksArr
        self.organizer = np.array([None] * (numDays*numSectionsDay)).reshape(numDays,numSectionsDay)

    def addTask(self, task, reorder = False):
        if task not in self.tasksArr:
            self.tasksArr.append(task)
            self.reorderOrganizer() if reorder else self.pushTask(task)

    def delTasl(self, task, reorder = False):
        if task in self.tasksArr:
            self.tasksArr.remove(task)
            self.reorderOrganizer() if reorder else self.delFromOrganizer()

    def reorderOrganizer(self):
        pass
    def pushTask(self, task):
        pass
    def delFromOrganizer(self, task):
        np.delete(self.organizer, task)

class Task:
    def __init__(self, id = 0, name = 0, duration = 0, deadline = 0, color = 0, userTxt = 0):
        self.id = id
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.color = color
        self.userTxt = userTxt



if __name__ == '__main__':
    a = np.array([None] * (7*4)).reshape(7,4)
    t = Task()
    a[1][1] = t
    a[1][3] = t
    a[3][3] = t
    print(a)
    a = np.where(a == t, None, a)
    print(a)