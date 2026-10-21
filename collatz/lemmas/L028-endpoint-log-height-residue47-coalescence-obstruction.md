# L028 — Endpoint logarithmic height clocks fail on residue 47

## Hypotheses

For positive integers let T(n)=n/2 when n is even and
T(n)=(3n+1)/2 when n is odd. Let S be the positive integers congruent
to 20 modulo 27. Fix a real B>=0. All logarithms are natural; both
clocks count shortcut steps and include zero. No convergence,
least-root or companion assumption is imposed.

## Conclusion

There are unbounded odd positive integers n=47+243k, k>=0, with
v_2(n+1)=4, for which there are no c in S and integers s,t satisfying

\[
0<c<n,\qquad 0\le s,t\le\log(n)/\log(12)+B,
\qquad T^s(c)=T^t(n).                                    \tag{1}
\]

Specifically, for every integer

\[
L\ge L_0=\max\left(6,\left\lceil
\frac{\log(163)+B\log(12)}{\log(2)}\right\rceil\right)
\]

one can select such a root with

\[
4^L<n_L\le4^L+162\cdot6^L<163\cdot6^L.                 \tag{2}
\]

This obstructs the stated endpoint companion cover outside any finite
base. It supplies no nonconvergent start or universal eventual descent.
The separate critical audit of 2026-10-06 below found no defect within
these hypotheses; it certifies no stronger clock or Collatz conclusion.

## Proof

### Assessed inputs and the necessary specialization

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-05-residue47-endpoint-log-coalescence.md`.
Use the audited shifted inverse identity and anchor argument of L026.
L025's offset bound enters through that input. The precise published
parity input reused there is Olivier Rozier, *Parity Sequences of the
3x+1 Map on the 2-adic Integers and Euclidean Embedding*, INTEGERS 19
(2019), A8, [Definition 1, Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
It gives identical first p input parities for integers equal modulo
2^p, including signed integers through its 2-adic formulation.
The other standard input is the named Chinese Remainder Theorem.
Neither standard result is reproved. Laurent's optional separation
theorem is unnecessary and is not applied.

L026 as stated cannot simply be applied at the new roots, since it
requires n>12^L. We replace the only size-dependent part of its
exclusion proof, then verify the remaining proof's hypotheses. This
quantitative difference is why a specialization is needed. No matching
endpoint theorem was established by the recorded search; that does
not certify originality.

### Reduced slopes give the smaller size guard

Fix an integer L>=6 and a positive n satisfying

\[
n\equiv47\pmod{3^{L+4}},\qquad
81n+97\equiv0\pmod{2^{L+1}},\qquad n>4^L.               \tag{3}
\]

The congruences alone give n=47 modulo 64, v_2(n+1)=4,
and the actual first L input symbols O^4 E O^(L-5), as in L026.
For y_t=T^t(n), its exact identities are

\[
y_t+1=K_t(n+q_t),\qquad
(K_t,q_t)=
\begin{cases}(3^t/2^t,1)&0\le t\le4,\\
(3^{t-1}/2^t,97/81)&5\le t\le L.
\end{cases}                                             \tag{4}
\]

Suppose a smaller c in S coalesces with y_t after s steps, where
0<=s,t<=L. Reverse its actual path, retaining all inverse guards.
If a is its number of odd inverses, 0<=a<=s, L026's identity gives

\[
c+1=\lambda(n+q_t)-d,\qquad
\lambda=K_t2^s/3^a,\qquad 0\le d\le2^s-1.               \tag{5}
\]

Set r=t when t<=4 and r=t-1 when t>=5; write h=s-t and j=r-a.
Thus lambda=2^h 3^j, with integer exponents of either sign. For
lambda>1 we claim

\[
\frac{2^s}{\lambda-1}\le4^L.                            \tag{6}
\]

There are exactly three cases.

* If h<0, lambda>1 forces j>0. The positive integer
  3^j-2^(-h) is at least 1, so lambda-1>=2^h. Therefore the
  ratio in (6) is at most 2^(s-h)=2^t<=2^L<=4^L.
* If h>=0 and j>=0, lambda is an integer greater than 1, hence
  lambda-1>=1. The ratio is at most 2^s<=2^L<=4^L. This includes
  either exponent being zero; h=j=0 gives equality lambda=1 and
  is outside the present case.
* If h>=0 and j<0, put b=-j>0. Then lambda=2^h/3^b>1,
  so 2^h-3^b is a positive integer and lambda-1>=1/3^b.
  Also 3^b<2^h. Consequently
  2^s/(lambda-1)<=2^s 3^b<2^(s+h)=2^(2s-t)<=4^L,
  since s<=L and t>=0. If h=0 the assumed inequality is
  impossible, so this introduces no omitted zero case.

These cases exhaust every slope above one. Since n>4^L, (6)
implies (lambda-1)n>2^s. Using q_t>=1 and (5),

\[
c-n=(\lambda-1)n+\lambda q_t-d-1
>2^s+\lambda-(2^s-1)-1=\lambda>0,
\]

contrary to c<n. Thus lambda<=1, including equality. This replaces
L026's coarse unreduced-denominator estimate, without dropping any
offset or any actual-path requirement.

### Reusing the anchor exclusion with all guards

We now use the lambda<=1 part of the audited proof of L026. Its
old bound n>12^L was used to eliminate lambda>1 and, finally, to
ensure n>47. The latter follows here from n>4^L and L>=6. For
clarity, the following checks account for every remaining condition.

Put h=s-t as above. Equation (5), a<=s and lambda<=1 imply h>=0
for t<=4 and h>=-2 for t>=5. Evaluate the same inverse word at
Y_t=K_t(47+q_t)-1, with output c0. Then

\[
c_0+1=\lambda(47+q_t)-d,\qquad c-c_0=\lambda(n-47).       \tag{7}
\]

The unchanged congruences give 64*3^(L+4) dividing n-47.
After multiplication by lambda the binary exponent is h+6>=4.
The ternary exponent is L+4+t-a before the exit and L+3+t-a
after it, each at least 3. Thus c0 is an integer, c0=c modulo 27,
and c0=c modulo 2^(h+6). Since lambda<=1 and d>=0, (7) gives
c0<=47 (after the exit its upper bound is 47+16/81 before
integer rounding). The residue condition leaves c0<=20 or c0=47.

Exactly p=min(s,h+6) symbols of the actual c-path transfer to the
signed anchor c0 by the cited parity coding. The rest are formal
rational branches. If c0<=20, it is 20 or nonpositive; its actual
orbit stays at most 20, as proved in L026. For t<=4 all s symbols
transfer. The possibility c0=47 would give lambda=1,d=0, hence
c=n by (7). Otherwise the output is at most 20 whereas Y_t>=47.
This excludes t<=4, including both zero clocks when applicable.

For t>=5 and c0=47, slope equality again gives c=n by (7).
For lambda<1, (7) and d>=0 force lambda>=243/244. The complete
integer comparisons in L026's section “The exceptional anchor 47”
exclude h=-2,-1,0 and every 1<=h<=53, so h>=54 and p>=59.
Its displayed exact orbit and terminal cycle prove T^p(47)<=40
for every p>=59. These existing finite claims are reused at their
proved scope; none depends on the height of n. The case c0<=20
also gives T^p(c0)<=40 for every p, including zero.

For t=5,6 one has p=s and the output is at most 40, whereas
Y_5=121 and Y_6=182. For t>=7 one has p=h+6 and s-p=t-6.
L026's formal suffix bound gives

\[
F(c_0)+1\le41(3/2)^{t-6}
<183(3/2)^{t-6}=Y_t+1,
\]

contrary to the inverse-word identity F(c0)=Y_t. No parity is
asserted past the transferred prefix. This exhausts lambda<=1
under (3), with no further size assumption. We have therefore
proved the guarded no-companion exclusion through horizon L
for every root (3), rather than applied L026 outside its statement.

### Controlled CRT selection and the endpoint clock

The coefficient 81 is invertible modulo 2^(L+1). Named CRT with
the coprime moduli in (3) gives one class modulo

\[
M_L=2^{L+1}3^{L+4}=162\cdot6^L.
\]

Let 0<=r_L<M_L represent it, H_L=4^L, and choose

\[
n_L=r_L+M_L\left(\left\lfloor
\frac{H_L-r_L}{M_L}\right\rfloor+1\right).
\]

For every real x, x<floor(x)+1<=x+1, including integral or
negative x. Hence H_L<n_L<=H_L+M_L. It satisfies (3) and
(2), since 4^L<6^L for L>=6. In particular n_L>47, and the
ternary congruence gives n_L=47+243k with k>=0. The previously
checked binary congruence gives oddness and valuation 4.

Now fix the stated real B>=0 and take any integer L>=L0.
The definition of L0 implies
L log(2)>=log(163)+B log(12). Using (2),

\[
\begin{aligned}
\log(n_L)/\log(12)+B
&<\frac{L\log(6)+\log(163)+B\log(12)}{\log(12)}\\
&\le\frac{L(\log(6)+\log(2))}{\log(12)}=L.
\end{aligned}
\]

Thus every permitted integer s,t in (1) is at most L, and the
exclusion already proved under (3) applies. This also covers B=0
and equality in the ceiling comparison; the upper height bound
is strict. The roots satisfy n_L>4^L, so they are unbounded as
L tends to infinity. They therefore escape any finite base.

The quantifiers are fixed B, then every sufficiently large integer
L, then a root excluding every permitted companion and both actual
paths. The roots vary with L; no infinite positive orbit or
nonconvergence of any selected root follows. Larger coefficients,
other cylinders and universal eventual descent remain unresolved.

### Focused verification

`python3 scripts/endpoint-coalescence/check.py` checks the changed
reduced-slope estimate for every formal exponent triple at four
finite horizons, and checks CRT selection, exact rational-B clock
inequalities and every prescribed input parity for selected roots.
The full certificate is
`scripts/endpoint-coalescence/certificate.json`. These checks test
transcription and boundary handling; the three-case argument and
real-B inequalities above, not finite samples, prove the conclusion.
L026's unchanged anchor certificate need not be regenerated.

### Critical audit, 2026-10-06

This audit uses the separately approved SPECIALIZE scope in
`drafts/literature/2026-10-05-endpoint-log-coalescence-audit.md`.
The complete proof above, the retained L026 proof and L025's offset
recurrences were checked. No mathematical repair or stronger bound
resulted. L026's theorem is not applied with its size hypothesis
violated: its size-independent proof is reused after the new
large-slope exclusion is established here.

For lambda>1, h<0 requires j>0, so the reduced binary denominator
gives the bound 2^t. With h,j>=0, integrality gives 2^s, including
the cases where one exponent is zero. With h>=0,j<0, the positive
integer numerator gives 2^s 3^(-j)<2^(2s-t)<=4^L. The assumption
lambda>1 excludes h=0 in that last case and excludes h=j=0 in
the preceding case. These cases are exhaustive even though a,s,t
and the word may depend on the selected root. The strict n>4^L
guard then gives (lambda-1)n>2^s; the retained q_t>=1 and
d<=2^s-1 imply c-n>lambda>0. There is no omitted zero-exponent
case or loss of the positive affine offset.

For lambda<=1, a<=s forces h>=0 before the exit and h>=-2
after it. Since n-47 is divisible by 64*3^(L+4), the product
lambda(n-47) has binary exponent at least h+6>=4 and ternary
exponent at least t+4 before the exit or t+3 after it. Hence the
anchor is integral and congruent to c modulo both 27 and
2^(h+6). Its bound c0<=47 uses integrality after the exit.
Only p=min(s,h+6) input parities transfer. No suffix parity or
positivity at the signed anchor is assumed. Nonpositive integers
stay nonpositive under the signed map; the explicit orbit of 20
supplies its bound at all times, including p=0.

If c0=47 and lambda=1, the difference identity gives c=n in
both time ranges; it does not require d=0 after the exit. If
t>=5 and lambda<1, nonnegative d gives lambda>=243/244.
For h=-2,-1,0 the largest possible slopes below one are 3/4,
1/2,1/3 respectively, including all integer ternary exponents.
The complete 53 positive-h comparisons exclude h<=53. Thus
h>=54 gives p>=59, where the complete orbit of 47 and its
terminal 1,2 cycle supply the bound 40 for every later p.
For t<=4 or t=5,6 the whole companion word transfers. For
t>=7 the remaining formal length is precisely t-6, so the
strict coefficient comparison 41<183 gives the contradiction
even for a negative prefix value. This covers s=0, t=0 and
equal slopes. Both original paths remain actual throughout;
only the auxiliary anchor suffix is formal.

The actual n-path follows from the two congruences alone. They
also imply the required binary anchor match, valuation 4 and
residue-20 membership. The only other old height use, n>47,
follows from L>=6 and n>4^L. Thus no hidden n>12^L assumption
survives. The sole direct local DAG input remains L026; L025's
offset bound is used through its fully checked recall in L026.

In the CRT formula, floor(x)+1>x also when x is integral or
negative. It therefore selects the first class member strictly
above 4^L, with upper bound 4^L+162*6^L<163*6^L. Positivity
and k>=0 follow from n>47, rather than from a sign assumption
on the representative multiplier. For every real B>=0, the
ceiling defining L0 yields L log(2)>=log(163)+B log(12).
The strict upper height estimate then makes the real clock
strictly less than L even at a ceiling equality. All permitted
integer clocks are consequently within the proved horizon.
The bound n_L>4^L proves unboundedness without asserting that
the selected representatives are monotone. B is fixed first;
the root may vary with each subsequent L.

`python3 scripts/endpoint-coalescence/audit.py` reads the existing
certificates without rewriting them. It independently checks all
69,529 exponent triples, completeness and every rational field
of the recorded above-one cases; all four CRT selections and
their complete actual paths (80 edges total); all 53 anchor
slope comparisons against the canonical table; and all 66
anchor-orbit edges against the canonical orbit and final cycle.
No failures occurred. Full results and input digests are in
`scripts/endpoint-coalescence/audit-certificate.json`.
The old finite inverse trees are not premises and were not
rerun. The four rational-B witnesses do not prove the arbitrary
real-B assertion; the analytical ceiling argument does. Finite
slope screens likewise do not replace the exhaustive sign proof.

This is local verification of the existing endpoint method
obstruction, not a new theorem, a novelty certification or a
complete candidate resolution. Universal eventual descent,
larger clocks and later arithmetic mechanisms remain open.

## Mathlib

Full endpoint logarithmic-clock residue-20 coalescence obstruction:
**not checked**. Supporting parity coding, CRT, rational arithmetic,
logarithmic monotonicity and floor/ceiling facts: **not checked**.
The published Rozier citation, named CRT and audited local input
suffice for this informal argument. Unknown coverage is not absence;
no Lean verification or complete Collatz solution is claimed.
