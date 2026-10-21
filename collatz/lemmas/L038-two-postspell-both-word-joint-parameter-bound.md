# L038 — Joint logarithmic restriction at both postspell boundaries

## Hypotheses

Use the shortcut map T(t)=t/2 for even positive integers and
T(t)=(3t+1)/2 for odd positive integers. O and E denote actual
input parities. For i=1,2 let J_i>=2, H_i>=3 and a_i>=0 be
integers, with a_i congruent to 2 modulo 18. Define

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=D_1+D_2.
\]

Assume W_1W_2 is actual at a positive odd integer n>1,
x=T^{D_1}(n) is positive and odd, both n and x are congruent
to 20 modulo 27, and T^N(n)=n. Both final even tails are exact.
No least-root, first-return, primitive-period, distinct-junction,
consecutive-minimum or relative-growth assumption is imposed.
Independent tails, repeated periods and x=n are admitted.
All logarithms are natural.

## Conclusion

\[
\boxed{\max(4J_1+H_1,4J_2+H_2)<144\log N+95.}       \tag{1}
\]

Thus A=144, B=95 satisfy the approved non-strict bound as well.
This necessary conditional restriction bounds both words' odd-prefix
parameters relative to represented N. No absolute upper bound on N
or exclusion of positive integer closure is established here. The two independent tails, entry
into this language, other cycles, divergent orbits and universal
eventual descent remain unresolved. The separate critical audit below
found no defect; this is not a complete Collatz candidate.

## Proof

### Reused effective input at the smaller junction

Let i=1 if n<=x and i=2 otherwise. Let b be that selected starting
junction, and m the endpoint of its own word. Thus (b,m)=(n,x)
if i=1 and (b,m)=(x,n) if i=2. In both cases this word and the
word starting at m are actual parts of the given closed orbit.
Use J=J_i, H=H_i, a=a_i and s=b+23/11. Define

\[
K=3(J_1+J_2)+H_1+H_2,\qquad
L=J_1+J_2+a_1+a_2,\qquad N=K+L.
\]

Since a_i>=2, K>=18 and L>=8, so 1<K<N. Both junctions
are positive odd integers 20 modulo 27, hence at least 47.
In particular s>=540/11>0.

L037 applies with exactly these hypotheses and the same selected
index. Its equation (5) and its conclusion give

\[
0<\log s<\frac{133}{10}\log K+8
               <\frac{133}{10}\log N+8,
\qquad 4J+H<50\log N+33.                              \tag{2}
\]

For clarity about the imported inputs behind this estimate, L037
uses John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117
(2005), 51–70,
[Lemma 12, printed p. 61, and section 1.2, printed p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
together with Christian Hercher, *There are no Collatz m-Cycles
with m <= 91*, JIS 26 (2023), Article 23.3.5,
[Theorem 16 and proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf).
The latter is applied through L035's occurrence-mass specialization.
The cycle is nontrivial because it contains n outside the invariant
shortcut cycle {1,2}. L037 already checks both imported estimates
with represented K,N, including nonminimal periods and x=n.
We reuse its resulting estimate (2); no general cycle theorem is
reproved. Rhin's input and source computations remain imported by
these precise citations, not independently certified locally.

### Transfer through that selected word

Let y=T^{4J}(b) and z=T^{4J+H}(b). L031's exact actual-word
identities give, with G=(27/16)^J(3/2)^H,

\[
y=\left(\frac{27}{16}\right)^J s-\frac{23}{11},
\qquad
z=\left(\frac32\right)^H(y+1)-1
  =Gs-\frac{12}{11}\left(\frac32\right)^H-1,
\qquad m=\frac{z}{2^a}.                              \tag{3}
\]

Both shifts are retained. All states are positive and all a final
steps are actual even steps. Since a>=2 and G>1, (3) implies

\[
m+\frac{23}{11}
 <\frac{Gs}{2^a}+\frac{23}{11}
 \le\frac{Gs}{4}+\frac{23}{11}<Gs.                    \tag{4}
\]

The last comparison follows from Gs>=s>=540/11, since
(3/4)(540/11)=405/11>23/11. No upper bound on a is used.
This is a consequence of following the selected word to its actual
endpoint, not an assumed comparability of n and x.

We have 27/16<(3/2)^4=81/16. Also log(3/2)<1/2 by
log(1+t)<t for t>0 (proved in L037). Since J,H are positive,

\[
\log G=J\log(27/16)+H\log(3/2)
 <(4J+H)\log(3/2)<\frac{4J+H}{2}.                   \tag{5}
\]

Taking logarithms in (4) and using (2) and (5), all at positive
arguments, gives

\[
0<\log\left(m+\frac{23}{11}\right)
 <\log s+\log G
 <\frac{383}{10}\log N+\frac{49}{2}.                 \tag{6}
\]

The constants are exactly 133/10+50/2=383/10 and 8+33/2=49/2.
This argument works when the selected word is W_2 as well as W_1;
it does not treat the designated junctions as consecutive minima.

### Use each junction's own valuations and intermediate height

For either actual word, denote its starting junction by r, its
parameters by J_r,H_r,a_r, and its B^{J_r} endpoint by y_r,
where B=OOEO. Set s_r=r+23/11. L031 gives

\[
11r+23=2^{4J_r+2}u_r\quad(u_r\text{ positive odd}),
\qquad v_2(y_r+1)=H_r,
\qquad y_r+1=\left(\frac{27}{16}\right)^{J_r}s_r-\frac{12}{11}.
\]

These are this word's own identities with its independent exact
tail. In particular the terminal identity
2^{H_r}(2^{a_r}r'+1)=3^{H_r}(y_r+1), where r' is the
positive odd endpoint, gives v_2(y_r+1)=H_r because a_r>=2.
No endpoint is identified with the global cycle minimum.

Since u_r>=1 and 2^{H_r}<=y_r+1, taking logarithms gives

\[
4J_r\log2\le\log s_r+\log(11/4),
\qquad (4J_r+H_r)\log2<J_r\log27+\log s_r.
\]

Substitute the first inequality into the second, with positive
coefficients and divisors, to obtain

\[
4J_r+H_r<
 \left(\frac{\log27}{4(\log2)^2}+\frac1{\log2}\right)\log s_r
 +\frac{\log27}{4(\log2)^2}\log(11/4).
\]

L037 proves the elementary estimates log2>2/3, log27<4,
and 0<log(11/4)<4/3 by a derivative inequality and positive
exponential-series terms. With log s_r>0 these give

\[
4J_r+H_r<\frac{15}{4}\log s_r+3.                   \tag{7}
\]

We have written the applicability and algebra here because L037's
conclusion selects only b, whereas (7) uses the other word's own
height and valuations. This repeats only the elementary combination
needed for the new target, not a general finite coding proof.

Apply (7) at r=m and use (6):

\[
4J_m+H_m
 <\frac{15}{4}\left(\frac{383}{10}\log N+\frac{49}{2}\right)+3
 =\frac{1149}{8}\log N+\frac{759}{8}
 <144\log N+95.                                    \tag{8}
\]

Here J_m,H_m denote the parameters of the word starting at m,
even when m=b as integers. The rational differences in the last
comparison are 144-1149/8=3/8 and 95-759/8=1/8, and log N>0.
At the selected index, (2) gives the smaller bound
50log N+33<144log N+95. Thus (1) follows for both indices.
If x=n, the prescribed index choice is i=1 and (3)–(8) still
apply to W_2 at its actual starting occurrence. Repeated states
and repeated representations never change this argument.

### Scope and limitations

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-07-two-postspell-both-word-joint-bound.md`.
This is REPRODUCTION: an elementary junction transfer and quantitative
combination of ready finite-word identities with the imported effective
cycle estimates. No originality or mathematical advance beyond the
sources checked is claimed. No finite screen or numerical approximation
is used to prove the constants.

Attempt 019's guard-only failure and history 069's full-minimum-count
mismatch remain valid. The present conditional bound uses L037's
independent linear-form input rather than another guard-only exclusion.
It removes the previous lack of any logarithmic bound on the other
word's prefix parameters. A later use might constrain K during closure
analysis, but no such further result is asserted here. Independent
tails, total N, integer divisibility, universal entry and eventual
descent remain open. The separate audit below checks the statement
and transfer without strengthening the conclusion.

### Separate critical audit

The 2026-10-08 audit used the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-08-two-postspell-both-word-audit.md`.
It read complete L038, L037, L031 and L036, and L035's finite-mass
proof and represented-cycle application. The working record is
`drafts/2026-10-08-two-postspell-both-word-audit.md`.
The statement, constants and direct mathematical inputs are unchanged.

**Effective input and represented counts.** Each OOEO has three odd
and one even inputs, giving exactly the displayed K,L,N. The allowed
tails have a_i>=2, so K>=18,L>=8 and 1<K<N. A positive odd
integer 20 modulo 27 is 20+27t with t a positive odd integer;
therefore both junctions are at least 47. The closed orbit containing
n outside the invariant set {1,2} is nontrivial. These are exactly
L037's hypotheses. Choosing the smaller junction once, with i=1 in
the tie, gives both inequalities (2) for that same word. In particular
s>=540/11>1, so its logarithm is positive.

The published lower bound and the occurrence-mass upper bound are
imported through L037, with the precise citations above. Their scopes
match the actual closed representation, rather than a presumed global
minimum. For a repeat factor q>=1, write K=qK_0,N=qN_0 and
Lambda=q Lambda_0. The primitive lower bound implies
q Lambda_0>q e^{-6.125581}K_0^{-13.3}
>=e^{-6.125581}(qK_0)^{-13.3}. L035's primitive state sums agree
with time occurrences, and its represented sums multiply by q, giving
its upper bound for the same K,N. Thus repeated representations do
not invalidate the selected-junction size estimate. Source computations
and Rhin's proof remain published imported inputs; this audit does
not claim to certify them independently.

**Actual transfer and both shifts.** If i=1, the selected word runs
from n to x. If i=2, it runs from x to n using actual closure.
For either index the exact identities are
y+1=(27/16)^J s-12/11 and
z=Gs-(12/11)(3/2)^H-1, followed by m=z/2^a.
Thus z<Gs strictly, while z and m are positive actual states.
Adding 23/11 to m and using a>=2 gives the first two comparisons
in (4). For the last one,
(3/4)Gs>=405/11>23/11, so Gs/4+23/11<Gs.
The +23/11 in s and in the endpoint height, and the -12/11
in the intermediate height, are all retained. Neither an upper
bound on a nor an assumed ratio between junction heights enters.

Since 27/16<(3/2)^4 and J>0,
log G<(4J+H)log(3/2). L037's inequality log(1+t)<t
with t=1/2 gives log G<(4J+H)/2. Logarithms in (4)
are legitimate and positive because m>=47. Adding L037's two
strict upper estimates therefore gives (6), with exact coefficients
133/10+25=383/10 and 8+33/2=49/2. This checks the
only transfer from the selected word to the other starting occurrence.

**Each word's own height and valuation.** At any of the two word
occurrences r, its actual endpoint r' is positive odd. The terminal
identity 2^{H_r}(2^{a_r}r'+1)=3^{H_r}(y_r+1) and a_r>=2
give v_2(y_r+1)=H_r. Write y_r+1=2^{H_r}v with v positive
odd. Since H_r>=3,
11y_r+23=4(11*2^{H_r-2}v+3) has valuation exactly 2.
The affine identity
16^{J_r}(11y_r+23)=27^{J_r}(11r+23)
then yields v_2(11r+23)=4J_r+2. This uses the word's own
tail and intermediate state, including for the other index; it is
not an application of L037's selected-index conclusion to both words.

Put s_r=r+23/11. Positivity gives 11s_r>=2^{4J_r+2},
hence 4J_r log2<=log s_r+log(11/4). Also
2^{H_r}<=y_r+1=(27/16)^{J_r}s_r-12/11
<(27/16)^{J_r}s_r. Taking logs, adding 4J_r log2 and
substituting the first upper bound for J_r yields exactly the
coefficient formula preceding (7). Every divisor and multiplier
in that substitution is positive. The -12/11 makes it strict.

L037's exact elementary estimates give
log27/[4(log2)^2]<9/4, 1/log2<3/2, and
0<log(11/4)<4/3. They follow from log2>2/3 and the
positive exponential-series sum 293/81>3 for e^{4/3};
no rounded logarithm is used. Since log s_r>0, substitution gives
(7), including its strict additive bound (9/4)log(11/4)<3.
Applying it to m and then (6) gives
(15/4)(383/10)=1149/8 and (15/4)(49/2)+3=759/8.
The final comparison has positive gap (3/8)log N+1/8.
At b, the smaller bound from (2) is also strictly below
144 log N+95, since log N>0. Thus both indices satisfy (1).

If x=n, i=1 by definition, and m names W_2's starting occurrence
even though its integer value equals b. All identities still apply
to that word's own J_2,H_2,a_2. This also explains why repeated
states cause no accidental identification of parameters. No junction
or intermediate height is asserted to be the global minimum, and
no successive-minimum theorem, primitive-period assumption, relative
growth condition, least-root filter or upper tail bound is used.

The audit found no defect, repair or stronger conclusion. It verifies
the conditional local REPRODUCTION, without claiming originality or
progress beyond the checked source mathematics. Attempt 019's guard-only
failure and history 069's full-minimum-count mismatch remain valid.
The audited bound alone does not supply an upper bound on total N,
an integer-closure exclusion, universal entry or eventual descent.

## Mathlib

Full matching both-word restriction, Simons–de Weger's effective input,
Hercher's cycle inequality and supporting valuation/logarithm results:
**not checked**. No matching declaration or absence from Mathlib is
asserted. The cited inputs and complete elementary specialization above
are the informal evidence.
