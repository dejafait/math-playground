# L109 — First-drop adjacent swaps do not order least-representative margins

## Hypotheses

Use the shortcut map T(n)=n/2 for even positive integers and
T(n)=(3n+1)/2 for odd positive integers. For a binary word
w=(w_0,...,w_{j-1}) of length j>=1, let q_k=sum_{i<k}w_i, q=q_j and m=2^j.
Say that w is a first-coefficient-drop word if

\[
3^{q_k}\geq 2^k\quad(0\leq k<j),\qquad 3^q<2^j.
\]

Let rho(w) be the least integer n>=2 with parity vector w, and set

\[
A(w)=\sum_{i=0}^{j-1}w_i2^i3^{q-q_{i+1}},\qquad
D=2^j-3^q,\qquad M(w)=D\rho(w)-A(w).
\]

For the one-edge comparison suppose w=u01v and w'=u10v are both
first-drop words of the same length. Put r=|u|, s=#ones(v), and
B=2^r3^s. All representatives below retain the n=1 parity class by
choosing its next member; that entire class is never removed.

## Conclusion

Let R be the representative in {1,...,m-1} of B(3^q)^(-1) modulo m,
and let c=floor((rho(w)-2+R)/m). Then c is 0 or 1 and

\[
\boxed{M(w')-M(w)=D(R-cm)+B.}
\]

The proposed uniform inequality M(u10v)<=M(u01v) is false, even with
both first-drop guards. At j=5,

\[
w=11010,\quad w'=11100,\quad
\rho(w)=11,\quad\rho(w')=23,\quad
A(w)=23,\quad A(w')=19,
\]

and M(w)=32 while M(w')=96. The margin difference is 64>0, where the
proposed certificate required a difference at most zero.

This refutes only that directed sorting certificate. Both displayed
orbits actually descend at their first coefficient drop. It is not a
counterexample to Collatz, to the coefficient stopping time conjecture,
or to the known ordering of additive remainders. No conclusion is made
about a modified order or about all longer words.

## Proof

### Imported finite facts and their specialization

[Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic
Integers and Euclidean Embedding*, INTEGERS 19 (2019), A8,
Lemma 1, equation (4) and its proof, printed pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2)
gives the single residue class of every finite binary word and the
affine identity

\[
3^q n+A(w)\equiv0\pmod{2^j},\qquad
T^j(n)=\frac{3^q n+A(w)}{2^j}
\]

on that class. Thus M(w)=2^j(rho(w)-T^j(rho(w))); strict descent
requires M(w)>0, and equality is not strict descent.
Its prefix-sum convention includes the current bit;
our q_{i+1} is that sum. Since 3^q is invertible modulo 2^j,
the least class member >=2 is its unique member in [2,m+1]:

\[
\rho(w)=2+\bigl((-A(w)(3^q)^{-1}-2)\bmod m\bigr).
\]

Here x mod m denotes the representative in {0,...,m-1}. This is a
finite positive-integer specialization; it asserts no positive
realization of an infinite parity sequence. The source theorem is
imported, not reproved.

[Rozier–Terracol, *Paradoxical behavior in Collatz sequences*,
arXiv:2502.00948v2 (2025-02-13), Definition 2.2 and Lemma 2.1 with
its two-step/common-suffix proof](https://arxiv.org/html/2502.00948v2#S2)
orders the additive remainder E(w)=A(w)/2^j under 01-to-10 swaps.
The displayed two-step difference is 1/4. The common suffix multiplies
that difference by 3^s/2^{|v|}. Therefore its exact numerator
specialization is

\[
A(w)-A(w')=2^j\frac14\frac{3^s}{2^{|v|}}
             =2^r3^s=B.
\]

This only rescales the source calculation. Neither source asserts
the margin order being tested here; the representative change must
also be included.

### The exact representative and margin change

The two sourced congruences and A(w')=A(w)-B give

\[
3^q(\rho(w')-\rho(w))\equiv B\pmod m.
\]

The power of 2 in B(3^q)^(-1) is exactly 2^r modulo m, with r<=j-2,
so this residue is nonzero. Its chosen representative R satisfies
0<R<m. Since 0<=rho(w)-2<=m-1,
0<rho(w)-2+R<2m, so c=floor((rho(w)-2+R)/m) belongs to {0,1}.
Reducing into [2,m+1] yields

\[
\rho(w')=\rho(w)+R-cm.
\]

The common q and j give the same D>0. Substitution now proves

\[
M(w')-M(w)
=D(\rho(w')-\rho(w))-(A(w')-A(w))
=D(R-cm)+B.
\]

In particular, when c=0 both summands are positive. The next explicit
guarded pair has exactly that carry, so no question about the other
carry case is needed to refute the proposed universal inequality.

### Complete guarded witness

Take u=11, v=0; thus the changed bits have indices 2 and 3 when
indices start at zero. The following table checks every prefix,
including the initial equality and the strict final drop.

| k | q_k(11010) | 3^q_k(11010) | q_k(11100) | 3^q_k(11100) | 2^k | Required relation for both |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | 1 | 1 | >= |
| 1 | 1 | 3 | 1 | 3 | 2 | >= |
| 2 | 2 | 9 | 2 | 9 | 4 | >= |
| 3 | 2 | 9 | 3 | 27 | 8 | >= |
| 4 | 3 | 27 | 3 | 27 | 16 | >= |
| 5 | 3 | 27 | 3 | 27 | 32 | < |

The numerator sums give A(11010)=9+6+8=23 and
A(11100)=9+6+4=19. Modulo 32, the inverse of 27 is 19 because
27*19=513=1+16*32. Hence the residue classes are
-23*19=11 modulo32 and -19*19=23 modulo32. The values 11 and 23
are >=2 and their preceding class members are -21 and -9, so they
are precisely the required least representatives.

Their complete direct trajectories, with the five parity-bearing
states before the endpoint, are

\[
11\longmapsto17\longmapsto26\longmapsto13\longmapsto20
  \longmapsto10,
\]
\[
23\longmapsto35\longmapsto53\longmapsto80\longmapsto40
  \longmapsto20.
\]

They have parity vectors 11010 and 11100, respectively. They also
verify the affine endpoints exactly:
27*11+23=320=32*10 and 27*23+19=640=32*20.
Thus D=32-27=5 and

\[
M(w)=5\cdot11-23=32,\qquad
M(w')=5\cdot23-19=96.
\]

For the comparison formula B=4, R=4*19 mod32=12 and
c=floor((11-2+12)/32)=0. Its difference is
5*12+4=64, agreeing with 96-32. This is an exact counterexample
with every required hypothesis checked.

### Reproduction and bounded-search qualification

Run from the active notebook:

```bash
python3 scripts/first-drop-swap-margin/test_swap_margin.py
```

The script saves all checked edges and the full witness to
`scripts/first-drop-swap-margin/certificate.json`. It uses exact
integer arithmetic, increasing length, lexicographic words and
increasing swap index. It prunes only prefixes that have already
dropped and explicitly checks both endpoints' first-drop predicates.
Direct iteration separately checks each representative and endpoint.
The complete `/counterexample` and `/lengths` values were inspected.
There were no verification failures.

Lengths1–4 completed with respectively 1,1,0,1 first-drop words and
no directed guarded edges. At length5 the first checked edge is the
counterexample above, so the script stops. Length5 is incomplete and
lengths6–24 are untested; there is no claim of a complete length24
screen. The written witness proof, rather than any finite-screen
coverage claim, proves the negative conclusion.

The local negative result was obtained under the saved EXPLORE
assessment `drafts/literature/2026-10-28-first-drop-swap-margin.md`.
It changes the route decision; it is not claimed to be original
beyond the sources checked. No new variant was tested after failure.

### Critical audit — 2026-10-28, step537

An independent audit under the saved SPECIALIZE assessment
`drafts/literature/2026-10-28-l109-critical-audit.md` found no defect
in the stated finite result. This validates the existing negative;
it adds no stronger theorem or claim of originality.

The finite inputs have the required hypotheses: Rozier's Lemma1
allows every binary word of positive finite length and identifies its
whole integer congruence class. Restricting that class to n>=2
therefore leaves exactly one representative in [2,m+1]. In particular,
residue0 is represented by m and residue1 by m+1. For example, the
word10 has class1 modulo4; its representative here is5, with
5-to8-to4, whereas1-to2-to1 is excluded only as a starting integer.
No whole parity class or infinite positive realization is discarded
or assumed. The inclusive prefix count in Rozier's Definition2 is
q_{i+1}, so multiplying its inverse formula by3^q gives exactly
the stated A and affine congruence.

Rozier–Terracol's Definition2.2/Lemma2.1 concerns the same shortcut
map and permits empty common words. In its two-step proof the
remainders differ by1/4, and the common suffix has multiplier
3^s/2^{|v|}; its identical additive part cancels. With
j=r+2+|v| this gives A(w)-A(w')=2^r3^s, in the stated direction.
An empty prefix uses E_0=0 from T^0(n)=n, and an empty suffix uses
multiplier1. No assertion about extremal remainders elsewhere in the
source, or about the order of representatives, is used.

For the carry argument, r<=j-2 and the inverse of3^q is odd.
Consequently B(3^q)^(-1) has 2-adic valuation r modulo2^j and
cannot be0; its R lies in [1,m-1]. The sum rho(w)-2+R lies in
[1,2m-2], so its quotient c is0 or1. Subtracting cm puts
rho(w)+R-cm in [2,m+1], and the sourced congruence makes it
rho(w'). This checks both carry cases, including either exceptional
residue representative. D>0 follows from the final first-drop
guard. Substitution gives the displayed difference with no further
guard, minimum, integrality or closure premise.

Every entry of both prefix tables, both complete direct trajectories,
both least representatives, the affine endpoints and the margin
calculation was checked. The witness has R=12,c=0 and difference64
against the proposed upper bound0. Its endpoints10<11 and20<23
are genuine descent, so the counterexample is to the certificate only.

The independent replay command is

```bash
python3 scripts/first-drop-swap-margin/audit_l109.py
```

It recovers A from direct iteration and separately checks the sourced
sum, enumerates the representative interval only to verify the two
existing witness classes, and independently replays the completed
lengths1–4. Their first-drop word lists are respectively {0}, {10},
empty, {1100}, all with no guarded directed edge. Review of the
original DFS confirms that it prunes only an already dropped proper
prefix; at length5 the first surviving word is11010 (the earlier
branches0,10,1100 already drop). The first01 swap at index2 gives
the recorded witness and stops the search immediately. No exhaustive
length5 or longer claim is licensed.

The full selected `/counterexample`, `/lengths`, `/checked_edges`
and `/failures` of the original certificate were inspected. The
replay's complete `/counterexample`, `/checks`,
`/completed_length_replay` and `/failures` were also inspected in
`scripts/first-drop-swap-margin/audit-certificate.json`: all checks
passed, no failures. The original certificate and stopped search
were preserved; no variant or longer search was performed. The
general carry formula is justified by the written argument above,
not by this finite replay. Universal descent, finite coefficient-drop
existence and coefficient-to-actual descent remain independent gaps.

## Mathlib

Full matching coverage for this exact least-representative margin
comparison and counterexample has not been checked. No Mathlib
theorem or formal verification is claimed. Unknown availability is
not evidence of absence. The mathematical imports are the two
precisely cited finite results above; all witness arithmetic is
displayed explicitly.
