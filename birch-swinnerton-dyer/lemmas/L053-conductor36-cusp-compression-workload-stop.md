# L053 — complete fixed cusp-compression plan exceeds the execution limits

## Hypotheses

Use L050's minimal curve E: y^2=x^3+1, exact conductor 36 and
associated normalized weight-two newform with trivial character. Use
L038's saved complete integral relative presentation in
`scripts/conductor36-table/presentation.json`: all 72 original oriented
generators, with 144 endpoint occurrences. Its new structural instance
has complete production replay and still awaits separate critical audit.
Use audited L049's ordinary Gamma_0(36) transportation, full good-prime
Hecke closing and complete tail bound, and audited L051's independently
certified positive total minimal period and coefficients through 4860.

This assertion concerns exactly the finite plan in
`scripts/conductor36-table/compressed_plan.json`, with representatives
selected from the endpoint domain in increasing (denominator, absolute
numerator, numerator), infinity first, and ell=37 closing. It does not
assert optimality over other representatives, primes, identities or
evaluation strategies. The execution limits are maximum cutoff 4860,
total distinct primitive Fourier terms 1000000, and full normalized
two-sided Fourier-tail width at most 2^-38 for every original generator.

## Conclusion

The complete independent plan replay passes with zero certificate
failures. The 67 distinct endpoints are assigned to 12 inequivalent
classes. There are 67 endpoint transports and 418 full closing transports,
including 36 exactly vanishing translation corrections. There are 734
distinct required primitive evaluations, and

    maximum H = 48600 > 4860,
    sum of H = 7047552 > 1000000.

Every generator's conservative normalized two-sided tail width passes;
the maximum is

    452048812597313536 / 166638467572977606763020498997
      <= 1/274877906944 = 2^-38.

Thus this particular compressed schedule fails both execution workload
limits, despite complete coverage and valid tail planning. This is a
known-method finite negative result, not a new impossibility theorem or
an analytic enclosure failure. No new Fourier sums, rational generator
table, integer isolation, coefficient or BSD comparison is supplied.
Finite arithmetic errors and period uncertainty for a new analytic table
remain unexecuted. The separate BSD-186 audit recorded in L054 checks the twelve
representatives and all 67 endpoint assignments/geometric witnesses used
there. It does not audit this plan's ell=37 closing or workload assertion;
that separate critical audit remains pending.

## Proof

**Imports and specialization.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-conductor36-cusp-class-compression.md`.
Import Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition (1997), [Proposition 2.2.3 and its constructive proof,
pp.16--17, cumulative-list Implementation p.17](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=10).
For reduced homogeneous cusps (a,m),(b,n), equivalence is tested by
the existence of a unit u modulo 36 such that n=u m modulo 36 and
u b=a modulo gcd(m,36). The homogeneous infinity (1,0) is retained;
gcd(0,36)=36. The matrix witnesses below also check every assignment
directly. The cumulative list covers this complete finite endpoint
domain; no claim about a global cusp catalog is needed.

Import Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, version 23 March 2017, Section 5.1 (11), pp.11--12;
equation (2), Lemma 4 and proof, pp.6--7](https://arxiv.org/pdf/1608.06423v2#page=11),
with L049's audited orientations and complete closing, which uses
Cremona [(2.9.1), pp.31--32](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=25).
These identities are imported, not reproved. The finite specialization
is their composition on every saved endpoint, with independent matrix,
point, weight, period and workload reconstruction. No matching workload
bound was supplied by the sources; no novelty of the algorithms is claimed.

**Full domain, representatives and matrix witnesses.** The independent
structural verifier replays the original presentation, including all
source/saturated relations, transforms/inverses, coordinates and actual
oriented generating paths; it returns s=72, saturation rank 59, free
rank 13 and removed torsion order one. This is production replay, not
the pending critical audit or a theorem about generic software.
The compressed verifier reconstructs the 67 endpoints from these paths.
Its cumulative representatives, in order, are

    infinity, 0, -1/2, -1/3, 1/3, -1/4, -1/6, 1/6,
    -1/9, -1/12, 1/12, -1/18.

It independently enumerates all twelve units modulo 36 for every
equivalence test; for all 66 distinct representative pairs the full
residue witnesses show that no unit meets both conditions. Each endpoint
is assigned to exactly one representative. This includes actual infinity,
zero, nonunitary cusps and both original orientations.

For source s=a/m and target r=p/q, choose Bezout integers
a s_s-m t_s=1 and p s_r-q t_r=1. For infinity use (s_s,t_s)=(1,0).
The retained transport is the exact product

    gamma = [p t_r; q s_r] [1 t; 0 1] [s_s -t_s; -m a],
    C = q s_s - m s_r - t m q.

The producer solves C=0 modulo 36 and, when m q!=0, compares the two
adjacent solutions nearest C=0. Replay independently multiplies the
three matrices, checks both Bezout identities, determinant one, 36|C,
the homogeneous cusp equation, and both inverse products. It also checks
that the adjacent congruence choices have |C| no smaller. This is a
statement about the retained family, not other analytic algorithms.

For C!=0 take tau=-D/C+i/|C| and gamma tau=A/C+i/|C|.
For C=0 take tau=i. Replay uses the full rational Mobius formula to
check every image and both positive heights. Determinant one in the
C=0 branch forces A=D=+/-1, so gamma z=z+B/D with integral B/D.
The infinity-based Fourier primitive P is invariant under integer
translation. Thus those 36 corrections are exactly zero, with their
matrices, positive points and shifts still checked. Only these witnessed
zero corrections omit primitive evaluations. For each remaining point,
an explicit integer shift reduces its real coordinate to [-1/2,1/2).
Fourier periodicity identifies the point with that canonical key; no
other point or cusp identifications are used. Replay checks all 970
interior points and the complete use of all 734 distinct keys.

**Closing and all original endpoint compositions.** Use P(infinity)=0
and P(z)=sum a_n exp(2*pi*i*n*z)/n, so the oriented generator {a,b}
has value P(b)-P(a). For each endpoint r with representative s and
gamma(s)=r, the imported transportation gives

    P(r)=P(s)+P(gamma tau)-P(tau).

This also applies when s is infinity, by cuspidality and the stated
primitive normalization. Infinity itself is assigned to infinity with
an identity transport; it is not silently replaced by a finite endpoint.
All eleven finite representatives have denominators prime to 37.
The good prime 37 is 1 modulo 36; the independent exhaustive count on
E/F_37 is 48, so a_37=-10 and h=38-a_37=48>0. For every finite s retain
all 38 endpoints v=37s and v=(s+j)/37, 0<=j<37. Replay verifies each
fraction reduction, its equivalence, matrix and point witnesses. L049's
full closing gives

    P(s)=(sum_v(P(tau_v)-P(gamma_v tau_v)))/48.

The generator rows are reconstructed independently from each original
endpoint, with signs -1,+1, giving 144 endpoint compositions. Each row
retains every nonzero correction occurrence and its rational weight.
Signed equal-key coefficients are also reconstructed for future finite
evaluation; the conservative error sum uses the uncombined occurrences,
so caching and cancellation do not remove repeated error contributions.
The maximum sum W of absolute occurrence weights is exactly 7.
No relation agreement is used to infer an individual primitive value.

**Positive period, complete tails and workload.** Audited L051 gives
the total minimal period, since Delta=-432 and the real locus is
connected. The new verifier independently replays its Machin pi bounds,
all positive square-root branches and twelve outward AGM iterations
using (x+1)(x^2-x+1), real root -1, conjugate real part 1/2,
v^2=3/4 and d=-3/2. This gives the positive lower bound

    Omega_lower=166638467572977606763020498997 / 2^95.

The source formula is Cremona, corrected second edition (1997),
[Section 3.7 (3.7.1), pp.97--98, one-real-root case](https://johncremona.github.io/book/fulltext/chapter3.pdf),
with [DLMF 19.8.1--19.8.5](https://dlmf.nist.gov/19.8.i);
its applicability and component factor are already audited in L051.
The source certificate is SHA-256-bound, not substituted by a decimal
period. Positivity and the entire relevant finite period evidence are
replayed here; no other analytic sums in that certificate need repeating
to use its audited coefficient-segment conclusion.

For y>0 use L049's complete tail bound

    R_H(y)=2^(-floor(6 H y))/(6y),
    rho=2^-38 Omega_lower/(2*7)
       =166638467572977606763020498997
         /152446500380580431631591824129432158732288.

The first H with R_H(y)<=rho is selected for each distinct required
primitive. Replay recomputes R_H and verifies both this inequality and
failure at H-1 for all 734 points. For generator g with uncombined
occurrence weights w_j and point indices i_j, the full normalized
two-sided tail width is bounded by

    width_g = (2/Omega_lower) sum_j |w_j| R_(H_i_j)(y_i_j).

This controls both signs and both endpoints. Since sum |w_j|<=7,
the choice of rho gives width_g<=2^-38. Replay also reconstructs the
actual rational width of every row and the maximum in the conclusion.
This is exclusively the tail planning contribution; it is not a full
normalized analytic enclosure including new finite arithmetic and
period uncertainty.

The worst primitive has x=-1909/5832, y=1/5832, H=48600 and
R_H=243/281474976710656. One load-bearing transport sends -1/9 to
224/333 with

    gamma=[-3923 -411; -5832 -611],
    tau=-611/5832+i/5832,
    gamma tau=3923/5832+i/5832.

Its image reduces by the witnessed shift one to that worst primitive.
The full replay checks this record along with every other record, and
then sums H over all distinct keys to obtain 7047552. Neither a worst
record alone nor a bounded preview establishes these totals. The
certificate and full report are produced by

    python3 scripts/conductor36-table/build_compressed_plan.py
    python3 scripts/conductor36-table/verify_compressed_plan.py

The verifier imports no plan producer. Its report is
`scripts/conductor36-table/compressed_plan_verification.json`.
Every original endpoint, all 485 matrices/inverses, 970 interior points,
72 generator weight/width rows and 734 complete tail tests pass.
Both workload inequalities fail. As a discriminating check, the verifier
also recomputes every generator's same conservative tail expression with
H=4860 at *all* primitives. For original generator 58, {2/9,1/4}, this
expression is greater than 5, hence greater than 2^-38; its full rational
value is saved under `cutoff_obstruction` in the report. Since R_H is
nonincreasing in H, no allocation with every H<=4860 can pass this
particular absolute-occurrence tail convention on these fixed points.
This is failure of a certified upper-bound convention, not a lower bound
on true analytic error; sharper tails or a different evaluation scheme
are not excluded. The direct plan and ATTEMPTS/025--026
remain unchanged. L052's clearing integer 24 is a downstream input only:
it is not needed for this plan's arithmetic or its negative decision,
and no new integer recovery is performed. The CM curve still cannot
meet L027's non-CM hypothesis. No universal runtime bound, arbitrary-curve
normalization or main BSD gap is resolved by this finite test.

## Mathlib

Full matching coverage of this composed numerical plan and complete
certificate replay was not checked. L049 and L051 retain their supporting
source and Mathlib qualifications. No absence or software correctness
claim is inferred from unknown formal coverage.
