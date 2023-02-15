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
    mySel = cmds.ls(sl=True)
    for i in mySel:
        print (i)

        createRivet()

def makeRivetJoint():
    cmds.group(em=True, n='pin_grp')
    cmds.group(em=True, n='joint_grp')

    myPin = cmds.ls('pinOutput*', transforms=True)
    for i in myPin:
        print (i)

        cmds.parent(i, 'pin_grp')

        cmds.select(cl=True)
        myJnt = cmds.joint()
        temp = i.replace('pinOutput', 'joint')
        cmds.rename(myJnt, temp)
        cmds.matchTransform(temp, i)
        cmds.parentConstraint(i, temp)
        cmds.parent(temp, 'joint_grp')

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
    ARKitDict.myMesh = 'Tolka_Face'

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
