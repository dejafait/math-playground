old_floor,old_ceil=replay.floor_checked,replay.ceil_checked
old_times,old_over=replay.times,replay.over
old_enc,old_plus=replay.enclose,replay.plus
old_neg,old_clip,old_product=replay.opposite,replay.intersect,replay.product
def floor_checked(n,d):
    actual=old_floor(n,d)
    assert d>0 and actual==n//d and actual*d<=n<(actual+1)*d
    signed['floor']+=1
    return actual
def ceil_checked(n,d):
    actual=old_ceil(n,d)
    assert d>0 and actual==-((-n)//d) and (actual-1)*d<n<=actual*d
    signed['ceiling']+=1
    return actual
def times(a,b):
    actual=old_times(a,b)
    al,au=a; bl,bu=b
    extrema=(al*bl,al*bu,au*bl,au*bu)
    assert actual==(min(extrema)//D,-((-max(extrema))//D))
    ai=0 if al>=0 else 1 if au<=0 else 2
    bi=0 if bl>=0 else 1 if bu<=0 else 2
    signed['sign_cases'][3*ai+bi]+=1
    signed['multiply']+=1
    if a==(0,0) or b==(0,0): signed['zero_operand_multiplications']+=1
    return actual
def over(a,k):
    actual=old_over(a,k)
    assert k>0 and a[0]<=a[1] and actual==(a[0]//k,-((-a[1])//k))
    signed['divide']+=1
    return actual
def enclose(n,d=1):
    actual=old_enc(n,d)
    assert d>0 and actual==((n*D)//d,-((-n*D)//d))
    signed['convert']+=1
    return actual
def plus(a,b):
    actual=old_plus(a,b)
    assert actual==(a[0]+b[0],a[1]+b[1])
    signed['plus']+=1
    return actual
def opposite(a):
    actual=old_neg(a)
    assert actual==(-a[1],-a[0])
    signed['negate']+=1
    return actual
def intersect(a,l,u):
    actual=old_clip(a,l,u)
    assert l<=u and actual==(max(a[0],l),min(a[1],u)) and actual[0]<=actual[1]
    signed['clip']+=1
    return actual
def product(a,b):
    before=replay.LEDGER.get('coefficient_pairs',0)
    actual=old_product(a,b)
    assert replay.LEDGER['coefficient_pairs']-before==len(a)*len(b)
    assert (len(a),len(b),len(actual)) in ((129,65,193),(193,65,257))
    assert all(l<=u for l,u in actual)
    signed['products']+=1
    return actual
for name,fn in [('floor_checked',floor_checked),('ceil_checked',ceil_checked),('times',times),('over',over),
    ('enclose',enclose),('plus',plus),('opposite',opposite),('intersect',intersect),('product',product)]: setattr(replay,name,fn)
intervals=[(-2*D,-D),(-D,0),(-D,D),(0,0),(0,D),(D,2*D)]
for a in intervals:
    for b in intervals: times(a,b)
for n in (-2*D-1,-D,-1,0,1,D,2*D+1):
    for d in (1,3,D): floor_checked(n,d); ceil_checked(n,d)
assert all(signed['sign_cases'])
save('primitive-controls.json',signed)
for key in signed: signed[key]=[0]*9 if key=='sign_cases' else 0
replay.LEDGER.clear()
