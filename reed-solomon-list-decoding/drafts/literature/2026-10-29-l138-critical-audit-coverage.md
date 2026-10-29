# L138 conditional cyclic-module specialization — completed audit coverage

TARGET: Critically audit L138's one-translation-inclusion equivalence over E and F, including cyclic factor degrees and the use of full-sheet directional constancies.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed directional-Fourier and coefficient-closure assessments; searched L138, drafts/audits and history/547–549 for prior audits and read ATTEMPTS/113 and the closure working record. L138 explicitly lacks a separate audit; L133's repeat audit is a recorded duplicate. No fresh internet search or claim of novelty.
SOURCE_EVIDENCE: Read the retained journal text of Evra–Kowalski–Lubotzky, Good cyclic codes and the uncertainty principle, L'Enseignement Mathematique 63 (2017), 305–332, Proposition 2.6(1),(3) and their complete proof, pp. 309–310, https://ems.press/content/serial-article-files/44351 ; local primary text drafts/sources/directional-fourier/evra-kowalski-lubotzky-2017.txt, lines 180–236, and the prime-power clarification immediately following the proof.
COMPARISON: The source supplies separability, CRT and nontrivial factor degree ord_p(|K|) for either finite coefficient field, including a nonprime field. It describes the quotient ring and its ideals; applying its factors to an invariant function space and using full-sheet constancies are the local specialization to audit, not assertions imported verbatim.
GAP: Essential source coverage is ready. The independent audit must still check both numerical orders, the actual restricted translation operator, the containing-1 dimension claim and all-label propagation. No translation inclusion, full-sheet rigidity, retention bound or RS transfer is established by this review.
REASON: Approve only the saved conditional audit as a reproduction/specialization of the ready module input plus the existing local argument; do not reopen the stopped closure attempt. This completes previously missing target-specific comparison, not a mathematical discovery or a correctness verdict on L138.
SCOPE: Exactly TARGET for q=137, T={16,64,70,102,112,118,121}, E=F_65537, F=F_(65537^28), arbitrary 61-core C and bijection sigma of L030, K=E or F, repeated quadratics, all full-sheet constancies, and each nonzero e in F_137^2. No closure derivation, counterassignment search, retained-family cap or RS transfer.

LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED for L138's separate conditional audit. Reuse of the retained primary proof resolves that specific missing comparison; further literature work on this unchanged target is unnecessary.

## Purpose, inputs and bounded test

The main gap remains arbitrary-center 67/68 safety. L138 claims that
even one translation inclusion for U=span_K{1,a_0,a_1,a_2} is equivalent
to full-sheet constancy, using factor degrees 136 over E and 34 over F.
An audit would determine whether this conditional reduction correctly
explains the strength of the parked closure bridge. It would supply no
inclusion and no new full-sheet rigidity result.

Essential inputs are L030's labeling setup, canonical L138, the prior
closure assessment and the cited primary proposition and its proof.
No cross-notebook input is needed. The subsequent audit must check exact field cardinalities,
squarefreeness, the invariant subspace and constant function, all
nonzero translation directions and directional propagation under the
full-sheet equations. These remain proposed mathematical audit checks, not findings of this source review.
Accept the restricted equivalence only if every implication and both
field cases pass; retain and correct any defect without extending scope.

The missing translation-inclusion premise, span-three rigidity, partial
retention, arbitrary label laws and global RS transfer remain independent
unresolved assumptions. The closure attempt stays parked pending a new
all-label rigidity input. A critical audit is not permission to rerun
the failed six-membership test or ATTEMPTS/109–113. Mathlib full and
supporting coverage is not checked here. The comparison below makes the
unchanged target ready for a separate research audit; this turn performs
no mathematical audit, new specialization or script verification.

## Primary theorem and essential proof cases inspected

The precise input is Proposition 2.6(1),(3), pp. 309–310 of the linked
2017 journal version, not an uncertainty inequality. Its hypotheses are
a prime p different from the coefficient field's characteristic; part
(3) assumes a finite field of order ell. The proof and the following
paragraph explicitly allow ell to be a prime power. Thus the source's
field hypothesis covers both E and F directly. There is no requirement
that the coefficient field contain F_137 or any nontrivial 137th root.

Part (1) uses separability of X^p-1, distinguishes g_0=X-1, and applies
CRT to all distinct irreducible factors. Part (3) sets r=ord_p(ell),
uses the cyclic multiplicative group of a finite field to identify the
smallest extension containing a nonidentity pth root, and identifies
every factor other than X-1 as degree r. Its resulting ring is the
direct sum of the coefficient field and (p-1)/r copies of its degree-r
extension. The p. 310 sentence about every pth root must retain the
exception of the identity root, as in the immediately following factor
statement and the explicitly separated X-1 component. The identity
component cannot be discarded when auditing a space containing 1.
All these proof cases were read in the retained primary text; the
following discussion of ideals was read only through its prime-power
clarification. No larger passage or unrelated theorem was needed.

## Scope comparison and exact audit obligations

L138's displayed degree values 136 and 34 are local arithmetic claims,
not values supplied by EKL. The audit must verify their short order
certificates and use cardinality 65537^28 for F, rather than reusing
the characteristic as the extension field's cardinality. No arithmetic
has been rerun or certified in this literature turn.

The source's ideal classification is not itself a classification of
arbitrary invariant subspaces of functions on G. The audit must justify
the actual operator restriction under the assumed inclusion, its
annihilating and minimal polynomials, and the application of CRT
idempotents for the larger-space threshold. It must retain the nonzero
fixed vector 1 and verify that the original bound dim U<=4 is the
relevant bound. This is ordinary finite-dimensional linear algebra
using the inspected factorization, not a new source theorem to seek.

The passage from trivial action in one nonzero direction to equal
quadratic messages is also local to L138. Audit it from the original
full-sheet equations: all nonzero e, a direction with nonzero intercept
increment, all 137 distinct labels in that direction, iteration in
the auxiliary prime field, and the polynomial root bound over K.
Repeated messages, arbitrary C and sigma, and the converse implication
remain in scope. No descent of an F-valued assignment to E is permitted.
The inherited labeling use was located in L030's construction; it
does not make sigma a field map.

ATTEMPTS/113 and the closure working record already explain why
translating the equations changes labels and supplies no membership
in the original U. Their transport identity and covariance may be
checked within L138's audit as qualifications, without another closure
search or a counterassignment script. The assessment approves checking
the conditional result, not deriving its premise. L137/C137a's geometry
is not a mathematical input to this argument. No cross-notebook input
or additional source hypothesis has been silently introduced.

## Decision and limits

SPECIALIZE is appropriate because the named theorem covers the cyclic
factorization, while the saved target audits its existing finite-field,
operator and full-sheet application. A fresh search for a stronger
uncertainty theorem would not settle these checks. Accept L138 only
after both field cases and every implication pass a separate critical
audit; record and repair any precise defect if they do not. A failure
would qualify this conditional input, not disprove the RS target.

This source review clears the audit's literature gate. It establishes
no result beyond the retained sources, no mathematical change to the
955–957 bracket and no reason to reopen closure. The full-sheet
span-three, retention, compatible-law and RS-transfer gaps remain.
