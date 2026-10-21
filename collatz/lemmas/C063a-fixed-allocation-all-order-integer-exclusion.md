# C063a — Fixed allocation all-order integer exclusion

## Hypotheses

Use exactly the 25 indexed triples (J_j,H_j,a_j) of L055's table:
a_j=2 for 0<=j<24 and a_24=166504412. Their totals are
K=397573379 and N=630138897. Let sigma be any permutation of
{0,...,24}, interpreted cyclically. At chronological position k the
outgoing triple is (J_sigma(k),H_sigma(k),a_sigma(k)); it stays attached
to its input junction s_k. Require real numbers s_k>=540/11,
s_25=s_0, all exact endpoints

\[
s_{k+1}=2^{-a_{\sigma(k)}}\left\{
(27/16)^{J_{\sigma(k)}}(3/2)^{H_{\sigma(k)}}s_k
-\frac{12}{11}(3/2)^{H_{\sigma(k)}}-1\right\}+\frac{23}{11},
\]

and every own-input non-strict J guard

\[
4J_{\sigma(k)}\log2\le\log s_k+\log(11/4).
\]

These are precisely L051 (4) and the J part of (3), on the fixed
allocation. All logarithms are natural. Define n_k=s_k-23/11.
No H guard, seed, primitive-count condition or actual parity is assumed
for this real subsystem.

For the actual-cycle consequence below, separately impose L041's
language hypotheses: actual shortcut words
W_j=(OOEO)^{J_j}O^{H_j}E^{a_j}, positive odd junctions 20 modulo 27,
exact final even tails, and closure. Here O(t)=(3t+1)/2 on odd inputs
and E(t)=t/2 on even inputs. Repeated periods and coincident junctions
are allowed. This consequence concerns exactly this allocation.

## Conclusion

There is no solution of this subsystem for which all n_k are integers,
for any sigma. Consequently no actual positive integer closed
concatenation satisfying the stated L041 language hypotheses realizes
any intact order of these 25 triples, including any cyclic rotation.

L055's positive rational witness remains valid. This excludes one fixed
allocation, not every allocation with these totals or every 25-word
cycle. Other allocations, unrestricted cycles, divergence, entry and
universal eventual descent remain unresolved. This is a local
REPRODUCTION assembly under the prior SPECIALIZE assessment
`drafts/literature/2026-10-12-fixed-allocation-integer-exclusion-assembly.md`,
with no claim of originality beyond the checked sources. The separate
critical audit below found no defect; it is not a Collatz candidate argument.

## Proof

### Cyclic normalization preserves the necessary subsystem

Suppose a solution exists. Let t be the unique position with sigma(t)=24.
For 0<=k<25 set

\[
j(k)=(t+1+k)\bmod25,\qquad
\widetilde s_k=s_{j(k)},\qquad \pi(k)=\sigma(j(k)),
\]

and set tilde s_25=tilde s_0. Then pi(24)=24, while pi restricted
to positions 0,...,23 is a permutation of rows 0,...,23. Every
original cyclic edge becomes the edge from tilde s_k to tilde s_(k+1)
with outgoing triple pi(k). In particular the edge crossing the old
index 24 uses s_25=s_0; none is omitted. Its own-input J guard rotates
with that same triple. Thus the lower domain, all endpoints and all
non-strict guards are preserved. If all n_k were integers, so would be
all tilde n_k=tilde s_k-23/11. No sorting or independent reassignment
of inputs occurs. The large tail is still included, now at the last edge.

### Audited rigidity and the unshifted obstruction

The normalized tuple satisfies exactly L063's hypotheses. Its audited
order-rigidity conclusion forces pi to be the identity. Its endpoint
uniqueness then identifies the normalized tuple with L055's literal
cyclic tuple. In particular tilde n_0 is L055's unshifted root, rather
than its shifted s_0 or its auxiliary B.

L056's audited coordinate match identifies this same root as Phi/Delta,
where Phi is the integer chronological affine numerator and
Delta=2^N-3^K>0. Its complete modulo-five calculation gives
Delta=0 modulo 5 and Phi=4 modulo 5. Therefore an integer tilde n_0
would imply the impossible integer identity Phi=tilde n_0 Delta.
This contradicts integrality of the normalized tuple and proves the
subsystem assertion.

The underlying known affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its nonempty chronological-word specialization, nonzero denominator
and unshifted-coordinate identification are already verified in L056
and L063. This assembly imports those audited results; it needs no
general reproof, fresh modular calculation or integer-parity converse.

### Actual words supply the necessary subsystem

Suppose an actual closed concatenation has the stipulated L041 language
hypotheses and uses this allocation in order sigma. Every positive odd
residue-20 junction n_k is at least 47, so s_k=n_k+23/11>=540/11.
Each table row has J>=2, H>=3 and a>=2 congruent to 2 modulo 18.
L041's section “Each occurrence's own prefix and the transfer to the
next” applies separately to each actual outgoing word and supplies the
exact shifted endpoint above and
4J_sigma(k) log2<=log s_k+log(11/4). These are necessary wordwise
identities and guards, retaining that word's exact tail and odd endpoint.
Closure supplies s_25=s_0 and every unshifted n_k is an integer.
The subsystem exclusion just proved is therefore a contradiction.

No full-cycle theorem is applied to real junctions, and no primitive
count or computational cycle cutoff is required for this implication.
The published computational, continued-fraction and Rhin/Crandall
qualifications in the broader L041/L051 background remain unchanged;
this assembly uses only their elementary wordwise subsystem. The seed,
H guards and count-ray estimates are not needed here. Attempts 027–031
remain valid: no claim of modular nonvanishing for every order is made.
Nonliteral orders fail necessary guards by L063; only the literal order
is tested for nonintegrality by L056. Neither input nor this conjunction
excludes other allocations or provides universal eventual descent.

### Separate critical audit — 2026-10-12

The approved RESEARCH/REPRODUCTION audit under
`drafts/literature/2026-10-12-fixed-allocation-integer-exclusion-audit.md`
found no defect in this conjunction. It reused the separately audited
L063 and L056 results, rather than rerunning their numerical certificates.
The complete L055 allocation, its cyclic-root definition, L051 (3)–(4)
and L041's elementary wordwise proof were checked against the applications
here. The following verifies the conjunction independently of its earlier
assembly; it supplies no new allocation or general theorem.

For normalization, regard the original input indices as elements of
Z/25Z. The map j(k)=t+1+k modulo 25 is bijective, and
j(k+1)=j(k)+1 modulo 25. Thus for every k the original equation
with input index j(k) has output index j(k+1) and outgoing row
sigma(j(k))=pi(k). This proves preservation of all 25 equations,
not just the edges away from a cut. More explicitly, if j(k)<24
the old equation ends at s_(j(k)+1); if j(k)=24 it ends at
s_25=s_0. Both are the required rotated output. At the new closing
edge k=24, j(24)=t and j(25)=j(0)=t+1 modulo 25, so the
outgoing row is sigma(t)=24 and its output is tilde s_0. These cases
also cover t=24, when the normalization is the identity. No assumption
that the input values are distinct is used. Bijectivity transfers the
lower bound and integrality at every input, and each guard uses exactly
the same input value and J parameter as its original equation.

L063 requires precisely these rotated endpoints, s>=540/11 and the
non-strict J guards, with rows 0 through 23 permuted and row 24 last.
It requires neither that s_0 be a minimum nor the other L051 premises.
In particular, importing the numbered endpoint and J formulas does not
silently import L051's seed, primitive count or minimum convention.
The forced identity order follows from the audited strict guard failure
for every nonidentity permutation, so its use with a non-strict guard is
valid. Literal existence is already supplied by L055.

To check the identification after rigidity, the multiplier of the full
unshifted affine composition is P=3^K/2^N. The unchanged intact triples
give the same K,N under rotation and permutation, and L055's audited
positive Lambda gives 0<P<1. Hence the closing affine equation has at
most one real root. Once pi is the identity, both the normalized tuple
and L055's literal tuple solve these identical endpoints; uniqueness
identifies their input roots and then every subsequent junction. The
coordinate is n=s-23/11 throughout. L056 (1)–(3) matches that literal
unshifted map to (3^K n+Phi)/2^N and its root to Phi/(2^N-3^K).
Its already audited residues Phi=4 and Delta=0 modulo 5 apply to this
root. An integer at the normalized first junction would force
Phi=n Delta, contradicting those residues. No modular residue for a
different ordered numerator is asserted, and no rational-parity theorem
or integer-realization converse is needed.

For the actual-word implication, the smallest positive odd integer
20 modulo 27 is 47, and 47+23/11=540/11. Every row in the complete
table has J>=2,H>=3; its tail is either 2 or
166504412=2+18*9250245. All L041 language guards therefore match,
with r=25. At each actual outgoing word set y=T^(4J)(n) and
z=T^(4J+H)(n)=2^a n_next. The identities in L041 give
y+1=(27/16)^J s-12/11 and
2^H(z+1)=3^H(y+1). Since z is even and y+1 is a positive integer,
v_2(y+1)=H. Writing y+1=2^H u with u odd, H>=3 gives
11y+23=4(11*2^(H-2)u+3), whose valuation is exactly 2.
The same word's identity
16^J(11y+23)=27^J(11n+23) then gives
v_2(11n+23)=4J+2. Positivity implies
11s=11n+23>=2^(4J+2), hence precisely
4J log2<=log s+log(11/4). Also
z=(3/2)^H(y+1)-1, so substituting for y+1 and dividing by the
actual 2^a gives the required shifted endpoint, including both additive
terms and that occurrence's tail. Closure and integer junctions finish
the implication. This verifies the local applicability of the imported
wordwise argument; it is not a reproof of general affine coding.

These checks cover all direct uses recorded in the unchanged DAG row.
Repeated periods and coincident junctions introduce no extra premise.
No published computational cycle bound, Rhin estimate or continued-fraction
bound enters this particular conjunction, although their qualifications
remain on the broader background results. The argument and dependency
structure did not change, so PROOF.md and DAG.md were not edited; this
canonical verdict supersedes their pending-audit wording for C063a.
L055 and Attempts 027–031 remain valid. The audit verifies only this
fixed-allocation exclusion, with all universal gaps still open.

## Mathlib

Full matching coverage and external Lean builds were not checked;
unknown availability is not evidence of absence. The proof uses audited
local inputs and their precise published affine source. No new numerical
certificate is needed for this finite logical assembly, and no Lean
verification or new general coding theorem is claimed.
