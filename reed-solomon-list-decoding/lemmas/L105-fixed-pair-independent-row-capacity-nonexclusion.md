# L105 — Independent scalar contraction rows do not exclude L098's pairs

## Hypotheses

Use n=1024,w=68,v=956,d=10 and the exact pair coordinates of L098:

    T=65537^28/2^128, N=floor(T)+1,
    g_i=binomial(68,i)binomial(956,i),
    U=binomial(1024,64)/binomial(68,64), M=(U+1)/2,
    alpha=(N-1)/(M-1),
    p_0=1, p_1=...=p_4=0,
    p_i=a_i/(2g_i) for 5<=i<=68,
    c_i=alpha*p_i+(1-alpha)*1_(i=0).

Here a_i is exactly L021's rational primal vector, with L022's factor
2 normalization and L023's original scalar-orbit conventions. No pair
is changed, and no L098 triple value is frozen. In particular c_0=1,
c_1=...=c_4=0, all other c_i>0, and sum_i g_i*c_i=N.

Keep every original actual orbit (i,j,t,s) with

    0<=i,j<=68,
    max(0,i+j-68)<=t<=min(i,j),
    max(0,i+j-956)<=s<=min(i,j), h=i+j-t-s.

There are 1,500,625 such ordered entries. Retain repetitions and
forbidden-distance entries. In the test below each original entry is
independent of all other entries, even when the source would identify
their variables. Different contraction rows also use independent copies.
All scalar inequalities induced by every presentation of that entry
are retained. PSD, shared-variable equalities and joint contractions
are omitted. This is a necessary relaxation, not an exact projection
of the source feasible region.

## Conclusion

Every one of the 69 L098 contractions has an attainable right-hand side
in this independent-entry scalar relaxation. Rows i=0,...,4 collapse
to equality. For every i=5,...,68 its attainable interval [L_i,U_i]
satisfies

    L_i=2c_i < N*c_i < U_i.

The minimum U_i/(N*c_i) over these 64 rows occurs at i=5 and lies in

    [95274477053795357/10^6, 95274477053795358/10^6).

Thus no individual contraction's scalar capacity excludes these fixed
pairs. This ends this diagnostic. It gives no simultaneous assignment
of the shared triples, PSD feasibility, actual packing, RS list, uniform
bound over other pairs or improvement of the 955–957 bracket.
This is a known-method finite specialization, classified REPRODUCTION;
no discovery beyond the sources checked is claimed. Separate critical
proof review remains pending.

## Proof

**Imported scalar and cardinality inputs.** Schrijver, *New code upper
bounds from the Terwilliger algebra and semidefinite programming*,
IEEE TIT 51 (2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(67), printed p.7, gives the source orbit normalization,
permutation identities, distance zeros and scalar rows. Kim–Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), (31)–(35),
pp.8–9, cross-checks these formulas. These are the primary passages
already inspected in foundations/04. They apply to nonempty binary
constant-weight codes, with 0<10<2*68<=1024. Only actual orbits are
used, and Schrijver (61)'s qualified complement prefactor is unused.
No PSD decomposition theorem is reproved or used here.

L098 imports and specializes the cardinality input from Raghavendra–Tan,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
Definitions 3.1,3.3 p.7 and the conditional-cardinality display pp.8–9,
with Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Proposition 1.1 and its full indicator proof p.2, Section 1.2 p.3.
The qualifications are recorded in foundations/12,13: constant weight
is retained in Polak's conclusion, and consistent local distributions
need not have a global representing measure. L098's separately audited
homogeneous conversion supplies

    sum_(j,t,s) D(i,j,t,s)*y_ij^(t,s)=N*c_i,
    D=binomial(i,t)binomial(68-i,j-t)
       binomial(i,s)binomial(956-i,j-s).

The two repeated third words for i>0 each have D=1 and y=c_i.
Zero pair probabilities cause no division. L098 also supplies the
necessary exact-N support reduction for arbitrary-center tuple lists
at 68 agreements, for every interleaving width m>=1, without averaging
actual RS labels. That necessity, not its converse, is the downstream
application here.

**Scalar interval and why it is a relaxation.** Write u=t-s. For any
permutation (a,b,c) of (i,j,h), its presentation is

    t'=(a+b-c+u)/2, s'=(a+b-c-u)/2.

These are integral actual-orbit indices: they arise by permuting the
three words. The invariant u is also explicit from the eight membership
regions below. Source permutation equalities identify the presented
values of an actual feasible assignment. Consequently all the source
rows y>=0, y<=c_a and 1+y-c_a-c_b>=0 apply to its single value. Their
intersection is exactly

    ell=max(0,c_i+c_j-1,c_i+c_h-1,c_j+c_h-1),
    upper=min(c_i,c_j,c_h).

All ordered permutations are included even when distances coincide.
If a distance belongs to {1,2,3,4}, fix the entry to zero and check
ell<=0<=upper. Otherwise, if a distance is zero, actual admissibility
forces the other two distances to be b,b; fix the entry to c_b and
check ell<=c_b<=upper. This includes the all-equal triple. In every
other case use the full interval [ell,upper]. An empty interval would
already be an obstruction; every interval here is checked nonempty.

Apply these derived necessary bounds separately to every original
entry and then remove the equalities coupling entries, including
couplings within a row and across rows. Every original feasible point
still satisfies all retained bounds, so this enlarges its feasible set.
Although interval endpoints depend only on the three distances at
these fixed pairs, no equality of entry variables based on distances
is imposed. The complete t,s lift is retained.

For a fixed row all D are positive integers. If [ell_e,u_e] is the final
interval at entry e, its minimum and maximum sums are therefore

    L_i=sum_e D_e*ell_e, U_i=sum_e D_e*u_e.

Both are attained independently by choosing all endpoints. Moreover
every value R in [L_i,U_i] is attained: if U_i>L_i choose
lambda=(R-L_i)/(U_i-L_i) and set each entry to
ell_e+lambda*(u_e-ell_e). If U_i=L_i, every permitted sum is that value.
This construction is per row only and supplies no shared-triple
assignment. These elementary endpoint rules are the needed finite
specialization; no interval-programming theorem or optimization solver
is being reproved or invoked.

**Full finite evidence.** Reproduce from this notebook:

    python3 scripts/finite-support/fixed-pair-row-capacity-construct.py
    python3 scripts/finite-support/fixed-pair-row-capacity-verify.py
    python3 scripts/finite-support/fixed-pair-row-capacity-summarize.py

The constructor recovers all 64 rational a_i from L021's canonical
`scripts/finite-support/delsarte-lp-results.json`, applies exactly the
above definitions and checks the endpoint objective M, 0<alpha<1,
c_0, forbidden pairs and objective N. With a positive common denominator
q it saves all integers P_i=q*c_i. For each original entry all six
presentations are checked before its endpoints are summed.

The complete constructor certificate is
`scripts/finite-support/fixed-pair-row-capacity-results.json`.
It saves exact input hashes, N,M,alpha, original pairs, q,P, all 69
endpoint sums and both comparison slacks. For each of the 4761 ordered
(i,j) entries it saves the complete t,s ranges, both D factor arrays and
the endpoint descriptors, coefficient sums and entry multiplicities
for every h. A descriptor specifies exactly zero, P_b or P_a+P_b-q.
For any original (i,j,t,s), h=i+j-t-s selects its unique record; multiplying
the two saved factors gives its individual D. This is a lossless original
entry lift. Factoring the endpoint sum does not identify variables.

The independent verifier imports no constructor routines. It reconstructs
the pairs from the canonical rational vector. For every orbit it builds
the following eight actual membership-region sizes, with bit positions
A,B,Z and array positions 0,...,7:

    (v-i-j+s, t, i-s, j-t, j-s, i-t, s, w-i-j+t).

They are nonnegative and sum to 1024. For each of the six orders it
reconstructs the half-distances, t',s' and u from these atoms, intersects
the presented scalar rows directly, applies the Boolean and forbidden
equalities, and compares the exact endpoints with the saved descriptors.
Thus no distance-only variable identification or unverified endpoint
formula is relied on for the finite computation.

It independently reconstructs source multinomials

    A_t=68!/[t!(i-t)!(j-t)!(68-i-j+t)!],
    B_s=956!/[s!(i-s)!(j-s)!(956-i-j+s)!]

and checks every integer product A_t*B_s/g_i against the saved D.
These ratios equal the four-region coefficient by direct factorial
cancellation. It sums D*ell and D*upper separately at every original
entry, rather than accepting the constructor's h aggregates. Each
shell coefficient sum equals g_j, each row sums to binomial(1024,68)
third supports, and all saved h multiplicities agree. All 205 repeated
entries and 10232 forbidden entries are retained and checked; for i>0
the repeated third words are exactly (j,t,s)=(0,0,0),(i,i,i), with
coefficient one in each case.

Full independent evidence is
`scripts/finite-support/fixed-pair-row-capacity-verification.json`.
All 69 endpoint sums, all comparisons and every interval pass; no
verification failures occur. The verifier performs over 30 million
exact comparisons. Construction and verification together visit
18,007,500 presentations, below the 20,000,000 visit cap; coefficient
work is performed during the first presentation visit of each orbit.
This covers 1,500,625 original entries per pass, below the 1,501,000
entry cap, with 69 rows. Measured combined elapsed time is 78.03 seconds
(cap 900), peak live memory 151797760 bytes (cap 1 GiB), combined main
certificates 23174523 bytes (cap 256 MiB), and maximum relevant integer
component length 1023 bits (cap 262144). The small exact summary checks
all 69 saved rows once more, without revisiting original entries, and
records the exact minimum ratio in
`scripts/finite-support/fixed-pair-row-capacity-summary.json`.

The first five rows have L_i=N*c_i=U_i. For i>=5 the verified lower
endpoint is exactly 2c_i, and N>2. Every verified upper endpoint is
strictly above N*c_i; the minimum ratio is the one stated in the
conclusion. The per-row interpolation above now proves the claimed
independent-row attainment. This supplies new finite evidence against
this exclusion mechanism, not against safety of the RS code or against
the still undecided shared-variable fixed-pair scalar system.

## Mathlib

Full matching fixed-pair row-capacity verdict or Schrijver/cardinality
specialization: not checked. Supporting finite interval sums, Boolean
counting and exact rational arithmetic coverage: not checked. The
primary inputs are imported with the above precise qualifications;
unknown Mathlib coverage is not evidence of absence.
