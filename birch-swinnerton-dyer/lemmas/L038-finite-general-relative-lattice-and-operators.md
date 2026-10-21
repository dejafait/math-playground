# L038 — Finite general relative lattice and operator construction

## Hypotheses

Let N be a supplied positive integer and let P be any supplied finite set
of primes ell not dividing N. Work at weight two with trivial character
for Gamma_0(N). Put M=M_2(Gamma_0(N)), meaning the entire relative symbol
module modulo all torsion, and V=M tensor Q. A path {alpha,beta} is
oriented from alpha to beta, including endpoints at infinity.

For the downstream application retain L029's supplied non-CM global
minimal E/Q, its independently established exact conductor N and its
normalized rational newform f. Independently certified integers
a_ell(E) are supplied whenever L037 requests them. This construction
does not compute or certify the conductor, minimal equation, newform
association or arithmetic eigenvalues.

All algorithms below use exact integer/rational arithmetic. No practical
runtime, polynomial complexity, prime cutoff, software plus convention,
period normalization, twist value or BSD assumption is imposed.

## Conclusion

There is a finite exact construction of the following complete evidence:

1. Every coset in Gamma_0(N)\SL_2(Z), with an SL_2(Z) lift, and every
   two/three-term Manin relation; a saturated relation basis giving
   M=Z^s/R_sat, an integral basis of M and the exact coordinates of
   all s original integral generators.
2. Integral column-convention matrices J and H_ell on that entire basis
   of M, for geometric reflection j{alpha,beta}={-alpha,-beta} and each
   good-prime path operator of L029 equation (1). Every generator image
   has finite endpoint/segment witnesses, and all saturated relations
   and matrix reconstruction identities have exact finite checks.

The evidence can be checked by finite arithmetic replay independently
of the builder. The source theorems identify the checked presentation
and operators with relative homology; arithmetic replay does not replace
those theorems. In particular no torsion or boundary directions are
discarded by rational elimination or an absolute-homology restriction.

This discharges the mathematical finishing-construction premises for
the presentation, reflection and good-prime matrices in audited L037.
Under its retained exact-level/newform and supplied arithmetic hypotheses,
L037 and L029 therefore give an eventual dimension-one line test with
constructible finite evidence. It gives no explicit stopping prime or
universal software-correctness guarantee. Independent arithmetic supply remains
a premise; q, period calibration, nonzero coefficients and the main BSD
comparison remain separate. The separate critical audit of 2026-10-09
passes under these hypotheses; it is known-algorithm reproduction, not a
BSD candidate. Subsequent parameterized structural certificates at N=1
and N=15 have complete independent replay as recorded below; their
separate executable critical audit of 2026-10-10 passes for these instances.

## Proof

**Imported results and specialization.** Import William Stein,
*Modular Forms, a Computational Approach*, GSM 79, AMS, 2007,
[equation (3.2.1), p. 40; Propositions 3.10--3.11, pp. 42--43;
Theorem 3.13, p. 44; Section 3.4.1, pp. 47--48](https://wstein.org/books/modform/stein-modform.pdf).
These identify the integral relative module and give complete generators,
relations modulo torsion, path reduction and the good-prime operator.
Use John Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition, 1997,
[Propositions 2.2.1--2.2.2, pp. 15--16](https://johncremona.github.io/book/fulltext/chapter2.pdf),
for composite-level projective cosets and coprime lifts. For the geometric
sign use Stein's online General Modular Symbols,
[equations (11)--(12), Remark 1.43](https://wstein.org/books/modform/modform/modular_symbols.html).
The group normalization holds for Gamma_0(N); weight two makes the
polynomial constant, and geometric j is the negative of Stein's star.

Import the general integer Smith normal form theorem and the terminating
rectangular/arbitrary-rank algorithm in Francis Sergeraert,
[*About the Kannan--Bachem algorithm*, arXiv:2411.02422v1,
4 November 2024, Sections 2, 3.1, 4, 6--7, Theorem 1](https://arxiv.org/html/2411.02422v1).
Tracking integral elementary operations provides unimodular transforms.
Its rank-deficient coefficient-growth warning is retained: termination
gives no practical runtime estimate. Neither the unread original
Kannan--Bachem paper nor Manin's original Section 1.7 is used as an
additional premise. Stein's stated Theorem 3.13, whose injectivity proof
is referred to Manin, is the precise imported presentation theorem.
No topological or normal-form theorem is reproved here.

The source domains allow arbitrary positive N, composite N and elliptic
points. The specialization below supplies the finite evidence contract
and its integral-coordinate algebra, which a citation alone does not
specify. No source supplies the actual matrices for an unspecified N.

**1. Complete finite cosets and coprime lifts.** For N>1 enumerate all
pairs (c_0,d_0) with 0<=c_0,d_0<N and gcd(c_0,d_0,N)=1. Enumerate every
unit modulo N and its scalar action on these pairs. Select one pair in
each orbit, for example the lexicographically first. Save the full
orbit-assignment table and unit witnesses. This is a finite enumeration,
and the cited projective-coset propositions show that the orbit list is
exactly Gamma_0(N)\SL_2(Z). In particular the prime-level list (1,t),(0,1)
is not substituted at composite N. For N=1 take the single coset and
the identity lift directly.

Here is a finite explicit specialization of the coprime-lift requirement.
For each representative at N>1 take c=c_0 if c_0>0 and c=N otherwise,
so c is positive and c=c_0 modulo N. Factor c by finite trial division.
If a prime q divides both c and N, the primitive-pair condition gives
q not dividing d_0; hence q does not divide d_0+kN for any k. For each
prime q dividing c but not N, exclude the single residue
k=-d_0 N^(-1) modulo q and choose any other residue. Such a residue
exists even for q=2. CRT for these distinct primes supplies k; with no
such primes take k=0. Then d=d_0+kN is divisible by none of the prime
divisors of c, so gcd(c,d)=1. Extended Euclid supplies x c+y d=1 and
therefore the lift

\[
 g=\begin{pmatrix}y&-x\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbf Z).
\]

Factorization, CRT and Bezout are finite. The checker needs only verify
the residue pair, gcd and determinant for each produced lift; it also
reconstructs all primitive pairs and unit orbits to certify completeness.
Thus a lift search is not justified merely by an unproved hope of
eventual coprimality.

Number the lifts g_1,...,g_s and associate column e_i in F=Z^s to
g_i{0,infinity}. For any h in SL_2(Z), its bottom row modulo N belongs
to the finite orbit table. The selected index i has
gamma=h g_i^(-1) in Gamma_0(N), by the cited coset criterion. Save gamma
and verify determinant one and lower-left entry divisible by N. This
gives a finite, directly checkable coset lookup for all later segments.

**2. Every relation and all torsion.** Use the convention

\[
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 R_3=\begin{pmatrix}1&-1\\1&0\end{pmatrix}.
\]

The right actions on the coset list are obtained by lookup of g_i S,
g_i R_3 and g_i R_3^2. Put their indices iS,iR_3,iR_3^2 into every
row e_i^t+e_(iS)^t and e_i^t+e_(iR_3)^t+e_(iR_3^2)^t of the
2s-by-s integer matrix A. Repeated indices contribute their full integer
multiplicity, including elliptic-point relations. R_3^3=-Id, and -Id
belongs to Gamma_0(N); no extra sign relation is required. These are
Stein's Theorem 3.13 conventions in its
[online weight-two statement](https://wstein.org/books/modform/modform/weight_two.html).
The convention (0,-1;1,-1) used elsewhere is R_3^2, whose square is
-R_3, so the same two three-term summands are interchanged on projective
cosets. No convention comparison or theorem from L030 is a premise.

Let R=im(A^t) in F. The imported theorem identifies M with
(F/R)/(F/R)_tors. Equivalently M=F/R_sat, where
R_sat=(R tensor Q) intersect F: a class z+R is torsion precisely when
n z lies in R for some positive integer n. This equivalence also shows
why keeping only the raw integral relation quotient would be wrong.

The imported finite normal-form algorithm gives

\[
 U A W=D,\quad U\in\mathrm{GL}_{2s}(\mathbf Z),\quad
 W\in\mathrm{GL}_s(\mathbf Z),
\]

with D rectangular diagonal, r nonzero diagonal entries delta_1,...,delta_r
and zero elsewhere. All transforms and inverses, or their complete
reversible elementary-operation logs, are retained. Check the whole
identity and both inverse products, every off-diagonal entry, all nonzero
pivots and the entire zero tail. Diagonal equivalence suffices below;
divisibility-ordered Smith form is available but unnecessary. This covers
r=0 and rank-deficient cases as well as full rank.

Write E_h for the s-by-r first-coordinate inclusion and E_t for the
s-by-(s-r) last-coordinate inclusion, and set d=s-r. Transposing the
identity shows

\[
 W^t R=\operatorname{im}(D^t)
       =\bigoplus_{j=1}^r\delta_j\mathbf Z e_j.
\]

Consequently the following are exact integral matrices:

\[
 K=W^{-t}E_h,\qquad Q=W^{-t}E_t,\qquad
 \Pi=E_t^t W^t.
\tag{1}
\]

The columns of K are a basis of R_sat, Pi:F->Z^d is onto with kernel
R_sat, and the columns of Q lift an integral quotient basis. Indeed
Pi Q=Id_d, Pi K=0, and [K Q]=W^(-t) is unimodular. Transforming z by
W^t splits it uniquely into its first r and last d coordinates; thus
z=K a+Q Pi z with a integral. This proves the kernel assertion without
guessing a lattice from its rational dimension. The torsion removed has
order product_(j=1)^r |delta_j| (empty product one); none of its prime
factors is retained. Every original generator has coordinate Pi e_i,
an integer column. The relation/saturation witnesses include Pi A^t=0
and Pi K=0 in addition to the full normal-form identities.

Via Stein's relative identification, this quotient is the entire
integral relative homology lattice. Its integral basis is also a rational
basis of V, meeting L029's coordinate requirement with no hidden
denominators. If a later rational basis is chosen, its full change matrix,
inverse and all generator coordinates must additionally be recorded.
The construction is valid also when d=0; the downstream elliptic-newform
setting has d>=1 by L029's nonzero integration on absolute cycles, which
does not use a granted dimension-one kernel.

**3. Finite witnesses for arbitrary oriented endpoint paths.** Given
{alpha,beta}, reduce it as {infinity,beta}-{infinity,alpha}. Treat a chain
to infinity as empty. For a finite reduced a/b with b>0, use the cited
continued-fraction construction from Proposition 3.11, starting at
infinity and ending at a/b. Integer endpoints have a single segment.
Signed numerators are allowed: Euclidean division with floor and positive
denominator leaves remainder in [0,b), so the successive nonzero
Euclidean remainders decrease and the chain is finite. This is not a
claim that the convergent denominators decrease. Neighboring convergents
have determinant of absolute value one by the cited construction.

For each segment with start u_0/v_0 and end u_1/v_1, including a
zero-denominator infinity endpoint, put Delta=u_1 v_0-u_0 v_1 in {1,-1}.
Then

\[
 h=\begin{pmatrix}\Delta u_1&u_0\\\Delta v_1&v_0\end{pmatrix}
 \in\mathrm{SL}_2(\mathbf Z),\qquad
 h(0)=u_0/v_0,\quad h(\infty)=u_1/v_1.
\tag{2}
\]

Multiplying one column by -1 changes no cusp and does not reverse the
path. Use step 1 to produce its coset index i and gamma=h g_i^(-1).
Thus its class is exactly g_i{0,infinity}. Save both endpoints, h, i
and gamma; the checker verifies each rational/projective endpoint,
determinant, membership and adjacent-chain equality. Telescoping proves
the complete path expression, with the minus sign on the alpha chain.
There is no division by infinity. Equal endpoints give zero after the
same chain cancellation. Repeating this for all original generator
paths checks their reductions against every Pi e_i.

**4. Every operator column and descent.** For each generator's actual
endpoints alpha_i=g_i(0), beta_i=g_i(infinity), reduce the reflected path
{-alpha_i,-beta_i} by step 3. For each ell in P reduce all ell+1 paths

\[
 \{\ell\alpha_i,\ell\beta_i\},\qquad
 \{(\alpha_i+t)/\ell,(\beta_i+t)/\ell\}
       \quad(0\le t<\ell).
\tag{3}
\]

These are exactly the endpoint representatives in the cited good-prime
formula; their matrices have positive determinant ell. Reflection
preserves the path-parameter direction and has the sign of L029's j,
not Stein's star. That it is well-defined follows from diag(-1,1)
normalizing Gamma_0(N), the cited reflection formula and the relative
path identification. Well-definedness of the sum (3) is the imported
good-prime correspondence on relative symbols. An individual summand
need not descend on its own; no such assertion is used.

For O=j or T_ell, let Z_O be the s-by-s matrix whose ith column is
the raw integral generator expression for O(g_i{0,infinity}) from all
the saved chains. Put Y_O=Pi Z_O. Because every chain represents the
stated geometric path and the imported operator is well-defined on M,
Y_O A^t=0. Also Y_O K=0: each column k of K has some positive multiple
n k in R, so n Y_O k=0, and Z^d is torsion-free. Both identities are
explicitly checked on the complete matrices, including every saturated
relation. No sampled relation test replaces them.

Define the operator matrix on the integral quotient basis by

\[
 B_O=Y_O Q\in\operatorname{Mat}_d(\mathbf Z).
\tag{4}
\]

For z=K a+Q Pi z, the preceding kernel identity gives
Y_O z=B_O Pi z. Thus check B_O Pi=Y_O on every original generator;
this proves its column convention and its action on all M and V. Set
J=B_j and H_ell=B_(T_ell). The complete path witnesses identify the
operator, while the kernel and reconstruction identities certify descent.
Neither eigenvalues on a proposed vector nor the optional identities
J^2=Id and J H_ell=H_ell J would suffice for that identification.

There are finitely many generators and relations, finitely many primes
in P, and finitely many paths for each. Each chain and each exact
matrix operation finishes. Hence all matrices and all witnesses above
are obtained in finite time. A separate checker regenerates the complete
coset/relations, verifies unimodularity and the entire diagonal identity,
checks every segment and coset witness, and checks (1), all relation
images and (4). Every check is finite exact arithmetic; the imported
theorems ensure that these constructed identities pass. This is an
existence/construction proof, not a report of a run or of observed values
for an unspecified level. The original abstract construction step
produced no mathematical script or instance certificate; the later
executed specializations are recorded below.

**5. Retained scope in the line test.** L037 needs only finitely many
operator constructions before its existential dimension-one stage. The
presentation and j are constructed once; step 4 constructs every
subsequently requested good-prime matrix. Exact Gaussian elimination
also finishes and can retain reversible rational operations, a nonzero
nullvector and a rank minor for each actual stop. Under the supplied
arithmetic hypotheses, audited L037 proves that enumeration eventually
reaches dimension one, and L029 then identifies that rational line with
real integration. No upper bound for the first such prime follows.

The argument changes the known-source assembly, not the theory of Manin
symbols or multiplicity one. L030 is only a comparison; its fixed matrices
are not imported. ATTEMPTS/022--024's calibration-production limitations
are preserved. Constructing a relative line supplies no independent
nonzero q, normalized all-level denominator, quadratic coefficient,
rational Kummer directions, elimination of divisible Sha or general
complex-order comparison. No complete solution or new beyond-source
mathematical discovery is claimed.

**Separate critical audit, 2026-10-09.** The finite-construction conclusion
passes. The decreasing-remainders sentence in step 3 was clarified above;
the quotient and operator formulas and hypotheses are unchanged. No
implementation, instance replay or practical complexity bound is claimed.

For step 1, the primitive-pair condition protects every prime dividing
both c and N. At each remaining prime divisor q of c, N is invertible,
so exactly one residue of k is excluded; even at q=2 an allowed residue
exists. CRT only combines distinct such primes, and avoiding them makes
gcd(c,d)=1, including d=0 when c=1. If c_0=0 then c=N and d_0 is a unit
modulo N; this branch has no unprotected prime divisor. The Bezout lift
has determinant y d+x c=1 and the required bottom row. Coset lookup uses
h g_i^(-1), not the reverse product: bottom-row unit equivalence makes
its lower-left entry divisible by N. All unit orbits are retained, so
no prime-level completeness claim has been substituted at composite N.

For step 2, S swaps the generator endpoints and R_3 cycles the three
paths {0,infinity}, {infinity,1}, {1,0}. The relations therefore have
the exact orientations of the cited theorem; repeated indices must
remain with multiplicities two or three. At N=1 all indices coincide,
so A has rows (2) and (3), R=Z, r=s=1 and d=0. The single identity lift
and the zero-dimensional quotient are consistent; no elliptic-curve
newform at level one is being asserted.

Transposing U A W=D gives W^t A^t=D^t U^(-t); since U^(-t) is an
integral automorphism, W^t R=im(D^t). Its saturation is exactly the
first r-coordinate lattice. The unimodular matrix W^(-t) therefore
gives both the full saturated kernel K and section Q, while Pi extracts
the complementary coordinates. Thus Pi Q=Id, Pi K=0 and
K E_h^t W^t+Q Pi=Id_s. These identities check every original generator,
not just a rational spanning subset. When r=0, K is empty and Pi,Q
are inverse automorphisms; when r=s, Pi and Q have no quotient
coordinates, K spans F and B_O is the unique 0-by-0 matrix. Empty
products and identity matrices have their usual meanings. Nonunit
pivots account for every torsion prime, not just a selected p.

For step 3, the floor Euclidean algorithm terminates also for negative
numerators, since each subsequent positive remainder is strictly smaller
than the preceding divisor. The convergent neighbor determinant is
plus or minus one, including the first infinity-to-integer segment.
Equation (2) has determinant Delta^2=1, sends 0 to the start and infinity
to the end, and changing the sign of the end column does not change
either projective cusp or path direction. It works for an infinity end
as well as an infinity start. The full chain must start at infinity,
end at the requested finite cusp and have every adjacent endpoint
identified. Subtracting the alpha chain gives precisely {alpha,beta};
an empty infinity chain and equal endpoints give the required special
cases. Reducing a generator again agrees with Pi e_i by the imported
presentation isomorphism, regardless of its chosen SL_2 lift.

For step 4, projective infinity is fixed by every affine endpoint map
in (3) and by reflection; finite fractions can be reduced without
altering their cusps. Each full ell+1 sum is the cited good-prime
correspondence on the entire relative module. Geometric reflection
normalizes Gamma_0(N), preserves endpoint order and equals negative
Stein star at weight two, as in L029. The imports give a genuine
integral map on F/R_sat, so its coordinate map Y_O kills A^t. For a
saturated relation k, some nonzero integer multiple lies in R;
torsion-freeness of Z^d then forces Y_O k=0, including all nonunit
pivot directions. This argument uses the complete sum, never an
individual Hecke summand. Finally the displayed decomposition of Id_s
gives Y_O=Y_O Q Pi=B_O Pi. Full path witnesses and this full matrix
identity together identify the operator; an eigenvector check would
not suffice. Every requested arithmetic replay identity has thus been
justified to pass in principle, without claiming an actual run.

For step 5, audited L037 uses only finitely many requested matrices
before its existential dimension-one stage. The present constructions
finish separately for each such prime, and exact rational elimination
finishes for each finite matrix. L029 identifies the resulting line
only after the actual rank and nullvector witnesses are retained.
There is no circular use of a dimension-one premise to construct the
lattice or operators. Supplied exact conductor/newform and independent
a_ell remain assumptions; q and the subsequent arithmetic/BSD gaps
remain open. No dependency changes are needed: L029 and L037 are the
direct inputs, and L030 is not used. The primary presentation/path/Hecke
passages were reopened only for these convention checks, reusing the
ready assessment; the unread-original and Mathlib qualifications remain.

**Executed structural specializations, 2026-10-10.** The separately
parameterized implementation in `scripts/general-relative/build_certificate.py`
now accepts positive N and a finite set of good primes; it rejects
nonpositive levels, repeated primes, composite primes and primes dividing
N. This supplies finite executable evidence for the two instances below,
not a proof of correctness of every execution or a practical runtime bound.
The separate checker `scripts/general-relative/verify_certificate.py`
imports no builder code. It reconstructs the primitive-pair unit orbits
and the entire Manin domain, uses elementary matrices to replay both
transform logs and their inverses, and verifies every saved path by
projective endpoints, segment orientation, adjacency and telescoping.
Continued-fraction terms are also checked, but no trust in the builder's
continued-fraction routine is needed for path identification.

In the exact certified integral basis (Pi,Q in each artifact), the results
are as follows. All matrices carry their full row and column dimensions.

| N, P | Primitive assignments | s,r,d | Relations | Paths / segments | Removed torsion order |
| --- | --- | --- | --- | --- | --- |
| 1, {2} | 0 (single identity coset) | 1,1,0 | 2 | 5 / 6 | 1 |
| 15, {2} | 192 | 24,19,5 | 48 | 120 / 501 | 1 |

At N=1 the relations are (2),(3), D has pivot 1, Pi is 0-by-1,
Q is 1-by-0, and both operators are 0-by-0. All five paths and six
segments are nevertheless replayed, including their raw sums and
Gamma_0(1) reductions; no empty-coordinate shortcut omits their evidence.
At N=15 there are eight units, every primitive pair is assigned to one
of the 24 complete unit orbits with a unit witness, and all 19 pivots
are 1. Thus the original relation quotient in these two instances already
has no torsion; the full saturation construction is still checked rather
than inferred from this observation.

The column-convention operators at N=15 are

\[
J=\begin{pmatrix}
1&0&0&0&0\\0&1&0&0&0\\-1&0&0&1&0\\
1&0&1&0&0\\0&0&0&0&1
\end{pmatrix},\qquad
H_2=\begin{pmatrix}
1&1&1&1&-1\\0&3&0&0&0\\0&-1&0&1&1\\
2&0&2&1&0\\-2&1&1&1&2
\end{pmatrix}.
\]

These matrices are not certified by their displayed entries alone. The
full artifacts `scripts/general-relative/N1-certificate.json` and
`scripts/general-relative/N15-certificate.json` retain all lifts, orbit
assignments, right-action lookup/gamma witnesses, relations, U,U^(-1),
W,W^(-1), reversible operation logs, Pi,K,Q, every generator coordinate,
all endpoints and path chains, Z_O,Y_O and B_O. The complete independent
reports are `scripts/general-relative/N1-verification.json` and
`scripts/general-relative/N15-verification.json`, each with the SHA-256
of its full certificate, all check labels, actual/required domain counts
and an empty failure list. No bounded preview substitutes for full replay.

Precisely, for N=15 the checker replays all 92 row operations, 51 column
operations and their 92 and 51 inverses; for N=1 it replays all three
row operations and inverses (there are no column operations). It checks
UAW=D and both inverse products for each transform, the full diagonal
and zero tail, every generator's coordinates, PiQ=Id, PiK=0,
Pi A^t=0 and K E_h^t W^t+Q Pi=Id. For each operator it reconstructs
all original-generator images from the complete paths, verifies every
source-relation and saturated-kernel image is zero, then checks
B_O=Y_O Q and B_O Pi=Y_O on every generator. At N=15 these mean 96
source-relation images, 38 saturated-kernel images and 48 generator
reconstructions across J and H_2; N=1 checks 4,2,2 respectively with
explicit empty output shapes. The supplementary involution/commutation
tests pass but are not substituted for these load-bearing checks.

Reproduce from this notebook directory:

```bash
python3 scripts/general-relative/build_certificate.py --level 1 --primes 2 --out scripts/general-relative/N1-certificate.json
python3 scripts/general-relative/build_certificate.py --level 15 --primes 2 --out scripts/general-relative/N15-certificate.json
python3 scripts/general-relative/verify_certificate.py scripts/general-relative/N1-certificate.json --level 1 --primes 2 --out scripts/general-relative/N1-verification.json
python3 scripts/general-relative/verify_certificate.py scripts/general-relative/N15-certificate.json --level 15 --primes 2 --out scripts/general-relative/N15-verification.json
python3 scripts/general-relative/check_rejection.py
```

The bounded sensitivity report `scripts/general-relative/rejection-checks.json`
records rejection of all eight specified corruptions: empty shape loss,
a Boolean operation coefficient, missing primitive assignment, incorrect
relation multiplicity, missing Hecke term, wrong segment start,
nonzero recorded saturated image and an out-of-range operation. These
tests support checker coverage but are not a universal soundness proof
or a substitute for the separate critical audit recorded below.
The sources and Mathlib qualifications below are
unchanged; these are reproductions of the cited known algorithms.
No elliptic curve, a_ell, real eigenline, q, period scale or coefficient
is attached to either structural level. The original BSD gap remains.

**Separate executable critical audit, 2026-10-10.** The complete N=1 and
N=15 certificates pass the relative-lattice/operator contract. All three
programs were read against the approved source domains and the formulas
above. The checker imports no builder; its proof obligations, rather than
its name or supplementary identities, establish what the replay verifies.
No code, certificate, hypothesis or displayed operator required repair.
This is validation of known-algorithm specializations, not a new theorem
about arbitrary software executions or an advance beyond the cited sources.

For N>1 the checker independently enumerates every pair with
gcd(c,d,N)=1 and partitions them by every unit. Primitivity implies the
unit action is free: from (u-1)c=(u-1)d=0 modulo N and a Bezout combination
of c,d,N equal to one, u=1 modulo N. Thus its orbit-size and partition
checks cover the complete coset domain. Every list length is checked before
zipping or indexing. Each lift has determinant one and the required bottom
row, and every lookup checks h g_i^(-1) explicitly in Gamma_0(N).
The S,R_3,R_3^2 right products reconstruct every relation, including repeated
indices. For N=1 the explicit identity branch gives A=(2,3)^t; it does not
pretend that an empty primitive-pair enumeration is a completeness proof
at this level. The stated Stein/Cremona imports identify these domains.

For an addition of row j to row i with coefficient a, the checker uses
E=Id+a e_i e_j^t on the left; the same column addition uses E^t on the
right. If row operations are E_1,...,E_t then U=E_t...E_1, and reversed
inverse replay gives U^(-1)=E_1^(-1)...E_t^(-1). If column matrices are
F_1,...,F_v then W=F_1...F_v and reverse replay gives
W^(-1)=F_v^(-1)...F_1^(-1). Grouping all row and then all column operations
is valid because left and right multiplication commute as actions on A.
The complete logs, stored transforms, both inverse products and UAW=D
were replayed, not inferred from determinants or a rank computation.
Strict integer checks reject Boolean coefficients, dimensions, coordinates
and indices; operation arity and index ranges precede use. The complete
positive diagonal and zero tail certify r. The transposed identities in
step 2 then identify K,Q,Pi and the entire saturated lattice; every
generator coordinate and the full integral decomposition were checked.
At N=15 the exact Q columns are e_16,e_1,e_21,e_22,e_23 in zero-based
generator indexing, and the corresponding Pi columns form Id_5.
At N=1, U=(-1,1;3,-2), U^(-1)=(2,1;3,1), W=1, K=1,
Q is 1-by-0 and Pi is 0-by-1. The matrix class retains both dimensions
through transpose, multiplication and addition, so the empty quotient
does not mask a missing raw path or malformed shape.

For every saved segment the checker verifies reduced projective cusps,
det(h)=1, h(0)=start, h(infinity)=end, the exact coset/Gamma_0 lookup,
adjacency from infinity and the final requested endpoint. These facts
prove the segment class and telescoping path independently of the builder's
Euclidean routine; the continued-fraction recurrence is an additional
check. Subtracting the entire start chain from the entire end chain fixes
the orientation. Every original generator is reduced again and compared
with Pi e_i, including all five paths at d=0. Negative cusps are actually
exercised: the N=15 reflection of {0,1/15} is {0,-1/15}; its end chain
has terms (-1,1,14), raw expression e_0+e_2 and coordinates
(0,-1,0,0,0)^t after subtraction of the start chain. This example checks
the convention; the exhaustive replay, not this example, verifies all paths.

The checker fixes J's endpoint map to diag(-1,1), without interchanging
endpoints or attaching Stein's star sign. It fixes T_2 to all three maps
diag(2,1),(1,0;0,2),(1,1;0,2) in the imported good-prime formula;
2 does not divide either level. All generator image paths reconstruct Z
and Y=Pi Z, all source and saturated images are checked against zero,
and B=YQ and BPi=Y are checked on the full matrices. With the imported
geometric path identification, these identities prove the full relative
operator action by step 4, not just involution, commutation or an eigenvalue
on a proposed vector. No boundary direction or individual Hecke term is
silently dropped.

The new complete reports `scripts/general-relative/N1-critical-audit.json`
and `scripts/general-relative/N15-critical-audit.json` have respectively
751 and 41210 passed check labels and no failures. Their full parsed
contents equal the original verification reports, including every label,
actual/required count and certificate hash. The original five program/input
hashes match the pre-audit source notes. The provenance and full domain
counts are retained in `scripts/general-relative/critical-audit-manifest.json`.
Reproduce the two verifier commands above with the output names changed to
these critical-audit reports. The full eight-case rejection evidence was
inspected and `check_rejection.py` rerun: all eight still reject with the
recorded contract failures. These bounded sensitivity checks supplement
the code-to-contract audit, without proving universal soundness.

The actual/required domains are exactly the counts in the executed section:
N=1 has 5/5 paths and 6 segments; N=15 has 120/120 paths and 501 segments.
All listed relation, transform, inverse, source-image, saturated-image and
reconstruction counts match their independently required domains.
Both instances have unit pivots, so no nontrivial torsion-removal execution
is certified by this audit; neither tests r=0. Structural N=1 is not an
elliptic arithmetic case. No a_ell, dimension-one dual kernel, q, period,
coefficient, cutoff, runtime bound or universal execution theorem follows.
The written construction and mathematical dependencies remain unchanged.

**Executed conductor-36 presentation, 2026-10-12, BSD-176.** The
unchanged structural hypotheses above also apply with N=36 and P empty.
This use concerns the relative integral module, independently of a
non-CM elliptic curve or any downstream line test. Under the prior
[full-table SPECIALIZE assessment](../drafts/literature/2026-10-12-conductor36-full-generator-recovery.md),
the existing builder and independent verifier construct and replay this
complete instance:

    python3 scripts/general-relative/build_certificate.py --level 36 --out scripts/conductor36-table/presentation.json
    python3 scripts/general-relative/verify_certificate.py scripts/conductor36-table/presentation.json --level 36 --out scripts/conductor36-table/presentation_verification.json

All 864 primitive-pair assignments and 72 coprime lifts are checked.
The relation matrix is 144 by 72. Its unimodular diagonalization has
59 positive pivots, all one, and the entire remaining zero tail. Both
transform inverses and all 287 row and 172 column operations, together
with their inverse replays, pass. Thus the imported Stein presentation
and the exact decomposition of step 2 identify the integral relative
module with Z^13: no torsion or boundary direction is lost. Specifically,
the verifier checks Pi Q=Id_13, Pi K=0, Pi A^t=0 and
K head+Q Pi=Id_72, as well as the coordinate of every original generator.
These integer identities certify generation and the complete saturated
kernel; a rational rank computation alone would not do so.

Every one of the 144 source relations, all 216 relation lookups and all
72 original oriented generating paths are reconstructed. The structural
contract also replays the 72 reflection paths, for 144 paths and 626
segments in total, with exact endpoints and every coset lookup. The
reflection output kills all 144 source relations and 59 saturated-kernel
columns and reconstructs all 72 generator images. This operator is a
supplementary structural check; it is not used to infer a real eigenline.
The report has 149753 passed checks and zero failures, with every actual
count equal to its independently reconstructed required count. The
independent verifier is unchanged and imports no producer.

The cited Stein/Cremona theorems above supply the mathematical
identification; the complete finite normal-form, coordinate and path
evidence supplies this instance's hypotheses. All previous evidence is
preserved. This establishes the full integral presentation needed by a
conductor-36 table, not its normalized values, analytic intervals,
integer isolation, coefficient or BSD comparison. The separate critical
audit of this instance now passes as recorded below. A direct endpoint
execution plan is preserved under `scripts/conductor36-table/`; its
large workload is recorded in the attempt notes and is not a runtime
bound or an additional conclusion of this structural result.

**Separate conductor-36 structural critical audit, 2026-10-12, BSD-188.**
The prior SPECIALIZE assessment
`drafts/literature/2026-10-12-conductor36-structural-instance-critical-audit.md`
approves precisely N=36, P empty. Reuse the Stein presentation/path,
Cremona coset and Sergeraert normal-form imports cited above, and L029's
geometric orientation. Their positive-level structural hypotheses allow
this composite level and impose no non-CM condition. L037 is downstream;
L049--L055 supply no structural premise. The audit establishes this fixed
instance, not a theorem of universal program correctness.

The entire producer and separate verifier were inspected against steps
1--4. The verifier reconstructs all primitive pairs and unit orbits before
reading assignments, tests strict integral types and matrix dimensions,
and reconstructs every relation including repeated-index multiplicities.
Elementary matrices replay the row operations on the left and transposed
column operations on the right. Inverse operations are applied in reverse
order with negated addition coefficients. Both inverse products, UAW=D,
the whole diagonal and its zero tail are checked. Thus the saturation
and section formulas in (1), the integral decomposition and all generator
coordinates have full integer witnesses; neither a rational rank nor a
saved success flag establishes this claim.

For each of all 144 paths, every reduced projective endpoint and every
segment's determinant-one lift is tested. The lookup explicitly checks
h g_i^(-1) in Gamma_0(36). Adjacency starts at infinity and ends at the
requested cusp, including empty infinity chains and signed fractions.
The end-chain minus start-chain expression fixes the path orientation.
Base paths equal every original generator coordinate. The sole requested
operator is geometric J, with endpoint map diag(-1,1), preserving endpoint
order. Its entire raw matrix, quotient image, 144 source-relation images,
59 saturated-kernel images and all 72 reconstructed generator images are
checked. Empty P omits Hecke calculations only, not these requirements.

Fresh full replay returns 149753 passed checks and no failures. Every
parsed field, including every check label, agrees with the original
production report. The actual/required domain is 864/864 assignments,
72/72 cosets, 144/144 relations, 216/216 relation lookups, 287/287 row
operations and inverses, 172/172 column operations and inverses,
144/144 paths (626 segments), 144/144 source images, 59/59 saturated
images and 72/72 generator reconstructions. The resulting ranks remain
(s,r,d)=(72,59,13), and the removed torsion order is one.

Two independent identities supplement that replay. First, all 59 pivots
are one, so transposing UAW=D gives

\[
A^tU^t=W^{-t}D^t,
\qquad K=A^t C,\quad C=(U^t)_{[:,0:59]}.
\]

The new audit script multiplies the saved integer matrices with separate
list arithmetic and verifies all 59 columns, retaining the full 144-by-59
matrix C. This explicitly expresses the complete saturated kernel in the
original integral relation lattice. Together with the audited unimodular
decomposition it confirms that this instance's original quotient is
already torsion-free. It does not test a nonunit-pivot instance.

Second, for every g_i=(a,b;c,d), set H=diag(-1,1) and
h_i=H g_i H=(a,-b;-c,d) in SL_2(Z). Since H fixes 0 and infinity,
h_i{0,infinity}={-g_i(0),-g_i(infinity)} with unchanged order. Independently
scan all representatives and units for the bottom row (-c,d) modulo 36,
find its unique index j and unit, and verify the full matrix
h_i g_j^(-1) has determinant one and lower-left entry divisible by 36.
The imported coset criterion therefore identifies the reflected symbol
with the single original generator e_j. No continued fraction, saved
path decomposition or involution assumption enters this reconstruction.

For all 72 indices the script checks Pi e_j against the saved reflected
path coordinate and Y_J e_i. The resulting permutation covers all 72
indices. Its full image matrix Y_direct satisfies
B_direct=Y_direct Q=B_J and B_direct Pi=Y_direct, checked entrywise.
In particular (Y_direct)_(0,0)=-1 in zero-based indexing; negative
reflection gives +1 there. This discriminates the geometric sign, whereas
J squared equals identity alone would also hold for -J. The complete
coset, Gamma_0, endpoint and coordinate witnesses are saved for every i.

Six independently saved altered certificates are rejected at their
specific contract checks: a nonunit assignment, an altered relation
entry, an altered column inverse, an altered generator coordinate,
a reversed reflection path, and a negated reflection basis matrix.
The last two fail respectively at endpoint identification and B=YQ,
not merely at an involution check. The rejected inputs and full partial
reports remain on disk. These sensitivity checks supplement exhaustive
replay and code inspection; they do not claim universal checker soundness.
All four original builder/checker/input/report hashes agree before and
after with the approved snapshot, so original evidence is byte-preserved.

Reproduce from the notebook root:

    python3 scripts/general-relative/verify_certificate.py scripts/conductor36-table/presentation.json --level 36 --out scripts/conductor36-table/structural-critical-audit/full_replay.json
    python3 scripts/conductor36-table/audit_structure.py

Full replay, independent integer/reflection witnesses, six rejected inputs
and their reports, and the provenance manifest are in
`scripts/conductor36-table/structural-critical-audit/`. The manifest has
zero audit failures and records all actual/required counts and original
hashes. The fixed structural audit passes. No new lemma, analytic sum,
normalized table, eigenline, nontrivial-torsion execution, practical
runtime bound or BSD consequence is claimed. The mathematical assembly
and direct inputs are unchanged; this is validation of a known-method
instance, not progress beyond the checked sources.

## Mathlib

Full matching finite general relative lattice/operator certificate:
not checked. Supporting integral relative Manin presentation, composite
projective cosets, all-torsion quotient, transformation-output Smith
normal form, oriented path reduction and good-prime operators: not
checked. Unknown coverage is not evidence of absence. The precise
standard source inputs and the coordinate/descent specialization used
here are recorded above.
