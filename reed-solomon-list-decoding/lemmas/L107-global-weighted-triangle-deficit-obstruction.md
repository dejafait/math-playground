# L107 — Global common normalization fails the weighted triangle prerequisite

## Hypotheses

Use exactly L098's N=floor(65537^28/2^128)+1 and fixed pair vector
c_0=1, c_1=...=c_4=0, c_i=alpha*a_i/(2*g_i) for 5<=i<=68,
where g_i=binomial(68,i)binomial(956,i), alpha=2(N-1)/(U-1),
U=binomial(1024,64)/binomial(68,64), and a_i is L021's rational vector.
In particular sum_i g_i*c_i=N and every permitted c_i is positive.
The vertex universe consists of all H=binomial(1024,68) supports.
Keep the complete graph on these vertices, including zero-weight pairs
at forbidden half-distances 1,...,4. Distinct pairs at half-distance i
have proposed distinct-third-vertex demand d_i=(N-2)c_i. Normalize by
one positive common divisor D, required to put all edge weights in [0,1].

## Conclusion

The best admissible divisor is D_*=(N-2)c_max, where
c_max=max_(1<=i<=68)c_i=c_5. For this divisor, the exact missing weight is

    W_* = (H/2)*sum_(i=1)^68 g_i*(1-c_i/c_max)
        = (H/2)*(H-1-(N-1)/c_max).

Every admissible common divisor gives missing weight at least W_*.
Moreover

    W_* >= (H/2)*sum_(i=1)^4 g_i >= 32504*H > H-4.

Thus Gruslys–Letzter Corollary 1.2's sufficient missing-weight hypothesis
fails for every such global common normalization. This stops only this
direct theorem application. It does not prove nonexistence of a weighted
triangle decomposition, failure of unrestricted shared-triple scalar
feasibility, or RS safety/unsafety. The 955–957 bracket is unchanged.
The finite specialization is REPRODUCTION; the separate critical review
below retains this limited theorem-application stop.

## Proof

**Imported theorem and comparison scope.** Gruslys–Letzter,
*Fractional triangle decompositions in almost complete graphs*,
[arXiv:2008.05313v1](https://arxiv.org/pdf/2008.05313v1), 12 August 2020,
Corollary 1.2, printed p.2: if h>=7 and phi:E(K_h)->[0,1] has
sum_e phi(e)>=binomial(h,2)-(h-4), there is a nonnegative triangle
weighting whose sums on edges equal phi. The definitions and Section 3,
pp.4–5, including rational averaging and the limiting case, were inspected
in the saved source assessment. Import the corollary, not the qualified
wording of its auxiliary Lemma 2.4; no computer-assisted base case is
reproved. Here H>=7, so only the edge-weight and deficit hypotheses
need testing. The theorem supplies no prescribed scalar capacities.

L098's exact-cardinality contraction has right side N*c_i. For i>0,
the third support equal to either endpoint has multiplicity one and
value c_i, so subtracting both leaves (N-2)c_i. These are the candidate
distinct-edge demands being tested, with no division by c_i, including
when c_i=0. This necessary demand interpretation is all that is used;
no equivalence between an arbitrary triangle weighting and the full
original t-s-preserving scalar system is asserted. Repeated supports
are not triangles, and no demand at i=0 is an edge demand.

**Optimal common normalization.** Since N>2 and c_max>0, the condition
d_i/D<=1 for every distinct pair is exactly D>=D_*. At D_* the weights
are phi_i=c_i/c_max in [0,1], and at least one equals one. Increasing D
weakly decreases every weight and hence weakly increases total missing
weight. More explicitly the total unnormalized demand is
(N-2)H(N-1)/2>0, so missing weight equals
binomial(H,2)-(N-2)H(N-1)/(2D) and is strictly increasing in D.
Smaller D is inadmissible; larger D cannot improve the comparison.

**Full unordered multiplicities.** For each vertex A, its neighbors at
half-distance i are obtained by deleting i of its 68 points and adding
i of the other 956 points. This gives exactly g_i choices. Each
unordered distinct pair is counted twice over all endpoints, so its
class has H*g_i/2 edges for i>=1. The class i=0 is the single repeated
support per vertex and is omitted. The binomial identity
sum_(i=0)^68 g_i=H follows by choosing another 68-subset according to
its intersection with A. Therefore the classes count all binomial(H,2)
edges. Multiplying their weights and using sum_(i>=1)g_i*c_i=N-1
gives the displayed exact formula for W_*.

Every summand in W_* is nonnegative. At forbidden distances it equals
the entire edge multiplicity, because c_i=0 independently of D.
Already g_1=68*956=65008 gives W_*>=32504H. Since H>0,
32504H-(H-4)=32503H+4>0. Thus the strict failure has a symbolic exact
certificate independent even of which permitted coordinate maximizes
c_i; it cannot be repaired by rounding or by another common scale.
Deleting forbidden pairs from this count would change the required
complete weighted graph and is not this theorem application.

**Finite evidence.** The sole 69-coordinate calculation is reproducible by

    python3 scripts/finite-support/weighted-triangle-deficit-check.py

It reads L021's canonical exact rational vector, reconstructs all c_i
without importing a solver or a large control certificate, and writes
`scripts/finite-support/weighted-triangle-deficit-results.json`.
The certificate saves all 69 pairs, g_i, demands, normalized weights,
unordered edge counts, N,H, optimal divisor, actual deficit, required
maximum H-4, strict slack and the input hash. All 14 exact checks pass.
The rational maximum is uniquely at i=5; its saved value and the entire
actual-deficit rational were inspected, not inferred from a preview.
The actual deficit is an integer, recorded in full in the certificate;
the displayed symbolic formula and 32504H bound suffice for its strict
comparison. The maximizer check is just the 64 rational comparisons
c_i<=c_5, with equality only at i=5; no parameter scan or optimization
is used. Failure of a sufficient hypothesis is no converse theorem.

No scalar upper/lower row, source presentation, PSD condition or
representing-measure condition is established by this calculation.
Other pair prescriptions, other weighted theorems, support-code and
RS realization remain unresolved, independently of the failed import.

**Separate critical audit (2026-10-21, step 400).** The approved audit
reused the inspected Gruslys–Letzter corollary and foundations/04,12,13;
it did not reprove the external theorem or assume its converse.
Independently start with L098's Boolean identity for fixed distinct A,B.
Its normalization divides by s_0=N/H>0, never by c_i. The summands Z=A
and Z=B are distinct, each has moment s_0*c_i and coefficient one;
the respective original indices are (j,t,s)=(0,0,0) and (i,i,i).
Subtracting both therefore gives (N-2)c_i, including null pairs.
At i=0 these are the same support, so one must not subtract twice:
this coordinate is only the objective identity and has no edge demand.
The original certificate correctly records its demand and weight as null
and its edge count as zero.

Counting neighbors by deleted and added points gives g_i, and summing
over endpoints counts each unordered edge twice. Thus the factors H
and 1/2 apply to every distinct class, including forbidden classes;
the sum of all classes is exactly H(H-1)/2. All demands are nonnegative
and their sum is (N-2)H(N-1)/2>0. Consequently admissibility is exactly
D>=(N-2)c_max and W(D)=H(H-1)/2-(N-2)H(N-1)/(2D) is strictly increasing
on positive D. These facts validate the optimal common scale without
using the asserted location of c_max. The zero distance-one pairs give
the independent strict lower-gap certificate
W(D)-(H-4)>=32503H+4>0 for every admissible D. No rescaling, rounding,
or omission of zero-weight edges repairs this application.

The independent checker

    python3 scripts/finite-support/audit_weighted_triangle_deficit.py

imports only L021's canonical rational vector, not the L107 constructor.
It reconstructs N,U,alpha and c_i, computes all g_i both by adjacent-shell
recurrence and integer binomial products, and compares every field of
all 69 saved coordinate records. It checks both repeated-term coefficients,
the complete edge/objective sums, every rational maximum comparison,
all top-level numerical fields and the input hash. In particular c_5 is
strictly greater than each other distinct-pair coordinate, and the full
saved exact deficit is the same integer as its independent reconstruction.
All 580 checks pass with no failures in
`scripts/finite-support/weighted-triangle-deficit-critical-audit.json`.
The complete c_max and deficit values were inspected after reconstruction.
L021's vector and L098's moment necessity are imported local results;
this audit does not re-audit the full LP, any unused PSD claim or scalar
capacity. Both the symbolic obstruction and the stronger finite-data
claims survive. The canonical dependency row remains L021,L098.

## Mathlib

Full matching weighted triangle-decomposition theorem: not checked.
Supporting finite-sum, binomial and rational-arithmetic coverage: not
checked. Unknown availability is not evidence of absence. No Mathlib
result is assumed here.
