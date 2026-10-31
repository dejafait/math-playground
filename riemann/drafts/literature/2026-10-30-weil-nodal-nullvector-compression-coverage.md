# Nodal compression at a conditional first-zero nullvector: source comparison

TARGET: Test whether positive/negative-part compression of L516's complete form at an assumed first-zero nullvector controls L522's signed prime remainder enough to force S<=P-H at lambda=0, retaining the signed pole and every prime atom.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched Beurling-Deny positive/negative-part criteria, nonlocal signed ground-state/nodal forms, Keller-Schwarz nodal-domain results, and Weil nodal/ground-state/modulus terms; checked the specific local Weil assessments and L517/L518 stops. No inspected theorem covers the signed derivative bound. This bounded comparison does not establish novelty.
SOURCE_EVIDENCE: Read Fukushima-Oshima-Takeda second edition Theorems 1.4.1 and 1.4.2(i) and relevant contraction proofs pp.25-28; Keller-Schwarz arXiv:1712.07414v1 Lemmas 3.4-3.5 with complete proofs, Theorem 3.6 and its sign step pp.7-9, and Appendix A.3 Lemma A.13 with proof p.23; Chen-Weth arXiv:1710.03416v6 Proposition 3.2/Lemma 3.3 and Theorem 3.4's ground-state proof pp.13-15; bramble_trace paper 67 v1 (2.1), (3.1)-(3.5); teal-sea revision 7bec0814 Sections 2.6/6 and their qualifications. Exact links/scope below; L515/L516/L521/L522 reused.
COMPARISON: Reference-part lattice closure has a precise standard source. Nodal sign and pure-log ground-state theorems require a modulus-energy comparison not supplied for the complete signed form. Pole-free ground-state transforms overlap existing work. None of the inspected results controls L522's signed derivative correlations from the proposed two-part constraints; the exact retained-kernel test remains distinct and unperformed.
GAP: Determine whether fixed-interval semidefiniteness plus the exact null equation and full nodal interactions yield S<=P-H, or merely quadratic overlap constraints. Domain membership must be justified from the reference part form; complete-form contraction, a positive ground state, simplicity and nonzero nodal parts cannot be imported.
REASON: Essential theorem scope is now inspected, so a single bounded mathematical test is justified after the supervisor's separate approval of this changed gate. EXPLORE covers that test and an informative failure; it does not authorize a sign theorem, repetition of generic identities, or another readiness loop.
LITERATURE_REASON: At turn start the unchanged target had REVIEW_REQUIRED coverage for essential lattice-domain/nodal hypotheses. This literature-only comparison closes that scope question; further literature needs a changed hypothesis or specific essential unread lead.
SCOPE: Retain L522's fixed model and hypotheses: 0<a<A, ell=2a>log(2), c=log(2pi), nu_rho, both shifts, cutoff-equality atoms, signed pole, real normalized nullvector, nonzero left trace and excluded direct reflected-endpoint collision. Additionally assume A_a>=0 on its actual form domain at this one interval. Existence, first-zero realization, global positivity, trace vanishing and uniform family estimates are not supplied. No simplicity, parity or positivity of the vector may be presumed.

The main gap remains actual-Xi all-degree positivity. The intermediate
question concerns whether the exact eigen-equation and extremality at
a hypothetical first zero yield a signed restriction unavailable for
arbitrary smooth tests. If it forced S<=P-H, L516's identity would
force zero boundary flux at that conditional nullvector. This alone
would still leave positive-eigenvalue rates, family uniformity, support
continuation, first-zero existence/realization and Xi transfer open.

For the proposed bounded test write v_+=max(v,0) and
v_-=max(-v,0) on (-a,a). Source coverage must first justify their
membership in the actual part-form domain. The proposed calculation
would inspect the two-by-two matrix b(v_i,v_j), i,j in {+,-},
and the null equation for v=v_+-v_-. No positivity-preserving
property of the full signed operator is assumed. A zero nodal part
must be allowed, and no division by either part is admissible without
a separate nonvanishing hypothesis. The pole and atomic cross terms
may not be dropped or replaced by absolute values.

Continue only if the comparison identifies a concrete way that these
constraints control the derivative correlations in L522, or a bounded
obstruction test distinguishing that control from quadratic overlaps.
A citation giving only generic nodal identities is not a sign theorem.
If this compression supplies only an energy restatement and leaves
the derivative correlations uncontrolled, record that limitation and
park this implementation; do not infer a counterexample to RH.

The three-way mechanism comparison and preserved stops are in
`../../ATTEMPTS/2026-10-30-l522-review-loop-and-nodal-continuation.md`.
The original REVIEW_REQUIRED nomination above is retained as the
question, not as a claim of a proved compression identity. The source
comparison below now covers its bounded exploration. Known quadratic
algebra must be identified as reproduction; only the attempted bridge
to the signed arithmetic derivative is the creative question. No such
bridge is derived in this literature turn. Full matching Mathlib
coverage is unchecked. No cross-notebook input is proposed.

## Primary statements and applicability boundary

[Fukushima, Oshima and Takeda, *Dirichlet Forms and Symmetric Markov
Processes*, second revised and extended edition, 2011, Theorems
1.4.1 and 1.4.2(i), pp.25-28](https://api.pageplace.de/preview/DT0400.9783110218091_A15362972/preview-9783110218091_A15362972.pdf)
give normal-contraction and lattice closure for a Dirichlet form.
Read the statements, the positive-measure approximating-form argument
(1.4.7)-(1.4.9), and the proof of (i). The relevant form is L515's
stipulated reference part Dirichlet form on the open interval with
Lebesgue measure. L516 already states that its bounded perturbation
has the same form domain. This supplies the source route for the
later membership justification. It supplies no contraction inequality
for the complete perturbed energy and no operator-domain membership
of the clipped vectors. Weak form tests suffice for the proposed
compression; any stronger use needs justification. No independent
reproof of the reference theorem is warranted.

[Keller and Schwarz, *Courant's Nodal Domain Theorem for Positivity
Preserving Forms*, arXiv:1712.07414v1, 20 December 2017](https://arxiv.org/pdf/1712.07414v1),
Lemma A.13 (p.23), assumes modulus contraction, not merely nonnegative
spectrum. Lemmas 3.4-3.5 and Theorem 3.6 (pp.7-9) retain positivity
preservation, compact resolvent and admissible nodal restrictions.
The complete relevant proofs were read: the sign comparison in
Lemma 3.4 explicitly uses modulus contraction; Lemma 3.5 expands
quadratic overlaps; the theorem then uses that sign in a variational
bound. Thus neither a nodal count nor a sign-definite full ground
state is available by automatic citation here. This is a hypothesis
comparison, not a proof that the full form fails the criterion. The
extracted text of Lemma A.13 displays sign inconsistencies; use the
explicit positive-part convention fixed above and verify the algebra
in any later specialization rather than trusting those extracted signs.

[Chen and Weth, *The Dirichlet Problem for the Logarithmic Laplacian*,
arXiv:1710.03416v6, 3 June 2019](https://arxiv.org/pdf/1710.03416v6),
Proposition 3.2 and Lemma 3.3 (p.13) give a positive difference-kernel
representation and strict modulus comparison for the pure operator
with symbol 2 log|xi| on a bounded domain. Theorem 3.4(iii), pp.14-15,
uses that comparison at a minimizer to get constant sign; strict
positivity invokes its cited strong maximum principle, not audited
here. Its pure operator is different from L516's complete operator.
Neither its sign nor simplicity transfers by citation after adding
the signed pole and prime shifts.

## Direct overlap, failures and coverage decision

The [teal-sea theory notes](https://zeta.teal-sea.com/read/hunts/weil_propagation/theory/RESULTS.html)
now identify compilation 30 October 2026, revision 7bec0814, rather
than the older revision in the reused resolvent assessment. Read
Section 2.6's stated hypotheses and full Proposition M/sector
qualification, and Section 6's ground-state-transform comparison.
Their sign-definite reference vector belongs to the pole-removed
operator. The notes label these arguments unreviewed and the gap
comparison failures measured. No numerical result, full-form sign
or new theorem is imported. Searches within this page found no
nodal/modulus statement matching the present target. Pole-free
Markov structure or the generic transform alone would repeat that
work without supplying the missing full-form derivative estimate.

[bramble_trace, paper 67 v1, 27 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/67),
(2.1) and (3.1)-(3.5), retains precisely the signed bounded
perturbation being compared. Its manuscript proof remains qualified
as in L516; this review does not audit it. Its already assessed
Section 9 leaves relative flux control open.

The local L522 readiness-loop stop remains in force. L517's
high-frequency obstruction is for smooth tests, expressly not exact
nullvectors; L518's raw adjoint residual cannot be silently removed.
The generic pole-resolvent stop does not prohibit the present
two-part test, but it prevents treating a changed spectral notation
as an arithmetic estimate. No matching previous assessment was found
in these narrow paths. Failed searches are not evidence of novelty.

The strongest usable standard input is domain closure, with generic
nodal quadratic machinery available only at its stated scope. A later
attempt must specialize it explicitly and compare the exact signed
cross terms with L522's derivative correlations, allowing a zero
nodal part. If only static overlaps remain, document that failure
and park this implementation. Do not infer logical independence of
the full arithmetic problem from a generic signed-matrix example.
No new inequality, countermodel, compression formula or cancellation
has been derived here. EXPLORE covers one such test after gate
approval, not a claim that standard sources settle it.

The guessed v2 HTML URL failed; the v1 primary PDF was accessible.
A shell PDF download failed DNS, without blocking the web reading.
The supplementary Bremen semigroup PDF was inaccessible and is an
unused lead. No essential source blocker remains for this bounded
target; no Mathlib absence claim is made.
