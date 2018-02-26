#-*- coding: utf-8 -*-
import random, time, requests, datetime
from pprint import pprint


people={1,2,5,10,8,3}
seqs=[]

def fill(var_k={'start':people, 'finish':set([]), 'pair': set([]), 'back':set([]), 'state':'start', 'seq':[], 'seqs':[]}):
    global seqs
    var={l:var_k[l] for l in var_k}

    if len(var['start'])==0 and var['state']=='finish':
        seqs+=[var['seq']]
        #print 'finish',' '*(30-len('finish')),  var['seq']
        #print 'finish',' '*(30-len('finish')),  'fin state: start:', var['start'], 'finish:', var['finish']
        #var['seq']=[]
        return()


    if var['state']=='start' and len(var['pair'])==0:
        for k in var['start']:
            for l in var['start']-set([k]):
                var['pair']=set([k]) | set([l])
                #print 'pair combining 1',' '*(30-len('pair combining 1')), 'from start:', var['start'], 'goes:', var['pair'], 'to finish:', var['finish']
                fill(var)
        return()


    if var['state']=='start' and len(var['pair'])==2:
        #print 'go',' '*(30-len('go')), 'goes:', var['pair']
        var['state']='finish'
        var['finish']=var['finish'] | var['pair']
        var['start']=var['start']-var['pair']
        var['seq']=var['seq']+[list(var['pair'])]
        var['pair']=set([])
        #print '----------------->',' '*(30-len('----------------->')), 'becmes: start:', var['start'], 'finish:', var['finish']
        fill(var)
        return()


    if len(var['back'])!=0:
        #print 'go back',' '*(30-len('go back')), 'goes back:', var['back']
        var['finish']=var['finish']-var['back']
        var['seq']=var['seq']+[var['back']]
        var['start']=var['start'] | var['back']
        var['state']='start'
        var['back']=set([])
        #print '----------------->',' '*(30-len('----------------->')), 'becomes: start:', var['start'], 'finish:', var['finish']
        fill(var)
        return()


    if len(var['start'])>0 and var['state']=='finish':
        for i in var['finish']:
            var['back']=set([i])
            #print 'choose back',' '*(30-len('choose back')), 'returns:', var['back']
            fill(var)
        #exit()
        return()
print time.asctime()
fill()
print time.asctime()

print len(seqs), type(seqs), seqs[0]
seqs={str(k):sum([max(l) if type(l)==list else sum(l) for l in k]) for k in seqs}
for k in sorted(seqs, key=seqs.__getitem__)[0:10]:
    print k, {k:seqs[k] for k in sorted(seqs, key=seqs.__getitem__)}[k]
