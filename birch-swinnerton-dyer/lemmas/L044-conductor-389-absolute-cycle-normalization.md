# L044 — Conductor-389 normalization from full absolute cycles

## Hypotheses

Let E/Q be the minimal curve y^2+y=x^3+x^2-2x, with coefficients
[0,1,1,-2,0], conductor N=389 and discriminant Delta=389. Let
f=sum_(n>=1) a_n exp(2 pi i n z) be its normalized weight-two newform,
omega_E its minimal differential, and Omega(E)=integral_(E(R))|omega_E|
its total real period. Use L030's audited independent arithmetic and
entire torsion-free integral relative lattice M=Z^390/R_sat. Its
zero-based quotient basis is e_0,...,e_64; the coordinates of g_i are
the last 65 entries of row i of its unimodular transform C. The last
65 rows of C^(-1) are the integral quotient lifts. All 780 source rows
and 325 saturated relation rows are retained.

Use L029's full-relative integration criterion as certified in L030:
I({alpha,beta})=Re(2 pi i integral_alpha^beta f(z)dz)=beta phi({alpha,beta})
on all M_R, with beta!=0. The complete 65-coordinate rational phi is
L030's audited dual supplement, `scripts/dual-kernel/conductor389-certificate.json`.
Apply L038's integral relative identification to L030's fixed-schema
witnesses, retaining their row convention rather than transposing the
general schema without justification. Use L031 only for its published
exact-model optimality import: E is the new X_0(389)-optimal quotient,
389a1, subject to the published complete-isogeny-class/two-period
computational qualification. Neither its twist ratio nor L032 enters
recovery. L028 supplies the symbol orientation, lambda-plus convention
and integral-generator denominator argument, not a twist calibration
premise. L043 is provenance for the already-audited method and elementary
interval implementation; its conductor-eleven numerical data are not
mathematical inputs here.

The complete new evidence is `scripts/conductor389-absolute-cycles/certificate.json`.
Its separate full replay is adjacent `verification.json`; fresh complete
L030 structural/dual replay is in `upstream-replay/`. Reproduce from the
notebook root:

```bash
python3 scripts/conductor389-absolute-cycles/build_certificate.py
python3 scripts/conductor389-absolute-cycles/verify_certificate.py
python3 scripts/conductor389-absolute-cycles/compare_recovered.py
```

The last command is a post-recovery comparison only. The separate critical
audit of 2026-10-11 passes, as recorded below. These are finite instance witnesses,
not a universal software theorem. No rank, Sha, complex-order,
coefficient, central nonvanishing or twist-value premise is assumed.

## Conclusion

With cusp classes ordered (zero,infinity), the entire integral boundary is

\[
\delta(x)=x_{64}([\infty]-[0]),\qquad
H_1(X_0(389),\mathbf Z)=\ker\delta
=\bigoplus_{j=0}^{63}\mathbf Z e_j,\qquad
\phi(\ker\delta)=\tfrac12\mathbf Z.
\tag{1}
\]

For the oriented cycle gamma={0,-1/5}=-g_5, phi(gamma)=-1, the independent
256-term, 64-bit Fourier enclosure gives

\[
I(\gamma)\in
\frac{[55445334949484787157,127964281715338701155]}{18446744073709551616}
\subset(0,\infty).
\tag{2}
\]

Consequently beta<0 and the exact full-relative normalization is

\[
F=I/\Omega(E)=-\phi.
\tag{3}
\]

All 390 normalized generator values are saved as reduced rationals in
the complete certificate, given by F(g_i)=-phi(g_i); their least common
denominator is 2, with prime factorization 2. For every good ordinary
p>=5, including p=5, L028/L027's all-argument constant is C=0:
v_p(F({infinity,r}))>=0 for every rational r. No calibration-twist
restriction is needed by this normalization route.

This reproduces a known algorithm and the already-known fixed
normalization via independent absolute-period inputs. It tests the
larger integral lattice and the other real-component case. It supplies
neither a new BSD case nor uniform normalization/coefficient production,
rational points, rational Kummer membership or arbitrary-curve rank equality.

## Proof

**Imported homology and exact-model inputs.** Import Stein, *Modular
Forms, a Computational Approach*, GSM 79 (2007),
[equation (3.2.1) and Theorem 3.7, p.40](https://wstein.org/books/modform/stein-modform.pdf#page=54),
and the online weight-two
[Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html).
These identify the complete torsion-free weight-two relative Manin
module with integral relative homology and its boundary kernel with
integral absolute homology. L030's complete saturation and unimodular
transforms meet this integral scope; L038 supplies the retained
construction/identification contract. The independent full replay below
checks the fixed instance, not a rational approximation to its lattice.
The boundary convention is end minus start.

Import Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition (1997),
[Proposition 2.2.3, pp.16--17](https://johncremona.github.io/book/fulltext/chapter2.pdf).
For reduced p_j/q_j, equivalence is characterized by a unit u modulo N
such that q_2=u q_1 modulo N and u p_2=p_1 modulo gcd(q_1,N).
Since N=389 is prime, a cusp p/q with 389 not dividing q is equivalent
to zero=(0,1) by u=q^(-1) modulo 389; the second congruence is modulo
one. Otherwise p is a unit and it is equivalent to infinity=(1,0) by
u=p modulo 389. The two classes are distinct, since equivalence from
zero to infinity would require 0=u modulo 389. Thus these are all cusp
classes, including infinity, rather than only classes appearing in a
saved endpoint sample.

L030 proves global minimality, conductor and newform association
independently. L031's exact optimality import uses Cremona's appendix to
Agashe--Ribet--Stein, *The Manin constant*,
[Theorem 5.2 and its proof](https://wstein.org/papers/ars-manin/html/node13.html),
for curve number one below conductor 60000 except 990h. The primary
[ecdata row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999)
is `389 a 1 [0,1,1,-2,0] 2 1`; its model and number match this instance.
Retain the published complete-isogeny-class and two-period computation
qualification. The rank column and L031's twist-value calculation are
unused. No new optimality proof is claimed.

**Entire boundary kernel.** The fixed generators g_i, 0<=i<389, have
endpoints (-1/i,0), with -1/0=infinity; g_389 has endpoints (0,infinity).
Thus the reduced raw boundary, measured in [infinity]-[zero], is
h=(-1,0,...,0,1). The certificate gives both congruence/unit witnesses
for every one of the 780 endpoints. Its full cusp boundary is (-h,h),
so the complete target was not replaced by an unproved scalar projection.

Let c_i be the integral coordinate row of g_i and q_j the raw integral
lift of e_j. Complete replay checks h annihilates all 780 source and
325 saturated rows. It computes B_j=h(q_j), giving B=(0,...,0,1), and
checks B c_i=h_i for every i. Hence delta(x)=x_64([infinity]-[zero])
on the entire integral quotient.

The normal-form witness T has columns (e_64,e_0,...,e_63); its saved
inverse is T^t. Both products T T^t and T^t T are checked to be the
65-by-65 identity over Z, and BT=(1,0,...,0). For any integral column
x put y=T^(-1)x. Then Bx=y_0, so Bx=0 precisely when y_0=0, with the
other 64 coordinates arbitrary integers. Its entire integral kernel
therefore has basis e_0,...,e_63. Every corresponding raw lift q_j is
saved and its quotient image rechecked. This proves completeness and
primitivity, not merely a rational kernel dimension or a plus sublattice.

Evaluate phi on all 64 basis vectors. Clearing their exact common
denominator two gives an integer list with gcd one. The complete list
is saved and replayed; in particular phi(e_57)=1/2, and the saved Bezout
vector is one in position 57 and zero elsewhere. Each image value is
an integer multiple of 1/2 and this vector attains 1/2, proving (1).
The primitive image functional is 2 phi on the full absolute lattice.
No desired normalized scale was used in this computation.

**Independent cycle and bounded orientation.** Candidate selection uses
only the fixed unnormalized coordinates. For t=1,...,388 with phi(g_t)!=0,
choose the least absolute integer representative c of 389^(-1) modulo t
(t=1 uses c=1), put a=(1-389c)/t, and use (a,-1;389c,t), multiplying
the whole matrix by -1 if c<0. Sort by (|c|,t) and retain at most three.
The complete replay reconstructs the selection from all eligible paths.
The three selected indices are 5,78,7, with matrices respectively
(-78,1;389,-5), (-5,1;389,-78), and (-111,-1;778,7).
For each, the reversed generator is an absolute cycle and the exact
matrix/cusp orientation and both upper-half-plane endpoints are checked.
This finite selection has no asserted uniform cutoff or guarantee.

The first candidate gamma=-g_5 has phi(gamma)=-1 and matrix
M=(-78,1;389,-5), with determinant one and lower-left entry 389.
It sends 0 to -1/5. The exact interior point alpha=(5+i)/389 maps to
M alpha=(-78+i)/389. Import Cremona's same book,
[Propositions 2.10.1--2.10.2, pp.34--35, equation (2.10.5)](https://johncremona.github.io/book/fulltext/chapter2.pdf).
The basepoint-independent oriented period equals the cusp-cycle period;
the primitive of 2 pi i f(z) dz is sum_(n>=1) (a_n/n) exp(2 pi i n z).
End minus start therefore gives

\[
I(\gamma)=\sum_{n\ge1}\frac{a_n}{n}r^n
\left(\cos\frac{-156\pi n}{389}-\cos\frac{10\pi n}{389}\right),
\qquad r=\exp(-2\pi/389).
\tag{4}
\]

The approved ordered schedule for each candidate is
(T,b)=(256,64),(1024,96),(4096,128), with a total of at most nine
evaluations. Production stops at the first interval strictly excluding
zero. Only the first candidate and first schedule pair are evaluated;
the other geometries are certified but their series are not evaluated.
The saved checkpoint preserves complete lattice/cycle data before
interval computation and the actual completed evaluation afterwards.

**Coefficients and complete rational interval evidence.** Import
Cremona's same book,
[Section 2.6, pp.24--26, Euler factors and prime-power recurrences](https://johncremona.github.io/book/fulltext/chapter2.pdf).
All 54 primes through 256 are good for this model. For each, the
producer saves complete model-derived point-count evidence and computes
a_ell=ell+1-#E(F_ell). At odd ell it counts roots using the quadratic
character of 1+4(x^3+x^2-2x); at two it enumerates every affine pair.
The verifier independently creates the histogram H(v)=#{y:y^2+y=v}
by traversing every y, then counts sum_x H(x^3+x^2-2x). This exhausts
all affine pairs without reusing the producer's Euler-criterion method.
Every character entry and affine trace is compared. Coprime coefficients
multiply and good prime powers use a_(ell^k)=a_ell a_(ell^(k-1))-
ell a_(ell^(k-2)); every factorization and all 256 coefficients are
saved and replayed. The approved later schedules would require the
multiplicative factor at 389, but it is absent from this successful
finite sum; no later-schedule execution is claimed.

All subsequent arithmetic is rational and outward on the grid D=2^64.
Machin's identity pi=16 atan(1/5)-4 atan(1/239) is enclosed using 48
terms and adjacent alternating partial sums. The verifier checks the
exact tangent identity; the principal branch follows from
0<4 atan(1/5)-atan(1/239)<4/5<pi/2. Each lower endpoint is rounded down
and each upper endpoint up to this grid. For the endpoints of
h=2 pi/389, the checked domain is 0<h<1. Degree-64 exponential sums
and adjacent degree-65 sums enclose exp(-h), with monotonicity reversing
the endpoints. Thus the saved interval encloses the actual r in (0,1).

Every cosine argument in the retained terms is reduced modulo 389 and
by cosine's evenness. There are 194 distinct required residues; all are
checked. At residue j>0 the full theta interval for 2 pi j/389 has
midpoint t and radius rho. The polynomial
P=sum_(k=0)^48 (-1)^k t^(2k)/(2k)! has error at most |t|^98/98! by
Taylor's theorem of degree 97, whose odd coefficient is zero. The
derivative bound |sin|<=1 adds rho for moving to any theta in the
interval. Hence P+[-epsilon,epsilon], epsilon=|t|^98/98!+rho, is a
valid enclosure. The zero residue, if used, is exactly one. The complete
rational polynomial, theta endpoints, error and outward interval are
saved for every required residue. Degrees are justified by their full
actual remainder, not by a floating-point approximation or an assertion
of sufficient precision.

Complete replay recomputes all 256 powers r^n, both cosine intervals,
their oriented difference, weighted terms and running sums with outward
rounding. The finite sum lies in

\[
[91704808332411743047,91704808332411745265]/D.
\]

Import Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, Lemma 4 and complete proof, pp.6--7](https://arxiv.org/pdf/1608.06423v2).
Its all-n bound |a_n|<=n and full geometric remainder give the combined
omitted error in the two Fourier series at height 1/389 as at most
2 r^257/(1-r). This is an imported all-n theorem, not inferred from the
finite check through 256. The outward next-power and r intervals give
an upper bound of 36259473382926955890/D for this entire tail.
Subtracting/adding that bound to the finite sum proves exactly (2).
Its lower endpoint is strictly positive. No AGM period magnitude,
twist value, normalized symbol or presumed sign enters this computation.
Since I(gamma)=beta*(-1), beta<0 follows.

**Full periods, two real components and relative scale.** Import the
full equality c Lambda_f=Lambda_E stated before Proposition 5.1 in
[Cremona's appendix to Agashe--Ribet--Stein](https://wstein.org/papers/ars-manin/html/node13.html).
Here Lambda_f is the image of all integral absolute cycles, Lambda_E
is the minimal-differential period lattice, and the quotient is optimal
by L031's exact-model import. Import Cesnavicius, *The Manin constant
in the semistable case*, Compositio Math. 154 (2018), 1889--1920,
[arXiv:1703.02951v3, Theorem 2.13, pp.8--9](https://arxiv.org/pdf/1703.02951v3).
The new optimal quotient has H=Gamma_0(389) and exact squarefree conductor
389. Thus p^2 does not divide N for every prime p, including two; the
theorem gives ord_p(c)=0 everywhere, so |c|=1. It supplies the minimal
Manin differential conclusion, not optimality itself. The complete
period lattices agree irrespective of differential sign.

Import Cremona's same book,
[Section 2.8, p.30, following (2.8.9)](https://johncremona.github.io/book/fulltext/chapter2.pdf).
Positive Delta gives the rectangular real lattice and two real components.
If Omega_+ is its least positive purely real period, the total real period
is Omega(E)=2 Omega_+. The projection of the entire period lattice onto
R therefore has generator Omega_+=Omega(E)/2. Keeping both components,

\[
\operatorname{Re}\Lambda_f=I(\ker\delta)
=\beta\tfrac12\mathbf Z
=\operatorname{Re}\Lambda_E=\tfrac{\Omega(E)}2\mathbf Z.
\]

Equality of these nonzero discrete subgroups gives |beta|=Omega(E).
The independent sign already proved beta<0, so beta/Omega(E)=-1.
L030 identified I=beta phi on the entire relative module, so (3) follows
on every relative path. No undetermined boundary functional, plus-lattice
index, isogeny factor or desired scale is used as a premise.

**All normalized values and evidence scope.** Apply (3) to the complete
390 coordinate rows. The new verifier checks every value, every one of
the 780 source rows and 325 saturated rows again after scaling, and the
least common denominator two. Every integral relative path is an integral
combination of these generators, so F(M) is contained in (1/2)Z.
L028's already-justified orientation identifies
S(r)=lambda^+(r)/Omega(E)=F({infinity,r}); every rational cusp path is an
integral relative class. For p>=5 the sole denominator prime two is a
unit, giving C=0 at all levels. This conclusion is normalization only;
L027 still needs coefficient data and its strict limiting-error test.

The new verifier imports no producer. It binds the three complete input
files by their current bytes and runs fresh full fixed-adapter structural
and dual replay before using their coordinates. This rechecks all 1,950
paths, 8,142 segments, normal-form operations and inverse transforms,
all full operator reconstruction, the exact rank-64 dual kernel and all
390 unnormalized functional values. L030's canonical independent
arithmetic proof and the primary source theorems remain mathematical
inputs; hashes and replay flags alone are not proofs of them.

The complete new report has 33,932 passing checks and no failures. It
checks all boundary witnesses, complete kernel inverses and image
primitivity, all three selected cycle geometries, the entire successful
interval computation and all 390 values, as detailed above. A schema-key
KeyError during development is preserved with the actual producer hash
in `development-failure-01.json`; the corrected SL2_lifts key was used
before any certificate was produced. No failed certificate is used.
The script's normal failure path writes failures to disk; its programs
are fixed-instance evidence. That actual report writer is exercised by
the separate critical audit below.

Only after recovery and successful complete replay, the comparison script
opens L032's audited certificate. `comparison.json` binds both current
certificates and the new report, checks the common structural bytes,
scalar and all 390 exact values, and agrees in every case. L032 is a
comparison, not a mathematical premise; neither recovery program reads it
or any twist-ratio certificate. The separate critical audit below validates
this finite assembly under the retained source qualifications. It reproduces
checked source mathematics and leaves the main BSD gap unchanged.

**Separate critical audit, 2026-10-11.** Under the prior SPECIALIZE scope,
the complete proof and producer/verifier contracts were compared with
the approved source hypotheses and the cited input arguments. No mathematical
correction was required. Reproduce this separate audit with

```bash
python3 scripts/conductor389-absolute-cycles/audit_certificate.py
```

Its full report is `scripts/conductor389-absolute-cycles/critical-audit/audit.json`.
The audit executes a byte-identical verifier in a separate mirror directory,
with the three original input files read through the original input
directories. It executes the actual `__main__` report writer, rather than
wrapping only `replay`. The fresh report has the same complete 33,932-check
list and summary as production. Fresh fixed structural audit and verification
reports agree in full with their original counterparts: all 1,950 paths,
8,142 segments, complete saturation, transforms, operator reconstruction
and the rank-64 dual test are retained. The boundary replay includes all
780 endpoints, 780 source rows, 325 saturated rows, all 390 descent checks,
both 65-by-65 inverse products, all 64 integral kernel lifts and image values,
and the complete gcd/Bezout evidence. In particular the image witness at
coordinate 57 is exactly 1/2. Every selected cycle geometry, all 256
coefficients, 194 required cosine residues, 256 terms, both tails and all
390 normalized values pass. These are full computations, not sampled
checks or reliance on saved success flags.

An independent enclosure uses the same oriented geometry (4) and the
fully replayed model-derived coefficients, with a separate elementary
calculation. Its full rational evidence is adjacent
`critical-audit/independent-fourier.json`. For each arctangent it uses 40
terms and the next term of the alternating series; the same exact Machin
identity and principal-branch argument apply. It rounds the resulting pi
interval outwards to denominator D=2^64, forms h=2 pi/389 with exact
rational endpoints, and uses degree-50 and degree-51 adjacent alternating
exponential sums at those endpoints. Their domain is checked to be (0,1).
Monotonicity gives an outward interval [r_l,r_u] contained in (0,1).

For every residue j=0,...,194, it forms the full angle interval,
midpoint t and radius rho. The degree-60 even Taylor polynomial has
error at most |t|^62/62!+rho, by the degree-61 Taylor remainder and the
cosine Lipschitz bound. Outward rounding produces independent cosine
intervals. Every finite term uses direct exact powers [r_l^n,r_u^n]
and rational endpoint products with the oriented cosine difference.
The terms are accumulated as exact rational numbers, without the
producer's repeated rounding of powers, products or running sums.
The finite sum lies in

\[
[91704808332411743983,91704808332411744425]/D.
\]

The complete two-series tail is bounded by the exact rational
2 r_u^257/(1-r_u), whose outward numerator is 36259473382926952018.
Subtracting/adding the exact tail before final rounding gives

\[
I(\gamma)\in
[55445334949484791966,127964281715338696442]/D
\subset(0,\infty).
\]

This distinct interval is contained in (2) and establishes the same
strict sign independently of the producer's rounded recurrence. It
requires no period magnitude, normalized value or twist input. The
argument identifying beta/Omega(E)=-1 then uses exactly the full absolute
image, minimal differential, optimality qualification and two real
components already stated above; no plus-lattice replacement is made.

Eight altered readable JSON cases test input-byte binding, the component
scope, oriented cusp path, kernel inverse, Bezout primitivity, the n=256
coefficient, the complete tail and normalized generator 389. Each case
starts with a deliberately stale success-like sentinel report and runs
the unchanged verifier main in its own directory. All eight exit nonzero
with the specific expected error, replace the sentinel by a nonempty
report whose certificate hash binds the actual altered bytes, and retain
no successful summary. The full altered certificates, outputs and reports
are under `critical-audit/altered/`; `audit.json` records their exact
paths, hashes and errors. This tests the stated valid-readable-JSON
contract only. The report hash read outside the catch does not establish
missing-file or arbitrary I/O-error recovery.

The audit's pre-replay manifest and final comparison establish unchanged
bytes for all 20 original input/program/report/checkpoint artifacts in
scope, including the preserved `KeyError: 'lifts'` development record.
The corrected producer reads `SL2_lifts`, matching the fixed structural
schema; that development error was not a mathematical obstruction.
Only after independent recovery, full replay, the distinct positive
enclosure and all rejection tests does the audit open L032's calibrated
certificate. The common structural bytes, scalar -1, all 390 exact
values and denominator two agree. L032 remains a final comparison only.

This validates the previously unaudited finite instance by reproduction
of the checked method. It neither improves the known source mathematics
nor removes the published optimality qualification, supplies a universal
software theorem, or advances the unresolved arbitrary-curve BSD rank
comparison. PROOF.md's mathematical assembly and DAG inputs are unchanged.

## Mathlib

Full matching fixed conductor-389 boundary/image/oriented-period certificate:
not checked. Supporting integral Manin homology, optimal-period equality,
semistable Manin constant, real-component factors and Fourier enclosure:
not checked. Unknown availability is not absence. Python replay does not
provide formal-library verification or remove the published optimality
qualification. Precise cited theorems and L030's audited arithmetic are
the mathematical inputs; the finite assembly passes the separate informal
critical review above, without a formal-library verification claim.
