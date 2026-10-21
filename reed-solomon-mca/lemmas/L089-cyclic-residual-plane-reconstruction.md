# L089 — Fullness and explicit reconstruction of a cyclic residual plane

## Hypotheses

Use precisely L088's setting: F=F_(97^20), H the order-sixteen
subgroup of F_97^*, and any bijection h:Z/16Z -> H. Write

    v_i=(1,h(i),...,h(i)^7)^transpose,
    B_t={t,t+1,t+4,t+6},   U_t=span_F{v_i : i in B_t},
    K=intersection_t ker(wedge^2(V -> V/U_t)),   V=F^8.

All indices below are modulo sixteen. No actual errors, finite chart,
weights, parameters or nonpersistent locators are assumed.
Let T_t={t,t+1,...,t+8}. For i in T_t define

    d_(t,i)=1/product_(j in T_t minus {i})(h(i)-h(j)).

These scalars are nonzero elements of F_97. Define four nonzero
scalars for each block, using only h:

    w_(s,s)=1,
    w_(s,s+4)=d_(s,s+4)/d_(s,s),
    w_(s,s+6)=w_(s,s+4) d_(s-1,s+6)/d_(s-1,s+4),
    w_(s,s+1)=w_(s,s+6) d_(s-2,s+1)/d_(s-2,s+6),
    r_s=sum_(i in B_s) w_(s,i) v_i.

Let R be the 8-by-16 matrix with columns r_0,...,r_15, and let M
be L088's full 96-by-28 alternating matrix.

## Conclusion

If K is nonzero, its rank-two plane S contains no moment column v_i.
Every S intersect U_s is a line, all sixteen lines are distinct,
and each line has four nonzero coefficients in its B_s column basis.
In fact

    S intersect U_s = F r_s   for every s.

Consequently rank R>=2 for every labeling, and

    K != 0  iff  rank R=2  iff  rank M=27.

Otherwise rank R>=3 and rank M=28. This is an explicit residual
test, not a determination of its outcome for any or every labeling.
Neither rank-two labeling nor uniform contradiction is exhibited.
No actual-error realization, arbitrary-family exclusion, original
chart or challenge resolution is inferred. The interval stays 11/q–16/q.

## Proof

### Inputs and scope of the specialization

L088, including its separate step-223 audit, makes every nonzero member
of K decomposable of contraction rank two, and gives dim K<=1.
Write one as a wedge b and put S=span{a,b}. The quotient equation
is exactly that the two images are dependent, or S intersect U_s!=0.
Only this elementary rank-two case of the exterior machinery already
cited in L088 is used. L010's Vandermonde proof supplies independence
of every set of at most eight distinct unshifted columns: multiply
each by its nonzero h(i) to recover L010's convention. L087 supplies
the distinct linear blocks and degree four. Its nonisomorphism theorem
and plane-family conclusions are not used.

### No contained column and distinct intersection lines

B_s and B_(s+7) are disjoint, so their four-dimensional column spaces
are complementary. S cannot be contained in U_s, as then its required
intersection with U_(s+7) would be zero. Hence each S intersect U_s
has dimension exactly one. Independence on the at-most-eight-label
union of two blocks gives

    U_s intersect U_t = span{v_i : i in B_s intersect B_t}.

First S cannot contain two distinct columns v_x,v_y. Those columns
would span S. At most eight blocks contain either x or y, so a block
avoids both. Its four columns together with v_x,v_y are independent,
contradicting its nonzero intersection with S.

Suppose now v_x belongs to S. Exactly four blocks contain x. In the
sixteen indexed consecutive pairs (B_t,B_(t+1)), each such block spoils
at most two pairs; therefore a pair avoids x in both blocks. Their
intersection is exactly {t+1}. If their S-intersection lines coincide,
that common line is F v_(t+1), giving a second column in S. If they
are distinct, they span S inside U_t+U_(t+1), which is spanned by
the seven columns of B_t union B_(t+1). Adjoining v_x makes eight
independent columns, so v_x cannot lie there. Both alternatives are
impossible. Thus S contains no v_x. For any two blocks, a coincident
intersection line would be a moment-column line by linearity (or
would lie in a zero intersection for disjoint blocks). All sixteen
lines are consequently distinct. No coefficient-zero branch was
discarded in this argument.

### The exact nine-column circuit

The nullspace of the eight moment rows on T_t has dimension one,
since any eight of these nine columns are independent. Its nonzero
vectors have no zero coordinate, by that same independence.
We need its explicit unshifted formula rather than an unspecified
null vector. Put

    P_t(X)=product_(i in T_t)(X-h(i)),
    Q_t(X)=product_(i not in T_t)(X-h(i)).

The sixteen labels are exactly H, so P_t Q_t=X^16-1. At h(i),
i in T_t, differentiation gives

    P_t'(h(i)) Q_t(h(i))=16 h(i)^15,
    d_(t,i)=h(i) Q_t(h(i))/16.

Here 16 is invertible in characteristic 97 and h(i)^16=1.
For 0<=j<=7, extend the sum by zero on H minus h(T_t):

    sum_(i in T_t) d_(t,i) h(i)^j
      = (1/16) sum_(x in H) x^(j+1) Q_t(x) = 0.

The last equality is exactly L010's subgroup power-sum identity:
x^(j+1) Q_t(x) has no constant term and degree at most fifteen,
so every exponent belongs to 1,...,15. This specializes L010's
moment-kernel calculation to the unshifted nine-label circuit; the
displayed calculation is needed to fix the coefficient formula and
its nonzero normalization, not to reprove a general interpolation
or higher-order-MDS theorem. Thus (d_(t,i)) is the circuit generator.

### Consecutive triangles force full coefficients

Choose nonzero representatives z_j of S intersect U_j for the three
blocks j=t,t+1,t+2, and write their unique block coefficients as
e_(j,i), extended by zero to T_t. These three distinct lines in S
have a relation

    c_t z_t+c_(t+1) z_(t+1)+c_(t+2) z_(t+2)=0,

with every c_j nonzero: a zero coefficient would make two of their
distinct lines dependent. The coordinate vector
f_i=sum_j c_j e_(j,i) lies in the nine-column nullspace.

It cannot be the zero vector. Indeed the pairwise shared labels are
{t+1,t+2,t+6}, and all other labels of T_t occur in exactly one
of the three blocks. If f=0, all coefficients on those six singleton
labels vanish. Every z_j then lies in the span W of the three
shared-label columns. Any two z_j span S, giving S contained in W.
At most twelve blocks contain any of those three labels, so some
block avoids them all. Independence of its four columns and the
three columns spanning W makes its span disjoint from W, contrary
to its required intersection with S. Therefore f!=0.

It follows that f=kappa (d_(t,i)) for a nonzero kappa. In particular,
each singleton coefficient in each of these three blocks is nonzero.
For a fixed block B_s the singleton pairs in its first, middle and
last roles among consecutive triangles are respectively

    {s,s+4},   {s+4,s+6},   {s+1,s+6}.

They cover all four labels. Thus all four coefficients of its line
are nonzero. The argument treats every translated triangle under
the original arbitrary bijection; translation is only an incidence
selection, never a symmetry of h.

### Reconstruction and the remaining rank test

Normalize the B_s coefficients of its line by setting its coefficient
at s equal to one. At two singleton labels i,j in any one of the
triangles, the common nonzero c_s and kappa cancel, giving

    e_(s,i)/e_(s,j)=d_(t,i)/d_(t,j).

Apply this successively to the three singleton pairs just listed.
They form a tree on the four labels, so they determine exactly the
four w_(s,i) in the statement. All divisions have already been
justified. This proves S intersect U_s=F r_s without presupposing
rationality of the chosen representatives or an affine chart.

For every labeling, each r_s is nonzero by independence on B_s,
and its four coefficients are nonzero by construction. Distinct
r_s,r_t cannot be proportional: their block spans intersect only
in zero or a shared column, whereas a full four-column expansion
cannot be supported on that intersection. Thus rank R>=2.
If K!=0, the reconstruction puts every r_s in S, hence rank R=2.
Conversely, if rank R=2, let S be its column space. Each nonzero r_s
lies in S intersect U_s. For any basis a,b of S, the images in every
V/U_s have rank at most one, so the nonzero tensor a wedge b belongs
to K. L088 then gives rank M=27; in the other case it gives rank 28.

For completeness the triangle's three shared-label equations remain
explicit necessary checks on h, beyond the three singleton ratios.
For a fixed t abbreviate

    A=d_(t,t),
    B=d_(t,t+5)/w_(t+1,t+5),
    C=d_(t,t+3)/w_(t+2,t+3).

Every nonzero kernel must satisfy all three equations

    A w_(t,t+1)+B = d_(t,t+1),
    B w_(t+1,t+2)+C = d_(t,t+2),
    A w_(t,t+6)+C w_(t+2,t+6) = d_(t,t+6).

These follow by dividing the circuit relation by kappa and inspecting
the shared coordinates; they are necessary, with no sufficiency claim.
All sixteen triangles and the full rank R test remain unevaluated.

This is one analytic residual-kernel attempt under the ready EXPLORE
assessment `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
It establishes a useful uniform intermediate restriction and retains
the precise remaining label-only equations. No rank sampling, label
sweep, computation, plane-family import or actual-error assumption is
used. POTENTIALLY_NEW means only that the assessed sources did not
establish this conclusion, not a certified originality claim. This
proof's separate critical audit is recorded below.

### Separate critical audit — October 15, 2026, step 226

The audit used the unchanged pre-existing EXPLORE assessment
`drafts/literature/2026-10-14-cyclic-residual-plane-audit.md` and checked
the complete proof. No mathematical defect or necessary change to the
argument was found. This validates L089 as a local input; it establishes
no stronger rank bound and makes no new originality claim.

**Input scope and conventions.** Audited L088 gives a decomposable
nonzero tensor with two-dimensional image S and dim K<=1, on precisely
the unshifted columns and full exterior quotient maps used here.
For independent a,b, their quotient wedge vanishes exactly when the
quotient map on S has rank at most one, equivalently S meets U_s
nontrivially. L010's first proof paragraph gives independence and the
subgroup power sums without using its later pencil hypotheses. Scaling
v_i by nonzero h(i) converts to its shifted moment convention. L087's
ordered-difference proof gives distinct linear blocks and degree four;
its nonisomorphism comparison with L072 is not used. The cited Conrad
exterior results in L088 apply over this finite-dimensional field
setting; no new exterior theorem or source import is required.

**Contained-column branches.** The offset sets {0,1,4,6} and
{7,8,11,13} are disjoint modulo sixteen, so U_s and U_(s+7) are
complementary by eight-column independence. A required nonzero
intersection with the latter excludes S contained in the former.
All S intersections therefore have dimension one. For distinct blocks,
independence of their union identifies the span intersection exactly
with the span of their common labels. If S contains two different
moment columns, those span S and at most eight blocks contain either
label; an avoiding block contradicts six-column independence.
For one contained column v_x, its four containing blocks spoil at most
eight of the sixteen consecutive pairs. A remaining pair has shared
label t+1 distinct from x. Coincident intersection lines give a second
column in S; distinct lines span S in its seven-label union, where
adjoining x contradicts eight-column independence. This covers both
alternatives without full-coefficient assumptions. Line coincidence
for any other pair is then excluded by linearity and the same exact
span-intersection identity.

**Circuit and the zero-coordinate branch.** The consecutive triangle
has offset blocks {0,1,4,6}, {1,2,5,7}, {2,3,6,8}, with union
{0,...,8}, shared labels {1,2,6} and singleton pairs {0,4}, {5,7},
{3,8}, respectively. All are distinct modulo sixteen, also at wrapping
indices. Three distinct lines in a plane have a relation with every
coefficient nonzero. If its combined coordinate vector were zero,
all six singleton coefficients would vanish. The three representatives
would then lie in the span W of the three shared columns, so S would
lie in W. At most twelve blocks meet those three labels; an avoiding
block has span disjoint from W by seven-column independence. This
contradicts its required intersection with S and proves the coordinate
relation nonzero before any singleton coefficient is used.

The nine-column kernel has dimension one and no nonzero vector with
a zero coordinate, by independence of each eight-column subset.
Differentiating P_t Q_t=X^16-1 at h(i) gives
1/P_t'(h(i))=Q_t(h(i))/(16 h(i)^15)=h(i)Q_t(h(i))/16.
Here Q_t has degree seven, and x^(j+1)Q_t(x), for 0<=j<=7,
has only exponents 1,...,15. Extending the sum by its zero terms
outside T_t thus proves all eight unshifted moment equations using
L010's exact power sums. Distinct labels and characteristic 97 make
every product denominator and 16 nonzero. This verifies the actual
circuit normalization, not merely its dimension.

**All roles, ratios and shared coordinates.** For B_s, the first,
middle and last roles occur at t=s,s-1,s-2 and give singleton pairs
{s,s+4}, {s+4,s+6}, {s+1,s+6}. Each coefficient is consequently
nonzero. In a fixed triangle, f=kappa d with kappa nonzero yields
e_(s,i)/e_(s,j)=d_(t,i)/d_(t,j) for singleton labels of B_s.
Starting with e_(s,s)=1, the three successive ratios are therefore
d_(s,s+4)/d_(s,s), d_(s-1,s+6)/d_(s-1,s+4), and
d_(s-2,s+1)/d_(s-2,s+6), in exactly L089's directions.
They connect all four coefficients with no cyclic consistency
assumption. Every denominator is a proved nonzero circuit coefficient.

Using these normalized representatives, the triangle relation divided
by kappa has coefficients A,B,C. The singleton labels t,t+5,t+3
give precisely A=d_(t,t), B=d_(t,t+5)/w_(t+1,t+5),
C=d_(t,t+3)/w_(t+2,t+3). At shared labels t+1,t+2,t+6,
the contributions are respectively A w_(t,t+1)+B,
B w_(t+1,t+2)+C, and A w_(t,t+6)+C w_(t+2,t+6).
They equal the corresponding entries of d, with no missing sign or
shift. The w denominators are nonzero by construction. These are
necessary gates only; their sufficiency is neither used nor asserted.

**Rank equivalence and limits.** Independently of K, each r_s has four
nonzero coefficients in an independent block basis. Two such vectors
cannot be proportional because the intersection of their block spans
is zero or a single common column. Hence rank R>=2 for every labeling.
If K is nonzero, reconstruction puts all r_s in its plane S, so rank
R=2. Conversely rank R=2 supplies a plane meeting every U_s at r_s;
the wedge of any basis of that plane is nonzero and killed by every
quotient map. Thus K is nonzero, without assuming the desired rank
conclusion or shared-coordinate gates. Finally ker M=K and dim K<=1
from L088 give rank M=27 exactly in this case and rank M=28 otherwise.

All checks are uniform in the bijection h and its extension-field
coefficients. No finite rank sample, labeling sweep, mathematical
script, actual error, original chart or additional dependency is used.
The direct inputs remain L010, L087 and L088, so DAG.md is unchanged.
The argument itself is unchanged, so PROOF.md is unchanged. Rank R=2
is neither exhibited nor excluded; the global interval and remaining
application, arbitrary-family and challenge gaps are unchanged.

## Mathlib

Full matching coverage for the cyclic fullness and reconstruction
result has not been checked. No absence or Lean-verification claim
is made. The moment-independence and subgroup power-sum inputs are
L010's already documented calculations; the exterior input and its
precise Conrad citations are reused through L088.
