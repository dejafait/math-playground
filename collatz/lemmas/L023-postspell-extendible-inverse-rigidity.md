# L023 — Uniqueness of an extendible postspell predecessor

## Hypotheses

Use the shortcut map T(x)=x/2 for even x and T(x)=(3x+1)/2
for odd x. O and E always require the indicated actual input parity.
Write

\[
B=(OOEO),\qquad W(J,H)=B^J O^H E^2,
\quad J\ge2,\ H\ge3.
\]

Fix a positive odd integer m congruent to 20 modulo 27. An allowed
predecessor n is a positive odd integer congruent to 20 modulo 27
with an actual W(J,H) from n to m. Call it extendible if there is
a positive odd p congruent to 20 modulo 27 and an actual W(K,L)
from p to n, with K>=2,L>=3. Thus both E^2 tails end at odd states
and are exact; every intermediate input parity is required.
There are no least-nonconvergent-root hypotheses or filters.

## Conclusion

At most one distinct allowed predecessor n of m is extendible.
Indeed at most one final label (J,H) can have an extendible predecessor.
This holds for the full unbounded parameter alphabet.

This is an inverse statement at a fixed endpoint. No uniform bound
on forward chain length at a fixed starting integer, universal entry
into this alphabet, eventual compensation, or Collatz convergence
is concluded.

## Proof

### Inputs and applicability

Reuse the EXPLORE assessment
`drafts/literature/2026-10-05-postspell-extendible-inverse-rigidity.md`.
No inspected primary theorem there settles this language-specific
uniqueness target. The argument below is classified POTENTIALLY_NEW
in that limited search sense, without a priority claim.

L020 supplies the actual B and odd-run affine identities and the
residue-20 membership check, imported from Sodelin, *Guarded root
descent after independently unbounded return spells and odd runs*,
node `AC-POSTSPELL-GUARDED-ROOT-DESCENT-001`,
[Postspell_Guarded_Root_Descent.md, sections 2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md).
The prior assessment inspected live main on 2026-10-04; no immutable
revision or verified Lean build is asserted. Only those identities
and finite coding are imported, not a uniqueness theorem.
L021 supplies composition for the supporting two-word finite screen.

For an actual B block at a positive residue-20 state x, let b(x)
denote its endpoint. The identities specialize to

\[
16b(x)=27x+23,\qquad
4b(x)+1=\frac{27(x+1)}4.                 \tag{1}
\]

The denominator is legitimate because these are identities of actual
integer iterates, not purported sufficient conditions for a word.
The first identity and invertibility of 16 modulo 27 give
b(x)=20 modulo 27. Hence every B endpoint in an actual B^J chain
starting in residue 20 remains in that class.

For any actual W(J,H) from n to m, put y=T^(4J)(n).
Then y is positive and residue 20. The actual two final even
steps give z=T^(4J+H)(n)=4m. L020's odd-run identity gives

\[
2^H(4m+1)=3^H(y+1).                    \tag{2}
\]

Because y+1=21 modulo 27, its exact 3-adic valuation is 1.
All quantities whose valuation is taken are positive. Thus

\[
v_3(4m+1)=H+1.                         \tag{3}
\]

In particular H is fixed by m, and (2) then fixes y uniquely.
This is a necessary identity for actual words; no integer affine
inverse is admitted merely on the basis of integrality.

### The obstruction to an extendible B endpoint

We claim that if an actual B at a positive residue-20 state x
ends at u, then u cannot be the endpoint of any actual W(K,L)
starting at a positive residue-20 state p.

Since v_3(x+1)=1, (1) gives v_3(4u+1)=4. If such a preceding
word existed, apply (3) to its endpoint u to obtain L=3.
Let v=T^(4K)(p), which is residue 20 by (1). Equation (2) for
that word then gives, using (1) again,

\[
v+1=\frac{8(4u+1)}{27}=2(x+1),
\qquad v=2x+1.                          \tag{4}
\]

But x=20 modulo 27 implies v=14 modulo 27, contradicting
v=20 modulo 27. This proves the claim. It concerns actual words
with the stated residue guard; it makes no assertion about all
unrestricted incoming Collatz paths.

### Comparing two putative extendible predecessors

Suppose n_1,n_2 are extendible predecessors of m with labels
(J_1,H_1),(J_2,H_2). Equation (3) gives H_1=H_2, and (2) gives
the same pre-odd-run state y for both histories. On actual B
blocks the affine map b(x)=(27x+23)/16 is injective, as are its
iterates. If J_1=J_2, the identity b^(J_1)(n_1)=b^(J_1)(n_2)
therefore gives n_1=n_2.

Otherwise exchange indices so that J_1<J_2. In the longer actual
B chain set d=J_2-J_1>=1. Its actual state after d B blocks has
J_1 blocks remaining to y. Injectivity identifies that state
with n_1. Thus n_1=b(x), where x is the state after d-1 B
blocks of the longer history. This x is positive and residue 20.
The preceding claim says n_1 cannot be the endpoint of an allowed
preceding W word, contradicting its extendibility.

Consequently different J labels cannot both be extendible. For the
unique possible J,H, injectivity fixes n. All parity guards were
retained as hypotheses of the actual histories; the comparison never
manufactures a history from an unguarded affine inverse. This proves
the full conclusion, with no finite-parameter inference.

### Supporting exact screen and its limits

The approved screen compares the 625 two-word labels with
2<=J<=6,3<=H<=7 for each word. Use L020's imported finite coding
with one extra O input at the final endpoint and L021's composition.
For each concatenation of length D and multiplier A, let p0 be
its least positive CRT root, imposing p=20 modulo 27 as well as
all D+1 parity bits. All positive roots are exactly
p0+27*2^(D+1)*k for integers k>=0. The endpoint affine identity
then gives exactly m0+54*A*k. Thus the endpoint set is the
class m=m0 modulo 54*A with the lower bound m>=m0. The extra
O makes the second tail exact, and the first O of the second
word makes the first tail exact. Both intermediate and final
endpoints are residue 20 by L020.

Every endpoint modulus is twice a power of 3, so the two
endpoint classes overlap exactly when their residues agree
modulo the smaller modulus. Their lower bounds do not prevent
an overlap: a sufficiently large common lift meets both.
The script `scripts/postspell-inverse/check_inverse.py` tests
all 195,000 unordered label pairs, with complete replay checks
at the minimum and next CRT root of every class. Its certificate
`scripts/postspell-inverse/result.json` records all classes and
pair compatibility tests. There are 1,250 compatible pairs;
every such pair has the same final (J,H), hence the same final
predecessor at any common endpoint. There are zero compatible
pairs with different final words and zero failed checks among
1,250 guarded class replays. Rerun with
`python3 scripts/postspell-inverse/check_inverse.py`.

The finite calculation checks the implementation and suggested
the obstruction (4). It is not the proof for unbounded J,H;
that proof is the preceding exact argument. In particular a
fixed-endpoint uniqueness theorem does not bound the unrestricted
future endpoints of a fixed positive start.

## Mathlib

Full postspell extendible-inverse uniqueness and supporting affine,
valuation, parity-coding and CRT coverage: **not checked**. No
matching declaration, absence result, or formal verification is
asserted. Primary source identities and the elementary comparison
above are the mathematical inputs.
