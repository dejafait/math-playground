# Joint antisymmetric placement / exterior-curl test

STEP_ID: YM-20261011-153-joint-curl-test
Ready assessment: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
Main gap: interacting ultraviolet control and a nonzero physical continuum
sector; immediate intermediate target is evaluation of L124's cubic
comparison. One bounded test asks whether L126's antisymmetric derivative
and L123's exterior-circulation term jointly depend only on transverse
curl, while retaining H explicitly. A genuine contraction identity could
reduce the actual coefficient evaluation. Continue on a justified identity
or a concrete failed necessary identity; otherwise record exploration.

Saved before extended algebra. L118's exact projected centered paths give,
for a real exterior vector v, P_c F(v)=d f(v)^T/lambda with
f(v)_(mu nu)=2[d_nu eta_mu v_mu-d_mu eta_nu v_nu]. Thus
F(v)^* P_c F(w)=f(v) f(w)^T/lambda. Substitute this into L125(3),
antisymmetrize v,w, and sum every ordered r at a fixed displacement rho.
A curl-only derivative tensor must annihilate every symmetric transverse
jet J_(m,b)=partial_m V_b. L123's K_f already vanishes on curl-free jets;
it cannot repair a nonzero antisymmetric-placement test on such a jet.
No nonzero tensor, curl identity, phase simplification, or actual-probe
value is assumed at this point. Verify original-phase derivative terms
before using centered expressions; arbitrary v/J tests need not isolate
physical probes and are only tests of a universal reduction.

Inputs read: L126 L125 L123 L118 in full; L120(1)--(3), L111(1)--(8),
L113(1)--(11), L088(3)--(13). Duplicate/failure check: L125/L126 do not
contract the retained antisymmetric part; ATTEMPTS/028--034 rule out
separate operator/moment/parity and half-tensor shortcuts, not this
joint physical-component test. Preserve all earlier and unfinished work.
Essential continuation IDs: L126 L125 L123 L118 L120 L111 L113 L088.
L124 L097 L098 L101 L104 L107 retain the remaining coefficients;
L084 L070 L079 L080 L082 fix the reference and IEEE qualifications.
Unresolved: joint curl reduction, evaluated actual-probe contractions,
compensation, finer scales/logarithm, other jets, matching and interacting
error <=c_box/2, continuum axioms, reflection positivity, infrared control
and finite positive mass. Full matching Mathlib coverage not checked.

Unfinished contraction after complete-plane substitution: at displacement
rho=2, derivative m=3, take exterior vectors e_2,e_3. Put x=d_2,
y=d_3,z=d_4, A=eta_2,B=eta_3,C=eta_4, L=x^2+y^2+z^2.
With v=(y,z,0), w=(-x,0,z), t=(0,x,y), and
S=I-n n^T/L, n=(z,-y,x), the complete ordered generator has
G=i A[-B^2 w e_(23)^T+C^2 t e_(24)^T] S.
The projected exterior columns are f(e_2)=2A v, f(e_3)=2B w.
Direct differentiation suggests that the antisymmetric coefficient is

 tau=-integral A^2 B^2 z^2/L
       [y^2+(y^2-z^2)(x^2+z^2)/(2L)].

The phase term vanishes only after the same integrated parity check as
L125(9). No sign has yet been certified. Analytically integrating theta_3
reduces -tau to the normalized two-dimensional integral of
F(theta_2,theta_4)=(1-X/4) Z/8
 [k+4-(k^2+6k+2Z)/sqrt(k(k+4))], X=d_2^2,Z=d_4^2,k=X+Z.
An exploratory ordinary floating-point midpoint evaluation at n=32,64,128
suggested -tau near -0.00836529; this is not evidence of a sign.
The next bounded check in this same attempt is an exact rational interval
midpoint certificate with a proved C^2 quadrature bound. Preserve this
expression if certification fails; neither universal curl removal nor
actual-probe noncancellation is established at this stage.

Completed result: L127 proves the formula for tau and certifies
7/1000<tau<1/100 by exact integer intervals and an analytic C^2 midpoint
bound. All planes and both ordered displacement-2 generators remain.
A compact curl-free test with symmetric bilinear coefficients makes the
antisymmetric term nonzero while K_f=0. This is an informative NEGATIVE
for universal curl removal with H fixed, not a sign for an actual probe.
Canonical proof: lemmas/L127-other-other-antisymmetric-placement-curl-obstruction.md.
Certificate: scripts/combined-ward-response/joint-curl-tensor-certificate.json.
Recorded stop: ATTEMPTS/035-antisymmetric-placement-universal-curl-removal.md.

Continuation under the unchanged ready comparison target: substitute
phi_(pi,b)=V_mu+V_nu, phi_(pi,q)=-V_mu+V_nu into the complete retained
transverse-H coefficient K_f+K_V+K_sc+K_en. Keep H and the antisymmetric
term, and use coordinate reflections/permutations to reduce the full
physical-component tensors before any actual heat-weighted evaluation.
Seek an exact reduction to independently certifiable scalar torus
coefficients; continue only if it reduces the actual comparison or gives
a new discriminating test. Do not infer complete compensation from
isolated tensor signs or demand a universal curl identity again.
Essential inputs: L127 L126 L125 L123 L120 L118 L113; L124 L097 L098
L101 L104 L107 retain the five other coefficients, while L084 L070 L079
L080 L082 fix the mixed reference and its original qualifications.
Unresolved assumptions: no full physical tensor reduction, actual-probe
coefficient or compensation is established. No special probe constraint
is assumed to cancel the test. Finer powers/logarithm, other jets,
matching and interacting error <=c_box/2, continuum field axioms,
reflection positivity, infrared control and finite positive mass remain.
