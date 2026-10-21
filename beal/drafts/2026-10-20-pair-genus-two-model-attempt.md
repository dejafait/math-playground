# Explicit pair-curve construction working record

2026-10-20. Ready target: construct L109's hyperelliptic model with
the original s,z and verified birational maps. Prior assessment:
`literature/2026-10-20-pair-genus-two-explicit-model.md` (SPECIALIZE).

Main gap: residual-signature integer exclusion. This intermediate model
could enable a later rational-point method; rational points, degree-nine
root recovery, remaining factors and both L095 systems stay unresolved.
Continue only with a squarefree quintic/sextic and inverse Q-function-field
maps retaining s=H0(u,z) and the exact extension v²=z. An equation alone
does not meet the test. Stop an implementation that cannot certify maps.

Reused the supplied primary-source comparison and checked L109's exact
definitions, its audit, history/376–377 and ATTEMPTS/046 (minus-three at
seven), 048 (scaling). Neither stop is reopened. No curve backend is on
PATH (Sage, Magma, Singular, Maple); default Python has no SymPy. No paid
service, API or package installation is used. L108 remains untouched.

Unfinished exact-elimination calculation, to be checked before assertion:
put q(t)=3t²+t+1, x=1−5a, y=1−5b, t=q(a)/q(b), so y=t^5 x.
Then 3 S11(t)x²−11 S6(t)x+33=0, S_n=sum_(i=0)^(n−1)t^i.
The discriminant Delta=121 S6²−396 S11 should have factor (t−1)².
Writing Y=(6 S11 x−11 S6)/(t−1), the unordered involution should be
(t,Y)->(1/t,−Y/t^4). Try T=t+1/t and W=Y(t²−1)/t³.
Then W²=(T²−4) R4(T), with R4 yet to be computed exactly.

Proposed inverse expressions, also unverified at this checkpoint:
F=T^5+T^4−4T³−3T²+3T+1, K=T²−T−1,
u=(F−11−K W)/(60F), M=2−10u,
z=−M² (T−2)(T²+T−1)²/[300(T+2)K²].
Conversely d=3u²+u+1−9z, e=6u+1,
T=2(d²−3ze²)/(d²+3ze²), W=(F−11−60F u)/K.
Need exact checks of all defining identities, both compositions,
denominator nonvanishing and smooth proper identification. These are
working formulas, not a completed model or new lemma.

Completed construction: the full proof and exact maps are canonical in
`lemmas/L110-explicit-pair-genus-two-model.md`. The sextic is
W²=11(T²−4)(7+52T−6T²−64T³−25T⁴). Exact rational arithmetic verifies
H1, the original scalar, both inverse compositions, the reciprocal
elimination and the removable finite chart. The full certificate is
`scripts/pair-genus-two/model-certificate.json`. The working formulas
above are now justified there, not separate canonical assertions.

Implementation recovery within this one attempt: direct Fraction-Euclidean
gcd simplification was interrupted during H1 substitution after excessive
intermediate coefficient growth. Primitive polynomial pseudo-remainders
replace it. An initial prototype used integer division to normalize a gcd,
introducing a float and failing exact divisibility before any certificate
was written. It was corrected to Fraction(1)/leading_coefficient; the
subsequent complete run passes. No failed mathematical identity was
discarded or replaced by a numerical check. All arithmetic is rational.

No canonical-differential backend was needed: exact elimination is within
the approved assessment and the verified squarefree model supplies the
smooth charts. L109's proper curve is identified by inverse function-field
maps and the imported normal-projective equivalence. Exceptional charts
are retained, and the constant in z and extension v²=z are unchanged.
No rational-point set, rational-root lift, integer exclusion or novelty
claim results. A separate critical audit is the sole proposed next target.
