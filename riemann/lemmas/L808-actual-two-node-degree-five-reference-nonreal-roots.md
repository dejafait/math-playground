# Lemma 808: the actual two-node degree-five reference has a nonreal pair

## Hypotheses

Use the actual probability law nu and exact two-node Gaussian nodes
v_1<v_2 and weights w_1,w_2 of audited L805, with its inherited
L791/L778 analytic evaluator and Decimal backend contracts. Use the
complete independent node/weight enclosures of step542, not a fitted
measure or the rounded display boxes. With L795's normalization define

\[
 Q(x)=Q_{2,5}(x)=\sum_{i=1}^2 w_i
       \sum_{j=0}^5(-1)^j\binom5j\frac{j!}{(2j)!}v_i^j x^j.
\]

This is the particular quadrature reference, not actual P_5. Only
moments through degree three are Gaussian-exact; actual fourth and
fifth moments are not substituted for quadrature moments.

## Conclusion

Q has exactly three simple positive real zeros and two simple nonreal
conjugate zeros. Each following open disk, of radius 1/100, contains
exactly one zero, counting multiplicity. Every displayed finite decimal
is an exact rational center:

| center | location of its zero |
| --- | --- |
| 19.379606 | positive real |
| 26.150079 - 18.380803i | nonreal |
| 26.150079 + 18.380803i | nonreal |
| 123.335006 | positive real |
| 216.169131 | positive real |

Thus the five-simple-positive-root prerequisite for a real-reference
barrier fails already for this actual n=2,d=5 reference. This conclusion
does not challenge known actual P_5 hyperbolicity, disprove RH, exclude
other references, or prove any degree-uniform mixed-sign assertion.
It is a finite computer-assisted specialization of known root-counting
tools, with no claim of a new general theorem or certified originality.
The independent finite audit below validates this certificate, retaining
the inherited evaluator contracts.

## Proof

**Input identity and normalization.** L805 proves that the actual
Gaussian nodes and weights exist, are strictly positive, and satisfy
w_1+w_2=1 exactly. Its step542 audit supplies rational enclosures of
these exact quantities with the inherited evaluator contracts retained.
L795 supplies the finite Laguerre coefficient formula. Set
S_j=w_1v_1^j+w_2v_2^j. The six ascending coefficients of Q are exactly

\[
 1,\quad -\tfrac52 S_1,\quad \tfrac56 S_2,\quad
 -\tfrac1{12}S_3,\quad \tfrac1{336}S_4,\quad
 -\tfrac1{30240}S_5.                                      \tag{1}
\]

The constant 1 uses the exact weight identity, not an interval
residual containing zero. Since S_5>0, Q has degree exactly five and
real coefficients. The factorial identity in (1) is checked for all
six j in the program; there is no extra factor of 4 or m_0.

**Finite certificate and provenance.** Run
`python3 scripts/theta-gauss/reference_roots_551.py`.
The complete certificate is
`scripts/theta-gauss/reference-roots-certificate-551.json`.
The input is `scripts/theta-gauss/audit-certificate-542.json`.
The program checks its PASS, all 106 recorded checks and empty failure
list, its program digest, and every current input hash in its provenance
map. In particular, the step540 certificate digest must equal
`f007b42bb0a51a1a9b13c39c5ee3b6010c605b33c0c87d95a271754a54db9f63`,
and the actual moment source digest must equal
`2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e`.
This reuses the audited boxes; it does not independently replay the
106-check audit or the transcendental theta evaluator.

The complete selected node and weight endpoints were inspected.
Parse them as exact Fractions and round each lower endpoint down and
upper endpoint up to a multiple of 10^(-40), checking containment.
All node and weight lower endpoints remain positive; node boxes are
ordered and disjoint. Addition takes endpoint sums, negation reverses
endpoints and signs, and multiplication takes extrema of the four
endpoint products. Repeated interval multiplication gives powers.
Apply these rules to S_j and (1), retaining every resulting rational
endpoint. Correlation loss only widens the boxes; no independence or
midpoint equality is assumed. The leading coefficient box is strictly
negative. The certificate contains all six coefficient boxes, all
quadrature moment boxes and exact input hashes.

**Imported root-counting theorem.** Becker, Sagraloff, Sharma and Yap,
*A Near-Optimal Subdivision Algorithm for Complex Root Isolation based
on the Pellet Test and Newton Iteration*, arXiv:1509.06231v4,
8 November 2016,
[Definition1, equations(3)-(4), and Theorem1, pp.12-13](https://arxiv.org/pdf/1509.06231v4),
state the Pellet test: for a complex polynomial F, r>0,
0<=k<=deg(F), K>=1,

\[
 |F^{(k)}(m)|r^k/k!>
 K\sum_{j\ne k}|F^{(j)}(m)|r^j/j!
                                                               \tag{2}
\]

certifies exactly k roots in the disk, counted with multiplicity.
We import this theorem with k=1,K=1; no simple-root assumption,
arbitrary-precision oracle, termination guarantee, general isolation
algorithm or reproof is used. The prior SPECIALIZE source assessment
is `drafts/literature/2026-11-05-theta-gauss-post-exact-reference-roots.md`.
Q is a degree-five complex polynomial, so the theorem's polynomial
hypothesis applies; its inequalities are supplied below.

**Exact application.** A single numpy root list of the midpoint
coefficient polynomial is used only to select the five rational centers
in the table. It has no evidentiary role. For each center m and each
0<=k<=5 construct the Taylor coefficient enclosure

\[
 T_k(m)\supseteq Q^{(k)}(m)/k!
       =\sum_{j=k}^5\binom jk c_j m^{j-k}.                    \tag{3}
\]

Complex interval multiplication uses
(a+ib)(c+id)=(ac-bd)+i(ad+bc), with the real interval operations
just specified. For a real interval I define
ell(I)=0 if 0 belongs to I, otherwise the smaller endpoint magnitude;
u(I) is the larger endpoint magnitude. For a rectangle R=I+iJ,

\[
 \max\{\ell(I),\ell(J)\}\le |z|\le u(I)+u(J)
       \quad(z\in R).                                     \tag{4}
\]

These conservative bounds require no floating square root. Denote
the lower and upper bounds for T_k by ell_k,u_k. For r=1/100
the program computes the exact rational quantities
L=r ell_1 and U=sum_(k!=1) r^k u_k. All Taylor rectangles, modulus
bounds, six summands (zero in slot1), their sum and L-U are saved.
The following simpler rational bounds were checked against those
complete quantities:

| center | L at least | U strictly less than |
| --- | --- | --- |
| 19.379606 | 10^(-4) | 10^(-7) |
| 26.150079 - 18.380803i | 10^(-4) | 10^(-6) |
| 26.150079 + 18.380803i | 10^(-4) | 10^(-6) |
| 123.335006 | 10^(-3) | 10^(-6) |
| 216.169131 | 10^(-2) | 10^(-5) |

In every row L>U, hence (2) holds for the exact Q, not merely its
midpoint polynomial. All five tests pass on the first region choice;
the permitted fallback radius is not used. Exact squared distances
between every pair of centers exceed 1, whereas (2r)^2=1/2500.
Thus the five disks are pairwise disjoint. The test counts one root
with multiplicity in each disk, so each of these roots is simple.
The fundamental theorem of algebra for degree-five Q exhausts all
complex zeros. No unseen or boundary zero can remain.

Since Q has real coefficients, conjugation preserves its zero multiset.
A disk centered on the real axis is invariant under conjugation. Its
unique root, counted with multiplicity, must therefore be real. All
three real centers exceed r, so their roots are strictly positive.
The other two disks lie strictly below/above the real axis because
18.380803>r. Their zeros are nonreal and conjugate to each other,
by conjugation of their centers and root uniqueness. This proves the
asserted geometry and the failure of the positive-root prerequisite.

**Scope.** L807's signed error identity supplies no hypothesis here.
The conclusion stops only this reference-root premise; it neither
assumes nor tests a common interlacer. Actual P_5, later signed
compensation, other n and the main all-degree mixed positivity gap
remain separate. Python Fraction/integer arithmetic and the audited
analytic/backend contracts remain trusted components. No new theta
precision was requested. The original program's PASS alone is not
independent critical review; the separate finite replay below supplies
that review within this scope.

### Independent finite audit — 5 November 2026, step553

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-05-theta-reference-root-audit.md`.
Run `python3 scripts/theta-gauss/reference_audit_553.py`; the complete
evidence is `scripts/theta-gauss/reference-audit-certificate-553.json`.
All 161 checks pass with no failures or mathematical defect found.
Neither step551's implementation nor the earlier audit implementation
is imported or executed, and no approximate roots or new theta moments
are computed. The already audited L805 construction is reused, with
its analytic/Decimal contracts retained rather than independently proved.

The replay checks every source hash in step551 and step542, step540's
provenance and inherited-original maps, and both recorded step551/542
program digests against current files. It checks the fixed step540 and
actual-moment digests stated above and the exact provenance-map scope.
Step542's 106-check record identifies the reused audited result; its
Boolean flags are not a substitute for today's reconstructed arithmetic.
All original input files remain unchanged.

The complete independent node and weight endpoints in step542 equal
step551's selected inputs. Integer floor/ceiling division independently
reconstructs their outward 10^(-40) coarsening, checks containment,
positivity and node ordering, and reproduces the saved coarse boxes.
Because the inputs are positive, the jth moment endpoints can be
computed directly as sum_i w_(i,end) v_(i,end)^j for end=lower,upper.
These give exactly the original repeated-multiplication enclosures,
including all six complete quadrature moment boxes. All factorial
factors and six coefficient boxes reproduce. For the constant term,
L805's exact formulas (5) give numerator sum v_2-v_1 over the same
nonzero denominator, hence w_1+w_2=1; an interval containing 1 is only
a consistency check. The degree-five coefficient upper endpoint is
strictly negative. No theta moment of order four or five is substituted
for its Gaussian counterpart.

For each saved rational center, the independent program builds the
exact point powers m^j by rational complex multiplication. It then
forms each real and imaginary Taylor interval as the scalar interval
sum of binom(j,k)c_j times the corresponding component of m^(j-k).
This uses linear combinations of point powers rather than the original
complex-interval multiplication implementation. Every endpoint of all
30 Taylor rectangles agrees exactly with the saved evidence. Independent
component absolute-value bounds give all 30 modulus bounds in (4).
Every radius power, all six upper summands with the k=1 slot set to
zero, each dominant lower bound, summed upper bound and strict margin
are reconstructed and compared as full rational numbers. None of the
original acceptance flags enters these strict comparisons.

In table order, the exact ratios L/U are strictly greater than
1838, 706, 706, 4751 and 3665 respectively, whereas the Pellet test
requires only L/U>1. The complete rational values also satisfy every
simpler lower/upper bound displayed above. All ten squared center
distances exceed 1>(2/100)^2. The three real-centered disks satisfy
m>1/100; the other two centers are conjugates at distance
18.380803>1/100 from the real axis. These are all hypotheses needed
for the imported k=1,K=1 test, the real-coefficient conjugation argument
and degree-five exhaustion already given. In particular no multiple
root, boundary root or additional unseen root is left uncounted.

Thus this finite three-positive-root/nonreal-pair conclusion is audited.
It remains a reproduction and applicability check of known root-counting
tools, not a new general root theorem or a resolution of the main gap.
Actual P_5, signed compensation and all-degree transfer remain separate.

## Mathlib

Full matching coverage is unchecked. Availability of the exact theta
quadrature specialization and Pellet certificate in Mathlib is unknown;
no formal verification or absence claim is made. Named root counting
and algebraic zero-count inputs are imported with the hypotheses above.
