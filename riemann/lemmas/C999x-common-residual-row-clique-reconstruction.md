# C999x: Exact row-clique representation of the shared-residual lift

## Hypotheses

Use precisely C999w Sections1–7, including its declared registry and
fixed arithmetic graph, without removing even zero-radius symbols.
Thus J=1024, d=1022, m=2044, N=512, K=65536, and p is C999w(10).
Both original complex endpoint vectors are independent, free2:1023.
The predictor is the same exact Galerkin Y, the reference is the same
R with rational head H, and the threshold is mu=999/1000000 in the
original free Euclidean metric. All finite outputs and the entire
n>=K tail are those of C999w, with penalty256 and reference fraction1/2.
Retain its exact-Y inclusion/pin conditions and analytic-response,
IEEE754/Decimal, neutral-core and original c_* qualifications.

All centers, radii, affine coefficients and scalar majorants in this
construction are fixed rational numbers as specified there. A radius
computed from coefficient bounds is a constant, not another noise
variable. Let Q denote the FULL constant matrix C_cert in C999w(12),
after arbitrary rational symmetric Gamma_a and rational symmetric
Lambda_i have been chosen. Every Lambda_i>=0 remains required.

Import N. Kakimura, *A direct proof for the matrix decomposition of
chordal-structured positive semidefinite matrices*, METR2009-13,
April2009, **Theorem1 and its proof, printed pp2–3**,
[primary report](https://www.math.keio.ac.jp/~kakimura/papers/METR09-13.pdf).
For a chordal graph including all diagonals and a real symmetric
matrix zero outside it, this theorem equates PSD with an exact sum
of clique-supported PSD matrices, including singular matrices.
The source was inspected in comparison629; its Corollary2 concerning
PSD completion is not used. The standard chordal definition concerns
cycles of length greater than three. No source theorem is reproved.

## Conclusion

The entire Q has a chordal support SUPERGRAPH with 64512 maximal
cliques. No multiplier sparsity restriction is imposed. Its largest
clique order, and hence largest clique PSD obligation, is

    41,721,952,216 <= 560,302,216,152 = (p+1)m/2,
    p=548,240,915,  (p+1)m=1,120,604,432,304.             (1)

Every separate Lambda_i obligation has order m=2044. Sections3–4
give an exact entrywise reconstruction scheme on every coefficient
and fill position, including all overlap sums. With PSD factors and
the Lambda_i orders verified, it implies C999w(12) and therefore its
CONDITIONAL full-output .000999 conclusion for all original complex
endpoints. The support/count test alone does not imply that conclusion.

This passes only the relative size gate in assessment629. The largest
block still has over41 billion scalar coordinates. There are no factors,
feasible multipliers, numerical floor, implementation-cost guarantee,
actual sign result or progress beyond the inspected general method.
The result is local standard-method REPRODUCTION. The separate bounded
audit632 in Section6 upholds it with all the stated qualifications.

## Proof

### 1. Partition of every declared symbol

Put h=K-J. A core symbol is any symbol other than the following
symbols assigned to a unique high output row n with J<=n<K:

- Primitive M[n,a], 0<=a<J: J symbols.
- Primitive T[n,a] and T[a,n], 0<=a<J: 2J symbols.
- Fresh errors of V[n,:], Fplus[n,:], Fminus[n,:]: 3d symbols.
- Fresh errors of VY[n,:]: m symbols.

Denote this set by I_n. The T primitive entries are distinct here:
one index is >=J and the other <J. The J-square intersection of the
two primitive rectangles lies entirely in the core. Sharing T with
its transpose never identifies symbols in different I_n. Likewise
the symmetric M J-square is core; its high rectangle has no
transposed copy in another high row of the input registry.
The sets I_n are disjoint and each has

    q=3J+3d+m=8182 symbols.                              (2)

For completeness, the following table counts ALL declared symbols.
The last column is per high row, not a total. Symmetrized A retains
the d² symbols allocated before symmetrization. Every zero radius,
exact zero and unused declared symbol is retained.

| Family | Core count | Count in each I_n |
| --- | ---: | ---: |
| Z ratios; t0 | d+1 | 0 |
| M primitive | J(J+1)/2 | J |
| T primitive union | J² | 2J |
| U primitive | J² | 0 |
| Y primitive | dm | 0 |
| V fresh | Jd | d |
| Fplus fresh | Jd | d |
| Fminus fresh | Jd | d |
| A fresh | d² | 0 |
| B fresh | dm | 0 |
| UZ fresh | Jd | 0 |
| U0 fresh | d² | 0 |
| G fresh | Jm | 0 |
| JY fresh | dm | 0 |
| VY fresh | Jm | m |
| rminus Z; rplus Z fresh | 2d | 0 |
| re G; ro G fresh | 2m | 0 |
| Delta head fresh | Nm | 0 |

The core count c and total count are therefore

    c=20,403,731, h=64,512,
    p=c+hq=548,240,915.                                 (3)

Summing this table gives exactly C999w(10); it does not identify
distinct errors or use any numerical coefficient being small.

### 2. Support of every polynomial and multiplier term

Use “depends on a set” to mean that all affine coefficients outside
that symbol set are identically zero, without assuming nonzero
coefficients inside it. All entries of Z and Y depend only on core
symbols. For n>=J, the n-th row of M and the two T orientations
depend only on I_n (and constants). In the AA rule C999w(2), the
linear coefficient of a product is X0 Z_i+X_i Z0. A missing input
coefficient remains zero; the fresh errors are local to their output
entries. Thus V_n, Fplus_n and Fminus_n depend only on core union
I_n. Multiplication VY sums input-column indices, never output-row
indices. Consequently

    rho_n=F_n-(VY)_n depends only on core union I_n.      (4)

The fixed coefficient sums defining its fresh radii do not add noise
variables. This verifies every high row, not a sampled subset.

All primitive rows below J, all Z/Y and U entries and all fresh errors
in A,B,UZ,U0,G,JY belong to the core. Restricting V or F to rows<J
does not use high rows. Hence E0, B, Y, JY and all residual rows<J
depend only on core symbols. The head action W rho_P and Delta,
including the constants e_j in C999w(4), also depend only on core
symbols, because P retains rows<N<J. Thus rho_P and X are core-only.
All six boundary functionals use Z or G with raw rows<J, and their
fresh errors are core symbols. The tail weights, ybar, omega_K and
tbar are fixed constants. The entire infinite-tail majorant therefore
depends only on core symbols.

This exhausts C999w(9): E0, B^tY, Y^tB, sym(Y^t JY), the whole
head rho_P^tX, rows N<=n<J, the entire tail and mu I are core-only;
each remaining finite term is exactly -omega_n rho_n^t rho_n for
one J<=n<K, with dependence (4). There is no product between
different high residual rows: R is diagonal on those outputs.
No within-row endpoint, predictor or mixed term is removed.

It follows that the full polynomial P has no monomial theta_i theta_j
with i in I_n, j in I_s, n!=s. Its scalar coefficient lift C likewise
has zero entries between their endpoint fibres: for such i,j the
whole m-square C_ij is identically zero. Symmetrizing coefficient
blocks cannot create a monomial absent from every summand.

Every scalar affine equality is also core-only. Indeed JY-B uses
only A,Y,B, and HX-rho_P uses only the head objects just traced.
Write l_a=l_a0+sum_i l_ai theta_i. Then l_ai=0 for every i in I_n.
For arbitrary FULL m-square Gamma_a and Lambda_i, the blocks of Q
are exactly

    Q00=C00-sum_i Lambda_i+sum_a l_a0 Gamma_a,
    Q0i=C0i+(1/2)sum_a l_ai Gamma_a,   Qi0=Q0i^t,
    Qii=Cii+Lambda_i,                  i>0,
    Qij=Cij,                          i,j>0, i!=j.       (5)

Thus box multipliers add only within individual fibres and fibre0;
equality multipliers add only between core fibres. In particular
all Q_ij between different I_n,I_s remain identically zero. No
Gamma or Lambda is omitted, assumed diagonal, or optimized here.

### 3. Explicit scalar graph and its PSD orders

Vertices are ALL scalar indices (i,a), 0<=i<=p, 1<=a<=m. Let V_*
be fibre0 together with all core fibres, and V_n the fibres of I_n.
Use the graph whose maximal cliques are

    K_n=V_* union V_n,   J<=n<K.                         (6)

All diagonals are included. Section2 proves Q is zero outside this
graph. This is a supergraph: many entries within these cliques may
also vanish, and their zeros remain prescribed.

An explicit perfect elimination ordering first removes vertices of
V_J, then V_(J+1), and so on, in any fixed order within each group,
and finally V_*. At each removal the remaining neighbors are the
rest of that same V_n together with V_*, which form a clique.
The final core is complete. This proves chordality directly. Since
each V_n is nonempty and no edge joins different V_n, the cliques
in (6) are exactly maximal.

The core scalar order is (c+1)m=41,705,228,208 and each high-row
scalar order is qm=16,724,008. Every maximal clique therefore has
(c+q+1)m=41,721,952,216 vertices. Together with (3) this gives(1).
Each Lambda_i still has order2044, and there are p of them. Keeping
these obligations avoids claiming that clique order is the only
cost. No full coefficient matrix or scalar graph is allocated.

### 4. Exact reconstruction, including overlap and fill

Order each K_n with V_* first. Its candidate rational symmetric
clique matrix must have the form

    B_n=[[D_n, Q_(V_*,V_n)],
         [Q_(V_n,V_*), Q_(V_n,V_n)]],
    sum_(n=J)^(K-1) D_n = Q_(V_*,V_*) ENTRYWISE.         (7)

All Q entries on the right are the complete fixed coefficients (5).
Only the symmetric D_n are split across cliques. If E_n selects K_n,
then (7) is equivalent to the exact full reconstruction identity

    Q=sum_(n=J)^(K-1) E_n^t B_n E_n.                    (8)

To check this, core/core entries sum every D_n; core/V_n and V_n/V_n
entries occur in exactly one clique with their prescribed coefficients;
entries between different V_n,V_s occur in none and are identically
zero by Section2. These cases exhaust every scalar pair (i,a),(j,b).
For a zero coefficient INSIDE the graph (a fill position), the same
entrywise equation still applies with right side zero. In particular
core/core fill entries require the sum of overlap contributions to
vanish; they are not free completion entries. Assigning each B_n to
the principal submatrix Q[K_n,K_n] generally fails the overlap equation.

Apply the cited Kakimura theorem to this finite real symmetric Q and
the explicitly chordal graph (6). It gives a real PSD decomposition
if Q is PSD, including singular cases; it does not supply positivity
of this Q. Independently, to obtain C999w's exact rational certificate,
it suffices to supply rational Gamma_a, rational Lambda_i>=0 and
rational D_n satisfying (7), with every B_n>=0 proved. There is no
assumption that an optimizer returns rational feasible values or that
such values exist. A complete exact rational identity B_n=L_n D'_n L_n^t
with nonnegative diagonal D'_n is one allowed witness; each Lambda_i
requires the same kind of verified PSD identity. Singular zero pivots
must satisfy the complete identity; a factor-success flag is insufficient.

For any such witness, (8) implies Q>=0 by adding PSD forms. This is
exactly C999w(12), so its audited congruence and actual-assignment
argument gives its (1), with all outputs and the original mu metric.
Neither a completion nor positivity on some selected principal blocks
can replace(8). Nothing in this step constructs these witnesses.

### 5. Verification and remaining gap

The exact integer count check is

    python3 scripts/separation-seven/common-residual-row-clique-counts-630.py

It writes the full family-count, order and reconstruction-obligation
record to the same basename `.json`. It checks the table sum against
C999w(10) and the actual/required size bounds; it is not a coefficient
instantiation or PSD verification. Sections1–4 supply the symbolic
support and reconstruction proof, for arbitrary coefficients satisfying
the fixed graph construction. No numerical input arrays are read.

The structural test passes its stated half-order gate but provides no
practical implementation or multiplier/factor feasibility. C999w's
actual .000999 comparison remains conditional and unpaid. Preserve598's
isotropic stop,600's final-box stop and unfinished603 unchanged. The
actual remote-plus-induced coupling, higher endpoints, C744q, H2,
non-neutral coverage, input inclusion/pins, source/core/c_* validation
and global actual-Xi assembly remain open. This is not a complete RH
candidate or an off-line-zero exclusion.

### 6. Independent structural audit — 12 November2026, step632

**Verdict and admitted scope.** Under assessment630, separately approved631,
Sections1–5 pass the registry, support, exact-reconstruction and integer-order
audit. No formula, graph or mathematical input needs correction. This
validates the local specialization of Kakimura Theorem1, not a new general
theorem or a feasible PSD certificate. Its complete real singular/positive
pivot proof cases were already inspected in comparison629 and are reused;
neither completion Corollary2 nor rational feasible-point existence enters.
The conditional analytic implication remains precisely C999w Section7's.

**Complete registry reconciliation.** Checked the21 families individually
against C999w Sections1–4, rather than treating the combined table as an
independent definition. The primitive families are the d Z ratios, t0,
symmetric-low/rectangular-high M, the union of two T rectangles, full U
and full Y. Their total is p0=202892807. In particular M contributes
J(J+1)/2+(K-J)J=66585088; T contributes2KJ-J²=133169152.
The latter uses one J-square intersection, not symmetry of T. For a
high n, T[n,a] and T[a,n] are distinct primitive entries, each shared
only with its prescribed adjoint occurrence. Neither T sharing nor M
symmetry identifies symbols in different high groups.

The ten product families are V, Fplus, Fminus, A, B, UZ, U0, G, JY
and VY, of respective total sizes Kd,Kd,Kd,d²,dm,Jd,d²,Jm,dm,Km.
A retains all d² pre-symmetrization errors: averaging two entries does
not merge their identifiers. The last five families are rminus Z,
rplus Z, re G, ro G and Delta, of sizes d,d,m,m,Nm. Their first four
are formed once, with repeated endpoint rows subsequently reused. Thus
all21 families, including exact-zero and unused symbols, are accounted
for. The product-family sum is344295448; boundary and head additions
are6132 and1046528, respectively. These give p=548240915.

Independently group the common contributions as

    c=(d+1)+J(J+1)/2+2J²+3dm+4Jd+2d²+2Jm+2d+2m+Nm
      =20403731.

Each high row contributes exactly3J primitive symbols,3d fresh V/F
symbols and m fresh VY symbols. Thus q=8182 and c+(K-J)q agrees
with C999w(10). This reconciliation checks the allocation rule, not
just the addition of the numbers in the saved certificate.

**All affine nodes and coefficient support.** For a product output(n,b),
the linear part in C999w(2) sums only over the input-column index.
Its old-symbol support is contained in the union of the supports of
the entries actually read in that row. Its fresh error belongs to that
output entry. All sums of coefficient absolute values defining radii
are fixed rational constants; they introduce no hidden dependence on
symbols from other rows. Consequently V_n and both F orientations use
only core union I_n, and VY_n uses those same symbols plus its own
row's fresh errors. Subtracting gives the stated support of rho_n.

For low rows, V/F use only the core M/T entries and Z. Therefore A,B,
UZ,U0,G and JY are core-only, as are E0 and every signed energy term
in C999w(9). The head uses rho_P with P below N<J; its fixed W,
fixed H and new Delta errors preserve core support. All four boundary
products use Z or G and the shared core t0. Hence the six tail rows,
their exact weighted quadratic product, and the fixed tbar/omega_K
terms are core-only. This checks the entire tail expression, not an
output sample. The only high-row products left in (9) are the separate
rho_n^t rho_n. R has no cross-row term there. Symmetrization and the
specified coefficient lift therefore cannot create a cross-I_n/I_s
coefficient for n!=s.

Both sets of affine equalities, JY-B and HX-rho_P, are core-only.
Formula(5) follows entry by entry from C999w(12). A full high-symbol
Lambda_i contributes both its high-fibre diagonal and -Lambda_i in
Q00; the latter is in the common core and has NOT been dropped.
Full Gamma_a contributes only00 and0i/i0 for core i. Thus unrestricted
endpoint-mixing multipliers respect the claimed scalar supergraph.
No small radius, interval containing zero, or floating center was used
as a structural zero.

**Chordality and reconstruction.** Since h=64512>1 and q,m>0, the
disjoint nonempty high groups and common core have exactly the maximal
cliques (6). Eliminating a high vertex leaves as neighbors only its
own remaining group and the complete core; this verifies every step
of the perfect elimination order. All diagonal entries are included.
The four exhaustive scalar-pair cases are core/core, core/high, same
high group, and distinct high groups. Equation(7) sums the first,
fixes each of the next two in its unique clique, and leaves the last
identically zero. Transposes give the reversed cases. This proves(8)
on every scalar entry, including all prescribed zeros inside the
supergraph. Core fill entries require cancellation of the overlap sum;
they are not free variables of a PSD completion. Applying the source
to this fully specified real symmetric Q is legitimate even if Q is
singular. It neither proves Q>=0 nor makes its clique factors rational.

**Exact replay and both order obligations.** Ran the Section5 command632
and inspected the COMPLETE registry_families, parameters, counts, orders,
symbolic_support, exact_reconstruction_obligations,
no_witness_or_floor_established and failures fields of
`scripts/separation-seven/common-residual-row-clique-counts-630.json`.
Used `python3 ../scripts/loop/inspect_json.py <certificate> --pointer
/<field> --full` for these selected fields, not bounded previews as
evidence. The replay reports no failures. Independent multiplication
gives core order41705228208, high-group order16724008 and clique
order41721952216. The full order is1120604432304, so twice the clique
order83443904432 is at most1120604432304. Each of the p additional
Lambda obligations has order2044, also below560302216152. These are
only size checks; the strings describing support/reconstruction in the
JSON do not prove the preceding hand-checked statements.

**Conditional implication and limits.** If rational multipliers and
symmetric rational D_n satisfy every entry of(7), and complete exact
factor identities establish every B_n>=0 and every Lambda_i>=0,
then(8) makes precisely C999w(12) PSD. Full identities remain required
at singular zero pivots. C999w Section7 then supplies its unchanged
actual-assignment, real-to-complex, original-metric and strong-trial
implication for all finite and infinite outputs. No new analytic tail,
solve inclusion, domain or physical-input claim is supplied by this
audit.600's inclusion/pins and analytic/IEEE754/Decimal/core/c_* contracts
remain hypotheses. No factors or .000999 floor have been verified;
the largest block still exceeds41 billion coordinates.598/600 stops,
unfinished603, and the independent gaps in Section5 persist. The DAG's
sole direct mathematical input remains C999w; no argument change in
PROOF.md or dependency change is needed. Mathlib status is unchanged.

## Mathlib

Full matching coverage for this registry-specific support partition,
clique reconstruction and actual response certificate has not been
checked. The cited primary theorem supplies the general real PSD
decomposition; no matching Mathlib theorem, absence or formal verification
is asserted. The count script does not establish Mathlib coverage.
