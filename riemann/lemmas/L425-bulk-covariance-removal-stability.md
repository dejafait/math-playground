# Lemma 425: covariance removal in the prescribed bulk transport observable

## Hypotheses

Use exactly L423's law on [H,2H], with real H tending to infinity,
ell=log H, height average E, fixed mixture g_H, remaining mass w,
full correction A_H, and actual physical discriminant matrix J(t).
Use L419's deterministic coordinate construction, with its same fixed
coordinate/pair orders, equality cases and complementary rotation.
In particular, the basis is not freely reselected. Write

    Sigma=ell g_H K+A_H, S=Sigma^(1/2),
    K=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]],
    V_i=sqrt(3/ell) S u_i,
    B_H=E[(w/3) sum_i Q(V_i)],

where Q is L424's function

    Q(a,b,d)=exp(-a^2-b^2)[b^2(1-2a^2)+ad(1-2b^2)].

Define the comparison by deleting only A_H:

    Sigma_0=ell g_H K, S_0=Sigma_0^(1/2),
    V_i^0=sqrt(3/ell) S_0 u_i^0,
    B_H^0=E[(w/3) sum_i Q(V_i^0)],

where u_i^0 is the same coordinate rule applied to S_0 J S_0.
All response derivatives, curvature, w, g_H, the height marginal and
the high/intermediate components remain unchanged. The comparison
states are not assumed to satisfy the original moment constraints.
No phase independence, clipping premise or RH assumption is made.

## Conclusion

For this exact comparison,

    |B_H-B_H^0|=o(1).                                  (1)

The proof is qualitative and uniform as H tends to infinity through
real values; it asserts no effective rate or evaluated onset. Together
with L424 it gives E_nu Q(X/sqrt(ell))=B_H^0+o(1) for the complete
unchanged L423 law. It does not evaluate B_H^0 or prove a nonzero
transport defect, reject or realize that law, or supply an actual clipped
statistic, regulator margin, positivity or zero-exclusion range.
The separate step-182 critical audit below validates this comparison
under its stated inputs; it does not evaluate the remaining integral.

## Proof

This RESEARCH / POTENTIALLY_NEW / proof_attempt uses the prior EXPLORE
assessment `drafts/literature/2026-10-17-gaussian-bulk-covariance-stability.md`.
The label records only the absence of a matching result in that scoped
comparison, not established originality. The inspected general
Schur--Horn continuity result does not identify this prescribed basis.
The elementary branch calculation below is therefore necessary. The
earlier floating phase screen is not used.

### Normalized square roots and the complete response error

L423 gives fixed bounds 0<g_-<=g_H<=g_+<infinity, 0<=w<=1,
||A_H||=O(sqrt(ell)), and a compact positive spectral range for
Sigma/ell. Put P=K^(1/2) and

    T_H=S/sqrt(ell), T_H^0=S_0/sqrt(ell)=sqrt(g_H)P.

Import the nonsingular square-root perturbation formula of Marcus
Carlsson, *Perturbation theory for the matrix square root and matrix
modulus*, [arXiv:1810.01464v1](https://arxiv.org/pdf/1810.01464v1),
(1.2) and Theorem 2.1/(2.2), pp. 1--3. For positive Hermitian B,
the divided difference of sqrt at eigenvalues alpha_i,alpha_j is
1/(sqrt(alpha_i)+sqrt(alpha_j)), including repeated eigenvalues;
the remainder is locally O(||E||^2). The family gK with
g in [g_-,g_+] is compact and separated from zero, and A_H/ell
is symmetric with norm O(ell^-1/2). The locally uniform formula,
on a finite cover of that family, therefore gives

    ||T_H-T_H^0||=O(ell^-1/2)                         (2)

uniformly in height. No singular square-root theorem is needed.

Let Z=zeta(5/2+it), R=exp(i phi), rho=|Z|, and choose a smooth
real lift theta of arg(RZ) on the eventual ray. L368 supplies
0<m<=rho<=M and |Z'|<=M_1; L369 supplies the carrier derivative
phi'=log(t/(2pi))/2+O(t^-2). These are the complete right-line
series and actual gamma carrier, not finite heads or free phases.

L390 (4)--(5), or L419's exact J expansion, gives the uniform
operator-norm estimate

    J(t)=c^2 rho(t)^2 J_*(theta(t))+O(ell^-1),
    c=1/(4pi),
    J_*(theta)=
      [[C^2/16, -CS/4, C^2/4+S^2/2],
       [-CS/4,  -C^2, CS],
       [C^2/4+S^2/2, CS, C^2]],                    (3)

where C=cos(theta), S=sin(theta) only in this displayed matrix.
Indeed its quadratic form is
[(z+x/4)^2-y^2]C^2-y(x-4z)CS/2+xz S^2,
which is L390's leading polynomial divided by c^2 rho^2.
The O(ell^-1) error retains every response derivative and the exact
curvature; it is not obtained by differentiating an unspecified error.

Define the normalized matrices to which the rule is applied by

    M_H=T_H J T_H, M_H^0=T_H^0 J T_H^0,
    M_*=g_H c^2 rho^2 P J_*(theta) P.

All matrices and square roots here have fixed norm bounds. From
(2)--(3),

    ||M_H-M_H^0||=O(ell^-1/2),
    ||M_H^0-M_*||=O(ell^-1).                        (4)

The original input matrices are ell M_H and ell M_H^0. Multiplying
a real symmetric input by a positive scalar preserves every comparison
with its trace average, its equality branches, and its rotation root:
both numerator and denominator of L419's eta scale by that scalar.
Thus these normalized matrices give exactly the original selected bases.

### All exceptional branches reduce to three original diagonal gaps

For a real symmetric matrix M set tau=tr(M)/3 and
D_i(M)=M_ii-tau. Suppose every |D_i(M)|>=b>0.
The first step has a strict low/high pair i,j because the three gaps
sum to zero. On each fixed sign pattern, L419 chooses the same pair.
With e=M_ij, its root is

    eta=(-e+sqrt(e^2+(M_jj-tau)(tau-M_ii)))/(M_jj-tau).

Here the denominator is at least b and the radicand at least b^2.
This formula and the resulting first vector and complementary vector
are continuous functions of M on that strict branch.

Let k be the unused original coordinate. In the complementary basis
formed by the rotated i,j vector and e_k, the diagonal belonging to
e_k is still M_kk. The restriction has trace 2tau, since the selected
first vector has Rayleigh value tau. Its other diagonal is therefore
2tau-M_kk. Their gaps from tau are D_k(M) and -D_k(M).
Both are separated from zero by b. The second stage is consequently
strict too; its low/high order is fixed by the sign of D_k(M), its
denominator is at least b, and its radicand is at least b^2. There
is no additional complementary tie locus away from the three original
diagonal equalities. Its off-diagonal may vanish without causing a
singularity in the positive root.

It follows that on a norm-bounded set with min_i |D_i(M)|>=b,
the entire selected basis is uniformly continuous separately on each
of the finitely many sign patterns. To see the uniformity precisely,
intersect each closed sign-pattern region with the norm bound and
these gap bounds. This is compact; both rotation formulas and the
fixed complementary orders are continuous there. Take the maximum
of their finitely many continuity moduli. Sufficiently close matrices
cannot have different sign patterns because each gap is separated
from zero. This also proves uniform comparison of the labeled vectors,
so no unproved invariance of the Q sum under arbitrary rotations is used.

### None of the three leading gaps is a persistent tie

Set F_i(theta)=D_i(P J_*(theta) P). The fixed square root is explicit.
With d=1/sqrt(180)=1/(6sqrt(5)) and D=sqrt(81/80+2d), it is

    P=[[ (1+d)/D, 0, -1/(12D)],
       [0, 1/sqrt(12), 0],
       [-1/(12D), 0, (1/80+d)/D]].                 (5)

For verification, the (1,3) block B of K has determinant d^2 and
trace 81/80. Its Cayley--Hamilton identity gives
(B+dI)^2=(tr(B)+2d)B. Since B+dI is positive definite,
(B+dI)/D is its positive square root. The middle entry is immediate.

Every row of P is either supported in coordinates 1,3 or only in
coordinate 2. Consequently the CS entries of J_* contribute to no
diagonal of P J_* P or to its trace. Each F_i has the form
A_i cos^2(theta)+B_i sin^2(theta) for fixed real A_i,B_i.
It suffices to check nonzero B_i. At theta=pi/2, the only nonzero
entries of J_* are J_*13=J_*31=1/2. Its transformed diagonal is

    (-(1+d)/(12D^2), 0, -(1/80+d)/(12D^2)),

with sum K_13=-1/12. Subtracting its mean -1/36 gives exactly

    B_1=-(159/80+d)/(36D^2),
    B_2=1/36,
    B_3=(39/40-d)/(36D^2).                          (6)

The first is negative, the second positive, and the third positive
because 0<d<1/10<39/40. Thus no F_i is identically zero.
For cos(theta)!=0 its zeros solve A_i+B_i tan^2(theta)=0,
which has finitely many solutions modulo 2pi. At cos(theta)=0
the value B_i is nonzero. Each zero set is therefore finite.

For delta>0 let

    E_delta={theta modulo 2pi: min_i |F_i(theta)|<=delta},
    epsilon_delta=Lebesgue length(E_delta).

Then epsilon_delta tends to zero as delta decreases to zero. For
example, surround the finite union of zero sets by arcs of arbitrarily
small total length. On their compact complement all three absolute
values have a positive minimum, so sufficiently small delta leaves
E_delta entirely within those arcs. This covers multiple zeros as
well as simple ones, without a quantitative sublevel theorem.

### Actual height control, with no phase independence

Since RZ never vanishes, the chosen lift has exact derivative

    theta'=phi'+Im(Z'/Z)
          =log(t/(2pi))/2+O(1).

The second term is bounded by M_1/m. Therefore there are fixed
0<c_0<C_0 and one eventual onset such that, on every [H,2H],

    c_0 ell<=theta'(t)<=C_0 ell.                    (7)

In particular theta is strictly increasing. Its image has length at
most C_0 H ell. A measurable periodic set of length epsilon_delta
per period intersects that image in length at most
(C_0 H ell/(2pi)+2)epsilon_delta: split into full periods and at most
two remaining pieces. Changing variable by theta and using its lower
derivative bound yields

    E 1_{theta(t) modulo 2pi in E_delta}
      <= [(C_0/(2pi c_0))+2/(c_0 H ell)] epsilon_delta.
                                                               (8)

This is a deterministic bound for the actual height marginal. It
requires no independence of theta, rho, g_H, w, or A_H, no limiting
phase distribution, and no derivative bound on g_H or w.

### Complete observable error and the order of limits

Fix delta>0 and call the complement of the set in (8) good. There
|D_i(M_*)|>=g_- c^2 m^2 delta. The two comparisons (4) imply,
for all sufficiently large H depending on this fixed delta, that
M_H and M_H^0 have the same diagonal-gap sign pattern as M_* and
their gap magnitudes are at least half that lower bound. Here
|D_i(M)-D_i(N)|<=2||M-N|| suffices. The two-stage continuity result
then gives

    max_i |u_i-u_i^0|=o_delta(1)

uniformly on the good heights. Together with (2) and the uniform
norm bounds this proves max_i |V_i-V_i^0|=o_delta(1) there.
All V_i,V_i^0 lie in a fixed compact ball, on every height including
ties. Q is smooth, hence bounded and uniformly continuous on that
ball. The good-height contribution to |B_H-B_H^0| is o_delta(1).

On the exceptional heights use only this fixed bound on |Q| and
0<=w<=1, retaining every equality branch exactly. Equation (8) gives

    |B_H-B_H^0|<=o_delta(1)+C epsilon_delta          (9)

for a constant C independent of delta and eventual H. First let H
tend to infinity with delta fixed; then let delta decrease to zero.
The limsup in (9) is zero, proving (1). There is no choice of a
shrinking arc before establishing uniformity and no unproved estimate
across a tie. The basis may jump there; its total possible contribution
has been bounded instead.

Finally L424 already retains the high and intermediate components and
the bounded translation, giving E_nu Q(X/sqrt(ell))=B_H+O(ell^-1).
Adding (1) proves the stated complete-law consequence. The leading
matrix (3) was used only to locate small exceptional sets; the
comparison observable still uses actual J and all other exact data.
Neither its value nor the later actual-height averaging problem has
been solved. The main global mixed-positivity gap remains unchanged.

### Separate critical audit — 2026-10-17, step 182

This RESEARCH / REPRODUCTION / proof_audit uses the prior EXPLORE
assessment `drafts/literature/2026-10-17-bulk-covariance-removal-audit.md`.
The audit checks this completed comparison, rather than importing a
general continuity theorem for an arbitrary Schur--Horn representative.
No defect was found in (1)--(9). This certifies the local comparison,
not a new theorem beyond the sources checked or any value of B_H^0.

**Exact inputs and normalization.** L423 (9)--(10) supplies bounded
m, the full symmetric constant matrix A_H=O(sqrt(ell)), and fixed
positive bounds for g_H. In particular A_H itself need not tend to
zero, and none of its even or odd entries may be discarded first.
The perturbation to g_H K is A_H/ell=O(ell^-1/2). K is positive
definite: its middle eigenvalue is 1/12 and its outer block has
positive trace 81/80 and determinant 1/180. Thus the compact positive
family required by the cited Carlsson formula is precisely the
normalized one. Repeated positive eigenvalues do not invalidate its
divided differences. A finite cover gives one constant in (2),
uniform in H and t. Expanding

    T_H J T_H-T_H^0 J T_H^0
      =(T_H-T_H^0)J T_H+T_H^0 J(T_H-T_H^0)

checks the first bound in (4) using bounded J and both square roots.

The complete L390 response triple is (ca,-ch/2,-ca/4)+O(1/L),
where a+ih=RZ, and its exact curvature term is
4q(xv_1-yv_0)^2/L^2. Polynomial dependence on the bounded response
triple makes its quadratic coefficient error O(1/L), and the
curvature coefficients are O(1/(t^2 L^2)). Since L>=ell on the
dyadic interval, this proves the operator error in (3), including
zeros of the real response projections. Expanding the leading
quadratic gives x^2 C^2/16-y^2 C^2+z^2 C^2,
xy coefficient -CS/2, xz coefficient C^2/2+S^2,
and yz coefficient 2CS. Halving the three cross coefficients gives
exactly J_* in (3). Bounded T_H^0 then proves the other bound in (4).
Here R has L369's phase of Q, not the phase of Qb; b's derivatives
are already included in the complete response estimate.

**The literal two-stage rule.** For a strict pair put
A=M_jj-tau>0 and B=tau-M_ii>0. The stated eta is the positive
root of A eta^2+2M_ij eta-B=0. On |D_i|>=b it has denominator
at least b and radicand at least b^2; a zero off-diagonal is harmless.
Its displayed vector has Rayleigh value tau and its displayed
orthogonal companion has unit length. In the ordered complementary
basis (companion,e_k), the second diagonal is exactly M_kk.
The first is 2tau-M_kk, because the complementary trace is 2tau.
Their gaps are therefore (-D_k,D_k). For D_k>0 the first vector
of that complementary basis is the low one; for D_k<0 the second
is the low one. Applying the same positive-root formula in that
low/high order checks both complementary branches, with the same
denominator and radicand lower bounds. Keeping each fixed original
pair order and each complementary order gives continuous labeled
vectors on each strict sign region. No eigenvalue simplicity is used.

The norm-bounded closed regions with |D_i|>=b are compact, so their
finitely many continuity moduli have a common modulus. Moreover
|D_i(M)-D_i(N)|<=2||M-N||, which prevents a sign change for close
matrices away from the gaps. Positive scalar multiplication preserves
tau comparisons and eta, at both stages and at equality. Thus the
normalized matrices really do give the prescribed original bases.
At a first-stage equality L419 selects a coordinate vector; at a
complementary equality it keeps the complementary basis, even if its
off-diagonal is nonzero. These cases need not be continuous. They
are retained and bounded on the exceptional set below, not omitted.

**All three possible ties.** For the outer block B of K,
det B=d^2=1/180 and tr B=81/80. Cayley--Hamilton gives
(B+dI)^2=(81/80+2d)B, and B+dI is positive definite. This verifies
the positive square root (5), including its off-diagonal sign.
At theta=pi/2 the transformed diagonal is as displayed and its
sum is -[81/80+2d]/(12D^2)=-1/12. After subtracting -1/36,
the first numerator is D^2-3(1+d)=-159/80-d; the third is
D^2-3(1/80+d)=39/40-d. These are exactly (6), and the middle
coefficient is 1/36. None vanishes. The row supports of P exclude
CS from every diagonal, so these checks apply to the full functions
F_i=A_i cos^2(theta)+B_i sin^2(theta), not just sampled phases.
Each zero set is finite, including any multiple zeros. Compactness
away from that finite union proves epsilon_delta tends to zero;
no numerical root locations or unproved simple-zero assumption enter.

**Actual-height exceptional measure.** L368's full right-line series
and Euler logarithm give |Z|>=m>0 and |Z'|<=M_1 on the ray.
Since the ray is an interval and RZ is smooth and nonvanishing, a
smooth argument lift exists. Its derivative is exactly
phi'+Im(Z'/Z). L369 (6) therefore gives
theta'=log(t/(2pi))/2+O(1), with one uniform error constant.
On every sufficiently high [H,2H] this proves both positive bounds
in (7); no hypothesis on a critical-strip zero is needed.
For any measurable periodic set of length epsilon per period, an
image interval of length D meets at most floor(D/(2pi)) complete
periods and two partial periods, whose intersections each have
length at most epsilon. Applying the inverse change of variable,
whose derivative is at most 1/(c_0 ell), proves (8) with
D<=C_0 H ell. This includes endpoints and arbitrary measurable
exceptional sets. It is a bound for the actual phase preimage, not
a product measure or a claim of phase independence.

**Uniform observable control and quantifiers.** Fix delta>0 first
and write a_delta=g_- c^2 m^2 delta. On good heights all leading
gaps have magnitude greater than a_delta. The errors (4) tend
uniformly to zero, so both exact matrices eventually have those
same signs and gaps at least a_delta/2. The compact-branch modulus
with b=a_delta/2 and (2) give uniform convergence of the labeled
V_i-V_i^0 on good heights. All these vectors have norm at most a
fixed R even on bad heights, because both normalized square roots
are bounded and every selected vector is a unit vector. If
K_Q=sup_{|v|<=R}|Q(v)|, the bad part of the difference is at most
2K_Q times its height probability: the factor w/3 and the three
terms introduce no additional growth. Equation (8) thus proves
(9) with one constant independent of delta, without any regularity
assumption on w or g_H. Taking limsup as H tends to infinity at
fixed delta, followed by delta decreasing to zero, proves (1).
There is no assertion of a quantitative rate uniform in delta.

Finally L424 (4) is used at its exact normalization X/sqrt(ell),
with the unchanged high/intermediate parts and the bounded paired
bulk translation. Its O(ell^-1) remainder tends to zero. This
checks the stated complete-law consequence without imposing the
original moment constraints on the comparison states. The audit
does not sign B_H^0, certify a transport defect, assume actual
critical-function realization, or address clipping and the regulator
margin. The step-175 numerical-signing stop remains in force.

## Mathlib

Full matching coverage for this prescribed-basis, H-dependent comparison
has not been checked. The nonsingular square-root input is cited precisely
above; L419's named real Schur--Horn existence theorem is inherited,
while its exact coordinate algorithm is analyzed here. Generic matrix,
continuity and change-of-variable support would not alone formalize the
complete result. Unknown coverage is not evidence of absence; no Lean
verification is claimed.
