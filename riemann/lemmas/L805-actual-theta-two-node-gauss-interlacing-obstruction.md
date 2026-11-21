# Lemma 805: actual theta two-node Gaussian compression and interlacing obstruction

## Hypotheses

Use L019/L021's actual strictly positive theta kernel K and moments
m_j=integral_0^infinity u^(2j)K(u)du. Let mu=K(u)du/m_0 and let nu
be its pushforward under v=u^2. Write t_j=m_j/m_0. Use L795's
normalizations P_d and F_(d,u). Only the actual gamma(0..3) enclosures
of L791, gamma(j)=j!m_j/(2j)!, are numerical inputs. Retain L791's
step478 audit and inherited L778 analytic evaluator/Decimal software
contracts. This is a computer-assisted informal specialization, not
formal verification; neither the fitted model nor its roots are inputs.

## Conclusion

The exact two-node Gaussian rule of nu has distinct positive nodes
v_1<v_2 and positive weights w_1,w_2 with w_1+w_2=1. It reproduces
t_0,...,t_3 and gives the exact polynomial identity

\[
 P_3(x)=w_1F_{3,\sqrt{v_1}}(x)+w_2F_{3,\sqrt{v_2}}(x).       \tag{1}
\]

Outward bounds, all finite decimals denoting exact rationals, are

\[
\begin{split}
 .024088&\le v_1\le .024089,& .219102&\le v_2\le .219103,\\
 .886564&\le w_1\le .886565,& .113435&\le w_2\le .113436.
\end{split}                                                   \tag{2}
\]

Nevertheless the two reference cubics have no common interlacer, even
allowing endpoint equality. If r_1<r_2<r_3 are the roots of
h(y)=y^3-30y^2+180y-120, the two required upper-minus-lower gaps obey

\[
\begin{split}
 1.000637&\le r_2/v_2-r_1/v_1\le1.000638,\\
 -195.451440&\le r_3/v_2-r_2/v_1\le-195.451439<0.             \tag{3}
\end{split}
\]

Thus moment compression does not supply this particular finite
common-interlacing sufficient premise. This does not refute real-rootedness
of P_3 (already known from the literature compared in the assessment),
all-degree signs or RH. There is no degree-uniform assertion.

## Proof

**Standard inputs and applicability.** Walter Gautschi, *Orthogonal
Polynomials: Computation and Approximation*, OUP2004, first edition,
Theorems1.6/1.19/1.45/1.46, pp.1–3/7/21–23,
[primary book scan](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf),
give existence of orthogonal polynomials, distinct interior Gaussian
nodes, positive weights, and exactness through degree 2n-1. The measure
may have unbounded support; all finite moments and nondegenerate
polynomial norms suffice. See also NIST DLMF
[3.5.18](https://dlmf.nist.gov/3.5.E18) and
[3.5.20_1](https://dlmf.nist.gov/3.5.E20_1).
L019/L021 make nu a probability measure with every finite moment.
Every open subinterval of (0,infinity) has positive nu measure: its
square-root preimage has positive K integral. A nonzero polynomial
therefore has strictly positive squared norm. The cited theorems apply
at n=2, with nodes in (0,infinity). No compact truncation, moment
determinacy or Gaussian remainder theorem is used. These general
theorems are imported; only the explicit finite specialization is derived.
The ready gate is `drafts/literature/2026-11-05-theta-gauss-two-node-test.md`.

**Exact construction.** The variance D=t_2-t_1^2 is strictly positive:
otherwise the integral of (v-t_1)^2 would vanish, contrary to the
positive norm just verified. Solving the two orthogonality equations
for the monic node polynomial q(v)=v^2-A v+B gives

\[
 D=t_2-t_1^2,\quad A=(t_3-t_1t_2)/D,\quad B=A t_1-t_2,
 \qquad v_{1,2}=(A\mp\sqrt{A^2-4B})/2.                       \tag{4}
\]

Indeed t_2-A t_1+B=0 and t_3-A t_2+B t_1=0. Uniqueness and the
cited Gaussian theorem identify these roots as the two Gaussian nodes.
Their interpolatory weights are

\[
 w_1=(v_2-t_1)/(v_2-v_1),\qquad w_2=(t_1-v_1)/(v_2-v_1).      \tag{5}
\]

They have sum one and weighted first moment t_1. To check the precise
degree-three exactness rather than merely invoke a numerical rule,
put s_j=w_1v_1^j+w_2v_2^j. The exact node equations give
s_(j+2)=A s_(j+1)-B s_j. Hence s_2=A t_1-B=t_2 and
s_3=A t_2-B t_1=t_3, using the two orthogonality identities.
These finite substitutions check the specialization of the imported
theorem, without reproving its general existence or exactness result.

L795's cited DLMF Laguerre expansion gives exactly

\[
 F_{3,\sqrt v}(x)=1-3vx/2+v^2x^2/4-v^3x^3/120.
\]

Thus (1) follows coefficientwise from s_j=t_j, j=0,...,3, and
t_j=(2j)! gamma(j)/(j! gamma(0)). In particular the conversion factors
from gamma(j)/gamma(0) to t_j are 1,2,12,120, with t_0=1 exactly.
The coefficients are 1,-3R_1,3R_2,-R_3 for R_j=gamma(j)/gamma(0).
This is a polynomial identity for every complex x, not an approximate
quadrature or a global replacement of the theta law by an atomic law.
The orthogonal polynomial q is in the raw v variable; it is not P_2.

**Complete input evidence and outward arithmetic.** Run
`python3 scripts/theta-gauss/two_node_540.py`. Its full certificate is
`scripts/theta-gauss/two-node-certificate-540.json`. The source is
`scripts/central-jacobi/fixed-model-certificate-476.json`, SHA256
`2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e`.
The program verifies this digest, all three original hashes recorded by
`scripts/central-jacobi/audit-478/audit-report.json`, its PASS/no-failures
status, and nineteen selected provenance/Cauchy/coefficient/gamma
enclosure/positivity records. Complete selected gamma intervals and
audit records were inspected. This identifies audited actual input;
it does not independently attest the inherited backend or repeat the
theta evaluator proof. Full decimals are parsed as exact fractions.

Interval addition uses endpoint sums, multiplication takes extrema of
the four endpoint products, and division uses the reversed reciprocal
interval only after exclusion of zero. The certificate retains every
endpoint for gamma, t, D,A,B, the discriminant, nodes, weights,
denominators and scaled roots. It checks positive lower endpoints for
gamma(0), D, 2, v_1, v_2, v_2-v_1 and 120, as well as B and the
discriminant. Both t_1-v_1 and v_2-t_1 have positive lower bounds;
thus (5)'s weights are also directly certified positive.

For a positive rational discriminant box [l,u], set S=10^40 and bound
its square root by a/S and b/S, where
a=isqrt(floor(l S^2)), b=isqrt(floor(u S^2))+1. The program checks
(a/S)^2<=l and (b/S)^2>=u. The resulting node boxes enclose the exact
roots in (4), regardless of correlations between input moments.
The interval calculation is performed once; no rearrangement or fresh
theta precision is needed. Exact symbolic cleared orthogonality,
weight and recurrence residuals all vanish, and the factorial coefficient
conversion residuals are zero. The saved interval moment residuals
contain zero, but are explicitly not used as proof of exact equality;
that equality is established by (4)–(5) and the exact recurrence above.

**Root isolation and common-interlacer decision.** Since
h(y)=-120 F_(3,1)(y), the roots at node v are r_j/v. Starting brackets
[0,1], [7,8], [22,23] have opposite nonzero h endpoint signs.
Fifty exact rational bisections per bracket yield the full disjoint
positive brackets and signed endpoint values stored in the certificate.
The signs are respectively (-,+), (+,-), (-,+). Three disjoint sign
changes account for every root of this cubic and certify simplicity.
This is isolation for the finite specialization, not a reproof of a
general Laguerre real-zero theorem. Scaling the brackets by the positive
node boxes gives these outward bounds:

| node | first root | second root | third root |
| --- | --- | --- | --- |
| v_1 | [31.577576,31.577577] | [296.323708,296.323709] | [917.510229,917.510230] |
| v_2 | [3.471679,3.471680] | [32.578214,32.578215] | [100.872269,100.872270] |

For the source definition use A. Marcus, D. Spielman and N. Srivastava,
*Interlacing families II: Mixed characteristic polynomials and the
Kadison--Singer problem*, Ann. Math.182 (2015), 327–350,
[Definition3.1, pp.331–332; Lemma3.5, p.333](https://www.cs.yale.edu/homes/spielman/PAPERS/Marcus_Spielman_Srivastava_IFII.pdf).
A common quadratic interlacer needs its jth root simultaneously between
the jth and (j+1)st roots of each cubic, j=1,2, with weak inequalities.
Since v_1<v_2 and r_j>0, the intersection in slot j is nonempty exactly
when r_j/v_1<=r_(j+1)/v_2. The full rational gap boxes were inspected;
outward rounding gives (3). The first intersection exists, whereas
the second is strictly empty. Endpoint equality cannot repair it.

Both cubics have negative leading coefficients. Multiplying both by
-1 gives equal-degree positive-leading cubics, the convention in the
MSS sufficient criterion, and (1) remains a convex representation of
-P_3 with the same weights. Their roots and the failed intersection
are unchanged. Failure of common interlacing excludes that premise;
it does not exclude real-rootedness of this particular convex combination.
Known low-degree Jensen hyperbolicity is therefore fully compatible
with the result. L795's full-support stop and L796's Favard stop remain
comparisons, not premises in this construction.

The certificate contains all formulas, input/program/audit hashes,
interval endpoints, symbolic residuals, square checks, root signs,
actual/required gap bounds, the slot2 criterion failure, and an empty
verification-failure list. The separate step542 audit below validates
this finite result with the inherited contracts retained. No all-degree
mixed-positivity bridge is established.

### Independent finite audit — 5 November 2026, step542

Reused the separately approved SPECIALIZE assessment
`drafts/literature/2026-11-05-theta-gauss-two-node-audit.md` and its
primary theorem/proof coverage. Run
`python3 scripts/theta-gauss/audit_542.py`; complete evidence is
`scripts/theta-gauss/audit-certificate-542.json`. It reports PASS,
106 checks and no failures. It never imports or runs the step540
implementation and leaves all original inputs unchanged. No mathematical
defect or changed conclusion was found. This is independent finite
reproduction, not a new quadrature or Jensen sign theorem.

The checker verifies the three step540 provenance digests, the three
step478 original digests, all nineteen selected records, and the exact
four selected gamma intervals. It also rechecks those nineteen
conditions rather than trusting their recorded Boolean values: source
digests against both ancestors, full inherited evaluator equality with
the step433 replay, the prior PASS, radius1600 and retained analytic
error, the first four Cauchy coefficient-error additions, factorial
gamma conversions and positivity. These rational enclosures are checked
in full. The comparison retains, rather than independently verifies,
the transcendental evaluator and Decimal backend contracts.

Independent sparse polynomial arithmetic clears both orthogonality
equations, the weight sum and first moment, and the second/third moment
recurrences. It additionally verifies that the weighted node equations
imply each recurrence after clearing the weight denominator. The node
equations hold exactly by (4); this conditional algebra and s_0=1,
s_1=t_1 establish exactness. All conversion factors 1,2,12,120 and
all four cubic coefficients agree. Neither the fitted L791 model nor
an interval residual containing zero enters that argument. The raw-v
orthogonal polynomial remains distinct from Jensen P_2.

Independent tuple/Fraction operations reconstruct every stored raw
moment, D,A,B, discriminant, node, weight, mean-between-node box,
denominator, scaled root and both complete gap boxes, without relying
on the original interval class. All required lower endpoints are
positive. The stored square-root endpoints satisfy their exact rational
square inequalities. A separate integer binary search at scale10^42
(the original used isqrt at scale10^40) gives a tighter square-root
box and independent node/weight boxes within the originals.

All six stored h endpoint values were independently evaluated in Horner
form and agree exactly, with the stated alternating signs. Positivity,
disjointness and degree3 exhaust the roots and ensure simplicity.
Eight further bisections inside each valid bracket supply independent
scaled-root and gap boxes, contained in the originals. Both complete
rational gap boxes and their displayed outward bounds are checked:
the first is at least 1.000637, while the second is at most
-195.451439<0. Thus weak endpoint allowance cannot repair slot2.
Simultaneous negation gives positive-leading cubics and the same
convex representation of -P_3, so the MSS convention changes neither
root intersection nor conclusion. No universal convex-combination
claim is inferred from the particular average's known real roots.

This audit validates only the stated exact identity and finite
common-interlacing obstruction. It supplies no fresh theta evaluation,
new moment, degree extension, independently verified backend or
degree-uniform sufficient-sign bridge. L795's full-support obstruction
and L796/L772 remain contrasts, not additional mathematical premises;
L795's normalization is used as above. The canonical DAG is unchanged.

## Mathlib

Full matching coverage is unchecked. No claim is made about absence of
Gaussian quadrature, Laguerre or interlacing support in Mathlib. Python
integer/Fraction arithmetic and the inherited transcendental contracts
remain trusted components of this informal certificate.
