# L123 — Exact endpoint-pair maximum and deletion diagnostic

## Hypotheses

Use exactly L122 and C122a: E=F_65537, H the multiplicative subgroup of
order n=1024, and P the unordered two-element subsets of H. Map
{a,b} to (a+b,ab). Let Omega consist of ordered triples of pairwise
disjoint elements of P with collinear images. C122a gives
T=|Omega|=2298250371072. For distinct a,b in H let d(a,b) count members
of Omega containing both a and b among their six endpoints, whether in
the same pair object or in different pair objects. A core K below is any
61-element subset of H; no selected support family or received center
is assumed.

## Conclusion

The exact finite computation described and checked below gives

\[
\max_{\{a,b\}\subset H}d(a,b)=67798380.
\]

Equality holds exactly when b=-a. For {1,-1}, the same-pair and
different-pair contributions are 15270744 and 52527636, respectively.
For every 61-element K, the number U(K) of members of Omega avoiding K
satisfies the diagnostic bounds

\[
1476805414224\ \le U(K)\le\ 1600876449624.                 \tag{1}
\]

The upper bound improves the singleton-incidence upper bound
2161342878264 by 560466428640. It is not claimed sharp. This is a bound
on all configurations avoiding a core, not a supersaturation or size
bound for selected support families. It does not improve arbitrary-center
67/68 safety or the 955–957 bracket. The separate 2026-10-25 critical
audit accepts this finite computational result under unchanged hypotheses;
this is not a complete challenge candidate.

## Proof

**Scope and sources.** The prior EXPLORE assessment
`drafts/literature/2026-10-25-endpoint-pair-incidence-count.md` covers
the endpoint-conditioned enumeration and its deletion diagnostic.
L122 supplies the matching-line reduction and histogram transport;
C122a supplies the audited full-H histograms and T. They do not already
give conditioned counts. The proof below supplies only that finite
specialization. The Bonferroni inequality used below is a standard
import, not a new incidence theorem. POTENTIALLY_NEW classification
means only that the recorded bounded comparison found no matching
endpoint-pair result; it is not a claim of mathematical originality.

**Coverage of all endpoint pairs.** Multiplication by h in H permutes
unordered pair objects and sends (s,t) to (hs,h^2 t), an invertible
linear map of the affine plane. It preserves collinearity, pairwise
disjointness and the order of the three pair objects. Consequently
d(a,b)=d(1,b/a). Every b/a lies in H minus {1}, and every such ratio
occurs. It suffices to enumerate all 1023 ratios, without assuming
transitivity on unordered endpoint pairs. Scaling by b^-1 also gives
d(1,b)=d(1,b^-1), separately for each endpoint-placement case.
The enumeration keeps both inverse ratios; it never divides by their
orbit sizes. In particular -1 is retained despite being its own inverse.
Once uniqueness of the maximizing ratio -1 is checked, this proves
exactly the stated antipodal equality characterization.

**Same-pair count.** Fix a=1. For x in H minus {1}, write A={1,x},
s_A=1+x and t_A=x in E. On every eligible line through A, L122 proves
that its r pair objects form a matching. Triples containing A on this
line number 3(r-1)(r-2): choose A's position, then an ordered choice of
two other pair objects. Every such triple determines a unique line.
Thus its sum over all eligible lines through A is the same-pair count
S(x). Enumerate the vertical line s=s_A and all q nonvertical slopes u
with intercept v=t_A-u*s_A. The line is a star exactly when
v=-u^2, equivalently (u-1)(u-x)=0; omit precisely u=1,x.
The horizontal line u=0 is retained. Use zero contribution when r<3.
This covers all lines, including s_A=0 at x=-1.

**Different-pair count.** For every A={1,x}, enumerate every unordered
B={b,c} disjoint from A. Their distinct sum/product images determine
one line ell. By L122 it cannot be a star. If its occupancy is r, every
one of its r-2 other pair objects is disjoint from both A and B. Together
with the six orders of these three pair objects this contributes
6(r-2) to the different-pair count D(b) and also to D(c).

To check multiplicity, fix a member of Omega containing 1 and b in
different pair objects. Its unique pair containing 1 is A, its unique
pair containing b is B, and its third pair is one of the r-2 choices.
Thus it is counted exactly once for endpoint b with the correct order;
the update to the other endpoint c of B is a different endpoint query,
not a duplicate for b. Conversely every update constructs precisely
such triples. Summing all these updates yields D(b), and
d(1,b)=S(b)+D(b). A triple with 1 and b in the same object contributes
only through S(b); hence the two cases are disjoint and exhaustive.

The unique line is vertical if s_B=s_A. Otherwise
u=(t_B-t_A)/(s_B-s_A), v=t_A-u*s_A. Equal sums are tested before
inversion, so vertical and antipodal cases are not lost.

**Occupancy lookup and finite certification.** Reuse C122a's complete
histograms, in order vertical, horizontal and the 64 nonzero-slope
representatives. For u!=0, write uniquely u=r_0*h with r_0 the stored
coset representative and h in H. L122 gives
R_(u,v)=R_(r_0,v*h^-2). Horizontal and vertical lookups are direct.
The program constructs all 65536 slope transports, checks that their
cosets partition E*, and excludes stars before using matching counts.
Every actual same-pair occupancy is checked between 1 and 512, and
every disjoint-two-pair occupancy between 2 and 512.

Reproduction command, from the notebook:

```text
python3 scripts/finite-support/endpoint_pair_count.py
```

The driver compiles `scripts/finite-support/endpoint_pair_count.c` using
`cc -O3 -std=c11 -Wall -Wextra`. Assertions remain enabled. Its complete
actual-field output is `scripts/finite-support/endpoint-pair-counts.txt`,
one row for each nonidentity ratio, containing that ratio, S and D.
The driver saves every count, check, small-field comparison, maximum,
attainer and diagnostic in `scripts/finite-support/endpoint-pair-count.json`.
The input H and representatives are saved in `endpoint-pair-input.txt`
in the same directory. The manifest records the C and Python source
hashes. The reused histogram bytes must have the audited SHA-256
`4f8161677371fe052b12ead70436b92c0ceb508883a5bd658a593086043aa681`.
The driver independently verifies H as all nonzero roots of X^1024=1
and verifies the complete coset partition. It verifies that the output
keys are exactly H minus {1}. Maximum and equality set are computed
over this complete output, not a sample or a preview. The result is
67798380, with the unique normalized attainer 65536.

There are 535822848 pair-loop trials, of which 533730813 have B
disjoint from A. There are at most 67045374 same-pair line queries
including the two omitted stars per A. These bounds established a
tractable finite algorithm before execution. No six-tuple enumeration
in the actual field is required. The histogram payload is 17301768
bytes; other arrays and interpreter overhead are additional.

All modular products are widened before multiplication. Signed modular
intermediates have magnitude at most 2^32 and are evaluated in int64;
uint64 is used for nonnegative products and accumulated counts. The
same-pair accumulator for one x is at most
(q+1)*3*511*510<2^36. Even the sum of every different-pair update is
at most 2*533730813*6*510<2^42, so each accumulator is safely below
2^64. The inverse recurrence inv[a]=q-(q/a)*inv[q mod a] mod q,
starting from inv[1]=1, is valid for 1<a<q because q is prime:
q mod a=q-floor(q/a)*a gives the identity after inversion modulo q.
No inverse of zero is used. Python diagnostic arithmetic uses integers
of arbitrary precision. The binary histograms are decoded explicitly
as little-endian uint32, independently of host byte order.

**Independent checks and their limits.** For (q,n)=(17,8),(17,16),
(41,8),(97,16), the driver constructs the histograms directly and runs
the compiled algorithm. Independently it enumerates every unordered
triple of pair objects, tests all six endpoints for distinctness and
the collinearity determinant, then adds its six orders to the relevant
same/different endpoint counts. Every count in each small instance
agrees exactly; full comparison dictionaries are retained. These checks
test the placement factors and exceptional cases; they do not replace
the general counting argument or the actual-field complete output.

For the actual field, multiplication acts transitively on single
endpoints. Each configuration has six endpoints, so the single-endpoint
count is the integer s=6T/n=13466310768. Each configuration containing
1 contributes once to sum_x S(x), four times to sum_x D(x), and five
times to sum_x d(1,x). Hence the required exact checks are

\[
\sum S=13466310768,\quad \sum D=53865243072,\quad
\sum d(1,x)=67331553840.
\]

Also summing d over unordered endpoint pairs gives 15T; by scaling this
is (n/2)*sum_x d(1,x)=34473755566080. This last expression is obtained
by halving the sum over ordered distinct endpoints, not by assuming
free unordered-pair orbits. Every equality and inverse-ratio symmetry
passes, with no reported failures. These are diagnostics; the proof
of exact enumeration is the placement and line argument above. A
separate independent critical audit of the new program and certificate
is recorded below; these diagnostics alone do not establish the result.

**Deletion use and direction.** Import the standard Bonferroni
inequalities, as stated in *Probability inequalities*, Section 15.1,
Proposition 15.2, printed pp.196–197,
[UConn-hosted chapter](https://probability.oer.math.uconn.edu/wp-content/uploads/sites/2187/2020/08/ch15M.pdf),
inspected in the prior assessment on 2026-10-25. The finite-event theorem
requires no independence. Its second truncation bounds a union below
by the sum of singleton probabilities minus the sum of pair intersections;
its first truncation bounds the union above by the singleton sum.

Apply it to the uniform probability space Omega (T>0 by C122a), with
event E_a that endpoint a occurs, for a in K. Multiply by T. Every
|E_a| is s and every |E_a intersect E_b| is at most M=67798380. Thus

\[
61s-\binom{61}{2}M\le |\bigcup_{a\in K}E_a|\le61s,
\qquad T-61s\le U(K)\le T-61s+1830M.
\]

Substitution gives (1). Dropping pair intersections from the lower
bound on the union would be invalid: T-61s is a *lower* survivor bound.
For a meaningful upper-bound comparison not using pair codegrees, each
configuration meets K in at most six endpoints. Therefore
61s=sum_omega |endpoints(omega) intersect K| <= 6|union E_a|,
giving U(K)<=T-ceil(61s/6)=2161342878264. The new upper bound is
strictly smaller by the amount claimed. It also improves the weaker
one-endpoint upper bound T-s=2284784060304. None of these bounds implies
that an arbitrary selected support family must contain a forbidden
configuration, or that the bound (1) is attained by a core. Those
transfer and sharpness questions remain independent gaps.

**Separate critical audit, 2026-10-25.** The prior SPECIALIZE assessment
`drafts/literature/2026-10-25-l123-critical-audit-coverage.md` authorizes
verification of this unchanged target, classified REPRODUCTION. Both
complete endpoint programs and the mathematical placement argument were
reviewed. Injectivity of the pair image makes the line through two
different objects unique. L122 makes each nonstar line a matching;
a vertical line is also a matching. Thus all r-2 third objects in the
different-pair update are admissible, and no extra endpoint exclusion
is missing. For each queried endpoint the unique pair containing 1 and
the unique distinct pair containing that endpoint determine the update.
The factor six counts orders, whereas the same-pair factor fixes one
of three positions before ordering the other two objects. There is no
duplicate across these two cases or across different lines.

The only star slopes through {1,x} are 1 and x, since their intercept
condition is (u-1)(u-x)=0. Horizontal slope zero is eligible. Equal sums
are handled before taking an inverse, retaining the antipodal vertical
line. For u=r*h the lookup uses v*h^(-2), the inverse of L122's
transport; each nonzero slope has exactly one such representation with
the saved representatives. Scaling and endpoint interchange give all
1023 ratios and inverse symmetry, without dividing by orbit size. The
self-inverse ratio -1 is included, so its unique normalized maximum
implies precisely the antipodal equality set.

In C, multiplication is widened to uint64 or int64 before reduction.
The sums H[i]+H[j] are at most 131072 and n(n-1)=1047552, within uint32.
Signed products have magnitude at most 4294967296, within int64.
The inverse recurrence uses only previous nonzero entries because q is
prime; the audit checks a*inv[a]=1 for all 65536 nonzero residues. Row
indices cover all slopes once. Histogram entries are decoded from exactly
four bytes in little-endian order, and the input must end after all bins.
The complete audited histogram bounds the vertical occupancies; the new
audit additionally checks all same-pair vertical queries explicitly.
All nonvertical same-pair and all different-pair occupancies are checked
by C assertions before unsigned subtraction. The same-pair accumulator
is bounded by 51239574540 < 2^36, and the sum of all different-pair
updates by 3266432575560 < 2^42. Both fit uint64. No floating-point
arithmetic is used in enumeration or deletion comparisons.

Run `python3 scripts/finite-support/critical_audit_l123.py`. The complete
certificate is `scripts/finite-support/l123-critical-audit.json`. It
reconstructs and compares every field of the original manifest, including
the entire 1023-row count dictionary, all 18 production checks, all four
small-instance comparison dictionaries, hashes, maximum, equality set,
diagnostics and completion/failure fields. Text row lengths, ordering,
distinctness and exact nonidentity-ratio coverage are checked before
building dictionaries, so duplicate output rows cannot be hidden.
Input subgroup and coset representatives agree with independently
reconstructed powers/roots and all 64 cosets. The full histogram hash
and manifest match C122a's accepted audit, including its row ordering;
the established histogram count is reused rather than re-audited here.

For each small field the audit regenerates every histogram bin from
ordered unequal endpoints using shifted products, tests evenness and
halves. Every byte equals the original artifact. Its independent brute
force enumerates every six-element subset and all 15 perfect matchings,
then tests the expanded three-by-three collinearity determinant. Each
passing matching contributes six orders; its unique partner of 1
determines the same/different classification. This differs from the
production driver's triple-of-pairs brute force and does not use line
occupancies to decide admissibility. All small S and D entries agree.

The audit compiles the unchanged C source with assertions enabled,
`-O2 -std=c11 -Wall -Wextra -fsanitize=undefined
-fno-sanitize-recover=all`, and reruns all five instances to separate
`*-audit-replay-counts.txt` files. Every count matches; all runs exit
successfully with no sanitizer diagnostics. This actual-field replay
uses the same reviewed enumeration, not an independent actual-field
algorithm. Its agreement supplements, rather than replaces, the
placement/transport proof. All 207 audit checks pass, without failures;
the original programs, manifests, inputs, outputs and histograms retain
their pre-audit hashes. The evidence is an executable finite-arithmetic
certificate, not a formal proof-assistant verification.

Finally, the audit checks the exact singleton, placement sums, unordered
pair total and every number in (1) and both baseline comparisons. Omega
is nonempty by C122a and the endpoint events are finite; the cited
Bonferroni theorem needs no independence. The second union truncation
is a lower bound, so its complement is the stated upper survivor bound.
Replacing each intersection by its maximum preserves that upper-bound
direction. The first truncation gives the lower survivor bound. The
incidence-only upper comparison follows from at most six core hits per
configuration. Neither maximum attainment at an antipodal pair nor
these inequalities asserts attainment by a 61-point core. Acceptance
establishes only the fixed-field endpoint maximum and uniform diagnostic;
exact core maxima, selected-family transfer and RS safety remain open.

## Mathlib

Full matching conditioned-count theorem, implementation certificate and
61-point numerical bound: **not checked** in Mathlib. Supporting finite
field, finite counting and Bonferroni coverage: **not checked**. The
precisely cited Bonferroni theorem is an imported standard result; no
matching Mathlib theorem or novelty claim is inferred from these checks.
