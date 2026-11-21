# Fixed complete-reference inverse-error test: source-approved scope

TARGET: Test one N=512, K=65536 half-complement reference-form majorant for C744z's fixed546 inverse correction, retaining full W0 covariance and the full lifted residual, against .093538.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed source comparison552/step553 searched form-order inverse bounds and full block preconditioning and checked the scoped scalar/prefix/signed comparison stops; no matching fixed546 bound was found, with no novelty inference.
SOURCE_EVIDENCE: Reopened [Behrndt-Hassi-de Snoo-Wietsma1403.5704v1](https://arxiv.org/pdf/1403.5704v1), Sections2.1-2.3/Proposition2.1 p4, Theorem3.4/nonnegative proof case p11 and Corollary3.5 p12; [Dritschel-Rovnyak0903.3639v1](https://arxiv.org/pdf/0903.3639v1), LemmaA.1 pp28-29; [Teschl GSM99, 12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf), Theorems2.13/2.18 pp71-72/77. Reuse assessments541/552 and C744v/w contracts.
COMPARISON: Standard inverse-order and Schur tools cover the method and non-dense restriction, but do not certify the proposed reference, its numerical inverse or the lifted residual's complete weighted tail.
GAP: Establish and certify this one reference's positivity and domination on V0, justify the constrained inverse comparison and bound the full quadratic inverse action; no one of these is asserted here.
REASON: Step554 completes the separate literature approval and repairs the missing direct source URLs; the unchanged fixed-data test remains a standard-method specialization with all local estimates unpaid.
SCOPE: Only fixed546 f,g,h/hash and original full D,S,T,U; P modes0:511, K=65536, complement fraction1/2, moment penalty256; no trial optimization, response truncation or changed separation.

The main gap is L030-L032/C032a actual-Xi positivity. This test concerns
only the minimized energy for one pair of fixed endpoints. It could
supply a paid fixed-endpoint comparison or rule out one conservative
majorant. Endpoint-uniform signs, C744q margin, strict H2 slack/existence,
non-neutral coverage and global assembly remain independent gaps.

The following is a proposed calculation/proof target, not a derived
reference inequality. Put P on raw modes0,...,511 and Q=I-P in L2,
L=D+W0 with W0=S+256C*C, and use the already certified raw complement
floor d0=6.14 below C744z's h512>6.1442765416. Seek certified finite
Hermitian matrices M_lower and G_upper satisfying

    M_lower <= PLP,
    (QW0P)*(QW0P) <= G_upper.

Both inequalities must be proved in operator order, not entrywise order.
The proposed reference has head M_lower-(2/d0)G_upper and complement
(1/2) QDQ, with no reference off-diagonal. Test positivity of its head
and justify its comparison to L by the covered Schur/Young method on
the full form domain. No such positivity or domination is claimed now.
Use exactly this allocation and stop if it is unusable.

Use C744w's full response-only covariance B0*B0 on rows512,...,65535,
its matrix/arithmetic error and the entire n>=65536 W0 tail, including
response/penalty covariance. A response prefix is not W0. Reuse the
complete audited head-entry contracts, including the true moment
penalty and its rounding error. A verified factor reconstruction or
solve residual must certify any finite inverse quadratic action; a
floating Cholesky success or sampled smallest eigenvalue is insufficient.

For the original exact neutral trial, define the full lifted strong
residual rho=Tf+T*h-Lg. Check Dom(L) membership and P0rho=r using
C999j's particular applicability, rather than asserting that the raw
head P preserves neutrality. Check that the two moments vanish exactly.
On V0 the penalty vanishes; the larger-space reference is a sufficient
comparison only. Apply the cited relation-order theorem with the
restriction encoded on H0 and its multivalued orthogonal complement,
after checking its hypotheses and inverse action. Do not assert an
identity with a projected unrestricted inverse. The proposed sufficient
majorant is the reference inverse quadratic action on rho, once that
comparison is justified. No substitution is authorized without proof.

Enclose the whole weighted residual tail, not only its head. Retain
all covariance between Tf, T*h, Dg and Sg within each output range;
only orthogonal output ranges allow an exact split. Use complete T
and T* with their distinct orientations, all S, and full U in the
trial-energy comparison. The n>=K tail needs an analytic bound; larger
finite inverses do not pay it. No c_*^-1 scalar loss or new scalar floor
is permitted. The old c_* qualification remains in the inherited A0
construction; this test does not replay or strengthen that source.

One complete certified upper endpoint strictly below .093538 is a pass.
A certified lower endpoint at least .094207 for the reference majorant
rejects this majorant, not the actual inverse correction or RH. A wider
or overlapping enclosure is inconclusive. Failure to certify a positive
reference or complete tail ends this fixed attempt with the exact unpaid
term recorded; do not tune the split, trial, fraction, penalty or cutoff.
Save a full certificate with actual/required bounds, all failures and
reproduction paths if calculations are undertaken. No numerical value
is evaluated or approved in this literature nomination.

Essential inputs: C999j Sections1/3/4 and audit552; C744z Sections1-3,
8-9 and fixed546 direction SHA256
f39d45d9754d0415f5180e2cb5803d8152bfbaba3eb34130b4bf4b91b81da013;
C744v's complete D,S,T; C744w(12)-(17), all response-only covariance
and534 audit; assessments541/548/549 and completed552. Preserve the
analytic/IEEE754/Decimal contracts and whole-core/unreplayed c_* source
qualifications. This is a standard-method REPRODUCTION specialization,
not creative work or a three-cell sign claim. Full matching Mathlib
coverage is not checked. Work outside this fixed scope requires review.


## Completed source approval — 12 November 2026, step554

This literature-only recovery addresses the supervisor's specific missing-URL
report. The exact TARGET and numerical allocation above are unchanged.
Primary PDFs were reopened at the direct URLs in SOURCE_EVIDENCE; the
previous searches and duplicate/failure comparison in assessment552 are
reused because neither the target nor its hypotheses changed. No broader
novelty search or new mathematical derivation was performed.

Behrndt–Hassi–de Snoo–Wietsma v1, Sections2.1-2.3, defines inverses,
operator/multivalued parts and order for selfadjoint relations.
Proposition2.1 characterizes order for lower-semibounded relations by
shifted square-root domain inclusion and norm comparison. Corollary3.5
states inverse antitonicity for nonnegative selfadjoint relations on a
separable Hilbert space. Theorem3.4's sufficient proof, including the
zero-negative-index case, uses positive shifts and successive strong
resolvent limits; no closed-range hypothesis is imposed there. These
source statements include non-dense domains. They do not supply the
proposed reference order or identify a restricted inverse with a projected
unrestricted inverse. The research step must check the relation encoding,
form-domain inclusion and inverse action specified above.

Dritschel–Rovnyak v1, LemmaA.1 and both proof directions, treats a bounded
operator on a Hilbert space split by a closed subspace: positivity is
equivalent to nonnegative diagonals and contraction factorization of the
off-diagonal through their square roots. Its proof uses block factorization
and partial isometries. LemmaA.2 already assumes positivity; it cannot
supply an unknown sign. Neither lemma directly supplies an unbounded
logarithmic form-domain bridge or the complete covariance estimate.

Teschl's author-hosted GSM99 PDF identifies its version as 12February2009.
Theorem2.13, its preceding dense-domain convention and proof pp71-72
associate a unique selfadjoint operator to a closed semibounded form.
Theorem2.18/proof p77 gives the selfadjoint lower-bound/resolvent criterion
and a resolvent bound below a strict spectral lower bound. These inputs
cover representation and inverse control only after their hypotheses
are established; pointwise strict positivity alone is insufficient.

The standard results are imported by citation; any future local proof
must address only their applicability and the fixed numerical difference.
No new lemma is approved here as a theorem. Full matching Mathlib coverage
remains unchecked. Existing scalar/prefix stops531/537/543/544/545/546/550/552
are preserved; assessment552 explains why they do not decide this metric
test. No new numerical evidence or improvement toward RH was obtained.
The required positivity, domination, full covariance, residual projection
and complete weighted-tail checks remain exactly as nominated above.
SPECIALIZE is approved for this unchanged target; stop without retuning
if its reference or complete tail cannot be certified. The two thresholds
and inconclusive case above are retained verbatim.
