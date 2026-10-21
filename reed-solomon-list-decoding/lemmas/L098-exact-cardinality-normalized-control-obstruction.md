# L098 — Exact-cardinality contractions reject the normalized frozen control

## Hypotheses

Use L021–L023's constant-weight parameters n=1024,w=68,v=956,d=10,
and their entire original-orbit assignment z=(p,y), including all
L023 untouched-orbit values. Put

    T=65537^28/2^128, N=floor(T)+1,
    U=binomial(1024,64)/binomial(68,64), M=(U+1)/2,
    alpha=(N-1)/(M-1).

The normalized singleton assignment e has p_0=y_00^(0,0)=1 and every
other actual-orbit value zero. The prescribed control is
z_c=alpha*z+(1-alpha)*e. This fixes the control; no parameters or
constraints are optimized. Keep all original admissible (i,j,t,s),
the invariant t-s, repeated words and forbidden distances. Impossible
multinomial orbits are absent, as in foundations/04. The inherited
constraints are all original scalar and basic pair rows, L097's unchanged
166 matrices, and L023's two complete zero-index matrices. Other source
PSD matrices are not asserted feasible.

For the RS application use L021's field/domain and degree-less-than-64
tuple messages, arbitrary center, any interleaving width m>=1 and
at least 68 simultaneous agreements. No actual-label averaging is used.

## Conclusion

Every actual exact-N binary constant-weight code of these parameters
necessarily satisfies, for i=0,...,68,

    sum_(j,t,s) D(i,j,t,s) y_ij^(t,s) = N p_i,                 (1)
    D(i,j,t,s)=binom(i,t)binom(68-i,j-t)
               binom(i,s)binom(956-i,j-s),

where j ranges from 0 to 68 and (t,s) over its full actual-orbit ranges.
The equation is homogeneous in the nonempty Boolean moments; there is
no division by p_i. At i>0 the two repeated third words each contribute
p_i. At i=0, (1) is exactly the source objective identity.

The control has objective exactly N, with 0<alpha<1, and passes every
inherited constraint above. Nevertheless all 64 rows i=5,...,68 violate
(1), with the strict exact bounds

    1383/1000 < (sum D y_c)/(N p_c,i) < 1384/1000.          (2)

Thus every such residual is positive, while the i=0 and forbidden-distance
i=1,...,4 controls are zero. The exact-cardinality equations are additional
necessary conditions not implied by this inherited relaxation even on its
objective-N slice. This is a known-method specialization and a fixed-control
obstruction, not a uniform upper bound or rejection of other assignments.
It gives no packing, RS list, safety/unsafety statement or improvement of
the 955–957 bracket. The separate critical audit below retains this
fixed-control obstruction.

## Proof

**Known inputs and scope.** Import Raghavendra–Tan, *Approximating CSPs
with Global Cardinality Constraints Using SDP Hierarchies*,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
Definitions 3.1,3.3 p. 7, conditional-cardinality display p. 8 and its
qualification p. 9. The finite Boolean universe here consists of all
H=binomial(1024,68) supports, with prescribed fraction N/H, not the
1024 evaluation positions. No rounding theorem or global representing
distribution for relaxed marginals is imported. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Proposition 1.1
and its complete indicator proof p. 2, Section 1.2 p. 3, supply the
constant-weight indicator necessity and unlabeled averaging context;
retain the printed A(n,d) versus proved constant-weight qualification.
The normalization is Schrijver, *IEEE TIT* 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (60),(62)–(66), p. 7, cross-checked in Kim–Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), (31)–(35),
pp. 8–9. The qualified complement prefactor in Schrijver (61) is unused.
Foundations/04,12,13 record the inspected hypotheses and proof cases.
These sources supply the method; the repeated-index conversion and
finite-control computation below are needed specializations, not a
reproof of a hierarchy or block diagonalization theorem.

**Exact-N reduction and homogeneous equation.** If an arbitrary-center
tuple list at 68 agreements exceeded T, its integer cardinality would be
at least N. Retain exactly N distinct candidates. Choose 68 agreement
columns from each. By L001 any common 64 selected columns force all
row-wise differences to vanish, so the supports are distinct, intersect
in at most 63 points and have binary distance at least 10. Extra agreements
and arbitrary m cause no change. Thus exact-N support codes are a necessary
test for safety, not a sufficient condition for an RS realization.

For an exact-N support code C and indicator variables X_A=1_(A in C),
the pointwise Boolean identity is

    sum_Z X_A X_B X_Z = N X_A X_B.                         (3)

Indices range over the whole support universe and include Z=A,B.
It remains true for A=B and for an absent pair. Averaging (3) over all
coordinate permutations is legitimate for this ordinary code condition.
It uses no assertion that labeled RS restrictions are permutation invariant.
Equivalently, multiplying the cited conditional-cardinality condition
for the assignment X_A=X_B=1 by its probability gives (3) in moments.
At zero pair probability the homogeneous expression remains defined:
every triple probability is zero by containment. No division by that
probability is required, and no arbitrary relaxed assignment is presumed
to satisfy cardinality merely from local consistency.

Write x(S)=E product_(A in S) X_A after this averaging and s_0=N/H>0.
The source orbit normalization gives x({A})=s_0,
x({A,B})=s_0*p_i, and x({A,B,Z})=s_0*y_ij^(t,s).
Indeed there are H*g_i ordered pairs at half-distance i, with
g_i=binom(68,i)binom(956,i), and H*G_ij^(t,s) ordered triples in an
orbit, where

    G_ij^(t,s)=multinomial(68;i-t,j-t,t)
                multinomial(956;i-s,j-s,s).

The source counts inside C are respectively N*g_i*p_i and N*G*y.
These formulas also hold when indices repeat: Boolean products refer
to sets of variables. Divide the averaged (3) by s_0, which is positive,
not by p_i.

Fix A,B at half-distance i. Its four regions A\B,A intersection B,
B\A, and the complement of A union B have sizes i,68-i,i,956-i.
For Z at half-distance j from A, its removal from A selects t elements
of A\B and j-t of A intersection B. Its additions select s elements
of B\A and j-s of the complement. These independent choices give exactly
D in (1). Nonnegative region sizes are precisely the actual-orbit ranges
max(0,i+j-68)<=t<=min(i,j), max(0,i+j-956)<=s<=min(i,j).
Their third distance is h=i+j-t-s. Direct factorial cancellation yields
G=g_i*D, matching the two source multinomials without approximation.
Grouping (3) by these regions proves (1).

For i>0, Z=A is (j,t,s)=(0,0,0), and Z=B is (i,i,i); each has D=1
and y=p_i. For i=0, t=s=0 and D=g_j, with y=p_j; hence the equation is
sum_j g_j p_j=N. Distances 1,...,4 have every y zero, so their equations
are zero identities in a distance-10 code. Forbidden and impossible
orbits are therefore handled differently and neither is silently dropped.

**Normalization and inherited feasibility at this same control.** L021
fixes the positive rational a_i and L022 gives p_i=a_i/(2*g_i) for i>=5,
p_0=1,p_1=...=p_4=0,lambda=p_68>0. L023 extends y to every actual orbit:
forbidden distance gives zero; a repeated word gives the corresponding
p_b; otherwise y=p_i*p_j*p_h/lambda. Its objective is M=(U+1)/2.
L097's strict integer endpoint gives M>N, and N>1. Consequently
0<alpha<1 and the affine source objective at z_c is
alpha*M+(1-alpha)=N. In particular this test is not a failure of the
objective or an attempt to apply fixed-size sampling to nonintegral M.

The normalized singleton e is an actual singleton-code assignment in
the source convention. Its scalar inequalities follow directly:
y is one only for three equal words, p_i is one only at distance zero,
and all remaining values are zero. L023 supplies every scalar row for z;
these rows and the source pair inequalities are affine. Each pair spectral
slack at e is 1; its mixed slack is alpha*slack_z+(1-alpha)>=0.
All scalar slacks likewise mix with nonnegative endpoint slacks.
Both endpoint formulas are symmetric in the complete distance multiset,
so every required t-s-preserving source equality holds in their mixture.
This does not identify different free t-s variables.

For completeness the singleton matrices can be seen explicitly in the
source blocks of labels (k,l). The included-anchor matrix is zero except
for an entry 1 at (i,j)=(0,0) when k=l=0 and that index is retained.
For the complemented family only h=0 survives; then i=j,t=s=i. Its
diagonal is

    binom(68-2k,i-k)binom(956-2l,i-l)
       - 1_(k=l=i=0),

which is nonnegative. This uses beta_(ii,k)^(i,68) and the distinct
label-l factor exactly, not a deleted zero-label coefficient. L097
and L023 provide full exact congruence certificates E^T A_z E=D_z
with E invertible and D_z nonnegative for all inherited matrices,
including every transformed entry at zero pivots. The present script
checks those complete frozen identities and the singleton diagonals
again. As source matrices are affine, their control matrices are
alpha*A_z+(1-alpha)*A_e, hence PSD by nonnegativity of both quadratic
forms. No new solve, old-block optimization or larger support is used.

**Complete exact computation.** Run from this notebook:

    python3 scripts/finite-support/fixed_cardinality_normalized_control.py
    python3 scripts/finite-support/verify_fixed_cardinality_normalized_control.py

The first writes `scripts/finite-support/fixed-cardinality-normalized-control-results.json`.
It records all endpoint input hashes, exact N,M,alpha,p,p_c, all 168
control matrices and singleton diagonals, all pair coefficients/slacks,
and every contraction lhs,rhs,residual. Every ordered (i,j) record saves
the full t,s ranges, the two integer factor arrays whose outer product
is every individual D, both source multinomial arrays, every h aggregate
and exact orbit multiplicity. This is a lossless factored coefficient
certificate, not a sampled list or an assertion that different t-s
variables agree in the relaxation. Every individual product coefficient
is independently checked by counting included Z points in the four
regions, using factorial binomials and complementary inside weights.
All 4761 ordered entries and all 1500625 actual ordered orbits are covered.
For each i the coefficient sum counts all binomial(1024,68) third supports.

Scalar values and three exact slacks are saved with common positive
denominators for every (i,j,h) value and its exact t,s multiplicity.
The code checks the value, all endpoint and mixed slack signs, and their
convex identities. This covers all 4501875 scalar rows, including 205
repeated and 10232 forbidden orbits. All 68 pair rows and all 168 complete
frozen PSD congruences pass; there are no construction or inherited-control
failures. Normalization and objective N are checked before discrimination.

The independent verifier imports no generator routine. It reconstructs
every source multinomial by factorials, checks all 1500625 products and
every h sum, and independently reevaluates all scalar values and slacks.
For each ordered entry, summing D*y_z and multiplying by g_i reproduces
the complete corresponding frozen L023 included-anchor matrix entry.
This compares the new four-region counts with the independently audited
source beta construction, not only with another spelling of D. Likewise
the mixed sums reproduce every control matrix entry.

As a second reconstruction of each complete contraction lhs, it uses

    lhs_i = [alpha*sum_j A_z,ij + (1-alpha)*1_(i=0)]/g_i,

where A_z is the frozen full included-anchor zero-index matrix. All 69
row values and residuals agree exactly with the direct third-support
sums. Full independent evidence is
`scripts/finite-support/fixed-cardinality-normalized-control-verification.json`.
All nonzero-row residuals are positive and satisfy the strict integer
cross-multiplications in (2), while rows 0,...,4 vanish exactly. The full
rational residuals, not numerical eigenvalues or decimal approximations,
are the certificates. No verification failures occurred.

This proves the stated nonimplication on the objective-N slice: a single
assignment satisfying every inherited constraint violates necessary
exact-N equations. It does not show that those equations exclude any
other assignment, bound their joint optimum or control an RS list.
The original L097 stop and all ancestral Schur stops remain valid.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-fixed-cardinality-normalized-control.md`;
the completed work is REPRODUCTION of assessed known methods, without
an originality claim.

**Separate critical audit (2026-10-20, step 362).** The prior
`drafts/literature/2026-10-20-l098-critical-audit.md` approves exactly
this audit. The support reduction uses injectivity on 64 columns, not
a projection of tuple messages. Selecting exactly N candidates is
legitimate since the finite list has integer cardinality greater than T.
Averaging actual indicators gives (3), including absent pairs; the sole
division is by N/H>0. At a null pair, containment makes every triple
term zero. At A=B the Boolean product has one variable, and (1)
becomes the objective. For A distinct from B, Z=A and Z=B are two
distinct summands, each with coefficient one. No cardinality conclusion
is inferred from local consistency alone.

For the singleton included-anchor endpoint, only i=j=t=s=0 can
contribute, requiring k=l=0. In the complemented family h=0 and
t,s<=min(i,j) force i=j=t=s. In beta_(ii,k)^(i,n), all terms except
u=i vanish: u<i gives binom(u,i)=0, while u>i gives
binom(n-k-u,i-u)=0. The surviving term is binom(n-2k,i-k).
The all-zero triple is subtracted only when k=l=i=0. This verifies
every stated singleton diagonal, including zero rows, with both
ordered beta labels. Convexity uses the same alpha in every affine
source matrix and scalar row and asserts no representing measure.

The original contraction verifier reconstructs the coefficients and
residuals independently but copies its inherited-control summary from
the constructor. That copied field alone is not an independent check.
The endpoint source auditors were therefore replayed to new outputs,
preserving the originals:

    python3 - <<'PY'
    import sys
    from pathlib import Path
    sys.set_int_max_str_digits(0)
    sys.path.insert(0, 'scripts/finite-support')
    import verify_free_pair_shell_batch as batch
    import audit_full_zero_blocks as full
    import verify_fixed_cardinality_normalized_control as contractions
    for module, filename in [
        (batch, 'fixed-cardinality-critical-batch-source.json'),
        (full, 'fixed-cardinality-critical-zero-source.json'),
        (contractions, 'fixed-cardinality-critical-contraction-replay.json'),
    ]:
        module.OUT = Path('scripts/finite-support') / filename
        module.main()
    PY
    python3 scripts/finite-support/audit_fixed_cardinality_normalized_control.py

The first two source replays reconstruct all retained coefficients and
all 168 endpoint matrices and multiply every congruence entry, including
transformed zero rows. They check invertibility and every diagonal sign;
the PSD flags do not supply the proof. The third replay reconstructs
all 1500625 coefficient products, all 4761 included-anchor source
entries and all 69 complete residuals independently of the constructor.
All three replays pass without failures. Both original fixed-cardinality
certificates are inspected in their full relevant scope, with every
original verification row compared against its reconstruction.

The additional audit imports no constructor routine. It reconstructs
p from L021's rational vector, checks all 64 defining equations and
68 pair rows, N,M,alpha and objective N, and verifies the frozen input
hashes. It checks all 11122 ordered entries of the 168 stored control
matrices against their exact affine mixtures, all singleton diagonals
and all endpoint pivots. It checks the 164289 ordered distance-value
records, all endpoint/control scalar signs and convex identities,
with complete multiplicities covering all 4501875 original scalar rows.
The coefficient replay checks that these records cover every original
orbit; equality of numerical values at different t-s does not identify
variables. Both endpoint formulas are symmetric in the distance
multiset, so every permissible source permutation retains its value.

Every factor array, shell count, support-universe count, repetition
record, original verification residual and recorded ratio is checked.
Rows 0,...,4 have zero residual, and rows 5,...,68 have positive residual
with the strict bounds (2). The new audit passes 355467 checks without
failures. Complete hashes, endpoint diagonals, all 69 residuals and
exact minimum/maximum ratios are in
`scripts/finite-support/fixed-cardinality-critical-audit.json`.
Use `PYTHONINTMAXSTRDIGITS=0` with the shared JSON inspector: some exact
pivots exceed its default integer conversion limit.

This retains only the stated necessity and frozen-control nonimplication.
It supplies no uniform fixed-cardinality infeasibility, larger-relaxation
optimum or safety result. The frozen diagnostic is complete; other
assignments and earlier stops retain their original scope.

## Mathlib

Full matching fixed-cardinality Schrijver specialization, hierarchy
theorem and finite control certificate: not checked. The primary results
above are imported with their qualifications; Boolean indicator counting,
factorial identities, affine convexity and exact rational checks provide
the local specialization. Unknown coverage is not evidence of absence.
