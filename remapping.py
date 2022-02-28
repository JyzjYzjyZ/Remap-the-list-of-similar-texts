import copy
import gc
import re
import warnings
import Levenshtein
# conda install python-Levenshtein
'''
author:goodjin5
release:1.0
date:Feb 28 ,2022
'''

sentences1 = ['DO YOU WANT TO SCULTIMATING CREATURES CHARACTERS BROPS ENVIRONMENTS BUTDONNO WORK TO START',
             'IF THAT IS THE CASE AND I WELCOME YOU TO NEXT SUTS COMPLETE GUIDE TO SEBURGH TWENTY TWENTY TWO',
             "MY NAME IS HABRAHAM LEOK I HAVE ELEVEN YEARS OF EXPERIENCE IN THE THREE DY INDUSTRY AND I'VE BEEN TEACHING FOR THE PAST SEVEN YEARS I ALSO MANAGE MY OWN INDUSTO DO HERE IN E",
             'AND NIGHT WILL BE YOUR INSTRUCTOR THROUGHOUT THIS COURSE',
             'IN THIS COURSE WE WILL BECOVERI OF THE MOST IMPORTANT ASPECTS INCIDE OF CEBER',
             'I WILL BE SHOWING YOU DIFFERENT WAYS IN WHICH YOU CAN START YOUR PROJECTS AND BRING TO LIFE ALL OF THE AMAZING THINGS THAT LIVE INSIDE YOUR IMAGINATIO',
             'THROUGHOUT THISCOURSE WE WILL BE LEARNING ABOUT THE PRINCIPLES OF SKOLTY',
             'DYE IN THE MASH SEIZE FEARS HART SURFICE TOOL BOLLY PAIN RENDERING AND MUCH MORE',
             'THIS COURSE IS DIVIDED INTO TEN CHAPTERS EACH CHAPTER WILL DEVELOP ONE PROJECT THAT WILL KEET USE SPECIFIC TOOLS ABOUT THE PIPE',
             'AT THE END OF ALL OF THIS ORCES YOU FLL BE ABLE TO CREATE ANYTHING THAT YOU CAN IMAGINE CORDISONINGS',
             'I HAVE THE SIGNED THIS COURSE FOR A BEGINNER LEVEL STUDENTS WHO WANT TO START THEIR CAREER INSIDE THE SEBER SHOPWAR',
             'AND THE ONLY THING YOU NEED IS TO HAVE A PEN TABLET TO WORK', 'SAID TO BE VERY IMPORT',
             "MAKE SURE TO HAVE SEGERSH TWENTY TUNS TOIS WOE AND DELAY THIS UPLAF AND YOU'LL YOUR BREADTH TO GO",
             'JOIN ME AND STARGRADING AMAZING SCULPTORS WITH TIVRISH TWENTY TWENTY TO']
punctuate1 =  "DO YOU WANT TO SCULTIMACING CREATURES, CHARACTERS, PROPS AND VIROMENTS BUT DONE NO WORK TO START? IF THAT IS THE CASE, AND I WELCOME YOU TO NEXTUDS. COMPLETE GUIDE TO SEBURSH. TWENTY TWENTY TWO. MY NAME IS ABRAHAMLYOK. I HAVE ELEVEN YEARS OF EXPERIENCS IN THE THREETY INDUSTRY AND I'VE BEEN TEACHING FOR THE PAST SEVEN YEARS. I ALSO MANAGE MY OWN EASE TO YOU HERE IN MEXICA AND I WILL BE YOUR INSTRUCTOR THROUGHOUT THIS COURSE. IN THIS COURSE, WE WIL BE COVERING OLL TDHE MOST IMPORTANT ASPECTS INSIDE OF SEBURSH. I WILL BE SHOWING YOU DIFFERENT WAYS IN WHICH YOU CAN START YOUR PROJECTS AND BRENG TO LIKE ALL OF THE AMAZING THINGS THAT LIT IN SITE YOUR IMAGINATION. THROUGHOUT THIS COURSE, WE WILL BE LEARNING ABOUT THE PRINCIPLES OF SCULTING: DIINAMASH, SEES, PHERS, PARTURE OF THE STOOL, POLLY PAIN, RENDERING AND MARCH MORE. THIS COURSE IS DIVIDED INTO TEN CHAPTERS. EACH CHAPTER WILL DEVELOP WANT PROJECT THAT WILL BE USE SPECIFIC TOOLS ABOUT THE PILETAT. THE END OF ALL THIS COURSES, YOU WILL BE ABLE TO CREATE ANYTHING T YOU CAN IMAGINE FOR THE NANSTREI. HAVE THE SIGNED THIS COURSE FOR BEGINNER LEVEL STUDENTS WHO WANT TO START THEIR CAREER IN SIDTE OF THE SEBURS STOPWIRT, AND THE ONLY THING YOU NEED IS TO HAVING PEN PABLET TO COURT, AS CAN BE VERY IMPORTANTMAKE. SURE TO HAVE SEBURSH TWENTY TWO INPOL AS WELLIN THE LATE, THE SUPLI, AND YOU'LL GO REGT TO GO JOIN ME AND START GRATING AMAZING SCULPTORS WITH SEBURSH TWENTY TWENTY TWO."


sentences2 = ['GEISON WILL COME TO THE NEXT PART OF THE SERIES TO DHO WORK I BE TALKING ABOUT THE INTRFACE AND BELIEVE ME IT IS A TRICKER ONE SO', 'WELCOME TO THE INTERFASE SEMERS IS FAMOUS FOR HAVING ONE OF IVNOT THE WORST INTERFACES INTO TRETY WORLD', 'AND ONE OF THE RECENCES THE GUISE THAT INITIALLY BUILT CIBERT THEY WERE NOT USED LIKE INTERPHASE THE SIGNERS THEY WERE JUST PROGRAMMERS WRITE SO', "THEY TRIED THEIR BEST AND THEY CREATED THIS WHICH IS NOT BAD IT'S NOT BAD BUT IT GETS A LITTLE BIT CONFUSING SO", 'THE SCHOOL']
punctuate2 = "M GUIS, AN WELCOME TO THE NEXT PART OF THE SERIES. TO DAY, WORKANA BE TALKING ABOUT THE INTERFHACE AND, BELIEVE ME, IT IS A TRICKY ONE. SO AWELCOME TO THE INTERFHASE. SEBERS IS FAMOUS FOR HAVING ONE OF IFNOT THE WORST INTERFHACES INTHO TREEDY WORLD AND ONE OF THE RECENCIS THAT THE GUISE TAD INITIALLY BUILT SEBER. THEY WERE NOT USED, LIKE INTERFHASE A SIGNERS. THEY WERE JUST PROGRAMMERS WRITE. SO THEY TRIED THEIR BEST AND THEY CREATED THIS, WHICH ITS NOT BAD. IT'S NOT BAD BUT IT GETS A LITTLE BIT CONFUSING. SO LET'S GO."
#这里可以完善参数-要查
#这里可以完善参数。。
#sentences需要添加内容，在初始化前[现在不需要了]
# 搜索debug删除内容

def Init(sentences,punctuate):
    def Transfrom(sentences,punctuate):
        sentences = str(sentences)[2:-2]
        sentences = sentences.replace(', ',',').replace(",",'<,>')\
            .replace("'<",'<').replace(">'",'>').replace('"<','<').replace('>"','>')
        punctuate = punctuate.replace('.','<.>').replace('?','<?>')\
            .replace(':','<?>').replace(',','<,>').replace('-','<->').replace('> ','>')

        sentences = sentences.replace('<',' <').replace('>','> ')
        punctuate = punctuate.replace('<',' <').replace('>','> ')
        #----------------------------------------------
        return [sentences,punctuate]
    sp = Transfrom(sentences,punctuate)

    def ToArr(str):
        arr = str.split(' ')
        while '' in arr:
            arr.remove('')
        return arr

    sp[0] = ToArr(sp[0])
    sp[1] = ToArr(sp[1])
    return sp
# ------------------------------------------------
def  assignment(list,sentences,punctuate,dic):
    psd = dic["P_sourceDecode"]
    res = []
    for c in list:
        r = psd[c[0]:c[-1]+1]
        rr = ''
        for v in r:
            rr = rr+v
        res.append(rr)
    if len(dic["S_sourceDecode"]) != len(res):
        warnings.warn((str(len(dic["S_sourceDecode"]) - len(res)) +"element was lost in the remapping process"))
    return res
# ------------------------------------------------
def FindSame(sp,func,debugBool=False):
    SP = sp.copy()
    sentences = sp[0]
    punctuate = sp[1]

    '''
        debug作图用
    '''
    if debugBool:
        xArr = []
        yPArr = []
        ySArr  = []
        yTrueArr = []


    pi = 0
    dictIndex = 0
    dic = {}
    while pi < len(punctuate):
        p = punctuate[pi]
        if p in sentences:
            '''
                找到了相同元素，但是目前不知道顺序是否正确
                si => 相同元素在s中的索引位置
                pi =>相同元素在p中的索引位置
                
                若位置不正确，pi => +
                           si后小于si前，1，3，2，5 ==> 在错误位置填充|，后continue
                           si后大大于前  1，3，20 ==>  si后-si前   pi后-pi前
            '''
            if p[0] == '<' and p[-1] == '>':
                pi +=1
                continue
            # 找到了符合要求的
            si = sentences.index(p)
            '''
                确定元素的顺序是否正确
            '''
            if dictIndex > 0:
                # 字典中至少有一对si  pi
                di_old = str(dictIndex-1)
                si_old = dic[di_old]['s']
                pi_old = dic[di_old]['p']
                if si < si_old:
                    # 靠前了
                    #错误的位置填充，p不填充
                    #pi不变，p不变，已查找和p相同的后续元素
                    sentences[si] = "|" + sentences[si]
                    continue
                if si > si_old:
                    #大于的情况默认是可行的，但若匹配到很远的地方也是错误的
                    si_dis = abs(si-si_old)
                    pi_dis = abs(pi-pi_old)
                    #不需要在后面填充的，只需要跳过错误项
                    '''
                        确定出错的容差值
                        最多三单词的距离识别
                        10 - 3
                        20 - 4
                        2 - 1
                        f(x)=x^0.5  {ground+1}
                    '''
                    #-----------------------------------
                    avg_dis = (si_dis+pi_dis)*0.5

                    si_re_dis = si_dis/len(sentences)*1000
                    pi_re_dis = pi_dis/len(punctuate)*1000
                    #需要测试。。
                    #当然，对于此视频。加20是非常合适的值
                    max_dis = func(pi_re_dis)
                    if debugBool:
                        xArr.append(dictIndex)
                        ySArr.append(si_re_dis)
                        yPArr.append(pi_re_dis)
                        yTrueArr.append(max_dis)
                    #这里可以完善参数
                    # if pi == 100:
                    #     print('s')
                    '''
                        此方法会随着句子长度的增加渐渐失去作用。。。。
                        考虑调整函数或分割句子
                    '''

                    if si_re_dis > max_dis and max_dis != -1:
                        #这个单词我不看了
                        if debugBool:
                            print('warn:  '+'  pi:  '+  str(pi)  +'  si:  '+  str(si)+'  word:  '+str(p) )
                        pi += 1
                        continue
            # ==============================================================================

            '''
                写入+排除已经找+找pi对应的si
            '''
            sentences[si] = "|"+sentences[si]
            punctuate[pi] = "|" + punctuate[pi]
            dic[str(dictIndex)] = {}
            dic[str(dictIndex)]['s'] = si
            dic[str(dictIndex)]['p'] = pi
            dic[str(dictIndex)]['w'] = p
            dictIndex += 1

        pi +=1
    # ====到此为止，循环结束咯=====================================================================
    if debugBool:
        arr = [xArr,ySArr,yPArr,yTrueArr]
        import matplotlib.pyplot as plt
        plt.plot(arr[0], arr[1], color='r')
        plt.plot(arr[0], arr[2], color='b')
        plt.plot(arr[0],arr[3],linestyle='dashed',color='g')
        plt.text(2,100,'blue:P\nred:S\ngreen:baseline\ndel S\nNum:'+str(len(xArr))+'\nmax:'+str(max(ySArr)))
        plt.show()

    return dic
# ------------------------------------------------
def decode(sn):
    srr = sn[0]
    prr = sn[1]

    scon = ''
    pcon = ''
    sres = []
    pres = []
    for s in srr:
        if s[0] == '<' and s[-1] == '>' and s[1] == ',':
            sres.append(scon[:-1])
            scon = ''
            continue
        scon = scon + s + ' '
    sres.append(scon)

    for p in prr:
        if p[0] == '<' and p[-1] == '>':
            sign = p[1:-1]
            pres.append(pcon[:-1] + sign)
            pcon = ''
            continue
        pcon = pcon + p + ' '
    if pres[-1] != pcon and pcon != '':
        pres.append(pcon)

    del pcon, scon, sign, s, p, sn;
    gc.collect()

    return [sres, pres]
# ------------------------------------------------
def FindClamp(sp_decode,index):
    lis = sp_decode[index]
    res = []
    resi = []
    resi_m = []
    for c in lis:
        i = re.findall(r"\|+\d+\|",c)
        for ci in range(len(i)):
            start_ = c.find(i[ci])
            arr = [start_,start_+(len(i[ci])) -1 ]
            resi_m.append(arr)

            i[ci] = str(i[ci])[1:-1]
        res.append(i)
        resi.append(resi_m)
        resi_m = []

    # 若s中有空，空在首尾
    # 在main中执行元素。。
    return [res,resi]
# ------------------------------------------------
def GradientList(list):
    s = list[0]
    e = list[-1]
    if s == e:
        return [e]

    res = [s]
    while res[-1] != e:
        s+=1
        res.append(s)
    return res
# ------------------------------------------------
def remappingFirst(indexDict):
    d = indexDict.copy()
    del indexDict;gc.collect()
    ssi = d['S_signIndex']
    psi = d["P_signIndex"]
    '''
        需求根据索引重映射

        获得数组，头尾距离有效索引的位置

        对于头不确定，看尾
        对于尾不确定看头

        若两边都未知
        看句子长度
        看单词相似度

        对于任意句，开头即前句的结尾+1

        理论序号，第一个和最后一个
        确定理论序号等于实际序号。查看开头结尾是否符合
    '''
    print('remappingStart!')

    for test in ssi:
        if test == []:
            raise Exception(print("your source have an empty list"))

    firstRemap = [0 for x in range(0,len(ssi))]
    i_c = 0
    for c in ssi:
        #若c中无元素直接报错
        start = c[0]
        end = c[-1]

        start_in_p = []
        end_in_p = []
        i = 0
        for p in psi:
            if start in p:
                start_in_p_sub = p.index(start)
                start_in_p = [i,start_in_p_sub]
            if end in p:
                end_in_p_sub = p.index(end)
                end_in_p = [i,end_in_p_sub]
                break
            i +=1
            #获得了哪句在p中的位置
        if start_in_p == [] or end_in_p == []:
            raise Exception(print("cant find signIndex"))
        #是否完全对应
        if start_in_p[1] == 0 and psi[end_in_p[0]][-1] == end:
            firstRemap[i_c] = [start_in_p[0],end_in_p[0]]
        i_c += 1
    pass
    del end_in_p,end_in_p_sub,end,start,start_in_p_sub,start_in_p,i,i_c,p,c;gc.collect()
    print('fisrt remapping over!')
    #得到所有含0的索引的数组
    #为了解决首尾没有完全匹配的问题
    i = 0
    zero_list = []
    while i + 1 < len(firstRemap):
        c = firstRemap[i]
        if c == 0:
            list_ = []
            while firstRemap[i] == 0:
                list_.append(i)
                if i+1 == len(firstRemap):
                    break
                i += 1
            zero_list.append(list_)
        i+=1
    #找到所有孤立的0了   【【2，3】【9，10，11】【13，14】】
    zero_list_in_S_first = zero_list.copy()
    del c,i,list_,test,zero_list;gc.collect()
    print('Get zero list for s')
    zero_list_in_P_first = []
    for c in zero_list_in_S_first:
        start = -1
        end = -1

        if c[0] == 0:
            start = 0
        else:
            start = firstRemap[c[0]-1][1] + 1

        if c[1] == len(firstRemap)-1:
            end = len(psi)-1
        else:
            end = firstRemap[c[-1]+1][0]-1

        zero_list_in_P_first.append([start,end])
    print('Get zero list for p')
    if len(zero_list_in_S_first) != len(zero_list_in_P_first):
        raise Exception(print("your len of list is not same"))
    zero_list_sp = []
    for i in range(len(zero_list_in_S_first)):
        s = zero_list_in_S_first[i]
        p = zero_list_in_P_first[i]
        zero_list_sp.append([s,p])
    del c,end,i,p,s,start,zero_list_in_S_first,zero_list_in_P_first;gc.collect()
    print("Combine zero list _s and _p")
    return [firstRemap,zero_list_sp]
# ------------------------------------------------
def remappingSecondd(indexDict,firstZeroList):
    print("start Second for remapping")
    '''
       得到[2，3]_s   [7,9]_p
       对其运算得到 2：【p，p】  3：【p，p】
    '''
    ssi = indexDict['S_signIndex']
    psi = indexDict['P_signIndex']
    psi_b = copy.deepcopy(psi)
    first = firstZeroList[1]
    res = []
    mainList = firstZeroList[0]

    def distance(seq1,seq2):
        '''
            需要数组类型的句子，形如
            【25，26，28，29，30，31】
            【25，26，28，30，31】

            可以按照相似元素的出现次数或者百分比输出，这里输出百分比。分母为s
            故将self_放到seq1的位置，up或down放第二句
        '''
        adder = 0
        if seq1 == seq2:
            warnings.warn('这很奇怪，你的数组中有相同元素。相同元素应该在之前的方法中去除。【有小概率会影响输出结果】')
            return 1
        for c in seq1:
            if c in seq2:
                seq2.remove(c)
                adder+=1
        r = adder/len(seq2)
        return r


    for c in first:
        s_ = c[0]
        p_ = c[1]
        s = ssi[  s_[0]:s_[-1]+1 ]
        p = psi[    p_[0]:p_[-1]+1   ]
        # 对于s的开始和结尾写入p的开始和结尾
        rs = [[] for x in range(0,len(s))]
        rs[0] = p[0]
        rs[-1] = p[-1]
        p[0] = 0
        p[-1] = len(s)-1
        # p中剩下的元素必在中间
        # 检测
        n_int_num = 0
        for x in p:
            if type(x) == int:
                n_int_num += 1
        if n_int_num == len(p):
            print("all Num in p")
            res.append(rs)
            continue
        # 若p中有未归类的非空列表
        i_no_ord_in_p = 0
        a_no_ord_in_p = []
        for no_ord in p:
            if type(no_ord) == list:
                if no_ord != []:
                    a_no_ord_in_p.append(i_no_ord_in_p)
            i_no_ord_in_p+=1
        #对于非空列表进行匹配
        del c, x, i_no_ord_in_p, n_int_num, no_ord, p_, s_;gc.collect()
        # print("Matching non-empty lists")

        def loopMatch(a_no_ord_in_p,s,p,rs):
            #在 a_no中找到
            #若a_no中只有一个元素，可能不行
            one = a_no_ord_in_p[0]
            two = a_no_ord_in_p[-1]
            o_up = s[p[one - 1]]
            o_down = s[p[one - 1] +1 ]
            t_down = s[p[two+1]]
            t_up = s[p[two+1] - 1]

            one_self_ = p[one]
            two_self_ = p[two]

            o_up_w = distance(one_self_,o_up)
            o_down_w = distance(one_self_,o_down)
            if o_up_w>o_down_w:
                for p__ in p[one]:
                    rs[  p[one - 1]  ].append(p__)
                p[one] = p[one-1]
            else:
                for p__ in p[one]:
                    rs[  p[one - 1]+1  ].append(p__)
                p[one] = p[one - 1]+1

            if one == two:
                a_no_ord_in_p.remove(one)
                # 现在a_no 中没有元素
                # p rs a 已更改，接下来返回
                return [a_no_ord_in_p, rs, p]

            t_up_w =distance(two_self_,t_up)
            t_down_w = distance(two_self_,t_down)
            if t_up_w>t_down_w:
                for p__ in p[two]:
                    rs[  p[two+1] -1  ].append(p__)
                p[two] = p[two+1] -1
            else:
                print(p[two])
                for p__ in p[two]:
                    rs[  p[two+1]  ].append(p__)
                p[two] = p[two+1]
            a_no_ord_in_p = a_no_ord_in_p[1:-1]

            #------------对于rs的每一个执行排序------rs中的数组，意味着p中的句子的序列号----------------
            # 但不是现在
            return [a_no_ord_in_p,rs,p]

        while a_no_ord_in_p != []:
            # 剩余数量为2k+n的情况，缺少数量为1的情况
            loopmatch = loopMatch(a_no_ord_in_p,s,p,rs)
            a_no_ord_in_p = loopmatch[0]
            rs = loopmatch[1]
            p = loopmatch[2]

        '''
            如上，loopMatch函数有易于解决的代码重复问题
            而且百分比相等的情况也没有得到很好的解决
            
            诉求
            定义一个范围函数，对结果百分比近似的进行处理
        '''
        res.append(rs)
        res_ = copy.deepcopy(res)
        for v in range(len(res_)):
            vv = res[v]
            for b in range(len(vv)):
                bb = vv[b]
                bb = list(map(int,bb))
                nn = sorted(bb)
                mm = list(map(str,nn))
                res_[v][b] = mm
            pass
        res = res_


    # del a_no_ord_in_p, down, down_w, up_w, up, n_int_num, no_ord, self_, x, s_, p_, i_in_p_, i_no_ord_in_p, p__, c,rs;
    # gc.collect()
    print("second no empty list is in order!")
    # 需要进行对res的内容：sign=>index_p的转换
    def transfromRes(res, psi):
        def GetIndex_in_psi(x):
            i = 0
            # 找到当前元素在psi中的索引
            for c in psi:
                if x in c:
                    return i
                i += 1

        res_b = []
        for c in res:
            res_m = []
            res_b_sub = []
            for c_sub in c:
                res_b_sub = [GetIndex_in_psi(c_sub[0]), GetIndex_in_psi(c_sub[-1])]
                res_m.append(res_b_sub)
            res_b.append(res_m)
        return res_b

    res_b = transfromRes(res, psi_b)

    print("transform Res")

    def addRes(first, mainList, res):
        f = []
        for f_ in first:
            f.append(f_[0])
        i = 0
        for c in f:
            if len(f[i]) != len(res[i]):
                raise Exception(print("your list len in err"))
            while len(f[i]) > 0:
                mainList[f[i][0]] = [res[i][0][0], res[i][0][-1]]
                f[i] = f[i][1:]
                res[i] = res[i][1:]
            i += 1
        return mainList

    mainList = addRes(first, mainList, res_b)
    del psi, psi_b, s, ssi, p, firstZeroList, first;
    gc.collect()
    return mainList
# ------------------------------------------------
def GetNoSame(dic,sp):
    srr = sp[0]
    prr = sp[1]

    sirr = list(range(len(srr)))
    pirr = list(range(len(prr)))

    dicirr_s = []
    dicirr_p = []
    for c in dic:
        dicirr_s.append(dic[c]['s'])
        dicirr_p.append(dic[c]['p'])

    for c in dicirr_s:
        sirr.remove(c)
    for c in dicirr_p:
        pirr.remove(c)
    del c,dicirr_s,dicirr_p;gc.collect()
    #----------到这里为止，找到了所有p s 中不相同的元素的序列号------------------------
    s_sign = []
    p_sign = []
    si = 0
    # 这里最后一个逗号分隔符是无效的，对于最后一个，添加-(len()+0)
    for s in srr:
        if s[0] == '<' and s[-1] == '>' and s[1] == ',':
            s_sign.append(si)
        si+=1
    # s_sign.append(  (len(srr)+0) )
    pi = 0
    for p in prr:
        if p[0] == '<' and p[-1] == '>':
            p_sign.append(pi)
        pi += 1
    del pi,si,p,s,dic,prr,srr;gc.collect()
    #----------------到这里为止，找到标点索引的工作已经全部完成----------------------
    def splitBySignIndex(irr,sign):
        i = irr.index(sign)
        irr_A = irr[:i]
        irr_B = irr[i+1:]
        return [irr_A,irr_B]
    res_Sirr = []
    res_Pirr = []
    # s中的最后一个是没有，的所以
    for s_sig in s_sign:
        arr = splitBySignIndex(sirr,s_sig)
        res_Sirr.append(arr[0])
        sirr = arr[1]
    res_Sirr.append(sirr)
    for p_sig in p_sign:
        arr  =splitBySignIndex(pirr,p_sig)
        res_Pirr.append(arr[0])
        pirr = arr[1]
    return [res_Sirr,res_Pirr]
# ------------------------------------------------
def MatchEmptyList(second,dic):
    '''
        速成的可以简单归一的方法
        到这里为止，需要signIndex的步骤已经基本完成
        注：此时second中的sign已经全部转换为P-index
    '''
    def Noun():
        rem = -10
        distance = []
        for c in second:
            for c_sub in c:
                if rem > c_sub:
                    raise Exception(print("your index is wrong"))
                else:
                    # 10 2 正确 x 正确
                    distance.append(abs(rem - c_sub) - 1)
                    rem = c_sub
        noun = distance[2::2]
        return noun

    def add_IsRmpyt(list):
        l = copy.deepcopy(list)
        ie = dic['isEmpty']
        res = [-1 for x in range(len(ie))]
        i = 0
        for c in ie:
            if c ==1:
                res[i] = l[0]
                l = l[1:]
            i+= 1
        return res

    _second_ = add_IsRmpyt(second)
    #----------作为-1加入了空列表-----------------
    #对于头和尾的空集识别失败,加入头尾
    if _second_[0] == -1:
        if 0 in _second_[1]:
            _second_[1].remove(0)
        _second_[0] = [0]

    if _second_[-1] == -1:
        least_index_p = len(dic['P_signIndex'])-1
        if least_index_p in _second_[-2]:
            _second_[-2].remove(least_index_p)
        _second_[-1] = [least_index_p]


    for c in  _second_:
        if -1 in c:
            warnings.warn('-1 in your "secondList"  在中间')
    print("Preparing to match")
    '''
        如果_second_的中间出现了空集
        对于单个中间的空集
        
        找到p的集合
        找权重最小
    '''
    #debug
    # _second_ = [[0], [1, 3], [], [], [14]]
    '''
        找岛
        岛中数字为_second_空集的索引
    '''
    oi = 0
    island = []
    while oi < len(_second_):
        o = _second_[oi]
        if o ==[]:
            island_sub = []
            while _second_[oi] == []:
                island_sub.append(oi)
                oi+=1
                if oi >= len(_second_):
                    break
            island.append(island_sub)
        oi+=1
    '''
        识岛
        通过——second_  p
        start ==> _second_index
        f_start ==> p_index
        
        island of p 中的数子代表p-index中的索引
        island of p 与 island匹配
    '''
    island_for_p = []
    for p in island:
        start = p[0]
        end = p[-1]
        if start == 0:
            f_start = 0
        else:
            f_start = _second_[start-1][-1]+1

        if end == len(_second_)-1:
            b_end = len(dic['P_signIndex'])-1
        else:
            b_end = _second_[end+1][0]-1
        k= [f_start,b_end]
        island_for_p.append(k)

    if len(island) != len(island_for_p):
        raise Exception('the len is different  -island -island of p')
    ji = 0
    for j in _second_:
        if len(j) == 1:
            if type(j) == list:
                j = int(j[0])
            _second_[ji] = [int(j),int(j)]
        ji+= 1
    return [_second_,island,island_for_p]
# ------------------------------------------------
def FindEndPoint(second,dic):
    psdecode = dic['P_sourceDecode']
    def Noun(second):
        rem = -10
        distance = []
        for c in second:
            for c_sub in c:
                if rem > c_sub:
                    raise Exception(print("your index is wrong"))
                else:
                    # 10 2 正确 x 正确
                    distance.append(abs(rem - c_sub) - 1)
                    rem = c_sub
        noun = distance[2::2]
        return noun

    noun = Noun(second)
    '''
        second 中的数字表示p-signindex中的索引
        故，a中的数字代表p中有几个没有被配对的元素
    '''
    i = -1
    for c in noun:
        i+=1
        if int(c) > 0:
            f_start = second[i][-1]
            if c == 1:
                arr = [f_start+1]
            else:
                arr = [f_start+1,f_start+c]
            attribution = []
            # 由于noun比psd少1，故i+1永远成立
            one = psdecode[i]
            two = psdecode[i+1]
            arr_index = []
            '''
            于arr对应。数字表示second的index即s，第几句
            '''
            for a in arr:
                one_w = Levenshtein.distance(one,psdecode[a])
                two_w = Levenshtein.distance(two,psdecode[a])
                if one_w >= two_w:
                    arr_index.append(i)
                else:
                    arr_index.append(i+1)
                try:
                    if arr_index[-2] == i+1:
                        # 若识别出来了一个句子属于第二句。则将以后的所有句子归类为第二句
                        arr_index[-1] == i+1
                except:pass

            bi = -1
            for b in arr_index:
                bi += 1
                second[b].append(int(arr[bi]))

            ni = -1
            for n in second:
                ni+=1
                nn = sorted(n)
                second[ni] = [nn[0],nn[-1]]

    su =  sum(Noun(second))
    if su !=0:
        warnings.warn(str(su)+"element was lost in the remapping process")
    pass

    return second
# ------------------------------------------------
def SignSame(sp,dic):
    sentences = sp[0]
    punctuate = sp[1]
    i = 0

    arr = list(range(len(dic)))
    for ai in range(len(arr)):
        arr[ai] = "|"

    for d_key in dic:
        d = dic[d_key]
        d_si = d['s']
        d_pi = d['p']
        arr[i] = sentences[d_si]
        sentences[d_si] =  "|"+str(i)+"|"+sentences[d_si]
        punctuate[d_pi] =  "|"+str(i)+"|"+punctuate[d_pi]
        i +=1
    return [sentences,punctuate,arr]
# ------------------------------------------------
def RequireSSi_emptyList(indexList_0):
    i = 0
    res = [1  for x in range(len(indexList_0))]
    for c in indexList_0:
        if c == []:
            res[i] = 0
        i+=1
    while [] in indexList_0:
        indexList_0.remove([])
    return [indexList_0,res]
# ------------------------------------------------
def  Main(sentences,punctuate,func,debugBool=False):
    if debugBool:
        print("如果出现下标越界的错误，说明你输入的语言质量实在离谱")
    sp =  Init(sentences,punctuate)
    s = sp[0].copy()
    p = sp[1].copy()
    sp_b = [s,p]
    sp_ba = []
    sp_ba.append(sp_b[0].copy())
    sp_ba.append(sp_b[1].copy())
    #-------deepcopy-------
    dic = FindSame(sp=sp,debugBool=debugBool,func=func)
    ns = GetNoSame(dic,sp_b.copy())
    sn = SignSame(sp_b,dic)
    indexList = ['','','']
    indexList[2] = sn[2]
    # print(sn[0], '\n', sn[1])
    #解码
    # sn为分开的
    sp_decode = decode(sn)
    sourceDecode = decode(sp_ba)
    del s,p,sp,sp_b,dic,sn;gc.collect()
    # 在此处，若句子没有相同的匹配元素则为空，会报错
    indexList[0] = FindClamp(sp_decode,0)[0]
    require= RequireSSi_emptyList(indexList[0])
    indexList[0] = require[0]
    is_empty = require[1]
    indexList[1] = FindClamp(sp_decode,1)[0]
    #进啥来啥，查找|d|并输出其在句中位置
    indexList.append( FindClamp(sp_decode,0)[1] )
    indexList.append( FindClamp(sp_decode,1)[1] )
    '''
        已经做的，配对【要调整max函数】
        编码
        
        需要做的
        句子根据序号映射
        
        目前有的indexList(3)
            sp_decode(2)
            
        需要输出的，p的index按序号排好的数组
        
        2.23
        indexList,用于映射句子的数组
        ns
    '''

    IndexDic = {
        'S_signIndex':indexList[0],
        'P_signIndex':indexList[1],
        'SameContect':indexList[2],
        'S_positionSign':indexList[3],
        'P_positionSign':indexList[4],
        'S_decode':sp_decode[0],
        'P_decode':sp_decode[1],
        'S_noSamePosition':ns[0],
        'P_noSamePosition':ns[1],
        'S_stringClip_sentences':sp_ba[0],
        'P_stringClip_punctuate':sp_ba[1],
        'isEmpty':is_empty,
        'S_sourceDecode':sourceDecode[0],
        'P_sourceDecode':sourceDecode[1],
    }
    IndexDic_b = copy.deepcopy(IndexDic)
    first = remappingFirst(IndexDic.copy())
    # [firstRemap,zero_list_sp]
    second = remappingSecondd(IndexDic_b, first)
    matchEmptylist = MatchEmptyList(second, IndexDic_b)
    second  = matchEmptylist[0]
    island = matchEmptylist[1]
    island_p = matchEmptylist[2]
    # matchEmpty.noun
    third = FindEndPoint(second,copy.deepcopy(IndexDic_b))

    u = assignment(third, sentences, punctuate, IndexDic_b)
    pass
    return u
#---------------------------------------------


def filters(float_c):
    res = float_c+16
    return res


u = Main(sentences2,punctuate2,filters,False)
print('=============================')
for c in u:
    print(c)
pass









