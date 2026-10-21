# L041 — Count-dependent represented length of closed postspell words

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for
odd positive integers. O and E specify actual input parities. Let r>=3
be an integer. For 0<=i<r let J_i>=2, H_i>=3 and a_i>=0 be integers,
with a_i congruent to 2 modulo 18. Put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\quad
D_i=4J_i+H_i+a_i,\quad N=\sum_{i=0}^{r-1}D_i.
\]

Assume the concatenation W_0...W_(r-1) is actual at a positive odd
integer n_0>1, is closed with T^N(n_0)=n_0, and has positive odd
junctions n_i=T^(D_0+...+D_(i-1))(n_0), each 20 modulo 27.
Each final even tail is exact. Set n_r=n_0. Independent tails, repeated
periods and coincident junctions are allowed. No least-root,
first-return, primitive-period, global-minimum or relative-height
assumption is imposed. All logarithms are natural.

## Conclusion

Define the explicit positive functions

\[
Q_r=\sum_{j=0}^{r-1}\left(\frac{23}{8}\right)^j
    =\frac{8}{15}\left(\left(\frac{23}{8}\right)^r-1\right),
\qquad A(r)=\frac{399}{5}Q_r,
\]
\[
B(r)=\left(\frac{264}{5}+6\log r\right)Q_r
       +\frac{69r}{1034}.
\]

Every representation satisfying the hypotheses obeys

\[
\boxed{N<A(r)\log N+B(r).}                              \tag{1}
\]

For r=3 this yields the absolute represented ceiling

\[
\boxed{N<11000.}                                        \tag{2}
\]

This is a conditional restriction on this word language, not a
resolution of arbitrary cycles, divergence or universal eventual
descent. Its separate critical audit below found no defect. No complete Collatz
candidate is asserted.

## Proof

### Occurrence counts and the sourced cycle estimates

Each OOEO has three odd and one even input. Thus the represented counts
are exactly

\[
K=\sum_i(3J_i+H_i),\qquad L=\sum_i(J_i+a_i),\qquad N=K+L.
\]

The congruence and nonnegativity of a_i give a_i>=2, so K>=9r,
L>=4r, N>=13r and 1<K<N. Every positive odd integer 20 modulo 27
is at least 47. In particular the closed orbit is nontrivial: it
contains n_0 outside the invariant shortcut cycle {1,2}.

Use L035's single-word calculation, equations (4)–(8), at each actual
word separately. Its hypotheses there require only a positive actual
word: the affine OOEO identity retains its positive offset, all three
odd inputs of each block are included, and the terminal O^H subrun
is included even though it continues the last block's odd run. The
final E^a contributes no odd input. For a word starting at n_i that
calculation gives its input reciprocal mass less than
(69-36(16/27)^(J_i))/(11n_i)<69/(11n_i).

The intervals [D_0+...+D_(i-1), D_0+...+D_i) are disjoint and cover
[0,N). Thus each junction is counted at its outgoing word occurrence,
and the last endpoint at N is excluded. Coincident state values do
not merge input times. Summing the single-word inequalities gives

\[
S:=\sum_{\substack{0\le t<N\\T^t(n_0)\text{ odd}}}
       \frac1{T^t(n_0)}
 <\frac{69}{11}\sum_i\frac1{n_i}.                       \tag{3}
\]

Import Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
JIS 26 (2023), Article 23.3.5,
[Theorem 16 and proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf):
for a positive nontrivial shortcut cycle,
0<(K+L)/K-log3/log2<S/(3K log2).
The source's maximal-odd-run partition counts the same odd inputs
as (3); no designated junction is substituted for a global minimum.

The occurrence scaling in L035 applies independently of the number
of words. Explicitly, if p is the least positive return time, division
of N by p and periodicity show N=qp for an integer q>=1. The
primitive states are distinct by the least-return argument in L035,
and K=qK_0, L=qL_0, S=qS_0. Applying the source first on the
primitive period and then multiplying gives the represented estimate
0<Lambda<S/3, where Lambda=Nlog2-Klog3. Hence (3) gives

\[
0<\Lambda<\frac{23}{11}\sum_i\frac1{n_i}
           \le\frac{23r}{517}.                        \tag{4}
\]

Import John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005),
51–70,
[Lemma 12, printed p. 61; period conventions, section 1.2, printed p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):

\[
\Lambda>\exp[-13.3(0.46057+\log K)]
         =e^{-c}K^{-133/10},\qquad c=6.125581.          \tag{5}
\]

As checked in L036, this uses the same shortcut convention and
permits nonminimal periods. Even a primitive-period application
suffices: q Lambda_0>q e^(-c)K_0^(-133/10)
>=e^(-c)(qK_0)^(-133/10), since q>=1. The closed orbit has both
odd and even inputs; its E-to-O transitions are precisely cyclic
local minima, so it is an m-cycle for its actual full minimum count.
Neither imported theorem requires replacing that count by r.

The inspected Lemma 12 proof uses Rhin's Proposition and Lemma 8,
including published computational height inputs. These remain imports,
not locally certified computations or a reproof of transcendence
estimates. Hercher's June 2026 corrigendum does not amend Theorem 16,
as recorded in the ready source assessment. No amended Theorem 21
claim is used.

### A seed at the smallest designated junction

Cyclically relabel the word occurrences so that b=n_0=min_i n_i.
This changes neither r,N nor the actual words around the closed
orbit; ties may be resolved by any one occurrence. It does not
identify b with the global orbit minimum.

Combining (4) before its last inequality with (5) yields

\[
b<\frac{23r}{11}e^c K^{133/10}.
\]

Put s_i=n_i+23/11 and h_i=log s_i, so every h_i>0. Since b>=47,
the elementary log(1+t)<t for t>0 gives

\[
h_0<\frac{133}{10}\log K+c+\log r+\log(23/11)
                   +\frac1{20}.
\]

Here 23/(11b)<=23/517<1/20. Also c<25/4 and
e>1+1+1/2+1/6=8/3>23/11, so log(23/11)<1.
As 25/4+1+1/20=73/10<8 and K<N,

\[
0<h_0<\frac{133}{10}\log N+8+\log r.                 \tag{6}
\]

This supplies the r-dependent seed; the two-word seed is not imported
unchanged.

### Each occurrence's own prefix and the transfer to the next

At occurrence i abbreviate J=J_i,H=H_i,a=a_i, set P_i=4J_i+H_i,
and let y=T^(4J)(n_i), z=T^(4J+H)(n_i). L031's finite actual-word
identities and necessity proof apply separately to this word:

\[
y+1=(27/16)^J s_i-12/11,\qquad
2^H(2^a n_{i+1}+1)=3^H(y+1).
\]

Because a>=2 and the endpoint is odd, v_2(y+1)=H. Writing
y+1=2^H u with u positive odd, H>=3 makes
11y+23=4(11*2^(H-2)u+3) have valuation exactly 2. The actual
affine identity 16^J(11y+23)=27^J(11n_i+23) then gives
v_2(11n_i+23)=4J+2. This is the wordwise part of L031;
no two-word closure converse or E^2-only identity is invoked.

Thus 11n_i+23>=2^(4J+2) and 2^H<=y+1<(27/16)^J s_i.
Taking logarithms and combining as in L038's own-word estimate gives

\[
4J\log2\le h_i+\log(11/4),\qquad
P_i\log2<J\log27+h_i,
\]
\[
P_i<\left(\frac{\log27}{4(\log2)^2}+\frac1{\log2}\right)h_i
        +\frac{\log27}{4(\log2)^2}\log(11/4)
     <\frac{15}{4}h_i+3.                             \tag{7}
\]

For completeness of the constants, L036 proves log2>2/3 by the
positive derivative of log t-2(t-1)/(t+1) for t>1. L037 proves
log3<4/3 from e^(4/3)>293/81>3. Therefore log27<4,
1/log2<3/2, log27/(4(log2)^2)<9/4, and
0<log(11/4)<4/3. Together with h_i>0 these imply the last
strict inequality in (7). Only these elementary estimates, not
L037's selected two-word conclusion, are reused.

Now put G_i=(27/16)^J(3/2)^H. The exact identities retain both
additive shifts:

\[
z=G_i s_i-\frac{12}{11}(3/2)^H-1,\qquad n_{i+1}=z/2^a.
\]

Hence, just as in L038's finite transfer calculation,

\[
s_{i+1}<G_i s_i/4+23/11<G_i s_i.                     \tag{8}
\]

Indeed a>=2 and G_i s_i>=s_i>=540/11, so
(3/4)G_i s_i>=405/11>23/11. No tail upper bound or assumed
ratio of junction heights is used. Since 27/16<(3/2)^4 and
log(3/2)<1/2, one has log G_i<P_i/2. Taking logs in (8),
then using (7), gives the same recurrence at every occurrence:

\[
h_{i+1}<h_i+P_i/2<\frac{23}{8}h_i+\frac32,
\qquad
h_{i+1}+\frac45<\frac{23}{8}\left(h_i+\frac45\right). \tag{9}
\]

Starting with the selected occurrence 0, induction for 0<=j<r
gives h_j+4/5<=(23/8)^j(h_0+4/5), with equality allowed only
at the initial induction step. This traverses every indexed word
once in cyclic order, even when some n_j coincide. By (7),

\[
P_j<\frac{15}{4}(h_j+4/5)
   \le\frac{15}{4}\left(\frac{23}{8}\right)^j(h_0+4/5).
\]

Summing and using (6) proves

\[
K=\sum_j(P_j-J_j)<\sum_j P_j
 <\frac{15}{4}Q_r
       \left(\frac{133}{10}\log N+\frac{44}{5}+\log r\right).
                                                               \tag{10}
\]

### Total length and the three-word test

The exact inequality 3^5=243<256=2^8 implies log3/log2<8/5.
Use log2>2/3 and (4) in the count identity to obtain

\[
N=K\frac{\log3}{\log2}+\frac{\Lambda}{\log2}
 <\frac85 K+\frac{69r}{1034}.                         \tag{11}
\]

Substituting (10) in (11) proves (1) with precisely the displayed
A(r),B(r). All independent tails remain in the represented N
throughout; the cycle linear form controls their total contribution.
The functions depend only on r and are finite and positive. In
particular, for each fixed r, (1) is a finite upper-length restriction
because t-A(r)log t-B(r) tends to infinity with t.

For r=3,

\[
Q_3=1+23/8+529/64=777/64,\qquad
A(3)=310023/320<969.
\]

The already justified log3<4/3 gives

\[
B(3)<\frac{304}{5}\frac{777}{64}+\frac{207}{1034}
     =\frac{236208}{320}+\frac{207}{1034}<739.
\]

The last comparison is exact: 236208/320<1477/2 since
236208<236320, and 207/1034<1/2. Since log N>0,

\[
N<969\log N+739.                                    \tag{12}
\]

The positive exponential series gives e>8/3; the full integer
comparison 8^10=1073741824>649539000=11000*3^10 gives
log11000<10. On t>=11000, the function F(t)=t-969log t-739
has derivative 1-969/t>0, and
F(11000)>11000-9690-739=571>0. If N>=11000, monotonicity
would contradict (12). This proves (2), without a numerical screen
or an approximate logarithm.

### Relevance, qualifications and bounded decision

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-multi-postspell-represented-length-bound.md`.
This is REPRODUCTION: the difference supplied here is the r-dependent
seed, cyclic assembly and exact constants for inspected wordwise inputs.
No general cycle theorem, finite parity-coding theorem or transcendence
bound is reproved; no priority or progress beyond the checked source
mathematics is claimed. The working record is
`drafts/2026-10-08-multi-postspell-length-calculation.md`.

The first usefulness test succeeds: 11000<225640000. The latter is
the published primitive odd-count lower threshold in Simons–de Weger,
[Corollary 2 and proof, printed p. 53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
It counts odd inputs K_0, not total represented steps N. A later
restricted exclusion can compare K_0<=K<N with that threshold, after
critical review of the present ceiling. The corollary imports the
computational height x_min>301*2^50, attributed to distributed [Ro]
computations with a Roosendaal personal-communication footnote, and
continued-fraction denominators 225644606 and 397573379. None of these
is independently certified here, and the corollary is not needed to
prove (1) or (2).

Attempt 019's guard-only failure and history 069's full-minimum-count
mismatch remain intact. The proof uses independent cycle estimates,
not a guard contradiction or an unjustified r-for-m substitution.
The constants grow with r; no bound uniform in all r is asserted.
Repeated representations are retained with their actual word count,
so an unrestricted repeat need not have the same r. Entry into this
language, other cycles, divergence and universal descent remain open.
The proof uses L031's explicit finite-word algebra, not an unchecked
external Lean build; recorded Sodelin version/build qualifications are
not upgraded. The separate audit of this assembly is recorded below.

### Separate critical audit — 2026-10-08

The pre-invocation SPECIALIZE assessment for this audit is
`drafts/literature/2026-10-08-multi-postspell-length-audit.md`.
The complete proof above and the essential finite-word passages of
L031, L035, L036, L037 and L038 were checked independently of the
two-word conclusions. Verdict: **no defect found within the stated
hypotheses and imported qualifications**. No stronger conclusion or
repair resulted. This is a REPRODUCTION audit, not a new discovery.

For the occurrence check, the three odd inputs of each B=OOEO block
at start t contribute 1/t+2/(3t+1)+8/(9t+5), at most 23/(9t).
The jth block start is (27/16)^j(n_i+23/11)-23/11, at least
(27/16)^j n_i. L035's geometric sum therefore gives the block
mass at most 69(1-(16/27)^J)/(11n_i). Its finite terminal-subrun
estimate contributes less than 3(16/27)^J/n_i. Their sum is the
stated (69-36(16/27)^J)/(11n_i). Terminal inputs start at 4J,
after the last block input at 4J-1; each outgoing junction is counted
once. This check needs no maximality of the terminal subrun, and
coincident junction values do not remove time occurrences.

The nontrivial primitive cycle exists because the actual positive
orbit closes at n_0 outside {1,2}. If N=qp+s with 0<=s<p, then
T^N(n_0)=T^s(n_0), so minimality of p forces s=0. A repeated
state inside [0,p) would give an earlier return by applying the
remaining iterates to that repeated state. Thus primitive state sums
match primitive occurrence sums. Scaling Hercher's precisely cited
Theorem 16 gives Lambda<S/3 at represented counts. Scaling the
published Lemma 12 gives
q Lambda_0>e^(-c)q^(143/10)K^(-133/10)>=e^(-c)K^(-133/10).
Here c=(133/10)(46057/100000)=6125581/1000000. This checks the
alternative primitive application as well as the source's explicit
nonminimal-period convention. The full cyclic minimum count is used
only for applicability, with no substitution of r for that count.

For b=min_i n_i, sum_i 1/n_i<=r/b. Combining the strict lower
and upper estimates gives b<(23r/11)e^c K^(133/10) in the correct
direction. Since b>=47, the logarithmic shift costs less than
23/517<1/20; c<25/4 and log(23/11)<1 give a constant less than
73/10<8. This verifies the r-dependent seed (6) without identifying
b with the global minimum. The cyclic relabeling preserves every
indexed word and chooses an arbitrary minimizing occurrence in a tie.

At each own word, the identity
2^H(2^a n_(i+1)+1)=3^H(y+1) gives v_2(y+1)=H. The positive
odd u=(y+1)/2^H and H>=3 give v_2(11y+23)=2; the affine
B^J identity gives v_2(11n_i+23)=4J+2. Thus the two logarithmic
inequalities before (7) hold at every index, independently of the
size ordering of junctions. Substitution has positive coefficient
log27, and h_i>0 permits the coefficient relaxations using
log2>2/3, log27<4 and 0<log(11/4)<4/3. These give precisely
P_i<(15/4)h_i+3. The cited elementary estimates were checked in
L036/L037; they do not require their two-word cycle hypotheses.

The exact endpoint z=G_i s_i-(12/11)(3/2)^H-1 is positive.
Dividing its strict upper bound by 2^a, using a>=2, and adding
23/11 gives s_(i+1)<G_i s_i/4+23/11<G_i s_i because
G_i s_i>=540/11. Both shifts and the exact tail remain accounted
for. Since log G_i<P_i/2, the affine recurrence has coefficient
1+(15/4)/2=23/8 and constant 3/2. Its shift is exactly
(3/2)/(23/8-1)=4/5. Induction from j=0 through r-1 covers all
r outgoing word occurrences; it requires neither unequal values nor
an assumption on which later junction is larger. Also
(15/4)(h_j+4/5)=(15/4)h_j+3. Summing this induction proves (10),
with K=sum(P_j-J_j)<sum P_j and the seed constant 8+4/5=44/5.

The exact identity N=K log3/log2+Lambda/log2 retains every tail.
The comparisons 3^5<2^8, log2>2/3 and Lambda<23r/517 give
the final additive term 69r/1034. Multiplying (10) by 8/5 gives
the common factor 6, hence coefficients 399/5 and 264/5 and
the term 6log r, exactly as in (1). No omitted tail is bounded
by a prefix length.

For r=3, Q_3=(64+184+529)/64=777/64 and
399*777=310023<310080=969*320. Using log3<4/3, the other
coefficient is less than 236208/320+207/1034<1477/2+1/2=739;
both comparisons are strict since 236208<236320 and 414<1034.
The integer powers 8^10=1073741824 and 11000*3^10=649539000,
together with e>8/3, prove log11000<10. Finally
F'(t)=1-969/t>0 for every real t>=11000 and F(11000)>571.
Thus N>=11000 contradicts (12). This is an all-real threshold
argument, not a tested finite range or a rounded logarithmic estimate.

The numerical comparison 11000<225640000 is valid, but importing
Corollary 2 for a later exclusion still retains K_0<=K<N and its
published computational and continued-fraction qualifications. No
three-word exclusion is newly proved in this audit. Theorem 16 and
Lemma 12 retain the precise citations above; Rhin's original proof,
source computation certificates, the external Lean build and Mathlib
matching coverage were not independently checked. L039/L040 were
comparators only, so no new DAG input is needed. Attempt 019 and
history 069 remain applicable to their failed mechanisms. The audit
supersedes the overview's pending-audit wording without changing the
argument, its r dependence or its unresolved universal-descent gap.

## Mathlib

Full matching theorem: **not checked**. Supporting finite-word affine
identities, dyadic valuations, geometric sums, real logarithms and
exponential-series inequalities: **not checked** for exact declarations.
No matching theorem or absence from Mathlib is asserted, and no
formal verification is claimed.
