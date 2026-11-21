# Signed rank-two Fredholm diagnostic — completed source comparison

TARGET: At (r,R)=(3,2048), certify the signed finite-rank Fredholm determinant and compare it with the original operator norm to test whether positivity survives norm>=1.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step434 searched finite-rank Sylvester/Fredholm determinant identities, general trace-norm determinant perturbations and actual-Xi low-order Toeplitz overlap; read Duits AppendixA Lemmas66/69 and their proofs, Bornemann Sections2–4 relevant cases, and Michalowski Section1.2. Reused the existing Fredholm, counting, evaluator and Decimal assessments and the named local stops. Queries/read limits below; no matching determinant-versus-original-norm certificate was located in the inspected material, and no novelty is inferred.
SOURCE_EVIDENCE: Maurice Duits, Determinantal point processes, DPP2 author PDF, AppendixA Sections1–3, Lemma66 p.51 and Lemma69 p.52/proof; Bornemann 0804.2543v2 Section2 p.7 Schatten product inequality, Section3 p.10 (3.2), Section4 pp.12–13 (4.1) and excluded Lemma4.1; Michalowski 2607.16795v1 Section1.1–1.2 pp.1–2 for coefficient normalization and recorded finite-order nonnegativity. Direct links and applicability limits below. Reuse L776/L777 and steps430/432/433; no essential source remains blocked.
COMPARISON: Known finite-rank determinant and general trace-norm perturbation results cover the signed method without selfadjointness or norm<1. L777 already supplies the conditional factorization and original-norm compression; sources do not supply the actual two-zero data, enlarged evaluator or numerical determinant/norm intervals. Low-order nonnegativity is already recorded in the inspected literature. The remaining work is a bounded specialization/implementation, not a new sign theorem or a uniform mechanism.
GAP: The source gate is paid for this exact one-pair test. All new numerical and specialization obligations remain unpaid: enlarged uniform evaluator error, both contour counts, true zero grouping, complete residues, F bounds, signed pairing, trace-norm error and two-sided original-norm enclosure. L777's operator error is not itself a determinant error. No estimate at (3,2048) was calculated here.
REASON: Approve one later calculation of the saved target using the cited general methods. Only a positive determinant together with norm>=1 supplies the proposed separation; success at this pair would still leave growing-order signed estimates and all-degree positivity unresolved. No source reproof, radius sweep or automatic refinement is justified.
LITERATURE_REASON: At invocation start the changed signed rank-two target lacked essential finite-rank determinant and perturbation coverage and required a larger evaluator domain; this review supplies that coverage while reusing the existing Fredholm/counting/Decimal assessments.
SCOPE: Source comparison completed in step434; the unchanged target is approved for one subsequent calculation. Retain actual G, r=3, R=2048 and the original Hilbert norm. An enlarged evaluator and one auxiliary factor circle are permitted only with newly proved bounds/counts as specified below. No radius sweep, assumed zero list, RH, desired minor sign or growing-order conclusion is allowed. No lemma, mathematical script, numerical experiment or new specialization identity was produced in this literature turn.

## Completed source review — step434

The main gap is actual-Xi all-degree mixed positivity. This diagnostic
tests a possible advantage of keeping signed interactions after the
sufficient norm criterion fails. It cannot establish uniform control.
The exact target above is unchanged from step433; this is its separate
source approval, not an invocation of the calculation.

### Newly inspected primary results

Maurice Duits, *Determinantal point processes*,
[author DPP2 PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf),
undated version identified by that filename, accessed 2026-11-04,
AppendixA Sections1–3, pp.49–52. Lemma66 and its complete block-matrix
proof give, for compatible rectangular complex matrices,

    det(I+XZ)=det(I+ZX).

Lemma69(2) and its complete proof reduce a finite-rank kernel with
square-integrable columns to its finite pairing matrix, without
invertibility, independent columns or selfadjointness. The proof uses
a finite-dimensional restriction and Lemma66. The source's inner product
is linear in the first entry, opposite to L777: translate by adjoints.
Its kernel framework starts with finite measure; the approved use is
the finite-dimensional algebra, not an unexamined extension to counting
measure. No point-process positivity is imported.

F. Bornemann, *On the numerical evaluation of Fredholm determinants*,
[0804.2543v2](https://arxiv.org/pdf/0804.2543v2), printed pp.7,10,12–13.
Section2 gives ||XY||_1<=||X||_HS||Y||_HS for Hilbert–Schmidt factors
and the two-sided Schatten ideal inequalities (2.3). Section3 (3.2)
identifies finite-rank determinants with finite-dimensional restriction.
Section4 (4.1), for arbitrary trace-class T,S on the same Hilbert space,
states

    |det(I+T)-det(I+S)|
       <= ||T-S||_1 exp(1+max(||T||_1,||S||_1)).

No selfadjointness, invertibility or norm<1 premise is needed. Read
Lemma4.1/proof: its sharper estimate requires a positive selfadjoint
base with largest eigenvalue<1 and a small trace-norm perturbation;
exclude it here. Also exclude (4.2)'s asymptotic error expression and
the Plemelj series outside its convergence disk. This review supplies
no trace-norm estimate for the pair.

### Reuse, overlap and failures

Reuse the ready assessments
`2026-11-04-zero-winding-fredholm-certificate-specialization.md`,
`2026-11-04-interior-zero-fredholm-norm-compression.md`,
`2026-11-04-actual-fredholm-fixed-pair-norm-test.md` and
`2026-11-04-actual-fixed-pair-certificate-audit.md` in this directory.
L776's zero-index symbol hypotheses, positive scalar prefactor and
L777's complex/confluent factorization and two Gram metrics remain
essential. Johansson 1802.07942v1 Sections2/2.1 and4 and the assessed
Python3.15.2/mpdecimal4.0.1 contracts need no new discovery. Their
methods apply to compact domains; all numerical constants and complete
analytic error estimates must be supplied for the changed domain.
L778's audited certificate is implementation evidence at its original
pair only. Its radius1600 bound supplies nothing on |w|=2048.

W. Michalowski, [2607.16795v1](https://arxiv.org/pdf/2607.16795v1),
Section1.1–1.2 pp.1–2, uses exactly G(w)=xi(1/2+sqrt(w)/2)/8 and
D_(r,k)=det[a_(k+j-i)]. Read its finite-order comparison and the
zero-sector argument. It records nonnegativity for all k and orders up
to approximately 9.4*10^12 using verified zeros and Schoenberg's theorem;
r=3 is included. Its Theorem1.1's independent strict-positivity wedge
k>=10^18 r^3 does not cover k=2. This checks substantial known overlap,
not an independent audit/import of Schoenberg's theorem or a claim
that the reviewed passage supplies strict positivity at this pair.
The diagnostic must certify its own strict determinant margin. No
new low-order sign beyond the inspected sources is claimed.

Read the specific shifted-boundary and q-Pascal ATTEMPTS records named
below and the L776/L777 proofs; neither stop applies to this signed
zero-index comparison. The former leaves a different finite boundary
sign unpaid. The latter obstructs an unchanged norm test on a different
model/ray. Neither supplies favorable signed cancellation. No local
duplicate of this pair comparison appeared in the inspected target
assessments and step433 history; this is not a novelty conclusion.

### Approved specialization and implementation obligations

These are obligations for the next mathematical turn, not results
derived in this source review.

1. Certify G on a new explicit compact disk covering every evaluation
   and Cauchy disk. A domain up to |w|<=4096 is within approved scope;
   that cap is an implementation choice, not a claimed error bound.
   Retain complete theta, integration, cosh, coefficient and arithmetic
   errors. Reusing the old polynomial construction is permitted;
   reusing its radius1600 remainder at the new radius is not.
2. Certify nonvanishing and count=2 with multiplicity on |w|=2048.
   One auxiliary factor circle sigma=9/8, |w|=2304, is approved for
   an independent same-count/nonvanishing check and positive F bound.
   Its admissibility is unproved. A wrong count on either required
   circle parks this proposed certificate rather than triggering a
   radius search. If grouping cannot be certified, stop inconclusively.
3. Obtain all true zero enclosures/grouping and complete derivatives in
   L777(2); do not assume two real simple zeros. Use confluent data if
   needed. Preserve the normalization of F, p, b, C, U and Y. Lower
   bounds for F and its reciprocal use full contours, not samples.
4. Apply the cited finite-rank identity to L777's already established
   A=UCY*. The intended factors for the substitution are U and CY*.
   Verify the signed pairing, order, adjoints and minus sign explicitly
   in the mathematical write-up, including dependent/confluent columns.
   Compute the pairing of finite approximating factors without replacing
   it by singular values or by the norm-compression matrix K.
5. Prove a trace-norm error certificate using the cited Schatten product
   inequality and the full-product expansion. Recheck Hilbert–Schmidt
   bounds for each factor difference; retain the cross term. L777's
   operator-norm conclusion alone cannot be inserted into (4.1). Enclose
   the approximating signed finite determinant with directed arithmetic,
   then apply (4.1) with independently certified trace-norm bounds for
   both operators. Include every root, residue, coefficient, Fourier
   alias and infinite-tail uncertainty. Check all negative Laurent modes
   in this changed k=2 case; the one-mode exclusion in L778 is insufficient.
6. Separately enclose the original operator norm on both sides through
   L777's two-Gram compression and full operator error. A certified
   finite singular-value enclosure plus the triangle inequality can
   support a lower bound; an upper bound alone cannot show norm>=1.
   Do not assume invertible Gram matrices. The exact determinant is real
   by L776; complex approximation errors must enclose its real value.

Continue signed-route development only if the determinant's strict
lower endpoint is positive and the norm lower endpoint is at least1.
If the norm upper endpoint is below1, stop finite-pair escalation for
lack of separation. Crossing intervals are inconclusive; failure to
certify positivity is not a negative minor. Preserve full certificates
and report all failed checks, with no automatic precision/radius sweep.
All-degree signs, growing-r interaction control, reciprocal-factor
budgets, multiplicity/tied-modulus issues and RH remain open.

### Search and access record

Queries included `Bornemann numerical evaluation Fredholm determinants
2008 finite rank determinant trace norm perturbation 4.1`, `Sylvester
determinant identity finite rank operators Fredholm determinant det I
AB I BA trace class`, `Riemann xi coefficients Toeplitz minors third
order positivity Polya frequency`, `"Lemma 66" "Sylvester"`, and
`"TRACE AND DETERMINANT FOR FINITE RANK OPERATORS"`. A targeted
low-order follow-up searched Schoenberg sector terminology; unread
1955 primary-theorem leads are not imported. Local reads were confined
to this notebook's named Fredholm/actual-Toeplitz assessments, relevant
L776–L778 ranges, step433 history and the two specific failure records:
`ATTEMPTS/2026-11-04-shifted-fredholm-boundary-sign-source-limit.md` and
`ATTEMPTS/2026-11-04-actual-qpascal-endpoint-norm-stop.md`.

Dyatlov–Zworski's large author PDF failed the web tool's size limit;
it is not evidence used here. Duits supplies the needed finite-rank
result, so no essential blocker persists. Böttcher–Widom's primary
pp.1–3 were reopened to confirm source identification; its existing
assessment is reused rather than replaced. No source supplies a signed
growing-order estimate. Thus a protected creative nomination is still
unjustified: the bounded diagnostic first tests whether signed interaction
demonstrates any advantage. Next routing is calculation/standard/high,
not a creative proof attempt. No cross-notebook input was read.
Full matching Mathlib coverage remains unchecked; supporting general
algebra/analysis coverage is not asserted to formalize this certificate.

## Original nomination — step433 (requirements retained)

## Mathematical purpose and bounded test

The main gap remains actual-Xi all-degree mixed positivity. L778 now
validates one sufficient norm test, but provides no uniform smallness
mechanism. The proposed intermediate target asks whether retaining the
signed finite-rank determinant can pay a coefficient sign where the
original norm criterion cannot. This is a concrete diagnostic, not a
claim of a new sign theorem. Its prospective use is deciding whether a
signed mechanism has demonstrated an advantage worth developing.

Essential local inputs are L017/L018/L021 and the audited conditional
L776/L777; L778 provides implementation experience, not estimates at the
new pair. Independently certify contour nonvanishing and exactly two
zeros with multiplicity in |w|<2048. Do not assume those zeros are real,
simple, or already known from a table. If needed, isolation/grouping,
complete residues, a zero-free F disk and a positive lower bound for F
must be obtained anew. Norm compression retains both Gram factors.
The signed determinant must use the correct finite-rank interaction;
the matrix of singular values cannot be substituted for it.

After coverage is approved in a separate turn, a future calculation
should attempt just this pair. Decisive evidence for developing a
signed route would be a strict lower determinant endpoint>0 together
with a norm lower endpoint>=1. If the norm upper endpoint is below1,
the test supplies no separation: stop this finite-pair escalation rather
than sweep radii or treat another sign as all-degree progress. A wrong
count parks the chosen pair. Crossing intervals are inconclusive, not
evidence of a sign failure or a norm obstruction. No automatic refinement
is authorized by this nomination.

## Required source comparison and reuse

Read precise finite-rank Fredholm/Sylvester determinant hypotheses and
the relevant nonselfadjoint error cases. Verify that the signed reduction
uses the actual operator, handles complex or confluent pole data where
needed, and propagates all coefficient, root, residue and truncation
errors. Reuse L776's Böttcher–Widom/Bornemann imports, L777's metric
audit, Johansson's whole-box/Cauchy coverage and step432's Decimal
contracts. Check existing low-order Xi sign results before attributing
any novelty to a finite coefficient sign. The radius/parameter changes
need an explicit approved evaluator scope; the old constants cannot
silently be reused. These are review obligations, not new mathematical
conclusions from this step.

The shifted-boundary stop concerns a different unpaid determinant and
must not be treated as a global ban. The q-Pascal original-norm stop
does not prove failure of this signed Fredholm test. Conversely neither
stop supplies favorable signed cancellation here. A genuinely creative
uniform mechanism is still not justified: the single scalar benchmark
gives no independently paid signed interaction estimate as r grows.
The next turn therefore receives theorem-comparison routing, not an
invented creative label. No cross-notebook input; full Mathlib matching
coverage is unchecked.
