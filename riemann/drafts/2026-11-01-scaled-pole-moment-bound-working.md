# Three scaled pole moments — bounded proof attempt

Completed: the full bound and every cluster-size case are now in
[C645e](../lemmas/C645e-three-scaled-pole-moment-lower-bound.md).
The initial reasoning below is preserved; independent audit remains.

Approved target: Test whether the first three n-scaled inverse-Blaschke pole moments have a uniform positive lower bound on C645d's admissible clusters.

The existing EXPLORE assessment is
`drafts/literature/2026-11-01-scaled-pole-moment-detector.md`.
Main gap: actual-Xi signs and the Pick detector's derivative normalization.
This finite-family bound could support vector contour detection; Xi
realization, unrestricted poles/multiplicities, interpolation, contour
clearance and weighted boundary control remain independent gaps.

## Reasoning saved before completion

Write the two possible additional scaled nodes as u,v and their exact
weights as A=B_n(x)/B_n(x+u/n), B=B_n(x)/B_n(x+v/n). Then
M0=1+A+B, M1=uA+vB and M2=u^2 A+v^2 B. The identity

    M2-(u+v)M1+uv M0=uv

is exact. If both |u|,|v|>=eta, it gives
max |Mk| >= (eta/(1+eta))^2 regardless of their separation, magnitude,
or the weights. Hence a sequence with all three moments tending to zero
must bring at least one additional scaled node to zero.

The exact inverse factor ratio is

    q_j(h)=(1+i t_j h/(R^2+i t_j x))/(1+h/(x-i t_j)).

On the permitted ball, d>1, R>5/4 and |h|<1/16 give
|q_j(h)-1| <= (656/375)|h| < 2|h|. Finite product expansion therefore
suggests |B_n(x)/B_n(x+h)-1| <= 2|u|/(1-2|u|), for u=nh and
|u|<1/2. In particular |u|<=1/8 gives weight error at most 1/3.

Candidate explicit threshold: max |Mk| >= 1/81, uniformly for all
the assessed delta and n>=5. If max |Mk|<1/81, the moment identity
forces one node |u|<1/8. Its weight A is within 1/3 of 1; M0 forces
|B|>=5/3-max |Mk|. M1 then forces

    |v| <= (max |Mk|+1/6)/(5/3-max |Mk|) < 29/268 < 1/8.

Both weights are consequently near +1, contradicting small M0.
The zero- and one-additional-node cases need explicit treatment.
No numerical sample, asymptotic interchange or independent-amplitude
countermodel is used. Finish all cases and constants before promoting
this reasoning to a canonical result. A complete bound continues this
finite-family mechanism only; a counterfamily would stop it. Neither
outcome resolves the main RH gap.
