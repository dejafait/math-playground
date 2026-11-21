# Pairing source review1338

17 November 2026. One literature comparison; outcome NEGATIVE for the
citation-only route, not a mathematical disproof or a new theorem.
The matching assessment is
[comparison1338](literature/2026-11-17-min-kang-pairing-source-nomination-1337.md).

## Question and threshold

L030-L032/C032a require actual-Xi algebraic-square mixed positivity.
The saved intermediate target, for d>=1, explicitly assumes
H_(d-1)=(S_(a+b+2))_(0<=a,b<d)>0 and asks for

    S_(2d+2)-v_d^T H_(d-1)^(-1)v_d >= 0,
    v_d=(S_(d+2),...,S_(2d+1))^T.

Such an independent estimate could pay one nonsingular extension.
Initialization, singular blocks, all degrees and analytic realization
would remain. Continue only with a precise independently signed identity
or bound; park a source offering only equivalence and zero-data transfer.
No Schur calculation is performed here.

## Primary source and normalization

Saha Min and Seojun Kang, *A Two-Variable Pairing Representation and a
Hankel-Stieltjes Reformulation for the Riemann Xi-Function*, v1,
23 September 2026, [primary PDF](https://www.alphaxiv.org/abs/2609.riemann-xi-pairing-hankel-stieltjes.pdf).
Printed page numbers below are one greater than zero-based PDF indices.

Read Section2.1/(2.1)-(2.4), p2; Theorems3.2/3.3 with proofs, pp3-5;
Section4 and full proofs, pp5-7; Section7 and full proof cases, pp9-12;
Section8/AppendixB, pp12-13. Section5's low-order/formal formulas were
viewed, not independently audited. References to external verification,
zero-free constants and Ingham are source inputs, not independently
revalidated numerical or analytic certificates in this step.

Comparison with the full L019/L021/L024/L025/L030 proofs gives the
normalization dictionary (definition comparison only):

    Phi(u)=K(u)/2 (u>=0),  xi(1/2)=M_0,
    p(x)=K(|x|)/(2M_0),
    M(z)=xi(1/2+z)/xi(1/2)=Xi(-iz)/M_0,
    F(z^2)=xi(1/2+z),  R=F'/F,
    source m_n = local S_(n+1).

The last identification compares the source's alternating R-series
(3.3) with L025's normalized local logarithm after z maps to -iz.
It uses the locally convergent expansions only, not real zeros or a
global logarithm. Thus L030's matrix is the source's shifted Hankel
family, with the corresponding size convention. The positive raw
kernel moments of L021 are not those logarithmic moments.

## Pairing statements and proof cases

Section4/(4.6)-(4.8), Lemma4.1, pp5-6, uses z=a+ib, a,b>0:

    P(a,b)=integral_R^2 e^(a(x+y))
       [a(x-y)sin(b(x-y))-b(x+y)cos(b(x-y))]p(x)p(y) dx dy,
    J(z)=M'(z) conjugate(M(z)),
    P=2[a Im J-b Re J],
    P=4|z|^2 |M(z)|^2 Im R(z^2)  if M(z)!=0.

The essential proof uses compact exponential domination, conjugate
symmetry and exchange of x,y in the two real integrals, then (4.4)
M'/M=2zR(z^2). The undivided identity remains valid at a zero, where
J=P=0; the divided formula does not. Remark4.3 also writes
P=-(b partial_a+a partial_b)|M|^2.

Theorem4.2, pp6-7, is an equivalence. Its forward proof assumes RH
and the Stieltjes measure of Theorem3.2, with nonzero mass at positive
tau; this supplies strict negative imaginary part. Its reverse proof
uses positivity of M on the real axis and reflection to put a hypothetical
off-line zero in the first quadrant, then uses the undivided identity
P=0. It does not prove negativity from p>=0. Corollary4.4 gives the
fixed-a boundary expansion with coefficient 8a^3 M(a)^2 R'(a^2);
the expansion itself does not determine that coefficient's sign.

## Exact Section7 qualifications

Lemma7.3, pp9-10, writes a possible off-line pair in the square
variable as -A+/-iB, A=gamma^2-delta^2, B=2gamma delta,
0<delta<1/2, gamma>0. For u=x+iy, y>0, away from the pair's poles:

    pair contribution to Im R(u)=
      -2y[(x+A)^2+y^2-B^2] /
      ([(x+A)^2+(y-B)^2][(x+A)^2+(y+B)^2]).

The proof is the locally uniform genus-zero logarithmic-derivative
sum, combined in conjugate pairs. Possible nonnegative contributions
are confined to (x+A)^2+y^2<=B^2. Critical-line contributions are
strictly negative. The PDF's displayed reflected-zero label has a
missing conjugation in its text extraction; the displayed ordinates
and square-variable pair specify the intended reflected pair. No
result here relies on reading 1-rho literally as an upper-half-plane zero.

Theorem7.4, p10, assumes all zeros through height H>=2 lie on the
line. With C_H=H^2-H-1/4 it proves P<0 for b^2-a^2<=C_H.
The proof uses gamma>H for remaining off-line zeros and A-|B|>C_H,
excluding every obstruction disk in that region. The boundary is
included. Its numerical specialization uses H=3*10^12 from
Platt-Trudgian. Corollary7.5 gives the corresponding flow sign and,
at that verified height, R'(x)<0 for x>=0. The latter proof separately
differentiates paired contributions and retains the A>|B| condition.

Proposition7.6, pp10-11, additionally assumes beta<=1-1/(R_0 log gamma)
for gamma>H, H=3*10^12. For L=b^2-a^2>C_H put

    Gamma(L)=1/2+sqrt(L+1/2), D_R0(t)=1/2-1/(R_0 log t).

Its sufficient condition is the strict inequality
ab>Gamma(L)D_R0(Gamma(L)). The proof bounds any dangerous pair by
ab<=gamma delta and gamma<Gamma(L), then uses monotonicity of
tD_R0(t). The published constant 5.558691 and preprint constant
4.896 are distinguished by the source; neither is a new local input.
There is no assertion at the equality boundary of this sufficient test.

Theorem7.8, pp11-12, fixes a>0 and H=3*10^12. Set

    alpha_H(a)=aH/sqrt(H^2+a^2), sigma_a=1/2+alpha_H(a),
    E_a(T)={b in [H,T]: P(a,b)>=0}.

For alpha_H(a)<1/2 it states
meas E_a(T) <<_a T^theta(a)(log T)^5, where
theta(a)=3(1-2alpha_H(a))/(3-2alpha_H(a))<1.
For alpha_H(a)>=1/2 it gives P<0 for every b>0.
Its proof solves the disk condition as a quadratic in b^2: a dangerous
pair requires delta>=a gamma/sqrt(gamma^2+a^2)>alpha_H(a).
It also gives |b-gamma|<=c_a=1+(a^2+1/4)/H, covers the exceptional
set by intervals of total length <=2c_a N(sigma_a,T+c_a), and invokes
Ingham's estimate. Poles/zero ordinates are exceptional too; a
measure-zero qualification does not exclude them pointwise. This is
fixed-a coverage, with no uniform a-down-to-zero exceptional-mass bound.

Section7.4 explicitly retains global kernel signing and both all-order
Hankel conditions as open. AppendixB's decimal determinants are not
interval enclosures or proof certificates. No finite computation is
imported here.

## Relevance, limits and route decision

The actual normalization matches, so this is not a rejected kernel
because of a scaling mismatch. The gap is mathematical: neither a
signed estimate for the displayed Schur residual nor a representation
with a paid exceptional contribution is in the inspected proof.
No source result permits discarding ordinates merely because their
set has density zero. No uniform limit/interchange or all-degree
moment bound is supplied for that purpose. These are missing inputs,
not a new theorem that no such bridge can exist.

Reuse the completed October31 Lorentz assessment and its fixed-x stop.
The undivided P identity is exactly the observable used there. Its
coordinate evolution does not improve the signed forcing, while this
paper's extra signs use zero data. The stronger finite-height region
does not remove the unbounded-height/all-degree requirement. No
previous domain stop is promoted to a global ban, and no attempt is
made to update zero-free frontiers or reprove known regions.

Queries: exact identifier with "4.6"; Min/Kang pairing Hankel with
"7.1". Local checks used the precise source title, the saved October31
transport assessment/stop, and the November17 discovery nomination.
The local covariance/contact and quartic-Fourier comparisons remain
different observables, not signs of this residual. No matching source
theorem or novelty claim emerged. Full/supporting Mathlib coverage is
unchecked. Shell PDF download failed DNS; browser PDF text was
accessible and supplied the complete essential passages, so this is
not SOURCE_BLOCKED. Screenshot calls returned no usable image; the
displaced theorem hypotheses were recovered in the complete PDF text.

Park citation-only pairing transfer. A creative central attempt is
not justified by these sources without an independent signed input.
For a different independently testable task, a narrow check found
no separate C032l audit in its canonical file or matching local
November17 records (C032k already has audit1302). Nominate C032l's
written finite-mixture obstruction for separate source-gate approval,
reusing review1301; do not redo C032k's audit or retry the stopped
finite-mixture construction. This is a surrogate-route integrity
check, with no promised sign advance. PROOF/DAG remain unchanged.
