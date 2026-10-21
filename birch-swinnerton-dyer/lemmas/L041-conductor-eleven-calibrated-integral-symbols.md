# L041 — Conductor-eleven calibrated integral symbols

## Hypotheses

Let E/Q be the globally minimal curve
y^2+y=x^3-x^2-10x-20, with coefficients [0,-1,1,-10,-20].
Let f be its normalized weight-two newform of conductor 11 and
Omega(E)=integral_(E(R)) |omega_E| its total real Neron period.
Let p>=5 be good ordinary for E, with p!=5. Use L028's symbol
conventions and its prime-twist normalization theorem.

Import audited L039's complete torsion-free relative integral presentation
at Gamma_0(11), all twelve oriented Manin generators g_i, i=0,...,11,
and full-relative real-integration line phi with quotient-basis row
(5/2,5,1). Import audited L040's independently certified
q=L(E^5,1)/Omega(E^5)=5, with its explicit published computational
optimality qualification. Neither input is reproved or strengthened here.
The generic adapter's supplied arithmetic provenance remains conditional;
L039's independent local arithmetic proof supplies this fixed model's
minimality, Delta=-11^5, conductor and non-CM hypotheses.

Full new finite evidence is
`scripts/conductor-eleven/calibrated-symbols/certificate.json`, SHA256
`c241f7531f5246eda9fc7ed6b44ab847f4fe3986aecf87c7883ddd2ecf8a6242`.
The complete independent replay is the adjacent `verification.json`.
Reproduce from the notebook root:

```bash
python3 scripts/conductor-eleven/calibrated-symbols/build_certificate.py
python3 scripts/conductor-eleven/calibrated-symbols/verify_certificate.py
```

This fixed finite specialization reuses known algorithms; no universal
software correctness, rank, Sha finiteness or coefficient is assumed.
Its production replay and separate critical audit of the new assembly
and programs pass, with the complete additional evidence below.

## Conclusion

For the quadratic character modulo five, set
G_5=sum_(a=1)^4 chi(a){infinity,a/5}, with signs (1,-1,-1,1).
In L039's integral quotient basis,

\[
[G_5]=(0,5,0)^t,\qquad \phi(G_5)=25,\qquad
F=\frac{5}{25}\phi=\frac15\phi=\frac{I}{\Omega(E)}.
\]

Here I({alpha,beta})=Re(2 pi i integral_alpha^beta f(z) dz).
The complete calibrated generator values, in the retained order, are

\[
(F(g_0),\ldots,F(g_{11}))=
(-1/5,1/5,0,1,1/2,-1/2,-1,-1,-1/2,1/2,1,0).
\]

Their least common denominator is 10=2*5. Therefore the all-argument
bound in L028, for every retained p, is C=0:

\[
F(M)\subseteq\mathbf Z_p,\qquad
v_p\bigl(S(r)\bigr)\ge0\quad\text{for every }r\in\mathbf Q,
\quad S(r)=F(\{\infty,r\}).
\]

This supplies L027's exact normalization and all-level denominator input
for this model. It supplies no finite coefficient enclosure or
nonvanishing inequality, rational point certificate, Sha elimination,
complex/p-adic order comparison or arbitrary-curve BSD resolution.

## Proof

**Known inputs and applicability.** Import L028, whose named inputs are
Stein, *Modular Forms, a Computational Approach*, online v0.1,
[weight-two Propositions 3.10--3.11 and Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html)
for integral path generation and the full Manin presentation modulo
all torsion; Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition, [Section 2.11, pp.38--39, identity preceding (2.11.4)](https://johncremona.github.io/book/fulltext/chapter2.pdf)
for the oriented quadratic-character integral; and Pal,
[arXiv:1012.0094v2, Corollary 2.6 and Theorem 3.2, pp.6--8](https://arxiv.org/pdf/1012.0094v2)
for the positive minimal-twist total-period comparison. L028 also checks
the plus convention in Stein--Wuthrich, Math. Comp. 82 (2013),
[Section 3, p.1762](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf).
These results and L028's normalization/valuation argument are imported,
rather than reproved to obtain another lemma.

Five is positive prime, 1 modulo 4 and prime to Delta=-11^5 and to p.
Thus the Gauss sum is positive sqrt5 and Pal's minimalization factor is
one. L039 supplies the entire relative integral lattice and the real line,
rather than just an absolute-cycle line. L040 supplies independent nonzero
q=5 using no unknown scalar from phi. These are precisely L028's
applicability conditions. It remains to produce the new fixed-instance
oriented character sum and all calibrated integral values.

**Path witnesses.** Retain L039's projective coset order
(0,1),(1,0),(1,1),...,(1,10) modulo 11. Denote by e_i the i-th
standard vector of the raw Z^12 presentation. All four cusp paths begin
at infinity; their exact checked chains, raw sums and quotient coordinates
are as follows. Endpoint directions in each chain are left to right.

| a | Endpoint chain | Raw integral sum | Quotient coordinates | phi value |
|---|---|---|---|---|
| 1 | infinity, 0, 1/5 | e_1+e_10 | (0,1,1) | 6 |
| 2 | infinity, 0, 1/2, 2/5 | e_1+e_7+e_5 | (-1,-1,1) | -13/2 |
| 3 | infinity, 0, 1, 1/2, 3/5 | e_1+e_2+e_6+e_8 | (1,-2,1) | -13/2 |
| 4 | infinity, 0, 1, 4/5 | e_1+e_2+e_3 | (0,1,1) | 6 |

For completeness the following table lists every distinct segment in
these chains. A four-tuple denotes a row-major 2-by-2 matrix. Let g_i
be L039's certified SL2 lift for coset i. Each saved segment h satisfies
det(h)=1, sends 0 to the start and infinity to the end, and has
gamma=h g_i^(-1) in Gamma_0(11). Thus its integral relative class is
the indicated generator with positive coefficient, even for a matrix
whose column has negative numerator and denominator.

| Segment | h | i | gamma=h g_i^(-1) |
|---|---|---|---|
| infinity to 0 | (0,1,-1,0) | 1 | (-1,0,0,-1) |
| 0 to 1/5 | (1,0,5,1) | 10 | (9,1,44,5) |
| 0 to 1/2 | (1,0,2,1) | 7 | (6,1,11,2) |
| 1/2 to 2/5 | (-2,1,-5,2) | 5 | (-9,-2,-22,-5) |
| 0 to 1 | (1,0,1,1) | 2 | (1,0,0,1) |
| 1 to 1/2 | (-1,1,-2,1) | 6 | (-6,-1,-11,-2) |
| 1/2 to 3/5 | (3,1,5,2) | 8 | (20,3,33,5) |
| 1 to 4/5 | (-4,1,-5,1) | 3 | (-9,-4,-11,-5) |

Every determinant, ordered endpoint, gamma product and lower-left
divisibility in this table is exact. Repeated segments are also checked
at every occurrence: the certificate contains twelve segments, not eight
sampled occurrences. Geometric adjacency and the final endpoints telescope
each chain to its claimed oriented path. The independent checker obtains
each coset by exhausting the ten units modulo 11, rather than sharing the
builder's inverse lookup. It checks the exact finite continued fractions
(0,5),(0,2,2),(0,1,1,2),(0,1,4); path identification relies on the
ordered endpoint and Gamma_0 witnesses. All twelve raw coordinates and
all three quotient coordinates are replayed on each path.

Weighting these four rows with (1,-1,-1,1) gives the full raw sum

\[
z=(0,0,0,1,0,-1,-1,-1,-1,0,1,0)^t,
\qquad [G_5]=(0,5,0)^t.
\]

Both the weighted-coordinate sum and direct projection of z are checked.
Evaluation gives d=6-(-13/2)-(-13/2)+6=25, also equal to
(5/2,5,1)(0,5,0)^t. It is nonzero. L028 therefore identifies the exact
Neron-normalized real functional on all of M as F=(q/d)phi=phi/5.
The orientation and total-period factors are supplied by L028's audited
proof; F(G_5)=5 is a consistency check using independent q, not a new
independent proof of the twist ratio.

**Every value and relation.** In L039's generator order the integral
coordinates are

\[
\begin{split}
&(0,0,-1),(0,0,1),(0,0,0),(0,1,0),(-1,1,0),(-1,0,0),\\
&(0,-1,0),(0,-1,0),(1,-1,0),(1,0,0),(0,1,0),(0,0,0).
\end{split}
\]

Evaluating F's quotient-basis row (1/2,1,1/5) on all these coordinates
gives exactly the twelve values in the conclusion. The checker compares
them both with (1/5) times all L039 values and with the independently
computed dot products; it also verifies z's evaluation is five.
No rational-basis denominator is omitted.

The checker reconstructs every order-two and order-three Manin relation
from the projective representatives and exhaustive unit-orbit lookup,
including repeated indices. All 24 reconstructed rows equal L039's full
source matrix A. It also checks all nine columns of the saturated-kernel
matrix K from that audited integral presentation. Every row/column pairs
to zero with both phi and F, and every saved residual is the exact zero
rational. L039 supplies the complete lattice identification and saturation;
the new relation checks certify descent of this functional on that lattice.
Neither a new rational dimension guess nor a new saturation theorem is
being inferred from those zeros.

**All-argument denominators and evidence scope.** Each reduced y_i=F(g_i)
has denominator dividing ten. The denominator five occurs at i=0 and
the denominator two at i=4, so the least common denominator is exactly
ten; both valuation witnesses have exponent one. Its complete prime
factorization is 2^1*5^1. For p>=5, p!=5, every nonzero y_i has
v_p(y_i)>=0. Zero values have infinite valuation. L028's finite-lattice
argument then gives C=max({0} union {-v_p(y_i): y_i!=0})=0 and
v_p(S(r))>=0 for every rational r. This applies to every level required
by L027 without enumerating infinitely many arguments or presuming which
primes are ordinary. The p=5 denominator is retained and explicitly
excluded; it is not silently declared integral.

The complete replay checks eight grouped conditions with no failures:
all current input bindings to the audited L039/L040 files and programs,
the exact instance, every coordinate and original functional value,
all four paths and twelve segments, the nonzero character sum, the scale
and all twelve calibrated values, all 24/nine relations, and the complete
denominator/valuation evidence. The certificate binds both prior audit
records and all original evidence they bind, including L040's distinct
enclosure. All originals remain unchanged. Byte binding reuses the
audited mathematical premises; it does not prove external source theorems.
The finite checker imports no construction program and recomputes all
new mathematical evidence, rather than trusting its success flag.

This is local production of a known-method fixed input. No coefficient
inequality is tested, no candidate BSD argument is asserted, and the
remaining arithmetic and arbitrary-complex-order gaps persist.

**Separate critical audit (2026-10-10).** The complete L028 proof, L039's
audited entire lattice and line, L040's independent q and qualifications,
this complete assembly and both new programs were reviewed under the
prior SPECIALIZE assessment. No mathematical correction was needed.
Reproduce the bounded audit from the notebook root by

```bash
python3 scripts/conductor-eleven/calibrated-symbols/audit.py
```

The full report is
`scripts/conductor-eleven/calibrated-symbols/critical-audit/audit.json`.
The four original production files and audit program are copied under
`originals/` before replay; `pre-replay-manifest.json` binds them and every
prior input. Complete replay executes the preserved verifier on a copy,
writes a fresh report under `replay/`, and agrees exactly with the original
report. This checks all twelve segment occurrences, all four paths and
all eight original grouped conditions. Neither original evidence nor any
prior bound input changes. Hash agreement establishes provenance only.

To test the continued-fraction programs' potentially shared choices, the
audit specifies the following upper Farey chains directly, without either
continued-fraction routine. All four raw representatives differ from
their original counterparts. Their full quotient coordinates agree:

| a | Alternative chain | Alternative raw sum | Quotient coordinates |
|---|---|---|---|
| 1 | infinity, 1, 1/2, 1/3, 1/4, 1/5 | e_1+e_6+e_4+e_3+e_9 | (0,1,1) |
| 2 | infinity, 1, 1/2, 2/5 | e_1+e_6+e_5 | (-1,-1,1) |
| 3 | infinity, 1, 2/3, 3/5 | e_1+e_8+e_7 | (1,-2,1) |
| 4 | infinity, 1, 4/5 | e_1+e_3 | (0,1,1) |

Here is every distinct segment of these chains, with the same matrix
and orientation conventions as the production table above:

| Segment | h | i | gamma=h g_i^(-1) |
|---|---|---|---|
| infinity to 1 | (-1,1,-1,0) | 1 | (-1,-1,0,-1) |
| 1 to 1/2 | (-1,1,-2,1) | 6 | (-6,-1,-11,-2) |
| 1/2 to 1/3 | (-1,1,-3,2) | 4 | (-4,-1,-11,-3) |
| 1/3 to 1/4 | (-1,1,-4,3) | 3 | (-3,-1,-11,-4) |
| 1/4 to 1/5 | (-1,1,-5,4) | 9 | (-9,-1,-44,-5) |
| 1/2 to 2/5 | (-2,1,-5,2) | 5 | (-9,-2,-22,-5) |
| 1 to 2/3 | (-2,1,-3,1) | 8 | (-15,-2,-22,-3) |
| 2/3 to 3/5 | (-3,2,-5,3) | 7 | (-20,-3,-33,-5) |
| 1 to 4/5 | (-4,1,-5,1) | 3 | (-9,-4,-11,-5) |

Each h has determinant one, its second column is the start cusp and
its first column is the end cusp in projective coordinates. Each gamma
has determinant one and lower-left entry divisible by eleven; direct
multiplication gives h=gamma g_i. These facts identify the oriented
segment with g_i. All thirteen occurrences are checked. The audit's
coset identification exhausts the exact products h g_i^(-1), rather
than either program's modular bottom-row lookup. Path additivity then
identifies each entire chain with {infinity,a/5}.

For a further integral check, let K be L039's 12-by-9 saturated-kernel
matrix, with its retained column order, and let delta_a be the alternative
raw vector minus the original raw vector. Exact multiplication gives
delta_a=K c_a for all four following **integer** vectors:

\[
\begin{split}
c_1&=(0,0,0,1,1,0,1,0,-1)^t,\\
c_2&=(0,0,0,1,0,0,0,-1,-1)^t,\\
c_3&=(0,0,-1,-1,0,0,0,1,1)^t,\\
c_4&=(0,0,-1,0,0,0,0,0,0)^t.
\end{split}
\]

All twelve entries of each equality and all three quotient coordinates
are checked. Thus the comparison holds in the entire integral relative
quotient, not merely after evaluating phi. The complete segment, raw,
quotient and saturated-relation witnesses are saved in the adjacent
`alternative-paths.json`. Weighting the alternative rows by (1,-1,-1,1)
again gives quotient (0,5,0), hence d=25. Independent L040 gives q=5;
L028 therefore gives scale 1/5. Agreement with F(G_5)=5 is still only
a calibration consistency check.

All twelve generator values are evaluated again from the full quotient
coordinates and compared with the complete displayed value list. Each
source relation is separately reconstructed by right-multiplying the
integral lifts by S=(0,-1,1,0) and U=(0,-1,1,-1), including both U and
U^2. The exact Gamma_0 lookup identifies the resulting cosets. All 24
rows equal the source matrix, all nine saturated columns have zero
projection, and all 33 pairings with F are zero. These checks retain
the complete lattice theorem from L039 rather than trying to infer
completeness from those zero pairings.

The complete reduced-denominator list is
(5,5,1,1,2,2,1,1,2,2,1,1). Its lcm is exactly ten; indices 0 and 4
witness the factors five and two. Since every integral relative class
is an integer combination of these generators, its F-value lies in
(1/10)Z. Every rational cusp path is such an integral class by L028's
imported generation theorem. Consequently the claimed valuation bound
holds at all rational arguments for every stated p>=5, p!=5, with
C=0. No enumeration of arguments or assumption of vanishing lower
coefficients enters this inference. In particular the nonintegral
five-adic generator value -1/5 has not been lost.

Five separate corrupted copies test reversed starting orientation, a
changed full-relative coordinate, an incorrect scale, an altered generator
value and omission of five from the denominator. The complete verifier
rejects each, replaces a seeded success report with a fresh failure report
binding that copy, and leaves empty result fields. These expected failures
are retained under `rejections/`; they are supplementary sensitivity tests,
not proofs of universal software soundness. The twenty audit comparisons
pass with no unexpected failure. The original files remain unchanged.

This separate audit validates the fixed normalization and all-level
denominator inputs only. Published computational optimality/torsion and
external theorem qualifications in L040 remain imports. L039's generic
SUPPLIED_CONDITIONAL provenance remains distinct from its local arithmetic
proof. No theorem beyond the cited methods, quadratic coefficient, point
witness, Sha conclusion or arbitrary-curve rank comparison is supplied.

## Mathlib

Full matching calibrated relative-symbol certificate: not checked.
Supporting Manin presentation, cusp-path orientation, quadratic-twist
period, rational linear algebra and p-adic valuation coverage: not checked.
Unknown coverage is not absence. The named results above and audited
L028/L039/L040 are the mathematical inputs, with all their qualifications.
