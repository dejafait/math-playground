# L055 — Free triples cannot repair the full-incidence distance-five slice

## Hypotheses

Use L053's universe V of all 68-subsets of the 1024-point domain H and
its fixed rational singleton rho>0 and pairs rho*p_i. In particular
p_0=1, p_1=...=p_4=0 and

  p_i=a_i/(2 binomial(68,i)binomial(956,i)), 5<=i<=68,

where a_i is L053's imported L021 primal. Let x be a real function on
unordered support families of cardinality at most three. Require
x(empty)=1, x({A})=rho, and x({A,B})=rho*p_i for distinct A,B at
half-distance i. Boolean repetitions use their lower-order moments.
Every coordinate is nonnegative. A distinct triple has moment zero
if it contains a pair at half-distance 1,...,4, or if its common part
has size 61, each pair-only part size two and each private part size three.
This **entire incidence zero**, including realizable L020 cases, is a
trial restriction; it is not asserted for arbitrary RS lists.

For each A require PSD of the entire union matrix with indices {A}
and {A,B} for all B satisfying |A\B|=5. The approved slice also requires
all three-index union matrices {A},{A,B},{A,C}, with duplicate indices
removed, at all anchors. Off-shell triple coordinates are globally free;
no product formula, complement PSD, extra scalar inequalities, or
four-support moments are assumed.

## Conclusion

No such x exists. The full distance-five shells alone contradict the
fixed pairs and stated zeros, even with all other triples free. After
the normalization below, an exact dual gives a shell row-sum upper bound

  1143872642/5,

whereas its constant Schur coordinate requires at least

  4982733184/5.

The strict gap is 3838860542/5. This excludes the approved restricted
class, rather than just L054's product assignment. It does not exclude
extensions that relax the entire incidence zero, different pairs, or the
general labeled RS program. No uniform list upper bound, unsafe list or
improvement of the 955–957 bracket follows. The independent arithmetic
reconstruction and the separate critical proof review below retain this
restricted exclusion.

## Proof

**Imported tools and why averaging is legitimate here.** Import the union
matrix definition and constraint-preserving averaging from Sven C. Polak,
*Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and its indicator proof, printed p. 2,
and Section 1.2, p. 3. The endpoint qualification is recorded in
[foundations/12](../foundations/12-global-degree-three-moment-source.md).
No hierarchy theorem is reproved. The matching prior SPECIALIZE gate is
`drafts/literature/2026-10-12-free-triple-five-shell-feasibility.md`.

For a permutation sigma of the 1024 underlying points, put
x_sigma(D)=x(sigma(D)), where sigma acts on every support in D. Fixed
singletons, pairs and Boolean repetitions are preserved because support
sizes and pair intersection sizes are preserved. Both types of zeros
are preserved because all seven occupied region sizes are preserved,
up to permutation of the supports. Nonnegativity is preserved. The shell
at A maps bijectively to the shell at sigma(A), and its union matrix
is the latter matrix with rows and columns relabeled. The same holds for
every retained principal matrix, including repeated indices. Thus every
x_sigma satisfies all the hypotheses. Their finite average is a feasible
invariant function if any feasible x exists: PSD and nonnegative cones
are convex and all fixed coordinates remain fixed. This averaging does
not apply to the different actual-label nonsingularity constraints.

We may therefore assume x invariant under all point permutations. No
independent per-anchor triple assignment is introduced. In the argument
below we even relax any identifications among its shell coefficients;
an obstruction for those relaxed coefficients still excludes x. No
off-shell coordinate is prescribed or used.

**Shell entries and complete spectrum.** Fix A. Reuse L054's bijection
B=(A\X) union Y with |X|=|Y|=5, X contained in A and Y in H\A.
For C=(A\X') union Y', put r=5-|X intersection X'| and
q=5-|Y intersection Y'|. The shell is J(68,5) x J(956,5), with

  S=binomial(68,5)binomial(956,5)=68643272053310642688.

Its stabilizer acts transitively on ordered B,C with a fixed (r,q).
All 36 relations exist. L054's complete region dictionary gives the
diagonal at (0,0), forbidden distances at 1<=r+q<=4, and the entire
incidence zero exactly at (r,q)=(2,3). Thus put

  R={(r,q): 0<=r,q<=5, r+q>=5, (r,q)!=(2,3)},

which has 20 members. The normalized shell block D, obtained by dividing
the actual block by rho*p_5, has coefficient one at (0,0), zero at the
specified zero relations, and free coefficient
d_rq=x({A,B,C})/(rho*p_5)>=0 at each relation in R. Invariance gives
one value on each relation. This uses only nonnegativity, not an extra
upper or Frechet constraint. The complete anchored matrix divided by rho is

  [1, p_5*1^T; p_5*1, p_5*D].

Import the Schur congruence and simultaneous Johnson eigenspaces already
used in L054: Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), p. 36, Sections 1.4.7 and 11.2, pp. 19,162–163;
and Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Sections 1.2,
3 and 3.4, pp. 3,10,12. Both factor parameters satisfy n>=2*5.
Their full spectra, positive multiplicities and identity relation are
retained. The source details are in
[foundations/09](../foundations/09-global-pair-johnson-source.md).

After Schur congruence with the positive top entry one, and division by
p_5>0, anchored PSD requires D-p_5*J PSD. For a factor of size n, write

  E_a^(n)(r)=sum_(h=0)^r (-1)^h binomial(a,h)
                  binomial(5-a,r-h)binomial(n-5-a,r-h).

The relation valency is E_0^(n)(r)=binomial(5,r)binomial(n-5,r),
and every factor mode 0<=a<=5 has positive multiplicity
binomial(n,a)-binomial(n,a-1). Product modes exhaust the shell. Set

  v_rq=E_0^(68)(r)E_0^(956)(q)>0,
  z_rq=v_rq*d_rq>=0,
  H_ab(r,q)=E_a^(68)(r)E_b^(956)(q)/v_rq.

For the 35 nonconstant modes, necessary PSD is exactly

  sum_((r,q) in R) -H_ab(r,q)*z_rq <= 1.                 (1)

The constant projector is J/S, so its Schur coordinate requires

  1+sum_((r,q) in R) z_rq >= S*p_5=4982733184/5.         (2)

The equality uses the fixed p_5 from L053, not a candidate triple value.
Singular PSD blocks are permitted throughout. The retained small-principal
constraints are not needed for the contradiction; dropping them only
enlarges this necessary shell relaxation.

**Explicit rational dual.** Assign the following nonnegative weights to
the indicated inequalities (1), and weight zero to every other mode:

| Mode (a,b) | Weight omega_ab |
|---|---|
| (0,1) | 60547/159 |
| (0,2) | 7197485/159 |
| (1,0) | 12663/325 |
| (1,1) | 255568887/17225 |
| (1,2) | 6076116837/3445 |
| (2,0) | 99603/160 |
| (2,1) | 2010220947/8480 |
| (2,2) | 47792739897/1696 |
| (3,0) | 45230829/10400 |
| (3,1) | 912863667821/551200 |
| (3,2) | 21703214217671/110240 |

For every one of the 20 relations in R, exact substitution in the finite
binomial formula verifies

  sum_((a,b)!=(0,0)) omega_ab*(-H_ab(r,q))=1,            (3)

and the sum of the displayed weights is 1143872637/5. The complete
twenty-column record is saved in the audit certificate's `dual_columns`;
each coefficient is exactly 1 and each slack is exactly 0. These equations
and the displayed formulas are also a finite certificate independent of
any solver's correctness or status. Multiply (1) by these nonnegative
weights and sum. Equation (3) gives sum z_rq<=1143872637/5. Consequently

  1+sum z_rq <= 1143872642/5 < 4982733184/5,

contradicting (2). This disproves existence of the invariant averaged
point, and hence of any point satisfying the hypotheses. Even potentially
inconsistent independent shell coefficients cannot satisfy this subset
of constraints, so imposing all global unordered identifications and
all three anchors cannot repair the contradiction.

**Full exact evidence and verification.** From the active notebook run

  `python3 scripts/finite-support/free_triple_five_shell.py`

then

  `python3 scripts/finite-support/audit_free_triple_five_shell.py`.

The constructor uses a bounded 140-digit Decimal simplex only to propose
a basis (27 pivots, cap 600), then reconstructs every primal and dual
entry by rational elimination. Its certificate is
`scripts/finite-support/free-triple-five-shell-results.json`, containing
all 700 coefficients, 20 primal values, 35 dual weights and every slack.
An exact feasible primal attains the same shell LP objective, but neither
this primal nor its sharpness is needed for infeasibility of the slice.
It is not a global feasible point or a representing distribution.

The independent verifier imports no constructor routines. It rebuilds
the unchanged pairs from the L053 input and checks all 64 L021 defining
equations. Factor eigenvalues are reconstructed by Schrijver's full source
beta summation, Theorem 1 (51), III.A (53)–(58), pp. 6–7 of the
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf), using
factorial binomials. All 72 factor values agree with the Johnson formula;
all 72 trace-orthogonality equations, positive multiplicities, valencies
and the full product dimension are checked. Actual support sets recover
all 36 relations and both zero cases; their six support permutations
preserve the zero restriction. This numerical check corroborates the
general group-invariance argument above; it does not replace that argument.

Every one of the 700 LP coefficients is checked independently, as are
every primal/dual sign, all 35 primal spectral inequalities, all 20 dual
equations (3), the dual objective, the exact required row sum and its
strict shortfall. The report
`scripts/finite-support/free-triple-five-shell-audit-results.json` saves
the full reconstructed factors, actual set dictionaries, all twenty dual
column values, sparse dual, exact bound and gap. All 1318 checks pass with
no failures. The proof uses this complete finite arithmetic and the
explicit symmetry argument, not a bounded JSON preview or solver status.

**Qualifications and route decision.** This is a local reproduction of
assessed moment/spectral methods. The inspected sources do not supply the
specific finite verdict; no originality beyond them is claimed. L053's
small-principal nonexclusion and L054's fixed-product failure are preserved.
The free-triple repair at these pairs with this entire incidence zero is
now excluded. Retain the independent missing safety at 67/68 agreements,
other pairs, relaxing the trial zero, the full labeled program, representing
measures and RS realization. The separate critical audit below verifies
this manuscript's source applicability and load-bearing steps.

**Separate critical proof review (2026-10-12, step 180).** Reuse the
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-12-free-triple-five-shell-critical-audit.md`.
The primary imports above and their qualifications in foundations/04,09,12
cover this exact audit; no new spectral or hierarchy theorem is needed.
The review retains the conclusion. The following checks explicitly connect
the finite certificate to every feasible assignment in the hypotheses.

First, the domain H is being used as a 1024-element set here. Its full
permutation group acts on V and on unordered families of supports.
For each permutation sigma, the map I -> sigma(I) is a bijection from
the matrix indices at A onto those at sigma(A), and
sigma(I union J)=sigma(I) union sigma(J). Thus the matrices of x_sigma
are permutation congruences of required matrices of x. The hypothesis
requiring every anchor, rather than only one preselected anchor, is
essential. Boolean repetition, nonnegativity, all fixed pairs, forbidden
pair distances and all seven occupied-region sizes survive this action.
Consequently finite averaging preserves the complete stated slice.
The averaged coordinates still form one function on unordered families;
no independence among different anchors is presumed. Actual subgroup
determinants are absent from these hypotheses, so their failure to be
invariant under arbitrary permutations is irrelevant to this exclusion.

Second, after choosing A the stabilizer is S_68 times S_956. An ordered
pair X,X' of head five-sets splits A into regions of sizes
(5-r,r,r,63-r), while the tail regions have sizes
(5-q,q,q,951-q). Given another pair with the same r,q, choose bijections
between corresponding regions and combine them into permutations of A
and its complement. This proves transitivity on each product relation,
including r=0 or q=0. All regions are nonnegative for all 36 choices,
so none of the product relations is fictitious. The dictionary gives
one Boolean diagonal, fifteen zero relations and twenty free relations.
Additional identifications resulting from unordered support families can
only shrink this coefficient space. The proof excludes the enlarged
space, and therefore needs no extension of independent shell variables
to off-shell triples. Nonnegativity and the dropped principal constraints
are never used to assert that such an extension exists.

Third, exact reconstruction gives p_5=1/68881143660>0 and
rho=(U+1)/(2 binomial(1024,68))>0. For B=C the union coordinate is
x({A,B})=rho*p_5, not a distinct-triple moment. The anchor diagonal is
rho and every anchor/shell entry is rho*p_5. Thus division by rho gives
exactly [1,p_5*1^T; p_5*1,p_5*D]. Schur congruence gives
diag(1,p_5*D-p_5^2*J), and the positive factor p_5 yields D-p_5*J.
No shell inverse is taken. The constant eigenvalue of J is S and the
other 35 product modes have eigenvalue zero for J. The diagonal I has
eigenvalue one on every mode. Hence both the sign in (1) and the factor
S*p_5 in (2) are correct; using S*p_5^2 here would be incorrect.
Both Johnson factors satisfy n>=10, all 36 mode multiplicities are
positive, and their sum is exactly S. Identity relations and singular
lower blocks are covered by the cited source statements.

Finally, the independent beta reconstruction was rerun and all 1318
checks pass. The separate command

  `python3 scripts/finite-support/critical_audit_free_triple_five_shell.py`

reads the eleven weights directly from this manuscript, gives zero weight
to each of the other 24 nonconstant modes, and compares all 35 values
with the saved rational dual. It independently substitutes the displayed
Johnson formula in all 700 coefficients, checks all 20 weighted column
identities, and reconstructs the full relation dictionary, positive mode
dimensions, p_5 and both constant bounds. All 967 checks pass. The complete
report is `scripts/finite-support/free-triple-five-shell-critical-audit-results.json`;
it includes every mode's contribution to every column and hashes of the
full arithmetic inputs. Complete failure lists, the exact p_5 value and
all twenty reconstructed column values were inspected; no solver rerun
or floating-point verdict is used. The optional primal optimum remains
unnecessary. Summing the valid nonconstant inequalities with the displayed
nonnegative weights proves the strict row-sum contradiction exactly.

This is completed local verification of L055, not a new theorem beyond
the assessed methods or a uniform bound over pair choices. The full
incidence zero still includes realizable configurations. Removing that
trial restriction, changing pairs, the general labeled program,
representing measures, common-center lists, and 67/68-agreement safety
remain outside this conclusion. No argument or DAG input was changed.

## Mathlib

Full matching theorem, product Johnson spectra, moment hierarchy and
Schur-complement coverage: not checked. Supporting finite-set/linear-algebra
coverage: not checked. Unknown availability is not evidence of absence.
