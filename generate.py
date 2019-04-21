# TianTcl - Whisper game - generator

import random

_subject    = ["ข้า","เอ็ง","เจ้า","เผือก","พวกเฮา","พวกเจ้า","ชาวโลก","ชาวเมือง"]
ext_sub     = [None,"สุดยอด","เทศบาล","ตรงนี้","ในห้องน้ำ"]
_verb       = ["กำลังกิน","นอน","เม้ามอย","ยืนอยู่"]
ext_verb    = [None,"รีบหรอ","สล็อต","เจี้ยวจ้าว"]
_object     = [None,"ในลู่วิ่ง","เรื่อง งูงู","ทางเท้า","ใต้ต้นไม้"]
ext_obj     = [None,"ที่สนามกีฬา","ที่มีป่าดงดิบ","ยักษ์ใหญ่"]

def make(_part):

    if _part == "subject":
        word = random.choice(_subject)
    elif _part == "verb":
        word = random.choice(_verb)
    elif _part == "object":
        word = random.choice(_object)
    elif _part == "ext subject":
        word = random.choice(ext_sub)
    elif _part == "ext verb":
        word = random.choice(ext_verb)
    elif _part == "ext object":
        word = random.choice(ext_obj)
    return word

def gen():
    parts =["subject","ext subject","verb","object","ext object","ext verb"]
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence
