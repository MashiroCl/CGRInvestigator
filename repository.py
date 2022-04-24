import os
import json
import glob


# create a folder to save information under current script path
def create_folder(folder):
    path = folder
    try:
        os.mkdir(path)
    except FileExistsError:
        os.system("rm -rf " + folder)
        os.mkdir(path)
    return path


def delete_foler(folder):
    try:
        os.system("rm -rf " + folder)
    except FileNotFoundError:
        print("File not found")


class Repository:
    def __init__(self, path):
        self.repoPath = path
        self.RMoutputPath = self.repoPath + "/RMoutput"
        self.comparePath = self.repoPath + "/compare"

    def setComparePath(self, s: str):
        self.comparePath = s

    def setRMoutputPath(self, s: str):
        self.RMoutputPath = s

    def createWorkSpace(self):
        create_folder(self.RMoutputPath)
        create_folder(self.comparePath)

    def addRemote(self, path: str):
        command = "(cd " + path + " && git remote add origin https://example.jp/dummy_url.git)"
        os.system(command)

    def gitGc(self, path: str):
        command = "(cd " + path + " && git gc --aggressive --prune=now)"
        os.system(command)

    'git-stein version https://github.com/sh5i/git-stein, squash according to recipe.json'
    def squashCommits(self, recipe, git_stein, output, repository, steinOutput="."):
        '''
        squash commits according to recipe using git-stein
        :param recipe: path for recipe.json
        :param git_stein: path for git-stein-all.jar
        :param output:  path for new .git output
        :param repository: path for being squashed repository
        :return:
        '''
        command = "java -jar " + git_stein + " Clusterer " + "--recipe=" + recipe + " -v -o " + output + " " + repository + ">" + steinOutput + "/stein.log"
        os.system(command)
