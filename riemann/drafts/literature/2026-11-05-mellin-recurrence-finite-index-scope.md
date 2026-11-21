# Finite negative index in the actual Mellin recurrence — completed comparison

TARGET: Assess whether finite negative-square index of the actual Mellin quotient q can transfer through its Bernstein-gamma recurrence to a finite nonreal-zero bound for Xi, or identify the exact missing hypothesis.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step646 searched Bernstein-gamma/negative squares, generalized Nevanlinna/Mellin, recurrence/nonreal zeros and finite-index factorization; inspected the primary passages below and reused step443's product-theorem scope. No adequate recurrence-to-Fourier-zero bound was located; no nonexistence or novelty inference.
SOURCE_EVIDENCE: KPS AIF74(2024), (4.14)/Theorem4.4 p396, Example4.2.4 p399 and Section5.2.6 pp416–417; Patie–Savov arXiv:1604.05960v4, (4.2)/(4.7) pp21–22, Theorem4.1(1) p22 and Section5.5 p33; Hassi–Wietsma arXiv:1312.7248v1, Section2.2/Proposition2.4 p4 and Lemma2.5/proof p5. C828a/L828 reused; links and qualifications below.
COMPARISON: Finite negative index controls exceptional zeros/poles of q itself. The inspected Fourier-zero theorem instead uses a distinguished Bernstein-gamma factor with Pick and unit-separation hypotheses; its recurrence proof explicitly uses the latter to cancel singularities. Neither source supplies their replacement for actual q.
GAP: Global finite index of actual q, identification with the distinguished recurrence solution, and a transfer theorem to Xi zeros remain unpaid. L828 Section2 already supplies the density-based meromorphic M and entire normalized E construction; its representation-dependent zero-freeness must be kept separate.
REASON: Informative source-scope negative: park the automatic q-index transfer, preserve the exact missing recurrence cancellation/zero-transfer obligation, and nominate direct interpolation of E for separate review rather than testing an index with no downstream theorem.
LITERATURE_REASON: The hypothesis changes from complete Pick positivity to finite negative-square index, outside both the actual-theta audit and the earlier reciprocal-tail assessments.
SCOPE: Completed literature-only step646 for the exact TARGET. No new membership, recurrence theorem, zero bound, lemma or mathematical script; no generalized-index theorem has been disproved. The new direct-interpolation nomination is REVIEW_REQUIRED.

## Original nomination — retained as the question, not current coverage

The main gap is actual-Xi all-degree mixed positivity. C828a now makes
the complete-Bernstein obstruction applicable to the actual normalized
density. The proposed intermediate target asks whether a controlled
failure of Pick positivity has any useful zero-transfer theorem for this
different representation variable. A quantitative bound on nonreal zeros
could restrict the remaining obstruction, but would still leave global
index verification, localization/effectivity, and ultimately exclusion
of every off-line zero. Finite index alone is not advertised as RH.

Use C828a's exact real quotient
\[
 q(s)=2(2s-1)M(s-1)/M(s),\qquad
 M(s)=\int_0^\infty x^{2s}p(x)\,dx,\quad s>1/2.
\]
For a possible meromorphic continuation, the proposed index is that of
the standard kernel
\[
 K_q(z,w)=\frac{q(z)-\overline{q(w)}}{z-\overline w}
\]
on its regular upper-half-plane domain: a uniform bound on the number
of negative eigenvalues of every finite evaluation matrix. This is a
target definition, not a proved continuation or index assertion.
No finite sample can establish that global premise.

Retrieve primary hypotheses and relevant proof cases for a recurrence
or entire-transform theorem before large source passages. The bounded
question is whether a theorem controls the nonreal zeros of the
resulting J/Fourier function from this index, with its other hypotheses
explicit and independently testable for actual theta. Do not confuse
zeros of q or of its recurrence solution with zeros of Xi. In L828 the
identification with a distinguished W requires the representation law;
that identification is not automatically available after weakening
complete Bernstein positivity. In particular a theorem for indefinite
canonical systems alone does not identify this particular recurrence.

The relevant existing cautions are the
[automatic reciprocal-index stop](../../ATTEMPTS/2026-11-04-reciprocal-kernel-automatic-index-import-stop.md)
and the
[closed fixed Taylor-index diagnostic](../../ATTEMPTS/2026-11-04-fixed-taylor-index-nondiscriminating.md).
Their precise conclusions were read for this nomination. Their missing
global premise and nondiscriminating fixed test remain preserved; neither
is a global ban on indefinite methods. Do not repeat their matrix-size
or precision sweep. This nomination concerns q itself and a recurrence
transfer theorem, not L777's reciprocal tail or the coupled J-Q form.
No matching Mellin transfer theorem was found by the narrow local search;
this says nothing about novelty or existence in the literature.

Continue only if the source review identifies a precise transfer
statement, a genuinely independent actual-data premise, and one bounded
test whose outcome would change the route. If the only available premise
already assumes the wanted Fourier-zero count, or no recurrence transfer
is supported, record that exact scope obstruction and park this target.
Do not assume ordinary Bernstein membership or reopen paper23 supplement
access. An index bound without a transfer theorem is below the threshold.

This is preparation for a possible new central mechanism, not an approved
creative proof attempt. At present no sufficient noncomplete class and
actual sign bridge has been identified. A future creative nomination
requires the specific obstruction, decisive bounded test and separate
ready coverage. No cross-notebook input; full Mathlib coverage unchecked.

## Completed source comparison — step646, 5 November 2026

The main gap remains actual-Xi all-degree mixed positivity. The reviewed
intermediate target was a quantitative passage from finite index of q
to a finite nonreal-zero bound for Xi. That could restrict the remaining
obstruction but would not exclude every off-line zero. The continuation
threshold was an explicit transfer theorem with a root-independent,
independently testable actual-data premise. This search did not meet it.

### Primary hypotheses and relevant proof cases

S. Hassi and H. L. Wietsma, *Products of generalized Nevanlinna functions
with symmetric rational functions*, [arXiv:1312.7248v1, 27 December 2013,
Section2.2/Proposition2.4, p4](https://arxiv.org/pdf/1312.7248v1):
the input is a conjugation-symmetric meromorphic function on C\R whose
kernel has a fixed global negative-square index. Its canonical factor
is rational times an ordinary Nevanlinna function, accounting for
nonreal zeros/poles and real generalized zeros/poles of nonpositive
type with multiplicities and infinity qualifications. This concerns
the function to which the hypothesis applies, not its Mellin recurrence
solution or another transform. Also read Lemma2.5 and its complete
rational-composition proof, p5. It changes the argument of a known
class member; it is not a recurrence theorem. Reuse step443's inspected
Theorem4.5/product proof and support conditions without re-reading it.
No class membership or rational-factor specialization to actual q is
established here.

P. Patie and M. Savov, *Bernstein-gamma functions and exponential
functionals of Lévy processes*, [arXiv:1604.05960v4, 23 July 2018,
(4.2)/(4.7), pp21–22 and Theorem4.1(1), p22](https://arxiv.org/pdf/1604.05960v4):
the coefficient belongs to the Bernstein class B, and W is the
distinguished normalized Mellin solution. Read the defining
positive-random-variable condition, convergent product, theorem's
zero-free domain and the Section5.5 zero-free/recurrence proof case,
p33. Neither arbitrary finite-negative-square coefficients nor an
arbitrary normalized solution fall under these hypotheses. Zero-freeness
of W on its stated half-plane is not a Fourier-zero count. The existing
root-zero product-law audit in L828 is reused, not repeated or extended
to an indefinite probability law.

T. Konstantopoulos, P. Patie and R. Sarkar, *A new class of solutions
to the van Dantzig problem, the Lee–Yang property, and the Riemann
hypothesis*, [AIF74(2024), (4.14)/Theorem4.4, p396 and Section5.2.6,
pp416–417](https://www.numdam.org/item/10.5802/aif.3600.pdf):
the sufficient class is Bernstein Pick with unit separation, including
the specified alignment of successive zeros and poles. The full local
proof sketch was read: separation cancels recurrence singularities
before invoking Laguerre's theorem on the entire reciprocal factor.
No finite-index relaxation or quantitative defect bound is stated.
Theorem4.4's other conclusion and Example4.2.4, p399, show ordinary
class membership alone does not imply all real zeros. They are not
here claimed to give a finite-index counterexample or an infinite
nonreal-zero census. Reference[25] contains a fuller proof, not an
inspected finite-index extension; reference[52] is a future direct
interpolation lead, not newly assessed coverage.

### Applicability, duplicate checks and exact stopping point

C828a fixes p, M, q and their normalization. L828 Section2 (5)–(7)
constructs meromorphic M and entire E from precisely its density
hypotheses, now checked in C828a. That construction is already local
input, whereas E=1/W(s+1) and the ensuing zero-free half-plane use the
assumed representation. The original nomination's blanket unpaid
continuation warning is therefore refined: continuation does not pay
global class index or distinguished-solution identification. No new
continuation is derived in this review. In particular finite index of
q would still not verify the positive-law hypothesis used to identify W.

The source comparison must distinguish three zero sets: q, its chosen
recurrence solution, and Xi. Counting exceptional zeros/poles of the
first does not invoke any inspected theorem about the third. The exact
unpaid interface is a theorem replacing KPS's separation/cancellation
argument and its subsequent entire-interpolation step by a bounded
defect statement, with appropriate growth and normalization. Those
requirements are absent even if one hypothetically grants q in N_kappa.
This is a scope obstruction, not proof that such a theorem is impossible.

Read the recorded automatic reciprocal-index and fixed Taylor-index
stops and the step443 assessment. They concern h_r and the coupled J-Q
form, not q. Their finite-packet/global-premise distinction remains
relevant; their numerical diagnostic is not repeated. Read the actual
Mellin/Levy source comparison's normalization and existing ordinary-class
sign gap. Preserve paper23's supplement-access and endpoint stops;
neither supplement access nor a re-audit of endpoint bounds is needed.
L828/C828a are the only detailed canonical proof ranges loaded for the
present target. No cross-notebook input was used.

### Bounded searches, access and route

Queries: `"Bernstein gamma" "negative squares"`;
`"generalized Nevanlinna" "Mellin"`;
`"Bernstein" "recurrence" "non-real zeros"`;
`"generalized Nevanlinna" "gamma" recurrence zeros`;
`"Bernstein-gamma" "Nevanlinna"`;
`"generalized Nevanlinna" "canonical factorization" theorem nonreal zeros`;
`"generalized Nevanlinna" "difference equation" gamma zeros`;
and `"finite" "nonreal zeros" "multiplier sequences" Laguerre gamma`.
The last search found Craven–Csordas's Fox–Wright paper and composition
survey as direct-interpolation leads. Their theorem hypotheses were
not inspected, and their finite-zero hypotheses are not imported.
Search snippets, secondary mirrors and discussion posts supply no
theorem evidence. No claim of exhaustive absence or originality follows.

The three essential PDFs were readable through the web tool. A guessed
Opuscula realization PDF path failed and a direct unauthenticated curl
download failed DNS; neither is essential to this scope decision.
Do not classify this as persistent source blockage or retry access by
changing credentials. No downloaded source file was created.

Park automatic q-index transfer; no q-index computation is nominated.
The materially different continuation asks about direct Laguerre
interpolation of E itself and a single fixed-point necessary test,
recorded in `2026-11-05-direct-mellin-laguerre-interpolation-scope.md`.
It requires separate source review, especially integer normalization,
growth, sign of interpolation nodes and duplicates. No sufficient
noncomplete actual class has yet been established, so a creative proof
attempt is not yet justified. The new review must identify a useful
actual-data test or park that proposal too. Full matching Mathlib
coverage is unchecked. No mathematical exploration budget was spent,
and no new lemma, script, proof assembly or DAG edge was written.
