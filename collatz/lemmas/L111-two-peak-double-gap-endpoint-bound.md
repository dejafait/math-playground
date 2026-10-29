# L111 — Endpoint bound for two peaks separated by two even steps

## Hypotheses

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for odd
positive integers. Let n>1 be an integer whose actual finite parity
word before the first j applications of T is

\[
w=1^a0^2\,1^c0^d,\qquad a,c,d\in\mathbb Z_{\ge1},\qquad
j=a+2+c+d.
\]

For q_k equal to the number of ones among the first k bits, assume

\[
3^{q_k}\ge2^k\quad(0\le k<j),\qquad 3^{a+c}<2^j.
\tag{1}
\]

Both odd runs and the intervening two even steps are exact. The last
d even steps are only an observed segment: their maximal run may
continue beyond j. No parity is imposed on y=T^j(n). There is no
minimum, seed, closure, distinctness or primitive-period premise.
Existence of this finite first coefficient drop is assumed only for
the given word, not asserted for arbitrary positive starts.

## Conclusion

The endpoint satisfies

\[
T^j(n)\le n+1.
\tag{2}
\]

Thus any non-descent at j in this family has endpoint n or n+1.
Neither case is excluded here. This is a partial result about the
specified word shape, not universal descent or finite-drop existence.
Its independent critical audit passed on 2026-10-29, within these
hypotheses only.

## Proof

### Exact junctions and the imported finite input

Put

\[
A=3^a,\quad C=3^c,\quad P=2^a,\quad Q=2^c,\quad D=2^d.
\]

L002's exact-run formula, applied to the first complete odd-even
block with even length two, gives a positive odd integer u such that

\[
n=Pu-1,\qquad x=T^{a+2}(n)=\frac{Au-1}{4}.
\]

The second odd run has exact length c. The same odd-run formula in
L002 therefore gives x=Qv-1 for a positive odd integer v. Equating
these expressions for x yields the changed junction identity

\[
Au+3=4Qv.
\tag{3}
\]

For the possibly partial terminal segment use
[Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic
Integers and Euclidean Embedding*, INTEGERS 19 (2019), A8,
Lemma 1, equation (4) and the affine identity in its proof,
printed pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
The finite identity applies to the actual segment `1^c0^d` without
any condition on the parity of its endpoint or maximality of d.
Its additive numerator is
sum_{i=0}^{c-1} 3^{c-1-i}2^i=3^c-2^c. Hence its specialization is

\[
y=\frac{Cx+C-Q}{QD}=\frac{Cv-1}{D}.
\tag{4}
\]

Positive integers are within the source's integer domain. This imports
the finite affine theorem; it does not reprove coding, assume closure
or infer any infinite positive orbit from a residue class. The work
required here is the simultaneous endpoint bound with the changed
middle-run length. L110 motivates this method but its length-one
conclusion is not a premise.

### Retaining every prefix guard

For this word the guards (1) are equivalent to

\[
a\ge4,\qquad 2PQD\le AC<4PQD.
\tag{5}
\]

Indeed, during the first odd run the coefficient ratio is (3/2)^k
and is at least one, including the empty prefix. The two intervening
even steps divide the ratio by two each, with minimum A/(4P).
Their endpoint is a proper prefix because c,d>=1. Since (3/2)^a
increases with a, (3/2)^3=27/8<4 and (3/2)^4=81/16>4, this minimum
is at least one exactly when a>=4. The second odd run increases
the ratio by 3/2 per step. During the final observed even run it
decreases by 1/2 per step. The smallest proper-prefix ratio in that
last portion is AC/(2PQD), at k=j-1; for d=1 this is the end of
the second odd run. The ratio at j is AC/(4PQD).

These observations prove necessity and sufficiency of (5) for all
the guards, without extending the final run or assigning y a parity.
In particular,

\[
\Delta:=4PQD-AC>0,\qquad \frac PA=(2/3)^a\le\frac{16}{81}.
\tag{6}
\]

### The integer increment

Let h=y-n, an integer whose sign is not assumed. Multiply (4) by
4QD and substitute (3) to obtain

\[
4QD y=4Q(Cv-1)=ACu+3C-4Q.
\]

On the other hand, n=Pu-1 gives

\[
4QD y=4QD(Pu-1+h)=4PQDu-4QD+4QD h.
\]

Consequently

\[
\Delta u+4QD h=4QD+3C-4Q.
\tag{7}
\]

All quantities divided by in the following chain are positive.
Since u>0 and Delta>0, (7), the strict final drop AC<4PQD,
and (6) give

\[
\begin{aligned}
h
 &=1+\frac{3C-4Q-\Delta u}{4QD}\\
 &<1+\frac{3C}{4QD}
 <1+\frac{3P}{A}
 \le 1+\frac{16}{27}
 =\frac{43}{27}<2.
\end{aligned}
\tag{8}
\]

The first strict inequality discards positive 4Q+Delta*u; the second
is exactly the final coefficient-drop inequality after division by
positive factors. Integrality of h now gives h<=1, proving (2).
The argument holds for every compatible positive integer start and
all exponents in (1), including d=1 and a partial final even run.

This completes the approved symbolic pass. The local progress is an
adaptation of L110's established method to the changed junction, not
a claimed new general finite-word theorem or certified originality.
The assessed sources did not provide this exact cap. No equality
exclusion, cycle application, enlarged family, numerical census or
universal finite-drop premise has been introduced.

### Independent critical audit (2026-10-29, step548)

**PASS, without a mathematical correction or strengthened conclusion.**
L002's hypotheses hold at both odd starts: the actual following even
bit makes each odd run maximal, and the actual odd bit after the two
middle even steps makes that even run exact. Thus u and v are positive
odd integers, and equating the same chronological x gives (3), including
the factor 4 and the additive 3. No hypothesis about the terminal
endpoint's parity is needed to obtain v.

For an explicit check of the guard coverage, write R_k=3^{q_k}/2^k.
On the four successive ranges its values are

\[
\begin{array}{ll}
R_k=(3/2)^k & (0\le k\le a),\\
R_{a+t}=A/(P2^t) & (0\le t\le2),\\
R_{a+2+r}=A(3/2)^r/(4P) & (0\le r\le c),\\
R_{a+2+c+t}=AC/(4PQ2^t) & (0\le t\le d).
\end{array}
\]

The common endpoints agree. The middle minimum A/(4P) occurs at
a proper prefix; the smallest proper-prefix value in the last range
is AC/(2PQD). When d=1 it is the shared endpoint t=0, not an
unobserved additional even step. These formulas check both directions
of (5), with the strict final inequality kept separate.

The imported affine formula has denominator 2^{c+d}=QD and additive
numerator
\(\sum_{i=0}^{c-1}3^{c-1-i}2^i=(3^c-2^c)/(3-2)=C-Q\).
Substitution of x=Qv-1 gives exactly (4). This checks the finite-sum
specialization, not a reproof of the imported coding theorem. An actual
observed terminal segment suffices, including a partial even run.

Finally, expanding 4QD*y once using (3) and once using y=n+h
gives (7) with the same u. Positivity of 4QD, A, P, Delta and u
justifies every division and the discarded term 4Q+Delta*u>0.
The strict comparison 3C/(4QD)<3P/A is precisely AC<4PQD.
The middle-prefix guard gives P/A<=16/81, so the resulting strict
bound h<43/27<2 applies even when h is negative. Since h is an
integer, h<=1 follows. No equality exclusion, actual descent theorem,
closure assumption or existence of a first drop has entered this audit.

This validates the existing cap only. Reproducing its algebra does not
establish originality or extend it to another word family. Mathlib
coverage remains as qualified below.

## Mathlib

Full matching theorem: **not checked**. Supporting finite-iterate,
valuation and integer-order results: **not checked**; no library
theorem names or direct links were verified. Unknown coverage is not
evidence of absence. The symbolic proof uses the precisely cited
finite input and L002; no computational certificate is required.
