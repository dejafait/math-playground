# L134 — Signature-conditioned alteration with four protected supports

## Hypotheses

Use exactly L131's pinned actual labels: E=F_65537, F=F_(65537^28),
k=64, H=<19139> of order 1024, h_e=19139^e, and m>=1. Its six
two-sets U_ij, 60-set K={h_12,...,h_71}, private two-sets W_i and
supports S_i are unchanged. Put a=h_0, b=h_10, C=K union {a},
C'=K union {b}, and Y=H minus (K union {a,b}). Use q=137,
T={16,64,70,102,112,118,121}, Omega=(T times F_q) disjoint union
{d_0,d_1,d_2,d_3}, and B_f={(t,f(t)):t in T} for deg f<=2.
Fix L131's entire ordered left bijection sigma, including
sigma(16,1)=b. Write p=0 and r=Z-16. On the right retain d_0->a
and sample independently uniform bijections in the four membership
signature classes of (B_p,B_r) onto those of
(R3,R4)=(S3 minus C', S4 minus C'), after removing d_0,a.

## Conclusion

**Restricted local construction; separate critical audit accepted below.** There exists
one such right bijection sigma' and subfamilies of the two L030 ambient
families with

\[
 |A_L|=2552584,\qquad |A_R|\ge2346331>1532496,
\]

containing S1,S2 and S3,S4 respectively, such that every two distinct
full supports in their union intersect in at most 63 points. The right
ambient star through a is empty. All four protected supports remain
L131's actual-label common-center obstruction for pairwise distinct
polynomial m-tuples, for every m>=1.

This is a conditional-labeling existence statement, without an explicit
favorable map, prescribed marginal laws, universal occurrence, RS-list
realization or improvement of the 955–957 bracket. It strengthens the
local retention example; it does not resolve arbitrary-center safety.

## Proof

**Coverage and standard inputs.** The prior SPECIALIZE assessment is
[the signature-conditioned source comparison](../drafts/literature/2026-10-26-signature-randomized-planted-obstruction.md).
Use finite averaging and endpoint deletion as in Noga Alon and Joel H.
Spencer, *The Probabilistic Method*, third edition, Wiley (2008),
Theorem 3.2.1 and full proof, printed pp. 29–30 (PDF pp. 48–49 of
[the primary book](https://math.bme.hu/~gabor/oktatas/SztoM/AlonSpencer.ProbMethod3ed.pdf)).
The theorem's independence bound does not give our balanced retention
or protection; only its averaging/deletion principles are imported.
Part-respecting independent uniform injections are the framework of
Kamcev–Sudakov–Volec, *Bounded colorings of multipartite graphs and
hypergraphs*, [arXiv:1601.02271v2](https://arxiv.org/pdf/1601.02271v2),
Section 2, Theorem 2.2, p. 5, Appendix A, pp. 16–17. No local lemma or
negative-dependency conclusion is applied. The new work is the finite
conditional count below, a reproduction/specialization of these tools,
with no certified originality claim.

**Eligible left family and complete signature counts.** Take all left
supports C union sigma(B_f) with f(16)!=1. As in L130, evaluation at 16
has q^2 preimages of each value, so there are q^3-q^2=2552584 such
supports. They have form K union {a} union U_f with U_f a seven-subset
of Y; they all omit b. L131 shows that p,r are eligible and give S1,S2.

Index signatures as 00,01,10,11. The target partition of Y by R3,R4
has sizes s=(949,6,6,1), as does the domain after removing d_0.
The three remaining dummies lie in class 00. Thus the sample space
has 949!6!6!1! elements and is nonempty. For each eligible f let
m(f) record the four target-part occupancies of U_f. For each right g
let n(g) record the four domain-part occupancies of B_g. The following
are the complete histograms; zero entries denote absent types.

| Occupancy (00,01,10,11) | Eligible left count | Right count |
| --- | ---: | ---: |
| (0,0,6,1) | 0 | 1 |
| (0,6,0,1) | 0 | 1 |
| (3,2,2,0) | 3 | 0 |
| (4,0,2,1) | 4 | 0 |
| (4,0,3,0) | 8 | 0 |
| (4,1,1,1) | 16 | 30 |
| (4,1,2,0) | 50 | 60 |
| (4,2,0,1) | 4 | 0 |
| (4,2,1,0) | 49 | 60 |
| (4,3,0,0) | 8 | 0 |
| (5,0,1,1) | 524 | 786 |
| (5,0,2,0) | 1559 | 1980 |
| (5,1,0,1) | 524 | 786 |
| (5,1,1,0) | 4142 | 3840 |
| (5,2,0,0) | 1560 | 1980 |
| (6,0,0,1) | 17697 | 17165 |
| (6,0,1,0) | 104079 | 103812 |
| (6,1,0,0) | 104078 | 103812 |
| (7,0,0,0) | 2318279 | 2337040 |

Here is a fully specified finite computation of this table, with its
complete certificate and checks below. Write f=u+vZ+wZ^2 and loop
w,v,u independently through 0,...,136, including zero and lower-degree
polynomials. At each t compute y=(u+vt+wt^2) mod 137. The right class
is 2*[y=0]+[y=t-16]. On the left omit f when its value at 16 is 1;
otherwise the class is 2*[sigma(t,y) in R3]+[sigma(t,y) in R4], using
the audited complete L131 left map. Tally the seven classes, then the
resulting four-tuple. The exhaustive ranges cover each polynomial
exactly once. The table sums are 2552584 and 2571353.

Every listed left type satisfies m_10+m_11<=3 and m_01+m_11<=3.
Consequently every eligible left support meets each of S3,S4 in at
most 60+3=63 points; no deterministic left deletion is needed.
For p,r the left type is (3,2,2,0), and their full cross intersections
with S3,S4 are all 62. The two right types (0,0,6,1) and (0,6,0,1)
belong respectively to p and r. Their right supports are fixed S3,S4
for every map in this sample space, by signature preservation.

**Exact conditional image law.** Fix a right g with occupancy n. In
class i, its n_i distinct labels are sent to any prescribed n_i-subset
of the s_i targets by exactly n_i!(s_i-n_i)! bijections. Therefore its
image subset is uniform within that class. The four choices are
independent because the four restricted bijections are independently
sampled. This assertion concerns one g at a time, with no independence
assertion between different polynomials. For a left U_f of type m,
J_i=|U_f intersect sigma'(B_g) intersect class i| has law

\[
 \Pr(J_i=j)=\frac{\binom{m_i}{j}\binom{s_i-m_i}{n_i-j}}
                         {\binom{s_i}{n_i}}.
\]

Use binomial coefficients zero outside their valid ranges. All n_i are
within their part capacities. Convolve these four laws to obtain
P_mn(j)=Pr(sum_i J_i=j), j=0,...,7, and put
tau(m,n)=sum_{j=4}^7 P_mn(j). This retains the singleton, small classes
and the two planted polynomials, rather than using L130's unconditioned
seven-subset distribution.

Let l_m and r_n denote the displayed histograms. Both supports in a
cross pair have form K union {a} union U and K union {b} union V,
with U,V subsets of Y. They are distinct, since every left support
contains a and no right support does: the right inverse image of a is
the dummy d_0. Their intersection has size 60+|U intersect V|.
Thus a forbidden cross edge is precisely sum J_i>=4, including seven.
Linearity of expectation gives the exact identity

\[
 \mathbb E E=\sum_{m,n} l_m r_n\tau(m,n)
  =\frac{953535880348964195654027}{4237514312360044716},
 \qquad 225022<\mathbb E E<225023.
\]

No event independence is used in this sum. All 238 type pairs and
their full eight-entry probability laws are in the certificate.
An independent arithmetic comparison uses binomial moments:
E binom(J_i,k)=binom(m_i,k)binom(n_i,k)/binom(s_i,k).
Convolving these moments and using the pointwise identity, valid for
each integer J=0,...,7,

\[
 1_{J\ge4}=\sum_{k=4}^7(-1)^{k-4}\binom{k-1}{3}\binom Jk
\]

gives the same tail for every type pair. This is a finite verification
of the probability arithmetic; it is not a new general alteration
theorem. In particular the total expected degree of each of the two
protected right blocks is zero, also proved deterministically above.

**One map, one loss bound and simultaneous survival.** The integer
E on this finite nonempty space has some value at most its mean and
hence at most 225022. Fix such a map and delete every right support
incident to a forbidden edge. There are at most 225022 deleted right
vertices, even when edges share endpoints. Neither S3 nor S4 has any
incident edge, so neither is deleted. S1,S2 remain in the unchanged
left family; their right conflicts are included in this same E.
There is no combination of separately favorable events.

The retained right size is at least 2571353-225022=2346331. The left
size exceeds the target by 1020088, while the right size bound exceeds
it by 813835. The averaged loss is below the right budget 1038857.
There are no remaining cross conflicts. Within each side, L030's root
bound gives intersection at most 61+2=63 and distinct indexing, for
arbitrary bijections; deleting vertices preserves these conditions.
The right ambient star through a stays empty before and after deletion.
The protected actual supports are exactly L131's S1–S4, so its audited
common-center nonrealizability applies, with no relabeling of actual
field operations or new rank argument.

**Certificate and scope of verification.** Run
`python3 scripts/finite-support/signature_alteration.py`.
The full certificate is `scripts/finite-support/signature-alteration.json`.
It records the audited embedding input's SHA-256, every histogram
layer for each w, complete aggregate histograms and planted records,
all 238 full probability laws and independent moment tails, exact
expectation and budgets, and actual/required check values. All 18
checks pass with no failures. The complete aggregate histograms,
planted records, exact result and checks were inspected. Every law
normalizes exactly and every alternate tail agrees. The symbolic
partition, averaging and protection argument above supplies the
existence claim; no random sample or approximate numerical bound is
used. These are the construction-stage checks; the separate critical
replay and logical verdict are recorded next. The original production
certificate retains its historical pending-audit qualification unchanged.

**Separate critical audit (2026-10-27, step 522).** The invocation-start
SPECIALIZE [audit assessment](../drafts/literature/2026-10-26-l134-critical-audit-coverage.md)
matches the exact audit target. The audit accepts this restricted
construction without correcting its mathematical statement or counts.
Run `python3 scripts/finite-support/critical_audit_l134.py`; the complete
replay is `scripts/finite-support/l134-critical-audit.json`.
All 678 checks pass, with no failures. Both production inputs and the
accepted L131 audit remain byte-identical; their complete hashes are
recorded. No production module is imported and no rank is recomputed.

The replay generates H by multiplication recurrence, reconstructs all
actual supports and cores, and rebuilds both ordered signature maps.
Every one of their 1926 saved entries, including graph labels, unused
labels, dummies and exponents, agrees. The accepted L131 audit's hash
links to exactly this embedding. In particular the target and remaining
domain sizes are 949,6,6,1, the right inverse image of a is only d_0,
and both planted right graph images are precisely R3,R4. The ordered
right map is checked as an input prescription only; it is not asserted
to be the favorable randomized map. All four supports and their six
62-point intersections match the actual-label obstruction imported
from L131, including its extension-field and every-m qualifications.

Independent u,v,w loop order and Horner evaluation cover all 2571353
coefficient triples, including zero and lower degrees. Every complete
w-layer, loss histogram, aggregate occupancy count and planted record
agrees with the original certificate. Exactly 2552584 triples satisfy
f(16)!=1. Their maximum residual intersection with either R3 or R4
is three, so the deterministic loss is zero. The left and right
histograms have respectively 17 and 14 types. The full histogram and
planted identities are also checked against complete actual supports,
not only counts or a preview.

For every one of the 238 type pairs, the audit forms an integer
generating polynomial counting image subsets in the four parts and
divides by the product of their binomial sample-space sizes. All eight
entries agree with the saved law. Each entry is nonnegative, every law
normalizes, and all eight binomial moments agree with independent
distinguished-subset counts. The indicator identity is checked for
every J=0,...,7. All saved tails, alternate tails, contributions and
right conditional degrees agree; the two protected right degrees are
exactly zero. All scalar results, deletion budgets and 18 original
actual/required check records pass independent replay. This verifies
the complete probability table, rather than using the old internal
alternate-tail checks as a replacement for enumeration.

The logical audit also passes. For one fixed g, uniform class
bijection completions give the displayed hypergeometric law, with
independence only between classes. Linearity needs no independence
between g's or between edges. Since all eligible left blocks meet
R3,R4 in at most three labels, S3,S4 have zero degree for every map
in this same nonempty finite sample space. Some integer edge count is
at most the mean, hence at most 225022. Deleting its right endpoints
costs at most that count and preserves S3,S4; leaving the left side
unchanged preserves S1,S2. Thus protection and the size inequalities
hold for one map and one deletion, without intersecting separately
favorable events. The exact right bound is 2346331, exceeding 1532496
by 813835, and the left bound exceeds it by 1020088.

Every cross support remains distinct because the left contains a and
omits b, whereas the right contains b and omits a. Its intersection
is exactly 60 plus the residual intersection; no equal-support case
is dropped. On each side injectivity of the labeling and the root
bound for a nonzero auxiliary quadratic give distinct full supports
and intersection at most 61+2=63. Deletion preserves these conditions.
The use of L030 is its arbitrary-label packing, of L130 its conditional
alteration model, and of L131 its exact support/obstruction statement;
the existing DAG's direct inputs suffice. No marginal law, universal
obstruction occurrence, explicit favorable map or actual RS list is
deduced. This audit is local REPRODUCTION of assessed methods, with
no certified originality or radius improvement. Full and supporting
Mathlib coverage remain not checked.

## Mathlib

Full matching conditioned construction and supporting finite-field,
partition, hypergeometric, averaging and deletion coverage: **not
checked**. Unknown availability is not evidence of absence. Standard
probabilistic inputs are cited precisely above. No theorem beyond the
checked sources' methods, universal packing-to-RS implication or full
challenge solution is claimed.
