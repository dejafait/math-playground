# L110 — Endpoint bound for two peaks separated by one even step

## Hypotheses

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for odd
positive integers. Let n>1 be an integer whose actual finite parity
word is

\[
w=1^a0\,1^c0^d,\qquad a,c,d\in\mathbb Z_{\ge1},\qquad
j=a+1+c+d.
\]

The bits describe the states before the applications of T. For
q_k equal to the number of ones among the first k bits, assume

\[
3^{q_k}\ge2^k\quad(0\le k<j),\qquad 3^{a+c}<2^j.
\tag{1}
\]

Thus j is an assumed finite first coefficient drop. The middle even
run has exactly one step, and both odd runs are exact. The final even
run is only the observed prefix: its maximal length may exceed d.
There is no restriction on the parity of y=T^j(n), no minimum or
closure premise, and no assumption that every trajectory has such a word.

## Conclusion

The endpoint satisfies

\[
y\le n+1.
\tag{2}
\]

If y>n, then y=n+1, c>=2, y is even, and

\[
T^{j+1}(n)=\frac{n+1}{2}<n.
\tag{3}
\]

In particular, **if c=1 and y is even, then y<n already at j**.
This is a restricted first-drop descent result. More generally, unless
y=n, descent occurs by j+1. Neither equality nor unit growth is excluded
for the whole family by this lemma.

The two non-descent cases have the following exact integer reduction.
Write

\[
A=3^a,\quad C=3^c,\quad P=2^a,\quad Q=2^c,\quad D=2^d,
\qquad \Delta=2PQD-AC.
\]

The guards (1) are equivalent, for this word shape, to

\[
a\ge2,\qquad PQD\le AC<2PQD.
\tag{4}
\]

For any exponents satisfying (4), define

\[
\begin{array}{c|cc}
h&N_h&V_h\\ \hline
0&C+2Q(D-1)&PD+A(D-1)\\
1&C-2Q&PD-A.
\end{array}
\tag{5}
\]

There is an actual start of the specified shape with y=n if and only
if Delta divides N_0. There is such a start with y=n+1 if and only if
c>=2 and Delta divides N_1. In either case the start and middle
junction are necessarily

\[
u=N_h/\Delta,\quad v=V_h/\Delta,\qquad
n=Pu-1,\quad x=T^{a+1}(n)=Qv-1,
\tag{6}
\]

with u,v positive odd integers. In the equality case the final even
run has exactly d steps. In the unit-growth case it has exactly d+a
steps, so the observed final run is genuinely partial.

These equivalences do not prove either uniform nondivisibility claim.
They are an exact boundary of the elimination, not a solution of the
remaining two-peak strict-descent problem or of universal descent.

## Proof

### Imported finite input and its applicability

L002 applies to the first complete block: the next odd state occurs
after exactly a odd steps and one even step. It gives a positive odd
integer u with

\[
n=Pu-1,\qquad x=(Au-1)/2.
\]

The exact second odd-run length c gives x=Qv-1 for a positive odd
integer v. Thus

\[
Au+1=2Qv.
\tag{7}
\]

For the possibly truncated second block use
[Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic
Integers and Euclidean Embedding*, INTEGERS 19 (2019), A8,
Lemma 1, equation (4) and its proof, printed pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
The imported finite affine identity applies to every actual finite
parity word. For `1^c0^d` its additive numerator is
sum_{i=0}^{c-1} 3^{c-1-i}2^i=3^c-2^c. Substituting x=Qv-1 gives

\[
y=\frac{3^c x+3^c-2^c}{2^{c+d}}
 =\frac{Cv-1}{D}.
\tag{8}
\]

This only uses the observed d even steps; it does not assume y odd.
The finite affine theorem is imported rather than reproved. The
specialization is to actual positive integer segments, with no
infinite realization or closure assertion. The new work below is
the simultaneous integer elimination at the two junctions.

### Every coefficient guard

During the first odd run the coefficient ratio is (3/2)^k>=1.
Immediately after the middle even step it is A/(2P), which is at
least one exactly when a>=2: for a=1 it is 3/4, for a=2 it is 9/8,
and it increases with a. Each step of the second odd run increases
this ratio by 3/2. During the final even run it decreases by 1/2
per step. Its smallest proper-prefix value on that run is AC/(PQD),
at k=j-1; its final value is AC/(2PQD).
This proves both directions of (4), accounting for all prefixes,
including the empty prefix. In particular Delta is a positive odd
integer and P/A=(2/3)^a<=4/9.

### The integer endpoint increment

Let h=y-n; it is an integer, with no sign assumed yet. Eliminating
v between (7) and (8) and using n=Pu-1 gives

\[
\Delta u+2QD h=2QD+C-2Q.
\tag{9}
\]

Indeed, multiplying (8) by 2Q gives
2QDy=ACu+C-2Q, whereas
2QDy=2PQDu-2QD+2QD h. All factors divided by below are positive.
Since u>0 and Delta>0,

\[
h=1+\frac{C-2Q-\Delta u}{2QD}
 <1+\frac{C}{2QD}
 <1+\frac PA
 \le\frac{13}{9}<2.
\tag{10}
\]

The second strict inequality is AC<2PQD. Integrality therefore gives
h<=1, proving (2). If h>0 it must equal one. Equation (9) then says

\[
\Delta u=C-2Q>0,
\]

so (3/2)^c>2, which forces c>=2. Since n is odd, y=n+1 is even;
(3) follows because n>1. If c=1, positive h is impossible. When
also y is even, h=0 is impossible because n is odd, and hence y<n.
This proves the stated strict-descent subcase without assuming the
final even run maximal. If h<0 there was already descent at j;
these observations also prove the claim for every case except y=n.

### Necessity and sufficiency of the surviving divisor conditions

Suppose first that an actual word has h=0 or h=1. Equation (9)
gives Delta*u=N_h. Substitution into (7) gives Delta*v=V_h;
equivalently, in both rows of (5),

\[
A N_h+\Delta=2Q V_h.
\tag{11}
\]

Thus the claimed divisibility is necessary, and c>=2 is necessary
for h=1. It also follows that the start is uniquely determined for
fixed exponents and h.

Conversely, fix exponents satisfying (4). For h=0 assume Delta
divides N_0. For h=1 assume c>=2 and Delta divides N_1. In either
case N_h is positive and odd, so u=N_h/Delta is a positive odd
integer. Since Delta is odd, it is coprime to 2Q. Identity (11)
shows that Delta also divides V_h. Both V_h are odd: PD is even,
D-1 is odd, and A is odd. Hence v=V_h/Delta is an odd integer.
Dividing (11) by Delta gives Au+1=2Qv, so v>0 as well, including
the h=1 case where positivity of PD-A was not assumed separately.

Set n=Pu-1 and x=Qv-1. Since P>=4 and u>=1, n>=3. The odd-run
formula in L002 shows that n has exactly a initial odd steps.
Equation (7) yields

\[
Au-1=2(Qv-1)=2x,
\]

where x is positive and odd; the next even run is therefore exactly
one step. Because v is odd, the next odd run has exactly c steps.
After them the value is Cv-1. Directly from (5),

\[
C V_h-PD N_h=\Delta\bigl(1-D+Dh\bigr),
\]

and division by Delta gives

\[
Cv-1=D(Pu-1+h)=D(n+h).
\tag{12}
\]

Here n+h is positive. Thus the next d states before application of
T are all even, and after these steps the actual endpoint is n+h.
No parity condition on that endpoint was used to establish the
observed word. The prefix analysis already proves (1).

For h=0 the endpoint n is odd, so (12) has exact 2-adic valuation d.
For h=1 the endpoint is n+1=Pu, with u odd, so (12) has exact
2-adic valuation d+a. These are the two asserted final-run cases
and complete the converse.

### Scope and remaining obstruction

The single symbolic pass stops at (5). Neither Delta not dividing
N_0 for all (4), nor Delta not dividing N_1 for all (4) with c>=2,
has been proved here. An equality candidate would be a closed actual
word; no closed-cycle exclusion is silently invoked. A unit-growth
candidate would be an actual first-drop non-descent word, followed
immediately by descent; no such candidate is exhibited or ruled out
by the formulas alone. In particular, failure to exclude a divisor
is not a counterexample and is not evidence for one.

The bound and the c=1 even-endpoint subcase are local mathematical
progress under the saved EXPLORE assessment. The sources checked
did not supply a matching theorem; this is not a verified originality
claim. Other intervening even-run lengths, more peaks, and existence
of finite coefficient drop remain unresolved. No enumeration or
mathematical script supports the proof. The separate critical audit below
accepts these claims without strengthening them.

### Critical audit (step541, 2026-10-28)

The audit used the prior SPECIALIZE assessment
`drafts/literature/2026-10-28-l110-critical-audit.md`, L002's full proof,
and the assessed Rozier2019 finite input. No additional mathematical
input, maximal-terminal-run assumption or cycle theorem was used.

All proper-prefix ranges in (1) are covered. The first run increases
the ratio from 1; the middle zero gives its first subsequent minimum
A/(2P), at the proper prefix a+1. The next run increases the ratio;
the last run has minimum proper-prefix value AC/(PQD), including d=1,
when j-1 is the end of the second odd run. These are exactly the two
lower tests in (4); AC/(2PQD)<1 is the final test. Thus both directions
of (4) retain every guard. The two source specializations retain the
actual integer domain: the first block is complete with even length 1,
whereas (8) divides the second even value by only the observed D.

Equating the two expressions for 2QDy verifies (9) without presuming
h>=0. In (10), the discarded numerator terms 2Q and Delta*u are
strictly positive; AC<2PQD gives C/(2QD)<P/A, and a>=2 gives P/A<=4/9.
Hence h<13/9<2, so the integer bound is h<=1, not merely a real bound.
For h=1 the equation Delta*u=C-2Q excludes c=1; n odd makes y even,
and (n+1)/2<n uses exactly n>1. For c=1 and even y, parity excludes
h=0 as well. No sign assumption or endpoint parity was lost.

For the converse, direct expansion of A*N_h+Delta yields respectively
2Q[PD+A(D-1)] and 2Q(PD-A), verifying both rows of (11).
Expanding C*V_h-PD*N_h yields respectively (D-1)(AC-2PQD)
and 2PQD-AC, verifying (12) for h=0 and h=1. Delta and both N_h
are odd; their positivity uses D>=2 for h=0 and c>=2 for h=1.
Since gcd(Delta,2Q)=1, (11) transfers divisibility to V_h.
Each V_h is odd, and Au+1=2Qv proves v>0 even when the sign of
PD-A was not known beforehand. Thus the reconstructed parameters
are positive odd integers, with n>=3 and x>=1.

L002 now gives exactly a first odd steps, followed by the even value
Au-1=2x with x odd: the middle even run has exactly length 1.
The representation x=Qv-1 with v odd gives exactly c next odd steps.
Equation (12) supplies all d following even states, because n+h>0.
Finally n odd makes the terminal valuation exactly d for h=0;
n+1=Pu with u odd makes it exactly d+a for h=1. The guard check
depends only on the unchanged exponents and therefore also applies
to these reconstructed words. This verifies necessity, sufficiency,
and uniqueness for each fixed exponent triple and h.

Result: every stated bound, strict subcase and divisor equivalence
passes. No proof repair, stronger theorem, divisor exclusion or new
originality claim results from this audit. The unresolved conditions
in (5) and the independent universal-descent gaps remain unchanged.

## Mathlib

Full matching coverage for (2), the strict-descent subcase and the
two divisor equivalences is **not checked**. Supporting arithmetic,
iteration and valuation coverage is also **not checked**; no Mathlib
theorem is assumed. Unknown availability is not evidence of absence.
The finite affine input is the precise source theorem cited above.
