# L020 — Exact postspell descent criterion and a lower final-halving bound

## Hypotheses

For positive integers use (T(x)=x/2) at even x and
(T(x)=(3x+1)/2) at odd x. O and E denote these actual branches.
Let (J\ge2,H\ge3,a\ge0) be integers with (a\equiv2\pmod{18}).
An actual word requires every input parity, not just an integral final
affine value. Suppose a positive (n\equiv20\pmod{27}) has prefix

\[
W=(OOEO)^J O^H E^a,
\qquad z=T^{4J+H}(n),\quad m=T^{4J+H+a}(n).
\]

For comparison with L019, put
(e(J,H)=J+H+((2-J-H)\bmod18)), with remainder in \(\{0,\ldots,17\}\).
The lower-tail application below has (a<e(J,H)).
The least-root conclusion is conditional on existence of a nonconvergent
positive start, with (n=\min\mathcal B_{20}) supplied by L014.

## Conclusion

Put

\[
\begin{aligned}
D&=4J+H+a,& A&=3^{3J+H},\\
C&=\frac{23\cdot3^H(27^J-16^J)}{11}
       +(3^H-2^H)16^J,& \Delta&=2^D-A.
\end{aligned}
\]

Then (C) is a positive integer, (m=(An+C)/2^D), and

\[
\boxed{m<n\quad\Longleftrightarrow\quad
\Delta>0\ \text{and}\ n>C/\Delta.}
\tag{1}
\]

The endpoint is positive and congruent to 20 modulo 27.
For fixed J,H,a, actual residue-20 words ending below their root exist
if and only if (\Delta>0); when this holds there are infinitely many.
This existence statement concerns arbitrary test roots, not bad roots.

In particular, if

\[
2\le J\le12,\qquad 3\le H\le12,\qquad J+H\ge21,
\tag{2}
\]

every actual word with (a=20) descends below every positive root.
There are ten pairs in (2), all with (e(J,H)=38). At a least bad
residue-20 root with the prefix ((OOEO)^J O^H) and (2), therefore

\[
\boxed{v_2(z)<20,}
\tag{3}
\]

a stronger conditional bound than L019's (v_2(z)<38).
Within (2\le J\le12,3\le H\le12), all other eligible triples
with (a<e(J,H)) have (a=2) and can never descend below a positive
root. No universal prefix entry or guard satisfaction is concluded.

## Proof

### Imported identities, followed by exact specialization

Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-04-sharp-postspell-final-halving.md`.
Sodelin, *Guarded root descent after independently unbounded return
spells and odd runs*, node `AC-POSTSPELL-GUARDED-ROOT-DESCENT-001`,
[sections 1–3 of Postspell_Guarded_Root_Descent.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
gives the exact actual-prefix identities

\[
y=(27/16)^J(n+23/11)-23/11,\qquad
z=(3/2)^H(y+1)-1,
\tag{4}
\]

unique parity-residue coding for a finite word, CRT realization, and
residue-20 endpoint membership after the congruent final tail.
The assessment inspected sections 1–5 from live main on 2026-10-04;
no immutable source revision or local Lean build is an input.
Import the identities and coding, rather than reprove general parity
theory or use the source's (a\ge J+H) size margin below its hypotheses.

Substitution in (4) gives (2^{4J+H}z=An+C), with the displayed C.
It is integral since (27\equiv16\pmod{11}), and positive since
both its summands are positive for J,H in the stated range.
Actual final E steps give (m=z/2^a>0). Consequently

\[
m<n\quad\Longleftrightarrow\quad (2^D-A)n>C.
\]

If \(\Delta\le0\), the left side of the last inequality is nonpositive;
if \(\Delta>0\), division gives exactly (1). Equality is not descent.
This retains the positive remainder. The general coefficient/remainder
comparison is also known from Rozier–Terracol,
[*Paradoxical behavior in Collatz sequences*, arXiv:2502.00948v2,
13 February 2025, equations (8)–(9)](https://arxiv.org/html/2502.00948v2).
The result here is a REPRODUCTION specializing inspected machinery,
not an originality claim.

For the membership guard, an actual OOEO block obeys
(16r'=27r+23), so preserves residue 20 modulo 27. From y in that
class, (2^H(z+1)=3^H(y+1)); H>=3 and invertibility of 2 imply
(z\equiv-1\pmod{27}). As (2^{18}\equiv1\pmod{27}) and
(4\cdot20\equiv-1\pmod{27}), actual division by (2^a) yields
(m\equiv20\pmod{27}). These arithmetic checks apply the cited
membership input to exactly the local map conventions.

### Guarded realizability, rather than merely an affine solution

The cited coding theorem supplies exactly one class
(n\equiv r_W\pmod{2^D}) for the D input parities of W. There is no
prescribed parity at the endpoint. The class may be computed by the
source's one-bit recursion: at step i the current affine numerator
has odd coefficient, so the two lifts modulo (2^{i+1}) have opposite
current parities. Choosing the required input bit extends the class.
This is the inspected coding construction, not a claim that final
integrality alone proves every parity.

CRT with (n\equiv20\pmod{27}) gives a unique positive representative
(n_0\in\{1,\ldots,27\cdot2^D\}) and all positive roots

\[
n=n_0+27\cdot2^D k,\qquad k\ge0.
\]

Every such root has actual W; positive shortcut branches preserve
positivity. If \(\Delta>0\), (1) holds for all sufficiently large k,
whereas \(\Delta\le0\) forbids it for every k. More precisely, in the
positive case the first allowable k is

\[
\max\left(0,
 1+\left\lfloor\frac{C-\Delta n_0}
                         {\Delta\,27\cdot2^D}\right\rfloor\right).
\]

This proves the stated if-and-only-if parameter test and infinite
realizability without relying on the bounded computation.

### Ten improved parameter pairs and the least-root implication

Rearranging C gives

\[
0<C=\frac{23A-12\cdot3^H16^J-11\cdot2^H16^J}{11}
  <\frac{23}{11}A.
\]

For (a=20,J\le12,H\le12),

\[
\frac{A}{2^D}
=2^{-20}(27/16)^J(3/2)^H
\le\frac{3^{48}}{2^{80}}
<\frac{11}{34},
\]

the last inequality being the exact integer comparison
(34\cdot3^{48}<11\cdot2^{80}). Hence (\Delta>23A/11>C).
For any positive n, (\Delta n\ge\Delta>C), proving descent.
The ten pairs are
((9,12),(10,11),(10,12),(11,10),(11,11),(11,12),
(12,9),(12,10),(12,11),(12,12)).
They have (21\le J+H\le24), so their old e is 38 and the available
20-step tail lies strictly below it.

Throughout the whole bounded rectangle, (5\le J+H\le24), so e is
20 or 38. Thus the eligible lower exponents are always 2, and also 20
only for the ten pairs. For (a=2),

\[
\frac{A}{2^D}=2^{-2}(27/16)^J(3/2)^H
\ge\frac{3^9}{2^{13}}>1.
\]

All 110 such triples have \(\Delta<0\). This proves their impossibility
for every positive root, not merely for tested representatives.

At the least root n supplied by L014, assume (2) and (v_2(z)\ge20).
Then the next twenty steps are actual E steps. The proven bounds give
a positive residue-20 iterate m<n. Minimality makes m convergent;
appending its finite path to 1 to the actual n-to-m path contradicts
nonconvergence of n. This proves (3) at the unchanged original root.

### An exact-tail family missed by the weaker bound

For (J=11,H=10,a=20), take

\[
\begin{aligned}
n_*&=470239661327756758709339,\\
m_*&=8171720986502293243553.
\end{aligned}
\]

The saved direct replay in `scripts/sharp-postspell/check_sharp.py`
checks each of the 74 input parities of W at (n_*), gives
(T^{74}(n_*)=m_*), and finds (m_*) odd. This is a finite exact
arithmetic verification of a witness, not evidence substituted for an
all-root proof. It may be rerun with
`python3 scripts/sharp-postspell/check_sharp.py`.

Since (A=3^{43},D=74), for every integer (t\ge0) put

\[
n_t=n_*+59049\cdot2^{75}t,\qquad
m_t=m_*+2\cdot59049\cdot3^{43}t.
\]

The root increment is divisible by (2^D), so all W input parities
are preserved by the cited coding theorem. The affine identity gives
the stated m_t, which stays positive and odd. Thus every member has
(z_t=2^{20}m_t) and exactly (v_2(z_t)=20<38), while (m_t<n_t)
by the proved margin. There are no extra final halvings available to
recover the old sufficient guard.

All roots are 47 modulo 243 and 40142 modulo 59049 (776 modulo 19683).
These congruences imply
(v_3(n_t+7)=v_3(4n_t+1)=v_3(128n_t-157)=3), and avoid both fixed
cylinders of L018. Thus the family satisfies the necessary arithmetic
restrictions recorded in L014–L018 and the weaker L019 bound for this
prefix. L020 excludes it as a possible least-root family. These are
ordinary admissible integers, not asserted nonconvergent roots; the
argument does not independently prove their convergence.

The bounded screen checked all 120 triples, three CRT lifts per triple,
the closed offset against branch composition, the strict inequality,
endpoint residue, and three members of this exact-tail family. Results
are saved in `scripts/sharp-postspell/result.json`. The infinite family
and parameter exclusions above have arithmetic proofs; finite replay
checks implementation and the witness. Entry into these words, the
remaining lower-tail cases, and later compensation are still open.

## Mathlib

Full exact postspell criterion, lower final-halving restriction and
supporting affine iteration, parity coding, CRT and valuation coverage:
**not checked**. No matching declaration or library absence is asserted.
The direct source citations are mathematical inputs; the external
repository's pending Lean work is not Mathlib coverage.
