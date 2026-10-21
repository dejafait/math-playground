# L022 — Finite growing-chain minima and a failed repeated-word bound

## Hypotheses

Use the positive-integer shortcut map T(n)=n/2 for even n and
T(n)=(3n+1)/2 for odd n. O and E specify actual input branches.
Let W(J,H)=(OOEO)^J O^H E^2, with integers J>=2,H>=3.
A K-word chain requires all input parities of W(J_1,H_1)...W(J_K,H_K).
Its root is positive and 20 modulo 27. No parity is required at the final
endpoint; internal endpoints are odd because the next word begins O.
These words need not be first returns. The screen does not impose the
additional least-root arithmetic restrictions of L014–L018.

For the finite minima restrict 2<=J_i<=4 and 3<=H_i<=5. Write mu_K
for the minimum root over this nine-word alphabet. Separately, let b_K
be the minimum positive residue-20 root realizing W(2,3)^K, with the
same unconstrained final-endpoint convention.

## Conclusion

The exact finite minima and their unique attaining parameter chains are:

| K | Number of chains | mu_K | Attaining (J,H) sequence |
|---|---:|---:|---|
| 1 | 9 | 77,915 | (2,3) |
| 2 | 81 | 796,340,315 | (2,3),(2,4) |
| 3 | 729 | 630,703,655,003 | (2,4),(2,5),(2,3) |
| 4 | 6,561 | 11,553,444,320,785,499 | (3,5),(2,5),(3,3),(2,4) |
| 5 | 59,049 | 37,597,514,278,222,600,283 | (2,5),(2,3),(2,3),(2,3),(2,3) |

The proposed uniform estimate n>=b_K for every actual chain in the
full alphabet J_i>=2,H_i>=3 is false. Already mu_2<b_2=1,249,325,147.
The K=4 witness has all four final even runs exactly two steps, yet
mu_4<b_4=66,920,253,169,807,451. Thus requiring an odd final endpoint
does not repair this particular bound: the minimum for the repeated
word with that additional guard is at least b_4.

A second test, using only positivity/integrality of the affine endpoint,
produces a negative lower bound for every K and every choice in the full
alphabet. Neither test refutes an unspecified bound tending to infinity.
No infinite growing chain, uniform escape theorem, or Collatz resolution
is established.

## Proof

### Imported finite coding and exact minimum calculation

The prior EXPLORE assessment is
`drafts/literature/2026-10-04-growing-postspell-initial-size.md`.
Finite coding is known mathematics: Bernstein–Lagarias,
[*The 3x+1 Conjugacy Map*, author PDF dated 15 February 1996](https://websites.umich.edu/~lagarias/doc/bernstein.pdf),
section 1, pp. 1–3, equations (1.3)–(1.5) and the reduction-modulo-2^d
permutation statement; Rozier–Terracol,
[*Paradoxical behavior in Collatz sequences*, arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2),
section 2, paragraph before Theorem 2.2 and the unique parity-vector
realization in the proof of Lemma 2.3. These concern the same shortcut
map and input-parity convention. A length-D word has precisely one
root class r modulo 2^D, independently of final-endpoint parity.
No positive-integer realization of an infinite vector is imported.

L020 supplies, at a=2,

\[
A_i=3^{3J_i+H_i},\quad q_i=2^{4J_i+H_i+2},\quad
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
 +(3^{H_i}-2^{H_i})16^{J_i}>0.
\]

For an actual word the endpoint is (A_i x+C_i)/q_i and is positive
and 20 modulo 27. L020 also proves A_i>q_i throughout J_i>=2,H_i>=3,
so each such endpoint strictly exceeds its input. Repeatedly applying
L021's affine substitution retains both offsets. Starting with
A=1,C=0,q=1, extension by word i gives

\[
A'=A_iA,\qquad C'=A_iC+qC_i,\qquad q'=q_iq.
\]

For the concatenation's imported parity residue r, CRT gives its least
positive residue-20 root as

\[
n_0=r+q\bigl((20-r)q^{-1}\bmod27\bigr),\qquad 0\le r<q.
\tag{1}
\]

If this expression is zero, replace it by 27q. The inverse exists since
q is a power of two. All positive roots are n_0+27q t, t>=0; (1) is
therefore a minimum, rather than an arbitrary large witness.

The exhaustive exact calculation is
`scripts/growing-postspell/check_chains.py`, with the full certificate
`scripts/growing-postspell/result.json`. Reproduce with
`python3 scripts/growing-postspell/check_chains.py`.
The script enumerates each of the nine extensions of every chain of
length K-1, starting with the empty chain, hence all 9^K parameter
chains exactly once. It computes the joint parity class in two ways:
the imported one-bit coding recursion on the complete word and an
independent incremental substitution. To check the latter, if the old
class is r modulo q, let s=(Ar+C)/q. For the next word's class r_i
modulo q_i, the new root is r+qt with

\[
t\equiv A^{-1}(r_i-s)\pmod{q_i}.
\]

Here s is integral and A is odd, so this chooses exactly one extension.
The new affine coefficients are those above. The code checks equality
with whole-word coding for every row, evaluates (1), and replays every
input parity at n_0 and n_0+27q. It checks each boundary's residue,
strict growth, all internal odd endpoints, the pre-tail state equal to
four times its endpoint, and the complete affine identity. Every row
retains the chain, A,C,D with q=2^D, r, CRT period, minimum root and
both sets of boundary endpoints. The selected minima additionally
retain every shortcut state, so all load-bearing parity cases are saved.

There are 66,429 rows, 66,429 matching whole-word codings and 132,863
complete guarded replays (including the five selected-minimum replays),
with zero failed checks. Taking the minimum of all rows at each K
gives the table. These are finite exhaustive arithmetic results using
known coding, reported as REPRODUCTION rather than a new escape theorem.

### Explicit failure of the repeated-smallest-parameters estimate

For W(2,3)W(2,4), the exact data are

\[
A=1,162,261,467,\quad C=2,656,567,591,\quad D=27,\quad
r=125,251,675,\quad n_0=796,340,315.
\]

The CRT period is 3,623,878,656. The boundary endpoints are
1,913,374,811 and 6,895,927,082, and the pre-tail states are
7,653,499,244 and 27,583,708,328. The complete 28-state replay is
stored at `/minima/1/states` in the certificate; it checks exactly the
27 inputs of these two words. The internal endpoint is odd, so the
first tail is exact. The final endpoint is even, which is allowed in
this finite-prefix test and must not be hidden.

For W(2,3)^2, the independently coded data are

\[
A=387,420,489,\quad C=879,930,125,\quad D=26,\quad
r=41,365,595.
\]

Formula (1) gives b_2=1,249,325,147 with period 1,811,939,328.
Thus the mixed actual root is strictly below the repeated-word minimum.

To retain exact tails even at the last word, use the K=4 attaining
chain in the table. Its D=65 inputs have the complete 66-state replay
at `/minima/3/states`. Its four boundary endpoints are

\[
105,399,639,185,987,675;\quad
569,800,716,640,629,851;\quad
2,310,298,634,736,732,251;\quad
8,326,466,313,633,380,297.
\]

They are all odd, and each stored pre-tail state is four times the
corresponding endpoint. Hence every final even run is exactly two.
Whole-word coding gives

\[
A=26,588,814,358,957,503,287,787,\quad
C=54,862,284,914,609,664,419,191,\quad
r=n_0=11,553,444,320,785,499.
\]

CRT places this positive root in residue 20 modulo 27. Applying (1)
to W(2,3)^4 gives b_4=66,920,253,169,807,451. The strict inequality
n_0<b_4 refutes the proposed estimate with every tail exact. This is
a counterexample to a bound on actual positive residue-20 chains,
not a nonconvergent start or a refutation of a bound restricted further
by the hypothetical least-root conditions.

### Full-parameter test of the positive-endpoint estimate

For a single word put rho_i=A_i/q_i and c_i=C_i/A_i. L020's constants
give exactly

\[
\rho_i=\tfrac14(27/16)^{J_i}(3/2)^{H_i}
 \ge\frac{19683}{8192}>1,
\qquad
c_i=\frac{23}{11}-(16/27)^{J_i}
 \left(\frac{12}{11}+(2/3)^{H_i}\right)
 \ge\frac{31567}{19683}.
\]

For the second inequality the subtracted positive product decreases
when either J_i or H_i increases; its maximum is at J_i=2,H_i=3.
Under affine composition C'/A'=C/A+(q/A)c_i. Induction thus gives
C/A>=31567/19683 and q/A<= (8192/19683)^K for every chain in the
full alphabet. Positivity and integrality of its endpoint m give
An+C=qm>=q, so the attempted lower estimate is n>=(q-C)/A.
But its right side satisfies

\[
\frac{q-C}{A}
\le (8192/19683)^K-31567/19683
\le -23375/19683<0\quad(K\ge1).
\]

It supplies no positive initial-size cost. This tests only that necessary
affine inequality; full parity constraints contain more information.
The fact that q grows, or that the exact finite minima grow, cannot
replace the missing uniform control of their CRT residues. L005's
fixed-word limitation and L008's boundary-error failure are comparisons,
not mathematical premises here. No limit over changing words is taken.

## Mathlib

Full finite minimum statements, repeated-word counterexamples and
supporting parity coding/CRT/affine-composition coverage: **not checked**.
No matching declaration or library absence is asserted. Imported finite
coding is cited precisely above; no infinite integer-realization theorem
or external Lean build is assumed.
