# L001 — Rank ambiguity in finite Selmer tower data

## Hypotheses

Fix a prime p. Let B be a finitely generated abelian group of rank r and
finite torsion subgroup T. Let A be a p-primary torsion abelian group with
A[p^n] finite for every n >= 1. Suppose there are finite groups S_n and
exact sequences of abelian groups

\[
0\longrightarrow B/p^nB\xrightarrow{\iota_n}S_n
 \xrightarrow{q_n}A[p^n]\longrightarrow0.
\tag{1}
\]

When discussing towers, require downward homomorphisms
rho_n: S_(n+1) -> S_n commuting with reduction on B/p^nB and multiplication
by p on A[p^n]. When A carries an alternating pairing b: A x A -> Q/Z,
write beta_n(x,y) = b(q_n(x),q_n(y)) for the pulled-back pairing on S_n.

For an elliptic curve E/Q, these hypotheses hold with B = E(Q),
A = Sha(E/Q)[p^infinity], and S_n = Sel_{p^n}(E/Q), by the standard inputs
in [the foundations](../foundations/02-standard-inputs.md). In that
application, an alternating pairing is available; nondegeneracy on A is
asserted only if A is finite.

## Conclusion

Put u_n = log_p |S_n| - log_p |T[p^n]|. Then

\[
u_n=nr+\log_p|A[p^n]|,
\qquad r\le\left\lfloor\frac{u_n}{n}\right\rfloor.
\tag{2}
\]

For every integer N >= 1, there are two systems (1), both with T = 0 and
finite A equipped with a nondegenerate alternating pairing, for which:

- one has r = 2 and the other r = 0;
- their groups S_n, downward maps, and pairings beta_n are isomorphic for
  all observed levels 1 <= n <= N;
- both give u_n = 2n at every observed level and both ranks have even parity.

Here the observed data do **not** specify the subgroups iota_n(B/p^nB),
the quotient maps q_n, or the whole groups A. The complete exact sequences
with their marked endpoints are not claimed to be isomorphic. Nor are these
abstract examples claimed to be realized by elliptic curves.

If A is finite, then lim_(n->infinity) u_n/n = r. Thus the obstruction is to
deducing rank from an arbitrarily long finite prefix of the specified data;
it does not contradict eventual recovery from the entire tower.

## Proof

**The exact defect.** The structure theorem for finitely generated abelian
groups gives B/p^nB isomorphic to (Z/p^n Z)^r direct-sum T/p^nT. On the
finite group T, multiplication by p^n has kernel T[p^n] and image p^nT,
so |T/p^nT| = |T[p^n]|. Taking orders in (1) now gives

\[
|S_n|=p^{nr}|T[p^n]|\,|A[p^n]|.
\]

This proves (2); its inequality uses |A[p^n]| >= 1. In the elliptic-curve
application the torsion correction therefore cannot be omitted without
justification.

**Two full systems.** Fix N, and choose any integer M >= 2N. For the first
system take B^+ = Z^2, A^+ = 0, and S_n^+ = (Z/p^n Z)^2 for every n. The
injection in (1) is the identity, the quotient is zero, and rho_n^+ is
coordinatewise reduction. The pairing on A^+ is the unique pairing; it is
nondegenerate since the group is zero. Every beta_n^+ is zero.

For the second system take B^- = 0 and

\[
A^-=(\mathbf Z/p^M\mathbf Z)^2,\qquad S_n^-=A^-[p^n]
\quad(n\ge1).
\]

The quotient q_n^- is the identity on A^-[p^n], and rho_n^- is
multiplication by p. These choices make (1) exact and commute with the
specified endpoint maps at every level, including n > M.

On A^- define, using integer representatives,

\[
b^-((a,b),(c,d))=\frac{ad-bc}{p^M}\pmod{\mathbf Z}.
\tag{3}
\]

Changing any representative by a multiple of p^M changes the value by an
integer. Thus (3) is well-defined and bilinear, and b^-(x,x) = 0. If (a,b)
pairs to zero with (1,0) and (0,1), then b and a are both zero modulo p^M.
Its radical is therefore zero, which proves nondegeneracy. This argument
works also for p = 2; alternation is checked directly.

**Equality of the observed data.** For n <= N define

\[
\phi_n:(\mathbf Z/p^n\mathbf Z)^2\longrightarrow A^-[p^n],
\qquad (u,v)\longmapsto p^{M-n}(u,v)\pmod{p^M}.
\tag{4}
\]

In Z/p^M Z the elements killed by p^n are exactly the multiples of
p^(M-n). Formula (4) is therefore a well-defined group isomorphism.
For n < N and x in (Z/p^(n+1) Z)^2,

\[
p\phi_{n+1}(x)=p^{M-n}x
 =\phi_n(x\bmod p^n).
\]

Hence these isomorphisms intertwine all observed downward maps. They also
intertwine upward maps if those are included: multiplication by p on
(Z/p^n Z)^2 corresponds to inclusion A^-[p^n] into A^-[p^(n+1)].

For u = (u_1,u_2) and v = (v_1,v_2), the second system has

\[
\beta_n^-(\phi_n(u),\phi_n(v))
 =p^{M-2n}(u_1v_2-u_2v_1)\pmod{\mathbf Z}=0,
\]

since M >= 2N >= 2n. It matches beta_n^+. Thus even observing zero
restricted pairings at every tested level does not separate these systems,
although the pairing on the full finite A^- is nondegenerate. Their
group orders are p^(2n), while their B-ranks are respectively 2 and 0.

**Threshold and limitations.** If A is finite, then
0 <= log_p |A[p^n]| <= log_p |A|. Dividing (2) by n proves the limit.
For the second example specifically, u_n = 2 min(n,M), so u_n/n tends to
zero after having equalled two through level M. Each chosen A^- is finite;
it is M, and hence A^-, that changes when a longer observation depth is
prescribed. This proves no claim about a single finite A imitating rank
two forever.

The bound actually obtained from the observed cardinalities is r <= 2.
Even if even rank parity is supplied, both r = 0 and r = 2 remain possible
in these systems. The required certificate for a rank-two application is
r = 2, so the missing lower bound has not been supplied. No analytic
order is attached to the abstract examples, and neither is a BSD
counterexample.

There are valid finite certificates with additional information. For
example, if B is independently known to contain k linearly independent
elements of infinite order and u_n < n(k+1), then k <= r < k+1, hence
r = k. For elliptic curves, certified independent rational points can
provide this lower bound. Actual local Galois data, marked Kummer images,
and pairings involving deeper lifts may also add information not included
in the observation used above. The lemma rules out only the inference
from the specified finite tower data alone.

For a finite verification of the coordinate maps and pairings, run
`python3 scripts/finite-selmer/check_models.py` from the notebook directory.
The saved output is `scripts/finite-selmer/check-results.json`. It checks
p = 2,3 and N = 1,2 with M = 2N using exact integer arithmetic. These
instances supplement, rather than replace, the proof for arbitrary p,N.

## Mathlib

Full statement, including the tower and restricted-pairing comparison:
**not checked**. Supporting finite abelian group and exact-sequence results
in Mathlib: **not checked**. No matching theorem name or absence claim is
asserted. The arithmetic supporting inputs are the named results in the
foundations; the finite algebra argument is supplied in full above.
