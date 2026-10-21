# L050 — Two six-coordinate lifts force a disjoint recovery at twelve

## Hypotheses

Use the complete gated tau=1 setup of L043 over F=F_(97^20), with H
of order sixteen in F_97, k=8 and 1/4<=delta<5/16. In particular,

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3},
    B={h,d,y_1,y_2,z_1,z_2}, O=H minus B,
    K_*={y_1,y_2,z_1,z_2}.

All nine labels are distinct. Retain arbitrary extension-field weights,
distinct original finite gamma_i, lambda!=0 and
p*q*(1-p-q)*r*(1-r)!=0. Let R be the set of distinct original finite
parameters admitted by L043 (4)–(7), with witnesses other than
A_0,A_1,A_2,K_*. Keep all quotient cases, mu!=0,-1, E(mu)!=0 and the
exclusion of all three gamma_i. Do not assume the fourth-weight gate (9).

Suppose two distinct parameters theta,theta' in R have witnesses

    K={d} union S, K'={d} union S', S,S' subsets of O, |S|=|S'|=3.

Audited L048–L049 give a label s in {w_1,w_2,w_3} such that

    S={s} union P, S'={s} union P', W_0={w_1,w_2,w_3} minus {s}

are described by three pairwise disjoint two-sets P,P',W_0, all outside
B and avoiding s. Define

    B'={d,s} union P union P', V=P union P',
    T_0=H minus (B union B').

Thus |B'|=6, B intersect B'={d}, |T_0|=5, and W_0 is contained in
T_0. Neither a finite universal lift, twelve-count equality, full weights,
rational normalized weights nor a rational original chart is assumed.

## Conclusion

In this two-d-tag branch, |R|<=12. If there is no original finite bad
parameter whose actual error has support exactly V, then |R|<=11.
More precisely, if |R|>=12, then |R|=12 and all finite sparse errors
have weight four. There is exactly one parameter theta_V in R with
actual support V. It satisfies all L043 finite/recovery gates and also
its full-weight gate; it is not a projected solution at original infinity.

Each of the nine parameters in R minus {theta,theta',theta_V} has
actual support of the form

    {b,b',t,t'}, b in B minus {d}, b' in B' minus {d},
    {t,t'} subset T_0, |{t,t'}|=2.

Every coordinate of T_0 occurs exactly four times among these nine
errors and A_2. Indeed every coordinate of O occurs exactly four times
among all fifteen errors indexed by R and the original triple. V is
the unique B-disjoint support in R; the other eleven meet B once.
In particular twelve candidates all meeting B are impossible when
two of them are d-tagged.

The three full errors on K,K',V have union B' of size six, pairwise
intersections {d,s}, P, P', respectively, and empty triple intersection.
This is a forced union-six branch, not an exclusion of that branch.
The result does not force two d-tags in every pencil, settle eleven,
provide universal extraction, or improve the global 11/q–16/q interval.
The original K_* may or may not have a finite lift. A separate scoped
critical audit on 2026-10-10 found no defect; its checks appear below.

## Proof

### Inputs, lower weights and the first lift

L043 (4)–(7) provides an actual error of weight at most four at every
parameter of R, before its last weight gate. It has all eight moments
of the original syndrome pencil, with the nonzero scaling lambda/(gE).
L042 supplies nonzero D and every nonzero coordinate locator. L010
therefore supplies uniqueness, same-support badness, and the weighted
bound on all finite sparse parameters. If any of them has weight at
most three, L010 (2) bounds the entire bad set by thirteen. Since R is
disjoint from the three stipulated parameters, |R|>=12 would supply at
least fifteen bad parameters. Thus under |R|>=12 every finite sparse
error has weight four. Every witnessing four-set is then its actual
support, and the two d-tag witnesses are full as well.

For the rest of the proof assume m=|R|>=12. At each coordinate x,
L010's pointwise locator identity makes every occurrence in these
full supports a distinct root of ell_x. Its nonzero degree is at most
four. Hence each coordinate occurs at most four times, including any
other finite errors we explicitly count. Distinctness here is of actual
original finite parameters, not support descriptions.

Interpolate the original full errors on A_0,A_1 in their original
parameter:

    n_B(t)=((gamma_1-t)e_0+(t-gamma_0)e_1)/(gamma_1-gamma_0).

This word is supported in B and has syndrome s(t) for every t in F,
since the two moment pencils agree at two distinct parameters. At a
parameter in R the coefficients at y_1,y_2,z_1,z_2 are all nonzero:
the original weights are nonzero and t differs from gamma_0,gamma_1.
If its actual four-support J met B in at least two labels, then
n_B(t)-e_t would be a codeword supported on B union J of size at most
eight. L010's kernel identity and distance nine force n_B(t)=e_t.
The four singleton coefficients would force J=K_*, which is excluded
from R. Consequently every support in R meets B at most once.

This is exactly the scoped six-lift argument already recorded in L045;
it is included to verify that use directly from audited L043 and L010,
without importing L045's unaudited complete profile theorem. It is not
claimed as a new result. L044 descent and the full L046 statement are
not used. The new step below couples this lift with a different one.

### The second lift and its only exception

By audited L048–L049, the two selected full errors have supports
K={d,s} union P and K'={d,s} union P', as in the hypotheses. Form

    n_B'(t)=((theta'-t)e_theta+(t-theta)e_theta')/(theta'-theta).

The denominator is nonzero. This is a word on B' whose syndrome is
again the original s(t), by affine interpolation. For every t other
than theta,theta', all four coefficients on V=P union P' are nonzero:
on P they are nonzero original weights times (theta'-t)/(theta'-theta),
and on P' they are nonzero original weights times
(t-theta)/(theta'-theta). No claim about the two coefficients at d,s
is needed.

For any further full four-support J at such a t, if |J intersect B'|>=2,
the word n_B'(t)-e_t is supported on at most eight labels and is a
codeword. Distance nine makes it zero. The four nonzero coefficients
on V therefore force J=V. Thus every parameter in R other than the
two selected ones and a possible V parameter has support meeting B'
at most once.

There is at most one finite parameter with support V. Indeed any such
parameter differs from theta,theta' and, by the preceding distance
argument, has e_t=n_B'(t). It must make the d coefficient of n_B'(t)
zero. That coefficient is an affine polynomial in t, nonzero at theta
and theta' because both chosen errors are full. It is therefore a
nonzero polynomial of degree at most one and has at most one root.
This also covers the case of a nonzero constant coefficient, when no
such parameter exists. Simultaneous vanishing at d and s is not
presumed, and no root at infinity is counted.

Any finite bad error with support V is necessarily indexed by R.
Its support differs from A_0,A_1,A_2,K_* and from K,K': V is outside
B and avoids s, whereas A_2 contains h and s. Uniqueness excludes the
three original parameters and theta,theta'. The complete converse of
L043 consequently puts it in the nonuniversal branch with every gate
(4)–(7), and its actual full weights satisfy (9). This uses the complete
criterion, not projected proportionality alone.

Let epsilon be one if this finite V error exists and zero otherwise.
The argument above proves epsilon is either zero or one and counts
exactly the possible exception in R.

### The five-coordinate capacity

The sets B,B' have union eleven. Their complement T_0 has five labels,
and so has total locator capacity 5*4=20. A_0,A_1,K,K',V have no
coordinates in T_0. The original A_2 contains exactly two of them,
namely W_0: its other two labels are h in B and s in B'. This uses
the residual-pair disjointness in L048 essentially.

Each of the m-2-epsilon remaining supports in R meets B and B' at
most once, hence has at most two labels in their union and at least
two in T_0. Counting only these distinct parameters and A_2 gives

    2 + 2(m-2-epsilon) <= 20, hence m <= 11+epsilon.       (1)

Any additional uncounted finite errors can only consume capacity;
their absence is not assumed. Since m>=12 and epsilon<=1, (1) forces
m=12 and epsilon=1. This proves the upper bound and the forced finite
V recovery. If m<12 to begin with, the asserted bounds already hold;
thus the proof has not imposed full weights on low-count cases.

Now (1) is equality. Each of the nine remaining supports has exactly
two coordinates in T_0 and two in B union B'. Since each intersection
with B or B' has size at most one, these two coordinates must be one
in B minus {d} and one in B' minus {d}. A support containing d would
have at most one coordinate in that union under the same bounds.
This gives the displayed support form. The twenty counted incidences
in T_0 saturate every one of its five coordinate capacities.

In R the supports K,K' meet B at d, V avoids B, and the other nine
meet B once. Thus exactly eleven supports meet B and their total
number of incidences in O is 12*4-11=37. The original triple contributes
three further O incidences, all in A_2. Hence the ten O coordinates
have forty incidences in total, each bounded by four; all are saturated.
The pairwise intersections and empty triple intersection of K,K',V
follow directly from the disjoint pairs P,P' and labels d,s. This
establishes the forced union-six branch without importing a bound for
its possible completions.

### Source scope and remaining gap

All recurrence applicability is inherited unchanged from L043:
Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2 dated July 17, 2026, source lines 2785–2935, DR2
`drc:lem-locator-recurrence` and DR6–DRC `drc:thm-exact-compiler`,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
L043 inspected and specialized these to eight shifted moments, four
distinct support labels and nonzero column multipliers in H. No source
refresh or recurrence reproof is needed here. The mutable version is
not certified identical to ePrint 2026/1463. L049's complete fixed-H
certificate remains an essential input for the initially arbitrary
two-d-tag pair; this proof does not replace it with sampling.

The capacity restriction is an intermediate result under the saved
EXPLORE assessment of the uniform eleven target. L047 already studied
a disjoint candidate *when given* and its possible union-six coupling;
here that candidate is forced at twelve from the two existing d-tags.
Neither its further compatibility nor the existence of two d-tags is
settled. No known theorem or count is presented as a new discovery;
POTENTIALLY_NEW refers only to this conditional restriction beyond the
assessed inputs, not certified originality. All interpolation is in the
original affine parameter, over F, with no chart change or descent.

### Separate scoped critical audit (2026-10-10)

The audit found no defect in the stated conditional result. It validates
this existing local restriction, without establishing eleven, a new
count bound, or originality. The argument was checked against L010's
full kernel, locator and weighted-count proof, L042's audited
nonpersistence, L043's complete criterion and recovery proof, and the
audited conclusions of L048–L049. The recorded L049 proof/certificate
audit is reused as an input; its enumeration was not replayed here.
No full L044–L046 theorem or L040 candidate bound is assumed.

The distance input also has the precise standard citation J. I. Hall,
*Notes on Coding Theory*, section 5.1, Theorem 5.1.1 and proof,
printed pp. 63–64 of the undated author-hosted
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
inspected in the saved 2026-10-08 coverage. H consists of sixteen
distinct elements of F and the evaluation multipliers are all one,
so n=16,k=8 gives distance nine over F, including extension-field
words. L010 identifies the kernel of the eight shifted moments with
this code. The two applications below check that identification and
the support bounds; they do not reprove the imported distance theorem.
The recurrence source and its exact specialization remain those cited
above and in L043; there is no new theorem import or source refresh.

For every member of R, L043 places N_K in the entire eight-moment
span of K before checking nonzero recovered weights. Its scale
lambda/(gE) is nonzero because lambda!=0, gamma_1!=gamma_0 and E!=0.
Thus each distinct original finite parameter has an actual sparse
representative. L042 gives all the hypotheses needed for L010 to make
it unique and bad on its actual support complement. R excludes the
three original parameters, which are themselves full-weight bad
parameters. If m>=12, there are at least m+3>=15 distinct bad
parameters. Any finite sparse error of weight at most three, whether
in R or outside it, would give at most thirteen by L010 (2). This
contradiction justifies full weights globally in the high-count branch.
It is not an assumption about a relaxed witness. L010's pointwise
identity then makes every actual occurrence at x a root of the
nonzero polynomial ell_x of degree at most four. This is the only
coordinate-capacity premise; sixteen-count equality is never invoked.

For the first lift, affine interpolation agrees with s(t) identically
because both vector-valued affine polynomials agree at gamma_0 and
gamma_1. Its four singleton coefficients are the nonzero original
weights multiplied by nonzero interpolation factors at any t in R.
If a full J meets B twice, |B union J|=10-|B intersect J|<=8.
The difference has zero full syndrome and is a codeword of weight
at most eight, hence zero. The four singletons force J=K_*.
At high count J is exactly its witnessing set, so R's exclusion of
K_* applies. This verifies the needed portion of L045 directly.

L048–L049 apply to the two distinct selected parameters with the same
relaxed gates as L050. They give s in W and the three disjoint residual
pairs, without any full-weight or prime-field-weight premise. The
already established high-count reduction makes the selected witnesses
actual full errors. Since theta!=theta', their second interpolating
word is well defined in the original affine parameter and again has
syndrome s(t) identically. At every other finite t its four coefficients
on P union P' are nonzero. If J meets B' twice, the same exact bound
|B' union J|<=8 forces equality with that lift and then J=V. These
arguments allow either shared coefficient, at d or s, to vanish.

For uniqueness, a full V error cannot be at theta or theta', because
uniqueness of sparse representatives would equate different actual
supports. At any other finite parameter it equals the second lift by
the preceding distance argument. The lift's d coefficient is nonzero
at theta and theta', so it is a nonzero affine polynomial. If constant
it has no zero; otherwise it has at most one finite zero. A V recovery
would require that zero and also a zero of the s coefficient. Thus
there is at most one, with no presumed simultaneous root or counted
root at infinity. No sufficiency claim follows from the d root alone.

Eligibility is a separate check. The disjoint pairs show V is outside
B, avoids s, and is a four-set distinct from K,K' and K_*. It also
differs from A_0,A_1,A_2, since each of those contains h whereas V
does not. Sparse uniqueness excludes all five selected/original
parameters. Any actual finite V recovery is therefore an additional
full-weight error to which L043's necessary direction applies. Its
universal case is only K_*, so V must satisfy the nonuniversal
proportionality, mu!=0,-1, E!=0, recovered shared-column equations,
and full-weight gate. In particular it belongs to R in the original
chart. This proves that epsilon counts exactly the possible exception
inside R; it does not manufacture that exception from a quotient root.

Finally, |B union B'|=6+6-1=11, so T_0 has five labels. W_0 is
disjoint from B and B', whereas h is in B and s is in B'. Thus A_2
contributes exactly two T_0 incidences. Each of the m-2-epsilon other
R supports has at most one element in each lift set, hence at least
two outside their union. All counted parameters are distinct. The
resulting lower bound is 2+2(m-2-epsilon) against capacity twenty.
For m=12 it is twenty-two if epsilon=0 and twenty if epsilon=1;
for m>12 even epsilon=1 exceeds twenty. This proves exactly the
claimed conditional bound, including the absence-of-V alternative.

At equality there are nine remaining supports, each with exactly two
T_0 labels. Their two other labels cannot include d: d already uses
the allowed intersection with both B and B', preventing a second
label in their union. Thus one is in B minus {d} and the other in
B' minus {d}. All five T_0 coordinates have four incidences because
their twenty total incidences meet five separate upper bounds of four.
K,K' give two B-overlaps, the nine mixed supports give nine, and V
gives none. The twelve R errors therefore contribute 48-11=37
incidences in O. Only A_2 contributes there from the original triple,
with three, so all ten O capacities are likewise saturated. Uncounted
errors could only add incidences and cannot weaken either bound; a
possible K_* error uses none of O. The support intersections of
K,K',V are exactly {d,s}, P and P', with empty triple intersection,
which verifies the forced union-six claim without invoking any
completion theorem. Low-count cases m<12 require no full-weight
argument and satisfy the stated numerical conclusions immediately.

The direct mathematical inputs and argument assembly are unchanged.
The finite forced-V completion, fewer-than-two-d branches, other
triple patterns, universal extraction and identification with ABF26
remain unresolved. No numerical experiment, certificate preview or
documentation check substitutes for this written audit.

## Mathlib

The full two-lift restriction and forced finite recovery: **not checked**
for matching Mathlib coverage. Supporting kernel/distance identities,
Vandermonde injectivity, polynomial root bounds and finite incidence
counting are used as established in L010 and the audited local inputs;
no new Mathlib lookup, absence claim or Lean verification is asserted.
The separate scoped informal audit above found no defect; it is not a
Lean verification or a critical review of a complete challenge solution.
