"""Nonrigorous continuum saddle diagnostic; no asymptotic certificate."""
import cmath
import json
from pathlib import Path
import numpy as np

OUT = Path(__file__).with_name('oblique-leading-saddle-diagnostic.json')
d, r, U = 1.25, .54, (11/8)**2
x = -d
phi = 13*np.pi/16
u = cmath.exp(1j*phi)
nodes, weights = np.polynomial.legendre.leggauss(192)
ss, ww = (nodes+1)/2, weights/2

def data(z):
    v = x+1j*r*cmath.cos(z)
    vp, vpp = -1j*r*cmath.sin(z), -1j*r*cmath.cos(z)
    a = U*u
    p = np.sum(ww*(np.log((x-ss*u)/(v-ss*u))
                   +np.log((a-ss*v)/(a-ss*x))))
    pv = np.sum(ww*(-ss/(a-ss*v)-1/(v-ss*u)))
    pvv = np.sum(ww*(-ss**2/(a-ss*v)**2+1/(v-ss*u)**2))
    return p-2j*z/3, pv*vp-2j/3, pvv*vp**2+pv*vpp

roots = []
for re in np.linspace(0,2*np.pi,25,endpoint=False):
    for im in np.linspace(-.5,.5,9):
        z = complex(re,im)
        try:
            for it in range(60):
                h, hp, hpp = data(z)
                if abs(hp)<1e-12:
                    break
                step = hp/hpp
                if abs(step)>.3:
                    step *= .3/abs(step)
                z -= step
                if abs(z.imag)>1:
                    break
            z = complex(z.real%(2*np.pi),z.imag)
            h,hp,hpp = data(z)
            if abs(hp)<1e-10 and abs(z.imag)<1 and all(abs(z-v)>1e-6 for v in roots):
                roots.append(z)
        except (OverflowError,ZeroDivisionError):
            pass

def pair(z):
    return [float(z.real),float(z.imag)]

records=[]
for z in sorted(roots,key=lambda z: z.imag):
    phase,der,sec=data(z)
    contour=[]
    for t in np.linspace(0,2*np.pi,4096,endpoint=False):
        hh,_,_=data(complex(t,z.imag))
        contour.append(float(hh.real))
    records.append({'z':pair(z),'phase':pair(phase),'derivative_abs':float(abs(der)),
                    'second_derivative':pair(sec),
                    'circle_max_real_phase':max(contour),
                    'circle_argmax':float(np.argmax(contour)*2*np.pi/4096),
                    'circle_sample_real_phase':contour})
selected = min(roots,key=lambda z:z.imag)
kappa = -selected.imag/np.sin(selected.real)
shaped = []
for t in np.linspace(0,2*np.pi,4096,endpoint=False):
    z = complex(t,-kappa*np.sin(t))
    hh,_,_=data(z)
    distance=abs((t-selected.real+np.pi)%(2*np.pi)-np.pi)
    shaped.append({'t':float(t),'real_alias_phase':float(hh.real),
                   'real_b0_phase':float((hh+2j*z/3).real),
                   'distance_to_saddle':float(distance)})
shape={'kappa':float(kappa),
       'maximum_alias_phase':max(v['real_alias_phase'] for v in shaped),
       'maximum_b0_phase':max(v['real_b0_phase'] for v in shaped),
       'maximum_outside_distance_point2':max(v['real_alias_phase'] for v in shaped if v['distance_to_saddle']>=.2),
       'samples':shaped}
result={'status':'NONRIGOROUS_DIAGNOSTIC_ONLY','phi':phi,
        'required_real_phase_lower':-.03,'roots':records,
        'shaped_contour':shape,
        'failures':['No root enclosure, branch/contour certificate, uniform sector estimate, or asymptotic remainder.']}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(result['status'],'required real phase >',result['required_real_phase_lower'])
for rec in records:
    print({k:v for k,v in rec.items() if k!='circle_sample_real_phase'})
print('Shaped contour:',{k:v for k,v in shape.items() if k!='samples'})
print('Unresolved:',result['failures'])
print('Full diagnostic:',OUT)
