import json
from RefactoringOperation.RefactoringOperation import RefactoringOperation


class RMcommit:
    def __init__(self,jsonPath):
        self.jsonPath = jsonPath
        self.commitID = ""
        self.refactorings=list()
        self._initFromRMjson()

    def _initFromRMjson(self):
        '''
        using result extracted from RefactoringMiner to initialize RefactoringOperation class
        :param jsonPath: file path for RefactoringMiner json result
        :return: sha1,type,description
        '''
        with open(self.jsonPath) as f:
            data = json.load(f)
        try:
            self.commitID = data["commits"][0]["sha1"]
            refactorings = data["commits"][0]["refactorings"]
            for each in refactorings:
                ro = RefactoringOperation(each,self.commitID)
                self.refactorings.append(ro)
        except KeyError:
            pass
        except IndexError:
            pass