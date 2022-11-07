import maya.cmds as cmds

myHead = 'CHA_PCF_Head_Head004_LOD0'
myTarget = cmds.listRelatives('target_grp', c=True)

cmds.blendShape(myTarget, myHead, n='BS_node')

# eye
cmds.setDrivenKeyframe ('BS_node.EyeBlinkLeft', cd='CTRL_L_eye_blink.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeBlinkLeft', cd='CTRL_L_eye_blink.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookDownLeft', cd='CTRL_C_eye.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookDownLeft', cd='CTRL_C_eye.ty', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookInLeft', cd='CTRL_C_eye.tx', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookInLeft', cd='CTRL_C_eye.tx', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookOutLeft', cd='CTRL_C_eye.tx', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookOutLeft', cd='CTRL_C_eye.tx', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookUpLeft', cd='CTRL_C_eye.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookUpLeft', cd='CTRL_C_eye.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeSquintLeft', cd='CTRL_L_eye_squintInner.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeSquintLeft', cd='CTRL_L_eye_squintInner.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeWideLeft', cd='CTRL_L_eye_blink.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeWideLeft', cd='CTRL_L_eye_blink.ty', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeBlinkRight', cd='CTRL_R_eye_blink.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeBlinkRight', cd='CTRL_R_eye_blink.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookDownRight', cd='CTRL_C_eye.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookDownRight', cd='CTRL_C_eye.ty', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookInRight', cd='CTRL_C_eye.tx', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookInRight', cd='CTRL_C_eye.tx', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookOutRight', cd='CTRL_C_eye.tx', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookOutRight', cd='CTRL_C_eye.tx', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeLookUpRight', cd='CTRL_C_eye.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeLookUpRight', cd='CTRL_C_eye.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeSquintRight', cd='CTRL_R_eye_squintInner.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeSquintRight', cd='CTRL_R_eye_squintInner.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.EyeWideRight', cd='CTRL_R_eye_blink.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.EyeWideRight', cd='CTRL_R_eye_blink.ty', dv=-1, v=1)

# jaw
cmds.setDrivenKeyframe ('BS_node.JawForward', cd='CTRL_C_jaw_fwdBack.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.JawForward', cd='CTRL_C_jaw_fwdBack.ty', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.JawForward', cd='CTRL_C_jaw_fwdBack.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.JawForward', cd='CTRL_C_jaw_fwdBack.ty', dv=1, v=-1)

cmds.setDrivenKeyframe ('BS_node.JawLeft', cd='CTRL_C_jaw.tx', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.JawLeft', cd='CTRL_C_jaw.tx', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.JawRight', cd='CTRL_C_jaw.tx', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.JawRight', cd='CTRL_C_jaw.tx', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.JawOpen', cd='CTRL_C_jaw.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.JawOpen', cd='CTRL_C_jaw.ty', dv=1, v=1)

# mouth
cmds.setDrivenKeyframe ('BS_node.MouthFunnel', cd='CTRL_C_mouth_funnelD.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthFunnel', cd='CTRL_C_mouth_funnelD.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthPucker', cd='CTRL_C_mouth_purseD.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthPucker', cd='CTRL_C_mouth_purseD.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthLeft', cd='CTRL_C_mouth.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthLeft', cd='CTRL_C_mouth.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthRight', cd='CTRL_C_mouth.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthRight', cd='CTRL_C_mouth.ty', dv=-1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthSmileLeft', cd='CTRL_L_mouth_cornerPull.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthSmileLeft', cd='CTRL_L_mouth_cornerPull.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthSmileRight', cd='CTRL_R_mouth_cornerPull.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthSmileRight', cd='CTRL_R_mouth_cornerPull.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthFrownLeft', cd='CTRL_L_mouth_cornerDepress.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthFrownLeft', cd='CTRL_L_mouth_cornerDepress.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthFrownRight', cd='CTRL_R_mouth_cornerDepress.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthFrownRight', cd='CTRL_R_mouth_cornerDepress.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthDimpleLeft', cd='CTRL_L_mouth_dimple.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthDimpleLeft', cd='CTRL_L_mouth_dimple.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthDimpleRight', cd='CTRL_R_mouth_dimple.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthDimpleRight', cd='CTRL_R_mouth_dimple.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthStretchLeft', cd='CTRL_L_mouth_stretch.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthStretchLeft', cd='CTRL_L_mouth_stretch.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthStretchRight', cd='CTRL_R_mouth_stretch.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthStretchRight', cd='CTRL_R_mouth_stretch.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthRollLower', cd='CTRL_C_mouth_lipsRollD.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthRollLower', cd='CTRL_C_mouth_lipsRollD.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthRollUpper', cd='CTRL_C_mouth_lipsRollU.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthRollUpper', cd='CTRL_C_mouth_lipsRollU.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthShrugLower', cd='CTRL_C_jaw_ChinRaiseD.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthShrugLower', cd='CTRL_C_jaw_ChinRaiseD.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthShrugUpper', cd='CTRL_C_jaw_ChinRaiseU.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthShrugUpper', cd='CTRL_C_jaw_ChinRaiseU.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthPressLeft', cd='CTRL_L_mouth_press.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthPressLeft', cd='CTRL_L_mouth_press.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthPressRight', cd='CTRL_R_mouth_press.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthPressRight', cd='CTRL_R_mouth_press.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthLowerDownLeft', cd='CTRL_L_mouth_lowerLipDepress.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthLowerDownLeft', cd='CTRL_L_mouth_lowerLipDepress.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthLowerDownRight', cd='CTRL_R_mouth_lowerLipDepress.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthLowerDownRight', cd='CTRL_R_mouth_lowerLipDepress.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthUpperUpLeft', cd='CTRL_L_mouth_upperLipRaise.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthUpperUpLeft', cd='CTRL_L_mouth_upperLipRaise.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.MouthUpperUpRight', cd='CTRL_R_mouth_upperLipRaise.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.MouthUpperUpRight', cd='CTRL_R_mouth_upperLipRaise.ty', dv=1, v=1)

# brow
cmds.setDrivenKeyframe ('BS_node.BrowDownLeft', cd='CTRL_L_brow_down.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.BrowDownLeft', cd='CTRL_L_brow_down.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.BrowDownRight', cd='CTRL_R_brow_down.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.BrowDownRight', cd='CTRL_R_brow_down.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.BrowInnerUp', cd='CTRL_C_brow_raiseIn.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.BrowInnerUp', cd='CTRL_C_brow_raiseIn.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.BrowOuterUpLeft', cd='CTRL_L_brow_raiseOut.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.BrowOuterUpLeft', cd='CTRL_L_brow_raiseOut.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.BrowOuterUpRight', cd='CTRL_R_brow_raiseOut.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.BrowOuterUpRight', cd='CTRL_R_brow_raiseOut.ty', dv=1, v=1)

# cheek
cmds.setDrivenKeyframe ('BS_node.CheekPuff', cd='CTRL_C_mouth_suckBlow.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.CheekPuff', cd='CTRL_C_mouth_suckBlow.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.CheekSquintLeft', cd='CTRL_L_eye_cheekRaise.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.CheekSquintLeft', cd='CTRL_L_eye_cheekRaise.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.CheekSquintRight', cd='CTRL_R_eye_cheekRaise.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.CheekSquintRight', cd='CTRL_R_eye_cheekRaise.ty', dv=1, v=1)

# nose
cmds.setDrivenKeyframe ('BS_node.NoseSneerLeft', cd='CTRL_L_nose.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.NoseSneerLeft', cd='CTRL_L_nose.ty', dv=1, v=1)

cmds.setDrivenKeyframe ('BS_node.NoseSneerRight', cd='CTRL_R_nose.ty', dv=0, v=0)
cmds.setDrivenKeyframe ('BS_node.NoseSneerRight', cd='CTRL_R_nose.ty', dv=1, v=1)
