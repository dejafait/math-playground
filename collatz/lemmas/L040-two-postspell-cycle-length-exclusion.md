# L040 — Exclusion of closed two-postspell representations by cycle length

## Hypotheses

Use the shortcut map T(t)=t/2 for even positive integers and
T(t)=(3t+1)/2 for odd positive integers. O and E denote actual
input parities. For i=1,2 let J_i>=2, H_i>=3 and a_i>=0 be
integers with a_i congruent to 2 modulo 18, and put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=D_1+D_2.
\]

The representation to be excluded would be actual at a positive odd
integer n>1, with positive odd junction x=T^{D_1}(n), both n and x
congruent to 20 modulo 27, exact independent final even tails, and
T^N(n)=n. No least-root, first-return, primitive-period,
distinct-junction or global-minimum assumption is imposed.
Repeated periods and x=n are admitted.

For the equivalent arithmetic conclusion define, as in L031,

\[
q_i=2^{D_i},\quad A_i=3^{3J_i+H_i},\quad
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i},
\]
\[
q=q_1q_2,\quad A=A_2A_1,\quad
C=A_2C_1+q_1C_2,\quad \Delta=q-A.
\]

These C_i and C are positive integers by L031's imported affine inputs.
The argument imports the published cycle lower bound and L039's
inherited source results with the qualifications specified below.

## Conclusion

There is no actual closed representation satisfying these hypotheses.
Equivalently, for every allowed parameter tuple,

\[
\boxed{\neg(\Delta>0\ \text{and}\ \Delta\mid C).}
\]

This excludes only the fixed two-postspell cycle language. It does not
exclude arbitrary positive nontrivial cycles or divergence, or establish
universal entry, eventual descent or the Collatz conjecture. The local
exclusion passed the separate critical audit recorded below, with the
published inputs still imported rather than independently certified.

## Proof

### Imported theorem and qualifications

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-two-postspell-cycle-length-comparison.md`.
The working record is
`drafts/2026-10-08-two-postspell-cycle-length-specialization.md`.
This is a REPRODUCTION theorem application; the needed general theorem
is imported, rather than reproved.

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[Corollary 2 and its complete proof, printed p. 53; map and period
conventions, sections 1.1–1.3, printed pp. 51–53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
give K>2.2564*10^8=225640000 for a positive nontrivial cycle.
K counts odd inputs of the shortcut map, not total shortcut steps,
local minima or steps of the unshortened map. The published period
convention permits nonminimal periods; we nevertheless apply the
theorem only to the primitive period below.

The cited proof uses Lemma 1, the published computational height input
x_min>301*2^50, and continued-fraction denominators q_18=225644606
and q_19=397573379. The height input is attributed there to distributed
computations [Ro] with a Roosendaal personal-communication footnote.
These height and continued-fraction inputs are imported as part of
the precise published corollary, not independently certified here.
Crandall's original proof was inaccessible in the preceding assessment;
it is not an additional inspected input. The published Corollary 2 and
its complete proof were inspected. No stronger modern bound is needed.

L039's inherited Hercher Theorem 16 and Simons–de Weger Lemma 12
inputs, including Rhin's estimate and published computations, retain
their existing citation and import qualifications. Hercher's 2026
corrigendum concerns Theorem 21, outside these load-bearing estimates,
as recorded in the saved assessment. No new certification of these
sources is claimed.

### Applicability and contradiction

Suppose such a closed representation exists. Its positive odd
residue-20 junction n is at least 47, so it lies outside the invariant
shortcut cycle {1,2}. Its positive closed orbit is therefore nontrivial.

L035 gives represented input counts

\[
K=3(J_1+J_2)+H_1+H_2,\qquad
L=J_1+J_2+a_1+a_2,\qquad N=K+L.
\]

In particular K>=18 and L>=8, so both kinds of input occur. Apply
L035's return-period argument: if p is the least positive return time
of n, then N=rp for an integer r>=1, and the parities repeat every p
steps. If K_0,L_0 are the primitive input counts, then
K=rK_0, L=rL_0 and p=K_0+L_0. The primitive states are distinct
by the least-return argument in that same proof. The primitive orbit
is positive and nontrivial and contains both odd and even inputs.
Its cyclic parity sequence therefore has an E-to-O transition.
At each such transition the odd state u has preceding state 2u>u
and succeeding state (3u+1)/2>u, so it is a strict local minimum.
Conversely an even state cannot be a local minimum since its next
state is smaller, and an odd state preceded by an odd input has a
smaller preceding state. Thus these transitions are precisely its
cyclic local minima, making it an m-cycle in the source convention
for some positive integer m. Corollary 2 imposes no fixed bound on m.
It applies and gives K_0>225640000.

L039 has exactly the assumed actual two-word hypotheses, including
independent exact tails and closure, and gives represented N<4500.
Since r>=1 and K_0>0, while N=K+L with L>0, we obtain

\[
225640000<K_0\le K<N<4500,
\]

an impossibility. This proves the language exclusion. No assumption
that the two designated junctions are global minima was needed:
the lower-height premise is part of the imported general corollary.
If x=n or the representation repeats a smaller period, the same
primitive scaling applies and the contradiction is unchanged.

Finally, L031 proves that Delta>0 and Delta|C imply an actual positive
closed representation with all the present guards, n=C/Delta>=47,
positive odd residue-20 junctions and exact tails. The exclusion just
proved contradicts that implication. Hence the displayed arithmetic
condition fails for every allowed tuple. This invokes the established
coding/closure equivalence; boundary guards are not treated as an
independent exclusion mechanism.

### Relevance and limits

The continuation test succeeds: the primitive odd-count lower threshold
225640000 strictly exceeds the represented shortcut ceiling 4500, with
all conversions justified. No enumeration, tail cap, minimum-count
substitution or new general cycle bound is used. Attempt 019's guard-only
failure and history 069's full-minimum count mismatch remain valid.

This is new local assembly of checked source inputs, without a claim
of originality or progress beyond the source mathematics assessed.
It removes the integer-closure gap only for this fixed two-word
language. More general cycle languages, infinite growing chains,
divergence and universal eventual descent remain unresolved. It is
not a complete Collatz candidate. The separate review below checks the
inherited ceiling, source hypotheses and arithmetic-equivalence use.

### Separate critical audit

The 2026-10-08 audit used the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-08-two-postspell-cycle-exclusion-audit.md`.
The working record is
`drafts/2026-10-08-two-postspell-cycle-exclusion-audit.md`.
Complete L040, L031 and L035–L039 were inspected, together with the
load-bearing affine/composition passages of L020/L021 and L034's
return-time proof. The statement and direct mathematical inputs do not
change. The verdict is **no defect found**, not a stronger theorem or
independent recertification of the source computations.

**Positive integer closure really supplies the actual word.** For each
index, 27^J-16^J is divisible by 11 and positive; 3^H-2^H is positive.
Thus each C_i, and then C=A_2 C_1+q_1 C_2, is a positive integer.
The formal single-block identity is 16B(t)=27t+23, and the imported
iteration and terminal-run formulas used in L020/L021 give the stated
affine constants without a residue hypothesis on t. The residue
hypothesis in those lemmas concerns endpoint membership, not that
polynomial identity. This checks the precise specialization needed here;
it does not import their least-root conclusions.

Bernstein–Lagarias's finite coding, cited in L031, gives one class r
modulo q=2^N for the complete N input bits. By CRT it has a positive
representative b congruent to 20 modulo 27. At that actual representative
L021's formula gives q dividing Ab+C. Because A is odd, there is exactly
one solution class to At+C=0 modulo q. It is therefore r. Every positive
integer satisfying that congruence has the entire actual word, not just
an integral formal endpoint. The CRT representative establishes this
class identity; it is not assumed to be the proposed closed root.

If Delta>0 and Delta divides C, then n=C/Delta is a positive integer
and An+C=qn. It belongs to that class, its actual endpoint is n, and
all intermediate states are positive. The first letter of W_1 and of
W_2 is O, so n and x are odd. The last endpoint is odd by closure,
not by any extra endpoint bit in finite coding. Hence the actual tails
z_1=2^{a_1}x and z_2=2^{a_2}n both have exactly the specified valuations.

For either word, L031's identities at its actual B^J endpoint y and
final endpoint m read
16^J(11y+23)=27^J(11t+23) and
2^H(2^a m+1)=3^H(y+1). Modulo 27 the first yields y=20, since
16 and 11 are invertible there. The second gives 2^a m=-1 because
H>=3. Nonnegative a congruent to 2 modulo 18 has a>=2 and
2^a=4 modulo 27, so m=20 modulo 27. Applying this to both incoming
words establishes x and n in that class without presupposing it of
the root. Positive odd membership forces n,x>=47. Thus L031's
sufficient direction supplies every hypothesis used by L040, including
n>1, independent exact tails, and nontriviality. Its necessary direction
is just Delta n=C with positive C. No infinite 2-adic realization or
unproved Periodicity Conjecture enters this finite argument.

**The inherited ceiling uses the same represented counts.** The input
counts are exactly K=3(J_1+J_2)+H_1+H_2 and
L=J_1+J_2+a_1+a_2, so K>=18,L>=8,N=K+L. L035 sums three
odd input occurrences in each OOEO, followed by a disjoint terminal
O^H subrun. The respective bounds are
(69/(11b))(1-(16/27)^J) and 3(16/27)^J/b, with the latter strict.
No junction is counted twice and no odd input after an isolated E is
omitted. This gives its uniform mass estimate. Under closure its
primitive-to-represented scaling gives
0<Lambda=N log2-K log3<(23/11)(1/n+1/x).

The lower input is the precisely cited Simons–de Weger Lemma 12:
Lambda>e^{-c}K^{-13.3}, c=6.125581. Even if applied first to a
primitive period with repeat factor d, it yields
Lambda=d Lambda_0>d e^{-c}K_0^{-13.3}
>=e^{-c}(dK_0)^{-13.3}. Thus repetition preserves the lower bound
as well as L035's upper bound. At b=min(n,x) these give
b<(46/11)e^c K^{13.3}. L037 retains that same word index, obtaining
log(b+23/11)<(133/10)log K+8 and 4J+H<50log N+33.

The local height argument is valid for each word's own parameters:
2^H(2^a m+1)=3^H(y+1) with m odd and a>=2 gives
v_2(y+1)=H. For H>=3, writing y+1=2^H u with u odd gives
11y+23=4(11*2^{H-2}u+3), of valuation exactly 2. The affine identity
then gives v_2(11t+23)=4J+2. With s=t+23/11,
4J log2<=log s+log(11/4) and
H log2<J log(27/16)+log s. Combining them and the exact bounds
log2>2/3, log27<4, log(11/4)<4/3 gives
4J+H<(15/4)log s+3. All logarithms multiplying coefficient bounds
are positive since t>=47. The estimates in L037 use the exact series
sums 563/128>46/11 and 293/81>3, and
c+3/2+1/20<25/4+3/2+1/20=39/5<8; no rounded constants are needed.

L038 transfers from the selected b to the other junction m through
its actual word. With G=(27/16)^J(3/2)^H it uses
z=G(b+23/11)-(12/11)(3/2)^H-1 and m=z/2^a. Since a>=2,
b+23/11>=540/11 and G>1, it follows that
m+23/11<G(b+23/11). Also log G<(4J+H)/2. Thus the other
shifted logarithm is less than (383/10)log N+49/2. Applying the
other word's own height inequality gives
4J_m+H_m<(1149/8)log N+759/8<144log N+95.
The selected word has the smaller bound above. Both index orders and
the tie x=n are valid: an index denotes a word occurrence even if its
starting value repeats. This verifies both prefix bounds without a
tail cap, global-minimum assumption or assumed ratio of junction sizes.

For P_i=4J_i+H_i, these bounds imply
K=P_1+P_2-(J_1+J_2)<288log N+190. Since n,x>=47,
Lambda<46/517. The exact inequalities 3^5<2^8 and log2>2/3 give
N<(8/5)K+69/517<(2304/5)log N+305. L039 solves this without
an approximate threshold: e>8/3 and
8^9=134217728>88573500=4500*3^9 imply log4500<9.
For F(t)=t-(2304/5)log t-305 and t>=4500,
F'(t)=1-2304/(5t)>0 and F(4500)>239/5>0. The necessary
F(N)<0 therefore forces N<4500. Both independent tails remain in
that same N throughout. This is a bound on representations satisfying
the two-word language, not on arbitrary repetitions of arbitrary cycles.

**Primitive source applicability and the final contradiction.** The
positive closed orbit containing n>=47 cannot enter the invariant
shortcut cycle {1,2}. Let p be its least positive return time. Dividing
N=dp+s with 0<=s<p and using determinism gives T^s(n)=n, so s=0.
The same determinism makes all input bits p-periodic, and consequently
K=dK_0,L=dL_0. If two states at times 0<=i<j<p were equal,
applying T^{p-j} would return to n at time p-j+i strictly between
0 and p. Thus primitive states are distinct. Because K,L>0,
the primitive period has both parities and a positive number of cyclic
E-to-O transitions. An E-to-O odd state u has predecessor 2u>u
and successor (3u+1)/2>u. An even state has a smaller successor;
an O preceded by O has a smaller predecessor. These transitions are
exactly the source's local minima, so the primitive orbit is an m-cycle
for some m>=1. No fixed-m hypothesis is needed in Corollary 2.

The published Corollary 2 and complete proof cited above therefore give
K_0>225640000. Since d>=1 and L>0, K_0<=K<N<4500 is impossible.
The numerical thresholds are in the required direction by a wide exact
margin; odd counts have never been equated with total shortcut counts.
The earlier verified sufficient direction of L031 then excludes
Delta>0 and Delta dividing C for every allowed tuple. Attempt 019's
guard-only failure remains correct: the independent length comparison,
not an extra boundary guard, supplies this contradiction.

**Source qualifications and verdict.** The published 2005 Corollary 2,
not the revised 2010 manuscript or an inaccessible original, is imported
with xmin>301*2^50, its [Ro]/personal-communication qualification and
continued-fraction values q_18=225644606,q_19=397573379. Lemma 12
retains its Rhin and source-computation imports. Hercher's Theorem 16
matches the odd-occurrence sum and is unaffected by the inspected 2026
correction to Theorem 21. L034's return argument is used; its Theorem 23
cutoff is not needed for this exclusion. The finite coding citation is
Bernstein–Lagarias, author manuscript 15 February 1996, section 1,
pp. 1–3, equations (1.3)–(1.6), including its finite permutation
statement. The Sodelin affine input remains live-main coverage inspected
2026-10-04, without an immutable revision or checked Lean build.
These precise existing source records were reused, not refreshed or
independently recertified. No missing essential hypothesis was found.

The audit retains L040 in its full stated scope, including repetitions
and x=n. It establishes no stronger bound, repair, originality claim or
progress beyond the assessed source mathematics. The result excludes
only the prescribed two-word periodic language and its arithmetic closure
condition; universal entry, other cycles, divergence and eventual descent
remain open. There is no complete Collatz candidate.

## Mathlib

The full matching two-postspell exclusion, the general computational
cycle-length lower bound, the inherited effective inputs, and supporting
finite-period/count results: **not checked**. No matching declaration
or absence from Mathlib is asserted. The precise published citation and
the applicability/contradiction proof above are the informal evidence.
