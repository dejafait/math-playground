# L069 — Complete-record two-identity reception for supplied balanced trees

## Hypotheses

Use the unconditional original-CNF/ordered-axiom definitions of L048,
without either existential size assertion. Supply the actual width-at-most-three
CNF F, including every signed occurrence, its binary OR and conjunction
trees, the complete distinct occurring-variable dictionary, the entire ordered
axiom dictionary A and disjoint position-role placeholder dictionary. An empty
clause denotes false, and the empty conjunction denotes true. Repeated clauses,
variables and complementary literals are retained in order.

Supply L054's ordered division-free F₂ occurrence tree C, with s nodes and
depth h≤a log₂(s+2), where the positive integer a is fixed independently of
the input. Constants, mixed degree, repeated/nonlinear placeholders and unused
permitted dictionary symbols are allowed. Both identities

    C(x,0)=0,                 C(x,A(x))=1                         (1)

are formal identities in the free noncommutative algebra, not Boolean-only
identities or unverified Frege premise records. The actual clause axiom is the
ordered product of the occurrence falsity factors 1+x or x, with either
binary product bracketing when there are three literals. Its bracketing need
not equal the actual clause OR bracketing. Boolean and commutator trees are
exactly (x*x)+x and (x*y)+(y*x). Empty products are 1. These are the bounded
factored source trees in L054's 11-node estimate. Arbitrary equivalent
expressions and unbounded expanded/padded representations are not admitted.

Use one fixed native encoding, L056's ax-1/2/3/MP basis, and one q throughout.
Write Y=(q→q), Z=¬Y, X(U,V)=((U→V)→¬(V→U)), E=¬X,
P(U,V)=¬(U→¬V), OR(U,V)=(¬U→V). Eval translates the actual
arithmetic tree using Y,Z,X,P; Φ is the actual CNF translated using P/OR
and its signed literals. Every abbreviation is expanded in every record.
The other format is exactly L056's literal NOT/OR image τ, with no
double-negation simplification or independent ordinary-input premise.

Names are distinct nonempty ASCII alphanumeric/underscore payloads in the
original dictionary. q may coincide with an original or schematic name.
Typed original and placeholder roles never alias. For other finite identifiers,
first use a fixed injective encoding, for example `o_` followed by the hex
encoding of the original identifier bytes and `t_` followed by the positive
position index for placeholders. Store the complete inverse dictionary and
role tags. The conclusion is Φ with precisely these encoded original names;
this is a bijective renaming of the input formula, not an identification of
distinct inputs. Use byte-string lexicographic order for the raw dictionary;
the fixed-width two-hex-digits-per-byte encoding preserves that order,
including proper prefixes. Thus the dictionary and i<k positions are
unchanged and meet L060's ordered convention after encoding.

Optional inputs may be any finite list of complete native primitive proof
occurrences with all records, declarations, headers, paths and payloads paid
and validated as in L068. They supply no hypothesis. Count repeated occurrences
separately. If encoding is needed, encode all propositional names consistently
in these proofs too, including auxiliary names, using one injective map; keep
their complete original payloads. There is no mutable external proof cache.
Let Q≥2 be two plus the complete uncompressed original input byte length,
including F,C,A, all dictionaries, names, paths and optional occurrences.
All component admissions and encoding conventions are fixed before inputs.

## Conclusion

There is an abstract deterministic construction of a complete primitive
native proof with exact last record ¬Φ and its exact literal image. In the
nonempty-clause branch it constructs the two actual L068 packages, retains
both whole output proofs, constructs guards for the exact source axiom trees,
retains each complete occurrence's L059 proof and emits the final primitive
composition. No proof premise, semantic equivalence, PIT answer or definition
is a rule. One fixed polynomial in Q bounds construction/checking bit time
and the full uncompressed output, including intermediate exports, optional
occurrences, names, dictionaries, reference relocation and specified manifests.

This was recorded as an **UNVERIFIED CANDIDATE for the conditional receiver**
at step 249. The separate step-251 informal audit in §8 finds no substantive
defect in the abstract assembly or its bound. It is not a P-versus-NP candidate.
The six new fixed native/image pairs are checked in full below. A generic
whole-receiver executable and nonempty-letter joined execution are not
implemented or verified; L068 is used by its audited abstract contract.
Neither short-certificate existence, arbitrary ER representation, arbitrary
ordinary-proof input completeness, W/V/U nor a SAT consequence is supplied.

## Proof

### 1. Prior coverage, exact source admission and naming

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-15-two-identity-original-cnf-complete-record-receiver.md`.
Li, Tzameret and Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, [arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4),
Definition 4.3 and Lemma 4.4, printed pp.21–23, provide the logical final
receiving pattern conditional on the two Boolean identity proofs. Theorem 4.1,
p.19, states a quasipolynomial general GF(2) 3CNF receiver; it is not imported
as this polynomial record bound. The specialization needed here is literal
source reception and complete primitive copying, not a reproof of a new PIT
theorem. L055 §6 and its step-166 audit provide the earlier informal pattern,
not a primitive whole-receiver premise.

Use L056's inspected [Church P2/Lukasiewicz completeness metatheorem,
§§1.2–1.2.2](https://us.metamath.org/mpeuni/mmtheorems1.html) only for fixed
finite laws. The primary schemas are ax-1 A→(B→A), ax-2
(A→(B→D))→((A→B)→(A→D)), ax-3 (¬A→¬B)→(B→A), and MP.
The live-page evidence and its lack of a pinned recursively checked set.mm
revision are as in L056. Step 248 inspected conjunction associativity
[anass, Whitehead–Russell *4.32 p.118](https://us.metamath.org/mpeuni/anass.html),
[bitrd](https://us.metamath.org/mpeuni/bitrd.html) and
[mtbi](https://us.metamath.org/mpeuni/mtbi.html), including their displayed
proofs. These justify the bounded logical comparison, not native inference
labels. All new native laws used here have primitive realizations in §2.

Injective renaming preserves (1): extending a map of distinct free generators
to words maps a formal polynomial identity to the same identity, and an
inverse on the image preserves distinctions. Native simultaneous substitution
also preserves each primitive inference by L056's record induction. Placeholder
roles are eliminated by arithmetic substitution before propositional reception;
they are never identified with an original variable sharing the payload text.
Thus the encoded dictionaries, common q and both source translations agree
literally at every receiving endpoint. Repeated variable occurrences are not
made distinct letters. No freshness of q is used.

Construct the actual copied trees f0=C(x,0), f1=C(x,A)+1, retaining the
written right-hand +1 branch. Their node counts U_i satisfy s≤U_i≤11s+2
and their depths d_i≤a log₂(s+2)+5. Since
bit_length(U_i+1)≥log₂(U_i+2) for integer U_i≥1, the single fixed admission
a*=a+5 suffices for both L068 calls. This is not an instance-chosen exponent.
The full distinct original dictionary, including unused letters in either
source, is the same in both calls. Their zero identities follow from (1).

L068 therefore constructs exact complete proofs with endpoints

    E(B,Z),             E(X(D,Y),Z),
    B=Eval(C(x,0)),     D=Eval(C(x,A)).                         (2)

Do not simplify either source before reception. All local/coordinate/chain
prefixes and source-row provenance promised by L068 are retained inside each
package. Optional occurrences may be supplied to both calls; their resulting
repetitions are charged, not deduplicated. There is no appeal to an executed
nonempty-letter fixture to establish this abstract theorem application.

### 2. New fixed primitive laws and paid copies

The following six endpoints use schematic arguments A,B,C,G and the same q:

    E(P(P(A,B),C),P(A,P(B,C)))                              associativity
    (G→E(A,B))→((G→E(B,C))→(G→E(A,C)))                     guarded transitivity
    E(A,Z)→¬A                                               zero reception
    E(X(A,Y),Z)→A                                           plus-one reception
    A→((G→E(A,B))→(¬B→¬G))                                final reception
    (G→Z)→¬G                                               empty-clause reception. (3)

These are fixed tautologies: P is conjunction, E equality of truth values,
X exclusive-or, Y true and Z false. In the final law, A true and the guarded
equivalence force B whenever G; ¬B consequently excludes G. These semantic
explanations select finite templates, not inference rules for instances.

`python3 scripts/two-identity/build_fixed.py` synthesizes (3) in the existing
primitive emitter and checks every serialized record with the independent
L056 checker, against separately reconstructed literal endpoints. All
formula and substitution fields and every reference are checked, and every
native/image record pair is compared. The full certificate is
`scripts/two-identity/output/certificate-249.json`; complete streams are its
six `fixed-<name>.<native|not-or>.jsonl.gz` pairs. There are no failures.
Line counts in display order are 1542,2033,641,799,871,548 in each format.
Over every complete fixed record, the required common bounds are

    L=2033;   (D_native,S_native)=(18,1104);
              (D_image,S_image)=(25,1490).                  (4)

D bounds formula/declaration depth and S their combined nodes per record.
The byte totals for each full stream, hashes and endpoint strings are in the
certificate. These bounds are on the checked selected fixed proof streams,
not every temporary helper generated while searching for a finite proof.

For every later copy, substitute simultaneously into all declared fields,
reconstruct its axiom instance, relocate each internal MP reference to its
earlier copied record and compare the reconstructed conclusion with the
substituted original. Keep all records of that fixed stream, unused ones
included. This is L056's primitive substitution induction. In particular it
allows coincident actual A/B/C/G/q names: substitution does not recurse into
replacement terms. Add only the explicitly stated external MPs below. Fixed
library names never become implicit extension variables.

### 3. Guards for the exact bounded source syntax

Assume F has at least one clause and none is empty. Form A^match by retaining
each ordered factor and choosing its product bracketing to match the actual
clause OR tree. Boolean and commutator trees do not change. Generate every
L060 proof Φ→E(Eval(A^match_j),Z), retaining every equal-position output.
This is a derived auxiliary guard package, not a modification of input A.

For width one/two the source tree already agrees. For width three, there are
exactly two ordered full binary shapes on its three occurrence factors.
If source and matched trees differ, substitute those exact factor evaluations
into associativity in (3). The left-to-right orientation is that line itself;
for right-to-left copy L056's E(U,V)→E(V,U) string and append one MP.
The factors may be X(Y,x) or x and may repeat; no ordering or cancellation
step occurs. This gives exactly E(U,V), with
U=Eval(A^match_j) and V=Eval(A_j). Each factor occupies its original slot.

Copy L061's checked fixed law

    (G→E(A,D0))→(E(A,B0)→(G→E(B0,D0)))                    (5)

with G=Φ,A=U,B0=V,D0=Z; two MPs, first the imported guard then the bridge,
end at Φ→E(Eval(A_j),Z). L061's whole expanded-word receiver is not
invoked. Only its literal four-argument law (5) is used, so no expanded-word
or same-polynomial normalizer premise enters. For matching trees simply use
the entire L060 guard. Every axiom position consequently has an exact source
guard. The fixed input clause trees, orders and dictionaries remain unchanged.

### 4. Replacement through the original C and final reception

List the r≤s placeholder leaf occurrences of the original tree C in written
preorder. Let T_i be its direct evaluation with the first i occurrences
replaced by Z and every other placeholder replaced by its actual Eval(A_j).
Original variables/constants and every X/P node retain their positions.
Thus T_0=D and T_r=B, literally; a repeated placeholder has separate visits.

For visit i, mark that one original leaf in the full original C skeleton,
use U=Eval(A_j), V=Z, and place the current bounded terms in every other
leaf. Import the complete exact guard from §3. L059 gives an entire proof

    Φ→E(T_(i-1),T_i).                                    (6)

The skeleton is the original tree, of height h; for s≥1,
log₂(s+2)≤2 ceil(log₂(s+1)), so its fixed admission 2a suffices. Deep Φ
is a separate parameter, never a term newly inserted inside X/P. No previous
guarded equivalence is substituted for a skeleton term. This verifies the
literal L059 receiving hypothesis and its logarithmic skeleton condition.

Start a fresh append-only final store. Copy both complete proof outputs in
(2), then all exact source-guard proofs from §3, including unused axiom
positions. A visit's separately exported proof still retains its own whole
guard occurrence; these are additional paid copies. Copy L056 reflexivity on D, then ax-1
E(D,D)→(Φ→E(D,D)) and one MP. For each visit copy all records of its
independently constructed (6), then the guarded transitivity string in (3)
with A=D,B=T_(i-1),C=T_i,G=Φ. Two MPs use the earlier cumulative root
and the just imported visit root. The new cumulative endpoint is
Φ→E(D,T_i). Crucially, the cumulative proof is not the supplied input to
the next L059 call, and is not recopied at every level. Its earlier line
number is used. For r=0, initial reflexivity already has the required endpoint.

At the end this store contains the exact records

    E(B,Z),        E(X(D,Y),Z),        Φ→E(D,B).            (7)

Copy zero reception with A=B and apply MP to the first record, obtaining
¬B. Copy plus-one reception with A=D and apply MP to the second record,
obtaining D. Finally copy final reception with A=D,B=B,G=Φ and apply
three MPs in order to D, Φ→E(D,B), ¬B. The actual last record is ¬Φ.
Every premise is an exact earlier record; E(X(D,Y),Z) has not been replaced
by an externally supplied D or a semantically equivalent source formula.

Keep all exported component streams and their headers as artifacts. Copy
every mathematical record into the final store as specified; its own header
states ¬Φ. Source headers and occurrence mappings remain in the manifest,
not as invented proof rules. Export τ by translating every formula and
declared substitution, keeping all tags and relocated references. Induction
on records gives precisely the literal translated proof of τ(¬Φ).

### 5. Exceptional inputs

If an empty clause occurs, its exact evaluation is Z. Copy/validate optional
proof occurrences into a fresh store and retain the original F/C/A inputs.
Use L060's checked identity, left/right conjunction projections and implication
composition templates down the actual conjunction path to this occurrence.
Their general arguments do not require nonempty clause syntax: start at
Φ→Φ, and at each child H of P(U,V) use its projection and two MPs with
composition to derive Φ→H. The last endpoint is Φ→Z, including a
zero-length path if F consists of that clause alone. Copy empty-clause
reception in (3) and one MP to obtain ¬Φ. This branch needs neither L060's
whole-list theorem on empty clauses nor a zero proof. All optional records
and intermediate path records survive. Its costs are covered below.

If there are no clauses, the occurring-variable dictionary is empty. Then
A is empty and the two substitutions in (1) coincide, making (1)
impossible over F₂. Even with an enlarged alphabet, evaluation at a Boolean
assignment kills every Boolean/commutator axiom and gives the same
contradiction. This is an exclusion of invalid promises, not a Frege
inference or a SAT test. If there are no original variables but at least one
clause, each legal clause must be empty, so the direct branch applies. q
supplies constants with no freshness or original-variable existence premise.

### 6. One original-input complete-record ledger

Here is a coarse polynomial bound with no measured intermediate free variable.
Constants below depend only on fixed a, encodings and fixed libraries. Enlarge
one constant c as needed throughout, with Q≥2. Charge both formats. Source
reconstruction, consistent name encoding and the input manifests cost at most
cQ², including complete inverse payloads and every optional occurrence.
Each of the two L068 input packages has at most cQ² bytes. Fix a monotone
polynomial p_68(t) dominating L068 §3 equation (11) and its record counts
at admission a+5, for input size at most t.
Such a polynomial is supplied by that section's finite original-input
majorant, not inferred from finite executions. Both complete output bundles
together cost at most 2p_68(cQ²).

All L060 guards from their cQ²-size derived package cost at most cQ⁸ by
its Q⁴ whole-list bound. Each bounded bracketing bridge and (5) copy has
only bounded axiom terms and one Φ argument. At most Q axiom positions
and their full guard copies add at most cQ⁸ after enlarging c. Every original
name payload has length at most cQ and every guard subtree at most cQ²
bytes; arbitrary guard depth causes no exponential term. Fixed libraries
and their checked maximum constants are included in c.

For every intermediate T_i, the original skeleton has depth h and bounded
axiom terms at its leaves. For either format its node recurrence is bounded
by v_(k+1)≤8+4v_k, starting at one fixed constant depending on the bounded
axiom syntax. Thus nodes≤c4^h≤c(s+2)^(2a) and complete formula bytes
≤cQ^(2a+3). Φ's direct P/OR expansion has linear node count in the CNF
syntax, regardless of its depth, and at most cQ² bytes. Therefore every
complete L059 visit input, including its exact entire guard prefix, literal
term trees, skeleton, names and paths, is bounded by

    I(Q)=cQ^(2a+10).

For admission 2a, fix the monotone bound ell(t)=c t^(4a+3) from L059's
full-input polynomial estimate, enlarged to include both formats, headers
and record counts. The r≤Q separate visit bundles cost
at most Q ell(I(Q)). This is a sum of independent calls on source-bounded
inputs, not Q iterated compositions of ell.

There are O(Q+1) additional fixed-copy/MP blocks in §4 or the exceptional
projection branch. Their arguments are Φ, T_i, B,D,Y,Z or bounded products
of these, never whole earlier proofs. With (4), every block's copied formula
and declared substitution bytes total at most cQ^(2a+3). A bound
cQ^(2a+6) pays all such blocks, their endpoint headers and initial references.
Let

    R(Q)=cQ² + 2p_68(cQ²) + cQ⁸
                  + Q ell(cQ^(2a+10)) + cQ^(2a+6) + c.    (8)

This is one fixed polynomial in original Q. In particular no optional-proof
depth, actual coefficient-table size, generated guard size or measured proof
length is an independent parameter in (8). Arbitrarily deep optional native
proofs are retained as strings; literal translation increases node count by
at most a fixed factor and does not expand depth exponentially.

Before final relocation, the sum of complete generated streams, their
record counts and the mathematical records that will be copied into the
final store is ≤cR. A copy of a component's already-contained nested
occurrences remains a copy of its whole complete stream; we do not flatten
it by fetching an uncounted external ancestor. Final references have
O(log(R+2)) bits. At most cR records, with at most two references each,
are changed; formulas and declaration fields are unchanged. Thus the final
native and image proofs and their copies cost O(R log(R+2)) bits on top
of the retained component bundles. Allow one occurrence-map entry per
copied record, source endpoint, optional input and package header, and store
source/destination offsets, original paths and dictionary positions explicitly.
There are O(R) entries, each at most O(R) bytes even with the original path
copied rather than referenced. Fixed output paths have length O(Q+log(R+2)).
One final bound K R(Q)^3 consequently dominates all specified uncompressed
artifact bits and metadata. Arbitrary extra diagnostics are not part of the
output contract. For time, each component has a fixed polynomial construction/
checking bound in its full explicit input by its cited contract. There are
two zero calls on inputs ≤cQ², polynomially many guard calls on inputs ≤cQ²,
and ≤Q context calls on inputs ≤I(Q). None receives the cumulative final
proof as input. The sum of these fixed polynomial time bounds is polynomial
in Q. Remaining explicit-stack parsing, substitution, relocation, serialization
and literal checking take polynomial time in Q+R(Q). Choose one polynomial
dominating this sum and K R(Q)^3 to obtain the joint conclusion; no particular
cubic checking-time exponent is asserted. This does not assert a wall-clock
or memory bound for the current recursive Python prototypes.

### 7. Original evidence and review test (step 249)

The original-input threshold is polynomial rather than formula-only. The new
fixed-law checks are complete; no preview or hash alone establishes them.
Only the six fixed pairs were executed in this step. The all-size composition
uses the exact component contracts and the copy/reference schedule above.
In particular this is not a claimed full primitive stream for a general
nonempty-letter certificate, a generic wrapper test, or an audit of the new
assembly. Independent review must check the actual source/bracketing matches,
both source admissions, every final MP and the retention/ledger schedule.

The continuation test passes provisionally at this abstract level: bounded
source bridges are paid, the guard stays separate, and (8) has no generated
size as a free input. An alias, wrong endpoint, required unbounded source
normalization, repeated import of an accumulated proof or unpaid artifact
would invalidate the corresponding claim and must be isolated rather than
hidden by the polynomial notation. Attempts 018 and 022–024 remain intact.
This reproduces known logical operations with local record/accounting progress;
no originality or unrestricted complexity separation is asserted.

### 8. Independent critical audit, 2026-10-16 (step 251)

**Scope and verdict.** The unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-16-two-identity-receiver-critical-audit.md`
authorizes this REPRODUCTION audit. The precise primary inputs in §1 and
their recorded inspected cases are reused; no new external theorem or
source reproof is needed. L048 contributes definitions only. L054 supplies
actual bounded source syntax, L056 primitive copying, L059 context lifting,
L060 exact guards, L061 its fixed four-argument law, and audited L068 the
abstract zero packages. None of L048's existential assertions or L055's
whole-receiver conclusion is assumed. No substantive defect was found;
the construction, displayed bounds and direct mathematical inputs are unchanged.
This verdict is informal all-size verification, not general program execution.

**Both source admissions and names.** A substituted axiom has at most 11
nodes and height at most four. Zero substitution preserves each original
leaf position; axiom substitution never decreases the original tree's node
count. Appending the actual +1 increases size by two and height by one.
Thus s≤U_i≤11s+2 and d_i≤a log₂(s+2)+5 as claimed. For U_i≥s≥1,
log₂(s+2)≤log₂(U_i+2)≤bit_length(U_i+1), and bit_length(U_i+1)≥1.
It follows that d_i≤(a+5)bit_length(U_i+1) for both calls. The single
admission constant is fixed before input, not adjusted after seeing a proof.
The two formal identities give zero for exactly these sources; characteristic
two is used for C(x,A)+1. No Boolean-only vanishing is substituted for this.

The original dictionary is distinct even when a letter is unused in a source.
Two hex digits per byte, with a common prefix, preserve byte lexicographic
order: the first differing byte has the same order in its two hex digits,
and a proper byte prefix remains a proper string prefix. Consistently encode
the entire received propositional-name set when encoding is needed, including
q and optional auxiliary names, rather than encoding only some colliding
payloads. Placeholder position roles remain separate and disappear before
propositional evaluation. Repeated occurrences of an original remain one
free generator. Simultaneous library substitution does not recurse into its
arguments, so q/original/schematic collisions require no freshness premise.
The same q, ordered dictionary and direct Eval therefore give precisely (2).

**Guards, visits and the final literal references.** On three ordered factors
there are only the two binary product trees in (3). If the matched source is
left-associated, associativity gives E(U,V); if it is right-associated, the
same instance gives E(V,U) and the copied symmetry string with one MP gives
E(U,V). The factors retain their slots even when their names coincide. Law
(5) with (G,A,B0,D0)=(Φ,U,V,Z), followed by the exact guard and bridge MPs,
gives Φ→E(V,Z). Other positions use their whole matching guard. This invokes
neither the expanded-word receiver nor arbitrary same-polynomial rewriting.

At visit i, the marked leaf has arguments Eval(A_j),Z. All other leaves
contain the current direct source terms, so L059's reconstructed endpoints
are literally T_(i−1),T_i. Its skeleton is still the original C. The inequality
h≤a log₂(s+2)≤2a ceil(log₂(s+1)) gives the fixed admission 2a, including
the one-leaf identity context. Φ is a separate parameter, and the entire
source guard is a paid input occurrence. The cumulative proof is not an
input to any visit. Reflexivity and ax-1 start Φ→E(D,D); each transitivity
copy and its two MPs use the earlier cumulative root and the current visit
root to produce Φ→E(D,T_i). The r=0 case needs no visit or special inference.

After all imports, select the transported last roots of the actual two L068
outputs, not equal-formula substitutes. Zero reception gives ¬B and plus-one
reception gives D. The copied final law gives successively
(Φ→E(D,B))→(¬B→¬Φ), then ¬B→¬Φ, then ¬Φ, using D, the cumulative root,
and ¬B in that order. Every antecedent exists earlier. Translation preserves
these same references, all declared substitutions and the exact endpoint.

**Exceptional branches.** With an empty clause, the actual conjunction path
ends at Z. The general identity/projection/composition strings remain valid
with Z as a child argument; the nonempty-clause L060 theorem is not invoked
on that clause. A path of length zero starts at Z→Z and still feeds the
empty-clause reception law. Optional proofs are validated and retained but
provide no hypotheses. With no clauses the occurring-original dictionary
and A are empty, so the two certificate substitutions coincide and cannot
have values 0 and 1. With no variables and a clause, that clause is empty.
These cases are respectively inconsistent promises and the direct branch,
not an unsound acceptance of satisfiable input.

**Original-input ledger and nested retention.** Encoding, tree substitution
and the two complete source envelopes cost at most cQ²; an occurrence can
repeat a paid original name but creates no unpaid name payload. L068 (11)
at fixed a+5 supplies a monotone polynomial majorant p_68 for the entire
two-format bundle and its counts. This includes all internal local/coordinate
prefixes, chain/bridge exports, optional occurrences and their manifests.
Copying each final zero stream adds at most a constant multiple of its paid
bundle. It does not require fetching further uncounted ancestors.

L060's whole-list fourth-power bound applied to cQ² gives cQ⁸. Retaining
those guards and each bridged guard separately multiplies this by at most
a fixed constant; each position has at most one bounded bridge and one (5)
copy. The node recurrence in §6 uses bounded axiom leaf terms in both
formats, so all T_i have at most c4^h nodes and cQ^(2a+3) bytes. The
direct Φ uses each CNF child once under P/OR. Its arbitrary depth is never
exponentiated. Each complete visit input consists of its skeleton/terms,
endpoint, one complete guard prefix and finite framing; all fit I(Q).
L059's exponent 2b+3 with admission b=2a gives ell(t)=ct^(4a+3).
Consequently ≤Q independent visit bundles cost Q ell(I(Q)); no iteration
of this polynomial on its own output occurs.

The fixed-copy/MP blocks have source-bounded formula arguments, not proof
arguments, so cQ^(2a+6) covers their total written fields before relocation.
R(Q) therefore pays all complete component exports and every record copied
to the final store up to a fixed multiplier. Repeated guard positions and
optional/nested occurrences are counted each time, including records unused
in the final inference ancestry. There are O(R) references/occurrence entries;
each relocated reference takes O(log(R+2)) bits. Even copying full source
paths and endpoints in the manifest costs at most O(R²), since each entry
fits O(R) bytes. Thus KR³ dominates the specified artifacts as asserted.
Component times are a sum of fixed polynomials on source-bounded inputs;
the final serialization/checking costs polynomial time in Q+R. This proves
the joint polynomial threshold, with no promise of practical output size.

**Complete fixed evidence and limits.** Run
`python3 scripts/two-identity/audit_fixed.py`. It imports only the independent
primitive checker, reconstructs the six endpoints without the emitter, checks
all twelve complete archives, rejects duplicate JSON fields, checks the ASCII
formula payloads, and compares every translated header, formula, substitution
and reference through simultaneous EOF. The full evidence is
`scripts/two-identity/output/audit-251.json`. There are 6434 records in each
format, with per-law counts 1542,2033,641,799,871,548. Maximum line count is
2033; native depth/record nodes are 18/1104 and image values 25/1490, exactly
the required common bounds (4). The certificate is complete with no failures.
No previous archive was regenerated or modified. These finite checks support
the fixed-library applications; the preceding induction and inequalities
establish the abstract all-size verdict, not the finite test count.

The generic implementation and a nonempty-letter joined execution remain
unverified. Arbitrary equivalent source trees, independent ordinary-input
completeness, certificate existence, arbitrary ER representation, W/V/U and
unrestricted SAT remain outside the conclusion. This audit is local verification
of reproduced machinery, not a new result beyond the checked sources.

## Mathlib

Full matching coverage for this complete-record two-identity receiver and its
polynomial ledger is **not checked**. The cited LTW and Metamath results
support the logical pattern and finite laws with their stated qualifications;
they do not establish matching Mathlib coverage. The primitive Python checks
are not Lean verification or proof of arbitrary ordinary-input completeness.
