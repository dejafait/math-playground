# L018 — Residual-pair elimination and the quadratic root-count limitation

## Hypotheses

Use L017's fixed instance Q=65537, E=F_Q, H of order n=1024,
A=66, C=binomial(n,A), and threshold tau=Q^28/2^128. Its incidence
energy is K=J_3-J_2/Q. For an A-subset S write
p_j(S)=sum_{x in S} x^j. All subset pairs below are ordered.

For a pair S,T put d_j=p_j(T)-p_j(S). Let E_r count pairs with
d_1=...=d_r=0, for r=2,3. Let B count pairs with d_1!=0, and let
N count those pairs that also satisfy

\[
 d_1^4+3d_2^2-4d_1d_3=0.                              \tag{1}
\]

For each pair S,T^- of subsets of sizes A,A-1 put
a=p_1(T^-)-p_1(S), b=p_2(T^-)-p_2(S),
c=p_3(T^-)-p_3(S). Let D count such pairs with
b=-a^2 and c=a^3. Put W=C binomial(n,A-1).

## Conclusion

The residual roots can be eliminated exactly:

\[
 J_3=QE_3+N,\qquad J_2=QE_2+B,\qquad
 K=QE_3-E_2+N-B/Q.                                    \tag{2}
\]

The first difference QE_3-E_2 is nonnegative. The remaining difference
N-B/Q is signed; no positivity or independence is assumed for it.

If l=|S minus T|, then the l=0 contribution to K is (Q-1)C, the
l=1 contribution is (1-1/Q)C A(n-A), and the l=2 contribution is
-B_2/Q, where B_2 counts l=2 pairs with d_1!=0. In particular the
positive part supplied by l<=2 is at most

\[
 P_{\rm near}=(Q-1)C+(1-1/Q)C A(n-A).                 \tag{3}
\]

Fixing S,T^- reduces (1), with T=T^- union {y}, to a polynomial of
degree at most two in y. Counting at most two roots unless this
polynomial is identically zero gives the valid certificate

\[
 N\le {2C^2\over n-A+1}+{n-A-1\over A}D,
 \quad K\le U_{\rm root}:=QE_3-E_2-B/Q+
              {2C^2\over n-A+1}+{n-A-1\over A}D.      \tag{4}
\]

Let K_req be the sufficient energy threshold in L017, equation (4).
This particular root-count allowance necessarily satisfies

\[
 U_{\rm root}\ge X:=\left({2\over959}-{1\over65537}\right)C^2,
 \qquad 6.14\mathbin{\cdot}10^{14}<X/K_{\rm req}
                                  <6.15\mathbin{\cdot}10^{14}.   \tag{5}
\]

Thus even evaluating E_2,E_3,B,D exactly cannot make the certificate
(4) certify K<=K_req. The limitation concerns this two-root allowance,
not actual K. More precise counts for larger symmetric differences could replace (4).

The proportion of all ordered subset pairs having half-symmetric-difference size l<=2 is less than
10^(-95), and P_near/K_req<10^(-80). The exact near-diagonal cases
do not supply the missing effective estimate for larger symmetric differences. No uniform
list bound below tau, unsafe list, or changed full-code grid bound is
obtained. The degree-67 family remains unresolved.

## Proof

**Coverage and purpose.** Reuse the prior
[EXPLORE assessment](../drafts/literature/2026-10-04-correlated-cubic-cofactor-error.md)
for the unchanged signed-correlation target. L017 supplies the energy
identity and the sufficient margin. Its imported finite-group Parseval
and orthogonality, from Tao's
[245C Notes 2](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
Section 1 Exercises 14 and 16 and Section 2 Lemma 17 and Corollary 22,
are used through that identity, rather than reproved. This local
elimination and root-count comparison reproduce elementary finite-field
and energy tools. They give no new character estimate or novelty claim.
The closest inspected source supplies the energy framework, not an
effective estimate for these large subset collisions. The local check
is needed to decide whether the remaining algebraic condition is usable.

**Eliminating the residual pair.** A pair of incidences counted by J_r
consists of S,T and z,w in E with
p_j(S)+z^j=p_j(T)+w^j, for 1<=j<=r. Thus z^j-w^j=d_j.
If d_1=0 then z=w. There are Q choices precisely when all the other
required d_j vanish, and zero otherwise. If d_1!=0, the first two
equations uniquely give

\[
 z-w=d_1,\quad z+w=d_2/d_1,\quad
 z={d_1+d_2/d_1\over2},\quad
 w={d_2/d_1-d_1\over2}.
\]

Since 2 is invertible, these are valid and unique. Their cubes satisfy
z^3-w^3=(d_1^4+3d_2^2)/(4d_1). This proves the two counts in
(2); subtracting J_2/Q gives K. For the nonnegativity assertion, fix
the first two subset moments and let c_t count subsets at each third
moment t in E. Cauchy–Schwarz gives (sum_t c_t)^2<=Q sum_t c_t^2.
Summing over the first two moments proves E_2<=QE_3. It does not
give a sign to N-B/Q.

**Small symmetric differences.** Common roots may be removed from both
subsets without changing d_j. For l=0 each identical subset pair has
d_j=0, hence contributes Q-Q/Q=Q-1 to K. There are C such pairs.
For l=1 the reduced subsets are {x},{y} with x!=y. Then d_1=y-x,
and the unique residual solution is z=y,w=x, including the third
equation. Each pair therefore contributes 1-1/Q. Choosing S, its
removed element and its replacement gives C A(n-A) pairs.

For l=2, equal first two power sums would determine the same two-root
multiset by Newton identities, contradicting disjointness of the two
reduced subsets. Thus E_2 and E_3 have no contributions from this class.
Nor can the reduced subsets, after each receives one residual root,
have equal first three power sums: Newton identities would determine
the same three-root multiset. The single residual root on one side
cannot supply both distinct roots of the other side. This argument
allows repeated residual roots. Hence N_2=0, leaving only -B_2/Q.
These facts prove (3). Nothing here excludes collisions for l>=3.

**The remaining one-root polynomial.** Substitute
d_1=a+y, d_2=b+y^2, d_3=c+y^3 into (1). Direct expansion gives

\[
 (a+y)^4+3(b+y^2)^2-4(a+y)(c+y^3)
 =6(a^2+b)y^2+4(a^3-c)y+a^4+3b^2-4ac.                \tag{6}
\]

Because the characteristic exceeds 3, this polynomial is identically
zero exactly when b=-a^2 and c=a^3. Those equalities kill its constant
term as well. Otherwise it has at most two roots in E, hence at most
two in H minus T^-. An identically zero polynomial permits at most
n-A+1 choices for y. Ignoring the additional d_1!=0 requirement can
only increase these upper counts.

Every pair counted by N has A choices of its marked y in T. Counting
the triples S,T^-,y therefore gives
A N<=2(W-D)+(n-A+1)D. Since
binomial(n,A-1)=A C/(n-A+1), division by A proves (4). Degenerate
configurations are not absent: T^-=S minus {x} already supplies them.
Keeping their count D avoids an invalid generic-root assumption.

**Quantitative limitation.** In (4), QE_3-E_2>=0, D>=0 and
n-A-1>0. Also B<=C^2. Consequently U_root>=X, independently of
how those unknown counts are evaluated. L017's threshold is

\[
 K_{\rm req}={Q\over Q-1}
 \left(\tau-{C\over Q^2}
       -{513(Q-1)\over Q^2}\binom{579}{66}\right)^2.
\]

Exact rational arithmetic proves (5). X is a lower bound on the
chosen *upper allowance*, and is not a lower or upper bound on actual
K. In particular (5) neither proves a large energy nor rejects the
possibility of a different useful signed estimate.

For any l the total number of ordered pairs with |S minus T|=l is
C binomial(A,l) binomial(n-A,l). Summing l=0,1,2 and dividing by C^2
gives the stated small fraction. Equation (3) and the displayed exact
K_req give its energy comparison. The l=2 negative term is retained
in (2); (3) bounds only the known positive contribution. The point is
that classifying a few near-diagonal cases does not estimate the
overwhelmingly larger unresolved classes, rather than an assertion
that their signed contributions cannot cancel.

**Checks and research decision.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_residual_pair_elimination.py`.
The saved output is
`scripts/coefficient-fibers/residual-pair-elimination-results.json`.
The fixed-instance inequalities use exact integers and fractions.
Small audits use the order-6 subgroup of F_13 at A=3 and the order-8
subgroup of F_17 at A=4. They independently enumerate every residual
pair, compare with the eliminated formula, check the marked-root
polynomial for every field element, and classify the l<=2 cases. The
F_17 audit reproduces J_3=2440, J_2=5816 and K=35664/17 from L017.
These are identity checks, not estimates for the 1024-point instance.

The bounded test gives a new quantitative limitation for a precise
counting mechanism, with the remaining collision counts unestimated.
Park this signed-energy route rather than repeat another reformulation.
It does not settle the family or the main sharp-boundary gap.

## Mathlib

Full residual-pair/proper-subgroup threshold result: **not checked**.
Supporting finite-group Parseval, Cauchy–Schwarz, Newton identities,
finite-field polynomial root bounds and counting identities: **not
checked** in Mathlib. The primary reference above supports the energy
framework, not the full effective statement. The pinned ArkLib model
definitions remain **present** as recorded in foundations/; they do
not estimate these collisions.
