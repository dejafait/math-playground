# L059 — Exact finite reduction and seven-scalar filter for triangles

## Hypotheses

Use the full hypotheses and notation of audited L057 and its local
converse from audited L041. Thus F=F_(97^20), F_0=F_97, H is the fixed
order-sixteen subgroup, C=RS[F,H,8], and 1/4<=delta<5/16. The nine
labels in
\[
 A_0=\{a,b,y_1,y_2\},\quad A_1=\{a,c,z_1,z_2\},\quad
 A_2=\{b,c,w_1,w_2\}
\]
are distinct. Put P={a,b,c}. Retain c_x, the projected vectors and beta
scalars of L057 (5)–(6). All those label data lie in F_0.

The original finite gamma_i are distinct, lambda!=0, g=gamma_1-gamma_0,
rho=(gamma_2-gamma_0)/g not in {0,1}. The normalized pair weights
w=(p,q,r) initially range over F with p,q,r not in {0,1}. Let R be the
set of distinct additional original finite parameters recovered by L057
on nonbase four-subsets K. Zero recovered coefficients and both-zero
projected systems are retained. In particular R excludes the three base
parameters and requires E=rho-(1-rho)mu!=0.

For the finite construction below only, put G=F_0 minus {0,1} and
M_0=F_0 minus {0,-1}; both have 95 elements. For w in G^3 define M(w)
as follows, without imposing E:

* For an isolated support K, use its unique nonzero proportionality
  scalar from L057 (7), require mu in M_0, and impose every applicable
  equation (10) of L057.
* For a both-zero support K, test mu in M_0 against all three equations
  (10). Keep every successful mu. L057's pivot theorem implies at most
  one such mu for this K and w; this definition also retains inconsistent
  and zero-pivot cases by rejecting them rather than dividing by zero.
* The other projected cases contribute nothing. Take a union of scalar
  values over all nonbase K, rather than counting support witnesses.

Define D(w) by the same rule but using only K disjoint from P.
Thus D(w) is a subset of M(w), not a set of error supports.

## Conclusion

For rational gated weights w in G^3 and every allowed original chart,
the exact count is
\[
 |R|=\left|M(w)\setminus\{\rho/(1-\rho)\}\right|.       \tag{1}
\]
Every additional recovered mu is rational in this case, including every
both-zero lift. Nonprime rho deletes no element of M(w); any rho deletes
at most one. The original gamma_i and lambda are not asserted rational.

For every nine-label triangle and every w in G^3,
\[
 |M(w)|\le13,\qquad
 |M(w)|=13\ \Longrightarrow\ |D(w)|\ge7.              \tag{2}
\]
There is an explicit finite table generating D and hence the set
\[
             W_7=\{w\in G^3:|D(w)|\ge7\}.             \tag{3}
\]
For K disjoint from P, all three beta rows exist. For each isolated K
use just its scalar mu in M_0; for each both-zero K use all 95 mu in
M_0. Form the point
\[
 \Phi_K(\mu)=\left(
 \frac{1-(\beta_a^Z-\mu\beta_a^Y)/c_a}{1+\mu},\quad
 \frac{\beta_b^Y-\beta_b^Z/\mu}{c_b},\quad
 \frac{\beta_c^Z-\mu\beta_c^Y}{c_c}\right).             \tag{4}
\]
Retain the row (Phi_K(mu),mu,K) iff Phi_K(mu) belongs to G^3.
At each weight point, deduplicate mu before applying the seven-scalar
filter. The scalar fiber of this table at w is exactly D(w).

For each labeling, if I is the number of isolated disjoint-P supports
whose scalar is in M_0 and B the number of both-zero supports, the table
has at most I+95B rows before deduplication, where I+B<=binom(13,4)=715.
Consequently
\[
                 |W_7|\le\lfloor(I+95B)/7\rfloor.     \tag{5}
\]
The bound is only a table-size estimate, not a recovery-count bound.

The following two statements are equivalent:

(A) Every L057 gated fixed-H triangle pencil, over all extension-field
weights and all original finite charts, has |R|<=12.

(B) For every ordered assignment of nine distinct labels from H and
every w in its table W_7, the full scalar union M(w) has size at most 12.

Thus only the points surviving (3), followed by the full support test,
need to be checked for a violation. No reduction by label symmetry is
assumed. No table has been enumerated here, and neither (A) nor (B) is
proved. This is an exact reduction of the approved count target, with
a necessary simultaneous seven-scalar restriction, not a twelve bound.
Its separate critical audit found no mathematical defect. Other patterns, arbitrary extraction
and the global 11/q–16/q interval remain unresolved.

## Proof

### Exact rational-weight count with the original chart retained

Fix w in G^3. An isolated admitted scalar is rational by the nonzero
projected ratio in L057 (7). For a both-zero recovery all A_x,B_x of
L057 (9) are now rational. Its actual successful lift has a nonzero B
pivot, so mu=-A_x/B_x is rational. If all B vanish, L057 excludes an
entirely free lift and the system is inconsistent. This argument uses
rationality of w, not an assumed high count.

Conversely, a scalar in M(w) passes the complete projected and restored
systems of L057. In a both-zero case, satisfying all three restored
equations is exactly A_x+mu B_x=0. Since w is gated, the entirely free
case is impossible by L057, so this successful system also has a nonzero
pivot. Thus the table-style all-equations definition has introduced
neither a spurious zero-direction solution nor a free family of lifts.

The only remaining parameter gate is E!=0. If it holds, L057 (12)–(14)
give the actual parameter
\[
 T=\gamma_0+g\rho/E
\]
and an error satisfying all eight moments, with same-support input
failure. Its proof applies even when recovered weights vanish. The
change of variables is bijective on the eligible original finite
parameters. In particular distinct mu give distinct T: equal T gives
equal E because g*rho!=0, and then equal mu because 1-rho!=0.
The excluded mu=0,-1 give base parameters and the remaining base has
no finite mu. Hence taking a union over supports counts exactly R.
E=0 is equivalent to mu=rho/(1-rho), proving (1).

For mu in M_0, the same equation is equivalent to
\[
                     \rho=\mu/(1+\mu)\in F_0.         \tag{6}
\]
Thus nonprime rho retains every mu in M(w). This is an exact formula
for any given original chart; no given pencil is replaced by a rational
chart and original infinity is never counted as finite.

### Realizing the full finite set and obtaining the seven-scalar test

For each labeling and w in G^3, choose rho in F minus F_0, which exists
because the extension degree is twenty, and choose
gamma=(0,1,rho), lambda=1. These are admissible original data. L041's
local converse constructs actual words realizing the triple, with full
base weights, same-support badness, nonzero D and nonpersistent locators
since the triangle has empty triple intersection. Equation (6) and
L057 show that every element of M(w) is a distinct actual additional
finite bad parameter in this chart. L010 applied to these parameters
and the three bases gives |M(w)|+3<=16, proving the first part of (2).
This construction is conditional on w and does not assume that thirteen
elements exist.

Suppose now that |M(w)|=13. The constructed pencil has sixteen distinct
bad parameters. L010's weighted inequality forces every one to have
weight four, and its equality case gives distinct supports with each
coordinate used exactly four times. Each of a,b,c is in two base
supports, so the thirteen additional supports have altogether six
incidences with P. At most six of them can meet P: each meeting uses
at least one of those six incidences. At least seven therefore miss P.
Their scalars are distinct, and each belongs to D(w). This proves the
second part of (2). Fullness precedes this support count; no padded
four-set or duplicate support witness is counted in it.

### Complete table, including both-zero lifts

If K misses P, then m=3 in L057, and its projected test is scalar-valued.
If the two projected scalars are nonzero, there is precisely the one
ratio to test. If both vanish, the projected system imposes no restriction
on mu, so test every mu in M_0. Exactly-one-zero cases have no recovery.
For either retained projected case, all three lost coefficient equations
must hold. Solving them for p,q,r gives exactly (4), with nonzero
denominators c_a,c_b,c_c, mu and 1+mu. There is no other choice of w.
Conversely (4) satisfies all three equations. A point passing G^3 thus
supplies a complete lifted system; the preceding argument ensures a
valid nonzero pivot when both projected scalars vanish. No fourth-weight
nonvanishing test is imposed, as required for relaxed recovery.

It follows in both directions that the table's distinct scalar fiber
at w is D(w). There are 715 possible K disjoint from the three labels
P, and none is a base support. Isolated cases contribute at most one
row each; both-zero cases contribute at most 95. Discarding nongated
points only decreases this count. Every point of W_7 consumes at least
seven different (w,mu) pairs; different w give disjoint such pairs.
Their total is at most the number of table rows, proving (5).

This enumeration specification is finite and exact, but an actual
certificate would still have to establish all label and table coverage,
deduplicate scalars, and compute M(w) using *every* nonbase support for
each survivor. The table size and its seven threshold alone prove no
uniform exclusion.

### Threshold equivalence for arbitrary extension-field weights

Assume (B), and suppose an original gated pencil has more than twelve
distinct additional relaxed recoveries. L041/L057 give the three bases
and L010 bounds the total by sixteen, so there are exactly thirteen
additional parameters. Only now invoke audited L058: its hypotheses
are actual distinct original finite recoveries with every gate retained,
and it gives w in G^3. Equation (1) yields |M(w)|>=13, while (2) gives
|M(w)|<=13. Thus |M(w)|=13 and w belongs to W_7, contradicting (B).
No unproved rationality of the original chart was used.

Conversely, if (B) fails, some labeled w in W_7 has |M(w)|>12.
The constructed nonprime chart above realizes all M(w), so (1) gives
more than twelve actual distinct additional finite recoveries and (A)
fails. In fact |M(w)|=13 by (2), with full weights by L010. This proves
the equivalence; it does not provide a failing table entry.

### Source reuse, comparison and scope

This attempt uses the pre-existing EXPLORE assessment
`drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md`.
The chart argument reproduces the elementary mechanism already used in
L044 for a different support pattern. L044 is a comparison, not an input:
its tau=1 classification does not cover triangle both-zero lifts. Those
lifts are retained here using audited L057, and the new seven-scalar
filter couples its full restored equations to L010 equality incidence.
The assessed sources do not supply this finite maximum or assert that
the table has no thirteen-scalar entry. No originality is certified.

The recurrence and finite recovery are imported through L057, whose
precise standard input is Przemek Chojecki, *Shortening Bounds for
Reed–Solomon MCA*, live author TeX v9.2, July 17, 2026, DR2
(`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), lines 2785–2935 of the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
L057's specialization is R=8,t=4, multiplier x, eta_j=s_(j+1), with
distinct labels and nonzero multipliers. Those hypotheses are unchanged;
no recurrence or standard shortening theorem is reproved. The mutable
source is not certified identical to ePrint 2026/1463. L010, audited
L041 and audited L058 supply the other stated local facts. There is no
computational input or selected-label maximum in this proof.

### Separate critical audit (2026-10-10)

The audit used the pre-existing EXPLORE assessment
`drafts/literature/2026-10-10-triangle-finite-threshold-audit-scope.md`.
It checked the complete proof against L010's weighted inequality and
equality proof, L041's local converse and nonpersistence proof, L057's
symbolic recovery proof and L058's conditional descent proof. The
following checks establish correctness of this reduction within its
stated fixed-field scope; they do not evaluate any table.

1. **Successful rational pivots and exhaustive cases.** For isolated
   recovery, any nonzero coordinate of the projected y vector gives
   mu=z_j/y_j in F_0. For both-zero recovery, L057 proves m=3. At
   w in G^3 all six A_x,B_x are rational, and they cannot all vanish:
   that would put the full base syndrome on a disjoint-P four-set,
   contradicting weight-at-most-four uniqueness. If every B vanishes,
   a nonzero A makes the equations inconsistent. Otherwise any
   successful solution has mu=-A_x/B_x in F_0 for a nonzero pivot;
   the remaining equations still have to hold. Thus testing all
   equations at each rational mu neither omits nonprime solutions
   nor adds an entirely free lift. Exactly-one-zero and independent
   projected vectors supply no eligible finite parameter by L057.

2. **Exact original-chart correspondence.** From L057's actual pencil,
   mu=-rho(1-t)/((1-rho)t) with t=(T-gamma_0)/g. Eligible parameters
   have t different from 0,1,rho, so this is defined and avoids 0,-1.
   Conversely E!=0 gives t=rho/E, which is nonzero; t=1 would force
   mu=0, and t=rho would force mu=-1. Equality of two such T values
   forces equality of E and then mu. L057's complete lifted test
   gives all eight moments and same-support failure, even for zero
   fourth weights. Thus no additional gate on fourth weights is
   warranted. Taking the scalar union before counting identifies all
   duplicate support witnesses. E=0 removes just rho/(1-rho), which
   itself is neither 0 nor -1. The absent finite mu for gamma_0 and
   the excluded mu=0,-1 account for all three base parameters.

3. **Realizing M before invoking a bound.** For each fixed labeling
   and gated rational w, choose rho in F_(97^20) minus F_97,
   gamma=(0,1,rho) and lambda=1. This is possible within the stated
   field and makes every alpha_i nonzero. L041's local converse,
   without its separate equality premise, constructs the words and
   three full base errors. Its pointwise identity gives D(gamma_i)
   nonzero. For every x in H some base support misses x, so at that
   base parameter ell_x is nonzero. Thus every polynomial hypothesis
   of L010 holds. For rational mu!=-1, E=0 would give
   rho=mu/(1+mu) in F_97, a contradiction. Every scalar of M is
   therefore an actual distinct additional finite bad parameter.
   L010 gives |M|+3<=16. This is construction of a new admissible
   pencil for fixed weights, not a chart change imposed on an
   existing pencil.

4. **Fullness before the seven-scalar threshold.** If |M|=13, the
   constructed pencil has sixteen distinct bad parameters, including
   the bases. L010's weighted inequality excludes every lower-weight
   error, and its equality proof gives distinct full supports and
   coordinate degree four. The three shared labels each already
   occur twice at the bases, leaving exactly six shared-label
   incidences in the thirteen additional supports. At most six
   additional supports can meet P; at least seven miss P. Each has
   its own scalar by the chart bijection. Hence |D(w)|>=7 counts
   distinct scalars, not padded or repeated witnesses. No equality
   incidence is used at a smaller count.

5. **Both directions of the table construction.** For K disjoint
   from P the quotient has dimension one. Its only eligible cases
   are two nonzero scalars (one ratio) or two zero scalars (all 95
   test values before lifting); exactly-one-zero contributes none.
   All three restored equations are present. Their respective
   coefficients of p,q,r are -c_a(1+mu), -mu*c_b, c_c, each nonzero
   for mu in M_0. Solving gives exactly (4), with its displayed
   signs. Conversely substituting that point satisfies every
   restored equation; when it is gated, check 1 supplies any required
   both-zero pivot. This proves exact table fibers D(w), with zero
   fourth weights retained. There are binom(13,4)=715 possible K,
   all nonbase. Counting rows gives I+95B as an upper bound; scalar
   deduplication and the gate can only decrease it. Each distinct
   w in W_7 requires seven distinct (w,mu) pairs, and different
   w have disjoint pairs, proving (5) without interpreting it as
   a bound on |M(w)|.

6. **Arbitrary-weight threshold equivalence.** A violation of (A)
   supplies thirteen actual additional finite recoveries after the
   L010 upper bound, together with L041's three bases. These are
   precisely L058's hypotheses, including the original finite gate
   and permitted zero fourth weights before equality. Only then
   does L058 imply w in G^3. Formula (1) gives |M|>=13; check 3
   bounds it by thirteen; check 4 puts w in W_7, contradicting (B).
   Conversely, a failure of (B) has |M|=13 by check 3, and its
   constructed nonprime chart retains all thirteen, violating (A).
   Neither direction assumes rational original parameters, an
   isolated disjoint-P recovery, or absence of both-zero supports.

No mathematical defect was found and no statement or formula needed
repair. The proof's direct inputs remain L010, L041, L057 and L058;
L044 is a comparison only. The precise recurrence citation and unchanged
specialization above are reused through L057; no new external result,
standard-theorem reproof, computational certificate or sampled count
is an input. This audit validates a local reduction, not a discovery
beyond the assessed sources or a uniform twelve bound. The uncomputed
survivor test, other patterns, extraction and challenge definitions
remain open. The narrative assembly in PROOF.md is unchanged.

## Mathlib

The full finite threshold reduction and seven-scalar filter: **not
checked**. Supporting subfield closure, finite-set fibers and incidence
counting: **not checked** for this step. No absence claim, matching
Mathlib theorem or Lean verification is asserted.
