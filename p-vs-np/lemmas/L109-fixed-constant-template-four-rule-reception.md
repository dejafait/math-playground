# L109 — Fixed constant-template reception in the four-rule system

## Hypotheses

Fix a finite library ℒ of finite ordered formula trees with formal slots
s₁,…,sₘ, primitive binary ∨, unary ¬, and Boolean constants true and
false. The slots are metasyntactic leaves, distinct from both constants.
Every member is a tautology for every Boolean assignment to its slots,
with true=1 and false=0. The library, including m, is fixed independently
of the receiving input. Abbreviations, if used to specify it, are expanded
literally before fixing these trees.

Use precisely the propositional system declared in L108: axiom instances
¬A∨A, the ground axioms true and ¬false, and the four directed rules

    A                         ⟹ B∨A,
    A∨A                       ⟹ A,
    A∨(B∨C)                   ⟹ (A∨B)∨C,
    A∨B,  ¬A∨C                ⟹ B∨C.

All matching is literal ordered-tree matching. A proof is a finite
sequence of fully written formula trees, axiom/rule tags and backward
premise references. There are no assumptions or additional inference
rules. In particular, substitution is not an inference rule.

Supply an explicit finite alphabet Γ and arbitrary formula trees
A₁,…,Aₘ over Γ, ∨, ¬, true and false. Every variable occurring in an Aᵢ
must be in Γ; unused names and unused slot arguments are allowed. Images
need not be distinct or have bounded depth. Γ may be empty.

For a concrete full-bit convention use prefix formula-tree encoding,
with fixed connective/constant tags and length-delimited binary variable
names. Proof records have fixed tags and self-delimiting binary premise
indices. Let ‖A‖ be the complete formula bit length in this convention,
including every name occurrence, and put

    P = 2 + |Γ| + Σᵢ ‖Aᵢ‖,

where |Γ| includes the entire supplied name dictionary and its framing.

## Conclusion

For each H∈ℒ there is an assumption-free proof ending at the **exact**
tree H[A₁/s₁,…,Aₘ/sₘ] in the specified system, with no variable names
outside Γ. After preparing ℒ once, a deterministic instantiation
procedure produces all its proof records, preserving unused lines and
backward references. There are library-dependent constants Cℒ,Nℒ such
that the number of output proof records is at most Nℒ and the complete
output bit length, including Γ if retained, is at most CℒP. Construction
takes at most CℒP² deterministic bit time in a straightforward explicit
copying implementation. In particular CℒP² is also a valid full-bit
bound. Summing the outputs for the entire fixed library satisfies the
same form of bound after increasing these constants.

Library preparation has no asserted polynomial bound as a function of
ℒ. This is a specialization/reproduction of the cited consequence
theorem and syntactic proof copying, without a novelty claim. It does
not assert short proofs for arbitrary input tautologies, implement a
specific template library, or establish an occurrence/parity receiver
composition. The separate step-432 critical audit below found no
substantive defect under the stated hypotheses; no implementation is
verified.

## Proof

### 1. The imported constant-free input

Use Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley (1967),
§2.6 pp.21–22 and §3.1, **Tautology Theorem (Post)**, printed p.27,
with proof pp.28–30
([primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf)).
The consequence form says that a tautological consequence of finitely
many proved formulas is provable. Its propositional proof uses the
axiom ¬D∨D and the four rules displayed above. The inspected proof's
commutation and detachment are derived operations; its complementary
literal, disjunction, double-negation and negated-disjunction cases use
no first-order axiom or quantifier inference. We use that propositional
fragment with additional nonlogical axioms, as permitted in §2.6.
Every derived operation is expanded into its finite primitive proof.
No proof-length bound for this completeness theorem is imported.

This source uses individual constants in its language, not primitive
truth constants. To realize the needed independent propositional atoms
syntactically, take distinct unary predicate letters R₁,…,Rₘ,U,V and
one individual constant c. The atomic sentences Rᵢ(c), U(c), V(c)
serve as sᵢ*,p,q. They are distinct elementary formulas and their truth
values are independent in the propositional theorem. The individual
term c will never be mapped separately: whole atomic sentences will be
replaced. This use of c introduces no Boolean-constant premise.

The local work below is needed because the source does not state
primitive truth-constant reception or a full-bit instantiation bound.
It does not reprove the cited connective completeness cases. The ready
source assessment is
`drafts/literature/2026-10-23-four-rule-constant-template-reception.md`.

### 2. Remove the two constant premises by literal replay

For H∈ℒ form the constant-free propositional tree H* by replacing each
slot sᵢ by sᵢ*, true by p, and false by q, preserving every connective
and ordered child. Under any truth valuation satisfying p and ¬q,
the values of p,q are 1,0. The hypothesis on H therefore implies that
H* is a tautological consequence of p,¬q.

In the source propositional fragment adjoin exactly p and ¬q as
nonlogical axioms. The cited consequence theorem supplies a finite
derivation δ of H*. After expanding derived operations, its records
are only instances of ¬D∨D, the two additional axioms p,¬q, and the
four primitive rules. This selection of a propositional derivation is
justified by the cited proof cases, not by deleting first-order steps
from an arbitrary proof.

Define a simultaneous syntactic map ρ on δ: map sᵢ* to sᵢ, p to true,
and q to false, and commute with ¬ and the ordered ∨ constructors.
Any other atomic formula in the selected finite propositional
derivation may be mapped to true. Thus the argument does not assume
that completeness forbids auxiliary atoms. The selected derivation
has no quantifier inference or first-order axiom. Formula images are
formed by recursion on their propositional trees; replacement does
not recurse inside an image.

Replay every record once, in the same order, with the same premise
indices. The axiom ¬D∨D becomes ¬ρ(D)∨ρ(D), a permitted instance.
The added axioms p and ¬q become exactly true and ¬false. For expansion,
ρ(B∨A)=ρ(B)∨ρ(A); for contraction, both copies of A have the same
image; for association, the two ordered bracketings become exactly
ρ(A)∨(ρ(B)∨ρ(C)) and (ρ(A)∨ρ(B))∨ρ(C). Finally cut's premise images
are exactly ρ(A)∨ρ(B) and ¬ρ(A)∨ρ(C), and its conclusion image is
ρ(B)∨ρ(C). These are all permitted primitive records. Collapsing two
distinct atoms or formula arguments causes no failure of any rule:
the rules have no distinctness or freshness side condition.

The result δ_H is consequently an assumption-free proof over slots
and constants, ending at exactly H. No p, q, source predicate, term c
or auxiliary name remains. In particular the two premises have become
legal axioms, rather than undischarged assumptions. The conclusion's
tree is unchanged except for the specified leaf images; no semantic
normalization or endpoint identification has been used.

### 3. Fixed proof selection and arbitrary formula images

Select one such finite δ_H for each member of ℒ. This finite preparation
can be incorporated into the instantiation procedure as fixed data.
It is effective if desired: enumerate finite proof records over the
finite slot/constant alphabet, check the displayed axiom and rule
patterns and references, and retain the first proof with endpoint H.
Section 2 proves termination for each H. Enumeration is only a possible
preparation procedure and supplies no efficiency claim in the library
size. No preparation search is performed on the receiving input.

Now replace each slot leaf sᵢ in every record of δ_H by the fully written
tree Aᵢ, simultaneously, leaving the two constants fixed. The record
replay checks in §2 apply verbatim to arbitrary formula images: they
use only commutation with the two tree constructors and equality of
repeated arguments. Every axiom/rule tag and backward reference can
therefore be retained. This is a procedure for writing a proof, not
an appeal to a substitution inference on a previously proved line.

All resulting formula names occur in the supplied Aᵢ and hence in Γ.
The endpoint is the literal ordered substitution H[A₁/s₁,…,Aₘ/sₘ].
Repeated images, images containing constants, arbitrary depth, m=0
and empty Γ cause no change to the replay. For empty Γ the input trees
contain only constants and connectives. There is no requirement for a
fresh propositional name even in that case. For an empty library the
all-library claim is vacuous.

### 4. Full copying, reference and time bounds

Across all selected δ_H let r be the total number of records, b the
total bit cost of non-slot formula tags and proof-record framing, and
kᵢ the total number of occurrences of slot sᵢ in every written proof
formula. These are finite constants depending only on the prepared
library. They count entire proofs, including intermediate and unused
records, rather than just the endpoints. Set k=max(1,k₁,…,kₘ), taking
k=1 if m=0.

Prefix tree serialization writes each slot image contiguously once at
each occurrence. Consequently the formula and fixed-record portions
of all outputs have total bit length at most

    b + Σᵢ kᵢ ‖Aᵢ‖ ≤ b + k Σᵢ ‖Aᵢ‖.

The premise-index lengths cost O(r log(r+2)) in total, a library
constant. Formula expansion creates no proof records and changes no
line indices. Retaining the complete Γ once, or once per fixed proof,
adds at most |ℒ|·|Γ| plus fixed framing. This pays long names at every
formula occurrence through ‖Aᵢ‖ and pays unused input names as well.
Thus the total is at most CℒP, with r≤Nℒ. No dictionary lookup or formula
sharing is used to omit copied names or trees.

A copying procedure traverses each fixed proof skeleton and copies
the requested input substring at each slot occurrence. There are at
most Σᵢ kᵢ requests, a library constant. Even rescanning the entire
explicit input for each request, writing every output bit, and checking
input syntax/membership by pairwise name comparisons takes at most
CℒP² bit operations with sequential scans and ordinary work tapes.
Arbitrarily deep input trees can be scanned using an explicit stack
of O(P) symbols. No proof-ancestry unfolding occurs. The bound concerns
this specified explicit prefix encoding; a different encoding requires
charging its conversion rather than silently treating names or internal
tree references as constant length.

These all-size replay and counting arguments meet the fixed-library
threshold. They do not provide concrete serialized library proofs or
a verified implementation. L108's algebraic extraction theorem is
not invoked here; its syntax is restated in the hypotheses. Combining
the results with occurrence transfer, an actual source compiler or an
original-Q ledger remains a separate obligation. L107 and Attempt 036
remain obstructions to the old three-scheme/MP presentation. No source
proof availability, M-only bound, universal W₂, arbitrary ER data or
unrestricted SAT result follows.

### 5. Independent critical audit — step 432, 2026-10-23

The audit reuses the completed step-429 primary coverage and the prior
SPECIALIZE scope in
`drafts/literature/2026-10-23-constant-template-reception-critical-audit.md`.
It checks this entire proof, including its receiving encoding, rather
than using semantic truth of a few instantiated endpoints as evidence.
The source citation and its propositional-fragment qualification in §1
remain essential. No additional completeness theorem is assumed.

**Consequence and constant reception.** The distinct atomic sentences
sᵢ*,p,q are independently valued elementary formulas in the cited
propositional theorem. Every valuation making both added axioms p,¬q
true evaluates H* exactly as a Boolean assignment evaluates H with its
prescribed constants. Thus the consequence premise is met for every
slot valuation, including when there are no slots. Treating p,¬q as
nonlogical axioms makes them proved premises for that theorem. Its
inspected constructive propositional proof supplies the required
derivation using only the axiom and rules in §1. This is stronger than
merely knowing that some first-order derivation exists; deleting
first-order records from an arbitrary proof would not be justified.

The simultaneous map acts on whole atoms, not on c or predicate symbols
inside them. Its images of the two added axioms are exactly true and
¬false. Any additional atom is sent to true. Therefore every formula in
the replay, not only the endpoint, is over slots and the two constants.
There are no surviving auxiliary atoms, eigenvariable conditions or
assumptions. At the endpoint each original constant and slot is restored
at its original position in H; order and bracketing are unchanged.

**Primitive-record induction.** For either the atom replay or the later
slot instantiation, write σ for the constructor-preserving map. The
axiom ¬D∨D maps to ¬σ(D)∨σ(D). The exact premise/conclusion pairs for
the four rules are, respectively,

    σ(A)                         ⟹ σ(B)∨σ(A),
    σ(A)∨σ(A)                    ⟹ σ(A),
    σ(A)∨(σ(B)∨σ(C))             ⟹ (σ(A)∨σ(B))∨σ(C),
    σ(A)∨σ(B), ¬σ(A)∨σ(C)        ⟹ σ(B)∨σ(C).

These have the declared directions, including association and cut.
They need no conversion to a Boolean-equivalent formula, detachment
rule or syntactic commutativity. The second map fixes true and false,
so both ground axioms also remain legal. Induction on the record index
establishes legality with the same strictly earlier references. Repeated
premise references and coincident images are harmless because no rule
requires distinct arguments. Inserted Aᵢ trees are copied without
applying σ to their internal names. Thus names resembling slot names
do not initiate recursive replacement. Empty Γ, constant-only images,
unbounded image depth and unused arguments all satisfy the same proof.

**Full-bit and time threshold.** Independently let b₀ count the fixed
non-slot formula bits and record tags over all selected proofs, and let
h count all fixed reference/framing bits. The total record count r is
fixed; self-delimiting references contribute O(r log(r+2)) to h. For
one or all library outputs, a complete bound is

    b₀ + h + Σᵢ kᵢ‖Aᵢ‖ + |ℒ|·|Γ| ≤ Cℒ P.

Any extra fixed framing can be absorbed using P≥2. All proof formulas,
including unused lines and every occurrence of each repeated slot, are
included in kᵢ. Prefix serialization requires no input-size-dependent
subtree pointers or new proof records. A copied variable occurrence
includes its complete length delimiter and name bits. Retaining unused
dictionary names is paid by |Γ|. For an empty library there are no proof
records; retaining a single optional dictionary still costs at most P.
Concatenating fixed proofs, if desired, shifts references by fixed record
counts and changes only h, not the input-dependent bound.

For the time claim, parse the m supplied prefix trees with an explicit
stack or pending-child counter; m is fixed. Even charging O(P) bit work
per input symbol gives O(P²) parsing time on ordinary work tapes. For
membership, let u be the number of variable occurrences in the input
trees, v the number of dictionary entries, L the sum of the complete
occurrence-name lengths, and D the complete dictionary length. All four
quantities are at most P. A sequential dictionary scan for each
occurrence, with a work-tape copy of its name, costs
O(uD+vL+P): compare and rewind that name for each candidate, while
scanning each candidate's serialized name once. This is O(P²).
Pairwise duplicate-name checking, if required by the dictionary format,
has the same bound with dictionary names on both sides. These scans
avoid any assumption of constant-time comparison of long names.

Finally the fixed skeletons issue only Σᵢ kᵢ copying requests. Locating
an input tree by a full input rescan and writing its full serialization
per request costs Oℒ(P), and even a coarse O(P²) allowance per request
stays Oℒ(P²). Arbitrary tree depth causes no recursion-depth assumption.
Together these operations establish the claimed quadratic bit-time
threshold separately from the linear output-length threshold. Neither
bound includes proof search over a varying library: library preparation
is deliberately unbounded and occurs before receiving the input.

**Verdict and limits.** No substantive defect or change to the theorem,
proof argument or dependencies was found. This establishes an independently
checked informal fixed-template input, reproducing standard consequence
and syntactic-copying machinery; it is not a new completeness result or
progress beyond the inspected sources' logical mechanism. No particular
library's tautologicity, serialized proofs or compiler has been checked.
L108's extraction conclusion is not a mathematical input to this proof.
L107 and Attempt 036 retain their old-interface stops. L097/L098/L106
composition, original-occurrence/Q accounting, short source proofs,
M-only bounds, universal W₂, arbitrary ER data and unrestricted SAT
remain unresolved. Mathlib coverage remains unchecked.

## Mathlib

Full matching four-rule theorem, truth-constant replay and full-bit
encoding bound: **not checked**. No absence claim is made. Supporting
formal ingredients would be induction on formula trees, syntactic
substitution and finite proof-record induction. The precise imported
mathematical input is Shoenfield's named theorem with its hypotheses
and propositional-proof qualification given above. No Mathlib theorem
or verified compiler is asserted.
