import sys

sys.path.append('../')
from repository import create_folder
from logger import logger_config
from utils import getConfig
import os

from ROExtract.extractRO import extractRO


def runServer(repoPath, squashedOutput, outputRepoDirectory, coarseGranularity):
    data = getConfig()
    RMPath = data["local"]["RMPath"]
    git_stein = data["local"]["git_stein"]

    repoName = repoPath.split("/")[-1]

    outputRepoDirectory = os.path.join(outputRepoDirectory, repoName)
    create_folder(outputRepoDirectory)
    recipe = os.path.join(outputRepoDirectory, "recipe.json")
    squashedOutput = os.path.join(squashedOutput, repoName)

    # start refactoring operations extractions according set CGR
    for num in range(coarseGranularity[0], coarseGranularity[1]):
        jsonOutputDirectory = os.path.join(outputRepoDirectory, str(num))
        create_folder(jsonOutputDirectory)
        logger = logger_config(log_path=outputRepoDirectory + '/log' + str(num) + '.txt',
                               logging_name=repoName + " " + str(num) + "by" + str(num))

        logger.info("start squash " + str(num) + "by" + str(num))
        extractRO(RMPath=RMPath,
                  repoPath=repoPath,
                  recipe=recipe, git_stein=git_stein,
                  squashedOutput=squashedOutput,
                  clusterNum=num, jsonOutputDirectory=jsonOutputDirectory, logger=logger,
                  steinOuput=outputRepoDirectory)
        logger.info("finish squash " + str(num) + "by" + str(num))

    os.system("rm -rf " + squashedOutput)
