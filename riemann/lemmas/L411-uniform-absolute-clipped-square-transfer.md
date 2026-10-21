# Lemma 411: uniform absolute clipped-square physical/head transfer

## Hypotheses

Use the fixed actual real functions F=F_0,G and positive gamma envelope A
of L390/L405, on t>=40. Every prime below means an ordinary height
derivative taken before normalization. Define

    T=1+t, L=log(2+t), f=F/A, (x,y,z)=(f,f'/L,f''/L^2),
    U=x^2+y^2+z^2, c=1/(4pi), R=exp(i phi), E=R^2,
    Z=zeta(5/2+it), b=z-x/4,
    M=(z^2+3xz/2+x^2/16-y^2)/2, K=(b-iy)^2/2,
    d=c^2[M|Z|^2+Re(K E Z^2)],
    B0=-c[b Re(RZ)+y Im(RZ)],
    Bcal=(2F'G'-FG''-F''G)/(A^2 T^2 L^2),
    Delta=[(2F'G'-FG''-F''G)^2
           -4(F'^2-FF'')(G'^2-GG'')]/(A^4 T^4 L^4).

The phase R is the actual gamma carrier, of modulus one on the real ray.
For every integer N>=1 set Z_N=sum_(n<=N)n^(-5/2-it), and define d_N
and B0_N by replacing Z by Z_N in the displayed formulas, exactly as
in L409. Put eta_N=sum_(n>N)n^(-5/2), ell=log H and r_-=max(-r,0)
for real r. The physical response G and its first two derivatives are
complete, not truncated. There is no RH, sign, independence, small-value
distribution or growing-head moment assumption.

## Conclusion

There exist C>0 and H_0>=40, independent of N, such that for every real
H>=H_0 and every integer N>=1,

    (1/H) integral_[H,2H]
       |Delta (Bcal_-)^2-d_N (B0_N_-)^2| dt
          <= C[ell^3+eta_N ell^4].                       (1)

This is a local REPRODUCTION specialization of the audited envelopes
and standard contraction. Constants and onset are existential. The separate
step-128 critical audit below validates (1). It removes absolute physical/head transfer
at quartic scale but evaluates no clipped signed coefficient. The total
regulator-pencil margin, actual common-zero upper counts, global mixed
positivity and RH remain unresolved.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-14-clipped-square-absolute-transfer.md`;
its COVERED_TARGET is exactly (1). Reuse its primary source comparison,
duplicate check and step-99 failure distinction. L405 proves the nearby
unclipped replacement, not (1). The specialization below is needed because
the clipped square is neither a polynomial nor globally Lipschitz with a
constant independent of its arguments. No new moment theorem is needed.

### Imported contraction and analytic envelope

Import negative-part contraction from Mathlib4, commit
`a63713524b66f0b5681eaa2bfa83e7218c5cdbe5`,
[Topology/MetricSpace/Lipschitz.lean, LipschitzWith.max_const and lipschitzWith_max](https://github.com/leanprover-community/mathlib4/blob/a63713524b66f0b5681eaa2bfa83e7218c5cdbe5/Mathlib/Topology/MetricSpace/Lipschitz.lean).
Negation is an isometry of R; max-with-zero preserves its Lipschitz
constant one. Hence for all real r,s, including r=0 or s=0,

    |r_- - s_-|<=|r-s|, 0<=r_-<=|r|.

The difference-of-squares identity therefore gives

    |(r_-)^2-(s_-)^2|<=|r-s|(|r|+|s|).                  (2)

This last inequality is the elementary weighted square specialization,
not an assertion of global Lipschitz continuity of the square.

Audited L390 (4)--(5), L405 (5)--(6) and L406 (6)--(7) supply, on
one fixed eventual ray,

    |Delta-d|<=C_1 U/L, |Delta|+|d|<=C_1 U,
    |Bcal-B0|<=C_1 sqrt(U)/L,
    |Bcal|+|B0|<=C_1 sqrt(U),
    (1/H) integral_[H,2H] U^2 dt<=C_2 ell^4.             (3)

Here C_1,C_2 and the onset are fixed for the actual family and contain
no N. These are pointwise absolute errors, valid at vanishing jets.
In particular the discriminant retains the exact correction
4q(xv_1-yv_0)^2/L^2, and the polarization retains -2q x v_0/L^2,
where q=(log A)''=O(T^(-2)) and v_j=(G/A)^(j)/(T^2 L^j).
Their sizes are respectively O(U/(T^2 L^2)) and
O(sqrt(U)/(T^2 L^2)), already included in (3). All ordinary response
derivatives and their absolutely convergent right-line series were
retained before the leading value replacement.

The last bound in (3) imports only the pure fixed orders j=0,1,2
of Bui--Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Theorem 3 and defining quartic asymptotic](https://arxiv.org/html/2304.05178v1),
through L390's audited ordinary-jet conversion. The ordinary fourth
moment has logarithmic exponent 4+4j; division by L^(4j), comparable
to ell^(4j) on the dyadic interval, leaves O(ell^4). The inequality
U^2<=3(x^4+y^4+z^4) gives the stated envelope. This is an imported
quartic bound, not a reproof of the source or a higher-moment premise.

### Physical replacement

An exact product subtraction, (2) and (3) imply

    |Delta (Bcal_-)^2-d (B0_-)^2|
      <=|Delta-d| (Bcal_-)^2
           +|d| |(Bcal_-)^2-(B0_-)^2|
      <=C U^2/L.                                      (4)

Indeed the first term is bounded by (C U/L)(C sqrt(U))^2,
and the second by (C U)(C sqrt(U)/L)(C sqrt(U)). Neither
term requires a sign for Delta or d. No clipping is differentiated.

### Head replacement with a common constant and onset

Set M_0=zeta(5/2), a fixed finite constant. Absolute convergence on
Re s=5/2 gives for every real t and every N>=1

    |Z|,|Z_N|<=M_0, |Z-Z_N|<=eta_N,
    ||Z|^2-|Z_N|^2|<=2M_0 eta_N,
    |Z^2-Z_N^2|<=2M_0 eta_N.                           (5)

Cauchy--Schwarz in the real jet vector gives
|b|+|y|<=C sqrt(U), and the displayed polynomials give
|M|+|K|<=C U. Since |R|=|E|=1, direct subtraction using (5) yields

    |d-d_N|<=C eta_N U, |d|+|d_N|<=C U,
    |B0-B0_N|<=C eta_N sqrt(U),
    |B0|+|B0_N|<=C sqrt(U).                            (6)

For example |B0-B0_N| is at most
c(|b|+|y|)|Z-Z_N|. These constants depend only on fixed polynomial
coefficients and M_0, so none depends on N or on a head asymptotic.
These are value-tail estimates; full derivative errors have already
been treated in (3). Applying (2) once more,

    |d (B0_-)^2-d_N (B0_N_-)^2|
      <=|d-d_N| (B0_-)^2
           +|d_N| |(B0_-)^2-(B0_N_-)^2|
      <=C eta_N U^2.                                  (7)

This also holds when Bcal, B0 or B0_N crosses or equals zero.
If U=0, all quantities in (3) and (6) vanish, so the same bounds
apply with no division by sqrt(U).

### Sharp integration and limits

Choose H_0 as the common onset of the finitely many physical and moment
bounds in (3). The head bounds (5)--(7) need no additional onset.
On [H,2H], L>=ell>0. The triangle inequality, (4), (7) and (3) give

    (1/H) integral |Delta (Bcal_-)^2-d_N (B0_N_-)^2|
      <=C(1/ell+eta_N)(1/H) integral U^2
      <=C C_2(ell^3+eta_N ell^4).

Absorb the fixed C_2 into C to prove (1), with the required quantifiers.
Integration is over the whole sharp interval; no smoothing, discarded
endpoint strip, signed contour shift or exchange of infinite sums is used.
Continuity of the functions and of negative-part clipping makes the
integrands integrable on every such compact interval.

For the downstream interpretation, define I(H) as the physical signed
mean normalized by H ell^4 and J_N(H) as the corresponding d_N/B0_N
signed mean. Then (1) proves

    |I(H)-J_N(H)|<=C(1/ell+eta_N),
    lim_(N->infinity) limsup_(H->infinity)|I(H)-J_N(H)|=0.

This does not assert existence or sign of any limit of J_N(H).
Although the absolute estimate itself holds for every N at each H,
a subsequent fixed-twist source application must still take H first
at fixed N, then N to infinity. No growing-head moment theorem follows.
The achieved errors meet exactly the approved threshold. The signed
step-99 blocker and L410 moment-only obstruction remain unchanged.

### Separate critical audit — 2026-10-14, step 128

This REPRODUCTION proof_audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-clipped-square-transfer-critical-audit.md`.
It validates the stated bound without changing its hypotheses, scale or
direct mathematical inputs. The cited contraction and Bui--Hall theorem
are imported under the already inspected source coverage, not reproved.
The following checks concern the full real physical functions.

**Compatible physical inputs.** L390's exact normalized minors are
a_1=xv_1-yv_0, a_2=xv_2-zv_0, a_3=yv_2-zv_1. Its identity is
Delta=a_2^2-4a_1 a_3+4q a_1^2/L^2. L405's distinct polarization
identity is Bcal=2y v_1-xv_2-zv_0-2q x v_0/L^2. Thus both
curvature signs and both powers of L in (3) agree with the physical
normalizations in the hypotheses. No division by a function or jet occurs.

The complete response is differentiated before normalization. In L390,
its exact quadratic factor is (t^2/4-3/16-it/2)/pi, with derivatives
(t/2-i/2)/pi and 1/(2pi). The product rules retain both derivatives
of R and every term of Z,Z',Z'', whose absolute series bounds are
sum n^(-5/2)(log n)^j for j<=2. Together with the audited phase
bounds these give a bounded response triple and error O(1/L) from
(ca,-ch/2,-ca/4). Each minor error is O(sqrt(U)/L), so the
quadratic discriminant error is O(U/L); the polarization error is
O(sqrt(U)/L). The leading polynomials are exactly d and B0 with
the signs displayed here. The curvature errors have the smaller sizes
stated in (3). L406 confirms compatibility but its power-three moment
is unused. Only L409's head definitions, not its cubic mean, enter.

**Quartic envelope.** L390 uses f equal to a constant sign times the
ordinary Hardy function (L389's exact identification). Hence its ordinary
derivatives of fixed orders j=0,1,2 inherit the cited Bui--Hall bound
integral_40^X |f^(j)|^4 <= C_j X(log X)^(4+4j). Restricting this
nonnegative integral to [H,2H] and using L>=ell gives
H^(-1) integral |f^(j)/L^j|^4 <= C'_j ell^4. The three finite
constants have a common onset. U^2<=3(x^4+y^4+z^4) proves the
last part of (3); no mixed-moment sign, sixth moment or asymptotic
uniform in a derivative order is needed.

**Both product errors, including zeros.** Choose a single K_*>=1
bounding each individual size/error in (3) and (6), without the moment
bound. Such K_* is independent of N: (6) uses only the fixed coefficients,
|R|=1 and M_0=zeta(5/2). For real r,s, the imported contraction and
difference of squares give (2), also when r or s is zero or their signs
differ. Therefore the two terms in the physical subtraction (4) have
bounds K_*^3 U^2/L and 2K_*^3 U^2/L. The two terms in the head
subtraction (7) have bounds K_*^3 eta_N U^2 and 2K_*^3 eta_N U^2.
These follow from exact product identities; neither signed factor is
silently replaced by a nonnegative one. At U=0 all physical and leading
quantities vanish by (3) and (6). No exceptional set or relative error
is needed anywhere, including crossings of any clipping threshold.

**Uniform quantifiers and sequential meaning.** Choose H_0 to exceed
the fixed physical and quartic onsets and 40. All head inequalities
hold at every real t and every N>=1; no additional onset depends on N.
Integration bounds the absolute difference by
3K_*^3 C_2(ell^3+eta_N ell^4), proving exactly (1) on the sharp interval.
Every integrand is continuous, so the endpoints create no exception.
For the normalized signed means, the absolute integral bounds
|I(H)-J_N(H)| by C(ell^(-1)+eta_N). Given any tolerance, choose
N with C eta_N below half that tolerance, then H with C/ell below
the other half. Since eta_N tends to zero by absolute convergence,
this proves the displayed iterated limsup comparison. It establishes
neither existence nor sign of a fixed-N mean. The uniform error also
does not furnish a growing-head asymptotic for that mean.

The approved audit threshold passes without a mathematical correction.
This verifies the local known-tool specialization; it supplies no new
source theorem, clipped coefficient, sign range or RH consequence.
No mathematical script is needed for these exact inequalities. The
signed-clipping stop and all independent regulator/count/positivity gaps
remain unchanged.

## Mathlib

Supporting negative-part contraction is present via the two precisely
cited max theorems above. Full matching coverage for the actual transfer,
ordinary Hardy quartic moments and physical gamma normalization is not
checked. This informal specialization is not a Lean verification, a new
source theorem, a certified originality claim or an RH resolution.
