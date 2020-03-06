
from naftawayh.ar_ctype import *
from data.arabic_const import *

L = [ ]

hrof_ila=(YEH,WAW)
hrof={YEH,WAW,HAMZA}

class isShihOrMoatal():
    """تحليل ومعالجة صحة واعتلال الفعل من خلال الجذر """
    def __init__(self,jader):
        self.jader      = jader
        self.jaderSplit = self.jader.split()
        self.fa         = self.jaderSplit[0]
        self.ain        = self.jaderSplit[1]
        self.lam        = self.jaderSplit[2]
        self.faal       = self.fa + self.ain + self.lam
        self.faAin      = self.jaderSplit[0:2]
        self.ainLam     = self.jaderSplit[1:]
        self.faLam      = self.jaderSplit[0::2]
        self.hrof_ila   = {YEH,WAW,HAMZA}
        self.findFa     = self.fa in self.hrof_ila
        self.findAin    = self.ain in self.hrof_ila
        self.findLam    = self.lam in self.hrof_ila
        self.findFaAin  = self.findFa or self.findAin
        self.findAinLam = self.findAin or self.findLam
        self.findFaLam  = self.findFa or self.findLam
        self.find       = self.findFaAin or self.findLam
        #any ( elem in self.hrof_ila for elem in self.jaderSplit)


    # def deco(self,*args):
    #     if len ( args ) == 3:
    #         lst = [ ]
    #         for x in self.jaderSplit:
    #             if HAMZA == self.ain : x = x.replace ( HAMZA , ALEF_HAMZA_ABOVE )
    #             if HAMZA==self.fa and self.findAin is False : x=x.replace ( HAMZA , ALEF_HAMZA_ABOVE )
    #             if HAMZA == self.fa and self.findAin is True: return True,''.join(ALEF_MADDA+self.lam+args[2])
    #             lst.append ( x + args [ len ( lst ) ] )
    #             fial = ''.join ( lst )
    #         return True , fial
    #     else:
    #         return True



    def is_sahih_salim(self): # ص ص ص صحيح سالم

        if (self.find is False) and self.ain != self.lam and self.ain != self.fa :
            return True
        return False
    def is_sahih_mahmoz_fa(self): # ء ص ص صحيح سالم مهموز الأول

        if self.findAinLam is False and self.fa == HAMZA and self.ain != self.lam:
            return True
        return False
    def is_sahih_mahmoz_ain(self): # ص ء ص صحيح سالم مهموز الوسط

        if self.findFaLam is False and  self.ain == HAMZA:
            return True
        return False
    def is_sahih_mahmoz_lam(self): #  ص ص ء صحيح سالم مهموز الآخر

        if self.findFaAin is False and  self.lam == HAMZA and self.fa != self.ain :
            return True
        return False
    def is_sahih_mahmoz_faLam(self):    #  ء ص ء صحيح سالم مهموز الأول و الآخر

        if self.findAin is False and  self.fa == HAMZA and self.lam == HAMZA:
            return True
        return False
    def is_ajwaf_yeh(self): # معتل العين أجوف يائي ص ي ص
        """الأجوف يائي: هو كل فعل اعتلت عينه بياء .مثال: ليس,باع  يبيع بيعا"""
        if self.findFaLam is False  and self.ain == YEH:
            return True
        return False
    def is_methal_yeh_modaf(self): #معتل مثال يائي مضعف ي (ص ص) معتل الأول يائي
        """المثال يائي مضعف: هو كل فعل اعتلت فاؤه بياء وعينه ولامه لهما نفس الحرف"""
        if self.findAinLam is False  and self.fa == YEH and self.ain==self.lam:
            return True
        return False
    def is_ajwaf_yeh_mahmoz_lam(self): #معتل  ص ي ء أجوف يائي مهموز الأخر
        """الأجوف يائي المهموز اخره: هو كل فعل اعتلت عينه بياء ولامه همزة """
        if self.findFa is False  and self.ain == YEH and self.lam==HAMZA:
            return True
        return False

    def is_sahih_salem_modaf_faAin(self):  # (ص ص ) ص صحيح سالم مضعف الاول و الأوسط
        """صحيح سالم مضعف الفاء و العين"""
        if self.find is False and self.fa == self.ain and self.ain != self.lam:
            return True
        return False
    def is_methal_yeh_mahmoz_ain(self):  # ي ء ص معتل الأول مهموز الأوسط
        """ المثال يائي مهموز العين: هو كل فعل اعتلت فاؤه بياء وعينه بهمزة"""
        if self.findLam is False and self.fa == YEH and self.ain == HAMZA:
            return True
        return False
    def is_ajwaf_waw_mahmoz_fa(self):  # ء و ض مهموز الاول معتل وسط واوي
        """ الأجوف واوي مهموز الاول: هو كل فعل اعتلت عينه بواو وهمزة أوله """
        if self.findLam is False and self.fa == HAMZA and self.ain == WAW:
            return True
        return False
    def is_naks_waw_mahmoz_ain(self):  # ص ء و مهموز الوسط معتل الاخر واوي
        """ الناقص واوي مهموز العين:هوكل فعل اعتلت لامه بواو وعينه بهمزة  """
        if self.findFa is False and self.ain == HAMZA and self.lam == WAW:
            return True
        return False
    def is_sahih_salem_modaf_ainlam(self):  # صحيح سالم مضعف الاخر و الأوسط ص (ص ض)
        """ صحيح سالم مضعف الاخر و الأوسط ص (ص ض)"""
        if self.find is False and  self.ain == self.lam and self.fa != self.ain:
            return True
        return False
    def is_naks_yeh_mahmoz_fa(self):  # ء ص ي مهموز الاول معتل الأخر يائي
        """ الناقص يائي مهموز الفاء:هوكل فعل اعتلت لامه بياء وفائه بهمزة """
        if self.findAin is False and self.fa == HAMZA and self.lam == YEH:
            return True
        return False
    def is_naks_waw(self): #معتل ناقص ص ص و معتل االاخر واوي
        """ الناقص الواوي:هوكل فعل اعتلت لامه بياء """
        if self.findFaAin is False  and self.fa != self.ain and self.lam==WAW:
            return True
        return False
    def is_methal_wawi_mahmoz_ain(self): # معتل مثال واوي مهموز العين و ء ص
        """ المثال واوي المهموز العين: هو كل فعل اعتلت فاؤه بواو وعينه بهمزة """
        if self.findLam is False  and self.fa == WAW and self.ain==HAMZA:
            return True
        return False
    def is_methal_wawi_modaf(self): #معتل مثال مضعف و (ص ص) معتل الأول واوي مضعف
        """المثال واوي مضعف: هو كل فعل اعتلت فاؤه بواو و مضعف الاخر """
        if self.findAinLam is False  and self.fa == WAW and self.ain==self.lam:
            return True
        return False

    def is_ajwaf_waw(self):  # الاجوف واوي ص و ص
        """ الاجوف واوي:هوكل فعل اعتلت عينه بياء """
        if self.findFaLam is False and self.ain == WAW:
            return True
        return False
    def is_lafif_makron_2yah(self):  # لفيف مقرون ص ي ي
        """ لفيف مقرون: وهو ما اجتمع فيه حرفا علة دون أن يفرق بينهما حرف آخر صحيح """
        if self.findFa is False and self.ain == YEH and self.ain== self.lam:
            return True
        return False
    def is_naks_yeh_mahmoz_ain(self):  # ص ء ي مهموز الوسط معتل الأخر يائي
        """ الناقص يائي مهموز العين:هوكل فعل اعتلت لامه بياء وعينه بهمزة """
        if self.findFa is False and self.ain == HAMZA and self.lam == YEH:
            return True
        return False
    def is_lafif_mafrok_w_h_y(self):  # لفيف مفروق مهموز العين و ء ي
        """ لفيف مفروق: وهو ما كان فيه حرفا علة غير متجاورين بمعنى أن يفرق بينهما حرف صحيح """
        if self.fa == WAW and self.ain == HAMZA and self.lam == YEH:
            return True
        return False
    def is_ajwaf_yeh_mahmoz_fa(self):  # ء ي ض مهموز الاول معتل وسط يائي
        """ الأجوف يائي مهموز الاول: هو كل فعل اعتلت عينه بياء وهمزة أوله """
        if self.findLam is False and self.fa == HAMZA and self.ain == YEH:
            return True
        return False

    def is_lafif_mafrok_w_y(self):  # لفيف مفروق  و ص ي
        """ لفيف مفروق: وهو ما كان فيه حرفا علة غير متجاورين بمعنى أن يفرق بينهما حرف صحيح """
        if self.findAin is False and self.fa == WAW and self.lam == YEH:
            return True
        return False

    def is_lafif_makron_2waw(self):  # لفيف مقرون ص و و
        """ لفيف مقرون: وهو ما اجتمع فيه حرفا علة دون أن يفرق بينهما حرف آخر صحيح """
        if self.findFa is False and self.ain == self.lam==WAW:
            return True
        return False

    def is_lafif_makron_y_w(self):  # لفيف مقرون ي و ص
        """ لفيف مقرون: وهو ما اجتمع فيه حرفا علة دون أن يفرق بينهما حرف آخر صحيح """
        if self.findLam is False and self.fa == YEH and self.ain==WAW:
            return True
        return False

    def is_sahih_mahmoz_fa_modaf(self): # ء(ص ص ) صحيح سالم مضعف مهموز الأول

        if self.findAinLam is False and  self.fa == HAMZA and self.ain == self.lam:
            return True
        return False

    def is_lafif_mafrok_y_y(self):  # لفيف مفروق  ي ص ي
        """ لفيف مفروق: وهو ما كان فيه حرفا علة غير متجاورين بمعنى أن يفرق بينهما حرف صحيح """
        if self.findAin is False and self.fa == YEH  and self.fa == self.lam:
            return True
        return False

    def is_lafif_makron_w_ain_y_lam(self):  # لفيف مقرون  ص و ي
        """ لفيف مقرون: وهو ما اجتمع فيه حرفا علة دون أن يفرق بينهما حرف آخر صحيح  """
        if self.findFa is False and self.ain == WAW and self.lam == YEH:
            return True
        return False
    def is_lafif_makron_w_fa_y_ain(self):  # لفيف مقرون و ي ص
        """ لفيف مقرون: وهو ما اجتمع فيه حرفا علة دون أن يفرق بينهما حرف آخر صحيح  """
        if self.findLam is False and self.fa == WAW and self.ain == YEH:
            return True
        return False

    def is_naks_yeh(self):  # معتل ناقص ص ص ي معتل االاخر يائي
        """ الناقص يائي:هوكل فعل اعتلت لامه بياء """
        if self.findFaAin is False and self.fa != self.ain and self.lam == YEH:
            return True
        return False
    def is_methal_wawi(self):  #  و ص ص معتل مثال واوي
        """ المثال واوي: هو كل فعل اعتلت فاؤه بواو """
        if self.findAinLam is False and self.ain != self.lam and self.fa == WAW:
            return True
        return False
    def is_naks_wawi_mahmoz_fa(self):  #  ء ص و معتل ناقض واوي مهموز الاول
        """ الناقض واوي: هو كل فعل اعتلت لامه بواو """
        if self.findAin is False and self.fa == HAMZA and self.lam == WAW:
            return True
        return False
    def is_methal_wawi_mahmoz_lam(self):  #  و ص ء معتل مثال واوي مهموز الاول
        """ المثال واوي: هو كل فعل اعتلت فاؤه بواو """
        if self.findAin is False and self.fa == WAW and self.lam == HAMZA:
            return True
        return False

    def is_methal_yeh(self):  # ي ص ص معتل مثال يائي
        """ المثال اليائي: هو كل فعل اعتلت فاؤه بياء """
        if self.findAinLam is False and self.ain != self.lam and self.fa == YEH:
            return True
        return False
    def is_lafif_makron_2yeh_mahmoz(self):  # لفيف مقرون يائي مهموز الاول ء ي ي
        """ لفيف مقرون يائي مهموز: وهو ما اجتمع فيه حرفا علة دون أن يفرق بينهما حرف آخر صحيح """
        if self.fa == HAMZA and self.ain == self.lam==YEH:
            return True
        return False
    def is_lafif_makron_h_w_y(self):  # لفيف مقرون مهموز  ء و ي
        """ لفيف مقرون مهموز: وهو ما اجتمع فيه حرفا علة دون أن يفرق بينهما حرف آخر صحيح  """
        if self.fa == HAMZA and self.ain == WAW and self.lam==YEH:
            return True
        return False
    def is_ajwaf_wawi_mahmoz_lam(self):  # ص و ء مهموز الاخر معتل وسط واوي
        """ الأجوف الواوي مهموز الاخر: هو كل فعل اعتلت عينه بواو وهمزة اخره """
        if self.findFa is False and self.ain == WAW and self.lam == HAMZA:
            return True
        return False
    def is_ajwaf_wawi_2hamza(self):  # ء و ء مهموز الاول و الاخر معتل وسط واوي
        """ الأجوف الواوي مهموز الاول و الاخر: هو كل فعل اعتلت عينه بواو وهمزة اوله و اخره """
        if self.ain == WAW and self.fa == self.lam == HAMZA:
            return True
        return False

    @property
    def run_all(self):
        # lst = set()
        for name in dir(self):
            if name.startswith('is'):
                method = getattr(self, name)
                # lst.add(name)
                if method() is True:
                    return True,method.__name__
        # import json
        # print(json.dumps ( lst , indent=1 ))
        # print ( lst  )
        return False , name

class Iallal:
    def __init__(self , w):
        self.word = w
        self.ain = self.word.split ()[1]
        self.lam=self.word.split ()[2]
    def split_space_w_tachkil(self , *args):  # حذف الفراغات من الجذر وتشكيله ليصبح فعل
        if len ( args ) == 3:
            lst = [ ]
            for x in self.word.split():
                print()
                if args[0]== FATHA and  x in hrof_ila and self.lam not in hrof_ila :
                    x = x.replace ( x , ALEF )
                if args[0]== FATHA and  x in hrof_ila and self.lam == YEH :
                    x = x.replace ( self.lam , ALEF_MAKSURA )
                lst.append ( x + args [ len ( lst ) ] )
            d=[z for z in lst[1] ][0]
            lst.pop(1)
            lst.insert(1,d)

            return ''.join(lst),ar_strip_marks(''.join(lst))


                # if HAMZA == self.ain: x = x.replace ( HAMZA , ALEF_HAMZA_ABOVE )
                # if HAMZA == self.fa and self.findAin is False: x = x.replace ( HAMZA , ALEF_HAMZA_ABOVE )
                # if HAMZA == self.fa and self.findAin is True: return True , ''.join (
                #     ALEF_MADDA + self.lam + args [ 2 ] )
                # lst.append ( x + args [ len ( lst ) ] )
                # fial = ''.join ( lst )



class WazenFaall:
    def __init__(self,w):
        self.word=w


    def split_space_w_tachkil(self , *args):  # حذف الفراغات من الجذر وتشكيله ليصبح فعل
        if len(args) == 3:
            lst = [ ]
            for x in self.word.split ():
                lst.append ( x + args [ len ( lst ) ] )

            return ''.join ( lst )


    def fa_a_la(self,CHKEL=FATHA):
        pass
        pass
    def fa_i_la(self):
        pass
    def fa_o_la(self):
        pass

    pass

import time
start=time.time()
tt=('و ب ب')
nn = isShihOrMoatal ( tt )

n = nn.run_all
st= nn.run_all
print ( type(n[1]))
# bn=Iallal(tt)
# print(bn.split_space_w_tachkil(FATHA,FATHA,FATHA))
# vn= ALEF_HAMZA_ABOVE+SHADDA+BEH+FATHA
# print(ar_isvowel(tt),vn,replace_letters(vn))

# m = input('ad  :')
# for v in m.split():
#     print('hi : ',)

TASHKEEL = (FATHATAN, DAMMATAN, KASRATAN, FATHA, DAMMA, KASRA, \
SUKUN, SHADDA,TATWEEL)
f = hrof_ila.count(WAW)
c= hrof_ila.__getitem__(f)
s= isShihOrMoatal(tt)
def ar_strip_marksT(w):
    return re.sub(f'[\s+{TASHKEEL}]',	'', w)
def strip_ila(w):
    w=w.replace(HAMZA,ALEF_HAMZA_ABOVE)
    fial = w
    res= n[1]
    if w [ 3 ] == FATHA:

        print(w,w[4:6])
        "strip tatweel and vowel from a word and return a result word"
        if res in {'is_ajwaf_waw','is_ajwaf_yeh'} :
            return  fial.replace(w[2:4],ALEF)
        elif res in {'is_ajwaf_yeh_mahmoz_fa','is_ajwaf_waw_mahmoz_fa'}:
            return fial.replace(w[:4],ALEF_MADDA)
        elif res in {'is_ajwaf_yeh_mahmoz_lam','is_ajwaf_wawi_mahmoz_lam'} :
            return fial.replace(w[2:5],ALEF+HAMZA)
        elif res in {'is_ajwaf_wawi_2hamza'} :
            return w.replace(w[:5],ALEF_MADDA+HAMZA)
        elif res in {'is_naks_waw','is_naks_wawi_mahmoz_fa'}:
            return fial.replace(w[4:],ALEF)
        elif res in {'is_naks_waw_mahmoz_ain',
                     'is_naks_yeh',
                     'is_naks_yeh_mahmoz_fa',
                     'is_lafif_mafrok_w_h_y',
                     'is_lafif_mafrok_w_y',
                     'is_lafif_mafrok_y_y',
                     'is_lafif_makron_2waw',
                     'is_lafif_makron_h_w_y',
                     'is_lafif_makron_w_ain_y_lam'}:
            return fial[:4]+ALEF_MAKSURA #fial.replace(w, w[:4]+ALEF_MAKSURA)#
        elif s.is_methal_wawi() \
                or s.is_methal_yeh() \
                or s.is_methal_wawi_mahmoz_ain()\
                or s.is_methal_wawi_mahmoz_lam() \
                or s.is_methal_yeh_mahmoz_ain():
            return fial
        elif s.is_methal_wawi_modaf()\
                or s.is_methal_yeh_modaf() \
                or s.is_sahih_mahmoz_fa_modaf()\
                or s.is_sahih_salem_modaf_ainlam() \
                or s.is_sahih_salem_modaf_faAin():
            return fial.replace(w,w[:3]+SHADDA+FATHA)
        elif s.is_lafif_makron_2yah() \
                or s.is_lafif_makron_2yeh_mahmoz()\
                or s.is_lafif_makron_w_fa_y_ain()\
                or s.is_lafif_makron_y_w():
            return None
        else:
            return w
    elif w [ 3 ] == KASRA: # **************************************/
        "strip tatweel and vowel from a word and return a result word"
        if s.is_sahih_mahmoz_ain() \
                or s.is_sahih_mahmoz_lam() \
                or s.is_ajwaf_wawi_mahmoz_lam() :
            return fial.replace(ALEF_HAMZA_ABOVE,YEH_HAMZA)
        elif s.is_sahih_mahmoz_faLam() \
                or s.is_ajwaf_wawi_2hamza()\
                or s.is_ajwaf_yeh_mahmoz_lam()\
                or s.is_lafif_mafrok_w_h_y()\
                or s.is_lafif_mafrok_w_y():
            return None
        elif s.is_ajwaf_waw() \
                or s.is_sahih_salim()\
                or s.is_sahih_mahmoz_fa()\
                or s.is_ajwaf_waw_mahmoz_fa()\
                or s.is_ajwaf_yeh()\
                or s.is_ajwaf_yeh_mahmoz_fa()\
                or s.is_lafif_mafrok_y_y()\
                or s.is_lafif_makron_2yah():
            return fial
        elif s.is_lafif_makron_2waw():
            return fial.replace(w[4:],YEH +FATHA)
        else:
            return 'this test nt fial'

    elif w[3] == DAMMA:
        return 'hi Tamer is in DAMMA',w
    else:
        return 'Plase Tamer Chakil Elfiall',w


t= WazenFaall(tt).split_space_w_tachkil

print(strip_ila(t(FATHA,FATHA,FATHA)))

end=time.time()
tim= end - start
print(tim)
print(f,c)



KAS= {
 "1": "",
 "2": "",
 "3": "",
 "4": "",
 "5": "",
 "6": "",
 "7": "",
 "8": "",
 "9": "",
 "10": "",
 "11": "",
 "12": "",
 "13": "is_lafif_makron_2yeh_mahmoz",
 "14": "is_lafif_makron_h_w_y",
 "15": "is_lafif_makron_w_ain_y_lam",
 "16": "is_lafif_makron_w_fa_y_ain",
 "17": "is_lafif_makron_y_w",
 "18": "is_methal_wawi",
 "19": "is_methal_wawi_mahmoz_ain",
 "20": "is_methal_wawi_mahmoz_lam",
 "21": "is_methal_wawi_modaf",
 "22": "is_methal_yeh",
 "23": "is_methal_yeh_mahmoz_ain",
 "24": "is_methal_yeh_modaf",
 "25": "is_naks_waw",
 "26": "is_naks_waw_mahmoz_ain",
 "27": "is_naks_wawi_mahmoz_fa",
 "28": "is_naks_yeh",
 "29": "is_naks_yeh_mahmoz_ain",
 "30": "is_naks_yeh_mahmoz_fa",
 "31": "",
 "32": "",
 "33": "",
 "34": "is_sahih_mahmoz_fa_modaf",
 "35": "",
 "36": "is_sahih_salem_modaf_ainlam",
 "37": "is_sahih_salem_modaf_faAin",
 "38": ""
}
h= {
 "": 0,
 "": 1,
 "": 2,
 "": 3,
 "": 4,
 "": 5,
 "": 6,
 "": 7,
 "": 8,
 "": 9,
 "": 10,
 "": 11,
 "": 12,
 "": 13,
 "": 14,
 "": 15,
 "": 16,
 "": 17,
 "": 18,
 "": 19,
 "": 20,
 "": 21,
 "": 22,
 "": 23,
 "": 24,
 "": 25,
 "": 26,
 "": 27,
 "": 28,
 "": 29,
 "is_sahih_mahmoz_ain": 30,
 "is_sahih_mahmoz_fa": 31,
 "is_sahih_mahmoz_faLam": 32,
 "": 33,
 "is_sahih_mahmoz_lam": 34,
 "": 35,
 "": 36,
 "is_sahih_salim": 37
}

































#
# class moaljaFaal(isShihOrMoatal):
#     """
#     توليد الفعل من الجذر
#     """
#
#     def __init__(self , jader , faall):
#         self.jader = jader
#         self.faall = faall
#
#         isShihOrMoatal.__init__ ( self , self.jader  )
#
#     def split_space_w_tachkil(self , *args):  # حذف الفراغات من الجذر وتشكيله ليصبح فعل
#         lst = [ ]
#         for x in self.jader.split ():
#             lst.append ( x + args [ len ( lst ) ] )
#
#         return ''.join ( lst )
#
#     def hamza_il_alif_hamza(self):  # قلب الهمزة الى همزة قطع
#         if HAMZA in moaljaFaal.split_space_w_tachkil():
#             return self.faall.replace ( HAMZA , ALEF_HAMZA_ABOVE )
#         else:
#             return self.faall
#
#     def faal_modaaf(self , chakl=FATHA):  # الفعل المضعف
#         if self.faall [ 2 ] == self.faall [ 4 ] and (self.faall [ 2 ] != ALEF_HAMZA_ABOVE and self.faall [ 4 ] != ALEF_HAMZA_ABOVE):
#             return self.faall [ 0:3 ] + SHADDA + chakl
#         elif self.faall [ 0 ] == self.faall [ 2 ] and (
#                 self.faall [ 0 ] != ALEF_HAMZA_ABOVE and self.faall [ 2 ] != ALEF_HAMZA_ABOVE):
#             return self.faall [ 0 ] + SHADDA + chakl + self.faall [ 4:6 ]
#         elif self [ 0 ] == ALEF_HAMZA_ABOVE and self [ 2 ] == ALEF_HAMZA_ABOVE:
#             return ALEF_MADDA + self [ 4 ] + chakl
#         elif self.faall [ 2 ] == ALEF_HAMZA_ABOVE and self.faall [ 4 ] == ALEF_HAMZA_ABOVE:
#             return self.faall [ 0:1 ] + chakl + ALEF_MADDA
#         else:
#             return self.faall
#
#     def faal_moatal(self , chakl=FATHA):  # الفعل المعتل
#         if self.faall [ 0 ] == ALEF_HAMZA_ABOVE and self.faall [ 2 ] == YEH:
#             return ALEF_MADDA + self.faall [ 4 ] + chakl
#         elif self.faall [ 0 ] == ALEF_HAMZA_ABOVE and self.faall [ 2 ] == WAW:
#             return ALEF_MADDA + self [ 4 ] + chakl
#         elif self.faall [ 2 ] == WAW and self.faall [ 4 ] == ALEF_HAMZA_ABOVE:
#             return self [ 0 ] + FATHA + ALEF + HAMZA + chakl
#         elif self.faall [ 2 ] == YEH and self.faall [ 4 ] == ALEF_HAMZA_ABOVE:
#             return self [ 0 ] + FATHA + ALEF + HAMZA + chakl
#         elif self.faall [ 2 ] == ALEF_HAMZA_ABOVE and self.faall [ 4 ] == YEH:
#             return self.faall [ 0 ] + FATHA + ALEF_HAMZA_ABOVE + chakl + ALEF_MAKSURA
#         elif self.faall [ 2 ] == ALEF_HAMZA_ABOVE and self.faall [ 4 ] == WAW:
#             return self.faall [ 0 ] + FATHA + ALEF_HAMZA_ABOVE + chakl + ALEF_MAKSURA
#         elif self.faall [ 4 ] == WAW:
#             return self.faall [ 0 ] + FATHA  + self.faall [ 2 ]+ chakl+ ALEF
#         elif self.faall [ 4 ] == YEH:
#             return self.faall [ 0 ] + FATHA  + self.faall [ 2 ]+ chakl+ ALEF_MAKSURA
#         else:
#             return self.faall