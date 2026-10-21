# Normal-closure repair — dyadic different transfer assessment

TARGET: Prove or refute d_2((C_o)_w)<=d_2(T_v)+10+1/e(T_v/Q_2) for every L089 survivor, all six orderings and actual v above two and w above v, where C_o=G_o^nor and d_2 is the absolute different exponent normalized by v_2(2)=1.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step373 reused step364/368's searches and primary readings, searched the scoped normal-closure records for different claims and failures, inspected L090/L092/L093's relevant statements and tower passages, and compared the exact target with the primary theorem below. No novelty inference or repeated authentication search.
SOURCE_EVIDENCE: Fresh targeted reading of April 2020 IV Propositions 1.1–1.3 notation, 1.3(ii) and its entire proof, printed pp.9–12, plus Theorem 1.10(ii), p.24, at https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf ; Milne ANT v3.08 8.10 with proof p.139 and 8.13 with proof p.141, https://www.jmilne.org/math/CourseNotes/ANT.pdf ; Milne FT v5.10 3.17 with proof pp.39–40, https://www.jmilne.org/math/CourseNotes/FT.pdf .
COMPARISON: The primary different bound has exactly the proposed absolute normalization; its intermediate field may equal its base. Standard Galois/completion coverage applies to L090's actual normal closure containing T, and L093 supplies the required degree input. Only the stated same-field specialization remains; no new local ramification theorem is needed.
GAP: The mathematical application has not been executed or saved as a canonical lemma; this literature-only step approves its exact hypotheses and method, not a proved bound or complete repair.
REASON: Essential coverage is now complete for the saved target, so the next step defaults to its bounded mathematical specialization rather than additional literature or authentication.
SCOPE: Ready only for the exact TARGET, all original quantifiers and qualifications retained. Cite the known bounds and completion theorems; check their applicability and substitute L093, without reproving them, sharpening constants, changing models or treating other primes.
LITERATURE_REASON: The invariant changes from degree to absolute different, requiring an exact comparison of Proposition 1.3(ii)'s Galois/tame-intermediate hypotheses and its base-field normalization with the actual C_o,T completion tower.

## Completed comparison — step373

The main gap remains original finite B>=A. The selected intermediate
target is the exact TARGET above. Its downstream use is one dyadic
contribution to a possible normal-closure repair; even success leaves
the global relative excess and exact-generation obligations unresolved.

### Primary theorem and normalization

[Mochizuki, IUT IV, April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
Proposition 1.3(ii), pp.11–12, uses finite local fields k_0 subset
k_1 subset k_i, with k_i/k_1 Galois and k_1/k_0 tame. It bounds
d_i by d_0+n_i+1/e_0, where n_i=v_p([k_i:k_0]); d_i,d_0 are
absolute different orders with ord(p)=1. The notation comes from
Propositions 1.1–1.2, pp.9–10. There is no proper-intermediate
requirement. Read the full proof: unramified reduction, zero-exponent
case, p-group induction and degree-p Kummer estimate with arbitrary
positive error. This is cited coverage, not a reproof. Theorem
1.10(ii), p.24, uses this estimate at 2,3,5. This reading does not
authenticate the reproduction against author/journal bytes.

### Applicability ledger for the later specialization

- Retain the actual tower T subset C_o subset M already proved in
  L090 and used in audited L093, with actual extending places v,w.
  C_o is the finite normal closure over Q, in characteristic zero.
- Use [Milne, FT v5.10](https://www.jmilne.org/math/CourseNotes/FT.pdf),
  Theorem 3.17 and its proof, pp.39–40: a finite Galois extension is
  Galois over an intermediate field. This covers C_o/T, without
  asserting that the literal nonnormal G_o is Galois.
- Use [Milne, ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Proposition 8.10 and proof, p.139: the completion of a finite
  Galois number-field extension at extending places is Galois,
  with its actual decomposition group. Proposition 8.13 and proof,
  p.141, retain the compatible tower. No equality between different
  completions or cancellation of a global core is required.
- The approved substitution is p=2, k_i=(C_o)_w and
  k_0=k_1=T_v. The intermediate extension is the identity, so its
  ramification index is one and it is tame, independently of
  whether T_v/Q_2 is wild. All fields are finite extensions of Q_2.
- The absolute different in the target is the source's invariant;
  it is neither the relative different of (C_o)_w/T_v nor its
  integer uniformizer exponent. L093's bound concerns the integer
  degree valuation n_i; this must remain distinct from field
  element valuations. Its audited upper allowance is ten.

This is a theorem-level applicability comparison only. The next
research turn must write the actual cited application and all-place
quantifiers in a canonical lemma. It should not compute a different
from scratch or claim a sharp value. Classification: REPRODUCTION
for that future SPECIALIZE application, with no originality claim.

### Duplicates, test and remaining limits

Reuse the exact searches and known-result comparison in the ready
local-degree scope and normal-closure-repair scope. The scoped search
found L092's explicit different limitation and L093's degree-only
conclusion, rather than an existing proof of this target.
ATTEMPTS/034's cyclic separator and /035's authentication stop are
not tests of this invariant and remain preserved. No further access
campaign or broad classification search is needed.

Continue with the exact cited specialization if these actual field
and normalization identifications survive the written application;
stop that application on a precise failed hypothesis. An insufficient
estimate would not be a refutation: that requires a larger proved
different for an actual survivor/place. A passing sufficient bound
would close only this target. Other primes, global relative degree,
exact prescription/repairs, height-selected prime, independent initial
data, native input/action/factorization/pilot and essentiality remain
open, as do April-version authentication and the def= qualification.
Full matching and supporting Mathlib coverage is unchecked.

No lemma, mathematical script, PROOF.md or DAG.md is changed in
this literature turn. Mathematical exploration usage remains zero.

## Invocation-start proposal — historical

The following was REVIEW_REQUIRED at invocation start; the completed
assessment above supersedes its pending-review language.

## Essential inputs and proposed test

Retain audited L089,L090,L092,L093, one unchanged original survivor,
fixed c,h,d_*,e_*, both domains, the fixed closure and all six
full-coordinate fields. Here T=F_tpd=Q(E[2]), C_o=G_o^nor is the
normal closure over Q, and M=Q(E[60]) is the existing ambient field.
Use every actual extending pair of places v,w. Keep d=6 and
epsilon_d=1 in the qualified source comparison. Do not assume that
the source's ell-division field is T or substitute prime seven.

For a finite local field K/Q_2, the proposed notation is
d_2(K)=v_2(D_(K/Q_2)), where D is the different ideal and the
valuation is normalized by v_2(2)=1, rather than by a uniformizer
of K. This fixes the target's meaning; no different formula is
derived here. The review must match this definition to the primary
statement before approving a substitution.

The main gap remains original finite B>=A. This distinct intermediate
target would test one local contribution in the claimed
different/conductor control after normal closure. Global relative
degree excess, exact generation and other places remain independent
even if it passes.

Continue only if the inspected primary theorem, with every
Galois/tame-intermediate hypothesis and normalized base identified,
covers the proposed inequality. If its actual hypotheses or
normalization do not match, record that precise obstruction and
review a corrected target separately. Failure of an upper estimate
is not a counterexample; refutation would need an actual survivor
and extending place with a proved larger different.

## Recovery comparison and route selection

Three mechanisms were compared without executing a second attempt:

- Sharpening the same dyadic degree bound: not selected. Audited L093
  already reaches the sufficient allowance ten; sharper degree alone
  does not supply the missing different or generation conditions.
- Transferring the actual local degree to a normalized different:
  selected. It changes the invariant and tests separate local tower
  hypotheses, using L093 as an input rather than repeating its audit.
- Repairing exact generation by changing the chosen model or field:
  deferred. L090–L092 test literal fields and their closures, not
  every alternative; a precise changed-model target and its own
  theorem comparison would be needed.

ATTEMPTS/034's recorded cyclic Frobenius powers cannot settle this
different question. ATTEMPTS/035's authentication and repeated
approval mechanism remains parked. No source retry, model change,
new lemma or calculation is undertaken in this proposal.

Remaining qualifications: April IV reproduction authentication and
current-version status, the def= boundary, other primes, complete
different estimates, exact prescription and possible repairs,
height-selected prime, independent initial data, native
input/action/factorization/pilot, essentiality and original finite
B>=A. Full matching and supporting Mathlib coverage is unchecked.
The next comparison must not treat a passing local different bound
as resolving these separate gaps.
