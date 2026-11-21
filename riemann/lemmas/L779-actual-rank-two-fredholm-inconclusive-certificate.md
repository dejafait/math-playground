# Lemma 779: actual rank-two admissibility and repaired signed separation

## Hypotheses

Use the actual G and original complex Hilbert space in L776/L777,
with r=3, k=2, R=2048. Use L017/L018's entire theta integral and
L021's coefficient normalization. Arithmetic trusts the same documented
Python Decimal/mpdecimal contracts as L778: directed finite operations,
nearest correctly rounded exp/sqrt widened by adjacent values, and
allcr=1. The runtime reports Python3.15.2, Decimal1.70, libmpdec4.0.1;
the executable is not independently attested. No zero table, real/simple
zero assumption, RH, desired minor sign or cross-notebook result is used.

This is a known-method specialization from steps435/437. Step435's
inconclusive recursive-power certificate is preserved below. Step437
repairs only its Fourier phase enclosure at the same fixed settings.
The separate conceptual audit in step439, below, reviews the analytic
implementation and replays every field. It retains the documented
arithmetic contracts; it is not formal verification or independent
attestation of the executable.

## Conclusion

The independent-phase repair of step437, under these arithmetic and
inherited analytic qualifications, gives for the ACTUAL operator

    0.00915280651930 < det(I-A) < 0.00915280748410,
    1.29740587671843 < ||A|| < 1.29740587679064.

Thus the signed determinant is strictly positive although the sufficient
norm<1 criterion fails at this pair. This is one fixed-pair signed
separation, accepted by the step439 analytic audit under the stated
contracts. Low-order positivity
already overlaps the inspected literature; this is not a new sign
theorem, a growing-order estimate or an RH candidate. The repair proof,
complete error bounds and verification limitations are given below.

### Preserved step435 conclusion

The saved full-contour enclosures give nonvanishing and exactly two zeros
with multiplicity in each of |w|<2048 and |w|<2304, with respective
boundary lower bounds greater than 8.419e-7 and 2.090e-7. Two disjoint
strict real brackets show that the zeros are real and simple. Outward
decimal versions of those brackets are

    -799.161819329547437854196 < w_1 < -799.161819329547437853328,
    -1767.704602296329961297339 < w_2 < -1767.704602296329961269583.

Thus the actual pair is admissible for L776/L777, with sigma=9/8.
For the finite approximating operator Ahat constructed below, rigorous
finite arithmetic encloses

    0.00915280700169 < det(I-Ahat) < 0.00915280700171,
    1.29740587675453 < ||Ahat|| < 1.29740587675454.

These are properties of Ahat, not the actual A. The full trace-norm error
bound E lies between 35377031.1124 and 35377031.1125. Consequently the
actual norm enclosure is only

    0 <= ||A|| < 35377032.410.

The general determinant perturbation bound crosses zero: its radius
exceeds 10^15364058. Neither det(I-A)>0 nor ||A||>=1 is certified.
Step435 established no signed advantage, new minor sign, uniform
estimate or RH conclusion. That specific 512-mode recursive rectangular
power implementation stays stopped without a resolution/precision sweep.

## Proof

### Imported methods and normalization

Reuse the assessed argument principle, Cauchy estimates, interval Taylor
integration and Fourier orthogonality of L778. The primary computational
reference is F. Johansson, *Numerical integration in arbitrary-precision
ball arithmetic*, [1802.07942v1](https://arxiv.org/pdf/1802.07942v1),
Sections2/2.1 pp.2–4 and4 pp.7–8. We use elementary Taylor integration,
not a reproof of its Gaussian algorithm. L776/L777 supply the already
audited normalization and complex/confluent finite-rank identity. Their
conditional inputs must still be supplied at this changed pair.

For the signed determinant import M. Duits, *Determinantal point
processes*, [DPP2 author PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf),
AppendixA, Lemma66 p.51 and Lemma69 p.52, with their finite-dimensional
proofs: det(I+XZ)=det(I+ZX), including dependent columns. Only this
finite-dimensional algebra is used; no finite-measure point-process
premise is extended to counting measure. The source's inner product is
linear in its first entry; L777 uses the opposite convention, so the
operator factors below are written with adjoints explicitly.

For arbitrary trace-class T,S on the same Hilbert space, F. Bornemann,
*On the numerical evaluation of Fredholm determinants*,
[0804.2543v2](https://arxiv.org/pdf/0804.2543v2), Section4 (4.1),
pp.12–13, gives

    |det(I+T)-det(I+S)| <= ||T-S||_1 exp(1+max(||T||_1,||S||_1)).

The Schatten product inequality ||XY||_1<=||X||_HS||Y||_HS is in its
Section2 p.7; finite-rank determinants are treated in Section3 (3.2),
p.10. These results require neither norm<1 nor selfadjointness.
The sharper positive-selfadjoint Lemma4.1 is excluded. Specialization
is necessary for the actual normalization, two-zero data and all numerical
errors; the sources do not supply those data. The pre-existing gate is
`drafts/literature/2026-11-04-signed-rank-two-fredholm-diagnostic.md`.
Low-order nonnegativity already overlaps the inspected literature, as
recorded there; no new sign theorem is claimed.

### Enlarged entire evaluator

The substitution x=exp(2u) in L017/L018 gives exactly

    A(u)=exp(u/2) sum_(m>=1) exp(-pi m^2 exp(2u)),
    J(w)=integral_0^infinity A(u) cosh(sqrt(w)u/2) du,
    G(w)=[1+(w-1)J(w)]/16.

The cosh notation is its entire series, with no branch choice. Compact
double-exponential domination justifies exchanging it with the integral.
Use L778's same 128 cells on [0,2], centers c=(2l+1)/128, halfwidth
h=1/128, Cauchy radius d=1/8, theta indices 1..8 and degree24 Taylor
integration. Increase the number of moments to 128: for 0<=n<128,

    j_n=integral_0^2 exp(u/2) sum_(m=1)^8 exp(-pi m^2 exp(2u))
                     u^(2n)/[4^n(2n)!] du.

Their exact integrals define a degree128 polynomial P_0 with coefficients
(1-j_0)/16, (j_(n-1)-j_n)/16 for 1<=n<=127, and j_127/16.
The saved intervals enclose these coefficients; P_0 is not a polynomial
chosen from arbitrary interval endpoints.

For |z-c|<=d, v=exp(2(c-d))(1-2d^2)>0 bounds Re exp(2z) below.
Since pi>3 and m^2>=1+3(m-1), the whole finite integrand A is bounded by

    M_A(c)=exp((c+d)/2) exp(-3v)/(1-exp(-9v)).

Cauchy's coefficient bound and the geometric remainder give an absolute
error in the nth cell integral at most

    2h M_A(c) (c+d)^(2n)/[4^n(2n)!] (h/d)^25/(1-h/d).

These errors are inside every moment/coefficient interval. Factorial-
normalized exp jets obey f_j=j^(-1) sum_(l=1)^j l q_l f_(j-l), f_0=exp(q_0),
for q=u/2-pi m^2 exp(2u). Multiplication by u^2/[4(2n+2)(2n+1)] updates
the monomial jets. This is the same finite Taylor construction justified
in L778, with all 128*128 errors and 128 sets of 25 A jets saved.

On the enlarged disk |w|<=4096, |cosh(sqrt(w)u/2)|<=exp(32u).
Three additional omitted J contributions satisfy

    E_theta = 2e exp(-243) exp(64)/(1-exp(-57)),
    E_u     = 2 exp(-97)/291.5,
    E_c     = [2e exp(-3)/(1-exp(-9))] [64^256/256!]
                                      /[1-4096/(257*258)].

For the first, m>=9 implies m^2>=81+19(m-9), and u<=2 gives exp(u/2)<=e.
For the second, write u=2+t, t>=0. The full theta sum is <=2 exp(-3exp(2u));
e^4>54 gives exp(2u)>=54(1+2t). Including exp((32+1/2)u) bounds the
integrand by 2exp(-97)exp(-291.5t), whose integral is E_u. For the third,
the omitted cosh series starts at n=128, with first term <=64^256/256!
and successive ratios <=4096/(257*258)<1; the retained A integral is
<=2e exp(-3)/(1-exp(-9)). Thus, in addition to coefficient widths,

    |G(w)-P_0(w)| <= E_G=(4097/16)(E_theta+E_u+E_c)
                              <1.521e-42  (|w|<=4096).

This is a newly bounded compact domain, not L778's radius1600 error.
Pi and sin/cos retain L778's Machin and factorial remainder bounds;
all directed arithmetic uses its documented contracts.

### Complete contours, multiplicity grouping and residues

For each S=2048,2304 use the four arcs
w(t)=S i^q(1+it)/(1-it), 0<=t<=1, q=0..3, each with 256 equal
parameter intervals. At each true midpoint w_0, expand P_0 through
degree16 on a disk of radius1024. Since |w_0|<=2304, this disk lies
in |w|<=3328<4096. Put M_P=sum_n sup|[w^n]P_0|4096^n. If Delta
encloses |w-w_0| over a parameter interval, its remainder is bounded by

    M_P (Delta/1024)^17/(1-Delta/1024).

Every saved ratio is <1. Add E_G and all interval coefficient/jet widths.
All 1024 rectangles on each circle exclude zero; no subdivision was
allowed or needed. Their component lower bounds give the conclusion's
strict full-boundary bounds. Exact decimal midpoints of the endpoint
enclosures form polygon vertices and are hulled into the same rectangles.
The true curve and each polygon edge are joined within their common
convex zero-free rectangle, giving a closed nonvanishing homotopy.
Adjacent vertices agree exactly. Exact rational signed crossings, with
y<=0<y' for upwards crossings and the reverse for downwards crossings,
give winding 2 on each circle; no edge hits zero. The argument principle
therefore gives counts with multiplicity, not sampled root counts.

Real signs at [-800,-799] and [-1768,-1767] are opposite and strict.
The fixed 70-iteration bisection cap yields the saved disjoint brackets.
Each contains a real root by the intermediate value theorem. The inner
count2 forces both roots to be simple and exhausts all interior zeros.
The same outer count shows no other zero out to |w|=2304. Therefore
alpha_j=w_j/2048 and P(z)=(z-alpha_1)(z-alpha_2) give entire
F(z)=G(2048z)/P(z), zero-free on a neighborhood of |z|<=9/8.

The initial count phase stopped on an unnecessary root-width assertion:
the second bracket width is 2.77555756156289135105907917022705078125e-17,
exceeding its 1e-17 goal. A midpoint enclosure containing zero is not
loss of the last strict endpoint signs. The same unchanged bisection
was repeated accepting that wider bracket, with all trials saved; no
precision, resolution, radius or iteration cap increased. The original
failure is retained in the certificate. Grouping follows from the strict
brackets and count2 and needs no such width premise.

Cauchy on radius100 disks about these roots, all inside |w|<4096,
adds E_G/100 to the interval polynomial derivatives. For l!=j,

    F(alpha_j)=2048 G'(w_j)/(alpha_j-alpha_l),
    d_j=alpha_j^2 2048 G'(w_j)/(alpha_j-alpha_l)^2.

These are the complete L777 simple-pole residues, including the uncertain
root, derivative and other root; no zero ball is divided by a zero ball.
The saved intervals have d_1>0 and d_2<0. No sign of A is inferred.

### Laurent extraction and full-product trace error

Take sigma=9/8, a=7/8, rho=15/16. The roots satisfy |alpha_j|<a.
The outer full-contour bound gives

    |F(z)| >= m_sigma=(outer G lower bound)/(sigma+a)^2 >0
                                                    on |z|=sigma.

L777 gives b=p/F=P^2/[z^2 G(2048z)] and M_b=(1+a/sigma)^2/m_sigma.
Its only possible negative Laurent modes are -2 and -1; its positive
coefficients satisfy |beta_n|<=M_b sigma^(-n). With fixed L=2048 roots
of unity and N=512, enclose all sampled b values and Fourier sums.
For 1<=n<=N<L-2, every congruent index n-jL, j>=1, is below -2.
Thus ALL negative modes are excluded from aliases, not just mode -1.
Absolute Laurent convergence on the unit circle justifies finite averaging,
and the complete alias error is

    M_b sigma^(-(n+L))/(1-sigma^(-L)).

Real symmetry gives real beta_n, and every imaginary enclosure contains
zero. Take exact decimal midpoint hats and errors epsilon_n. Retain all
sample, trig, root, evaluator, Fourier and arithmetic uncertainty. In this
implementation the Fourier powers are recursively multiplied as complex
rectangles; that enclosure remains valid even when it becomes very wide.

Apply L777(6)–(8) with these nodes/residues and coefficients. Explicitly,
with t=rho-a, q=sigma^(-2),

    M_S=sum_j |dhat_j|/t,
    E_S=sum_j [e_dj/t+|dhat_j| e_j/t^2],
    h_B=M_S rho/(1-rho^2), delta_B=E_S rho/(1-rho^2),
    h_b^2=sum_(n=1)^N n|betahat_n|^2,
    delta_b^2=sum_(n=1)^N n epsilon_n^2+M_b^2 T_N(q),
    T_N(q)=q^(N+1)[(N+1)-Nq]/(1-q)^2.

Let Hhat=H(bhat), Bhat=Vhat Chat What*, with real diagonal Chat=diag(dhat).
The full-product difference is

    A-Ahat=Q_r[Delta_H Bhat+Hhat Delta_B+Delta_H Delta_B]Q_r.

L777's bounds on each Hilbert–Schmidt factor, together with Bornemann's
Schatten inequality and the ideal contraction by Q_r, give the TRACE
norm bound

    ||A-Ahat||_1 <= E=delta_b h_B+h_b delta_B+delta_b delta_B.

This explicitly strengthens the type of the error estimate for this use;
L777's operator conclusion alone is not inserted into a determinant bound.
The cross term is retained. Since operator norm <= trace norm, the same
E is available for both operator triangle inequalities.

### Signed finite determinant and original norm

Rows i=4..512 of Uhat are exactly L777(9); later rows vanish.
The two Gram matrices are Gu=Uhat*Uhat and
Gy_(j,l)=(alphahat_j alphahat_l)^3/(1-alphahat_j alphahat_l).
Real nodes were proved rather than assumed. Hence Yhat*=Vhat^T Q_r,
and the signed pairing is

    S_(j,l)=sum_(i=4)^512 alphahat_j^(i-1) Uhat_(i,l).

The factorization is Ahat=Uhat Chat Yhat*. Substitute X=-Uhat and
Z=Chat Yhat* in the imported finite-rank determinant identity. It gives

    det(I-Ahat)=det_(2x2)(I-Chat S).

This retains the signs of both residues, the order, adjoints and minus
sign. No singular-value matrix or norm-compression K is substituted for
the pairing. The identity would also hold for dependent/confluent columns;
the actual grouping certified here is simple. Directed arithmetic and
exact integer/rational checks give the finite determinant in the conclusion.

To enclose the original norm without square-root metric errors, the two
nonzero squared singular values of Ahat have sum and product

    t0=tr(Chat* Gu Chat Gy)=sum_(j,l) dhat_j dhat_l Gu_(j,l) Gy_(j,l),
    d0=det(Gu)det(Gy)|det(Chat)|^2.

Indeed L777's norm reduction gives K=Gu^(1/2)Chat Gy^(1/2), whose
K*K has that trace/determinant. This remains valid with singular Grams.
Positive semidefiniteness gives t0>=0,d0>=0,t0^2-4d0>=0. Therefore

    ||Ahat||=sqrt((t0+sqrt(t0^2-4d0))/2),
    ||Ahat||_1=sqrt(t0+2sqrt(d0)).

Both finite Grams are retained. The saved finite trace norm is between
1.59258118022078 and 1.59258118022079. The actual trace norm is at
most ||Ahat||_1+E, and both actual norm endpoints follow from
max(0,||Ahat||-E)<=||A||<=||Ahat||+E. Finally apply Bornemann with
T=-A,S=-Ahat and the separately bounded trace norms:

    |det(I-A)-det(I-Ahat)| <= E exp(1+||Ahat||_1+E).

L776 makes the exact determinant real; the approximation and this absolute
error thus enclose its real value. The saved enormous radius exceeds
10^15364058, so the interval crosses zero. No positivity conclusion follows.

### Error diagnosis, evidence and limits

The saved bounds have delta_b>1.2857598708e8, h_B<0.275145,
h_b<10313.212, delta_B<3.469e-15. The high-mode Fourier rectangles
dominate the error: epsilon_192<3.202e-15 but epsilon_512>4.017643e6.
The weighted error norm from modes1..192 is <4.376e-13; that from all
512 modes is >1.2857598708e8. In contrast, M_b sqrt(T_512)<1.722e-17.
These are comparisons of the complete saved evidence, not a new evaluation
or truncation run. Recursive rectangular multiplication mixes component
widths with the noncontractive absolute-component matrix
[[|Re z|,|Im z|],[|Im z|,|Re z|]]; its maximal factor is |Re z|+|Im z|,
which can exceed1 even for |z|=1. The resulting wrapping explains why
the rigorous high-mode error budget loses usefulness. It is a failure
of this certificate, not proof of failure of the signed method or minor.

Implementation: `scripts/actual-fredholm/signed_pair_435.py`.
Full certificate: `scripts/actual-fredholm/signed-pair-certificate-435.json`.
Phases coeff, count, roots, signed are recorded in that order, with roots
the same-resolution recovery above. Reproduction at a fresh path preserves
the historical files. The corrected count phase already accepts wider
strict brackets; a fresh run need not reproduce the historical assertion.
No radius sweep or automatic refinement was performed.

Run `python3 scripts/actual-fredholm/check_signed_435.py` for the complete
saved-data checks in `scripts/actual-fredholm/signed-saved-data-check-435.json`.
They passed: all 2048 contour segments/endpoint inclusions/coverages,
both exact windings, every sampled denominator and coefficient/error/alias
record, and exact integer/rational verification of all509 U rows, both
Grams, signed pairing/determinant and finite singular-value enclosures.
The full HS/trace-product budgets and triangle transfers are checked.
This does not independently replay the exp jets, analytic tail estimates,
contour enclosure theorem, Fourier factors or Bornemann's exponential
evaluation. Those remain subject to the mathematical reasoning above,
the software contract and a future independent critical review.

`scripts/actual-fredholm/signed-error-diagnostic-435.json` preserves the
error comparison. The original width assertion and an initial checker
typo (parameter coverage endpoint2 instead of1, introduced while adapting
the winding count) were corrected without changing the numerical evidence.
The final checker PASS concerns the corrected finite checker; no earlier
failed check is treated as proof. No finite hatted norm/sign transfers
through an unpaid small error. Growing-order signed interactions,
reciprocal budgets, other indices and all-degree positivity remain open.

### Independent-phase repair, step437

Only the phase mechanism changes. Reuse the exact evaluator, both
count2 contours, strict simple grouping, roots/residues and all2048
sampled b enclosures above. The new certificate retains those complete
fields unchanged and records the old input's SHA256 and primitive-source
SHA256. Every phase, G sample and b sample was recomputed at the SAME
precision75, degrees129/128 and L=2048 and matched the old interval
endpoints exactly. This is provenance/containment replay, not an
independent audit of the enlarged evaluator or contour argument.

For the known phase identities import NIST *Digital Library of
Mathematical Functions*, v1.2.8 (2026-09-15),
[4.14.3,4.14.8–9](https://dlmf.nist.gov/4.14),
[4.21.2–3,4.21.34](https://dlmf.nist.gov/4.21),
[4.19.1–2](https://dlmf.nist.gov/4.19),
[4.20.1–2](https://dlmf.nist.gov/4.20) and
[1.4.35–37](https://dlmf.nist.gov/1.4#vi).
The pre-existing assessment is
`drafts/literature/2026-11-04-independent-phase-rank-two-repair.md`.
Only integer periodicity/De Moivre, real derivatives and real Taylor
remainders are used. No fractional-power identity or complex-angle
remainder is substituted. These standard identities are imported, not
reproved; their implementation specialization is necessary to replace
the failed rectangular powers without changing the operator.

Write z_j=exp(2pi i j/L). For each 0<=j<L, divide j into a quadrant
and a remainder 0<=m<L/4. The true reduced angle 2pi m/L belongs to
[0,pi/2), and its interval lies in [0,2). Use the same enclosed pi and
L778's audited real sine/cosine Taylor primitive, with common error
2^130/130!, followed by exact quadrant rotations. It encloses z_j in
a rectangle Z_j. All2048 rectangles are saved; their largest component
width is <=3.735e-72. Since the true component lies in the interval,
this also bounds any component's error from an endpoint or midpoint
chosen within it; no midpoint accuracy is assumed without containment.

For EVERY 1<=n<=512 and 0<=j<2048, the imported integer identities give

    z_j^(-n)=z_k,  k=(-jn) mod2048.

Compute that index with exact integers. If B_j is the full reused
rectangle for b(z_j), interval multiplication and directed summation
therefore enclose the complete complex average

    s_n=(1/L) sum_(j=0)^(L-1) b(z_j) z_j^(-n)

in (1/L) sum_j B_j Z_((-jn) mod L). No recursively multiplied
phase rectangles occur. Repeated occurrences may share pi or roots:
setwise interval inclusion requires no statistical independence.
The already justified absolute Laurent convergence and finite Fourier
orthogonality identify s_n=beta_n+sum_(h>=1) beta_(n+hL).
Both possible negative modes -2,-1 are excluded because n<L-2.
The unchanged complete alias bound above therefore applies to each
n. Add it before taking real midpoint hats and upward errors. Retain
every imaginary enclosure; all512 imaginary intervals widened by their
alias errors contain zero, as required by real symmetry.

The same Hilbert–Schmidt and full-product trace calculation above now
gives

    delta_b <1.164e-12, delta_B <3.469e-15,
    h_b <10313.212, h_B <0.275145,
    ||A-Ahat||_1 <= E <3.609621e-11.

The finite sums include ALL512 epsilon_n and the same infinite tail
M_b^2 T_512; the cross term delta_b delta_B remains present. These
rounded factor bounds are descriptive; the final E uses the saved
unrounded directed intervals, not substitution of the displayed rounded
numbers. The exact same signed pairing, both Grams and singular-support
formulas above are applied to the NEW hats. They give

    0.00915280700169 < det(I-Ahat) <0.00915280700171,
    1.29740587675453 < ||Ahat|| <1.29740587675454,
    1.59258118022078 < ||Ahat||_1 <1.59258118022079.

Bornemann(4.1), with the separately enclosed actual trace norm
<=||Ahat||_1+E, gives determinant error <4.823978e-10. In particular
the saved complete actual determinant lower endpoint is
0.00915280651930207196282725395775497936476759789197369684364455588247808962161,
which is positive. The saved complete original-norm lower endpoint is
1.29740587671843660390743107863532844169433989418464005766731906009482722528,
which exceeds1. Reverse and ordinary triangle inequalities and the
determinant perturbation bound give the conclusion's outward rounded
two-sided intervals. No hatted sign/norm is promoted across an unpaid
error. L776's positive prefactor can transfer this fixed determinant
sign; no new finite-order positivity beyond the assessed sources is
claimed here.

Implementation: `scripts/actual-fredholm/independent_phase_437.py`,
importing the unchanged primitives and finite reduction from
`scripts/actual-fredholm/signed_pair_435.py`.
Full evidence: `scripts/actual-fredholm/independent-phase-certificate-437.json`.
Reproduction uses the same old input and a fresh output path (change
the new script's CERT only); it refuses to overwrite an existing run.
No radius, precision, degree or resolution changed; no automatic
refinement, sweep or second mathematical attempt was made.

Run `python3 scripts/actual-fredholm/check_independent_phase_437.py`.
The full report in
`scripts/actual-fredholm/independent-phase-check-437.json` is PASS,
with no new failures. It checks complete inherited-field equality and
input hash; all contour coverages, zero-free boxes, exact windings and
strict group/error records; all2048 phase provenance/widths and sampled
denominators; all1048576 phase products using exact integer interval
endpoints and a separately indexed exact modular accumulator; all512
complete complex DFT enclosures, imaginary/alias transfers, epsilons
and HS budgets; and all509 U rows, both Grams, signed pairing,
determinant, singular-value and triangle bounds using exact integers
and rationals. The checker verifies every entry, not selected previews.
Decimal reports no exceptional flags beyond expected Inexact/Rounded.
The inherited step435 width-assertion failure stays separately recorded;
there is no new numerical/check failure.

This finite checker does NOT independently replay or audit the analytic
theta/Cauchy tails, enlarged contour theorem, trig remainder/provenance
proof or Bornemann exponential evaluation. Those rely on the stated
analytic reasoning and documented trusted arithmetic contracts; the
installed binary is not independently attested. At completion of step437
an independent analytic audit was still required; step439 below pays
that obligation under these contracts. Signed advantage is local progress
within known methods, not progress beyond the checked positivity
literature. Growing-order signed interactions, actual reciprocal bounds,
other indices, exceptional signs and all-degree positivity remain open.

### Independent conceptual audit, 2026-11-04 (step439)

The supplied starting Next action exactly matches TARGET in the prior
SPECIALIZE assessment
`drafts/literature/2026-11-04-repaired-rank-two-certificate-audit.md`.
That coverage is reused. This audit finds no mathematical defect in the
repaired fixed-pair result. It validates a local known-method benchmark,
not a new low-order sign theorem.

**Evaluator and arithmetic.** Substitution in L017 gives I=4J and
s(s-1)=(w-1)/4; L018 therefore gives exactly G=[1+(w-1)J]/16.
On each closed cell disk, Re exp(2z)>=exp(2(c-d))cos(2d)
>=exp(2(c-d))(1-2d^2)>0. Thus M_A bounds the whole finite-theta
integrand. Multiplication by (c+d)^(2n)/(4^n(2n)!) bounds the full
moment integrand. Summing Cauchy's coefficient bounds from degree25
and integrating over length2h gives the implemented remainder. The
exponential-jet recurrence and monomial update use factorial-normalized
coefficients; even monomials integrate to 2h*h^j/(j+1). Every moment,
cell jet, quadrature error and resulting coefficient interval replayed.

The enlarged tails are valid independently of the radius1600 bounds.
For theta indices use m^2>=81+19(m-9), giving ratio exp(-57).
For u=2+t the full tail integrand is bounded by
2exp(65+32.5t-162(1+2t))=2exp(-97-291.5t).
For the retained finite-theta integral the cosh tail starts at n=128;
its first term is at most64^256/256! and subsequent ratios at most
4096/(257*258)<1. These bound distinct omitted parts of J, while
cell errors already enclose exact polynomial coefficients. The factor
|w-1|/16<=4097/16 proves the stated analytic remainder on disk4096,
so its derivative may be bounded by the complex Cauchy formula.

The primitives use exact integer/decimal inputs and directed operations;
powers use interval multiplication, not general Decimal power. Reciprocal
endpoints are reversed correctly also on negative intervals. Squaring
handles intervals meeting0; adjacent-neighbor exp/sqrt enclosures use
the assessed contracts. Machin's alternating remainder starts at
t^361/361. Midpoint hats and vertices are arbitrary exact chosen decimals
with upward distance errors; ideal midpoint accuracy is unnecessary.
No exceptional context flags beyond Inexact/Rounded occurred. The stated
allcr/backend contracts, rather than independent binary attestation, remain
explicit premises.

**Contours and residues.** The true parameter midpoint has modulus S
although its enclosure is rectangular. Its radius1024 Cauchy disk lies
inside3328<4096. Horner jets contain the Taylor coefficients at that
true point; interval subtraction contains the whole arc displacement.
Exact-rational checks of all boxes give Delta^2<137<1024^2, validating
every geometric remainder. All2048 zero-free segment rectangles and
shared exact vertices were reproduced. Straight interpolation between
the true image curve and polygon lies in their common convex rectangles,
so gives a closed nonvanishing homotopy. The half-open signed-crossing
convention handles real-axis vertices. Both complete windings equal2;
no sampled-root count is substituted.

All real bracket trials, final strict endpoint signs and residues replayed.
Two disjoint opposite-sign brackets give two distinct real roots; total
inner multiplicity2 forces simplicity and exhaustiveness. The equal outer
count and boundary nonvanishing leave no other zeros through2304, making
F entire and zero-free on a neighborhood of the closed disk9/8. Both
whole root intervals plus radius100 lie in disk4096, so E_G/100 bounds
G'-P0'. The residue formula alpha_j^2 R G'(w_j)/(alpha_j-alpha_l)^2
retains the radius factor and all root/derivative/other-root uncertainty.
The old failed arbitrary width goal is unnecessary and stays recorded.

**Fourier and trace transfer.** The whole outer circle, with
|P|<=(sigma+a)^2, supplies the factor lower bound. Since 1/F is
holomorphic through that disk, b=z^-2 P/F has no negative modes below-2
and its Laurent series converges absolutely on the unit circle.
For1<=n<=512 all congruent lower indices are <=n-2048<-2, excluding
both negative modes. The remaining aliases have exactly the displayed
geometric bound. Each reduced angle is enclosed in [0,2). The degree128
cosine polynomial can be viewed as degree129 with zero odd coefficient;
both degree129 Taylor remainders are bounded by2^130/130!. Exact integer
periodicity therefore justifies every modular phase index. Common pi/root
uncertainty does not impair setwise containment. All2048 samples/phases
replayed, and the exact checker covers all1048576 phase products and
all512 complex DFT/alias/error records, with no recursive interval powers.

All512 weighted errors and the full infinite T_512 term enter delta_b.
The rational-Hankel Cauchy estimates give both HS bounds with factor
rho/(1-rho^2). All three HS products, including the cross term, are
retained, and the Schatten inequality makes E a TRACE-norm error.
The signed matrix is C Y*U; both Gram metrics determine the singular
values of U C Y*. Every U row, both Grams, signed pairing/determinant
and norm/trace-norm enclosure passes the exact checker. The support
argument remains valid for singular Grams; no unsigned coefficient
matrix is substituted for the pairing or original norm.

Bornemann(4.1) applies to T=-A,S=-Ahat with their separately bounded
trace norms on the same Hilbert space. It gives radius at most
E exp(1+||Ahat||_1+E), without norm<1 or selfadjointness. A new exact
rational check independently bounds this exponential: for
x=1+upper(||Ahat||_1)+upper(E), sum through degree256 and add
(x^257/257!)/(1-x/258), valid since0<=x<258. The saved determinant
radius dominates upper(E) times that rational majorant. Both actual
thresholds and the stated outward endpoints survive. The sharper
positive-selfadjoint lemma is not used.

**Full evidence.** Reproduction: `python3 scripts/actual-fredholm/audit_439.py`
with a fresh audit output directory; it refuses to overwrite its report.
Complete fresh evidence is
`scripts/actual-fredholm/audit-439/independent-phase-certificate-437.json`;
the report is `scripts/actual-fredholm/audit-439/audit-report.json`.
The unchanged exact checker ran on that fresh evidence, producing
`scripts/actual-fredholm/audit-439/independent-phase-check-437.json`.
Every evaluation, contour, root/residue and signed field matched exactly.
The report records hashes, actual/required thresholds, complete checks,
the rational exponential majorant (hexadecimal integer numerator and
denominator), and an empty failure list. Original certificates and the
primitive-source hash were preserved. This is independent conceptual
scrutiny and reviewed-code replay, not an independent implementation or
formal verification of the backend. Uniform-order positivity remains open.

## Mathlib

Full matching coverage has not been checked. No presence or absence claim
is made for this actual certificate or its complete complex finite-rank
specialization. The named primary identities and the standard Cauchy,
argument-principle, intermediate-value and elementary2x2 spectral formulas
are the informal inputs. This is not formal verification.
