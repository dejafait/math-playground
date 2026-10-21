# L097 — Sparse block parities cannot transfer to the product dual

## Hypotheses

Put k=F_97 and retain exactly L088/L089's arbitrary bijection
h:Z/16Z -> H, where H is the order-sixteen subgroup of k^*.
Write v_i=(1,h(i),...,h(i)^7)^transpose in V=k^8 and
B_s={s,s+1,s+4,s+6}, with indices modulo sixteen. Suppose there is
a two-dimensional k-subspace P of V meeting every block space
U_s=span_k{v_i:i in B_s} nontrivially. This is the hypothetical
rational surviving plane; its existence is not asserted.

Let W=Ann(P), identified with a six-dimensional subspace of k[X] of
degree at most seven, and let C=ev_h(W) in k^16. Define

    D=(C*C)^perp,

where C*C is the k-linear span of all coordinatewise products and
perpendicularity uses the ordinary coordinate pairing. The full plane
relations, including L089's nonzero coefficients on all four labels of
every block, are essential. No actual errors or original chart are used.

## Conclusion

Every nonzero vector in D has support size at least twelve. In
particular no nonzero vector supported on the union of two blocks is
in D, and the same holds for any three blocks whose union has size
at most eleven. This includes arbitrary cancellations among their
linear block parities and arbitrary coordinate weights on that union.

The vector z_i=h(i) is in D and has full support. Thus at least one
product-dual direction is known, but this argument supplies no further
independent direction. The approved upper target dim(C*C)<=10 would
require dim D>=6. The source-backed lower comparison remains
dim(C*C)>=11. Neither that upper implication nor a surviving plane
is established or refuted here. The result is negative evidence for
the sparse-parity transfer, not a cyclic exclusion or a stronger MCA
error bound. The separate step-256 critical audit below found no defect
in this conditional obstruction.

## Proof

### Source inputs and the exact bilinear test

Import Hugues Randriambololona, *On products and powers of linear
codes under componentwise multiplication*, Contemporary Mathematics
637 (2015), 3–78, Proposition 2.38, printed p. 28,
[author's manuscript](https://perso.telecom-paristech.fr/randriam/maths/HR_AGCT-14.pdf),
[DOI](https://doi.org/10.1090/conm/637/12749). Its coordinate adjunction,
as inspected in the prior assessment, gives

    z in D iff z*C is contained in C^perp.

For any basis f_1,...,f_6 of W this is exactly all twenty-one equations

    sum_i z_i f_a(h(i)) f_b(h(i))=0,  1<=a<=b<=6.             (1)

Bilinearity and symmetry make these equivalent to vanishing for
every f,g in W; no single-factor parity is substituted for (1).
The rank argument below tests the entire system (1), without choosing
a labeling or a basis numerically. It is written out because the
needed support obstruction is not a conclusion of the cited adjunction.

For comparison, import Christine Bachoc, Oriol Serra and Gilles Zemor,
*Revisiting Kneser's Theorem for Field Extensions*,
[arXiv:1510.01354v2](https://arxiv.org/pdf/1510.01354v2),
24 February 2017, Theorem 3, printed pp. 2–3, and the stabilizer
remark before Corollary 14, p. 9. Apply it to the nonzero
six-dimensional factors W,W inside k(X). A stabilizer of their
finite-dimensional product consists of elements algebraic over k,
whereas the only such elements of k(X) are constants. Indeed, for
nonconstant r=p(X)/q(X), the nonzero polynomial p(T)-r q(T) makes
X algebraic over k(r), so algebraicity of r over k would contradict
transcendence of X. The theorem therefore gives dim(W W)>=11.
Products have degree at most fourteen, and evaluation at sixteen
distinct labels is injective by the polynomial root bound. This
imports dim(C*C)>=11. It uses neither an MDS assumption on C nor
an identification of stabilizers in k(X) and k^16; the source theorem
is not reproved.

### Projection ranks, including all small supports

Let Q=V/P and q_i=v_i+P. Pairing Q with W identifies the rank of
the restriction C -> k^S with

    r(S)=dim_k span{q_i:i in S}.                             (2)

For a basis a,b of P, every quotient V/U_s sends a,b to dependent
vectors, so the nonzero tensor a wedge b belongs to L088's K.
Thus L089 applies after scalar extension to F_(97^20); all ranks and
containments here descend to k, since P and the columns are defined
over k. In particular q_i is nonzero, P intersect U_s is a line,
P is not contained in U_s, and its unique block expansion has all
four coefficients nonzero.

Any two q_i,q_j are linearly independent. L088's incidence separation
fact supplies disjoint blocks containing i and j respectively. Their
four-dimensional spaces are complementary in V by eight-column
independence. Each image in Q has dimension three, and their sum is
all six-dimensional Q. Their images therefore intersect in zero.
The two nonzero q_i,q_j in those respective images cannot be
proportional. This uses the separation fact proved in L088, not an
assumption that disjoint containing blocks exist in an arbitrary family.

P is not contained in the span of any four columns indexed by S.
If it were, choose any block B_t different from S; one exists among
the sixteen distinct blocks. Independence on S union B_t, which
has at most eight elements, gives

    span{v_i:i in S} intersect U_t
       = span{v_i:i in S intersect B_t}.

The nonzero line P intersect U_t would then have zero coefficients
at B_t minus S, contrary to its full four-coordinate expansion from
L089. Thus dim(P intersect span{v_i:i in S})<=1 for |S|=4,
which gives r(S)>=3. For |S|=3, the pair result already gives
r(S)>=2, covering possible three-column dependencies without
assuming they are absent.

For 5<=|S|<=7, the original columns are independent and quotienting
by a two-plane lowers their rank by at most two, giving
r(S)>=|S|-2. For |S|>=8, any eight original columns span V, so
their images span Q and r(S)=6. We have proved all the bounds needed:

| Support size s | Lower bound on r(S) |
| --- | --- |
| 1, 2 | s |
| 3, 4 | s-1 |
| 5, 6, 7 | s-2 |
| 8, 9, 10, 11 | 6 |

Every row satisfies 2r(S)>s. Only L010's Vandermonde input, the
L088 separation fact and L089's full simultaneous plane conclusions
were used; no conjectural upper product bound enters these ranks.

### Excluding every support of size at most eleven

Suppose z is a nonzero vector of D, and put S=supp(z). On k^S
the symmetric bilinear form

    beta_z(u,v)=sum_(i in S) z_i u_i v_i

is nondegenerate: its diagonal entries are all nonzero by the
definition of S. Let A be the image of C in k^S, of dimension r(S).
All of (1) say exactly beta_z(A,A)=0. Hence A is contained in its
orthogonal complement. Nondegeneracy gives
dim A^perp=|S|-dim A, so 2r(S)<=|S|. This contradicts each of
the displayed rank bounds for 1<=|S|<=11. No sign, square-class,
or genericity assumption on z was used. Empty support is precisely
the excluded zero vector. This proves the support obstruction.

For each block normalize its full plane-intersection coefficients
as in L089 and extend them by zero to b_s in k^16. Then b_s is
in C^perp, since sum_i b_(s,i) v_i belongs to P. It is not in D
by the support obstruction. The failure can also be seen on actual
codewords: C restricted to B_s has dimension three and equals the
hyperplane b_s dot u=0. For three distinct indices a,b,d in B_s,
choose f,g in W with respective restrictions

    ev(f)|B_s = e_a-(b_(s,a)/b_(s,d)) e_d,
    ev(g)|B_s = e_b-(b_(s,b)/b_(s,d)) e_d.

These restrictions lift because they lie in that hyperplane. The
product residual is b_(s,a)b_(s,b)/b_(s,d), which is nonzero.
It follows that at least one of the twenty-one basis equations fails,
regardless of the basis. More generally, any nonzero combination of
two b_s, or of three with union at most eleven, is excluded by its
support; cancellations only decrease support. This conclusion does
not assert that all of C^perp is generated by the b_s, or that D
is contained in C^perp. Neither assertion is needed.

### The surviving global direction and limits of the attempt

For f,g in W, the polynomial X f(X)g(X) has degree at most fifteen
and zero constant coefficient. L010's subgroup power-sum identity
for exponents 1,...,15 gives

    sum_i h(i) f(h(i))g(h(i))=0.

Thus (h(i)) is a nonzero full-support member of D. This is the
standard polynomial-evaluation parity specialized to the fixed H,
not a new product constraint from cyclic incidence.

The failed sparse transfers do not exhaust possible dense vectors
or combinations involving more blocks. For the dense ansatz
z=sum_s lambda_s b_s, (1) requires the single choice of coefficients
lambda_s to annihilate all twenty-one sums
sum_s lambda_s sum_(i in B_s) b_(s,i) f_a(h(i))f_b(h(i)).
The sixteen available linear parities annihilate f_a alone and do
not supply that quadratic cancellation; no such simultaneous identity
was obtained. Nor is this ansatz asserted to cover all of D.
In particular, one guaranteed
direction falls short of six required for the upper target ten,
while the imported lower comparison is eleven. The decision to stop
this product-upper-bound candidate records that failed transfer; it
is not a proof that no different product-based argument could work.
All conclusions remain conditional on the hypothetical plane, whose
existence or impossibility is still open. No global error interval,
arbitrary-family result or challenge qualification changes.

### Separate critical audit — October 16, 2026, step 256

The complete proof was checked under the unchanged pre-invocation EXPLORE
assessment `drafts/literature/2026-10-16-cyclic-product-dual-obstruction-audit.md`.
No mathematical correction was necessary. This is verification of a local
conditional input, not a new product bound or a claim of originality.

**Input scope and descent.** A k-basis a,b of the hypothetical plane is
independent after extending scalars to F=F_(97^20). For every s, the map
P -> V/U_s has a nonzero kernel by the stated intersection hypothesis,
so its rank is at most one and its exterior square kills a wedge b.
Thus this nonzero tensor is in precisely L088's K; L089's conclusions
apply to its plane after extension. Containment, intersection dimension
and zero or nonzero coordinates are determined by ranks of matrices over
k and are unchanged by extension. The resulting block-intersection line
therefore exists over k and has four nonzero k-coefficients. L010's
opening Vandermonde and power-sum facts do not require any of its later
pencil hypotheses. The nonzero factors h(i) convert its shifted columns
to the unshifted columns here. No actual-error hypothesis has entered.

**Every restriction rank.** The natural dual of V/P is Ann(P)=W, so
the matrix of evaluation on S is the transpose of the matrix of the
q_i in any dual bases. This proves (2), including non-surjective
restrictions. L089 excludes q_i=0. For a pair of indices, each of
L088's disjoint containing blocks has quotient image of dimension
4-1=3. Those images sum to Q because their original spaces sum to V;
their intersection consequently has dimension 3+3-6=0. This proves
independence of every pair without excluding three-column circuits.
For an arbitrary four-set S, if P were contained in its column span,
choose a block different from S. Independence of the union identifies
the span intersection with the shared-coordinate span. The nonzero
plane-intersection line would have a zero coefficient on a label of
that block outside S, contradicting L089. Thus rank loss on a four-set
is at most one. On sets of sizes five through seven, rank loss is at
most dim P=2. On every set of size at least eight, an eight-subset
already surjects onto Q. In order s=1,...,11 the certified lower bounds
are exactly

    1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 6.

The corresponding lower bounds for 2r(S)-s are

    1, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1,

all strictly positive. No support size or possible three-column
dependency is missing from the contradiction.

**Bilinear test and cancellation.** The six basis vectors of W give
twenty-one unordered products; these span every product f*g by
bilinearity. Their vanishing is exactly total isotropy of the
restriction image A for beta_z. On the exact nonzero support of z,
the diagonal form is invertible, and the isomorphism with the dual
gives dim A^perp=s-r(S), irrespective of the square classes of z_i.
Thus 2r(S)<=s is necessary, contradicting every bound above. The
argument treats the zero vector separately and tests arbitrary weights,
so cancellations in a block-parity combination cannot evade it.
For the displayed single-block example, restriction rank three and
the nonzero parity give equality with its hyperplane. Both displayed
restrictions therefore lift to W. Their only common nonzero product
coordinate is d; pairing with b_s gives precisely
b_(s,a)b_(s,b)/b_(s,d), a nonzero element of k. This also checks the
explicit witness against the full product test, rather than a linear
parity test. No containment between D and C^perp is assumed.

**Sources, global parity and limits.** Reused the inspected primary
statements and proof passages recorded in the saved product assessment;
no new browsing or source theorem reproof was needed. Randriambololona
Proposition 2.38 has exactly the coordinate adjunction used above.
For BSZ Theorem 3, the ambient multiplication is in k(X), the product
space is nonzero and finite-dimensional, and its stabilizer has only
algebraic elements by the cited p. 9 remark. Constants are the only
algebraic elements of k(X). If a formulation normalizes a factor to
contain 1, divide W by any fixed nonzero f_0 in W: this scales its
product by f_0^(-2), preserves all dimensions and the stabilizer, and
does not change the lower bound eleven. Return to polynomial W W
before evaluating. Degree at most fourteen makes that evaluation
injective at sixteen distinct labels. No coordinate-algebra stabilizer
or MDS assumption is substituted for these hypotheses.

Finally Xfg has exponents only 1 through 15, including when f or g
has smaller degree or is zero. Every corresponding subgroup power sum
vanishes, proving that (h(i)) lies in D; all its coordinates are
nonzero. This certifies one independent direction, not that D has
dimension one. Square dimension at most ten would require at least
six dual directions, whereas the imported lower bound is eleven.
No dense constraint, plane existence, contradiction to the full
conditional upper implication, or stronger MCA count follows from
this audit. ATTEMPTS/035's sparse-transfer stop remains justified.
The argument and its direct mathematical inputs are unchanged.

## Mathlib

Full coverage of this conditional support obstruction was not checked.
No matching theorem or absence is claimed. The cited code-product
adjunction and field-extension theorem are the imported mathematical
inputs; the finite-dimensional rank specialization is supplied above.
