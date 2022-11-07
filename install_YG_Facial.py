import maya.cmds as cmds
import maya.mel as mel

gShelfTopLevel = mel.eval("$tmpVar=$gShelfTopLevel")
myTap = cmds.tabLayout(gShelfTopLevel, query=True, selectTab=True)
myCommand = '''import Facial.module.YG_Facial
reload(Facial.module.YG_Facial)'''
usd = cmds.internalVar(usd=True)
mayascripts = '%s/%s' % (usd.rsplit('/', 3)[0], 'scripts/')
tempPath = mayascripts+"Facial/icon/"
cmds.shelfButton(command=myCommand,
                 annotation="YG_Facial",
                 label='YG_Facial',
                 image=tempPath+'YG_Facial.bmp',
                 parent=myTap)


