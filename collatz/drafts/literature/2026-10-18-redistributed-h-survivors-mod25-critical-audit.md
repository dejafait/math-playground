# Proposed audit of the two changed-table arithmetic certificates

TARGET: Critically audit L080's two-survivor modulo-25 nonintegrality proof and complete certificates for the redistributed-H table.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 306 exact-mechanism searches and primary-source comparison; read complete L080, L078 definitions and step 297 audit, L079 hypotheses/conclusion, the prior L078 audit assessment, and Attempts 027/028/030/031; scoped L080 duplicate search found only its calculation and proposed audit.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 pp. 228–229 and printed induction cases, plus pinned PadicVal.Basic statements/proofs as recorded in 2026-10-18-redistributed-h-survivor-mod25.md; no changed theorem hypotheses require fresh retrieval.
COMPARISON: L080 uses the already assessed nonempty formal word, positive integer denominator, audited unshifted row-0 identity and prime-five cancellation; changed-table finite evidence and power/composition implementation still require independent audit, not a new general theorem.
GAP: Source scope is ready; independent verification of all 50 row evaluations, both complete compositions, denominator powers, nonzero premises and coordinate matching remains. No audit verdict or downstream assembly is supplied.
REASON: This separate literature comparison approves exactly the saved audit as RESEARCH/REPRODUCTION using ready coverage; no general theorem reproof, new factor or feasibility search is needed.

The original proposal below is preserved; its pending scope-comparison wording is superseded by the completed review appended below.

The main gap remains universal eventual descent. The intermediate target
is exactly TARGET. Its downstream use would be to validate both finite
nondivisibility certificates before any separately scoped assembly with
L078. No full-table exclusion or actual-word consequence is part of the
audit. The completed step reports REPRODUCTION, not a new general theorem.

Essential inputs are L055's explicit table, audited L079's changed data
and positive Lambda, audited L078's complete formula and unshifted row-0
identity, and L080's proof with
`scripts/postspell-word-count/test_redistributed_h_survivors_mod25.py`
and `scripts/postspell-word-count/redistributed-h-survivors-mod25-certificate.json`.
Only H_0=39 and H_24=32670622 change; r=25, B=9250245, tau=2.
Retain t=0,1 only, b_23=t, b_24=B-t and earlier entries zero,
with a_i=2+18b_i including the closing edge. Reported residues are
Phi(0)=16, Phi(1)=7, Delta=5 modulo 25; they are audit subjects,
not independently verified inputs for the proposed audit.

Compare ready source coverage first. Then a separately approved audit
must independently check all 50 contributions, prefix/suffix exponents,
both denominator powers and complete composition states, positive/nonzero
premises, the power algorithm and exact coordinate n=s-23/11.
No feasibility, new prime/modulus, parameter search or table assembly is
authorized by this proposal. A mismatch or unsupported premise requires
repair or an unresolved verdict within this scope. Continue only when
the independent checks validate both certificates; otherwise stop the
dependent assembly. Survivor feasibility and all universal gaps remain
unresolved. Attempts 026–031 and both original witnesses are preserved.


## Step 308 completed source-scope comparison — 2026-10-18

SCOPE: Exactly TARGET; L079 changed-H table, r=25, B=9250245, tau=2, normalized literal allocations t=0,1 and modulus 25 only.
LITERATURE_REASON: The newly proposed critical audit is REVIEW_REQUIRED; its exact obligations need comparison with ready coverage before a separate mathematical audit. No additional external discovery is necessary.

The main gap is universal eventual descent. The intermediate target is
independent verification of L080's two finite nonintegrality certificates.
Its plausible downstream use is to discharge L078's survivor arithmetic
premise for this one changed table. That assembly and its actual-word
application remain outside this audit; survivor feasibility and all
universal gaps remain unresolved.

### Reused primary coverage and applicability

Reuse the completed step 306 assessment
`2026-10-18-redistributed-h-survivor-mod25.md`, including its recorded
searches and inspected primary statements and essential proof cases.
The precise affine import is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
That review read the chronological convention, concatenation formula,
fixed point, length-one and appended-zero induction cases, and the
printed assertion that appended one is analogous. Only formal affine
composition for a nonempty word and its fixed point with nonzero
denominator are imported. No integer-itinerary converse, rational
parity converse, rotation-gcd theorem or empty-word claim is required.
No external passage was newly retrieved in this turn.

L080's displayed word is the same chronological shortcut word; later
maps act on the left. The exact table changes only H_0 and H_24, as in
L079. L078's already audited formulas cover arbitrary permitted table
entries and all test allocations, without requiring feasible guards.
Read its full definitions and step 297 audit: the positive integral
row offsets, every earlier-denominator/later-odd weight, positive Lambda
and the normalized unshifted identity are established there. Read L079's
hypotheses/conclusion, including its recorded audit verdict; it supplies
the changed data and only the necessary survivor set. Source coverage
therefore extends to this verification task without a changed theorem
hypothesis. Verifying that L080 faithfully uses those inputs remains
part of the next audit; this review does not independently certify its
reported residues or traces.

The supporting valuation source remains
[Mathlib PadicVal.Basic](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean)
at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953,
`padicValInt_dvd_iff`, `padicValRat.defn` and
`Rat.num_or_den_zero_padicVal`. Step 306 inspected their statements
and complete proofs. Their prime and nonzero qualifications match the
intended application at 5 with positive integer numerator/denominator;
the next audit must check those premises before interpreting evidence.
Full matching Mathlib coverage for this particular changed table is
unchecked; these are supporting declarations, not formal verification
of the certificate. No reproof or Lean build is needed.

### Duplication, failures and audit boundary

A scoped search for L080 and its certificate name found the existing
calculation and this proposed audit, with no completed independent
L080 audit. Read complete L080 and the ready arithmetic comparison.
L056/L066 are different literal-table inputs and cannot supply the new
numerator residues. Attempts 027/028/030 record common-zero and exact
prime-cancellation stops for different fixed orders; Attempt 031 rejects
one such order's real guards. Those failures are preserved and do not
block a critical verification of these changed-table certificates.
No novelty follows from the absence of an exact duplicate. Unread broader
leads are unused; no essential source blocker remains.

SPECIALIZE now covers a separate RESEARCH/REPRODUCTION proof_audit of
exactly TARGET. Essential input IDs are L055's underlying explicit table,
audited L079's replacements and positive Lambda, audited L078's complete
integer pair and coordinate, and L080 as the subject of verification.
Use the two script/certificate paths named in the original proposal.
Independent implementation checks are justified because the changed
finite data are not provided by the general source theorem. Reproving
that theorem or expanding the parameter/modulus range is unnecessary.

The discriminating test is full agreement of independently recomputed
50 row offsets/weights/triples, both chronological composition traces,
both denominator powers and the claimed normalized unshifted coordinate.
Check complete evidence rather than previews, both actual tails including
closure, all raw exponent totals, the repeated-power algorithm, the unit
use of 11, absence of division by Delta, and nonzero premises. Reported
residues 16/7/5 are audit subjects, not newly verified facts here. Continue
to rely on both certificates only if these checks and the cited valuation
interpretation succeed. Any mismatch or unsupported premise requires
repair or an unresolved verdict within this scope and stops dependent
assembly. No new factor, modulus, allocation, feasibility or actual-word
consequence is authorized. Both rational witnesses remain valid.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. The new work is
exact audit-scope comparison, not a mathematical advance or no-defect
verdict. No lemma, mathematical script, certificate, DAG or argument
overview is changed. Mathematical exploration usage remains zero.
