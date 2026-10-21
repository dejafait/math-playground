# L059 — One distance-six column is compatible with the full shell kernel

## Hypotheses

Use the 1024-point set H, 68-subset universe, positive singleton rho and
fixed pairs rho*p_i of L053. Fix D,G with |D\G|=6. Retain L056's complete
anchored distance-five shell, with indices {D} and {D,E} for all |D\E|=5,
at exactly its audited coefficients. Add the index {D,G}. Its diagonal
and entry against {D} are both rho*p_6. For each distinct triple D,E,G,
retain L056's unordered moment whenever it is represented by a
distance-five shell; retain zero when E,G have half-distance 1,...,4;
all other new triple entries are free nonnegative real numbers.

Only this ordinary unlabeled slice and the necessary kernel condition
are tested. No extra actual-label nonfaces, extra scalar upper bounds,
L053's old trial on free triples, or fourth-order entries are imposed.

## Conclusion

For every such D,G there is a complete rational nonnegative column
satisfying every fixed entry and annihilating the full kernel of the
retained anchored shell. The explicit column below provides one witness.
Thus the necessary kernel test alone cannot exclude this fixed partial
prescription. Its 36 invariant coordinates consist of 21 free, five
represented and ten forbidden entries; the complete kernel imposes
20 independent equations on the free coordinates. Nonnegativity leaves
a nonempty interval, and the displayed witness uses its lower endpoint.

This is a local reproduction/specialization of known spectral and
singular-matrix tools, not a result beyond the checked sources claimed
as original. It is not a PSD completion: the scalar generalized-Schur
energy inequality is untested. Other moments, global and labeled
feasibility, representing measures and RS realization remain unresolved.
There is no change to the 955–957 boundary or the 67/68-agreement gap.
The separate critical proof review below retains this conclusion.

## Proof

**Known inputs and applicability.** The prior SPECIALIZE gate is
`drafts/literature/2026-10-13-full-shell-nullspace-extension.md`.
Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum (27 February 2026),
DOI 10.1007/s44146-026-00231-y,
[Section 2, Theorem 2.6 and Corollary 2.2](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For a finite real symmetric matrix [A,B;B^T,C], PSD requires C PSD
and B annihilating ker C; together with the scalar/block energy condition
A-B C^dagger B^T PSD these conditions are sufficient. Here C is the
retained anchored shell and A=[rho*p_6]. Only the kernel part is tested.
The singular case is included; no inverse of C is assumed.

The union-index program is Polak, *Semidefinite Programming Bounds for
Constant-Weight Codes*, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 (1)–(3), Proposition 1.1 and its indicator proof, p. 2,
with the A(n,d,w) qualification in foundations/12. Nonnegative coordinates
are explicit in Brouwer–Polak,
[arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1), Section 2 (1), p. 2.
Singleton anchor D allows every index {D,E} used here at order three.

For complete Johnson eigenspaces, eigenvalues and multiplicities import
Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Sections 1.2, 3,
3.4, pp. 3,10,12; for the common decomposition, tensor eigenvectors and
positive-leading-block congruence use Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf), Sections
11.2 and 1.4.7, pp. 162–163,19, and Theorem 2.7.1(i), p. 36.
The factors J(68,5), J(956,5) satisfy n>=10. These imported theorems are
not reproved. The application-specific orbit and column calculations
below are necessary because none of these sources decides the fixed
entries in this problem. L054 supplies the shell dictionary and L056
supplies the retained coefficients and complete zero modes.

**Compression preserves the exact question.** Write U=D\G and V=G\D,
each of size six. Every shell support is uniquely E=(D\X) union Y,
where X is a five-subset of D and Y a five-subset of H\D. Put
i=|X intersection U|, j=|Y intersection V|. The group K of point
permutations preserving D and G separately is the product of symmetric
groups on U, D\U, V, and H\(D union V), whose sizes are 6,62,6,950.
It has precisely the 36 orbits (i,j), 0<=i,j<=5. Each occurs; its size is

  W_i^(68) W_j^(956), where W_i^(n)=binomial(6,i)binomial(n-6,5-i).

Indeed each of the four intersections of X,Y with these regions can be
mapped to another of equal size by a region permutation. This proves
both transitivity and exhaustiveness, rather than assuming distance-only
orbit classification for arbitrary triples.

L056's retained shell is unchanged by K: its pair and full-region
coefficients are point-permutation invariant. K also preserves the
new anchor entry/diagonal, each forbidden distance and every represented
triple coefficient, since the whole unordered region partition is
preserved. Nonnegativity is preserved. The shell kernel is invariant,
so averaging a compatible column over K preserves compatibility.
Consequently restricting to orbit-constant columns loses no feasible
column for this necessary test. This does not average actual-label RS
constraints, which are absent from the hypotheses. A point permutation
also carries any ordered pair D,G at distance six to another, preserving
exactly these constraints; the construction therefore works for all D,G.

Normalize the new triple column by rho*p_5 and call its orbit values
t_ij. Direct intersections give |E\G|=11-i-j. Thus i+j>=7 requires
t_ij=0; these are ten coordinates. The represented case is i+j=6,
where E is the unique eligible distance-five anchor. At that anchor,
L054's full eight-region tuple is

  (5-r,r,r,63-r,5-q,q,q,951-q), with (r,q)=(6-i,i).

In particular the common region has size 57+i, not a distance-only
choice of coefficient. Therefore the five fixed coordinates are

  t_(i,6-i)=d_(6-i,i), 1<=i<=5,
  d_rq=z_rq/[binomial(5,r)binomial(63,r)binomial(5,q)binomial(951,q)],

with exactly the 21 z values in L056. For i+j<=5 the remaining 21
coordinates are free nonnegative. D,E,G are always distinct, so there
is no further Boolean identification within this column. L056 already
proves consistency for its represented unordered orbits.

**Anchor transport and complete invariant kernel.** Write B for L056's
shell block divided by rho*p_5 and J for the shell all-ones matrix.
The retained matrix and new column, after division by positive rho, are

  C=[1,p_5*1^T; p_5*1,p_5*B],     b=[p_6; p_5*t].

The invertible change of coordinates (s,u) -> (s-p_5*1^T*u,u)
changes C to diag(1,p_5*(B-p_5*J)) and changes b to
[p_6; p_5*(t-p_6*1)]. This is the same congruence on both blocks.
L056's constant Schur eigenvalue is 4982733184/5>0. Every zero mode
is therefore nonconstant, and the constant subtraction p_6*1 has
zero projection onto it. Thus the required condition is precisely that
t be orthogonal to all zero modes of B-p_5*J. This uses p_5,rho>0,
not invertibility of the shell. The value of p_6 remains its fixed L053
value throughout; its magnitude is irrelevant to this kernel test.

For completeness the invariant part of every zero mode can be identified
by an explicit six-dimensional quotient, without guessing multiplicities.
On five-subsets of an n-set with a distinguished six-set, the distance-one
Johnson relation acts on functions of i by the matrix Q^(n) with entries

  Q_(i,i-1)=i(n-11+i),  Q_(i,i+1)=(5-i)(6-i),
  Q_(i,i)=5(n-5)-Q_(i,i-1)-Q_(i,i+1).

Boundary entries are omitted. The two off-diagonal counts respectively
remove a distinguished point and add an undistinguished point, or the
reverse; the remaining distance-one moves preserve i. The weights W_i
are the exact orbit sizes. Construct h_a^(n), a=0,...,5, by weighted
Gram–Schmidt on the six evaluation vectors 1,i,...,i^5, keeping leading
coefficient one. Positive weights and the Vandermonde matrix at 0,...,5
ensure every step is nonzero and give a basis. The exact certificate
verifies for both n=68,956 and every a the six identities

  Q^(n) h_a^(n) = ((5-a)(n-5-a)-a) h_a^(n).

These six eigenvalues are distinct (successive differences n-2a>0).
By the imported Johnson decomposition the lifted vector is in exactly
factor mode a. The 36 products h_a^(68)(i) h_b^(956)(j) consequently
form an orthogonal basis of the full K-invariant space, each in the
corresponding product mode. This proves that its intersection with
the full kernel is spanned by exactly the zero-mode products below.

For a K-invariant t, orthogonality to this invariant kernel implies
orthogonality to the entire kernel: for any kernel vector v, its finite
K-average is still a kernel vector, and <t,v>=<t,average_K(v)>.
Hence the following 20 equations exhaust the kernel condition:

  sum_(i,j=0)^5 W_i^(68) W_j^(956) h_a^(68)(i) h_b^(956)(j) t_ij = 0,

for (a,b) in

  {(0,1),(0,2),
   (1,0),(1,1),(1,2),(1,4),(1,5),
   (2,0),(2,1),(2,3),(2,4),
   (3,0),(3,1),(3,2),(3,3),
   (4,0),(4,1),(4,2),(5,0),(5,1)}.

This is L056's complete zero table. All other product modes are positive.
The exact calculation also reconstructs all 36 eigenvalues directly from
L056's z values using the imported Eberlein formula, checking the signs.

**Exact nonnegative solution.** The table below specifies all 21 free
coordinates; the five represented coordinates and ten zeros are fixed
by the formulas above. Every displayed fraction is nonnegative.

| (i,j) | t_ij |
|---|---|
| (0,0) | 407371877936178924193788598477918937/14331502346960463151555147846790566589742696000 |
| (0,1) | 1291721605294996417523395854869509/45448738943849248894995183446481712229628000 |
| (0,2) | 678393256845414324038538367/23584614757512686044051462199238760000 |
| (0,3) | 0/1 |
| (0,4) | 553790615596151552732520493/6401452904464735008341934938740440000 |
| (0,5) | 335724475814777438010509/29170439300363340206616244879200 |
| (1,0) | 3241687518414250888990912713459593/114043785254327292983197462971808222199544000 |
| (1,1) | 1781660142792219017191343362931/62687915784619653648269218546871327213280 |
| (1,2) | 33952292120240399315210491939/1182077156898092729828579320917018540000 |
| (1,3) | 153184259773116225418155799/16114002138825022607205560363036280000 |
| (1,4) | 4497601688950925245321901/44147951065274034540289206474072000 |
| (2,0) | 468372668850577507388179765091/16477568305709972867814026325462705069120 |
| (2,1) | 62922589970551431551514645587/2213556348326965171195946982587264379000 |
| (2,2) | 7977122811256207498626698497/280492884687683020637290008353190840000 |
| (2,3) | 3826948593076525737749263/221908927759242896073805386355372500 |
| (3,0) | 3274674814525374802509899/115205319492569318492047313160214800 |
| (3,1) | 6926455107620893161809/243563043324670863619550344947600 |
| (3,2) | 3403482988494788419/122473496919933053562402748000 |
| (4,0) | 1374755827/48364677790213097775 |
| (4,1) | 113372647/3987785272343151825 |
| (5,0) | 22687/798408127148775 |

Substitution into all 20 displayed equations gives zero exactly. One
construction takes t_23 as parameter; rational row reduction has rank 20.
Intersecting all 21 coordinate nonnegativity constraints gives the closed
interval with lower and upper endpoints respectively

  3826948593076525737749263/221908927759242896073805386355372500,
  689512027427211313039687769/826754522994296083897677764417880000.

The endpoints are in increasing order, both positive. The lower endpoint
is imposed by t_03>=0, the upper by t_02>=0; all other inequalities hold
throughout this interval. The table uses the lower endpoint, so t_03=0.
The compatible column is x({D,E,G})=rho*p_5*t_ij, with the independently
fixed anchor entry and diagonal rho*p_6. It annihilates the full retained
kernel by the transport and invariant-basis proof above.

**Exact evidence and limitations.** Run from the notebook:

  `python3 scripts/finite-support/full_shell_nullspace.py`

The certificate `scripts/finite-support/full-shell-nullspace-results.json`
contains all quotient weights/bases, 36 full-region representatives, all
36 shell spectra, the complete 20-by-21 system, exact row transformation,
affine solution, all parameter bounds and the selected rational column.
It uses Fraction arithmetic only and imports no notebook modules or
numerical optimizer. The full elimination identity and all original
kernel equations are checked. The invariant reduction is proved above;
the finite matrix rank alone would not justify it.

All 182 constructor checks pass. Independently run

  `python3 scripts/finite-support/verify_full_shell_nullspace.py`.

This verifier parses the 21 fractions from this manuscript, reconstructs
the five fixed coefficients directly from L056, and obtains the factor
eigenvectors by the distance-one three-term recurrence starting at value
one, without importing the constructor's Gram–Schmidt or elimination.
It checks all six coordinates of every eigenvector, orthogonality,
nonzero norms, all 36 shell spectra, all 36 column signs, and every raw
and transported zero-mode projection. It compares every free/fixed
coordinate, all 36 full-region records and orbit sizes, and both complete
bases with the constructor certificate. All 342 checks pass with no
failures. Full exact evidence is in
`scripts/finite-support/full-shell-nullspace-verification.json`.
Both full failure lists, the full rational solution, fixed entries,
zero-mode list, bases and all 36 final projections were inspected.
This calculation is not the separate critical proof audit. In particular,
kernel compatibility supplies no value or bound for b^T C^dagger b.
The new diagonal rho*p_6 must still dominate that energy to obtain PSD.
No such inequality, other column, global moment system or RS claim is
deduced. L057/L058 and ATTEMPTS/038–040 remain contrasting small tests,
not mathematical inputs to this argument.

**Separate critical proof review — step 196, 2026-10-13.** The unchanged
SPECIALIZE gate is
`drafts/literature/2026-10-13-full-shell-nullspace-critical-audit.md`.
The review retains the full stated result and interval, with no changed
hypotheses, coefficients or boundary claim. This is local verification
of a reproduction, not a new theorem beyond the checked sources.

The four-region stabilizer fixes D,G individually and preserves every
constraint in this ordinary slice. Each shell support is specified by
four subsets of the regions, so the two intersection counts exhaust its
orbits. The five represented cases have E as their only eligible anchor;
all six permutations of all 36 actual support representatives were
checked against the full eight-region dictionary. The new Boolean
diagonal and anchor entry both remain rho*p_6. Transporting the column
by the same congruence as C is essential: its shell part is
p_5*(t-p_6*1), as above. The strictly positive constant Schur coordinate
leaves precisely the 20 nonconstant zero modes.

For an independent check of mode identification, count the complete
relation-r quotient between intersection classes i,j as

  sum_(u=0)^5 binomial(i,u) binomial(6-i,j-u)
    binomial(5-i,5-r-u) binomial(n-11+i,r+u-j).

Here u points of X' are in X intersection U, j-u are in U outside X,
5-r-u are in X outside U, and the remaining r+u-j are outside both.
This exhausts X' with |X'|=5, |X' intersection U|=j and |X intersection
X'|=5-r; out-of-range choices vanish. For n=68,956 the audit reconstructs
all six quotient matrices, their orbit-weight adjoint identities and
all six eigenvectors by recurrence. Every coordinate of their action
under every relation is checked. Thus the product vectors are in the
claimed modes, not merely eigenvectors of an unverified quotient.
The basis/exhaustion and finite-group averaging proof above then tests
the full kernel, including noninvariant vectors and singular modes.

Run `python3 scripts/finite-support/critical_audit_full_shell_nullspace.py`.
It imports no notebook modules, reads both manuscripts and both complete
original certificates, and compares all entries, spectra and projections.
It reconstructs every original equation and checks all 440 entries of
T*[A|rhs]=R. The 20 pivot columns of R form the identity: rank(A)>=20,
and its 20 rows give equality, without assuming T invertible. The
reconstructed affine constant and slope satisfy all original equations,
with parameter coordinate t_23 respectively zero and one. Hence they
give every solution. All nine lower bounds, six upper bounds and six
constant coordinates are checked; all coordinates are nonnegative at
both interval endpoints, and affine dependence gives nonnegativity
throughout. The active lower and upper constraints are exactly t_03
and t_02. Every manuscript fraction agrees with the lower-endpoint
solution. No sampled parameter or numerical rank test is substituted.

All 2238 additional exact checks pass, as do all 342 checks of the
rerun independent substitution verifier. Complete evidence, including
every quotient, support permutation, equation, elimination residual,
coordinate bound and source hash, is saved in
`scripts/finite-support/full-shell-nullspace-critical-audit-results.json`.
The full failure list, summary and all coordinate bounds were inspected;
the verifier checks all load-bearing certificate entries in full.
No energy computation is included. Critical verification parks only
this necessary kernel-exclusion test; other columns, labeled constraints,
global feasibility, measures and the main safety gap remain unresolved.

## Mathlib

Full matching column certificate, stabilizer quotient and complete Johnson
product-kernel application: not checked. Supporting spectral, singular
Schur, finite-group averaging and finite-set results: not checked.
Unknown availability is not evidence of absence.
