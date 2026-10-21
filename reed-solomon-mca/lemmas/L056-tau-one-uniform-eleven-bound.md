# L056 — Uniform eleven nonuniversal candidates for a tau=1 pencil

## Hypotheses

Use the complete gated local setup of audited L043: F=F_(97^20),
H={x in F_97^*: x^16=1}, C=RS[F,H,8], and the pinned radius cell
1/4<=delta<5/16. The three base supports are

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3}.

All nine labels are distinct. The original finite gamma_0,gamma_1,gamma_2
are distinct in F, lambda!=0, and p*q*(1-p-q)*r*(1-r)!=0.
The parameters, weights and excluded original direction remain arbitrary
over F. Put B={h,d,y_1,y_2,z_1,z_2}, O=H minus B, and
K_*={y_1,y_2,z_1,z_2}. Thus |B|=6 and |O|=10.

Let R be the set of distinct original finite parameters satisfying L043
(4)–(7) for some four-set K other than A_0,A_1,A_2,K_*.
Retain its nonzero proportional quotient case, mu!=0,-1, E!=0, and
T=gamma_0+g*rho/E; these parameters differ from all three gamma_i.
Do not impose the nonzero recovered-weight gate (9).
Multiple witnessing supports at one parameter count only once.

Use the separately audited conclusions of L051 (only its conditional
two-d-tag exclusion) and L055 (its uniform singleton-eight consequence).
Their complete fixed-H computational inputs and original-chart scopes
remain essential; this lemma does not independently replay them.

## Conclusion

There are at most eleven distinct nonuniversal candidates:

    |R| <= 11.

Moreover, the entire finite bad set of this gated local pencil has at
most fifteen parameters in the pinned event. In particular a sixteen-error
equality pencil cannot contain an actual triple with these tau=1 supports.
This is conditional on the existence of this local triple; it is not a
classification or extraction theorem for arbitrary pencils.

A separate critical audit on 2026-10-10 found no defect in this assembly
or its conditional fifteen consequence; the checks are recorded below.
This verifies the stated local counting target, retaining its audited
computational inputs. The global interval 11/q–16/q, other triple patterns,
arbitrary extraction and the challenge-definition gaps remain unchanged.
No complete challenge solution or certified originality is claimed.

## Proof

### Applicable inputs and support classification

L043, through audited L041–L042, supplies the actual three full-weight
base errors and nonzero D and all nonzero coordinate locators. Hence
L010's uniqueness, moment-kernel identity and weighted bound apply to
this actual original finite pencil. In particular each coordinate locator
has degree at most four. L043 (4)–(7), before (9), supplies a word omega
on K with the same eight moments as the B-supported word n(mu), where

    n(y_i)=-mu*c_(y_i), n(z_i)=c_(z_i),
    n(h)=c_h(q-mu*p), n(d)=c_d[1-(1+mu)r].

The corresponding actual sparse error is lambda*omega/(g*E).
The scaling factor is nonzero. These statements retain zero recovered
coefficients, and every such parameter is bad by L010.

The recurrence input is imported through L043 from Przemek Chojecki,
*Shortening Bounds for Reed–Solomon MCA*, live author TeX v9.2,
July 17, 2026, source lines 2785–2935, DR2
(`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), with the inspected zero-direction proof cases,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
This mutable source is not certified identical to ePrint 2026/1463.
L043's specialization has eight moments, four distinct support labels,
nonzero column multipliers x and shifted moments eta_j=s_(j+1).
It gives full moment membership, not merely four recovered equations.
No external recurrence or compiler theorem is reproved here; neither
that citation nor the inspected design comparisons supply this count.

For completeness verify the short support observation also appearing
in L045, rather than assume its unaudited full conclusion. If |K intersect
B|>=2, then |K union B|<=8. The difference n(mu)-omega is in ker(sigma)
and is supported in this union. L010's moment injectivity on at most
eight columns forces n(mu)=omega. The four singleton coefficients
-mu*c_(y_i), c_(z_i) are nonzero, so all four singleton labels lie in K.
Since |K|=4, this gives K=K_*, which was excluded. Consequently every
nonuniversal witnessing support satisfies

    |K intersect B| <= 1.                              (1)

This verifies only the needed elementary classification, already present
locally. The new step below combines it with the audited simultaneous
constraints; it does not assert a new MDS or overlap lemma.

### A hypothetical twelve count forces full and unique supports

Suppose n=|R|>=12. Together with the three base parameters there are
at least fifteen distinct finite bad parameters. If any finite bad
parameter had an error of weight at most three, L010 (2) would bound
the entire bad set by at most thirteen. Thus every finite bad error,
including every member of R, has weight exactly four.

L010's sparse uniqueness then makes each witnessing K precisely the
actual support: an allowed zero recovered coefficient would give weight
at most three, which was just excluded. Multiple choices of K at the
same parameter therefore coincide. By L010's pointwise locator formula,
each coordinate in any of these full supports is a root of its nonzero
coordinate locator at that original finite parameter. Distinct parameters
give distinct roots. Each coordinate thus occurs in at most four supports
among the base triple and the members of R. This uses only the degree
bound, not sixteen-count equality, complete splitting or rational descent.

### Counting the remaining support types

By (1), the supports from R are partitioned into those meeting B at one
of its six labels and those disjoint from B. Let s count those tagged
by a singleton y_1,y_2,z_1,z_2, let a count h-tagged supports, let b count
d-tagged supports, and let c count B-disjoint supports. These are counts
of distinct parameters with unique full supports, so

    n=s+a+b+c,                 j=s+a+b

is exactly the total number of their incidences with B.

Audited L055 gives s<=8 under precisely the present gates, even before
full weights were deduced. It does not require pairwise-disjoint outside
triples and does not assert unconditional singleton-two. The h coordinate
already occurs at each of the three distinct base parameters. Its locator
has degree at most four, so a<=1.

If b>=2, two distinct nonuniversal parameters have supports {d} union S
and {d} union S' with three-subsets of O, by (1) and full weights.
This is exactly the two-d branch of audited L051, whose conditional
conclusion gives |R|<=11. Its audited internal geometric reduction and
finite certificates apply for this same fixed H and arbitrary original
chart; no universal lift is required. This contradicts n>=12. Therefore
b<=1 in the hypothetical high-count case. Combining these three bounds,

    j <= 8+1+1 = 10.                                   (2)

The three base errors contribute exactly three incidences to O, namely
the three w-labels of A_2. The errors from R contribute 4n-j incidences
to O, including four for each B-disjoint support and three for every
tagged support. The ten coordinates of O each have capacity at most four,
so

    3+4n-j <= 40.                                      (3)

But n>=12 and (2) imply 3+4n-j>=3+48-10=41. This contradicts (3),
proving |R|<=11. Equivalently twelve would require j>=11 while the
audited simultaneous constraints give j<=10. No independent B-disjoint
bound, finite universal recovery or unproved parameter descent is needed.
Additional bad errors outside the counted set could only consume further
locator capacity; omitting them does not invalidate this upper bound.

### Conditional fifteen bound for the full bad set

L010 already bounds the entire bad set by sixteen. If it had sixteen
parameters, all would have full weight by L010. Apart from the three
base parameters, any full-weight error is covered by L043, provided
its support differs from the three base supports. No second parameter
can have a base support A_i: if it did, affine interpolation between its
syndrome and the base syndrome would represent the entire pencil on
A_i, making every locator at a coordinate of A_i identically zero,
contrary to L043's nonpersistence. This is the same fixed-support
argument used in L010's same-support failure proof.

L043 classifies all the remaining supports. Its unique universal support
K_* has at most one eligible finite parameter, requiring both actual
lift gates. Every other full-weight error satisfies the nonuniversal
(4)–(7) gates, hence belongs to R. The sixteen-count assumption would
therefore require at least 16-3-1=12 members of R, contradicting the
proved eleven bound. Thus the full bad set has size at most fifteen.
This argument does not assume a universal lift exists: if absent it
would require thirteen members of R instead. It also does not overlook
lower-weight errors, since the sixteen-count premise excluded them first.

No global interval improvement follows without proving that arbitrary
potential equality pencils contain the specified triple, or separately
excluding their other configurations. The pinned event is not identified
with the unread ABF26 definition.

### Separate critical audit (2026-10-10)

The audit checked the full assembly against L010's weighted bound,
L043's complete quotient and recovery cases, and the already audited
conclusions of L051 and L055. It found no mathematical defect. This is
verification of the existing local result, not a stronger count or an
independent replay of its computational theorem inputs. The approved
source comparison was reused without new external searches. The direct
mathematical inputs remain L010, L043, L051 and L055.

**Original pencil and relaxed membership.** All nine labels lie in H;
the seven roots of Q are outside their union, so every displayed c_x is
nonzero. The gates give g,lambda,rho,1-rho nonzero. From L043 (16)–(19),
at t=rho/E the identities

    (1-t)/(1-rho)=-mu/E,       t/rho=1/E

hold with E nonzero. Thus sigma(n(mu))=N_K and
s(T)=lambda*N_K/(gE) as full eight-entry vectors. L043 (6)–(7) imply
recurrence membership, and its first-four-moment solve recovers the
unique coefficients of that full vector on K. A zero coefficient still
gives a sparse actual error; L010's same-support argument makes it bad
on its actual complement, whose size is at least twelve. Consequently
the relaxed definition of R discards neither these parameters nor the
original input-failure requirement. E=0 has no finite solution, and
mu=-1 is exactly the excluded third base parameter. All counted T lie
in the original affine chart.

**Fullness before tagging.** Distinct members of R are distinct from
the three gamma_i by L043. Hence n>=12 gives at least fifteen bad
parameters. In L010 (2), any N_3>=1 bounds the total by thirteen;
N_2>=1, N_1>=1 or N_0>=1 gives an even smaller bound. None is possible.
Thus every weight-at-most-four representative has weight four. Sparse
uniqueness then forces every four-set witnessing one of these parameters
to equal its actual support. In particular one parameter cannot acquire
several different tags by padding a smaller support.

For the short overlap observation, n(mu)-omega has zero eight-moment
vector and support contained in B union K. If |B intersect K|>=2,
this union has size at most eight, so injectivity forces equality of
the two words. Since mu and the four singleton c_x are nonzero, K
contains all four singleton labels and hence equals K_*. This checks
(1) without using the unaudited full L045 theorem. It actually holds
before the fullness argument; the latter is needed for the unique
support partition and exact incidence counts.

**Simultaneous bounds and capacities.** L055's unconditional eight
consequence has exactly this relaxed candidate definition, label set,
field and original-chart gates. It covers both intersecting outside
triples and candidates witnessed by more than one support, so it applies
in particular to the now unique singleton-tagged supports. It does not
assert the false unconditional singleton-two restriction of ATTEMPTS/024.
L010's formula L(gamma,X)=D(gamma) product_(x in supp(e))(X-x)
makes each full error occurrence a root of the corresponding nonzero
locator. The three distinct base parameters already use three roots at h,
leaving at most one h-tagged member of R. If two d-tagged members exist,
(1) puts their other three labels in O. These are exactly L051's initial
two-d hypothesis and relaxed R; its intersection pattern and forced V
recovery are consequences of its audited inputs, not additional
assumptions on this invocation. No finite universal lift or rational
original parameter is required. L051 contradicts n>=12, leaving b<=1.

The unique supports therefore give j=s+a+b<=10. There are ten labels
in O, each in at most four of the counted full errors, whether or not
other bad parameters exist. The base O incidence count is exactly three:
A_0 and A_1 are in B and A_2 contributes W. A tagged support contributes
three and a disjoint support four, giving exactly 3+4n-j. For n>=12
this is at least 41, exceeding capacity 40. Thus no zero-weight gate,
witness multiplicity, or omitted universal parameter affects the
contradiction. The achieved bound eleven meets the required threshold.

**Entire finite bad set and equality exclusion.** L010 gives a total
ceiling of sixteen, and a sixteen-count premise forces all errors full.
If an extra parameter T had support A_i, interpolation of its error
and e_i would give a word e_i+(X-gamma_i)(e_T-e_i)/(T-gamma_i)
supported on A_i whose moments equal the pencil identically in X.
The same determinant dependence used in L010 then makes every locator
at a label of A_i the zero polynomial, contradicting L043. This is a
polynomial identity, not an inference from many field evaluations.
Hence all thirteen additional errors have nonbase supports and fall
under L043's exhaustive cases. The one-zero and independent quotient
cases admit none; E=0 admits no finite point; mu=-1 returns gamma_2.
The sole both-zero support is K_*, with at most one finite lift even
when both actual lift gates hold. Every other full additional error
belongs to R. Sixteen would therefore require |R|>=12, already excluded.
Lower-weight errors cannot evade this argument because the premise
sixteen excluded them before classification. The resulting fifteen
bound covers the full finite bad set, not only chosen recoveries.

Finally an actual tau=1 triple inside an L010 equality pencil satisfies
L041's normalized local gates after renaming. Audited L043 includes
that setup, so the conditional exclusion applies to such a triple.
Existence of a suitable triple in an arbitrary equality family is not
proved. ATTEMPTS/022–024 remain valid stop evidence; the assembly uses
audited simultaneous counts absent from those failed approaches.

## Mathlib

The full uniform eleven assembly and conditional fifteen bound: not
checked for a matching Mathlib theorem. L010 supplies the moment
injectivity and polynomial root bounds; audited L043, L051 and L055
supply the substantive local inputs. Their full hypotheses and finite
certificate qualifications remain in force. No Mathlib absence claim,
Lean formalization, new certificate verification or fresh external-source
inspection is asserted. The separate informal audit above verifies the
assembly within this fixed-H scope, reusing the completed input audits.
