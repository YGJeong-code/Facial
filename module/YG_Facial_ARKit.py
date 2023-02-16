import maya.cmds as cmds
import maya.mel as mel
import Facial.module.YG_Facial_ARKitDict as ARKitDict
from imp import reload
reload(ARKitDict)

def makeCorrectiveShape(target, pose):
    print (target)

    # mouth close
    makePose('Default')
    myHead = cmds.duplicate(ARKitDict.myMesh)

    makePose(target)
    target1 = cmds.duplicate(ARKitDict.myMesh)

    makePose(pose)
    target2 = cmds.duplicate(ARKitDict.myMesh)

    myBlend = cmds.blendShape( target1, target2, myHead )
    cmds.setAttr(myBlend[0]+'.'+target1[0], 1)
    cmds.setAttr(myBlend[0]+'.'+target2[0], -1)

    myTarget = cmds.duplicate(myHead, n=target, rc=True)
    cmds.parent(myTarget[0], ARKitDict.myTargetGrp)
    cmds.delete(myHead,target1,target2)

# makeCorrectiveShape('MouthClose', 'JawOpen')

def duplicateLODGroup():
    if cmds.checkBox('combineHeadGrp', q=True, v=True ):
        # combine mesh
        myList = cmds.listRelatives('head_lod0_grp', c=True)
        myMesh = cmds.polyUniteSkinned( myList, ch=0 )
        ARKitDict.myMesh = myMesh[0]
    else:
    # head only
        ARKitDict.myMesh = cmds.textFieldButtonGrp('targetHeadAssign', q=True, text=True )

    # target group
    ARKitDict.myTargetGrp = cmds.group(em=True, n='target_grp')
    cmds.hide(ARKitDict.myTargetGrp)

    # make pose & duplicate
    for target in ARKitDict.myList:
        print (target)

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
    # cmds.blendShape( myTargetList, ARKitDict.myMesh, n='BS_ARKit' )
    cmds.blendShape( myTargetList, 'Default', n='BS_ARKit' )

    if cmds.checkBox('deleteTargetCheck', q=True, v=True ):
        cmds.delete(ARKitDict.myTargetGrp)

    makePose('Default')

    # unlock
    myList = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr('%s.%s' % ('Default', i), keyable=True, lock=False)

    cmds.setAttr ("Default.tx", -27)

    # connect blendShape 2 ui
    importUI()
    # connectBlendShape2UI()

# pose
def newCon(con):
    cmds.ls(con)
    for i in cmds.ls(con):
        if 'head_grp' not in cmds.listRelatives(i, f=True)[0]:
            return i

def oldCon(con):
    cmds.ls(con)
    for i in cmds.ls(con):
        if 'head_grp' in cmds.listRelatives(i, f=True)[0]:
            return i

def defaultPoseNew():
    for item in ARKitDict.myNewDict:
        for con in ARKitDict.myNewDict[item]:
            for axis in ARKitDict.myNewDict[item][con]:
                cmds.setAttr(newCon(con)+'.'+axis, 0)
                cmds.setAttr(newCon('CTRL_C_eye')+'.tx', 0)
                cmds.setAttr(newCon('CTRL_C_eye')+'.ty', 0)

def defaultPose():
    for item in ARKitDict.myDict:
        for con in ARKitDict.myDict[item]:
            for axis in ARKitDict.myDict[item][con]:
                if bool(oldCon(con)):
                    cmds.setAttr(oldCon(con)+'.'+axis, 0)
                    cmds.setAttr(oldCon('CTRL_C_eye')+'.tx', 0)
                    cmds.setAttr(oldCon('CTRL_C_eye')+'.ty', 0)
                elif bool(newCon(con)):
                    defaultPoseNew()
                # if len(cmds.ls('CTRL_C_eye'))>1:
                #     defaultPoseNew()
                #     cmds.setAttr(oldCon(con)+'.'+axis, 0)
                #     cmds.setAttr(oldCon('CTRL_C_eye')+'.tx', 0)
                #     cmds.setAttr(oldCon('CTRL_C_eye')+'.ty', 0)
                # else:
                #     cmds.setAttr(con+'.'+axis, 0)

def makePoseNew(target):
    if target == 'Default':
        defaultPoseNew()
    else:
        defaultPoseNew()

        for con in ARKitDict.myNewDict[target]:
            for axis in ARKitDict.myNewDict[target][con]:
                value = ARKitDict.myNewDict[target][con][axis]
                cmds.setAttr(newCon(con)+'.'+axis, value)

def makePose(target):
    if target == 'Default':
        defaultPose()
    else:
        defaultPose()

        for con in ARKitDict.myDict[target]:
            for axis in ARKitDict.myDict[target][con]:
                value = ARKitDict.myDict[target][con][axis]
                if bool(oldCon(con)):
                    cmds.setAttr(oldCon(con)+'.'+axis, value)
                elif bool(newCon(con)):
                    makePoseNew(target)
                else:
                    makePoseNew(target)

                # if len(cmds.ls('CTRL_C_eye'))>1:
                #     makePoseNew(target)
                #     cmds.setAttr(oldCon(con)+'.'+axis, value)
                # else:
                #     cmds.setAttr(con+'.'+axis, value)

def importUI():
    usd = cmds.internalVar(usd=True)
    mayascripts = '%s/%s' % (usd.rsplit('/', 3)[0], 'scripts/')
    tempPath = mayascripts + "Facial/template/facial_ui_v01.ma"

    cmds.file(tempPath, i=True)

# connect
def connectExpToTarget(con, axis, conExp, target):
    cmds.connectAttr ( newCon(con)+'.'+axis, conExp+'.input', f=True )

    myExpTarget = newCon('CTRL_expressions') + '.' + conExp.replace( 'CTRL_expressions_', '' )
    cmds.connectAttr ( conExp+'.output', myExpTarget, f=True )
    cmds.connectAttr ( myExpTarget, 'BS_ARKit.'+target, f=True )

def connectExp(con, axis, conExp):
    cmds.connectAttr ( newCon(con)+'.'+axis, conExp+'.input', f=True )

    myExpTarget = newCon('CTRL_expressions') + '.' + conExp.replace( 'CTRL_expressions_', '' )
    cmds.connectAttr ( conExp+'.output', myExpTarget, f=True )
    # cmds.connectAttr ( myExpTarget, 'BS_ARKit.'+target, f=True )

def eyeBlinkConnect(target, exp, blink):
    myCond = cmds.createNode('condition', n=target+'_cond')
    cmds.setAttr(myCond+'.operation', 2)

    myMult = cmds.createNode('multiplyDivide', n=target+'_mult')

    cmds.connectAttr(oldCon('CTRL_expressions')+'.'+exp, myCond+'.colorIfTrueR', f=True)
    cmds.connectAttr(oldCon('CTRL_expressions')+'.'+blink, myCond+'.firstTerm', f=True)
    cmds.connectAttr (myCond+'.outColorR', myMult+'.input1X', f=True)
    cmds.connectAttr (oldCon('CTRL_expressions')+'.'+blink, myMult+'.input2X', f=True)
    cmds.connectAttr (myMult+'.outputX', 'BS_ARKit.'+target, f=True)

def eyeConnect():
    # CTRL_C_eye
    cmds.connectAttr ( newCon('CTRL_C_eye')+'.tx', 'animCurveUA1.input', f=True )
    cmds.connectAttr ( newCon('CTRL_C_eye')+'.ty', 'animCurveUA2.input', f=True )
    cmds.connectAttr ( newCon('CTRL_C_eye')+'.tx', 'animCurveUA3.input', f=True )
    cmds.connectAttr ( newCon('CTRL_C_eye')+'.ty', 'animCurveUA4.input', f=True )

    # CTRL_L_eye
    cmds.connectAttr ( newCon('CTRL_L_eye')+'.tx', 'LOC_L_eyeUIDriver_rotateY.input', f=True )
    cmds.connectAttr ( newCon('CTRL_L_eye')+'.ty', 'LOC_L_eyeUIDriver_rotateX.input', f=True )

    # CTRL_R_eye
    cmds.connectAttr ( newCon('CTRL_R_eye')+'.tx', 'LOC_R_eyeUIDriver_rotateY.input', f=True )
    cmds.connectAttr ( newCon('CTRL_R_eye')+'.ty', 'LOC_R_eyeUIDriver_rotateX.input', f=True )

    # BS
    cmds.connectAttr ( 'CTRL_expressions_eyeLookLeftL.output', 'BS_ARKit.EyeLookOutLeft', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeLookLeftR.output', 'BS_ARKit.EyeLookInRight', f=True )

    cmds.connectAttr ( 'CTRL_expressions_eyeLookRightL.output', 'BS_ARKit.EyeLookInLeft', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeLookRightR.output', 'BS_ARKit.EyeLookOutRight', f=True )

    cmds.connectAttr ( 'CTRL_expressions_eyeLookUpL.output', 'BS_ARKit.EyeLookUpLeft', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeLookUpR.output', 'BS_ARKit.EyeLookUpRight', f=True )

    cmds.connectAttr ( 'CTRL_expressions_eyeLookDownL.output', 'BS_ARKit.EyeLookDownLeft', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeLookDownR.output', 'BS_ARKit.EyeLookDownRight', f=True )

    # CTRL_L_eye_blink
    cmds.connectAttr ( newCon('CTRL_L_eye_blink')+'.ty', 'CTRL_expressions_eyeBlinkL.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeBlinkL.output', 'BS_ARKit.EyeBlinkLeft', f=True )

    cmds.connectAttr ( newCon('CTRL_L_eye_blink')+'.ty', 'CTRL_expressions_eyeWidenL.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeWidenL.output', 'BS_ARKit.EyeWideLeft', f=True )

    # CTRL_R_eye_blink
    cmds.connectAttr ( newCon('CTRL_R_eye_blink')+'.ty', 'CTRL_expressions_eyeBlinkR.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeBlinkR.output', 'BS_ARKit.EyeBlinkRight', f=True )

    cmds.connectAttr ( newCon('CTRL_R_eye_blink')+'.ty', 'CTRL_expressions_eyeWidenR.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeWidenR.output', 'BS_ARKit.EyeWideRight', f=True )

    # CTRL_L_eye_squintInner
    cmds.connectAttr ( newCon('CTRL_L_eye_squintInner')+'.ty', 'CTRL_expressions_eyeSquintInnerL.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeSquintInnerL.output', 'BS_ARKit.EyeSquintLeft', f=True )

    # CTRL_R_eye_squintInner
    cmds.connectAttr ( newCon('CTRL_R_eye_squintInner')+'.ty', 'CTRL_expressions_eyeSquintInnerR.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeSquintInnerR.output', 'BS_ARKit.EyeSquintRight', f=True )

    # CTRL_L_eye_cheekRaise
    cmds.connectAttr ( newCon('CTRL_L_eye_cheekRaise')+'.ty', 'CTRL_expressions_eyeCheekRaiseL.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeCheekRaiseL.output', 'BS_ARKit.CheekSquintLeft', f=True )

    # CTRL_R_eye_cheekRaise
    cmds.connectAttr ( newCon('CTRL_R_eye_cheekRaise')+'.ty', 'CTRL_expressions_eyeCheekRaiseR.input', f=True )
    cmds.connectAttr ( 'CTRL_expressions_eyeCheekRaiseR.output', 'BS_ARKit.CheekSquintRight', f=True )

    # minus eye blink
    myBlinkPlus = cmds.createNode('plusMinusAverage', n='EyeBlinkLeft_plus')
    cmds.setAttr(myBlinkPlus+'.operation', 2)

    cmds.connectAttr(oldCon('CTRL_expressions')+'.eyeBlinkL', myBlinkPlus+'.input1D[0]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookDownLeft', myBlinkPlus+'.input1D[1]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookInLeft', myBlinkPlus+'.input1D[2]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookOutLeft', myBlinkPlus+'.input1D[3]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookUpLeft', myBlinkPlus+'.input1D[4]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkSquintLeft', myBlinkPlus+'.input1D[5]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkCheekSquintLeft', myBlinkPlus+'.input1D[6]', f=True)
    cmds.connectAttr (myBlinkPlus+'.output1D', 'BS_ARKit.EyeBlinkLeft', f=True)

    myBlinkPlus = cmds.createNode('plusMinusAverage', n='EyeBlinkRight_plus')
    cmds.setAttr(myBlinkPlus+'.operation', 2)

    cmds.connectAttr(oldCon('CTRL_expressions')+'.eyeBlinkR', myBlinkPlus+'.input1D[0]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookDownRight', myBlinkPlus+'.input1D[1]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookInRight', myBlinkPlus+'.input1D[2]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookOutRight', myBlinkPlus+'.input1D[3]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkLookUpRight', myBlinkPlus+'.input1D[4]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkSquintRight', myBlinkPlus+'.input1D[5]', f=True)
    cmds.connectAttr ('BS_ARKit.EyeBlinkCheekSquintRight', myBlinkPlus+'.input1D[6]', f=True)
    cmds.connectAttr (myBlinkPlus+'.output1D', 'BS_ARKit.EyeBlinkRight', f=True)

    # connect
    eyeBlinkConnect('EyeBlinkLookDownLeft', 'eyeLookDownL', 'eyeBlinkL')
    eyeBlinkConnect('EyeBlinkLookInLeft', 'eyeLookRightL', 'eyeBlinkL')
    eyeBlinkConnect('EyeBlinkLookOutLeft', 'eyeLookLeftL', 'eyeBlinkL')
    eyeBlinkConnect('EyeBlinkLookUpLeft', 'eyeLookUpL', 'eyeBlinkL')
    eyeBlinkConnect('EyeBlinkSquintLeft', 'eyeSquintInnerL', 'eyeBlinkL')
    eyeBlinkConnect('EyeBlinkCheekSquintLeft', 'eyeCheekRaiseL', 'eyeBlinkL')

    eyeBlinkConnect('EyeBlinkLookDownRight', 'eyeLookDownR', 'eyeBlinkR')
    eyeBlinkConnect('EyeBlinkLookInRight', 'eyeLookLeftR', 'eyeBlinkR')
    eyeBlinkConnect('EyeBlinkLookOutRight', 'eyeLookRightR', 'eyeBlinkR')
    eyeBlinkConnect('EyeBlinkLookUpRight', 'eyeLookUpR', 'eyeBlinkR')
    eyeBlinkConnect('EyeBlinkSquintRight', 'eyeSquintInnerR', 'eyeBlinkR')
    eyeBlinkConnect('EyeBlinkCheekSquintRight', 'eyeCheekRaiseR', 'eyeBlinkR')

def jawConnect():
    connectExp('CTRL_C_jaw_fwdBack', 'ty', 'CTRL_expressions_jawFwd')
    connectExp('CTRL_C_jaw_fwdBack', 'ty', 'CTRL_expressions_jawBack')

    myMult = cmds.createNode('multiplyDivide', n='jaw_mult')
    cmds.setAttr(myMult+'.input2X', -1)
    cmds.connectAttr ( newCon('CTRL_C_jaw_fwdBack')+'.ty', myMult+'.input1X', f=True )
    cmds.connectAttr ( myMult+'.outputX', 'BS_ARKit.JawForward', f=True )

    connectExpToTarget('CTRL_C_jaw', 'tx', 'CTRL_expressions_jawLeft', 'JawLeft')
    connectExpToTarget('CTRL_C_jaw', 'tx', 'CTRL_expressions_jawRight', 'JawRight')
    connectExpToTarget('CTRL_C_jaw', 'ty', 'CTRL_expressions_jawOpen', 'JawOpen')

def mouthConnect():
    myList = ['UL','UR','DL','DR']
    # mouthFunnel
    cmds.connectAttr ( newCon('CTRL_C_mouth_funnelD')+'.ty', 'BS_ARKit.MouthFunnel', f=True )

    # MouthPucker - mouthFunnel
    myMult = cmds.createNode('multiplyDivide', n='mouthFunnel_mult')
    cmds.setAttr(myMult+'.input2X', 0.75)
    cmds.connectAttr ( newCon('CTRL_C_mouth_purseD')+'.ty', myMult+'.input1X', f=True )

    myPlus = cmds.createNode('plusMinusAverage', n='mouthFunnel_plus')
    cmds.connectAttr ( myMult+'.outputX', myPlus+'.input1D[0]', f=True )
    cmds.connectAttr ( newCon('CTRL_C_mouth_funnelD')+'.ty', myPlus+'.input1D[1]', f=True )

    myClamp = cmds.createNode('clamp', n='mouthFunnel_clamp')
    cmds.setAttr(myClamp+'.maxR', 1)
    cmds.connectAttr ( myPlus+'.output1D', myClamp+'.inputR', f=True )

    for i in myList:
        cmds.connectAttr (myClamp+'.outputR', newCon('CTRL_expressions')+'.mouthFunnel'+i, f=True)
        cmds.connectAttr ( myClamp+'.outputR', 'CTRL_expressions_mouthFunnel'+i+'.input', f=True )

    # MouthPucker -mouthPurse
    for i in myList:
        connectExp('CTRL_C_mouth_purseD', 'ty', 'CTRL_expressions_mouthLipsPurse'+i)

    # MouthPucker - mouthTowards
    myMult = cmds.createNode('multiplyDivide', n='mouthTowards_mult')
    cmds.setAttr(myMult+'.input2X', 0.41)
    cmds.connectAttr ( newCon('CTRL_C_mouth_purseD')+'.ty', myMult+'.input1X', f=True )

    for i in myList:
        cmds.connectAttr ( myMult+'.outputX', 'CTRL_expressions.mouthLipsTowards'+i, f=True )
        cmds.connectAttr ( myMult+'.outputX', newCon('CTRL_expressions')+'.mouthLipsTowards'+i, f=True )

    cmds.connectAttr ( newCon('CTRL_C_mouth_purseD')+'.ty', 'BS_ARKit.MouthPucker', f=True )

    # Mouth etc
    connectExpToTarget('CTRL_C_mouth', 'ty', 'CTRL_expressions_mouthLeft', 'MouthLeft')
    connectExpToTarget('CTRL_C_mouth', 'ty', 'CTRL_expressions_mouthRight', 'MouthRight')
    connectExpToTarget('CTRL_L_mouth_cornerPull', 'ty', 'CTRL_expressions_mouthCornerPullL', 'MouthSmileLeft')
    connectExpToTarget('CTRL_R_mouth_cornerPull', 'ty', 'CTRL_expressions_mouthCornerPullR', 'MouthSmileRight')
    connectExpToTarget('CTRL_L_mouth_cornerDepress', 'ty', 'CTRL_expressions_mouthCornerDepressL', 'MouthFrownLeft')
    connectExpToTarget('CTRL_R_mouth_cornerDepress', 'ty', 'CTRL_expressions_mouthCornerDepressR', 'MouthFrownRight')
    connectExpToTarget('CTRL_L_mouth_dimple', 'ty', 'CTRL_expressions_mouthDimpleL', 'MouthDimpleLeft')
    connectExpToTarget('CTRL_R_mouth_dimple', 'ty', 'CTRL_expressions_mouthDimpleR', 'MouthDimpleRight')
    connectExpToTarget('CTRL_L_mouth_stretch', 'ty', 'CTRL_expressions_mouthStretchL', 'MouthStretchLeft')
    connectExpToTarget('CTRL_R_mouth_stretch', 'ty', 'CTRL_expressions_mouthStretchR', 'MouthStretchRight')

    # MouthRollUpper
    myMult = cmds.createNode('multiplyDivide', n='MouthRollLower_mult')
    cmds.setAttr(myMult+'.input2X', 0.5)
    cmds.connectAttr ( newCon('CTRL_C_mouth_lipsRollD')+'.ty', myMult+'.input1X', f=True )

    myCond = cmds.createNode('condition', n='MouthRollLower_cond')
    cmds.setAttr(myCond+'.operation', 1)
    cmds.connectAttr ( myMult+'.outputX', myCond+'.firstTerm', f=True )
    cmds.connectAttr ( myMult+'.outputX', myCond+'.colorIfTrueR', f=True )
    cmds.connectAttr ( newCon('CTRL_C_mouth_lipsRollU')+'.ty', myCond+'.colorIfFalseR', f=True )

    cmds.connectAttr ( myCond+'.outColorR', 'CTRL_expressions_mouthUpperLipRollInR.input', f=True )
    cmds.connectAttr ( myCond+'.outColorR', 'CTRL_expressions_mouthUpperLipRollOutR.input', f=True )
    cmds.connectAttr ( myCond+'.outColorR', 'CTRL_expressions_mouthUpperLipRollInL.input', f=True )
    cmds.connectAttr ( myCond+'.outColorR', 'CTRL_expressions_mouthUpperLipRollOutL.input', f=True )

    cmds.connectAttr ( newCon('CTRL_C_mouth_lipsRollU')+'.ty', 'BS_ARKit.MouthRollUpper', f=True )

    # MouthRollLower
    connectExp('CTRL_C_mouth_lipsRollD', 'ty', 'CTRL_expressions_mouthLowerLipRollOutR')
    connectExp('CTRL_C_mouth_lipsRollD', 'ty', 'CTRL_expressions_mouthLowerLipRollInR')
    connectExp('CTRL_C_mouth_lipsRollD', 'ty', 'CTRL_expressions_mouthLowerLipRollOutL')
    connectExp('CTRL_C_mouth_lipsRollD', 'ty', 'CTRL_expressions_mouthLowerLipRollInL')

    cmds.connectAttr ( newCon('CTRL_C_mouth_lipsRollD')+'.ty', 'BS_ARKit.MouthRollLower', f=True )

    # MouthShrugLower
    connectExp('CTRL_C_jaw_ChinRaiseD', 'ty', 'CTRL_expressions_jawChinRaiseDL')
    connectExp('CTRL_C_jaw_ChinRaiseD', 'ty', 'CTRL_expressions_jawChinRaiseDR')
    cmds.connectAttr ( 'CTRL_C_jaw_ChinRaiseD'+'.ty', 'BS_ARKit.MouthShrugLower', f=True )

    # MouthShrugUpper
    connectExp('CTRL_C_jaw_ChinRaiseU', 'ty', 'CTRL_expressions_jawChinRaiseUL')
    connectExp('CTRL_C_jaw_ChinRaiseU', 'ty', 'CTRL_expressions_jawChinRaiseUR')
    cmds.connectAttr ( 'CTRL_C_jaw_ChinRaiseU'+'.ty', 'BS_ARKit.MouthShrugUpper', f=True )

    # MouthPressLeft
    connectExp('CTRL_L_mouth_press', 'ty', 'CTRL_expressions_mouthPressUL')
    connectExp('CTRL_L_mouth_press', 'ty', 'CTRL_expressions_mouthPressDL')
    cmds.connectAttr ( 'CTRL_L_mouth_press'+'.ty', 'BS_ARKit.MouthPressLeft', f=True )

    # MouthPressRight
    connectExp('CTRL_R_mouth_press', 'ty', 'CTRL_expressions_mouthPressUR')
    connectExp('CTRL_R_mouth_press', 'ty', 'CTRL_expressions_mouthPressDR')
    cmds.connectAttr ( 'CTRL_R_mouth_press'+'.ty', 'BS_ARKit.MouthPressRight', f=True )

    # MouthLowerDownLeft, MouthLowerDownRight
    connectExpToTarget('CTRL_L_mouth_lowerLipDepress', 'ty', 'CTRL_expressions_mouthLowerLipDepressL', 'MouthLowerDownLeft')
    connectExpToTarget('CTRL_R_mouth_lowerLipDepress', 'ty', 'CTRL_expressions_mouthLowerLipDepressR', 'MouthLowerDownRight')

    # MouthUpperUpLeft, MouthUpperUpRight
    connectExpToTarget('CTRL_L_mouth_upperLipRaise', 'ty', 'CTRL_expressions_mouthUpperLipRaiseL', 'MouthUpperUpLeft')
    connectExpToTarget('CTRL_R_mouth_upperLipRaise', 'ty', 'CTRL_expressions_mouthUpperLipRaiseR', 'MouthUpperUpRight')

    # MouthClose
    myMult = cmds.createNode('multiplyDivide', n='MouthClose_mult')
    cmds.connectAttr ( newCon('CTRL_C_jaw')+'.ty', myMult+'.input1X', f=True )
    cmds.connectAttr ( 'CTRL_C_mouth_close.ty', myMult+'.input2X', f=True )

    myCond = cmds.createNode('condition', n='MouthClose_cond')
    cmds.setAttr(myCond+'.operation', 1)
    cmds.setAttr(myCond+'.colorIfFalseR', 0)
    cmds.connectAttr ( newCon('CTRL_C_jaw')+'.ty', myCond+'.firstTerm', f=True )
    cmds.connectAttr ( myMult+'.outputX', myCond+'.colorIfTrueR', f=True )
    cmds.connectAttr ( myCond+'.outColorR', 'BS_ARKit.MouthClose', f=True )

    # cmds.connectAttr ( 'CTRL_C_mouth_close.ty', 'CTRL_expressions_mouthLipsTogetherUL.input', f=True )
    # cmds.connectAttr ( 'CTRL_C_mouth_close.ty', 'CTRL_expressions_mouthLipsTogetherUR.input', f=True )
    # cmds.connectAttr ( 'CTRL_C_mouth_close.ty', 'CTRL_expressions_mouthLipsTogetherDL.input', f=True )
    # cmds.connectAttr ( 'CTRL_C_mouth_close.ty', 'CTRL_expressions_mouthLipsTogetherDR.input', f=True )
    connectExp('CTRL_C_mouth_close', 'ty', 'CTRL_expressions_mouthLipsTogetherUL')
    connectExp('CTRL_C_mouth_close', 'ty', 'CTRL_expressions_mouthLipsTogetherUR')
    connectExp('CTRL_C_mouth_close', 'ty', 'CTRL_expressions_mouthLipsTogetherDL')
    connectExp('CTRL_C_mouth_close', 'ty', 'CTRL_expressions_mouthLipsTogetherDR')

def browConnect():
    # BrowDownLeft, BrowDownRight
    connectExpToTarget('CTRL_L_brow_down', 'ty', 'CTRL_expressions_browDownL', 'BrowDownLeft')
    connectExpToTarget('CTRL_R_brow_down', 'ty', 'CTRL_expressions_browDownR', 'BrowDownRight')

    # browRaiseInL
    myPlus = cmds.createNode('plusMinusAverage', n='browRaiseInL_plus')
    cmds.connectAttr ( 'CTRL_C_brow_raiseIn.ty', myPlus+'.input1D[0]', f=True )
    cmds.connectAttr ( newCon('CTRL_L_brow_raiseOut')+'.ty', myPlus+'.input1D[1]', f=True )

    myClamp = cmds.createNode('clamp', n='browRaiseInL_clamp')
    cmds.setAttr(myClamp+'.maxR', 1)
    cmds.connectAttr ( myPlus+'.output1D', myClamp+'.inputR', f=True )

    cmds.connectAttr ( myClamp+'.outputR', 'CTRL_expressions_browRaiseInL.input', f=True )
    cmds.connectAttr ( myClamp+'.outputR', newCon('CTRL_expressions')+'.browRaiseInL', f=True )

    # browRaiseInR
    myPlus = cmds.createNode('plusMinusAverage', n='browRaiseInR_plus')
    cmds.connectAttr ( 'CTRL_C_brow_raiseIn.ty', myPlus+'.input1D[0]', f=True )
    cmds.connectAttr ( newCon('CTRL_R_brow_raiseOut')+'.ty', myPlus+'.input1D[1]', f=True )

    myClamp = cmds.createNode('clamp', n='browRaiseInR_clamp')
    cmds.setAttr(myClamp+'.maxR', 1)
    cmds.connectAttr ( myPlus+'.output1D', myClamp+'.inputR', f=True )

    cmds.connectAttr ( myClamp+'.outputR', 'CTRL_expressions_browRaiseInR.input', f=True )
    cmds.connectAttr ( myClamp+'.outputR', newCon('CTRL_expressions')+'.browRaiseInR', f=True )

    # BrowInnerUp
    connectExp('CTRL_C_brow_raiseIn', 'ty', 'CTRL_expressions_browLateralL')
    connectExp('CTRL_C_brow_raiseIn', 'ty', 'CTRL_expressions_browLateralR')

    cmds.connectAttr ( 'CTRL_C_brow_raiseIn.ty', 'BS_ARKit.BrowInnerUp', f=True )

    # BrowOuterUpLeft
    connectExp('CTRL_L_brow_raiseOut', 'ty', 'CTRL_expressions_browRaiseOuterL')
    cmds.connectAttr ( newCon('CTRL_L_brow_raiseOut')+'.ty', 'BS_ARKit.BrowOuterUpLeft', f=True )

    # BrowOuterUpRight
    connectExp('CTRL_R_brow_raiseOut', 'ty', 'CTRL_expressions_browRaiseOuterR')
    cmds.connectAttr ( newCon('CTRL_R_brow_raiseOut')+'.ty', 'BS_ARKit.BrowOuterUpRight', f=True )

def cheekConnect():
    connectExp('CTRL_C_mouth_suckBlow', 'ty', 'CTRL_expressions_mouthCheekSuckL')
    connectExp('CTRL_C_mouth_suckBlow', 'ty', 'CTRL_expressions_mouthCheekSuckR')
    connectExp('CTRL_C_mouth_suckBlow', 'ty', 'CTRL_expressions_mouthCheekBlowL')
    connectExp('CTRL_C_mouth_suckBlow', 'ty', 'CTRL_expressions_mouthCheekBlowR')
    connectExp('CTRL_C_mouth_suckBlow', 'ty', 'CTRL_expressions_mouthLipsBlowL')
    connectExp('CTRL_C_mouth_suckBlow', 'ty', 'CTRL_expressions_mouthLipsBlowR')
    cmds.connectAttr ( 'CTRL_C_mouth_suckBlow.ty', 'BS_ARKit.CheekPuff', f=True )

def noseConnect():
    connectExp('CTRL_L_nose', 'ty', 'CTRL_expressions_noseWrinkleL')
    connectExp('CTRL_L_nose', 'ty', 'CTRL_expressions_noseNostrilDilateL')
    cmds.connectAttr ( newCon('CTRL_L_nose')+'.ty', 'BS_ARKit.NoseSneerLeft', f=True )

    connectExp('CTRL_R_nose', 'ty', 'CTRL_expressions_noseWrinkleR')
    connectExp('CTRL_R_nose', 'ty', 'CTRL_expressions_noseNostrilDilateR')
    cmds.connectAttr ( newCon('CTRL_R_nose')+'.ty', 'BS_ARKit.NoseSneerRight', f=True )

def tongueConnect():
    connectExp(newCon('CTRL_C_tongue_inOut'), 'ty', 'CTRL_expressions_tongueIn')
    connectExp(newCon('CTRL_C_tongue_inOut'), 'ty', 'CTRL_expressions_tongueOut')

    connectExp(newCon('CTRL_C_tongue_narrowWide'), 'ty', 'CTRL_expressions_tongueNarrow')
    connectExp(newCon('CTRL_C_tongue_narrowWide'), 'ty', 'CTRL_expressions_tongueWide')

    connectExp(newCon('CTRL_C_tongue_press'), 'ty', 'CTRL_expressions_tonguePress')

    connectExp(newCon('CTRL_C_tongue_roll'), 'ty', 'CTRL_expressions_tongueRollUp')
    connectExp(newCon('CTRL_C_tongue_roll'), 'ty', 'CTRL_expressions_tongueRollDown')
    connectExp(newCon('CTRL_C_tongue_roll'), 'tx', 'CTRL_expressions_tongueRollLeft')
    connectExp(newCon('CTRL_C_tongue_roll'), 'tx', 'CTRL_expressions_tongueRollRight')

    connectExp(newCon('CTRL_C_tongue_tip'), 'ty', 'CTRL_expressions_tongueTipUp')
    connectExp(newCon('CTRL_C_tongue_tip'), 'ty', 'CTRL_expressions_tongueTipDown')
    connectExp(newCon('CTRL_C_tongue_tip'), 'tx', 'CTRL_expressions_tongueTipLeft')
    connectExp(newCon('CTRL_C_tongue_tip'), 'tx', 'CTRL_expressions_tongueTipRight')

    connectExp(newCon('CTRL_C_tongue'), 'ty', 'CTRL_expressions_tongueUp')
    connectExp(newCon('CTRL_C_tongue'), 'ty', 'CTRL_expressions_tongueDown')
    connectExp(newCon('CTRL_C_tongue'), 'tx', 'CTRL_expressions_tongueLeft')
    connectExp(newCon('CTRL_C_tongue'), 'tx', 'CTRL_expressions_tongueRight')

def multipliersConnect():
    mySide = ['L','R']
    for i in mySide:
        # CTRL_C_brow_raiseIn
        # CTRL_L_nose, CTRL_R_nose
        myBrowLateralPlus = cmds.createNode ( 'plusMinusAverage', n='browLateral%s_plus'%i )
        myBrowLateralClamp = cmds.createNode ( 'clamp', n='browLateral%s_clamp'%i )
        cmds.setAttr ( myBrowLateralClamp+'.maxR', 1 )

        cmds.connectAttr ( newCon('CTRL_expressions')+'.browLateral%s'%i, myBrowLateralPlus+'.input1D[0]', f=True )
        cmds.connectAttr ( myBrowLateralPlus+'.output1D', myBrowLateralClamp+'.inputR', f=True )
        cmds.connectAttr ( myBrowLateralClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_browsLateral_'+i, f=True ) #04, #06
        cmds.connectAttr ( myBrowLateralClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_browsLateral_'+i, f=True ) #05, #07

        myMult = cmds.createNode( 'multiplyDivide', n='noseBrowLateral%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.3 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.noseWrinkle'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myBrowLateralPlus+'.input1D[1]', f=True ) #04 #05, #06 #07

        cmds.connectAttr( newCon('CTRL_expressions')+'.browRaiseIn'+i, newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_browsRaiseInner_'+i, f=True ) #08 #10
        cmds.connectAttr( newCon('CTRL_expressions')+'.browRaiseIn'+i, newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_browsRaiseInner_'+i, f=True ) #09 #11

        # CTRL_L_brow_down, CTRL_R_brow_down
        # CTRL_L_nose, CTRL_R_nose
        myBrowDownPlus = cmds.createNode ( 'plusMinusAverage', n='browDown%s_plus'%i )
        myBrowDownClamp = cmds.createNode ( 'clamp', n='browDown%s_clamp'%i )
        cmds.setAttr ( myBrowDownClamp+'.maxR', 1 )

        cmds.connectAttr ( newCon('CTRL_expressions')+'.browDown%s'%i, myBrowDownPlus+'.input1D[0]', f=True ) #08 #10, #09 #11
        cmds.connectAttr ( myBrowDownPlus+'.output1D', myBrowDownClamp+'.inputR', f=True )
        cmds.connectAttr ( myBrowDownClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_browsDown_'+i, f=True ) #00, #02
        cmds.connectAttr ( myBrowDownClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_browsDown_'+i, f=True ) #01, #03

        myMult = cmds.createNode( 'multiplyDivide', n='noseBrowDown%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.2 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.noseWrinkle'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myBrowDownPlus+'.input1D[1]', f=True ) #08 #09, #10 #11

        cmds.connectAttr ( newCon('CTRL_expressions')+'.noseWrinkle'+i, newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_noseWrinkler_'+i, f=True ) #36, #38
        cmds.connectAttr ( newCon('CTRL_expressions')+'.noseWrinkle'+i, newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_noseWrinkler_'+i, f=True ) #37, #39

        # CTRL_L_brow_raiseOut, CTRL_R_brow_raiseOut
        cmds.connectAttr( newCon('CTRL_expressions')+'.browRaiseOuter'+i, newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_browsRaiseOuter_'+i, f=True ) #12, #14
        cmds.connectAttr( newCon('CTRL_expressions')+'.browRaiseOuter'+i, newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_browsRaiseOuter_'+i, f=True ) #13, #15

        # CTRL_L_eye_blink, CTRL_R_eye_blink
        # CTRL_L_eye_squintInner, CTRL_R_eye_squintInner
        # CTRL_L_eye_cheekRaise, CTRL_R_eye_cheekRaise
        # CTRL_L_mouth_cornerPull, CTRL_R_mouth_cornerPull
        # CTRL_L_mouth_dimple, CTRL_R_mouth_dimple
        # CTRL_L_eye, CTRL_R_eye
        # blink
        myBlinkPlus = cmds.createNode ( 'plusMinusAverage', n='blink%s_plus'%i )
        myBlinkClamp = cmds.createNode ( 'clamp', n='blink%s_clamp'%i )
        cmds.setAttr ( myBlinkClamp+'.maxR', 1 )

        cmds.connectAttr ( myBlinkPlus+'.output1D', myBlinkClamp+'.inputR', f=True )
        cmds.connectAttr ( myBlinkClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_blink_'+i, f=True ) #16, #20
        cmds.connectAttr ( myBlinkClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_blink_'+i, f=True ) #18, #22
        # squintInner
        mySquintInnerPlus = cmds.createNode ( 'plusMinusAverage', n='squintInner%s_plus'%i )
        mySquintInnerClamp = cmds.createNode ( 'clamp', n='squintInner%s_clamp'%i )
        cmds.setAttr ( mySquintInnerClamp+'.maxR', 1 )

        cmds.connectAttr ( mySquintInnerPlus+'.output1D', mySquintInnerClamp+'.inputR', f=True )
        cmds.connectAttr ( mySquintInnerClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_squintInner_'+i, f=True ) #17 #21
        cmds.connectAttr ( mySquintInnerClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_squintInner_'+i, f=True ) #19 #23
        # cheekRaiseInner
        myCheekRaiseInnerPlus = cmds.createNode ( 'plusMinusAverage', n='cheekRaiseInner%s_plus'%i )
        myCheekRaiseInnerClamp = cmds.createNode ( 'clamp', n='cheekRaiseInner%s_clamp'%i )
        cmds.setAttr ( myCheekRaiseInnerClamp+'.maxR', 1 )

        cmds.connectAttr ( myCheekRaiseInnerPlus+'.output1D', myCheekRaiseInnerClamp+'.inputR', f=True )
        cmds.connectAttr ( myCheekRaiseInnerClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseInner_'+i, f=True ) #24 #30
        cmds.connectAttr ( myCheekRaiseInnerClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseInner_'+i, f=True ) #27 #33
        # cheekRaiseOuter
        myCheekRaiseOuterPlus = cmds.createNode ( 'plusMinusAverage', n='cheekRaiseOuter%s_plus'%i )
        myCheekRaiseOuterClamp = cmds.createNode ( 'clamp', n='cheekRaiseOuter%s_clamp'%i )
        cmds.setAttr ( myCheekRaiseOuterClamp+'.maxR', 1 )

        cmds.connectAttr ( myCheekRaiseOuterPlus+'.output1D', myCheekRaiseOuterClamp+'.inputR', f=True )
        cmds.connectAttr ( myCheekRaiseOuterClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseOuter_'+i, f=True ) #25 #31
        cmds.connectAttr ( myCheekRaiseOuterClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseOuter_'+i, f=True ) #28 #34
        # smile
        mySmilePlus = cmds.createNode ( 'plusMinusAverage', n='smile%s_plus'%i )
        mySmileClamp = cmds.createNode ( 'clamp', n='smile%s_clamp'%i )
        cmds.setAttr ( mySmileClamp+'.maxR', 1 )

        cmds.connectAttr ( mySmilePlus+'.output1D', mySmileClamp+'.inputR', f=True )
        cmds.connectAttr ( mySmileClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_smile_'+i, f=True ) #40 #50
        cmds.connectAttr ( mySmileClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_smile_'+i, f=True ) #41 #51
        # lips
        myLipsPlus = cmds.createNode ( 'plusMinusAverage', n='lips%s_plus'%i )
        myLipsClamp = cmds.createNode ( 'clamp', n='lips%s_clamp'%i )
        cmds.setAttr ( myLipsClamp+'.maxR', 1 )

        cmds.connectAttr ( myLipsPlus+'.output1D', myLipsClamp+'.inputR', f=True )
        cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm13_lips_U'+i, f=True ) #52, #56
        cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm13_lips_D'+i, f=True ) #53, #57
        cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm13_lips_U'+i, f=True ) #54, #58
        cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm13_lips_D'+i, f=True ) #55, #59

        # eyeLookDown
        myMult = cmds.createNode( 'multiplyDivide', n='eyeLookDown%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 1.0 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.eyeLookDown'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myBlinkPlus+'.input1D[0]', f=True ) #16 #18, #20 #22
        # eyeBlink
        myMult = cmds.createNode( 'multiplyDivide', n='eyeBlink%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.3 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.eyeBlink'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', mySquintInnerPlus+'.input1D[0]', f=True ) #17 #19, #21 #23
        # eyeSquintInner
        myMult = cmds.createNode( 'multiplyDivide', n='eyeSquintInner%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.8 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.eyeSquintInner'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', mySquintInnerPlus+'.input1D[1]', f=True ) #17 #19, #21 #23
        # eyeCheekRaise
        myMult = cmds.createNode( 'multiplyDivide', n='eyeCheekRaise%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.8 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.eyeCheekRaise'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myCheekRaiseInnerPlus+'.input1D[0]', f=True ) #24 #27, #30 #33
        cmds.connectAttr ( myCheekRaiseInnerPlus+'.output1D', myCheekRaiseInnerClamp+'.inputR', f=True )
        cmds.connectAttr ( myMult+'.outputX', myCheekRaiseOuterPlus+'.input1D[0]', f=True ) #25 #28, #31 #34
        cmds.connectAttr ( myMult+'.outputX', newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseUpper_'+i, f=True ) #26 #32
        cmds.connectAttr ( myMult+'.outputX', newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseUpper_'+i, f=True ) #29 #35
        # mouthCornerPull
        myMult = cmds.createNode( 'multiplyDivide', n='mouthCornerPull_0.8_%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.8 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthCornerPull'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myCheekRaiseInnerPlus+'.input1D[1]', f=True ) #24 #27, #30 #33
        cmds.connectAttr ( myMult+'.outputX', myCheekRaiseOuterPlus+'.input1D[1]', f=True ) #25 #28, #31 #34
        ## mouthCornerPull
        myMult = cmds.createNode( 'multiplyDivide', n='mouthCornerPull_1.0_%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 1.0 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthCornerPull'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', mySmilePlus+'.input1D[0]', f=True ) #40 #41, #50 #51
        cmds.connectAttr ( myMult+'.outputX', myLipsPlus+'.input1D[0]', f=True ) #52 #53 #54 #55, #56 #57 #58 #59
        # mouthDimple
        myMult = cmds.createNode( 'multiplyDivide', n='mouthDimple_0.4_%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.4 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthDimple'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', mySmilePlus+'.input1D[1]', f=True ) #40 #41, #50 #51
        # mouthDimple
        myMult = cmds.createNode( 'multiplyDivide', n='mouthDimple_0.5_%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.5 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthDimple'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myLipsPlus+'.input1D[1]', f=True ) #52 #53 #54 #55, #56 #57 #58 #59
        # mouthStretch
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthStretch'+i, myLipsPlus+'.input1D[2]', f=True ) #52 #53 #54 #55, #56 #57 #58 #59
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthStretch'+i, newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_mouthStretch_'+i, f=True ) #60, #62
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthStretch'+i, newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_mouthStretch_'+i, f=True ) #61, #63

        # mouthLeft, mouthRight
        if i == 'L':
            # lips
            myLipsPlus = cmds.createNode ( 'plusMinusAverage', n='lips_plus' )
            myLipsClamp = cmds.createNode ( 'clamp', n='lips_clamp' )
            cmds.setAttr ( myLipsClamp+'.maxR', 1 )

            cmds.connectAttr ( myLipsPlus+'.output1D', myLipsClamp+'.inputR', f=True )
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_UL', f=True ) #42
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_UR', f=True ) #43
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_DL', f=True ) #44
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_DR', f=True ) #45
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_UL', f=True ) #46
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_UR', f=True ) #47
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_DL', f=True ) #48
            cmds.connectAttr ( myLipsClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_DR', f=True ) #49

            myMult = cmds.createNode( 'multiplyDivide', n='mouthLeft_0.5_mult' )
            cmds.setAttr ( myMult+'.input2X', 0.5 )
            cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLeft', myMult+'.input1X', f=True )
            cmds.connectAttr ( myMult+'.outputX', myCheekRaiseInnerPlus+'.input1D[4]', f=True ) #24 #27
            cmds.connectAttr ( myMult+'.outputX', myCheekRaiseOuterPlus+'.input1D[2]', f=True ) #25 #28
            cmds.connectAttr ( myMult+'.outputX', myLipsPlus+'.input1D[0]', f=True ) #42 #43 #44 #45 #46 #47 #48 #49
            #
            myMult = cmds.createNode( 'multiplyDivide', n='mouthLeft_1.0_mult' )
            cmds.setAttr ( myMult+'.input2X', 1.0 )
            cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLeft', myMult+'.input1X', f=True )
            cmds.connectAttr ( myMult+'.outputX', mySmilePlus+'.input1D[2]', f=True ) #40 #41
        else:
            myMult = cmds.createNode( 'multiplyDivide', n='mouthRight_0.5_mult' )
            cmds.setAttr ( myMult+'.input2X', 0.5 )
            cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthRight', myMult+'.input1X', f=True )
            cmds.connectAttr ( myMult+'.outputX', myCheekRaiseInnerPlus+'.input1D[4]', f=True ) #30 #33
            cmds.connectAttr ( myMult+'.outputX', myCheekRaiseOuterPlus+'.input1D[2]', f=True ) #31 #34
            myLipsPlus = 'lips_plus'
            cmds.connectAttr ( myMult+'.outputX', myLipsPlus+'.input1D[1]', f=True ) #42 #43 #44 #45 #46 #47 #48 #49
            #
            myMult = cmds.createNode( 'multiplyDivide', n='mouthPucker_0.625_mult' )
            cmds.setAttr ( myMult+'.input2X', 0.625 )
            cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLipsPurseU'+i, myMult+'.input1X', f=True )
            myLipsPlus = 'lips_plus'
            cmds.connectAttr ( myMult+'.outputX', myLipsPlus+'.input1D[2]', f=True ) #42 #43 #44 #45 #46 #47 #48 #49
            #
            myMult = cmds.createNode( 'multiplyDivide', n='mouthRight_1.0_mult' )
            cmds.setAttr ( myMult+'.input2X', 1.0 )
            cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthRight', myMult+'.input1X', f=True )
            cmds.connectAttr ( myMult+'.outputX', mySmilePlus+'.input1D[2]', f=True ) #50 #51

        # CTRL_C_jaw_ChinRaiseD
        # chinRaise
        myChinRaisePlus = cmds.createNode ( 'plusMinusAverage', n='chinRaise%s_plus'%i )
        myChinRaiseClamp = cmds.createNode ( 'clamp', n='chinRaise%s_clamp'%i )
        cmds.setAttr ( myChinRaiseClamp+'.maxR', 1 )

        cmds.connectAttr ( myChinRaisePlus+'.output1D', myChinRaiseClamp+'.inputR', f=True )
        cmds.connectAttr ( myChinRaiseClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_chinRaise_'+i, f=True ) #72, #74
        cmds.connectAttr ( myChinRaiseClamp+'.outputR', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_chinRaise_'+i, f=True ) #73, #75
        # jawChinRaiseD
        myMult = cmds.createNode( 'multiplyDivide', n='jawChinRaiseD%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 1.0 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.jawChinRaiseD'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myChinRaisePlus+'.input1D[0]', f=True ) #72 #73, #74 #75

        # CTRL_C_mouth_close
        # mouthLipsTogetherU
        myMult = cmds.createNode( 'multiplyDivide', n='mouthLipsTogetherU%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.25 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLipsTogetherU'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myChinRaisePlus+'.input1D[1]', f=True ) #72 #73, #74 #75
        # mouthLipsTogetherD
        myMult = cmds.createNode( 'multiplyDivide', n='mouthLipsTogetherD%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.25 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLipsTogetherD'+i, myMult+'.input1X', f=True )
        cmds.connectAttr ( myMult+'.outputX', myChinRaisePlus+'.input1D[2]', f=True ) #72 #73, #74 #75

        # CTRL_C_mouth_purseD
        # mouthLipsPurseU
        myMult = cmds.createNode( 'multiplyDivide', n='mouthLipsPurseU%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.528 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLipsPurseU'+i, myMult+'.input1X', f=True )
        cmds.connectAttr( myMult+'.outputX', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_purse_U'+i, f=True ) #64 #66
        cmds.connectAttr( myMult+'.outputX', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_purse_U'+i, f=True ) #65 #67
        # mouthLipsPurseD
        myMult = cmds.createNode( 'multiplyDivide', n='mouthLipsPurseD%s_mult'%i )
        cmds.setAttr ( myMult+'.input2X', 0.528 )
        cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLipsPurseD'+i, myMult+'.input1X', f=True )
        cmds.connectAttr( myMult+'.outputX', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_purse_D'+i, f=True ) #68 #70
        cmds.connectAttr( myMult+'.outputX', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_purse_D'+i, f=True ) #69 #71
        # #
        # myMult = cmds.createNode( 'multiplyDivide', n='mouthPucker_0.625_mult' )
        # cmds.setAttr ( myMult+'.input2X', 0.625 )
        # cmds.connectAttr ( newCon('CTRL_expressions')+'.mouthLipsPurseU'+i, myMult+'.input1X', f=True )
        # myLipsPlus = 'lips_plus'
        # cmds.connectAttr ( myMult+'.outputX', myLipsPlus+'.input1D[2]', f=True ) #42 #43 #44 #45 #46 #47 #48 #49

    # center
    # CTRL_C_jaw
    cmds.connectAttr( newCon('CTRL_expressions')+'.jawOpen', newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_jawOpen', f=True ) #76
    cmds.connectAttr( newCon('CTRL_expressions')+'.jawOpen', newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_jawOpen', f=True ) #77

def headShaderConnect():
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_browsDown_L', 'shader_head_shader.maskWeight_00', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_browsDown_L', 'shader_head_shader.maskWeight_01', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_browsDown_R', 'shader_head_shader.maskWeight_02', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_browsDown_R', 'shader_head_shader.maskWeight_03', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_browsLateral_L', 'shader_head_shader.maskWeight_04', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_browsLateral_L', 'shader_head_shader.maskWeight_05', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_browsLateral_R', 'shader_head_shader.maskWeight_06', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_browsLateral_R', 'shader_head_shader.maskWeight_07', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_browsRaiseInner_L', 'shader_head_shader.maskWeight_08', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_browsRaiseInner_L', 'shader_head_shader.maskWeight_09', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_browsRaiseInner_R', 'shader_head_shader.maskWeight_10', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_browsRaiseInner_R', 'shader_head_shader.maskWeight_11', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_browsRaiseOuter_L', 'shader_head_shader.maskWeight_12', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_browsRaiseOuter_L', 'shader_head_shader.maskWeight_13', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_browsRaiseOuter_R', 'shader_head_shader.maskWeight_14', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_browsRaiseOuter_R', 'shader_head_shader.maskWeight_15', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_blink_L', 'shader_head_shader.maskWeight_16', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_squintInner_L', 'shader_head_shader.maskWeight_17', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_blink_L', 'shader_head_shader.maskWeight_18', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_squintInner_L', 'shader_head_shader.maskWeight_19', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_blink_R', 'shader_head_shader.maskWeight_20', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_squintInner_R', 'shader_head_shader.maskWeight_21', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_blink_R', 'shader_head_shader.maskWeight_22', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_squintInner_R', 'shader_head_shader.maskWeight_23', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseInner_L', 'shader_head_shader.maskWeight_24', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseOuter_L', 'shader_head_shader.maskWeight_25', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseUpper_L', 'shader_head_shader.maskWeight_26', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseInner_L', 'shader_head_shader.maskWeight_27', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseOuter_L', 'shader_head_shader.maskWeight_28', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseUpper_L', 'shader_head_shader.maskWeight_29', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseInner_R', 'shader_head_shader.maskWeight_30', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseOuter_R', 'shader_head_shader.maskWeight_31', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_cheekRaiseUpper_R', 'shader_head_shader.maskWeight_32', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseInner_R', 'shader_head_shader.maskWeight_33', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseOuter_R', 'shader_head_shader.maskWeight_34', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_cheekRaiseUpper_R', 'shader_head_shader.maskWeight_35', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_noseWrinkler_L', 'shader_head_shader.maskWeight_36', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_noseWrinkler_L', 'shader_head_shader.maskWeight_37', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_noseWrinkler_R', 'shader_head_shader.maskWeight_38', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_noseWrinkler_R', 'shader_head_shader.maskWeight_39', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_smile_L', 'shader_head_shader.maskWeight_40', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_smile_L', 'shader_head_shader.maskWeight_41', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_UL', 'shader_head_shader.maskWeight_42', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_UR', 'shader_head_shader.maskWeight_43', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_DL', 'shader_head_shader.maskWeight_44', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm13_lips_DR', 'shader_head_shader.maskWeight_45', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_UL', 'shader_head_shader.maskWeight_46', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_UR', 'shader_head_shader.maskWeight_47', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_DL', 'shader_head_shader.maskWeight_48', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm13_lips_DR', 'shader_head_shader.maskWeight_49', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm3_smile_R', 'shader_head_shader.maskWeight_50', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm3_smile_R', 'shader_head_shader.maskWeight_51', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm13_lips_UL', 'shader_head_shader.maskWeight_52', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm13_lips_DL', 'shader_head_shader.maskWeight_53', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm13_lips_UL', 'shader_head_shader.maskWeight_54', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm13_lips_DL', 'shader_head_shader.maskWeight_55', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm13_lips_UR', 'shader_head_shader.maskWeight_56', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm3_color_head_wm13_lips_DR', 'shader_head_shader.maskWeight_57', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm13_lips_UR', 'shader_head_shader.maskWeight_58', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm3_normal_head_wm13_lips_DR', 'shader_head_shader.maskWeight_59', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_mouthStretch_L', 'shader_head_shader.maskWeight_60', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_mouthStretch_L', 'shader_head_shader.maskWeight_61', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_mouthStretch_R', 'shader_head_shader.maskWeight_62', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_mouthStretch_R', 'shader_head_shader.maskWeight_63', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_purse_UL', 'shader_head_shader.maskWeight_64', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_purse_UL', 'shader_head_shader.maskWeight_65', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_purse_UR', 'shader_head_shader.maskWeight_66', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_purse_UR', 'shader_head_shader.maskWeight_67', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_purse_DL', 'shader_head_shader.maskWeight_68', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_purse_DL', 'shader_head_shader.maskWeight_69', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_purse_DR', 'shader_head_shader.maskWeight_70', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_purse_DR', 'shader_head_shader.maskWeight_71', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_chinRaise_L', 'shader_head_shader.maskWeight_72', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_chinRaise_L', 'shader_head_shader.maskWeight_73', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_chinRaise_R', 'shader_head_shader.maskWeight_74', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_chinRaise_R', 'shader_head_shader.maskWeight_75', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm1_color_head_wm1_jawOpen', 'shader_head_shader.maskWeight_76', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm1_normal_head_wm1_jawOpen', 'shader_head_shader.maskWeight_77', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_neckStretch_L', 'shader_head_shader.maskWeight_78', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_neckStretch_L', 'shader_head_shader.maskWeight_79', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_cm2_color_head_wm2_neckStretch_R', 'shader_head_shader.maskWeight_80', f=True )
    cmds.connectAttr ( newCon('FRM_WMmultipliers')+'.head_wm2_normal_head_wm2_neckStretch_R', 'shader_head_shader.maskWeight_81', f=True )

def connectBlendShape2UI():
    eyeConnect()
    jawConnect()
    mouthConnect()
    browConnect()
    cheekConnect()
    noseConnect()
    tongueConnect()
    multipliersConnect()

    if cmds.checkBox('shaderCheck', q=True, v=True ):
        headShaderConnect()
