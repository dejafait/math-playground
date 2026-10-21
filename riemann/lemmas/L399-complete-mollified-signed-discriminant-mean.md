# Lemma 399: the complete sharp mollified signed discriminant mean is negative

## Hypotheses

Use the fixed actual functions F=F_0, G and positive envelope A of L395,
with its carrier R=Q/A, |R|=1. These are the actual functions, not an
arbitrary real-analytic pair. On the positive ray set T=1+t,
L(t)=log(2+t), f=F/A, and retain ordinary height derivatives. Define

    mathscr L(u)=u'^2-u u'',
    B_*=2F'G'-FG''-F''G,
    D=B_*^2-4 mathscr L(F) mathscr L(G),
    Delta=D/(A^4 T^4 L^4).

This is exactly L370 (1)'s normalized physical discriminant. In the
notation of L395 put

    x=f, y=f'/L, z=f''/L^2, E=R^2, c=1/(4 pi),
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-i y)^2/2,
    Z_+(t)=zeta(5/2+it),
    d=c^2 (M |Z_+|^2 + Re(K E Z_+^2)).

For real H>1 use precisely the undifferentiated mollifier

    Y=H^(1/100),
    P_H(t)=sum_(a<=Y) mu(a)a^(-1/2-it)(log(Y/a)/log Y)^2.

All integrals below are sharp on the real interval [H,2H]. No RH,
zero simplicity, noncoincidence, phase independence, discriminant sign,
common-zero bound or growing response cutoff is assumed.

## Conclusion

The complete signed physical mean has the limit

    lim_(H->infinity) H^(-1) integral_[H,2H] Delta(t)|P_H(t)|^2 dt
      = -c^2 (10282/1125) zeta(5)
      = -5141 zeta(5)/(9000 pi^2) < 0.                    (1)

There is no extra division by log H. The complete mean is consequently
negative for every sufficiently large real H, with an existential onset.
This stops this specified mollifier as a positive-leading-mean witness.
It does not prove an eventual pointwise sign of D, control positive D
values or common zeros, give a total L367 pencil margin, extend an
actual-theta positivity or zero-exclusion range, or resolve RH.
No effective convergence rate for the full response is asserted.
The separate step 78 critical audit below validates this assembly.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-complete-mollified-signed-mean.md`.
This is local REPRODUCTION using already audited components. It supplies
only their physical assembly and an ordered-limit argument; no analytic
moment theorem or component coefficient is reproved.

### Imported components and their applicability

L395 (2)–(3), separately audited at step 61, gives constants C>0 and
H_0 independent of every integer N>=1 such that, for H>=H_0,

    |I(H)-J(H)| <= C/log H,
    |J(H)-J_N(H)| <= C eta_N,                            (2)

where I(H) is the mean in (1), J(H) is the same mean with Delta replaced
by d, Z_N=sum_(r<=N)r^(-5/2-it),

    d_N=c^2 (M |Z_N|^2 + Re(K E Z_N^2)),
    J_N(H)=H^(-1) integral_[H,2H] d_N |P_H|^2,
    eta_N=sum_(r>N)r^(-5/2).

The signed comparisons (2) follow from L395's absolute weighted bounds
by the integral triangle inequality. Its physical estimate retains all
response derivatives and the common-envelope curvature before replacing
response values in d. Its uniform tail constant follows from the weighted
jet mass bound and absolute convergence on Re s=5/2, not from a
fixed-head moment constant. Thus (2) applies simultaneously for every N.

For each fixed N, define the two actual projections

    B_N(H)=H^(-1) integral_[H,2H] M |Z_N|^2 |P_H|^2,
    C_N(H)=H^(-1) integral_[H,2H] Re(K E Z_N^2)|P_H|^2.

They have identical ordinary jets, mollifier and sharp endpoints to the
component lemmas. L397's conclusion, using the audited L396 reduction
and the separate step 70 limit audit, gives C_N(H)->0 at fixed N.
L398's separately audited step 74 conclusion gives

    B_N(H)=b_N+O_N(1/log H),
    b_N=-(10282/1125) sum_(r<=N)r^(-5).                   (3)

In (3) both functional-equation diagonals and all ordered response twists
have already been evaluated. In C_N both sharp carrier connectors and
the growing mollifier were retained by L396/L397. Neither component
contains the external factor c^2. No component error bound uniform in
growing N is required or assumed.

For precise source provenance, the analytic inputs imported by these
components are H. M. Bui and R. R. Hall, *On the derivatives of Hardy's
function Z(t)*, arXiv:2304.05178v1 (11 April 2023), Proposition 1 and
(6)–(8), printed pp. 6–8,
[primary paper](https://arxiv.org/html/2304.05178v1#S3);
M. P. Young, *A short proof of Levinson's theorem*, Arch. Math. 95 (2010),
539–548, DOI 10.1007/s00013-010-0199-9, Lemmas 3–7, (6.1)–(6.4) and
Section 7, pp. 540–547,
[published paper](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf);
and S. Baluyot and S. M. Gonek, *Explicit formulae and discrepancy
estimates for a-points of the Riemann zeta-function*, Pacific J. Math.
303 (2019), 47–72, DOI 10.2140/pjm.2019.303.47, Section 2, p. 53,
before (2-3),
[published reciprocal-zeta bound](https://msp.org/pjm/2019/303-1/pjm-v303-n1-p02-p.pdf#page=9).
The primary statements and relevant proof cases are those already
inspected in the reused assessments; no new source retrieval or direct
Titchmarsh book inspection is claimed. Bui–Hall permits the actual
P(u)=u^2 and exponent 1/100. Young's fixed-N twist range and the classical
reciprocal bound are checked in the components, including their ordinary
jet, finite-prime and endpoint specializations. Sources supply the tools;
the component proofs supply these specific statistics. A direct source
citation alone would not establish (1).

### Fixed-head physical assembly

Linearity of each finite integral gives the exact identity

    J_N(H)=c^2 (B_N(H)+C_N(H)).                          (4)

Thus (3) and the fixed-N carrier zero limit imply

    lim_(H->infinity) J_N(H)=a_N,
    a_N=-c^2 (10282/1125) sum_(r<=N)r^(-5).              (5)

The carrier projection has been included and evaluated, not discarded by
phase independence. The physical factor is c^2, not c^4; the latter
belongs to a square-moment problem. The envelope correction is included
in (2)'s physical replacement, so (4) does not drop it from I(H).

### Full response by an explicit epsilon argument

Absolute convergence gives a_N->a_infinity, where

    a_infinity=-c^2 (10282/1125) zeta(5).

The elementary integral comparisons, for every integer N>=1, give

    eta_N <= 2/(3 N^(3/2)),
    |a_N-a_infinity| <= c^2 (10282/1125)/(4 N^4).        (6)

Given epsilon>0, first choose one fixed N so large that

    C eta_N + |a_N-a_infinity| < epsilon/2.

This is possible by (6), with C the N-independent constant in (2).
For this chosen N, (5) and 1/log H->0 give a real H_epsilon>=H_0
such that for every H>=H_epsilon,

    C/log H + |J_N(H)-a_N| < epsilon/2.

Now (2) and the triangle inequality give, for every such H,

    |I(H)-a_infinity|
      <= C/log H + C eta_N + |J_N(H)-a_N| + |a_N-a_infinity|
      < epsilon.

This proves existence and the value of the actual full-response limit.
H_epsilon may depend on the fixed N selected from epsilon. No choice
N=N(H), interchange of infinite limits or uniform fixed-head rate is
made. All mollifier cutoff changes as real H varies are already covered
by the component statements for real H.

Finally c^2=1/(16 pi^2), so 10282/(1125*16)=5141/9000.
The Dirichlet series zeta(5)=sum_(r>=1)r^(-5) is finite and strictly
positive. Hence a_infinity<0. Taking epsilon=|a_infinity|/2 in the
proved limit gives I(H)<0 for every sufficiently large real H.
That is an averaged sign with a nonnegative weight, not a pointwise sign
assertion. It settles the proposed positive-mean diagnostic adversely
while leaving the independent main gaps unresolved.

### Separate critical audit — 2026-10-12, step 78

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-complete-mollified-mean-audit.md`
authorizes this REPRODUCTION audit. The complete sharp limit (1) passes
under its stated hypotheses. This validates the assembly of the already
audited components; it does not independently reprove their analytic
moment theorems or claim a result beyond the sources checked.

**Exact statistic and physical factor.** Squaring L370 (1)'s normalized
B_* and multiplying its two Laguerre coefficients give the same positive
denominator A^4 T^4 L^4. Hence its Delta is precisely the statistic here,
on the positive ray where T=1+t. In L395 the normalized response triple
has leading value c(a,-h/2,-a/4), with a+ih=R Z_+. Each discriminant
term is quadratic in that triple, so its external factor is c^2.
L390's polynomial identity gives exactly the displayed M and K; E=R^2
converts (a+ih)^2 into E Z_+^2. Thus the real projection is not a
modulus square. The common-envelope curvature and the ordinary response
derivatives belong to L395's absolute physical error, not an omitted
third leading projection. All formulas are zero-safe.

**Absolute comparisons with simultaneous constants.** L395 (1)–(3)
state one onset and constants valid for every integer N>=1. Their proof
uses only the fixed scalar mollified moments and the full absolute
response series to obtain the weighted bound for U=x^2+y^2+z^2.
The polynomial estimates give |M|+|K|<=2U. If B_0=zeta(5/2), both
response-square differences are at most 2 B_0 eta_N, because |Z_+|
and |Z_N| are at most B_0. Consequently

    |d-d_N| <= 4 c^2 B_0 eta_N U

holds before integration, without any N-dependent constant. The physical
bound is |Delta-d|<=C_0 U/L(t), and L(t)>=log H. Integration against
the nonnegative |P_H|^2 proves exactly the two signed comparisons (2).
There is no substitution of an unweighted norm for a weighted one, no
sign assumption on M, and no differentiated response tail left behind.

**Both fixed-head projections.** L396 (2) and L397's conclusion apply
to exactly Re(K E Z_N^2)|P_H|^2 on sharp [H,2H]. Their retained ordinary
jets, real cutoff Y=H^(1/100), collision multiplicities, and fixed-N
quantifiers agree with C_N here. L396's two powers of H after substituting
Y are strictly negative, and L397's diagonal tends to zero. Neither
statement carries an external c^2. L398's conclusion is exactly B_N,
again without c^2. Its proof expands every ordered r,s pair; after both
functional-equation diagonals are combined, the constant coefficient
vanishes for r!=s, and the surviving r=s weight is r^(-5). Its separate
audit controls both endpoint bumps in absolute weighted jet mass, so a
signed smooth-to-sharp inference is not being used here. In particular,
the O_N(1/log H) error is for the same real H and actual Y, not a
mollifier of length (2H)^(1/100).

The imported scalar coefficient also passes the arithmetic check:
L398 (9)'s signed combination is

    (m_22+3m_02/2+m_00/16-m_11)/2
      = -1/4-4/(45 vartheta)-vartheta/15
      = -10282/1125,                 vartheta=1/100.

This checks its use in the assembly; the full fixed-twist analytic
evaluation remains the previously audited L398 input. Linearity now
gives exactly J_N=c^2(B_N+C_N). In particular no phase-independence
heuristic, extra factor two, c^4, or division by log H enters (5).

**Tail and limit quantifiers.** The decreasing positive functions
u^(-5/2) and u^(-5) bound their sums over integers greater than N by
their integrals over [N,infinity). These are 2/(3N^(3/2)) and
1/(4N^4), respectively, proving both inequalities in (6). Given any
epsilon>0, these bounds select a single integer N from epsilon and the
fixed L395 constant. Only after that choice do the fixed-N limits select
H_epsilon. The two pairs of errors in the displayed proof are each less
than epsilon/2 for every real H>=H_epsilon. Thus the argument proves an
ordinary full-response limit, not merely a subsequential or iterated
formal limit. N-dependent component errors and onsets cause no problem;
no bound for N=N(H) is used. The components already cover the real cutoff
and sharp interval as H varies.

Finally 10282/(1125*16)=5141/9000 and zeta(5)>0. The negative constant
is therefore unchanged. Taking half its absolute value as epsilon
justifies eventual negativity of this weighted mean. It validates the
specified positive-leading-mean witness stop, with no inference to an
eventual pointwise sign, positive-value exclusion, total L367 margin,
common-zero upper bound, global mixed positivity or RH. The audit found
no normalization, hypothesis, projection, tail or quantifier defect in
the approved assembly. Its direct mathematical inputs remain L370,
L395, L397 and L398; the L390/L396 information is used through those
components, so no DAG edge changes are required.

## Mathlib

Full matching coverage for this mollified physical mean and the analytic
component theorems has not been checked. No library absence or Lean
verification is claimed. Integral linearity, triangle inequalities,
summable Dirichlet tails and elementary limit arguments are supporting
ingredients, not replacements for the cited moment inputs. This is a
local assembly of known-source specializations, not an originality claim
or an RH candidate. Step 78 validates the local physical assembly and
ordered-limit argument; it does not constitute library verification.
