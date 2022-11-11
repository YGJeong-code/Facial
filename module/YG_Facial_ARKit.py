import maya.cmds as cmds
import maya.mel as mel
import Facial.module.YG_Facial_ARKitDict as ARKitDict
reload(ARKitDict)

# old
def fwdBackKey(myTime, myCon, myPos, myValue):
    cmds.currentTime( myTime-1, edit=True )
    cmds.setKeyframe(myCon, attribute=myPos, v=0)

    cmds.currentTime( myTime, edit=True )
    cmds.setKeyframe(myCon, attribute=myPos, v=myValue)

    cmds.currentTime( myTime+1, edit=True )
    cmds.setKeyframe(myCon, attribute=myPos, v=0)

def fwdKey(myTime, myCon, myPos, myValue):
    cmds.currentTime( myTime-1, edit=True )
    cmds.setKeyframe(myCon, attribute=myPos, v=0)

    cmds.currentTime( myTime, edit=True )
    cmds.setKeyframe(myCon, attribute=myPos, v=myValue)

def backKey(myTime, myCon, myPos, myValue):
    cmds.currentTime( myTime, edit=True )
    cmds.setKeyframe(myCon, attribute=myPos, v=myValue)

    cmds.currentTime( myTime+1, edit=True )
    cmds.setKeyframe(myCon, attribute=myPos, v=0)

def makeKey():
    cmds.currentUnit( time='film' )
    cmds.playbackOptions( e=True, min=0, max=51, aet=51 )

    # 0 Default

    # 1 EyeBlinkLeft
    fwdBackKey(1, 'CTRL_L_eye_blink','ty',1)

    # 2 EyeLookDownLeft
    fwdBackKey(2, 'CTRL_L_eye','ty',-1)

    # 3 EyeLookInLeft
    fwdKey(3, 'CTRL_L_eye','tx',-1)

    # 4 EyeLookOutLeft
    backKey(4, 'CTRL_L_eye','tx',1)

    # 5 EyeLookUpLeft
    fwdBackKey(5, 'CTRL_L_eye','ty',1)

    # 6 EyeSquintLeft
    fwdBackKey(6, 'CTRL_L_eye_squintInner','ty',1)

    # 7 EyeWideLeft
    fwdBackKey(7, 'CTRL_L_eye_blink','ty',-1)

    # 8 EyeBlinkRight
    fwdBackKey(8, 'CTRL_R_eye_blink','ty',1)

    # 9 EyeLookDownRight
    fwdBackKey(9, 'CTRL_R_eye','ty', -1)

    # 10 EyeLookInRight
    fwdKey(10, 'CTRL_R_eye','tx', 1)

    # 11 EyeLookOutRight
    backKey(11, 'CTRL_R_eye','tx', -1)

    # 12 EyeLookUpRight
    fwdBackKey(12, 'CTRL_R_eye','ty', 1)

    # 13 EyeSquintRight
    fwdBackKey(13, 'CTRL_R_eye_squintInner','ty', 1)

    # 14 EyeWideRight
    fwdBackKey(14, 'CTRL_R_eye_blink','ty', -1)

    # 15 JawForward
    fwdBackKey(15, 'CTRL_C_jaw_fwdBack','ty', -1)

    # 16 JawLeft
    fwdKey(16, 'CTRL_C_jaw','tx', -1)

    # 17 JawRight
    backKey(17, 'CTRL_C_jaw','tx', 1)

    # 18 JawOpen
    fwdBackKey(18, 'CTRL_C_jaw','ty', 1)

    # 19 MouthFunnel
    fwdKey(19, 'CTRL_L_mouth_funnelU','ty', 1)
    fwdKey(19, 'CTRL_R_mouth_funnelU','ty', 1)
    fwdKey(19, 'CTRL_L_mouth_funnelD','ty', 1)
    fwdKey(19, 'CTRL_R_mouth_funnelD','ty', 1)

    # 20 MouthPucker
    fwdBackKey(20, 'CTRL_L_mouth_purseU','ty', 1)
    fwdBackKey(20, 'CTRL_R_mouth_purseU','ty', 1)
    fwdBackKey(20, 'CTRL_L_mouth_purseD','ty', 1)
    fwdBackKey(20, 'CTRL_R_mouth_purseD','ty', 1)
    backKey(20, 'CTRL_L_mouth_funnelU','ty', 0.75)
    backKey(20, 'CTRL_R_mouth_funnelU','ty', 0.75)
    backKey(20, 'CTRL_L_mouth_funnelD','ty', 0.75)
    backKey(20, 'CTRL_R_mouth_funnelD','ty', 0.75)
    fwdBackKey(20, 'CTRL_L_mouth_towardsU','ty', 0.41)
    fwdBackKey(20, 'CTRL_R_mouth_towardsU','ty', 0.41)
    fwdBackKey(20, 'CTRL_L_mouth_towardsD','ty', 0.41)
    fwdBackKey(20, 'CTRL_R_mouth_towardsD','ty', 0.41)

    # 21 MouthLeft
    fwdKey(21, 'CTRL_C_mouth','tx', 1)

    # 22 MouthRight
    backKey(22, 'CTRL_C_mouth','tx', -1)

    # 23 MouthSmileLeft
    fwdBackKey(23, 'CTRL_L_mouth_cornerPull','ty', 1)

    # 24 MouthSmileRight
    fwdBackKey(24, 'CTRL_R_mouth_cornerPull','ty', 1)

    # 25 MouthFrownLeft
    fwdBackKey(25, 'CTRL_L_mouth_cornerDepress','ty', 1)

    # 26 MouthFrownRight
    fwdBackKey(26, 'CTRL_R_mouth_cornerDepress','ty', 1)

    # 27 MouthDimpleLeft
    fwdBackKey(27, 'CTRL_L_mouth_dimple','ty', 1)

    # 28 MouthDimpleRight
    fwdBackKey(28, 'CTRL_R_mouth_dimple','ty', 1)

    # 29 MouthStretchLeft
    fwdBackKey(29, 'CTRL_L_mouth_stretch','ty', 1)

    # 30 MouthStretchRight
    fwdBackKey(30, 'CTRL_R_mouth_stretch','ty', 1)

    # 31 MouthRollLower
    fwdKey(31, 'CTRL_L_mouth_lipsRollU','ty', 0.5)
    fwdKey(31, 'CTRL_R_mouth_lipsRollU','ty', 0.5)
    fwdBackKey(31, 'CTRL_L_mouth_lipsRollD','ty', 1)
    fwdBackKey(31, 'CTRL_R_mouth_lipsRollD','ty', 1)

    # 32 MouthRollUpper
    backKey(32, 'CTRL_L_mouth_lipsRollU','ty', 1)
    backKey(32, 'CTRL_R_mouth_lipsRollU','ty', 1)

    # 33 MouthShrugLower
    fwdBackKey(33, 'CTRL_L_jaw_ChinRaiseD','ty', 1)
    fwdBackKey(33, 'CTRL_R_jaw_ChinRaiseD','ty', 1)

    # 34 MouthShrugUpper
    fwdBackKey(34, 'CTRL_L_jaw_ChinRaiseU','ty', 1)
    fwdBackKey(34, 'CTRL_R_jaw_ChinRaiseU','ty', 1)

    # 35 MouthPressLeft
    fwdBackKey(35, 'CTRL_L_mouth_pressU','ty', 1)
    fwdBackKey(35, 'CTRL_L_mouth_pressD','ty', 1)

    # 36 MouthPressRight
    fwdBackKey(36, 'CTRL_R_mouth_pressU','ty', 1)
    fwdBackKey(36, 'CTRL_R_mouth_pressD','ty', 1)

    # 37 MouthLowerDownLeft
    fwdBackKey(37, 'CTRL_L_mouth_lowerLipDepress','ty', 1)

    # 38 MouthLowerDownRight
    fwdBackKey(38, 'CTRL_R_mouth_lowerLipDepress','ty', 1)

    # 39 MouthUpperUpLeft
    fwdBackKey(39, 'CTRL_L_mouth_upperLipRaise','ty', 1)

    # 40 MouthUpperUpRight
    fwdBackKey(40, 'CTRL_R_mouth_upperLipRaise','ty', 1)

    # 41 BrowDownLeft
    fwdBackKey(41, 'CTRL_L_brow_down','ty', 1)

    # 42 BrowDownRight
    fwdBackKey(42, 'CTRL_R_brow_down','ty', 1)

    # 43 BrowInnerUp
    fwdKey(43, 'CTRL_L_brow_raiseIn','ty', 1)
    fwdBackKey(43, 'CTRL_R_brow_raiseIn','ty', 1)
    fwdBackKey(43, 'CTRL_L_brow_lateral','ty', 1)
    fwdBackKey(43, 'CTRL_R_brow_lateral','ty', 1)

    # 44 BrowOuterUpLeft
    backKey(44, 'CTRL_L_brow_raiseIn','ty', 1)
    fwdBackKey(44, 'CTRL_L_brow_raiseOut','ty', 1)

    # 45 BrowOuterUpRight
    fwdBackKey(45, 'CTRL_R_brow_raiseIn','ty', 1)
    fwdBackKey(45, 'CTRL_R_brow_raiseOut','ty', 1)

    # 46 CheekPuff
    fwdBackKey(46, 'CTRL_L_mouth_suckBlow','ty', 1)
    fwdBackKey(46, 'CTRL_R_mouth_suckBlow','ty', 1)
    fwdBackKey(46, 'CTRL_L_mouth_lipsBlow','ty', 1)
    fwdBackKey(46, 'CTRL_R_mouth_lipsBlow','ty', 1)

    # 47 CheekSquintLeft
    fwdBackKey(47, 'CTRL_L_eye_cheekRaise','ty', 1)

    # 48 CheekSquintRight
    fwdBackKey(48, 'CTRL_R_eye_cheekRaise','ty', 1)

    # 49 NoseSneerLeft
    fwdBackKey(49, 'CTRL_L_nose','ty', 1)

    # 50 NoseSneerRight
    fwdBackKey(50, 'CTRL_R_nose','ty', 1)

    # 51 TonqueOut
    # fwdBackKey(51, 'CTRL_C_tongue','ty', -0.82)
    # fwdBackKey(51, 'CTRL_C_tongue_inOut','ty', -0.76)
    # fwdBackKey(51, 'CTRL_C_tongue_roll','ty', -0.24)
    # fwdBackKey(51, 'CTRL_C_tongue_narrowWide','ty', 0.62)

    # 51 mouthClose
    fwdBackKey(51, 'CTRL_C_jaw','ty', 1)
    fwdBackKey(51, 'CTRL_L_mouth_lipsTogetherU','ty', 1)
    fwdBackKey(51, 'CTRL_R_mouth_lipsTogetherU','ty', 1)
    fwdBackKey(51, 'CTRL_L_mouth_lipsTogetherD','ty', 1)
    fwdBackKey(51, 'CTRL_R_mouth_lipsTogetherD','ty', 1)

# new
def duplicateLODGroup():
    # lod0
    myList = cmds.listRelatives('head_lod0_grp', c=True)
    myMesh = cmds.polyUniteSkinned( myList, ch=0 )
    myMesh = myMesh[0]

    # target group
    myGrp = cmds.group(em=True, n='target_grp')
    cmds.hide(myGrp)

    # make pose & duplicate
    for target in ARKitDict.myList:
        makePose(target)
        cmds.duplicate(myMesh, n=target, rc=True)

        if target != 'Default':
            cmds.parent(target, myGrp)

    # mouth close
    makePose('Default')
    myHead = cmds.duplicate(myMesh)

    makePose('MouthClose')
    target1 = cmds.duplicate(myMesh)

    makePose('JawOpen')
    target2 = cmds.duplicate(myMesh)

    myBlend = cmds.blendShape( target1, target2, myHead )
    cmds.setAttr(myBlend[0]+'.'+target1[0], 1)
    cmds.setAttr(myBlend[0]+'.'+target2[0], -1)

    myTarget = cmds.duplicate(myHead, n='MouthClose', rc=True)
    cmds.parent(myTarget[0], myGrp)
    cmds.delete(myHead,target1,target2)

    # blendShape
    myTargetList = cmds.listRelatives(myGrp, c=True)
    cmds.blendShape( myTargetList, 'Default', n='BS_ARKit' )
    cmds.delete(myGrp)
    # cmds.hide(myMesh)

    makePose('Default')

    # unlock
    myList = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
    for i in myList:
        cmds.setAttr('%s.%s' % ('Default', i), keyable=True, lock=False)

    cmds.setAttr ("Default.tx", -27)

    # connect blendShape 2 ui
    importUI()
    connectBlendShape2UI()

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

def defaultPose():
    for item in ARKitDict.myDict:
        for con in ARKitDict.myDict[item]:
            for axis in ARKitDict.myDict[item][con]:
                if len(cmds.ls('CTRL_C_eye'))>1:
                    defaultPoseNew()
                    cmds.setAttr(oldCon(con)+'.'+axis, 0)
                else:
                    cmds.setAttr(con+'.'+axis, 0)

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

                if len(cmds.ls('CTRL_C_eye'))>1:
                    makePoseNew(target)
                    cmds.setAttr(oldCon(con)+'.'+axis, value)
                else:
                    cmds.setAttr(con+'.'+axis, value)

def importUI():
    usd = cmds.internalVar(usd=True)
    mayascripts = '%s/%s' % (usd.rsplit('/', 3)[0], 'scripts/')
    tempPath = mayascripts + "Facial/template/facial_ui_v01.ma"

    cmds.file(tempPath, i=True)

def plusConnect(con, axis, target):
    if bool(cmds.ls(target+'_clamp')) == False:
        myClamp = cmds.createNode('clamp', n=target+'_clamp')
        cmds.setAttr(myClamp+'.maxR', 1)

        cmds.connectAttr(newCon(con)+'.'+axis, myClamp+'.inputR', f=True)
        cmds.connectAttr(myClamp+'.outputR', 'BS_ARKit.'+target, f=True)

def minusConnect(con, axis, target):
    if bool(cmds.ls(target+'_clamp')) == False:
        myMult = cmds.createNode('multiplyDivide', n=target+'_mult')
        cmds.setAttr(myMult+'.input2X', -1)

        myClamp = cmds.createNode('clamp', n=target+'_clamp')
        cmds.setAttr(myClamp+'.maxR', 1)

        cmds.connectAttr(newCon(con)+'.'+axis, myMult+'.input1X', f=True)
        cmds.connectAttr(myMult+'.outputX', myClamp+'.inputR', f=True)
        cmds.connectAttr(myClamp+'.outputR', 'BS_ARKit.'+target, f=True)

def multiConnect(conA, conB, axis, target, value):
    if bool(cmds.ls(target+'_clamp')) == False:
        myMultA = cmds.createNode('multiplyDivide', n=target+'_A_mult')
        cmds.setAttr(myMultA+'.input2X', value)

        myMultB = cmds.createNode('multiplyDivide', n=target+'_B_mult')
        cmds.setAttr(myMultB+'.input2X', value)

        myClampA = cmds.createNode('clamp', n=target+'_A_clamp')
        cmds.setAttr(myClampA+'.maxR', 1)

        myClampB = cmds.createNode('clamp', n=target+'_B_clamp')
        cmds.setAttr(myClampB+'.maxR', 1)

        myPlus = cmds.createNode('plusMinusAverage', n=target+'_plus')

        cmds.connectAttr(newCon(conA)+'.'+axis, myMultA+'.input1X', f=True)
        cmds.connectAttr(myMultA+'.outputX', myClampA+'.inputR', f=True)
        cmds.connectAttr(myClampA+'.outputR', myPlus+'.input1D[0]', f=True)

        cmds.connectAttr(newCon(conB)+'.'+axis, myMultB+'.input1X', f=True)
        cmds.connectAttr(myMultB+'.outputX', myClampB+'.inputR', f=True)
        cmds.connectAttr(myClampB+'.outputR', myPlus+'.input1D[1]', f=True)

        cmds.connectAttr(myPlus+'.output1D', 'BS_ARKit.'+target, f=True)

def connectBlendShape2UI():
    plusConnect('CTRL_L_eye_blink', 'ty', 'EyeBlinkLeft')
    multiConnect('CTRL_C_eye', 'CTRL_L_eye', 'ty', 'EyeLookDownLeft', -1)
    multiConnect('CTRL_C_eye', 'CTRL_L_eye', 'tx', 'EyeLookInLeft', -1)
    multiConnect('CTRL_C_eye', 'CTRL_L_eye', 'tx', 'EyeLookOutLeft', 1)
    multiConnect('CTRL_C_eye', 'CTRL_L_eye', 'ty', 'EyeLookUpLeft', 1)
    plusConnect('CTRL_L_eye_squintInner', 'ty', 'EyeSquintLeft')
    minusConnect('CTRL_L_eye_blink', 'ty', 'EyeWideLeft')

    plusConnect('CTRL_R_eye_blink', 'ty', 'EyeBlinkRight')
    multiConnect('CTRL_C_eye', 'CTRL_R_eye', 'ty', 'EyeLookDownRight', -1)
    multiConnect('CTRL_C_eye', 'CTRL_R_eye', 'tx', 'EyeLookInRight', 1)
    multiConnect('CTRL_C_eye', 'CTRL_R_eye', 'tx', 'EyeLookOutRight', -1)
    multiConnect('CTRL_C_eye', 'CTRL_R_eye', 'ty', 'EyeLookUpRight', 1)
    plusConnect('CTRL_R_eye_squintInner', 'ty', 'EyeSquintRight')
    minusConnect('CTRL_R_eye_blink', 'ty', 'EyeWideRight')

    minusConnect('CTRL_C_jaw_fwdBack', 'ty', 'JawForward')
    minusConnect('CTRL_C_jaw', 'tx', 'JawLeft')
    plusConnect('CTRL_C_jaw', 'tx', 'JawRight')
    plusConnect('CTRL_C_jaw', 'ty', 'JawOpen')

    plusConnect('CTRL_C_mouth_funnelD', 'ty', 'MouthFunnel')
    plusConnect('CTRL_C_mouth_purseD', 'ty', 'MouthPucker')

    plusConnect('CTRL_C_mouth', 'ty', 'MouthLeft')
    minusConnect('CTRL_C_mouth', 'ty', 'MouthRight')
    plusConnect('CTRL_L_mouth_cornerPull', 'ty', 'MouthSmileLeft')
    plusConnect('CTRL_R_mouth_cornerPull', 'ty', 'MouthSmileRight')
    plusConnect('CTRL_L_mouth_cornerDepress', 'ty', 'MouthFrownLeft')
    plusConnect('CTRL_R_mouth_cornerDepress', 'ty', 'MouthFrownRight')
    plusConnect('CTRL_L_mouth_dimple', 'ty', 'MouthDimpleLeft')
    plusConnect('CTRL_R_mouth_dimple', 'ty', 'MouthDimpleRight')
    plusConnect('CTRL_L_mouth_stretch', 'ty', 'MouthStretchLeft')
    plusConnect('CTRL_R_mouth_stretch', 'ty', 'MouthStretchRight')
    plusConnect('CTRL_C_mouth_lipsRollD', 'ty', 'MouthRollLower')
    plusConnect('CTRL_C_mouth_lipsRollU', 'ty', 'MouthRollUpper')
    plusConnect('CTRL_C_jaw_ChinRaiseD', 'ty', 'MouthShrugLower')
    plusConnect('CTRL_C_jaw_ChinRaiseU', 'ty', 'MouthShrugUpper')
    plusConnect('CTRL_L_mouth_press', 'ty', 'MouthPressLeft')
    plusConnect('CTRL_R_mouth_press', 'ty', 'MouthPressRight')
    plusConnect('CTRL_L_mouth_lowerLipDepress', 'ty', 'MouthLowerDownLeft')
    plusConnect('CTRL_R_mouth_lowerLipDepress', 'ty', 'MouthLowerDownRight')
    plusConnect('CTRL_L_mouth_upperLipRaise', 'ty', 'MouthUpperUpLeft')
    plusConnect('CTRL_R_mouth_upperLipRaise', 'ty', 'MouthUpperUpRight')
    plusConnect('CTRL_C_mouth_close', 'ty', 'MouthClose')

    plusConnect('CTRL_L_brow_down', 'ty', 'BrowDownLeft')
    plusConnect('CTRL_R_brow_down', 'ty', 'BrowDownRight')
    plusConnect('CTRL_L_brow_raiseOut', 'ty', 'BrowOuterUpLeft')
    plusConnect('CTRL_R_brow_raiseOut', 'ty', 'BrowOuterUpRight')
    plusConnect('CTRL_C_brow_raiseIn', 'ty', 'BrowInnerUp')

    plusConnect('CTRL_L_eye_cheekRaise', 'ty', 'CheekSquintLeft')
    plusConnect('CTRL_R_eye_cheekRaise', 'ty', 'CheekSquintRight')
    plusConnect('CTRL_C_mouth_suckBlow', 'ty', 'CheekPuff')

    plusConnect('CTRL_L_nose', 'ty', 'NoseSneerLeft')
    plusConnect('CTRL_R_nose', 'ty', 'NoseSneerRight')
