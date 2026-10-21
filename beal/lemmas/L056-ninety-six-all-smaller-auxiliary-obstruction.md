# L056 — No smaller auxiliary fields in MN cover L96

## Hypotheses

Use L051's L96=K96F of degree 36 and audited L055's actual finite
Galois overfield MN, with

    G=Gal(MN/Q)={(g,s) in PGL2(F11) x S3 : sign(g)=sign(s)},
    |G|=3960, X=P1(F11) x {0,1,2}, H=Stab_G((0,0)).

The G-set of all embeddings of L96 is X, of size 36. The sign on
PGL2(F11) is its determinant square class, equivalently the sign on
the twelve lines. In particular |H|=110. No normality of L96, GRH,
class-group completeness or particular subgroup classification is assumed.

Import Fabrice Etienne, *Computing class groups by induction with
generalised norm relations*,
[arXiv:2411.13124v2](https://arxiv.org/pdf/2411.13124v2), April 23, 2025,
Proposition 2.7 (printed pp.12–15) and Definition 2.9 (p.15).
They identify generalized norm relation existence with a surjection
from arbitrary copies of the auxiliary rational permutation modules
to Q[G/H]. The complete orbital-map correspondence is Proposition 1.3,
Definitions 1.8 and 1.10, Lemmas 1.11–1.12 and Proposition 1.13
(pp.5–9), assessed and used in L055. Only these known criteria are
imported, not an arithmetic or class-group conclusion.

## Conclusion

All subfields E of MN with [E:Q]<36, jointly and with arbitrary
module multiplicities, fail to support a generalized norm relation
for L96 over Q. The sum of the images of **all** equivariant maps
Q[G/J] -> Q[G/H], over every subgroup J with [G:J]<=35, has rational
dimension 14, rather than the required 36.

There are exactly seven qualifying subgroup conjugacy classes, of
indices 1,2,3,6,12,22,24. Complete unfiltered enumeration gives 67
subgroup conjugacy classes and 6,906 actual subgroups in G.
This parks smaller auxiliaries in this particular overfield only.
It neither excludes the 96a1 integer branch nor supplies any auxiliary
class/unit arithmetic, integral saturation, transfer, torsion lifts,
support/norm maps, descent compatibility or full-disk disjointness.
The independent critical audit below confirms this finite certificate without a mathematical correction.

## Proof

### Exact finite group and the enumeration procedure

Use L055's complete normalized projective matrices, their twelve-line
actions, all S3 permutations, and all sign-compatible pairs. For a pair
(g,s), the program uses the faithful permutation on fifteen letters
given by g on 0,...,11 and by s on 12,13,14. All 3,960 such permutations
are distinct. Composition of every ordered pair gives the multiplication
table; a missing permutation is an execution failure. The four generators

    (u,id), (v,id), (diag(2,1),(01)), (id,(012)),
    u=(1,1;0,1), v=(1,0;1,1),

generate all 3,960 elements, as in audited L055. Their induced actions
on X are saved completely. Direct enumeration gives a transitive action
on 36 points and stabilizer size 110, agreeing with the actual field
interface. These field identifications are inputs, not conclusions
inferred from the finite program.

The backend starts at the trivial subgroup. For each discovered subgroup
conjugacy representative K, with saved generators, it performs the
following exact operations, **without** an index filter:

1. Generate K by closure under its generators and enumerate its full
   normalizer N_G(K). To test n in N_G(K), conjugate each generator into K;
   inclusion nKn^{-1} subset K is equality because both groups have the
   same finite order. Generate the entire resulting normalizer as a check.
2. Partition all 3,960 elements x into orbits under left and right
   multiplication by K's generators and conjugation by N_G(K)'s generators.
   All these operations are bijections. Forward closure in this finite set
   includes the inverse operations and therefore gives complete orbits.
3. For one x in each orbit, generate <K,x>. Find its subgroup conjugacy
   class by exact element-set equality. If new, retain it and generate
   **every** conjugate under the four generators of G. Store an actual
   conjugating element for each equality. Hashes only locate candidates;
   full bitsets are compared, so hash collisions do not identify subgroups.
4. Continue until every discovered representative has been processed.
   The runtime cutoff, if reached before this point, explicitly reports
   incomplete coverage. It was not reached in this completed run.

The reduction in step 2 loses no subgroup class. For k,k' in K,
<K,kxk'>=<K,x>; for n in N_G(K),
<K,nxn^{-1}>=n<K,x>n^{-1}. A sequence of the orbit operations consequently
changes an extension only within its conjugacy class.

For completeness, take any subgroup S=<s1,...,sr> of this finite group
and its prefix subgroups S_i=<s1,...,si>. The trivial prefix is present.
If K=a S_i a^{-1} is represented, adjoining a s_(i+1) a^{-1} gives
a S_(i+1) a^{-1}. Its element belongs to one of the completely processed
reducing orbits, whose representative produces a conjugate of that same
extension. Induction supplies a representative of S. An exhausted
frontier therefore covers **all** subgroups, including perfect ones;
no perfect seeds or classification theorem are needed for this method.
Conjugate permutation modules are isomorphic, so class representatives
suffice only because we subsequently retain every equivariant map.

The output has 67 processed and 67 discovered classes. The complete
conjugacy orbits contain 6,906 distinct subgroup sets. The Python driver
checks every processed subgroup's full generator closure, every full
normalizer and reducing orbit, and every extension equality with its
saved conjugating witness. It also checks every saved subgroup conjugate
and closure of each whole conjugacy class under all four generators of G.
This verifies the exhausted frontier and the distinct class coverage,
not merely the count of an incomplete displayed list.

Only after full enumeration apply [G:J]<=35. The seven rows below give
the exhaustive qualifying representatives. Element numbers refer to
the complete sign-compatible group list in the certificate; their full
permutations and all subgroup elements are saved, so they are exact
generators, not unspecified catalogue labels.

| Enumeration class | Generators (element numbers) | Order | Index | J-orbit sizes on X |
| --- | --- | --- | --- | --- |
| 35 | 4,369 | 3960 | 1 | 36 |
| 29 | 3,361 | 1980 | 2 | 36 |
| 30 | 3,369 | 1320 | 3 | 12,24 |
| 28 | 3,360 | 660 | 6 | 12,12,12 |
| 33 | 4,30 | 330 | 12 | 3,33 |
| 32 | 3,781 | 180 | 22 | 36 |
| 24 | 3,34 | 165 | 24 | 3,33 |

G itself is included (the auxiliary field Q). All qualifying J are
nontrivial, as required by the imported criterion. Every fixed field
of degree below 36 corresponds to one of these classes and its conjugates
by finite Galois correspondence in this **actual** overfield MN.

### Complete maps and their rational images

For each J, a G-equivariant map from Q[G/J] to Q[X] is determined by
the image v of the basis vector e_J. Equivariance makes v J-invariant,
and conversely every such vector gives the well-defined map e_(gJ) -> gv.
The indicators of the J-orbits on X form a basis of Q[X]^J. Thus using
every J-orbit indicator and every left coset gJ gives every map in a
basis of this Hom space, not a selected trace or selected compositum.
This is the imported orbital correspondence in explicit coordinates.

The certificate saves a complete left-coset partition for each of the
seven J, all J-orbits on X, and every resulting 36-by-[G:J] map matrix.
There are respectively 1,1,2,3,2,1,2 maps in the order of the table,
and 121 columns altogether. The coset partition is exact; no embedding
or unequal compositum column is omitted.

For **every** saved column w and every a in {0,...,11}, b in {0,1,2},
the exact integer check gives

    w(a,b)-w(a,0)-w(0,b)+w(0,0)=0.

This forces w(a,b)=f(a)+g(b), by setting f(a)=w(a,0) and
g(b)=w(0,b)-w(0,0). Hence every complete auxiliary map has image in
the coordinate-sum space W of audited L055, of dimension 12+3-1=14.
L055's K96 and F are among the smaller fields under consideration;
their complete maps already span W. This supplies the matching lower
bound 14 without relying on a numerical rank estimate. Exact rational
row reduction of all 121 columns independently gives rank 14 and saves
all pivot indices and the complete reduced matrix. Its actual rank is
14 against required rank 36, and all checks have zero failures.

Arbitrarily many copies of these modules can only sum images in W.
They cannot surject onto Q[X]. Etienne Proposition 2.7 and Definition
2.9 apply to this finite Galois overfield and these nontrivial J, giving
the stated generalized-relation obstruction. No normality of L96 or
unconditional auxiliary arithmetic is needed for this finite criterion.

### Reproduction and qualifications

Run

    python3 scripts/ninety-six-generalized-relation/all_smaller.py

This compiles `all_subgroups.c` with clang and regenerates the full
unfiltered frontier before checking it. The completed run used Apple
clang 21.0.0; Python version, platform byte order and source SHA-256
values are recorded in the main certificate. The backend's multiplication
table is an explicit native-endian uint16 array with 3,960 squared
entries, with its checksum and byte order retained.

The full result is
`scripts/ninety-six-generalized-relation/all-smaller-certificate.json`.
It contains every processed class, its generators and elements, complete
normalizers, every reducing orbit and extension witness, all seven
coset partitions and map matrices, exact rational row reduction,
coordinate checks, actual/required rank, and all failures. The companion
`all-smaller-conjugates.jsonl` contains every conjugate subgroup and its
witness; `all-smaller-classes.jsonl`, `all-smaller-summary.json` and
`all-smaller-multiplication.bin` retain the backend evidence. Checksums
identify these artifacts. The driver loads and checks complete relevant
evidence, not JSON previews or selected samples.

This is REPRODUCTION under the preexisting SPECIALIZE assessment
`drafts/literature/2026-10-11-ninety-six-smaller-auxiliary-coverage-test.md`.
The general relation theorem is imported; the equivalent enumeration's
completeness argument and exact field-specific coverage are necessary
because GAP/Sage were unavailable and runtime success was not assessed.
No originality beyond the sources checked is asserted. This extends the
pair-specific stop of L055 to all strictly smaller fields in MN. Other
overfields, equal or larger auxiliary fields, and different arithmetic
mechanisms are outside the conclusion. The independent critical review below verifies this enumeration and certificate.

### Independent critical audit — 2026-10-11

This audit uses the preexisting SPECIALIZE scope in
`drafts/literature/2026-10-11-ninety-six-all-smaller-obstruction-audit.md`.
It confirms the conclusion, with no change to hypotheses, mathematical
inputs or the MN-only scope. The actual field interpretation remains
L051 and audited L055; this audit does not infer it from a finite group.
The cited Etienne v2 Proposition 2.7 and orbital correspondence are reused,
not reproved. Neither perfect-seeded cyclic-extension algorithms nor an
unexecuted GAP catalogue supplies completeness here.

**Independent group and evidence provenance.** The separate verifier
constructs every invertible projective matrix over F11 normalized to
first nonzero entry one. It checks distinctness of the 1,320 twelve-line
actions, their permutation signs against determinant square classes,
and every sign-compatible pair with S3. These recover exactly all 3,960
saved fifteen-letter permutations, in the saved numbering. It also
reconstructs all 3,960 actions on the 36 pairs, the actual 110-element
stabilizer H, transitivity, the identity and the four specified generators.
Their closure is the full group. The entire backend input is compared.
Source and companion-artifact hashes match the recorded provenance;
hashes alone are not mathematical verification.

The native-endian table is decoded using its recorded byte order, with
its exact byte length and every entry's range checked. For every ordered
pair (a,b), the permutation at the saved product index equals the
coordinatewise composition a after b. Thus all 3,960^2=15,681,600 entries,
not a sample or just generator rows, are verified. Inverses reconstructed
from the permutations satisfy both product identities, and both identity
rows are checked. Subsequent use of this table therefore refers to
independently verified permutation composition. Associativity follows
from this faithful composition model; it is not assumed from the binary
file. No producer routine is imported.

**Every subgroup and exhausted frontier.** All 67 representative sets
are regenerated by fixed-point multiplication closure. The initial set
is explicitly the trivial subgroup with empty generator list. For every
representative, the verifier conjugates every subgroup element by every
group element to reconstruct the complete normalizer, then independently
checks its saved generators. For the reducing orbits, a disjoint-set
component algorithm uses all generator edges for left/right multiplication
by K and conjugation by its normalizer. These are bijections of a finite
set, so their undirected components equal the orbits under the operations
and their inverses; positive closure gives the same orbits. The complete
partition of all 3,960 elements agrees with the saved partition.

Every orbit has its saved representative x, and the whole generated
extension <K,x> equals the whole conjugate of its claimed target class
under the saved conjugator. All target class indices refer to processed
representatives. There is no index filter at this stage. The two
identities <K,kxk'>=<K,x> and
<K,nxn^{-1}>=n<K,x>n^{-1} for n in N_G(K) justify the reductions.
The prefix-subgroup induction in the proof consequently starts at the
verified trivial class and reaches a represented conjugacy class of
any subgroup. It does not assume solvability and includes perfect
subgroups. Exhaustion is proved from these checks, not from a Boolean
completion flag or the original empty failures list.

Every one of the 6,906 conjugate records is checked against its full
conjugating witness. All recorded element sets are distinct, each
representative occurs in its own class, and every conjugacy class is
closed under all four group generators. Independently, each class has
exactly |G|/|N_G(K)| members. Thus full orbits and their disjointness
are verified, with no absent seed orbit or erroneous class fusion.
The main certificate's entire class data agree with the companion
records; 67 processed/discovered classes and 6,906 actual subgroups
agree with the independently verified sets.

**Every map and exact rank.** Only after the exhaustive check does the
verifier select index below 36, recovering exactly the seven stated
classes. Their orders divide 3,960 and all are nontrivial. It reconstructs
left cosets using every group element and J-orbits on X using every
subgroup element, rather than trusting saved representatives or orbit
sizes. Every coset, representative, orbit and entry of every map matrix
is compared with the full original evidence: twelve maps, 121 columns.

The image of e_J determines an equivariant map and must be J-invariant;
conversely the assignment e_(gJ) to gv is well-defined for a J-invariant
v. Hence the complete orbit-indicator basis checks the entire Hom space.
Conjugate J yield isomorphic source modules, so class representatives
lose no possible images. Every mixed coordinate difference of every
column is zero. The dimension of the resulting coordinate-sum space is
14 because the 12-dimensional and 3-dimensional coordinate function
spaces intersect precisely in constants. L055's two smaller fields
supply the matching lower bound. In addition, a separate exact rational
elimination, choosing pivots independently, verifies rank 14 and compares
all saved pivot columns and every entry of the full reduced matrix.
The required dimension is 36. Arbitrary copies of the auxiliary modules
still sum images in the same proper subspace. The actual finite Galois
overfield and nontrivial J meet the cited Etienne criterion; neither
normality of L96 nor GRH is assumed.

Reproduce this independent check with

    python3 scripts/ninety-six-generalized-relation/audit_all_smaller.py

It uses Python and NumPy for bounded exact integer arrays and Fraction
for rational elimination. Versions and verifier/source/input hashes are
recorded in
`scripts/ninety-six-generalized-relation/all-smaller-audit-certificate.json`.
The separate certificate retains independently reconstructed group/actions,
all normalizers and reducing orbits, all checked extension/conjugate
witnesses, all cosets and maps, every mixed difference, full rational
reduction, checks and failures. Its status is VERIFIED with no failures,
actual rank 14 and required rank 36. All original evidence is preserved.
This verifies a field-specific reproduction of the known criterion,
not progress beyond the sources toward a Beal resolution. It closes the
pending finite audit only: unconditional arithmetic, descent, full-disk
disjointness, other overfields and residual signatures remain unresolved.
This canonical audit supersedes pending-review wording in the unchanged
PROOF.md assembly; no mathematical correction or DAG change is needed.

## Mathlib

Full matching field-specific exhaustive auxiliary obstruction: **not
checked**. Supporting finite groups, Galois correspondence and permutation
module results: **not checked**. Unknown availability is not absence.
No formal verification or Beal resolution is claimed.
