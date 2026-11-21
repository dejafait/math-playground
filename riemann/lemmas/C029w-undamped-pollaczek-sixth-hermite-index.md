# C029w — The undamped P_{6,0} has Hermite inertia (5,1,0)

## Hypotheses

Use the exact full real coefficients beta_k and basis p_k specified in
C029n, retaining every odd coefficient. They are Kuznetsov's b_k and
P_k^(3/4)(t/2;pi/2) in *Expansion of the Riemann Xi Function in
Meixner-Pollaczek Polynomials*, Canad. Math. Bull. 51(4) (2008),
561–569, [primary source](https://doi.org/10.4153/CMB-2008-055-0),
recurrence (2) and formulas (4)/(13), printed pp563/566. In particular

    p_(-1)=0, p_0=1,
    (k+1)p_(k+1)(t)=t p_k(t)-(k+1/2)p_(k-1)(t).

Put S=sin(pi/8)/sqrt(2)>0 and q_k=beta_k/S as in C029n. Define

    P_{6,theta}(t)=sum_(k=0)^6 beta_k p_k(t)
                    product_(j=0)^(k-1)(1-j theta),
    U(t)=P_{6,0}(t)/S=sum_(k=0)^6 q_k p_k(t).

The empty product is one. Only theta=0 is considered here: all seven
weights are exactly one. U is different from C029p's Jensen-weighted
T_6/S, whose weights are 6!/((6-k)!6^k).

Use exactly C029n's audited Machin/isqrt rational enclosures for pi and
sqrt(2), both of width 10^(-60), without refinement. Degree, simplicity,
minor signs and index are conclusions, not hypotheses. Once actual
degree six is certified, let s_j be the root power sums with algebraic
multiplicity, s_0=6, and H=(s_(i+j))_(0<=i,j<6).

## Conclusion

U and P_{6,0} have actual degree six. The leading principal determinants
of H have signs

    (Delta_1,...,Delta_6): (+,+,+,-,-,-).

H has inertia (positive,negative,zero)=(5,1,0). P_{6,0} has four distinct
real roots and one distinct nonreal conjugate pair, with all roots simple.
Thus this single endpoint satisfies the proposed negative-index ceiling
one. It supplies no whole-path ceiling, no collision census, no eventual-N
bound, no weighted convergence result and no RH conclusion.

This is a finite known-method reproduction under assessment2048,
independently validated in audit2051 under assessment2049. The earlier
integrity check below is narrower. No novelty beyond the sources
checked or complete RH candidate is asserted.

## Proof

### Exact construction and legitimate normalization

C029n provides the exact source formulas for u_0/S,...,u_8/S and
q_0,...,q_6 in Q(sqrt(2))[pi], and the containment proof for the fixed
input intervals. Its elementary phase reduction is

    sin(pi*m/2+pi/8)/sin(pi/8)=1,1+sqrt(2),-1,-1-sqrt(2)

for m congruent to 0,1,2,3 modulo four. The program reconstructs those
finite sums, including the Bernoulli recurrence through B_18 and the
omission of the negative-index u term for k=0,1. Every exact u and q
coefficient agrees with the pinned C029n certificate. All source
factorial denominators are positive. All q interval endpoints also
agree with that certificate. No trigonometric or floating input is used.

The rational recurrence constructs p_0,...,p_6 coefficient by coefficient.
Each has degree k and leading coefficient 1/k!, verified exactly. Write

    U(t)=sum_(j=0)^6 b_j t^j,
    b_j=sum_(k=j)^6 q_k [t^j]p_k(t).

This is a finite change of basis with denominators k+1 in {1,...,6};
all are nonzero. In particular b_6=q_6/720. Interval Horner evaluation
of each exact coefficient in the unchanged pi/sqrt(2) intervals yields
a strictly negative b_6 enclosure, with the following exact rational
outer bounds (decimal notation here and below denotes exact rationals):

    -8.04778826 * 10^(-5) <= b_6 <= -8.04778825 * 10^(-5).

Thus degree six is certified before normalization. For the monic
polynomial V=U/b_6 write

    V(t)=t^6+c_1 t^5+...+c_6,  c_i=b_(6-i)/b_6.

Every interval division uses that same nonzero b_6 interval. The only
other divisions in the construction are by explicit positive integers.
The scalar S and then b_6 are nonzero, so these normalizations preserve
the roots and their multiplicities. No convergence of V is claimed.

### Newton sums, determinants and inertia

Import Newton's identities from Michel Coste, *An Introduction to
Semialgebraic Geometry* (October 2002), Section1.4.1, Exercise1.13,
printed pp17–18, [author text](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf).
For the actual monic degree-six V these give, with s_0=6,

    s_j=-(sum_(i=1)^(j-1) c_i s_(j-i)+j c_j), 1<=j<=6,
    s_j=-sum_(i=1)^6 c_i s_(j-i),                 j>6.

The script applies the first identity through j=6 and the second for
j=7,...,10, without inserting an extra c_j or using s_0 in the first
sum. These are the power sums with algebraic multiplicities even when
roots repeat. All entries H_ij=s_(i+j) are consequently enclosed.

Use the real-interval inclusion rules of S. M. Rump, *Verification
methods: Rigorous results using floating-point arithmetic*, Acta
Numerica 19 (2010), 287–449,
[corrected primary PDF](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf),
Sections5/5.1/5.5, (5.1)/(5.4)/(5.16)–(5.17). Exact rational endpoints
implement those enclosing operations; division is used only when the
divisor interval excludes zero. This imports the standard inclusion
principle, rather than deriving a new enclosure theorem. The fixed
Machin/isqrt containment is the established C029n input.

For each n=1,...,6 compute the full finite Leibniz expression

    Delta_n=sum_(sigma in S_n) sign(sigma)
                 product_(i=0)^(n-1) s_(i+sigma(i)).

Every one of the n! permutations occurs exactly once. The certificate
stores the permutation, its inversion parity, enclosing signed product,
and the sum interval for each minor. The 1!+...+6!=873 terms are not a
sample or determinant-polynomial preview. No pivot division is used.
The complete resulting rational intervals lie in the following outer
intervals; these outward bounds are verified against the full endpoints:

| n | Scale | Lower bound / scale | Upper bound / scale |
| --- | --- | ---: | ---: |
| 1 | 1 | 6 | 6 |
| 2 | 10^3 | 3.37023139 | 3.37023140 |
| 3 | 10^7 | 8.10122066 | 8.10122067 |
| 4 | 10^13 | -8.59941170 | -8.59941169 |
| 5 | 10^20 | -6.63531988 | -6.63531987 |
| 6 | 10^27 | -1.63766052 | -1.63766051 |

Every minor excludes zero. Coste, Section1.4.2, printed p19, Jacobi's
theorem therefore applies without any zero-minor convention: sign
changes in (1,Delta_1,...,Delta_6) count negative eigenvalues. There is
exactly one change, hence negative index one. Delta_6!=0 implies zero
nullity, and dimension six gives positive index five.

Import the multiplicity-aware Hermite theorem with the interpretation
already recorded in C029l: Daniel Plaumann, *Real Algebraic Geometry*,
IHP lectures (14 October 2023), Theorem1.1 and full proof, printed pp3–4,
[primary text](https://rtca2023.github.io/pages_Paris/files_m5/rag-ihp.pdf).
For a real monic polynomial, Hermite rank counts distinct complex roots,
signature counts distinct real roots, and negative index counts distinct
nonreal conjugate pairs. Here rank six equals the actual degree, so all
roots are simple; signature 5-1=4 gives four real roots and the remaining
two form one conjugate pair. Applying the theorem does not assume
reality, simplicity or an index bound in advance.

### Reproduction and verification limits

Run from this notebook:

    python3 scripts/pollaczek/jensen_zero_endpoint_2049.py
    python3 scripts/pollaczek/jensen_zero_endpoint_integrity_2049.py

The first program saves the full certificate, exact source and monomial
coefficients, basis, fixed intervals, all normalization denominators,
s_0,...,s_10, the complete Hermite matrix and all signed determinant
terms in `scripts/pollaczek/jensen-zero-endpoint-2049.json`. All 28
construction/completeness checks pass; no minor is unresolved. Input
hashes pin C029n's certificate and helper script, and the certificate
also records this calculation script's hash. The input hashes are

    tilted-boundary-metric-2010.json:
    361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7
    tilted_boundary_metric_2010.py:
    21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc

The separate integrity script reads every stored signed-term endpoint,
checks permutation completeness/parity, sums them as exact rationals,
checks every saved determinant endpoint and its strict sign, and verifies
the readable bounds contain the complete intervals. Its 34 checks pass,
with evidence in `scripts/pollaczek/jensen-zero-endpoint-integrity-2049.json`.
The complete normalization endpoints and all readable strict-sign bounds
were also inspected with the shared JSON inspector. No truncated preview
is used to infer a sign. This integrity check does not independently
reconstruct source coefficients, Newton sums or determinant products;
the stronger independent replay is recorded next.

### Independent arithmetic and applicability audit2051

Run from this notebook:

    python3 scripts/pollaczek/jensen_zero_endpoint_audit_2051.py

This separate program imports no original calculation or arithmetic
helpers. It reconstructs the source formulas as sparse polynomials in
pi and sqrt(2), retaining all odd coefficients and all seven unit weights.
It checks the unchanged pinned C029n inputs, all Bernoulli and u/q
coefficients, every source denominator, the separately implemented
rational basis recurrence, all monomial coefficients, and all their
complete interval endpoints. It uses the audited2012 fixed pi/sqrt(2)
containment as an input; it neither refines those intervals nor replaces
their proof by a decimal approximation.

The independently reconstructed b_6 interval is identical to the saved
one and is contained in the strictly negative rational bounds displayed
above. Thus degree is established before division. Its reciprocal has
endpoints (1/upper,1/lower), valid on the negative half-line. Every monic
coefficient endpoint, every unsigned Newton term in both degree ranges,
all eleven sums s_0,...,s_10 and all 36 Hermite entries agree exactly.
The only nonconstant division is this normalization; the source and
basis formulas divide only by explicit positive integers.

For the determinant replay, recursively select a column from the ordered
remaining columns at each row. Selecting its zero-based rank r contributes
r inversions with the columns to be chosen later, so contributes (-1)^r
to permutation parity. This construction generates every permutation
once; the script independently checks uniqueness, n! completeness and
the ordinary inversion-count parity. Multiplication traverses the rows
in reverse order, using the independently reconstructed Newton sums.
It compares the full endpoints of each of the 873 enclosing signed
products, then all six sum endpoints, with the original certificate.
Every equality holds. The canonical rational outer bounds and the saved
readable bounds contain the complete reconstructed intervals, and all
six strict signs are reproduced. No preview is used for an inequality.

All 79 checks pass without failures or unresolved minors. Full rebuilt
coefficients, normalization divisor/reciprocal, Newton terms/sums,
Hermite entries, signed products and determinant endpoints are retained
in `scripts/pollaczek/jensen-zero-endpoint-audit-2051.json`, with input
and audit-script hashes. This is independent arithmetic reconstruction,
not formal verification or independent discovery of a root-count theorem.

On paper, actual real monic degree six is now justified, every leading
minor is nonzero, and exactly one sign change occurs starting from
Delta_0=1. These pay Jacobi's hypotheses, with no zero-minor convention.
Hermite's theorem permits multiplicities rather than assuming simplicity:
rank six first proves simplicity, then signature four counts the real
roots. Scaling by the nonzero S and b_6 preserves every root and its
multiplicity. Thus the stated inertia and root counts survive the audit
without a correction. C029l supplies only the Hermite interpretation;
its compact-limit assertion and C029m's conditional conclusion are unused.

The finite pass leaves all interior parameters and exceptional fibers
unexamined. It does not establish any relation between varying degree
and this fixed-degree parameter, or pay C029m's eventual index premise.
Its weighted-convergence/upstream[9] qualification is unused. Actual-Xi
all-degree positivity remains open. C029p is the different endpoint
comparison, not a premise in this calculation; C029q/r/v and earlier
stops likewise are not mathematical inputs to the proof.

## Mathlib

Full matching finite calculation, Newton/Hermite/Jacobi implementation
and interval coverage not checked in Mathlib. No absence or formal
verification claim is made. The argument imports the cited standard
theorems and specializes them only to the specified finite coefficients.
