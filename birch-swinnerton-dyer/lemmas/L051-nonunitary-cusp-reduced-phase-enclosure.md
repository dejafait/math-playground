# L051 — fixed nonunitary-cusp real enclosure with reduced phases

## Hypotheses

Use E: y^2=x^3+1 with its minimal differential dx/(2y), the associated
normalized conductor-36 newform f, and the oriented path {1/6,infinity}.
Use L050's independently certified arithmetic and L049's cited Hecke
transportation, Fourier-tail and minimal-target total-period identities.
The statement concerns the finite certificate
`scripts/nonunitary-cusp/reduced_phase_certificate.json` and its complete
separate replay, with the original failed certificate retained unchanged.
No optimality, Manin constant, eta product, integral generating table,
rational denominator, rank or non-CM hypothesis is used.

## Conclusion

Put A_f({a,b})=2*pi*i integral_a^b f(z) dz and let Omega(E) be the
total real minimal period. The following outward rational interval contains
Re(A_f({1/6,infinity}))/Omega(E):

    [-6602346876266374004306815782 / 2^96,
     -6602346876111015594619213162 / 2^96].

Its actual width is

    38839602421900655 / 19807040628566084398385987584 < 2^-38 < 2^-20.

Complete independent finite replay passes. This meets the approved
single-path production threshold and repairs the diagnosed complex-power
rectangle failure; it does not supply exact rational recovery, a full
normalized functional, a p-adic coefficient or a BSD comparison.
This is reproduction of known enclosure algorithms, not progress beyond
the checked sources. The separate fixed proof/software audit below passes;
neither the audit nor finite replay is a generic software correctness theorem.

## Proof

**Imports and reason for specialization.** Reuse the unchanged prior
[SPECIALIZE assessment](../drafts/literature/2026-10-11-nonunitary-cusp-enclosure-production.md).
L050 proves global minimality, Delta=-432, conductor 36 and additive
factors a_2=a_3=0 using Cremona, *Algorithms for Modular Elliptic Curves*,
corrected second edition (1997),
[Sections 3.1--3.2, pp.62--67, Tate lines 1--28](https://johncremona.github.io/book/fulltext/chapter3.pdf).
The normalized newform is supplied by Breuil--Conrad--Diamond--Taylor,
*On the modularity of elliptic curves over Q*, JAMS 14 (2001), 843--939,
[Theorem A, Introduction (1)--(2)](https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf).
Coefficient multiplicativity and prime-power recurrence are Cremona
[Section 2.6, (2.6.1)--(2.6.2), p.25](https://johncremona.github.io/book/fulltext/chapter2.pdf).
For the analytic layer use Wuthrich, *Numerical modular symbols for
elliptic curves*, arXiv:1608.06423v2, 23 March 2017,
[equation (2), Lemma 4 and Section 5.1 (11), pp.6--7,11--12](https://arxiv.org/pdf/1608.06423v2),
and Cremona [Proposition 2.2.3 and (2.9.1), pp.16--19,31--32](https://johncremona.github.io/book/fulltext/chapter2.pdf).
The positive minimal-target period is Cremona
[Section 3.7, (3.7.1), pp.97--98](https://johncremona.github.io/book/fulltext/chapter3.pdf),
with positive AGM bounds from [DLMF 19.8.1--19.8.5](https://dlmf.nist.gov/19.8.i).
L049 has separately audited the source orientation and both real-period
cases. We import these identities, rather than reprove them. Taylor's
theorem, Machin's identity and exponential periodicity are standard named
inputs. The difference requiring implementation is a complete outward
finite certificate and independent replay, absent from the cited numerical
return contracts. No new analytic identity is asserted.

**Exact arithmetic, all points and closing orientation.** The producer
copies the original certificate's arithmetic, pi, coefficients, transport
and period evidence; its SHA-256 is bound in the new certificate. The
separate verifier checks this binding and then reconstructs those fields
arithmetically. Thus copying evidence is not a substitute for checking it.
It independently verifies the discriminant scaling/minimality argument,
both transformed early Tate exits, conductor and local factors; all 648
good-prime counts by y-square histograms and 1,454,362 x-checks; all
factorizations and recurrences through T=4860. The coefficient bound
|a_n|<=n is checked on the finite segment as a consistency check; the
infinite tail uses the imported theorem, not this finite test.

The selected prime is ell=37, h=38-a_37=#E(F_37)>0. All 38 endpoints
are 37/6 and (1/6+j)/37, 0<=j<37. Each retained matrix gamma has
determinant one, lower-left entry divisible by 36 and sends 1/6 to its
prescribed reduced endpoint. Replay independently multiplies the Bezout
matrices and verifies every cusp equation and Mobius image. For C!=0
the points are tau=-D/C+i/|C| and gamma tau=A/C+i/|C|; for C=0 use
tau=i and its exact image. Positive heights and all indices are checked.
The 69 distinct points and every truncation H are unchanged from L050.
L049's audited identity, valid for the individually chosen tau, gives

    Re(A_f({1/6,infinity}))
      = sum_v (Re(P(gamma_v tau_v))-Re(P(tau_v)))/h,
    P(z)=sum_(n>=1) a_n exp(2*pi*i*n*z)/n.

All terms are present with this r-to-infinity sign. The nonunitary cusp
has gcd(gcd(6,36),36/gcd(6,36))=6; no unitary shortcut is used.

**Independent finite cosine and real attenuation intervals.** Every
endpoint is an integer divided by D=2^96. An operation takes the minimum
and maximum of all endpoint products/quotients and rounds outwards;
addition and subtraction are exact at this scale. The verifier instead
uses Fraction endpoint arithmetic. Induction on these operations gives
containment for every propagated interval. Correlations may widen an
interval, but do not invalidate it. The shared pi evidence consists of
40 alternating arctangent terms and their next term, in Machin's identity;
replay reconstructs the rational brackets and verifies 3<pi<4.

For a point x+iy, write

    Re(P(x+iy)) = sum_(n>=1) (a_n/n) exp(-2*pi*y)^n cos(2*pi*n*x).

For each n, reduce n*x exactly modulo one to s in [-1/2,1/2).
Periodicity makes this reduction exact even at -1/2. Enclose theta=2*pi*s
by the pi interval, so |theta|<=4. Compute the degree-80 even Taylor
polynomial using t_0=1 and

    t_k = -t_(k-1) theta^2 / ((2k-1)(2k)), 1<=k<=40.

Taylor's theorem on the real segment from 0 to theta, with all cosine
derivatives bounded by one, bounds its degree-80 remainder by
4^81/81!. Both endpoints are enlarged by the ceiling of D times that
rational bound. This contains cos(theta) for the true pi, including
signed s and zero. The certificate retains all 3672 distinct phases,
their theta/square intervals, polynomial, remainder and outward radius;
replay reconstructs every polynomial operation. Reusing a certified
phase for an identical rational s introduces no extra assumption.

For each of the 19 distinct positive heights, 0<y<=1, enclose
w=-2*pi*y in [-8,0). Compute exp(w)'s degree-160 polynomial with
t_0=1, t_k=t_(k-1)w/k. Taylor's remainder bound is at most
3^8*8^161/161!, since |w|<=8 and exp(8)<3^8. Replay verifies the
entire polynomial and the outward enlargement by this bound. Every
resulting q interval satisfies 0<q^-<=q^+<1 and contains exp(-2*pi*y).
No clipping or assumed floating-point positivity is used.

For each primitive, start a real power interval at 1 and multiply it by
this positive q interval for every n=1,...,H. It contains exp(-2*pi*y)^n
by induction. Independently multiply by the freshly reduced phase's
cosine interval, scale by the signed exact a_n/n, and add outwardly.
Replay reconstructs all 181,410 powers and terms, including zero
coefficients, and checks the terminal power and sum at every point.
Every phase and damping entry is used; there are no omitted points or
unverified table entries. No imaginary-part enclosure is needed or claimed
for this real functional. Unlike L050's complex rectangle recurrence,
this schedule does not propagate real/imaginary correlation errors.
Its success is certified by the actual resulting width, not by assuming
that any positive-power schedule must remain narrow.

**Full tails, period and division.** At each point, the imported full
Fourier tail is bounded by

    R_H(y)=2^(-floor(6Hy))/(6y)<=2^-38,

using pi>3 and exp(1)>2 as in L049. Replay verifies this bound and its
failure at H-1, reconstructs the radius ceiling(D R_H), and enlarges
the finite real sum by that radius. This controls the whole tail,
including uncomputed coefficients. The complete signed closing sum is
then enclosed by interval subtraction/addition and division by h.
The resulting integral interval is

    [-27773077929156362300138033631 / 2^96,
     -27773077928502839954210702375 / 2^96].

The independent minimal-target period evidence is unchanged and fully
replayed: x^3+1=(x+1)(x^2-x+1), with real root -1, conjugate real part
1/2, v^2=3/4, d=-3/2, R=sqrt(3)>|d|. Both square roots in

    Omega(E)=pi/AGM(sqrt(R),sqrt((R+d)/2))

are positive. Replay checks all squared endpoint inequalities, all twelve
AGM iterations and the final positive geometric/arithmetic bracket.
Delta<0 gives one real component, so this is the total period without
an extra factor two. The exact outward period interval is

    [166638467572977606763020498997 / 2^95,
     166638467572977606763020499043 / 2^95].

Taking the minimum/maximum of all four integral/period endpoint quotients,
with outward dyadic rounding, gives the conclusion's interval. This
division remains valid for the negative integral. Replay recomputes its
exact width and checks the strict required threshold; rational comparison
also gives width<2^-38. Thus the requested finite threshold succeeds.
Existence of a rational of prescribed denominator has not been checked;
no rational rounding or L048 integer isolation is performed.

**Evidence and limits.** Reproduction from the active notebook:

    python3 scripts/nonunitary-cusp/build_reduced_phase.py
    python3 scripts/nonunitary-cusp/verify_reduced_phase.py

Full evidence is `scripts/nonunitary-cusp/reduced_phase_certificate.json`
and `scripts/nonunitary-cusp/reduced_phase_verification.json`. Producer and
verifier both report PASS and the actual/required rational bounds. The
verifier imports no producer code; it checks all finite operations and
source-input arithmetic, rather than sampling a preview. The producer
reuses the old interval class; independence here refers to the verifier's
Fraction implementation, not two independently invented analytic methods.
The failed schedule and ATTEMPTS/025 remain preserved. The separate critical
audit below validates this fixed assembly. No complete integral
generator list, all-level denominator, exact symbol recovery, p-adic
coefficient, rational point, Sha or complex-order comparison is supplied.

**Separate critical audit, 2026-10-12, BSD-170.** The unchanged
[audit assessment](../drafts/literature/2026-10-11-nonunitary-reduced-phase-critical-audit.md)
approves this fixed SPECIALIZE/REPRODUCTION audit. The source applications,
full finite replay and following discriminating tests pass. No conclusion
beyond this fixed real enclosure is added.

1. **Inherited arithmetic and source hypotheses.** Read both complete
   fixed proofs and the producer/verifier implementations, including the
   inherited interval class. The actual Tate rows are exactly the primes
   2 and 3, in that order. Their integral translations preserve the
   discriminant; valuations 4 and 3 prohibit a smaller integral local
   discriminant. The zero a6 tests and b8/b6 divisibilities reach III/IV
   before any uninspected later Tate branch. At other primes Delta is a
   unit. Thus the modularity input has exact conductor 36, and the
   p^2-divides-N recurrence supplies zero bad-prime coefficients. The
   good-prime count at 37 gives a_37=-10 and h=48. All 648 good-prime
   counts, all 1,454,362 x-residue counts, and all coefficient recurrences
   through 4860 were independently replayed. These checks apply to the
   actual minimal target; CM is allowed. They do not transfer any non-CM
   or optimality premise from another curve.

2. **Finite interval inclusion and real remainders.** For a fixed dyadic
   scale, the minimum and maximum of the four endpoint products contain
   every scalar product. Division is used only with positive denominator
   intervals, where the four endpoint quotients contain all quotients.
   Floor and negative-floor implement downward/upward rounding also on
   negative numbers. Signed scalar multiplication selects both endpoint
   products, so negative Fourier coefficients and negative Taylor terms
   retain inclusion. Addition and subtraction at the common scale are
   exact. Repeated occurrences of an interval variable create dependency
   overestimation, never an inward bound. These facts justify induction
   on both independently implemented operation sequences.

   The true pi is in the Machin bracket by the imported named identity
   and the complete alternating-series brackets. The verifier's tangent
   identity alone is not used to select an arctangent branch. For the
   cosine series and periodicity, reuse DLMF
   [4.19.2](https://dlmf.nist.gov/4.19#E2) and
   [4.14.9](https://dlmf.nist.gov/4.14#E9), as inspected in the assessment.
   Exact reduction s=nx-floor(nx+1/2) gives -1/2<=s<1/2, so true
   theta=2*pi*s has |theta|<4. All real cosine derivatives have absolute
   value at most one on the full segment from zero to theta. Taylor's
   degree-80 Lagrange error is therefore at most 4^81/81!, including
   negative theta, theta=0 and s=-1/2. All 40 even terms have the correct
   alternating coefficients; theta squared as an interval product is a
   containing enclosure, without requiring two independent arguments.

   For attenuation, true w=-2*pi*y lies in [-8,0), and the entire segment
   from w to zero is nonpositive. Every exponential derivative there is
   at most one, so even 8^161/161! suffices for degree 160. The larger
   recorded 3^8*8^161/161! is consequently valid. The stated auxiliary
   e<3 bound follows from e=sum 1/k! and k!>=2^(k-1) for k>=2, with
   strict inequality from k=3. The imported exponential series is DLMF
   [4.2.19](https://dlmf.nist.gov/4.2#E19). Every enlargement radius is
   the ceiling of the exact error times 2^96; there is no truncation or
   clipping of an error interval. Replay verifies strict 0<q^-<=q^+<1
   for all 19 heights. Multiplying these intervals successively contains
   every q^n, and fresh phase reduction gives every real Fourier term.

3. **Complete tails, transports and sign.** Replay visits every one of
   3672 phase entries, 19 damping entries, 69 distinct primitive points,
   181410 finite terms and all 38 Hecke transports. It verifies both
   directions of table coverage (every needed entry exists and every
   saved entry is used), point indices and the full sum n=1,...,H at
   each point, including zero coefficients. SHA binding identifies the
   inherited evidence; its arithmetic and matrix entries are additionally
   reconstructed. The matrices actually satisfy determinant one and
   C=0 modulo 36, with the stated cusp image and positive-height Mobius
   image. Transport indices 0 and 7 have C=0; both are retained, including
   any zero contribution. The arbitrary-tau transport identity is valid
   for each separately chosen point.

   With P based at infinity, A_f({r,infinity})=-P(r) and the full Hecke
   sum gives h A_f({r,infinity})=sum_v A_f({r,v}). Transportation gives
   A_f({r,v})=P(gamma_v tau_v)-P(tau_v). This proves the implemented
   image-minus-original sign, without inferring it from a desired value.
   The global tail bound uses Wuthrich's |a_n|<=n for the associated
   elliptic newform, not the finite coefficient check. For y>0,
   sum_(n>H) exp(-2*pi*n*y)=exp(-2*pi*H*y)/(exp(2*pi*y)-1).
   Since pi>3 and e>2, this is bounded by the exact R_H(y) displayed
   above. Every radius and minimal truncation is rechecked. Thus all
   uncomputed terms, as well as all computed terms, are covered.

4. **Target period and signed quotient.** The factorization and Vieta
   identities fix r=-1,u=1/2,v^2=3/4,d=-3/2,R=sqrt(3). In particular
   R>|d|, a=sqrt(R)>b=sqrt((R+d)/2)>0, and the real curve has one
   component. Cremona's one-real-root identity therefore gives the
   target total minimal period with factor one. Integer squared-endpoint
   inequalities verify all positive roots and all twelve AGM updates.
   The exact geometric iterate is below the true AGM and the exact
   arithmetic iterate above it; interval inclusion yields the final
   bracket [G_12^-,A_12^+]. This reasoning does not require the rounded
   iterates themselves to be monotone or disjoint. The positive period
   bracket and all four final quotients preserve the negative integral's
   ordering. Exact rational width comparison gives the stated strict
   width <2^-38 <2^-20.

5. **Distinct inclusion and altered-evidence tests.** The separate audit
   script evaluates degree-120 cosine and degree-200 exponential
   polynomials by exact rational Horner evaluation, with no intermediate
   dyadic rounding. For each saved argument bracket [l,u], put
   c=(l+u)/2 and delta=(u-l)/2. The mean value theorem bounds variation
   from c by delta: |cos'|<=1 globally and exp'<=1 on the negative
   exponential arguments. Accordingly the exact-polynomial brackets
   use errors delta+4^121/121! and delta+8^201/201!, respectively.
   Rounding these brackets outwards only once, at 160 bits, still puts
   them inside the original 96-bit enclosures. This is a containing
   bracket for the true function value, not a floating-point sample.

   All seven selected cosine cases pass: the actual half-open boundary,
   zero, the largest positive phase, phases nearest +/-1/4 and the two
   nonzero phases nearest zero. All 19 damping heights pass. The full
   replay, rather than this bounded subset, covers all remaining cosines.
   A separate exact-rational closing sum with a single final outward
   rounding is also contained in the saved normalized interval.

   Six altered certificates separately change the original-input hash,
   cosine remainder, damping endpoint, finite-sum endpoint, full-tail
   radius and final signed-division endpoint. Every invocation exits 1,
   rejects the altered field at its corresponding assertion, and replaces
   a deliberately stale passing report with a fresh failure report.
   All altered inputs and full tracebacks are preserved under
   `scripts/nonunitary-cusp/audit_cases/`. SHA-256 before/after checks
   show that both original certificates, both original replay reports
   and the failed-schedule diagnosis retained their bytes. These are
   bounded fixed-artifact tests, not universal corruption detection.

Audit reproduction, with separate outputs:

    python3 scripts/nonunitary-cusp/verify_reduced_phase.py scripts/nonunitary-cusp/reduced_phase_certificate.json scripts/nonunitary-cusp/audit_full_replay.json
    python3 scripts/nonunitary-cusp/audit_reduced_phase.py

Full replay is in `scripts/nonunitary-cusp/audit_full_replay.json`;
all independent endpoint bounds, exact closing evidence, rejection records
and preservation hashes are in
`scripts/nonunitary-cusp/audit_discriminating_checks.json`. No mathematical
inclusion failure or unsupported source hypothesis was found for this
fixed certificate. The audit establishes local correctness of the stated
known-method enclosure, not new analytic mathematics. Rational existence
with a usable denominator, exact value recovery, an entire generator
table and every subsequent BSD input remain outside this conclusion.

## Mathlib

Full matching fixed nonunitary-cusp certified real enclosure: not checked.
Supporting Tate branches, modularity and coefficients, Hecke transport,
Fourier tails, interval Taylor bounds, positive AGM/target periods and
outward division formalization: not checked. No absence claim is made.
The cited named results and complete finite replay provide the stated
informal evidence; no formal software correctness theorem is asserted.
