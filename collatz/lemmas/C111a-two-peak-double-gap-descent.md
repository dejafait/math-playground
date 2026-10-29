# C111a — Descent for two peaks separated by two even steps

## Hypotheses

Let T be the shortcut Collatz map on positive integers, with T(z)=z/2
for even z and T(z)=(3z+1)/2 for odd z. Let n>1 be an integer whose
actual parity word before the first j applications of T is

\[
1^a0^2\,1^c0^d,\qquad a,c,d\in\mathbb Z_{\ge1},\qquad
j=a+2+c+d.
\]

For q_k the number of ones among the first k bits, assume every guard

\[
3^{q_k}\ge2^k\quad(0\le k<j),\qquad 3^{a+c}<2^j.
\tag{1}
\]

These are exactly L111's hypotheses. Both odd runs and the middle
two-step even run are exact. The last d even steps are an observed
segment whose maximal run may continue beyond j. No parity is imposed
on y=T^j(n). There is no closure, global-minimum, least-period or
distinctness assumption, nor an assertion that every positive start
has a finite first coefficient drop. The first bit implies that n is odd.

## Conclusion

The endpoint y is not n. Exactly one of the following holds:

- y<n, giving descent at j;
- y=n+1, which is even, and T^{j+1}(n)=(n+1)/2<n.

Thus some r in {j,j+1} satisfies T^r(n)<n. This is a restricted
family theorem. It neither excludes unit growth at j nor proves
universal descent or finite coefficient-drop existence. The local
specialization below passed its separate critical audit on 2026-10-29
(step552), under exactly the stated hypotheses.

## Proof

### Published cycle input and its qualifications

Import John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005),
51–70, DOI 10.4064/aa117-1-3,
[Theorem 3(b), printed p.55](https://www.impan.pl/shop/en/publication/transaction/download/product/82263#page=5).
It excludes nontrivial m-cycles for 1<=m<=68; only m=2 is used here.
The map in section 1.1, printed p.51, is this same shortcut map, and a
nontrivial cycle contains an integer greater than 2. Section 1.2, p.52,
counts local minima by their positions in a displayed period. The
period need not be least, and the starting minimum need only be local.
The m-fold repetition of {1,2} is explicitly the trivial m-cycle.
In particular the theorem has no requirement that the two even-run
lengths be one or that the numerical minima be distinct.

The m=2 case is included in Lemma 15 and its complete proof, printed
p.62, which uses Lemma 14 and Corollary 11. Section 1.3, pp.52–53,
records the external computational bound X0=301*2^50 behind these
estimates. This proof imports the published theorem with that
computational basis; it does not independently replay those computations
or reprove the cycle exclusion. No additional unproved conditional
hypothesis is attached to the cited theorem. The source coverage for
this exact specialization was assessed before this application.

### Equality would give a nontrivial m=2 cycle

Assume for contradiction that y=n, and write n_i=T^i(n). All states
are positive integers. The equality n_j=n_0 and determinism of T imply
n_{i+j}=n_i for every i>=0, so j is an actual displayed period. We
keep that period and the original chronological states; j is not assumed
to be the least period.

For a positive odd z, T(z)-z=(z+1)/2>0; for a positive even z,
T(z)=z/2<z. The actual word therefore gives precisely four successive
strictly monotone segments:

\[
n_0<\cdots<n_a>n_{a+1}>n_{a+2}
 <\cdots<n_{a+2+c}>\cdots>n_j=n_0.
\tag{2}
\]

The inequalities on each increasing segment include all of its a or c
steps, respectively; the last decreasing segment has exactly d steps.
Both internal switches are actual parity switches. At the cyclic
boundary, n_j=n_0 is odd, whereas n_{j-1} is even. Consequently the
observed terminal even run ends at j in this equality case: it cannot
continue past j. In particular n_{j-1}=2n>n and n_1>n, so position
0 is a strict local minimum in the displayed cycle.

All run lengths are positive. The two local minimum positions and the
two local maximum positions are therefore exactly

\[
t_0=0,\quad t_1=a+2;\qquad
s_0=a,\quad s_1=a+2+c,
\]

with 0<s_0<t_1<s_1<j. There are no other local extrema, because every
interior point of a run lies on a strict monotone segment. This matches
the source's chronological parameters

\[
(k_0,l_0,k_1,l_1)=(a,2,c,d),\quad
K=a+c,\quad L=2+d,\quad p=K+L=j.
\tag{3}
\]

Thus the actual orbit is an m=2 cycle in the source's positional sense.
Coincident numerical minima or a repeated shorter period would not
invalidate this match. We have neither rotated to a global minimum nor
discarded any repetition.

Since n is odd and n>1, it is at least 3. This cycle contains an integer
greater than 2, so it is nontrivial; in particular it cannot be the
repeated trivial cycle {1,2,1,2}. The m=2 instance of Theorem 3(b)
contradicts its existence. Hence y is not n. The first-drop guards were
not needed for this equality-only import, but remain in the hypotheses
for the cap application below.

### The open-endpoint alternatives

Apply audited L111 to the original n,a,c,d and every guard (1). It gives
the integer bound y<=n+1, without any closure or terminal maximality
premise. For integers y,n, this bound and y!=n imply that either y<n
or y=n+1. The former already gives the asserted descent at j.

In the latter case n is odd, so y=n+1 is even. The next actual step is

\[
T^{j+1}(n)=T(y)=\frac{n+1}{2}<n,
\]

where the strict inequality is equivalent to 1<n. This even step is
allowed to continue the terminal run beyond j. The terminal exactness
proved under equality has not been assumed in this open-endpoint case.
Both alternatives retain d=1 and every other permitted d, all proper
prefix guards and the strict final coefficient drop.

This completes the approved specialization and elementary combination.
The cycle theorem was applied only to an actual closed orbit under
hypothetical equality, never to an open endpoint or a formal affine
solution. L111 is the only local lemma input. C110a is a comparison of
methods, not a premise; its length-one statement was not applied here.
This is local reproduction of assessed mathematics, not a claim of a
new cycle theorem or progress beyond the sources' cycle exclusion.

### Independent critical audit (2026-10-29, step552)

**PASS, with no mathematical correction or extra hypothesis.** The
following checks validate this specialization and its combination with
L111, rather than independently verifying the published computation.

First, under equality alone, positivity and integrality are preserved
at every iterate and determinism repeats the complete chronological
segment of length j. The final observed even input n_{j-1} then maps
to n_j=n, which is odd because the first bit is 1. Consequently that
even run has exactly d steps in the closed word. This proves the
terminal exactness required by the cycle parameters only in the case
where it is used; it imposes no condition on an open endpoint.

Second, the sign of each step difference is positive at an odd input
and negative at an even input. A strict local maximum therefore occurs
exactly at a change from an odd input step to an even input step, and
a strict local minimum exactly at the opposite change, with indices
taken modulo j. The given word has exactly the four changes listed
in (2): maxima at a and a+2+c, minima at a+2 and 0. Since a,c,d>=1,
their ordering is 0<a<a+2<a+2+c<j; these are four distinct positions,
even when d=1. There are no additional extrema inside any run.
In particular the boundary minimum has neighbors n_{j-1}=2n>n
and n_1=(3n+1)/2>n. Thus (3) matches every run in the source's
displayed m=2 period, not merely two selected minima of a longer
unclassified word. Numerical values at distinct positions may coincide.
A shorter least period is allowed by the cited convention, so neither
coincident minima nor repetition changes this application.

Third, the source's exceptional trivial m-cycle contains only 1 and 2.
Here the original n is odd and greater than 1, hence n>=3, so the
closed orbit is nontrivial. This checks the exception at the actual
starting position without assuming a global minimum or choosing a
different representative. The same shortcut map, m=2 within 1<=m<=68,
positive run lengths (a,2,c,d), actual closure and nontriviality are
all present. Theorem3(b) therefore excludes equality with its stated
computational basis retained; no source theorem is used on an open
trajectory or on a merely formal affine solution.

Finally, the original tuple n,a,c,d,j and every guard (1) match L111
verbatim. The audited cap y<=n+1 and the equality exclusion exhaust
the integer alternatives: y<=n-1 or y=n+1. In the second case the
original odd n makes y even, and its next actual iterate is
(n+1)/2<n because n>1. This argument permits the observed terminal
run to continue past j; it does not import the equality case's
terminal exactness. It includes d=1, repetitions and all proper-prefix
guards. Hence the asserted r is indeed j or j+1 under every stated
hypothesis. L111 remains the sole direct local input; C110a remains
a comparison. Other word shapes, finite coefficient-drop existence
and universal eventual descent are not established by this audit.

## Mathlib

Full matching coverage of this descent statement and the imported
m=2 exclusion is **not checked**. Supporting finite-iteration, parity
and integer-order coverage is also **not checked**; no Mathlib theorem
is assumed or claimed absent. The published theorem is cited precisely
above. L111 supplies the cap, and the remaining applicability and parity
arguments are written out here; no numerical certificate is needed.
