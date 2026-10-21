# L050 — fixed conductor-36 arithmetic and a failed enclosure schedule

## Hypotheses

Use the exact integral model E: y^2=x^3+1, the differential dx/(2y),
and the oriented path {1/6,infinity}. Use the named modularity,
coefficient, transport, Fourier-tail and real-period results specified
below, with the conventions of L049. The claim concerns only the
fixed finite certificate `scripts/nonunitary-cusp/certificate.json`
and its separate replay. No optimality, Manin constant, eta product,
rank, denominator, integral generating list or non-CM hypothesis is used.

## Conclusion

The equation is global minimal, Delta=-432, and its conductor is 36.
The small-prime Tate exits are IV at 2 and III at 3, both with conductor
exponent 2. Its associated normalized newform has a_2=a_3=0 and trivial
local Euler factors at these primes. The cusp 1/6 is nonunitary.

The preserved 96-bit rectangle schedule supplies a rational outward
interval J containing Re(A_f({1/6,infinity}))/Omega(E), with the actual
endpoints and exact width in the certificate's `result`. Separate finite
replay passes. **The approved width test fails:** width(J)>2^2000,
where the required width is <2^-20. Thus this is an informative failed
implementation schedule, not production of the requested narrow interval.
No useful sign, nonvanishing or rational recovery is claimed from J.
No new numerical-modular-symbol method or BSD result is claimed.

## Proof

**Coverage and citations.** The prior SPECIALIZE assessment is
[the fixed production assessment](../drafts/literature/2026-10-11-nonunitary-cusp-enclosure-production.md).
For arithmetic we import Cremona, *Algorithms for Modular Elliptic
Curves*, corrected second edition (1997),
[Section 3.1 (3.1.3), pp.62--63, and Section 3.2 Tate lines 1--28,
pp.66--67](https://johncremona.github.io/book/fulltext/chapter3.pdf).
For modularity we use Breuil--Conrad--Diamond--Taylor, *On the modularity
of elliptic curves over Q*, JAMS 14 (2001), 843--939,
[Theorem A and Introduction (1)--(2)](https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf).
For normalized coefficients use Cremona
[Section 2.6 (2.6.1)--(2.6.2), p.25](https://johncremona.github.io/book/fulltext/chapter2.pdf).
For the unitary definition use Wuthrich, *Numerical modular symbols for
elliptic curves*, arXiv:1608.06423v2, 23 March 2017,
[p.3](https://arxiv.org/pdf/1608.06423v2).
The analytic identity/tail, positive AGM, and period source statements
are the precise imports in audited L049. We apply them rather than
reprove them; the independent finite replay verifies their numerical
specialization. Full matching Mathlib coverage has not been checked.

**Minimality and both early Tate branches.** The invariant formulas give
(b2,b4,b6,b8,c4,c6,Delta)=(0,0,4,0,0,-864,-432).
Since Delta=-2^4*3^3, any local discriminant valuation is below 12.
An isomorphism to a smaller integral local model would lower its
valuation by a positive multiple of 12, by the discriminant scaling
formula, while the new integral discriminant has nonnegative valuation.
This is impossible at every prime. Thus the model and differential are
minimal globally; primes other than 2 and 3 have good reduction.

At 2, Tate's first coordinate branch has r=0,t=1,s=0, that is x=X,
y=Y+1. Substitution gives coefficients [0,0,2,0,0], with invariants
(0,0,4,0,0,-864,-432). The coefficients a3,a4,a6 are divisible by 2;
c4 is divisible by 2, so there is no multiplicative exit. The tests
2^2 not dividing a6 and 2^3 not dividing b8 are false, since both are
zero. The test 2^3 not dividing b6 is true. Line 27 therefore gives
IV, f_2=v_2(Delta)-2=2. The residual quadratic at line 26 is
T^2+T, whose two F_2 roots are 0,1, so c_2=3.

At 3, Tate's branch permits r=-1,t=0,s=0; -b6=-4 has balanced
residue -1. Substitution x=X-1 gives [0,-3,0,3,0]. Its b-values
are (-12,6,0,-9), and c4=0,c6=-864,Delta=-432. Again a3,a4,a6
are divisible by 3 and there is no multiplicative exit. The II test
fails since a6=0; 3^3 does not divide b8=-9. Line 24 gives III,
f_3=v_3(Delta)-1=2 and c_3=2. No later Tate branch is reached.
Consequently N=2^2*3^2=36. As an independent published comparison,
[Cremona's exact primary row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999)
is `36 a 1 [0,0,0,0,1] 0 6`; the
[Table One documentation](https://johncremona.github.io/ecdata/)
identifies the conductor and minimal coefficients. No rank or torsion
column is needed or used as a proof input.

BCDT associates the normalized newform at this conductor. At both bad
primes p^2 divides N, so the imported newform recurrence gives a_p=0
and all positive p-power coefficients zero. At every other prime up to
4860 the producer counts the target using quadratic characters. The
separate verifier instead enumerates y-squares into a residue histogram
and checks every x's number of y-solutions. It checks all 648 good primes
and 1,454,362 x-counts, then independently trial-factors every integer
2 through 4860 and verifies every prime-power recurrence and product.
The complete coefficient list and factorizations are retained, not a
sample or comparison with rounded software output. At m=6,N=36,
M=gcd(m,N)=6 and Q=N/M=6, so gcd(M,Q)=6 and the cusp is nonunitary.

**All transports and orientation.** Choose ell=37, prime, 1 modulo 36,
and coprime to 6. Count E(F_37) for h=38-a_37>0. All 38 reduced
endpoints are 37/6 and (1/6+j)/37 for j=0,...,36. The certificate
retains each reduced fraction, Bezout pair, middle translation and
matrix gamma=(A B;C D). Independent matrix multiplication verifies
both Bezout identities, determinant one, C divisible by 36 and
(A+6B)/(C+6D) equal to the prescribed endpoint. These are all terms
of L049's good-prime closing identity.

The imported transportation formula holds at any upper-half-plane tau.
For C nonzero choose tau=-D/C+i/|C|. Exact Mobius division gives
gamma tau=A/C+i/|C|: indeed gamma z=A/C-1/(C(Cz+D)), and Cz+D is
+i or -i according to the sign of C. For C=0 choose tau=i; determinant
one forces A=D=+1 or -1 and gamma i=B/D+i. The verifier independently
computes the real and imaginary parts of every image from the original
matrix, retaining positivity. This evaluation-point choice specializes
the already imported arbitrary-tau identity; it does not require a
unitary-cusp expansion or new theorem. Reduce each real coordinate
modulo one before exponential evaluation. The resulting 69 distinct
interior points are retained with all transport-to-point indices.

Write P(z)=sum a_n exp(2*pi*i*n*z)/n, as in L049. Transportation and
the full Hecke identity give, with the prescribed r-to-infinity orientation,

    A_f({r,infinity}) = sum_v (P(gamma_v tau_v)-P(tau_v))/h.

The sign is the audited L049 sign. Distinct choices tau_v are allowed
because each individual transportation difference is constant. No
central vanishing or proposed normalized value enters this closing sum.

**Finite exponential rectangles, full tails and failed propagation.**
All arithmetic intervals use outward dyadic endpoints with scale 2^96.
Machin's identity uses 40 alternating terms for each arctangent and
the next-term remainder. The full exact rational brackets are retained
and separately reconstructed, giving a pi interval inside (3,4).
At each point x+iy use w=2*pi*(-y+i*x) with x reduced to [-1/2,1/2).
The verified bound 8(|x|+y)<=12 gives |w|<=12. Compute the complex
Taylor polynomial through degree 160, propagating both real and imaginary
rectangle endpoints at every operation. Enlarge both coordinates by

    3^12 * 12^161 / 161!.

Taylor's theorem bounds the complex remainder by this value since
e^12<3^12. The certificate retains the integer outward radius and q
rectangle; the verifier reconstructs all 160 propagated terms and errors
with separate Fraction endpoint arithmetic. It neither trusts q as a
floating approximation nor assumes its rectangular powers stay sharp.

For each point the first H with

    R_H(y) = 2^(-floor(6Hy))/(6y) <= 2^-38

is chosen; these truncations are at most 4860. L049's imported full
Fourier tail is bounded by R_H(y), using pi>3 and e>2. The verifier
checks both this inequality and failure at H-1, every coefficient,
every complex power multiplication and scaled term, and both tail
radii. It replays all 181,410 finite Fourier terms. The complete signed
closing interval is then divided by h. The certificate stores the
finite sums and resulting enclosures; deterministic replay reconstructs
all intermediate operations, rather than inspecting a bounded preview.

This method remains outward even when rectangles become very wide:
interval multiplication/subtraction encloses the exact product in each
coordinate, and induction encloses every q^n and partial sum. It does
not preserve the correlation of the real/imaginary errors under repeated
complex multiplication. At the worst finite-sum point (certificate
primitive 40), H=4860 and both q coordinates are positive; its rectangular
l1 upper bound is

    13828836435609312992082850725 / 9903520314283042199192993792 > 1.

Its finite-coordinate width is enormous before adding the tiny tail.
This supplies a concrete diagnosis of poor rectangle propagation, not
failure of the analytic transport/tail theorem. Fixed pi precision,
coefficients, full Hecke coverage and positive period division are
independently checked; increasing H in this same fixed-precision
power recurrence is not a justified response. A new finite schedule
should change the elementary evaluation representation and test it.

**Independent total minimal period and final failure.** The completed
square here is already Y^2=x^3+1, differential dx/(2Y).
Factor (x+1)(x^2-x+1), so the real root is -1 and the conjugate roots
are 1/2 +/- i sqrt(3)/2. Thus d=-3/2, v^2=3/4 and R=sqrt(3).
The negative-discriminant, connected-real-locus formula imported in
L049 gives

    Omega(E)=pi/AGM(sqrt(R), sqrt((R+d)/2)).

The verifier checks the exact factorization/Vieta identities, R>|d|,
both positive branches, all outward square-root inequalities and all
12 AGM iterations. The final lower geometric and upper arithmetic
endpoints enclose the positive exact AGM by its standard theorem.
The total-component factor is one. The resulting exact period interval is

    [166638467572977606763020498997/39614081257132168796771975168,
     166638467572977606763020499043/39614081257132168796771975168].

The final normalized interval takes the min/max of all four quotient
endpoints, covering either sign of the integral. Its exact width is
recorded in `result/width` and independently in `verification.json`.
Exact rational comparison gives width>2^2000, hence it fails the required
strict width<1/1048576. Replay PASS means correct finite evidence and
outward inclusion; `target_passed: false` means the requested production
threshold was not achieved. This does not contradict L049's terminating
refinement theorem, whose finite errors are refined as needed.

Reproduction from the active notebook directory:

    python3 scripts/nonunitary-cusp/build_certificate.py
    python3 scripts/nonunitary-cusp/verify_certificate.py
    python3 scripts/nonunitary-cusp/diagnose.py

The producer deliberately exits 1 on this preserved failed schedule;
the verifier exits 0 on full successful arithmetic replay while reporting
the false target flag. Full evidence is in those scripts' certificate,
verification and diagnosis JSON files. The separate verifier imports no
producer code and uses different point-count, factorization, matrix and
interval arithmetic implementations. This is finite replay, not a
separate critical proof audit or formal software correctness theorem.
No threshold-success, exact value, full normalized table, coefficient,
rational point, Sha statement or complex-order comparison follows.

## Mathlib

Full matching fixed arithmetic plus certified nonunitary-cusp enclosure:
not checked. Supporting Tate branches at 2,3, modularity/coefficients,
Hecke transport, finite complex interval arithmetic, Fourier tails and
positive target-period AGM formalization: not checked. No absence claim
is made. Named source statements and complete finite replay provide the
informal evidence under the stated qualifications.
