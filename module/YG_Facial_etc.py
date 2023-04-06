from maya import cmds
from maya.internal.nodes.uvpin.node_interface import createRivet

from imp import reload

import Facial.module.YG_Facial_ARKitDict as ARKitDict
reload(ARKitDict)

from Facial.module.YG_Facial_ARKit import (
    makeCorrectiveShape,
    makePose,
    makePoseNew,
    defaultPose,
    defaultPoseNew,
    oldCon,
    newCon,
)

def createRivet2selVtx():
    # head
    ARKitDict.myMesh = cmds.textFieldButtonGrp('targetHeadAssign', q=True, text=True )

    # select vertex
    myList = ['956:957','1399','1416','1441','1458','1476','1491','1682:1683','1686','1708','1721','1738:1739','1741','1743','1745',
    '1753','1778','1781','1783:1784','1787','1789','1791','1793','1795','1797','1823:1824','1861','1863','1865','1874:1875','1888',
    '1932','1934','1946','2393','3473:3474','3936','3953','3978','3995','4013','4028','4219:4220','4223','4245','4258','4275:4276',
    '4278','4280','4282','4290','4315','4318','4320:4321','4324','4326','4328','4330','4332','4334','4361','4398','4400','4402',
    '4411:4412','4425','4469','4471','4483','4944']

    mySelList = []
    for i in myList:
        temp = ARKitDict.myMesh + '.vtx[' + i + ']'
        #print (temp)
        mySelList.append(temp)
    cmds.select(mySelList)

    # rivet
    createRivet()

def makeRivetJoint():
    # joint
    cmds.group(em=True, n='pin_grp')
    cmds.group(em=True, n='joint_grp')

    myJointList = []

    myPin = cmds.ls('pinOutput*', transforms=True)
    for i in myPin:
        # print (i)

        cmds.parent(i, 'pin_grp')

        cmds.select(cl=True)
        myJnt = cmds.joint()
        temp = i.replace('pinOutput', 'joint')
        cmds.rename(myJnt, temp)
        cmds.matchTransform(temp, i)
        cmds.parentConstraint(i, temp)
        cmds.parent(temp, 'joint_grp')

        myJointList.append(temp)

    # skin
    myEyeBrow = cmds.textFieldButtonGrp('eyebrowsAssign', q=True, text=True )
    myEyeLash = cmds.textFieldButtonGrp('eyelashesAssign', q=True, text=True )

    cmds.skinCluster(myJointList, myEyeBrow, tsb=True)
    cmds.skinCluster(myJointList, myEyeLash, tsb=True)



def makeBSetc():
    ARKitDict.myMesh = 'Default_etc'

    ARKitDict.myTargetGrp = cmds.group(em=True, n='target_grp')

    # make pose & duplicate
    for target in ARKitDict.etcList:
        print (target)

        makePose(target)
        cmds.duplicate(ARKitDict.myMesh, n=target, rc=True)

        if target != 'Default':
            cmds.parent(target, ARKitDict.myTargetGrp)
        else:
            if bool(cmds.listRelatives(target, p=True)):
                cmds.parent(target, world=True)

    # mouth close
    #makeCorrectiveShape('MouthClose', 'JawOpen')

    # eye
    makeCorrectiveShape('EyeBlinkLookDownLeft', 'EyeLookDownLeft')
    makeCorrectiveShape('EyeBlinkLookInLeft', 'EyeLookInLeft')
    makeCorrectiveShape('EyeBlinkLookOutLeft', 'EyeLookOutLeft')
    makeCorrectiveShape('EyeBlinkLookUpLeft', 'EyeLookUpLeft')
    makeCorrectiveShape('EyeBlinkSquintLeft', 'EyeSquintLeft')
    makeCorrectiveShape('EyeBlinkCheekSquintLeft', 'CheekSquintLeft')

    makeCorrectiveShape('EyeBlinkLookDownRight', 'EyeLookDownRight')
    makeCorrectiveShape('EyeBlinkLookInRight', 'EyeLookInRight')
    makeCorrectiveShape('EyeBlinkLookOutRight', 'EyeLookOutRight')
    makeCorrectiveShape('EyeBlinkLookUpRight', 'EyeLookUpRight')
    makeCorrectiveShape('EyeBlinkSquintRight', 'EyeSquintRight')
    makeCorrectiveShape('EyeBlinkCheekSquintRight', 'CheekSquintRight')

    # blendShape
    myTargetList = cmds.listRelatives(ARKitDict.myTargetGrp, c=True)
    cmds.blendShape( myTargetList, ARKitDict.myMesh, n='BS_ARKit_etc' )

    #if cmds.checkBox('deleteTargetCheck', q=True, v=True ):
    cmds.delete(ARKitDict.myTargetGrp)

    makePose('Default')
    #makePose('EyeBlinkLeft')

def BSconnect():
    myList = ['EyeBlinkLeft','EyeLookDownLeft','EyeLookInLeft','EyeLookOutLeft',
            'EyeLookUpLeft','EyeSquintLeft','EyeWideLeft','EyeBlinkRight','EyeLookDownRight',
            'EyeLookInRight','EyeLookOutRight','EyeLookUpRight','EyeSquintRight','EyeWideRight',
            'JawForward','JawLeft','JawRight','JawOpen','BrowDownLeft','BrowDownRight','BrowInnerUp',
            'BrowOuterUpLeft','BrowOuterUpRight','CheekSquintLeft','CheekSquintRight','NoseSneerLeft',
            'NoseSneerRight','EyeBlinkLookDownLeft','EyeBlinkLookInLeft','EyeBlinkLookOutLeft',
            'EyeBlinkLookUpLeft','EyeBlinkSquintLeft','EyeBlinkCheekSquintLeft','EyeBlinkLookDownRight',
            'EyeBlinkLookInRight','EyeBlinkLookOutRight','EyeBlinkLookUpRight','EyeBlinkSquintRight','EyeBlinkCheekSquintRight']

    for i in myList:
        #print(i)
        cmds.connectAttr ('BS_ARKit.'+i, 'BS_ARKit_etc.'+i, f=True)

def makeARKitBS():
    # ARKitDict.myMesh = 'Tolka_Face'
    ARKitDict.myMesh = cmds.textFieldButtonGrp('targetHeadAssign', q=True, text=True )

    # target group
    ARKitDict.myTargetGrp = cmds.group(em=True, n='target_grp')
    cmds.hide(ARKitDict.myTargetGrp)

    # make pose & duplicate
    for target in ARKitDict.myList:
        print(target)

        makePose(target)
        cmds.duplicate(ARKitDict.myMesh, n=target, rc=True)

        if target != 'Default':
            cmds.parent(target, ARKitDict.myTargetGrp)
        else:
            if bool(cmds.listRelatives(target, p=True)):
                cmds.parent(target, world=True)

    # mouth close
    makeCorrectiveShape('MouthClose', 'JawOpen')

    # eye
    makeCorrectiveShape('EyeBlinkLookDownLeft', 'EyeLookDownLeft')
    makeCorrectiveShape('EyeBlinkLookInLeft', 'EyeLookInLeft')
    makeCorrectiveShape('EyeBlinkLookOutLeft', 'EyeLookOutLeft')
    makeCorrectiveShape('EyeBlinkLookUpLeft', 'EyeLookUpLeft')
    makeCorrectiveShape('EyeBlinkSquintLeft', 'EyeSquintLeft')
    makeCorrectiveShape('EyeBlinkCheekSquintLeft', 'CheekSquintLeft')

    makeCorrectiveShape('EyeBlinkLookDownRight', 'EyeLookDownRight')
    makeCorrectiveShape('EyeBlinkLookInRight', 'EyeLookInRight')
    makeCorrectiveShape('EyeBlinkLookOutRight', 'EyeLookOutRight')
    makeCorrectiveShape('EyeBlinkLookUpRight', 'EyeLookUpRight')
    makeCorrectiveShape('EyeBlinkSquintRight', 'EyeSquintRight')
    makeCorrectiveShape('EyeBlinkCheekSquintRight', 'CheekSquintRight')

    # blendShape
    myTargetList = cmds.listRelatives(ARKitDict.myTargetGrp, c=True)
    cmds.blendShape( myTargetList, ARKitDict.myMesh, n='BS_ARKit' )

    # if cmds.checkBox('deleteTargetCheck', q=True, v=True ):
    #     cmds.delete(ARKitDict.myTargetGrp)

    makePose('Default')

# createRivet2selVtx()
# makeRivetJoint()
# makeBSetc()
# BSconnect()
