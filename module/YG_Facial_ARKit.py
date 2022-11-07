import maya.cmds as cmds

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

cmds.currentUnit( time='film' )
cmds.playbackOptions( e=True, min=0, max=51, aet=51 )


# 0 Default

# 1 EyeBlinkLeft
fwdBackKey(1, 'CTRL_L_eye_blink','translateY',1)

# 2 EyeLookDownLeft
fwdBackKey(2, 'CTRL_L_eye','translateY',-1)

# 3 EyeLookInLeft
fwdKey(3, 'CTRL_L_eye','translateX',-1)

# 4 EyeLookOutLeft
backKey(4, 'CTRL_L_eye','translateX',1)

# 5 EyeLookUpLeft
fwdBackKey(5, 'CTRL_L_eye','translateY',1)

# 6 EyeSquintLeft
fwdBackKey(6, 'CTRL_L_eye_squintInner','translateY',1)

# 7 EyeWideLeft
fwdBackKey(7, 'CTRL_L_eye_blink','translateY',-1)

# 8 EyeBlinkRight
fwdBackKey(8, 'CTRL_R_eye_blink','translateY',1)

# 9 EyeLookDownRight
fwdBackKey(9, 'CTRL_R_eye','translateY', -1)

# 10 EyeLookInRight
fwdKey(10, 'CTRL_R_eye','translateX', 1)

# 11 EyeLookOutRight
backKey(11, 'CTRL_R_eye','translateX', -1)

# 12 EyeLookUpRight
fwdBackKey(12, 'CTRL_R_eye','translateY', 1)

# 13 EyeSquintRight
fwdBackKey(13, 'CTRL_R_eye_squintInner','translateY', 1)

# 14 EyeWideRight
fwdBackKey(14, 'CTRL_R_eye_blink','translateY', -1)

# 15 JawForward
fwdBackKey(15, 'CTRL_C_jaw_fwdBack','translateY', -1)

# 16 JawLeft
fwdKey(16, 'CTRL_C_jaw','translateX', -1)

# 17 JawRight
backKey(17, 'CTRL_C_jaw','translateX', 1)

# 18 JawOpen
fwdBackKey(18, 'CTRL_C_jaw','translateY', 1)

# 19 MouthFunnel
fwdKey(19, 'CTRL_L_mouth_funnelU','translateY', 1)
fwdKey(19, 'CTRL_R_mouth_funnelU','translateY', 1)
fwdKey(19, 'CTRL_L_mouth_funnelD','translateY', 1)
fwdKey(19, 'CTRL_R_mouth_funnelD','translateY', 1)

# 20 MouthPucker
fwdBackKey(20, 'CTRL_L_mouth_purseU','translateY', 1)
fwdBackKey(20, 'CTRL_R_mouth_purseU','translateY', 1)
fwdBackKey(20, 'CTRL_L_mouth_purseD','translateY', 1)
fwdBackKey(20, 'CTRL_R_mouth_purseD','translateY', 1)
backKey(20, 'CTRL_L_mouth_funnelU','translateY', 0.75)
backKey(20, 'CTRL_R_mouth_funnelU','translateY', 0.75)
backKey(20, 'CTRL_L_mouth_funnelD','translateY', 0.75)
backKey(20, 'CTRL_R_mouth_funnelD','translateY', 0.75)
fwdBackKey(20, 'CTRL_L_mouth_towardsU','translateY', 0.41)
fwdBackKey(20, 'CTRL_R_mouth_towardsU','translateY', 0.41)
fwdBackKey(20, 'CTRL_L_mouth_towardsD','translateY', 0.41)
fwdBackKey(20, 'CTRL_R_mouth_towardsD','translateY', 0.41)

# 21 MouthLeft
fwdKey(21, 'CTRL_C_mouth','translateX', 1)

# 22 MouthRight
backKey(22, 'CTRL_C_mouth','translateX', -1)

# 23 MouthSmileLeft
fwdBackKey(23, 'CTRL_L_mouth_cornerPull','translateY', 1)

# 24 MouthSmileRight
fwdBackKey(24, 'CTRL_R_mouth_cornerPull','translateY', 1)

# 25 MouthFrownLeft
fwdBackKey(25, 'CTRL_L_mouth_cornerDepress','translateY', 1)

# 26 MouthFrownRight
fwdBackKey(26, 'CTRL_R_mouth_cornerDepress','translateY', 1)

# 27 MouthDimpleLeft
fwdBackKey(27, 'CTRL_L_mouth_dimple','translateY', 1)

# 28 MouthDimpleRight
fwdBackKey(28, 'CTRL_R_mouth_dimple','translateY', 1)

# 29 MouthStretchLeft
fwdBackKey(29, 'CTRL_L_mouth_stretch','translateY', 1)

# 30 MouthStretchRight
fwdBackKey(30, 'CTRL_R_mouth_stretch','translateY', 1)

# 31 MouthRollLower
fwdKey(31, 'CTRL_L_mouth_lipsRollU','translateY', 0.5)
fwdKey(31, 'CTRL_R_mouth_lipsRollU','translateY', 0.5)
fwdBackKey(31, 'CTRL_L_mouth_lipsRollD','translateY', 1)
fwdBackKey(31, 'CTRL_R_mouth_lipsRollD','translateY', 1)

# 32 MouthRollUpper
backKey(32, 'CTRL_L_mouth_lipsRollU','translateY', 1)
backKey(32, 'CTRL_R_mouth_lipsRollU','translateY', 1)

# 33 MouthShrugLower
fwdBackKey(33, 'CTRL_L_jaw_ChinRaiseD','translateY', 1)
fwdBackKey(33, 'CTRL_R_jaw_ChinRaiseD','translateY', 1)

# 34 MouthShrugUpper
fwdBackKey(34, 'CTRL_L_jaw_ChinRaiseU','translateY', 1)
fwdBackKey(34, 'CTRL_R_jaw_ChinRaiseU','translateY', 1)

# 35 MouthPressLeft
fwdBackKey(35, 'CTRL_L_mouth_pressU','translateY', 1)
fwdBackKey(35, 'CTRL_L_mouth_pressD','translateY', 1)

# 36 MouthPressRight
fwdBackKey(36, 'CTRL_R_mouth_pressU','translateY', 1)
fwdBackKey(36, 'CTRL_R_mouth_pressD','translateY', 1)

# 37 MouthLowerDownLeft
fwdBackKey(37, 'CTRL_L_mouth_lowerLipDepress','translateY', 1)

# 38 MouthLowerDownRight
fwdBackKey(38, 'CTRL_R_mouth_lowerLipDepress','translateY', 1)

# 39 MouthUpperUpLeft
fwdBackKey(39, 'CTRL_L_mouth_upperLipRaise','translateY', 1)

# 40 MouthUpperUpRight
fwdBackKey(40, 'CTRL_R_mouth_upperLipRaise','translateY', 1)

# 41 BrowDownLeft
fwdBackKey(41, 'CTRL_L_brow_down','translateY', 1)

# 42 BrowDownRight
fwdBackKey(42, 'CTRL_R_brow_down','translateY', 1)

# 43 BrowInnerUp
fwdKey(43, 'CTRL_L_brow_raiseIn','translateY', 1)
fwdBackKey(43, 'CTRL_R_brow_raiseIn','translateY', 1)
fwdBackKey(43, 'CTRL_L_brow_lateral','translateY', 1)
fwdBackKey(43, 'CTRL_R_brow_lateral','translateY', 1)

# 44 BrowOuterUpLeft
backKey(44, 'CTRL_L_brow_raiseIn','translateY', 1)
fwdBackKey(44, 'CTRL_L_brow_raiseOut','translateY', 1)

# 45 BrowOuterUpRight
fwdBackKey(45, 'CTRL_R_brow_raiseIn','translateY', 1)
fwdBackKey(45, 'CTRL_R_brow_raiseOut','translateY', 1)

# 46 CheekPuff
fwdBackKey(46, 'CTRL_L_mouth_suckBlow','translateY', 1)
fwdBackKey(46, 'CTRL_R_mouth_suckBlow','translateY', 1)
fwdBackKey(46, 'CTRL_L_mouth_lipsBlow','translateY', 1)
fwdBackKey(46, 'CTRL_R_mouth_lipsBlow','translateY', 1)

# 47 CheekSquintLeft
fwdBackKey(47, 'CTRL_L_eye_cheekRaise','translateY', 1)

# 48 CheekSquintRight
fwdBackKey(48, 'CTRL_R_eye_cheekRaise','translateY', 1)

# 49 NoseSneerLeft
fwdBackKey(49, 'CTRL_L_nose','translateY', 1)

# 50 NoseSneerRight
fwdBackKey(50, 'CTRL_R_nose','translateY', 1)

# 51 TonqueOut
# fwdBackKey(51, 'CTRL_C_tongue','translateY', -0.82)
# fwdBackKey(51, 'CTRL_C_tongue_inOut','translateY', -0.76)
# fwdBackKey(51, 'CTRL_C_tongue_roll','translateY', -0.24)
# fwdBackKey(51, 'CTRL_C_tongue_narrowWide','translateY', 0.62)

# 51 mouthClose
fwdBackKey(51, 'CTRL_C_jaw','translateY', 1)
fwdBackKey(51, 'CTRL_L_mouth_lipsTogetherU','translateY', 1)
fwdBackKey(51, 'CTRL_R_mouth_lipsTogetherU','translateY', 1)
fwdBackKey(51, 'CTRL_L_mouth_lipsTogetherD','translateY', 1)
fwdBackKey(51, 'CTRL_R_mouth_lipsTogetherD','translateY', 1)

# duplicate LOD group

# myLod = 'head_lod0_grp'
myList = cmds.listRelatives('head_lod0_grp', c=True)
myMesh = cmds.polyUniteSkinned( myList, ch=0 )

myGrp = cmds.group(em=True, n='target_grp')
myList = ['Default','EyeBlinkLeft','EyeLookDownLeft','EyeLookInLeft','EyeLookOutLeft',
        'EyeLookUpLeft','EyeSquintLeft','EyeWideLeft','EyeBlinkRight','EyeLookDownRight',
        'EyeLookInRight','EyeLookOutRight','EyeLookUpRight','EyeSquintRight','EyeWideRight',
        'JawForward','JawLeft','JawRight','JawOpen','MouthFunnel',
        'MouthPucker','MouthLeft','MouthRight','MouthSmileLeft','MouthSmileRight',
        'MouthFrownLeft','MouthFrownRight','MouthDimpleLeft','MouthDimpleRight','MouthStretchLeft',
        'MouthStretchRight','MouthRollLower','MouthRollUpper','MouthShrugLower','MouthShrugUpper',
        'MouthPressLeft','MouthPressRight','MouthLowerDownLeft','MouthLowerDownRight','MouthUpperUpLeft',
        'MouthUpperUpRight','BrowDownLeft','BrowDownRight','BrowInnerUp','BrowOuterUpLeft',
        'BrowOuterUpRight','CheekPuff','CheekSquintLeft','CheekSquintRight','NoseSneerLeft',
        'NoseSneerRight']

for i in range(len(myList)):
    #print myList[i]
    cmds.currentTime( i, edit=True )
    cmds.duplicate(myMesh, n=myList[i], rc=True)
    cmds.parent(myList[i], myGrp)

# mouthClose target
cmds.currentTime( 0, edit=True )
myHead = cmds.duplicate(myMesh)

cmds.currentTime( 51, edit=True )
target1 = cmds.duplicate(myMesh)

cmds.currentTime( 18, edit=True )
target2 = cmds.duplicate(myMesh)

myBlend = cmds.blendShape( target1, target2, myHead )
cmds.setAttr(myBlend[0]+'.'+target1[0], 1)
cmds.setAttr(myBlend[0]+'.'+target2[0], -1)

myTemp = cmds.group(em=True, n='MouthClose_grp')
cmds.parent(myTemp,myGrp)
myTarget = cmds.duplicate(myHead, rc=True)
cmds.parent(myTarget[0], myTemp)
cmds.delete(myHead,target1,target2)

cmds.currentTime( 0, edit=True )
