# Nonreal multiple-zero splitting checkpoint — 2026-09-11

The prior L126 step is complete and preserved. Current calculation: write
f(w+u)=c u^m(1+A u+O(u²)). Weighted heat rescaling gives
G(s,v)=c[P_m(v)+A s P_(m+1)(v)+O(s²)]. At a root α of P_m,
P_(m+1)(α)=-2P_m'(α), so every branch has
z=w+α sqrt(t)+2A t+O(t^(3/2)). This is draft reasoning pending the
product/sign audit. A=h'(w)/h(w) for h=f/(z-w)^m.

Resume by checking removal of m copies of the opposite pair in L063,
then extracting the conjugate quartet with multiplicity m. Expected highest
height coefficient is at most -m/b-mb/|w|². No moving global supremum
conclusion is intended; if Im A=0 in the unrestricted case higher orders
may decide the height and are not covered by this first-order calculation.

Completed: the rescaling, multiplicity removal, and sign audit are proved in
L127. The unrestricted coefficient may vanish; the highest-zero coefficient
is strictly negative. No failed approach or unfinished claim was promoted.
