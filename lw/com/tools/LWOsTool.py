import os


class LWOsTool(object):

    def __init__(self,filePath = os.getcwd()):
        if filePath:
            self.currentPath = filePath
        if not os.path.exists(self.currentPath):
            os.makedirs(self.currentPath)

    def saveDatas(self,fileName,datas):
        cur_modle = 'a+'
        if type(datas) == bytes:
            cur_modle = 'wb+'
        if fileName:
            self.currentPath = self.currentPath + '/{}'.format(fileName)

        try:
            with open (self.currentPath,cur_modle ) as file:
                file.write (datas)
        except RuntimeError as error:
            print(error)


