# L074 — The exterior centering defect of the first pair is O(N²)

## Hypotheses

Keep L064's two original probes i=3,6, fixed tau=1/16, SU(2)
straight-forest Gaussian, actual residual, and admitted even meshes
a=8/N. Take the small-coupling coefficient at fixed mesh first.
Use ordinary dimensionless coordinates, every upper edge e=(v,w),
every transverse plaquette p at levels 1<=s<N, and all pinned end
rows. Use L069's direct/axial split only in the right residual lift;
leave the base covariance row H unchanged.

For each transverse plane mu<nu write the four signed edges as
(x_1,x_2,x_3,x_4)=(A,B,-C,-D), where A,C are positively oriented
mu-links and B,D are positively oriented nu-links on opposite sides
of that same plaquette. Fixed links have value zero. Applied to the
actual exterior column v_l, L062's three rows are

    t_l,1=A+B-C-D, t_l,2=A+B, t_l,3=B-C.

Define opposite-edge averages m_mu=(A+C)/2, m_nu=(B+D)/2,
and change only the exterior coefficients to

    bar t_l=(t_l,1, m_mu+m_nu, m_nu-m_mu).

In particular this operation does not change the right path maps
B_2,B_3 in H or W, the circulation D, the covariance Sigma_T,
the residual A_0, axial embeddings or any upper endpoint coefficient.
Here D as a map denotes circulation; the edge value D above is used
only in the four-edge formulas.

## Conclusion

Let F_i^dir(t) be L064(1)'s complete first line with W=W^dir and
the complete exterior heat sum. The replacement has the exact defect

    delta t_l,2=delta t_l,3=t_l,1/2,
    delta Q_l=Q_l-bar Q_l=(1/2) M_(t_l,1)(B_3-B_2).       (1)

Consequently, with all products in L070(1)'s original order,

    F_i^dir(t)-F_i^dir(bar t)
      =sum_(k,l)c_(i;kl) sqrt(N)
         Tr[G C_(r_k) G E_0^T A_0 I_T Sigma_T
                    D^T delta Q_l S],                    (2)

and for both probes

    |F_i^dir(t)-F_i^dir(bar t)| <= C_i N².                (3)

The same replacement has exactly zero effect on the axial-prefix
part of this pair. Thus (3) is also the defect bound for the full
first pair. This does not bound the centered pair itself.

The separate test in proof section 5 also centers both rough right
rows. That simultaneous shear leaves the direct pair exactly invariant
and moves the exterior defect into the centered path/path term. Its
joint ordered trace is explicit, but the available complete heat-sum
estimate stays O(N³), above the O(N²) threshold.

This is a boundedness result only. It proves neither an o(N²)
defect nor a scaled limit, sign, original-trace coefficient or cutoff
logarithm. In particular a² times this defect may survive; it cannot
be dropped when identifying an a²-scaled coefficient. The certified
finite diagnostic in L073 is still not identified with the original
trace. This is local REPRODUCTION under the unchanged SPECIALIZE
combined-response assessment, with no novelty claim beyond its sources.

## Proof

### 1. Exact four-edge identity and preservation of pinned rows

The two differences are, without any smoothness assumption,

    (A+B)-(A+C+B+D)/2=(A+B-C-D)/2,
    (B-C)-(B+D-A-C)/2=(A+B-C-D)/2.

These prove (1), since Q_l=M_(t_l,2)B_3-M_(t_l,3)B_2.
They are polynomial identities in the four actual edge evaluations,
so still hold when any fixed boundary row is zero. The opposite
values are from the same retained plaquette; there is no translation
past a physical face and no extension to level N. For a general
right field, B_3-B_2=x_3-x_1=-(A+C), with A,C now its right
edge evaluations. This fixes the sign and shows explicitly that no
right path or right covariance has been centered implicitly.

L070(1) is linear in Q_l. Subtraction with every other finite map
unchanged proves (2). The monomials with exterior t_l,1 are unchanged
and therefore cancel in this subtraction. No variable multiplier is
commuted with a Green function, covariance or residual.

### 2. Expand both endpoint placements before estimating

For this section write W=W^dir. Since H_1=(TH)_1=0, the
fixed-(k,l) difference in the original determinant expression is

    delta F_kl=(1/2) sum_(e,p) r_k(e)t_l,1(p) {
        W_1(v,p)[(TH)_2(e,p)-(TH)_3(e,p)]
       +[H_3(v,p)-H_2(v,p)] (TW_1)(e,p) }.               (4)

Indeed expand det(delta t,W,TH)+det(delta t,H,TW) with
delta t=(0,t_l,1/2,t_l,1/2). The first determinant is
(t_l,1/2)W_1[(TH)_2-(TH)_3]; the second is
(t_l,1/2)(H_3-H_2)TW_1. This independently checks the sign in
(2) and retains both upper endpoint placements. The formula is
valid on end edges because all endpoint maps use zero pinned values.

L069 section 1 proves W_1^ax=0 before the residual is inserted:
the right axial-prefix lift is a transverse gradient and its full
pinned circulation is zero. Hence TW_1^ax=0 as well. Formula (4)
therefore vanishes for the axial part, and W_1^dir=W_1^full.
This uses an exact right-map identity, not differentiation of a
base-law covariance zero. There is no unrestricted transverse
residual bound hidden in this reduction.

### 3. Complete-array bound and full heat sum

L064(3), using L062's boundary-inclusive smooth exterior estimates,
gives for a fixed polynomial p, enlarged if necessary,

    ||r_k||_infinity <= a² p(k),
    ||t_l,1||_infinity <= a² p(l),
    sum_(k,l)|c_(i;kl)| p(k)p(l) <= C_i.                 (5)

The second bound is on the circulation, not on an arbitrarily
centered smooth path. In L062(11) the forest-prefix gradient cancels
exactly from this circulation, including normal end edges and zero
tangential rows. Thus no interior-only regularity assertion is being
extended to pinned plaquettes in (5).

L064 section 3 gives ||W_1^full||_HS<=C N³ on the full
upper-vertex by plaquette array. By section 2 it is also W_1^dir.
Pullback to v or taking the upper difference T changes this by only
a fixed factor: each upper vertex meets at most six edges. L062(9)
gives the corresponding complete-array bounds

    ||W_1(v,p)||_HS+||(TW_1)(e,p)||_HS <= C N³,
    sum_(b=2,3)(||H_b(v,p)||_HS+||(TH)_b(e,p)||_HS)
                                                    <= C N³. (6)

These sum all p, all s and all upper endpoints before the estimate;
there is no subsequent uncounted level or edge multiplicity. Apply
Cauchy–Schwarz to each of the four scalar products in (4), with
the multiplier bounded by (5). It follows that

    |delta F_kl| <= C a^4 p(k)p(l) N^6
                  = C' N² p(k)p(l),                     (7)

because a=8/N. The complete heat sum in (5) now proves (3).
The constants are uniform over all admitted sufficiently fine meshes
for both original probes. The finite sums justify every rearrangement
at fixed mesh, and (5) is the uniform absolute majorant; no exchange
with an unproved continuum limit is used.

The standard determinant identity and matrix Cauchy–Schwarz specialize
the existing local bounds. No new general heat-kernel, flow-finiteness
or stress-matching result is required or reproved. The applicable
known-result comparison is the saved assessment
`drafts/literature/2026-09-26-current-target.md`.

### 4. Scope of the improvement

L064's coarse circulation/path bound had a³ N^6=O(N³):
one upper curvature coefficient a² and one exterior path coefficient
a. The exact difference here replaces that path coefficient by
a curvature coefficient a² and gives a^4 N^6=O(N²).
It improves only the replacement error, not the whole original pair.
The remaining exterior t_1 path/path monomials were unchanged, and
the centered circulation/path trace still needs its own estimate.

Axial normalization, identification with the diagnostic, variable
coefficient and pinned-boundary trace remainders, the other endpoint
monomials, all nine mixed placements at logarithmic order, other
action/measure/insertion/flow and forest jets remain unresolved.
Conditional signs remain conditional and the shared quartic is
subtracted only once. The reflected error <=c_box/2, continuum fields,
reflection positivity, infrared control and finite positive mass
are not improved by (3). No complete candidate is asserted.

### 5. Subsequent bounded right-row centering test, 2026-10-08

This section records the separate attempt
YM-20261008-095-first-pair-right-centering-test. It retains the
hypotheses above and tests both rough right rows of the direct first
pair; it does not strengthen (3). The result is EXPLORATION /
RESEARCH / REPRODUCTION: exact local algebra and a surviving upper
bound, with no O(N²) bound for the pair or source-level discovery.

On the three right coefficients use the fixed linear map

    L(c,b,q)=(c,b-c/2,q-c/2), det L=1.

Write bar B_2=B_2-D/2 and bar B_3=B_3-D/2. For the four actual
edges in the hypotheses these are respectively m_mu+m_nu and
m_nu-m_mu. Every pinned zero row is retained. Write W=W^dir.
Then bar W=(W_1,W_2-W_1/2,W_3-W_1/2). Since H_1=0,
bar H=H, and L commutes with the upper endpoint difference T.
Multilinearity and det L=1 give, at each retained (e,p),

    det(bar t,bar W_v,T H)=det(t,W_v,T H),
    det(bar t,H,T bar W)=det(t,H,T W).                    (8)

Thus simultaneous exterior and rough-row centering leaves the entire
direct first pair invariant, before summation or estimation. This
does not assert invariance of an individual monomial.

Here is its ordered decomposition, retaining the path/path terms.
For fixed exterior indices k,l suppress them in r,t and set
C=C_r from L069, W_X=sqrt(N)G E_0^T A_0 I_T Sigma_T and
H_X=G S^T from L070. Thus W_b=W_X B_b^T and H_b=H_X B_b^T
for b=2,3, while W_1=W_X D^T.
The exact identity D S=0 gives H_X D^T=0 and
H_X bar B_b^T=H_X B_b^T. All maps are finite pinned maps.
For each p let the following scalars use columns indexed by p:

    A_p=W_1(p)^T C H_3(p), B_p=W_1(p)^T C H_2(p),
    P=sum_p t_1(p)[W_2(p)^T C H_3(p)
                                  -W_3(p)^T C H_2(p)],
    F_circ=sum_p[-t_2(p)A_p+t_3(p)B_p].

L069's skew identity gives F_kl=P+F_circ, including both endpoint
placements. Define delta=sum_p(t_1(p)/2)(-A_p+B_p). Direct
substitution, without commuting any multiplier, gives

    bar P=P+delta, bar F_circ=F_circ-delta,
    F_kl=bar P+bar F_circ.                               (9)

Here bar P uses bar W and bar F_circ uses bar t; H is unchanged.
The scalar delta is exactly the exterior-only difference (4), after
its upper-edge sum. Its complete heat sum is O(N²) by sections 2–3.
Equation (9) shows that this difference is transferred to the
path/path term, rather than eliminated by centering the rough rows.

For an explicit joint operator formula put

    Lambda_l=bar B_3^T M_(t_l,1) bar B_2
                         -bar B_2^T M_(t_l,1) bar B_3,
    bar Q_l=M_(bar t_l,2)bar B_3-M_(bar t_l,3)bar B_2.

Expansion of the finite diagonal sum gives
bar P=Tr[W_X^T C H_X Lambda_l]. Both C and Lambda_l are
skew-symmetric. Transposing the scalar trace introduces their two
minus signs, so bar P=Tr[Lambda_l H_X^T C W_X]. Substituting
H_X^T=S G and W_X, and cycling only the finite trace, yields

    F_kl=sqrt(N) Tr[G C_(r_k) G E_0^T A_0 I_T Sigma_T
                                (Lambda_l+D^T bar Q_l) S]. (10)

The circulation term follows with the same sign from L070(1).
Equation (10) retains the actual residual/covariance order, every
axial level, and the complete pinned right and left maps. It is not
a frozen symbol or a three-dimensional covariance substitution.

One can also check (10) against the original uncentered trace
without relying just on determinant invariance. Let Lambda_l^old
be the same formula using B_2,B_3, and let Q_l be L070's original
alternating map. Expansion gives

    Lambda_l=Lambda_l^old
      +(1/2)[D^T M_(t_l,1)(B_3-B_2)
                             +(B_2-B_3)^T M_(t_l,1)D].

Since D S=0, Lambda_l S=Lambda_l^old S+D^T delta Q_l S,
with delta Q_l from (1). Also bar B_b S=B_b S and
bar Q_l S=(Q_l-delta Q_l)S. Therefore

    (Lambda_l+D^T bar Q_l)S
                           =(Lambda_l^old+D^T Q_l)S.     (11)

No variable coefficient passes through D, G, Sigma_T or A_0 in
this check. In particular the term involving M_(t_l,1)D vanishes
because D S=0 on its right, not because that multiplier is constant.

The rough shear supplies no new right-gradient identity. For every
pinned transverse vertex field z, D Tz=0 and consequently
bar B_b Tz=B_b Tz. At an interior plaquette with successive corners
v,v+mu,v+mu+nu,v+nu these values remain exactly

    bar B_2 Tz=z(v)-z(v+mu+nu),
    bar B_3 Tz=z(v+mu)-z(v+nu).

For example the pinned fields z=1 at v only and w=1 at v+mu
only give path pairs (1,0) and (0,1). The single-plaquette
alternating path minor is nonzero. This is a local incidence check;
it does not show nonvanishing of the complete variable-weight
Lambda_l S, the actual residual composition or either signed heat
sum. Further signed cancellations remain possible.

Finally estimate only after the exact regrouping. Section 3 and
L064's direct component of its whitened lift give

    ||W_1||_HS+||TW_1||_HS<=C N³,
    sum_(b=2,3)(||W_b||_HS+||TW_b||_HS)<=C N⁴.

For clarity, the second bound applies to the isolated direct block:
in L064(7) replace the right lift by I_T followed by B_b. Its
whitened norm is O(N) by the full Hodge gap, the left HS norm is
O(N²), and the whitened residual norm is O(N). Their product is
O(N⁴); endpoint pullbacks have bounded norm. The first bound uses
W_1^ax=0 and the full bound already used in section 3. Subtracting
W_1/2 from either path leaves bar W_b bounded by O(N⁴), not an
established O(N³) bound. H and TH have O(N³) full-array bounds.
Also |r_k|,|t_l,1|<=a²p and |bar t_l,b|<=C a p(l), b=2,3.
Thus, by complete-array Cauchy–Schwarz on the original two
placements,

    |bar P_kl|<=C a^4 p(k)p(l)N⁴N³=O(N³)p(k)p(l),
    |bar F_circ,kl|<=C a³ p(k)p(l)N³N³=O(N³)p(k)p(l).

L064(3)'s summable full heat expansion proves both O_i(N³)
bounds and the same bound for their sum. The achieved bound remains
one power above the required O(N²). Neither this upper bound nor
the nonzero local minor proves signed growth or failure of a sharper
joint estimate. L066's stronger-residual-norm obstruction remains
relevant contrast, not a lower bound for (10).

This bounded shear-plus-generic-norm closure is parked. Resolving
the centered trace, axial normalization, scaled defect or pinned
remainder requires additional information about the actual composition.
All other response and construction limitations in section 4 remain.
The exact identities are elementary finite determinant and trace
algebra specialized to the assessed target; no known general
renormalization theorem is reproved and no mathematical script or
numerical diagnostic is used.

## Mathlib

Coverage of the full exterior-centering statement: **not checked**.
Coverage of section 5's simultaneous right-row centering and ordered
trace identity: **not checked**.
Supporting determinant multilinearity, finite matrix Cauchy–Schwarz
and finite incidence algebra: **not checked**. No matching theorem
or absence claim is made. The specialized covariance, heat-sum and
pinned-row estimates are imported with their exact scope from the
local results used in the proof.
