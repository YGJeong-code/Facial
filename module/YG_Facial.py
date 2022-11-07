import maya.cmds as cmds

#class
class YG_Facial(object):
    def __init__(self):
        self.myWin = 'YG_Facial'
        self.size = 150
        self.createWindow()

    def createWindow(self):
        if cmds.window(self.myWin, ex=True):
            cmds.deleteUI(self.myWin)

        self.myWin = cmds.window(self.myWin, t=self.myWin+'_v0.1', sizeable=True, resizeToFitChildren=True)
        self.myColor = {'red':[0.6,0,0],'orange':[0.6, 0.2, 0],'yellow':[0.7, 0.6, 0.1],'green':[0.4, 0.6, 0.1]}

        ## build
        cmds.columnLayout( adjustableColumn=True, p=self.myWin )
        self.targetFrame = cmds.frameLayout( label='Target', collapsable=True, collapse=False, bgc=self.myColor['red'], cc=self.winResize, ec=self.winResize)
        cmds.columnLayout( adjustableColumn=1, p=self.targetFrame )
        cmds.button(label='make ARKit target', w=self.size*2, c=self.makeARKitTargetBtn)
        cmds.setParent( '..' )
        cmds.setParent( '..' )

        ## window
        cmds.showWindow(self.myWin)

    ############################################################################################################################################################################################################################
    # btn
    ############################################################################################################################################################################################################################
    def makeARKitTargetBtn(self, *args):
        import Facial.module.YG_Facial_ARKit

    ############################################################################################################################################################################################################################
    # window resize
    ############################################################################################################################################################################################################################
    def winResize(self, *args):
        cmds.window(self.myWin, e=True, w=50L, h=50L)

    def getsize(self, *args):
        size = cmds.window(self.myWin, q=True, widthHeight=True)
        print size

myTest = YG_Facial()
myTest.winResize()
