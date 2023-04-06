import maya.cmds as cmds
import Facial.module.YG_Facial_ARKit as ARKit
import Facial.module.YG_Facial_ARKitDict as ARKitDict
import Facial.module.YG_Facial_etc as etc
from imp import reload
reload(ARKit)
reload(etc)

#class
class YG_Facial(object):
    def __init__(self):
        self.myWin = 'YG_Facial'
        self.size = 150

        self.createWindow()

        self.myUpAxis = cmds.upAxis( q=True, axis=True )
        if self.myUpAxis == 'z':
            cmds.radioButton(self.upAxisZBtn, e=True, select=True)

        # assign target head
        if cmds.objExists('head_lod0_mesh'):
            cmds.textFieldButtonGrp('targetHeadAssign', e=True, text='head_lod0_mesh')

    def createWindow(self):
        if cmds.window(self.myWin, ex=True):
            cmds.deleteUI(self.myWin)

        self.myWin = cmds.window(self.myWin, t=self.myWin+'_v1.3', sizeable=True, resizeToFitChildren=True)
        self.myColor = {'red':[0.6,0,0],'orange':[0.6, 0.2, 0],'yellow':[0.7, 0.6, 0.1],'green':[0.4, 0.6, 0.1]}

        ## up axis
        cmds.columnLayout( adjustableColumn=True, p=self.myWin )
        self.upAxisFrame = cmds.frameLayout( label='Up Axis', collapsable=True, collapse=False, bgc=self.myColor['red'], cc=self.winResize, ec=self.winResize)
        cmds.columnLayout( adjustableColumn=1, p=self.upAxisFrame )
        cmds.rowLayout( numberOfColumns=2, columnWidth2=(self.size/2, self.size/2) )
        cmds.radioCollection()
        self.upAxisYBtn = cmds.radioButton( label='Y', select=True, cc=lambda *_:self.setUpAxis('y'))
        self.upAxisZBtn = cmds.radioButton( label='Z', cc=lambda *_:self.setUpAxis('z'))
        cmds.setParent( '..' )
        cmds.setParent( '..' )

        ## target
        cmds.columnLayout( adjustableColumn=True, p=self.myWin )
        self.targetFrame = cmds.frameLayout( label='Target', collapsable=True, collapse=False, bgc=self.myColor['orange'], cc=self.winResize, ec=self.winResize)
        cmds.columnLayout( adjustableColumn=1, p=self.targetFrame )
        cmds.textFieldButtonGrp('targetHeadAssign', label='Target Head : ', text='text', buttonLabel='Assign', editable=False, adjustableColumn=2, columnAlign=(1,'left'), columnWidth=(2,130), bc=lambda *_:self.assignBtn('targetHeadAssign') )
        cmds.checkBox('combineHeadGrp', label='Combine Head Group', v=True )
        cmds.checkBox('deleteTargetCheck', label='Delete Target', v=True )

        cmds.button(label='make ARKit target', w=self.size*2, c=self.makeARKitTargetBtn)

        # cmds.checkBox('shaderCheck', label='Shader Connect', v=True )
        cmds.button(label='connect UI', w=self.size*2, c=self.connectUIBtn)

        cmds.button(label='delete MetaHuman', w=self.size*2, c=self.deleteMetaHumanBtn)

        cmds.separator()
        cmds.button(label='skin transfer A to B', w=self.size*2, c=self.skinTransfer)

        cmds.separator()
        cmds.button(label='make keyframes ARKit list', w=self.size*2, c=self.makeKeyframsARKitList)
        # cmds.button(label='make expressions key', w=self.size*2, c=self.makeExpressionsKey)

        cmds.separator()
        cmds.text(label='Face etc')
        cmds.textFieldButtonGrp('eyebrowsAssign', label='Eyebrows : ', text='text', buttonLabel='Assign', editable=False, adjustableColumn=2, columnAlign=(1,'left'), columnWidth=(2,130), bc=lambda *_:self.assignBtn('eyebrowsAssign') )
        cmds.textFieldButtonGrp('eyelashesAssign', label='Eyelashes : ', text='text', buttonLabel='Assign', editable=False, adjustableColumn=2, columnAlign=(1,'left'), columnWidth=(2,130), bc=lambda *_:self.assignBtn('eyelashesAssign') )
        cmds.button(label='make face etc rig', w=self.size*2, c=self.makeFaceEtcRig)

        cmds.setParent( '..' )
        cmds.setParent( '..' )

        ## pose
        cmds.columnLayout( adjustableColumn=True, p=self.myWin )
        self.poseFrame = cmds.frameLayout( label='Pose', collapsable=True, collapse=True, bgc=self.myColor['yellow'], cc=self.winResize, ec=self.winResize)
        cmds.columnLayout( adjustableColumn=1, p=self.poseFrame )
        cmds.button(label='0 Default', w=self.size*2, c=lambda *_:self.makePose('Default'))

        cmds.text(l='eye', align='left')
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=(self.size, self.size), adjustableColumn=1)
        cmds.button(label='1 EyeBlinkLeft', w=self.size, c=lambda *_:self.makePose('EyeBlinkLeft'))
        cmds.button(label='8 EyeBlinkRight', w=self.size, c=lambda *_:self.makePose('EyeBlinkRight'))

        cmds.button(label='2 EyeLookDownLeft', w=self.size, c=lambda *_:self.makePose('EyeLookDownLeft'))
        cmds.button(label='9 EyeLookDownRight', w=self.size, c=lambda *_:self.makePose('EyeLookDownRight'))

        cmds.button(label='3 EyeLookInLeft', w=self.size, c=lambda *_:self.makePose('EyeLookInLeft'))
        cmds.button(label='10 EyeLookInRight', w=self.size, c=lambda *_:self.makePose('EyeLookInRight'))

        cmds.button(label='4 EyeLookOutLeft', w=self.size, c=lambda *_:self.makePose('EyeLookOutLeft'))
        cmds.button(label='11 EyeLookOutRight', w=self.size, c=lambda *_:self.makePose('EyeLookOutRight'))

        cmds.button(label='5 EyeLookUpLeft', w=self.size, c=lambda *_:self.makePose('EyeLookUpLeft'))
        cmds.button(label='12 EyeLookUpRight', w=self.size, c=lambda *_:self.makePose('EyeLookUpRight'))

        cmds.button(label='6 EyeSquintLeft', w=self.size, c=lambda *_:self.makePose('EyeSquintLeft'))
        cmds.button(label='13 EyeSquintRight', w=self.size, c=lambda *_:self.makePose('EyeSquintRight'))

        cmds.button(label='7 EyeWideLeft', w=self.size, c=lambda *_:self.makePose('EyeWideLeft'))
        cmds.button(label='14 EyeWideRight', w=self.size, c=lambda *_:self.makePose('EyeWideRight'))

        cmds.columnLayout( adjustableColumn=1, p=self.poseFrame )
        cmds.text(l='jaw', align='left')
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=(self.size, self.size), adjustableColumn=1)
        cmds.button(label='15 JawForward', w=self.size, c=lambda *_:self.makePose('JawForward'))
        cmds.button(label='16 JawLeft', w=self.size, c=lambda *_:self.makePose('JawLeft'))
        cmds.button(label='17 JawRight', w=self.size, c=lambda *_:self.makePose('JawRight'))
        cmds.button(label='18 JawOpen', w=self.size, c=lambda *_:self.makePose('JawOpen'))

        cmds.columnLayout( adjustableColumn=1, p=self.poseFrame )
        cmds.text(l='mouth', align='left')
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=(self.size, self.size), adjustableColumn=1)
        cmds.button(label='19 MouthClose', w=self.size, c=lambda *_:self.makePose('MouthClose'))
        cmds.button(label='', w=self.size, enable=False)
        cmds.button(label='20 MouthFunnel', w=self.size, c=lambda *_:self.makePose('MouthFunnel'))
        cmds.button(label='21 MouthPucker', w=self.size, c=lambda *_:self.makePose('MouthPucker'))
        cmds.button(label='22 MouthLeft', w=self.size, c=lambda *_:self.makePose('MouthLeft'))
        cmds.button(label='23 MouthRight', w=self.size, c=lambda *_:self.makePose('MouthRight'))
        cmds.button(label='24 MouthSmileLeft', w=self.size, c=lambda *_:self.makePose('MouthSmileLeft'))
        cmds.button(label='25 MouthSmileRight', w=self.size, c=lambda *_:self.makePose('MouthSmileRight'))
        cmds.button(label='26 MouthFrownLeft', w=self.size, c=lambda *_:self.makePose('MouthFrownLeft'))
        cmds.button(label='27 MouthFrownRight', w=self.size, c=lambda *_:self.makePose('MouthFrownRight'))
        cmds.button(label='28 MouthDimpleLeft', w=self.size, c=lambda *_:self.makePose('MouthDimpleLeft'))
        cmds.button(label='29 MouthDimpleRight', w=self.size, c=lambda *_:self.makePose('MouthDimpleRight'))
        cmds.button(label='30 MouthStretchLeft', w=self.size, c=lambda *_:self.makePose('MouthStretchLeft'))
        cmds.button(label='31 MouthStretchRight', w=self.size, c=lambda *_:self.makePose('MouthStretchRight'))
        cmds.button(label='32 MouthRollLower', w=self.size, c=lambda *_:self.makePose('MouthRollLower'))
        cmds.button(label='33 MouthRollUpper', w=self.size, c=lambda *_:self.makePose('MouthRollUpper'))
        cmds.button(label='34 MouthShrugLower', w=self.size, c=lambda *_:self.makePose('MouthShrugLower'))
        cmds.button(label='35 MouthShrugUpper', w=self.size, c=lambda *_:self.makePose('MouthShrugUpper'))
        cmds.button(label='36 MouthPressLeft', w=self.size, c=lambda *_:self.makePose('MouthPressLeft'))
        cmds.button(label='37 MouthPressRight', w=self.size, c=lambda *_:self.makePose('MouthPressRight'))
        cmds.button(label='38 MouthLowerDownLeft', w=self.size, c=lambda *_:self.makePose('MouthLowerDownLeft'))
        cmds.button(label='39 MouthLowerDownRight', w=self.size, c=lambda *_:self.makePose('MouthLowerDownRight'))
        cmds.button(label='40 MouthUpperUpLeft', w=self.size, c=lambda *_:self.makePose('MouthUpperUpLeft'))
        cmds.button(label='41 MouthUpperUpRight', w=self.size, c=lambda *_:self.makePose('MouthUpperUpRight'))

        cmds.columnLayout( adjustableColumn=1, p=self.poseFrame )
        cmds.text(l='brow', align='left')
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=(self.size, self.size), adjustableColumn=1)
        cmds.button(label='42 BrowDownLeft', w=self.size, c=lambda *_:self.makePose('BrowDownLeft'))
        cmds.button(label='43 BrowDownRight', w=self.size, c=lambda *_:self.makePose('BrowDownRight'))
        cmds.button(label='44 BrowInnerUp', w=self.size, c=lambda *_:self.makePose('BrowInnerUp'))
        cmds.button(label='', w=self.size, enable=False)
        cmds.button(label='45 BrowOuterUpLeft', w=self.size, c=lambda *_:self.makePose('BrowOuterUpLeft'))
        cmds.button(label='46 BrowOuterUpRight', w=self.size, c=lambda *_:self.makePose('BrowOuterUpRight'))

        cmds.columnLayout( adjustableColumn=1, p=self.poseFrame )
        cmds.text(l='cheek', align='left')
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=(self.size, self.size), adjustableColumn=1)
        cmds.button(label='47 CheekPuff', w=self.size, c=lambda *_:self.makePose('CheekPuff'))
        cmds.button(label='', w=self.size, enable=False)
        cmds.button(label='48 CheekSquintLeft', w=self.size, c=lambda *_:self.makePose('CheekSquintLeft'))
        cmds.button(label='49 CheekSquintRight', w=self.size, c=lambda *_:self.makePose('CheekSquintRight'))

        cmds.columnLayout( adjustableColumn=1, p=self.poseFrame )
        cmds.text(l='nose', align='left')
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=(self.size, self.size), adjustableColumn=1)
        cmds.button(label='50 NoseSneerLeft', w=self.size, c=lambda *_:self.makePose('NoseSneerLeft'))
        cmds.button(label='51 NoseSneerRight', w=self.size, c=lambda *_:self.makePose('NoseSneerRight'))

        cmds.setParent( '..' )
        cmds.setParent( '..' )

        ## window
        cmds.showWindow(self.myWin)

    ############################################################################################################################################################################################################################
    # btn
    ############################################################################################################################################################################################################################
    def makeARKitTargetBtn(self, *args):
        ARKit.duplicateLODGroup()

    def makePose(self, target):
        ARKit.makePose(target)

    def setUpAxis(self, axis):
        cmds.upAxis( ax=axis, rv=True )

        if axis == 'y':
            if bool(cmds.ls('root_drv')):
                cmds.setAttr('root_drv.rx', -90)
                cmds.setAttr('headRig_grp.rx', -90)
                cmds.setAttr('Lights.rx', -90)
        else:
            if bool(cmds.ls('root_drv')):
                cmds.setAttr('root_drv.rx', 0)
                cmds.setAttr('headRig_grp.rx', 0)
                cmds.setAttr('Lights.rx', 0)

    def deleteMetaHumanBtn(self, *args):
        # cmds.delete('DHIhead:spine_04','DHIbody:root','root_drv','rig','Body_joints','FacialControls','PSD')

        try:
            cmds.delete('polySurface1')
            cmds.delete('head_grp')
        except:
            pass

        cmds.setAttr('Default.tx', 0)
        cmds.setAttr('CTRL_faceGUI.tx', 20)

    def connectUIBtn(self, *args):
        ARKit.connectBlendShape2UI()

    def assignBtn(self, assign):
        mySel = cmds.ls(sl=True)[0]
        cmds.textFieldButtonGrp(assign, e=True, text=mySel)

    def skinTransfer(self, *args):
        mySource = cmds.ls(sl=True, l=True)[0]
        mySourceShape = cmds.listRelatives (mySource, s=True, f=True)[0]

        temp = cmds.listHistory(mySourceShape, lv=True)
        mySkinJNT = []
        for i in temp:
        	if 'skinCluster' in i:
        		mySkinJNT = cmds.skinCluster(i,query=True,inf=True)

        myTarget = cmds.ls(sl=True, l=True)[1]

        cmds.select (myTarget, mySkinJNT, r=True)
        cmds.optionVar(iv=[('multipleBindPosesOpt',1),('bindMethod',1),('bindTo',2),
                    ('skinMethod',1),('removeUnusedInfluences',0),('colorizeSkeleton',0),
                    ('maxInfl',3),('normalizeWeights',2),('obeyMaxInfl',0)])
        cmds.SmoothBindSkin()

        cmds.select (mySource, myTarget, r=True)
        cmds.copySkinWeights  (noMirror=True, surfaceAssociation='closestPoint', influenceAssociation='closestJoint')

    def makeKeyframsARKitList(self, *args):
        myList = ARKitDict.myList
        for i in range(len(myList)):
            print(i, myList[i])

            cmds.currentTime(i)
            ARKit.makePose(myList[i])

            myCon = cmds.ls('CTRL_*', tr=True, s=False)
            cmds.setKeyframe(myCon, attribute=('tx','ty'))

    def makeExpressionsKey(self, *args):
        myList = ARKitDict.myExpresstionList
        cmds.playbackOptions(min=0, max=len(myList), aet=len(myList))

        myNode = 'CTRL_expressions'
        # attrs = cmds.listAttr(myNode, k=True)

        # disconnect
        for i in myList:
            cmds.disconnectAttr (myNode+'_'+i+'.output', myNode+'.'+i)

        # zero key
        cmds.currentTime(0)
        for attr in myList:
            cmds.setAttr(myNode+'.'+attr, 0)
            cmds.setKeyframe(myNode, attribute=attr)

        # pose key
        for i in range(len(myList)):
            print(i, myList[i])
            cmds.currentTime(i+1)

            for attr in myList:
                cmds.setAttr(myNode+'.'+attr, 0)
                cmds.setKeyframe(myNode, attribute=attr)

            cmds.setAttr(myNode+'.'+myList[i], 1)

    def makeFaceEtcRig(self, *args):
        etc.createRivet2selVtx()
        etc.makeRivetJoint()

    ############################################################################################################################################################################################################################
    # window resize
    ############################################################################################################################################################################################################################
    def winResize(self, *args):
        cmds.window(self.myWin, e=True, w=50, h=50)

    def getsize(self, *args):
        size = cmds.window(self.myWin, q=True, widthHeight=True)
        print (size)

myClass = YG_Facial()
myClass.winResize()
