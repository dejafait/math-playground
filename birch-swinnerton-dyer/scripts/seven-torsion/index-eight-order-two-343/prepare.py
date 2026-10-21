"""Guarded source adaptation only, inside the sole watchdog."""
from pathlib import Path
D=Path(__file__).resolve().parent; S=D.parent
def put(n,s):
    with (D/n).open('x') as f:f.write(s)
def replace(s,a,b):
    if s.count(a)!=1:raise ValueError('nonunique adaptation '+a[:100])
    return s.replace(a,b)
s=(S/'index-four-order-two-335/produce.py').read_text()
s=replace(s,'Actual L086 S producer. One shared stage, scale 124.','Actual L088 U producer. One shared stage, scale 248.')
s=replace(s,"nb=json.loads((OUT/'basis.json').read_text())","nb=json.loads((OUT/'u-basis.json').read_text())")
s=replace(s,'Q=[[124*x for x in row] for row in M]','Q=[[248*x for x in row] for row in M]')
s=replace(s,"nb['scale']==124 and nb['input_scale']==62","nb['scale']==248 and nb['input_scale']==124")
s=replace(s,"nb['original_scale']==31 and nb['index']==4,'actual_scale_124_S'","nb['original_scale']==31 and nb['prior_scales']==[31,62,124] and nb['index']==8,'actual_scale_248_U'")
s=replace(s,"'identity':identity,'scale':124}","'identity':identity,'scale':248}")
s=replace(s,"(OUT/('product-%02d.json'%i))","(OUT/('u-product-%02d.json'%i))")
s=replace(s,',15376)',',61504)')
s=s.replace('integral_S_inverse','integral_U_inverse').replace('scaled_S_basis_integral','scaled_U_basis_integral').replace('S_basis_inverse_both','U_basis_inverse_both').replace('S_two_coordinate_transports','U_two_coordinate_transports')
put('produce.py',s)
s=(S/'index-four-order-two-335/verify.py').read_text()
s=replace(s,"got=load(HERE/'basis.json')","got=load(HERE/'u-basis.json')")
s=replace(s,"load(HERE/('product-%02d.json'%i))","load(HERE/('u-product-%02d.json'%i))")
s=replace(s,"validation=read('input-report.json')","validation=read('u-verification-report.json')")
s=replace(s,"validation['index']==4","validation['index']==8 and validation['scale']==248")
s=replace(s,"ib['scale']==124","ib['scale']==248")
s=replace(s,'# Each column of Wpolys represents 62 times the actual radical element.','# Every Wpolys row represents 248 times the actual radical element.')
s=replace(s,'[124*x for x in expansion[j]]','[248*x for x in expansion[j]]')
put('verify.py',s)
