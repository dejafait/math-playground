# L071 — A rational cubic norm-one unit is excluded at the rational dyadic place

## Hypotheses

Use L033's entire field K and curve E0, L046's rational embedding
K -> Q2, and L069's field D=K[θ] with

    g(θ)=0,   g(X)=X³−4X²−160X−1264.

Let V be L069's norm-square ordinary-unit kernel in D*/D*².
Let A=Q2[X]/(g), with the same distinguished generator θ, and let H
be L070's entire cubic Kummer image for E0/Q2. All local integer
rings below are maximal rings. No unit-group completeness, class-group,
rank, primitive solution, or GRH assumption is made.

## Conclusion

The rational cubic F=Q[θ] has an integral generator t satisfying

    t³−t²+t+1=0,           θ=8−14t+6t²,
    t=(−92−62θ+3θ²)/484.

Its unit u=−t has inverse t²−t+1 and norm N_F/Q(u)=1.
Under the specified inclusion F -> D it gives a nonzero class in V
whose rational dyadic localization lies outside H. Explicitly,

    u=(92+62θ−3θ²)/484.

Thus the necessary rational dyadic condition removes an actual global
ordinary-unit direction. This answers the saved subfield witness target
positively; it does not compute all subfield or degree-36 units, the full
filtered descent space, a rank bound, or any integer exclusion. In
particular it does not resolve ordered (3,4,11) or Beal.

## Proof

### Exact field coordinates and a genuine norm-one unit

Put f(T)=T³−T²+T+1. Modulo two, f(T)=(T+1)³. More usefully,
with s=t+1 its translate is

    f(s−1)=s³−4s²+6s−2.

This is Eisenstein at two: every nonleading coefficient is even and
the constant coefficient is not divisible by four. The standard
Eisenstein theorem proves irreducibility over Q2 and Q. Its root field
L=Q2[s] is totally ramified of degree three, has residue field F2,
and has maximal ring O_L=Z2[s]. These are the precise Eisenstein local
field consequences cited in L046 from Pete L. Clark, *Algebraic Number
Theory II: Valuations, Local Fields and Adeles*,
[author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 2.8 and Proposition 2.9/Corollary 2.10, printed pp.64–65
in the inspected 161-page version. The assertions concern the maximal
local ring, not the potentially nonmaximal global order Z[t].

In Q[t]/(f), exact reduction gives

    (8−14t+6t²)²=196−128t+124t²,
    g(8−14t+6t²)=0,
    −92−62(8−14t+6t²)+3(196−128t+124t²)=484t.

Therefore the assignment θ -> 8−14t+6t² identifies Q[X]/(g)
with Q[t]/(f), including its inverse displayed above; both have degree
three. The same identities after tensoring with Q2 identify the ENTIRE
algebra A with L, not just one factor. In particular g has no Q2 root,
so E0(Q2)[2]={O} in L069's origin-preserving cubic coordinates.

The relation t(t²−t+1)=−1 gives u(t²−t+1)=1. Both elements are
algebraic integers, so u is a unit of O_F without any assertion that
Z[t] is maximal. Since the constant coefficient of f is one,
N_F/Q(t)=−1, and hence N_F/Q(−t)=1. The exact multiplication
determinant in the certificate independently checks this norm.

The same integral equations and inverse hold in D. Norm is the
determinant of multiplication on the entire rank-three algebra and
commutes with base change, by Stacks Project
[Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2).
Applying Q -> K to the specified cubic and the same θ gives
N_D/K(u)=1. Thus [u] belongs to V. Nothing about its nonsquareness
in D is inferred from the even-degree extension D/F; it will follow
from the specified local obstruction below.

### A complete local image from one nontrivial point image

On Y²=g(X), take X=5. Then g(5)=−2039=1 modulo eight,
so there is an odd Y in Q2 with Y²=−2039. One can verify this familiar
dyadic square test directly: start with b3=1 satisfying the equation
modulo 2³. For n>=3, choose ε in {0,1} and put
b_(n+1)=b_n+ε·2^(n−1); its square changes by ε·2^n b_n
modulo 2^(n+1), so precisely one choice lifts the congruence.
The increments tend to zero two-adically and the limit has the required
square. This short lifting argument supplies the actual point; it is
not a finite residue sample substituted for local solubility.

Simon's *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.1,
Propositions 1.1–1.2, printed p.8, identifies the nonexceptional cubic
Kummer evaluation as X−θ. Our point is neither infinity nor a
two-torsion point: its norm g(5) is nonzero. Its image is therefore

    h=5−θ=−23+26s−6s².

Import Barrera Salazar–Pacetti–Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Lemma 1.3 and Remark 1.4, printed p.4.
For a finite extension B/Q2 the lemma gives
|δ(E(B)/2E(B))|=[O_B:2O_B]·|E(B)[2]|. Here the base is Q2,
not the cubic L. Its index is two, and the complete two-torsion size
is one by the entire irreducible factorization above. Consequently
|H|=2. The lemma includes the abstract evaluation at all exceptional
points. Once [h] is proved nontrivial, {1,[h]} is the full H; no disk
enumeration or assumption that sampled points exhaust H is needed.

### Exact square obstructions in the full maximal local ring

Here s³=4s²−6s+2 and s⁴=10s²−22s+8. For an arbitrary element
w=a+bs+cs² of O_L (using a,b,c in Z2 for its coordinates), its square
has coefficients

    constant: a²+4bc+8c²,
    s:        2ab−12bc−22c²,
    s²:       b²+2ac+8bc+10c².

An element is a unit exactly
when a is odd, because reduction modulo the uniformizer s is a modulo
two. If a local unit is a field square, its root has valuation zero and
is itself a maximal-ring unit. Therefore any putative square root here
has a odd and all three coordinates in Z2.

The s coefficient of every such square is even. Its s² coefficient
modulo four is b²+2c(a+c). Since a is odd, c(a+c) is even, so this
coefficient is b² modulo four, hence either zero or one. These
identities hold for every possible local square root, not merely
bounded integral candidates.

Now

    u=1−s,
    h=−23+26s−6s²,
    uh=−11+13s−8s².

All three are units, since their constant coordinates are odd.
The s coefficients of u and uh are odd, so neither is a square.
The s² coefficient of h is −6=2 modulo four, so h is not a square.
It follows that H={1,[h]}, while [u] differs from both elements:
the second comparison uses [uh]!=1 since every square class has
order two. Thus the localization of [u] is outside the entire H.
This is a specialization of the assessed exact local-square and
image-size methods; it does not reprove L070's index theorem.

Finally L046's fixed rational embedding K -> Q2 induces a unital
map D -> A=L by the same distinguished θ. Because D is a field
by L069 this map is injective. If u were a square in D, its image
would be a square in L, contrary to the coefficient obstruction.
Hence [u]!=1 in V. L070's necessary local condition therefore cuts
an actual global unit class. Full filtered ambient dimension remains
uncomputed; other units, S-units, ideal classes and other places are
independent obligations, as are rank and primitive integer lifting.

### Certificate and qualifications

Run `python3 scripts/rational-cubic-unit/check_witness.py`.
The full [certificate](../scripts/rational-cubic-unit/witness-certificate.json)
retains exact coordinate identities, unit/inverse and multiplication
norms, every one of the 256 unit residues of O_L/8O_L, their squares,
and the complete nonmembership comparisons. Fourteen checks pass with
no failures. The full target and square-residue fields were inspected.
There are sixteen square residues; the residues of u,h,uh are
(1,7,0),(1,2,2),(5,5,0), respectively, with no matching roots.
The coefficient proof above independently explains why no actual
two-adic root is missed. No sufficiency claim about finite precision
is required: impossibility modulo eight already excludes a square.
The initial hand-entered expected middle coefficient of uh was 39;
the exact checker rejected it. Reduction gives 13, now corrected;
both have the same residue modulo eight, so this correction changed
no square obstruction. The proof uses the corrected exact value.

The achieved witness threshold is one, matching the required one.
This is local progress using known methods, classified REPRODUCTION,
not a new unit theorem or a certified novelty claim. The independent
critical audit below accepts this witness. No complete Beal candidate follows.

### Independent critical audit (2026-10-15)

The audit accepts the statement and proof without a mathematical
correction. Run `python3 scripts/rational-cubic-unit/audit_witness.py`.
The full [audit certificate](../scripts/rational-cubic-unit/audit-certificate.json)
records 31 passing checks and no failures. It uses rational polynomial
long division and permutation determinants, imports no code from the
original checker and does not execute or overwrite that checker or its
certificate. It records the original certificate's SHA-256 and compares
every one of its 256 unit-root records, all sixteen square residues,
all three target/root comparisons and every load-bearing coordinate,
norm and point field with the independent recomputation. The original
success flags are checked for consistency only, not used as proof.

Both coordinate compositions are checked: t(θ(t))=t modulo f and
θ(t(θ))=θ modulo g, as well as f(t(θ))=0 and g(θ(t))=0.
Thus the specified generator is retained under both rational and local
identifications. The translated polynomial is exactly s³−4s²+6s−2.
Its leading coefficient is one and constant coefficient has valuation
one, so Clark's cited Eisenstein and integral-closure results apply to
the full cubic. They give O_L=Z2[s], not merely a suborder of unknown
index. Unit inverses are verified in both coordinates. The independent
multiplication matrices for u in the t and s bases have determinant
one; that for h has determinant −2039. Integral u and its displayed
integral inverse remain integral in D. The entire rank-three base
change F tensor_Q K=D, with θ fixed, meets Stacks 0BD2's finite locally
free constant-degree hypothesis and gives N_D/K(u)=1. This proves the
required unit-kernel membership, rather than just norm-square membership
in an unrelated cubic field.

The point-existence proof is an infinite lifting argument. For every
n>=3, an odd b_n with b_n²=−2039 modulo 2^n has exactly one lift of the
stated form, since b_n is odd and 2^(2n−2) is divisible by 2^(n+1).
The differences have valuation at least n−1, so the sequence converges
in Z2; continuity and the improving congruences give Y²=−2039. This
checks existence in Q2, not only the square residue. The origin-preserving
change X=4x, Y=8y+4 from L069/L070 identifies the whole elliptic curve
with Y²=g(X). All nonidentity two-torsion on this model has Y=0.
Irreducibility of the entire cubic over Q2 therefore proves that its
two-torsion group has order one. The base in BPT Lemma 1.3 is Q2;
[Z2:2Z2]=2 consequently gives |H|=2. Simon's nonexceptional evaluation
applies to the constructed point because g(5) is nonzero. Once h is
shown nonsquare, its class and the identity exhaust the image, including
all abstract exceptional evaluations. No enumeration assumption enters.

The square formula is independently checked as an identity in all six
homogeneous quadratic monomials in a,b,c. Every square root of a unit
must have valuation zero, hence belong to the full O_L and have odd a.
For these arbitrary Z2 coordinates its s coefficient is even, and its
s² coefficient is b² modulo four: a odd makes c(a+c) even. Thus the
obstructions to u and uh use their odd s coefficients, while the
obstruction to h uses its s² coefficient 2 modulo four. Recalculation
gives exactly uh=−11+13s−8s², confirming the previously corrected
middle coefficient 13. This proof covers all local roots independently
of the finite table; the full table agrees with it. In a square-class
group [u]=[h] would imply [uh]=1, so both members of H are excluded.

Finally L033's K and E0 are unconditional field/curve data; no primitive
solution or GRH-dependent Selmer dimension is assumed. Recalculation of
L046's m(2v)/4 gives the integral coefficient list with reduction 1+v,
so its simple odd root defines the specified rational embedding K -> Q2.
The map D=K[X]/(g) -> Q2[X]/(g)=L extends this embedding and sends θ
to the same θ. L069 establishes that D is a field, making the unital
map injective. Even without appealing to injectivity, an equation u=w²
in D would map to the forbidden local square equation. Thus the witness
survives in D; nonsquareness has not been transferred merely across the
even-degree extension D/F. The audit reuses L070's verified necessary
local condition rather than rederiving its index theorem.

The actual excluded-witness count is one, meeting the required one.
This closes L071's verification gap only. Full ordinary-unit generators,
non-unit contributions, the full filtered descent dimension, other
places, rank, subgroup indices/cosets and primitive integer lifting
remain unresolved. Existing direct mathematical inputs in the DAG are
unchanged. The result is a verified specialization of the assessed
methods, not a new general theorem or a complete Beal candidate.

## Mathlib

Full matching explicit unit/local-exclusion result and supporting field,
Eisenstein, norm, Kummer and dyadic-image coverage: **not checked**.
Unknown availability is not evidence of absence. The imported inputs
are the precise named primary results above.
