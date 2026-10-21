# L021 — Two postspell excursions with compensation below the original root

## Hypotheses

Use the shortcut map T(x)=x/2 for even x and T(x)=(3x+1)/2
for odd x; O and E specify actual input parities. For i=1,2 let
J_i>=2, H_i>=3 and a_i>=0 be integers with a_i congruent to 2
modulo 18. Put W_i=(OOEO)^(J_i) O^(H_i) E^(a_i).
Let a positive n congruent to 20 modulo 27 have the actual concatenation
W_1 W_2, and write x=T^(D_1)(n), y=T^(D_1+D_2)(n), where
D_i=4J_i+H_i+a_i. Every input parity is required; final integrality
alone is not the hypothesis. No first-return or minimal-return claim is made.

The least-root application additionally assumes n is the least
nonconvergent positive residue-20 root supplied by L014.

## Conclusion

Use the single-word constants of L020:

\[
A_i=3^{3J_i+H_i},\qquad q_i=2^{D_i},\qquad
C_i=\frac{23\cdot3^{H_i}(27^{J_i}-16^{J_i})}{11}
 +(3^{H_i}-2^{H_i})16^{J_i}.
\]

Define

\[
A=A_2A_1,\quad C=A_2C_1+q_1C_2>0,\quad
q=q_1q_2,\quad \Delta=q-A,\quad B=A_1-q_1.
\]

Then x,y are positive residue-20 integers and

\[
x=\frac{A_1n+C_1}{q_1},\qquad y=\frac{An+C}{q},\qquad
\boxed{x>n>y\ \Longleftrightarrow\ Bn+C_1>0\ \text{and}\ \Delta n>C.}
\tag{1}
\]

In particular the final descent requires Delta>0 and n>C/Delta.
For fixed word parameters, let n_0 be the least positive representative
of the joint parity class intersected with residue 20 modulo 27, and
M=27q. When Delta>0 define

\[
k_* = \max\left(0,\left\lfloor\frac{C-\Delta n_0}{\Delta M}
                         \right\rfloor+1\right).
\tag{2}
\]

Joint guarded compensation exists exactly when Delta>0 and

\[
B(n_0+Mk_*)+C_1>0.
\tag{3}
\]

If B>=0 and Delta>0, infinitely many actual roots compensate.
If B<0, only the lifts also satisfying n<C_1/(-B) compensate;
this upper bound must not be dropped. At a least bad root with x>n,
the necessary condition is Delta n<=C, so any actual compensating
pair satisfying (1) excludes that root.

There is an infinite actual family with W_1 parameters (2,3,2) and
W_2 parameters (2,3,20), having exactly the stated final-even lengths
and x>n>y. Its roots satisfy the arithmetic necessary conditions
of L014–L018; its first excursion does not descend under L020.
No assertion that any root is nonconvergent is made.

## Proof

### Imported machinery and the required specialization

The ready assessment is
`drafts/literature/2026-10-04-two-postspell-compensation.md` (SPECIALIZE).
L020 gives each positive offset and actual residue-20 endpoint.
Its identities apply to W_2 at the actual positive endpoint x, so
substituting the first formula into the second gives the displayed A,C,q.
Both offsets remain; C>0. Subtracting n gives

\[
q_1(x-n)=Bn+C_1,\qquad q(n-y)=\Delta n-C,
\]

which proves (1), with strict inequalities throughout. Comparing y
only with x would not establish the second inequality in (1).

Import arbitrary finite-word parity coding and CRT realization from
Sodelin, *Guarded root descent after independently unbounded return
spells and odd runs*, node `AC-POSTSPELL-GUARDED-ROOT-DESCENT-001`,
[Postspell_Guarded_Root_Descent.md, sections 2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md).
The prior assessment read sections 1–5, live main, on 2026-10-04;
no immutable revision or checked Lean declaration is assumed.
Supporting general coefficient/remainder comparison and parity coding
appear in Rozier–Terracol,
[*Paradoxical behavior in Collatz sequences*, arXiv:2502.00948v2,
equations (8)–(9), the paragraph before Theorem 2.2 and Lemma 2.3](https://arxiv.org/html/2502.00948v2).
These are supporting results, rather than citations for this complete
two-excursion statement. The local work specializes their machinery
to simultaneous overshoot and descent below the unchanged root;
it is REPRODUCTION, without a priority claim.

The imported coding gives exactly one input-parity class modulo q
for the complete concatenation. Since q is coprime to 27, CRT gives
all its positive residue-20 roots as n_0+Mk, k>=0. No endpoint parity
is presumed. The first endpoint is nevertheless odd because the next
letter, the first letter of W_2, is O. Thus its preceding E tail
is exact: v_2(T^(4J_1+H_1)(n))=a_1.

If Delta<=0, positivity of C forbids descent. If Delta>0, (2) is
exactly the first nonnegative lift with Delta(n_0+Mk)>C.
When B>=0, C_1>0 makes overshoot automatic at every positive root.
When B<0, B(n_0+Mk)+C_1 strictly decreases with k, so no later
descending lift can overshoot if the first one fails (3); if it
succeeds, it is a witness. Division by -B gives the strict upper
bound. This proves the general joint realizability test, including
the finite-interval case.

At the least root of L014, any positive residue-20 iterate y<n
converges by minimality. Its path to 1 appended to the actual n-to-y
path makes n converge, a contradiction. Thus Delta n<=C whenever
the specified actual pair occurs there; assuming x>n does not change
which original root is used. This is conditional exclusion, not
universal entry or compensation.

### A jointly guarded infinite family

For (J_1,H_1,a_1)=(2,3,2), (J_2,H_2,a_2)=(2,3,20),

\[
A_1=A_2=19683,\quad C_1=C_2=31567,\quad
D_1=13,\quad D_2=31,
\]

and hence

\[
A=387420489,\quad C=879930125,\quad q=2^{44},\quad
B=11491>0,\quad \Delta=17591798623927>C.
\tag{4}
\]

Every positive actual realization of this pair therefore has x>n>y:
the achieved margin Delta-C=17,590,918,693,802 is positive, exceeding
the required strict bound Delta n>C already at n=1.

Take

\[
\begin{aligned}
n_*&=1551572790861574235,\\
x_*&=3727979399722700891,\\
y_*&=34169209434065.
\end{aligned}
\]

The finite exact replay in `scripts/two-postspell/check_pairs.py`
checks all 44 input parities of W_1 W_2, gives x_* after 13 steps,
y_* after 44 steps, and finds both endpoints odd. The computed
parity class with an extra O input at the final endpoint is
12,350,488,260,699 modulo 2^45; n_* belongs to it and is 47 modulo
59049. The states just before the two even tails are respectively
14,911,917,598,890,803,564=4x_* and
35,829,012,951,534,141,440=2^20 y_*.
These finite integer checks certify the stated witness; they are
not numerical evidence for an all-start convergence theorem.

For every integer t>=0 put

\[
\begin{aligned}
n_t&=n_*+59049\cdot2^{45}t,\\
x_t&=x_*+59049\cdot2^{32}\cdot19683t,\\
y_t&=y_*+2\cdot59049\cdot387420489t.
\end{aligned}
\tag{5}
\]

The root increments preserve the complete parity class including
the final O guard. The affine formulas give precisely x_t,y_t;
their increments are even, so both endpoints stay odd. Thus the
two pre-tail states equal 4x_t and 2^20 y_t and have exactly
valuations 2 and 20. All roots and endpoints remain positive and
residue 20 modulo 27. Equations (4) prove x_t>n_t>y_t for every t.
The first tail has 2<e(2,3)=20 and grows, while the second tail
repays that growth below the original n_t.

Every n_t is 47 modulo 59049. The residues n_t+7=54,
4n_t+1=189 and 128n_t-157=5859 modulo 59049 each have exact
3-adic valuation 3. The roots avoid 4529 modulo 19683 and 17813
modulo 59049. Thus they meet the necessary arithmetic restrictions
of L014–L018 (valuation 3 is untouched by the lower-row exclusions).
These references compare existing exclusions; their theorems are
not needed to construct or prove (5). This family is excluded as
a hypothetical least root only when the compensating path is used;
the argument does not independently establish convergence of y_t.

### Approved finite screen and limits

The resumed pre-existing script screens 2<=J_i<=12, 3<=H_i<=12,
a_i in {2,20}, with a_1<e(J_1,H_1). L020 proves all 110 first
words with a_1=2 have B>0 and the ten eligible a_1=20 first words
have q_1-A_1>C_1, so can never overshoot any positive root.
There are 120 first choices and 220 second choices.

The exact screen partitions their 26,400 pairs into 2,200 incapable
of first overshoot, 15,361 remaining pairs with Delta<=0, and 8,839
compensating pairs. For 7,225 of the last group Delta>C; for all
8,839 the least positive joint CRT root already meets the strict
descent bound, with no extra lift needed. All concatenations are
replayed; compensating cases are replayed at two successive CRT
lifts. There are 35,239 complete replays with zero failed checks.
The exact coefficients, classes and categories are retained in
`scripts/two-postspell/result.json`; rerun with
`python3 scripts/two-postspell/check_pairs.py`.

This finite screen checks identities and joint applicability; (1)–(3)
and (5) have the all-parameter arithmetic arguments above. No bound
on arbitrary actual itineraries, no universal occurrence of a pair,
and no complete Collatz candidate follows. Attempts 010–011 are
not reopened, and the main eventual-descent gap remains.

## Mathlib

Full two-excursion criterion and supporting affine iteration, parity
coding, CRT and valuation coverage: **not checked**. No matching
declaration or library absence is asserted. The source citations
above support the imported machinery; pending external Lean work
is not Mathlib coverage.
