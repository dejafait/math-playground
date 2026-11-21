# Fixed exponential-momentum symmetry: proposed next target

TARGET: Test whether L909's common-profile asymptotic extends to the exp(-P/4) form norm strongly enough to force a nonzero Gram entry between distinct large positive real Xi zeros, with all complex-zero images retained by L910.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step162 searched the exact identifier/title with asymptotic, metric, orthogonality and imaginary-shift terms, theta common-profile terminology and Fourier endpoint remainders; compared the scoped local domain/profile assessments and metric/sign stops. No inspected theorem supplies the uniform weighted profile; unsuccessful searches establish no novelty.
SOURCE_EVIDENCE: Rechecked Hedenmalm2606.17494v1 https://arxiv.org/html/2606.17494v1#S4.SS2 Definition4.2.1/Theorem4.2.2 and both proof cases; DLMF https://dlmf.nist.gov/2.3#i (2.3.4)-(2.3.6), https://dlmf.nist.gov/1.9#iii (1.9.29)-(1.9.31); Teschl2009 https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf (3.50)-(3.51), p97, Theorem7.5 and preceding L1/L2 paragraph, p164. Reuse the saved Hardy1914 assessment and audited L909/L910; precise applicability and limits below.
COMPARISON: Endpoint remainders, Cauchy derivative formulas and Plancherel supply the standard tools; audited L909 supplies the ordinary-L2 profile and L910 the wider zero-free strip and per-zero shift identity. None supplies a uniform weighted remainder or F in Q. The unpaid difference is a theta-specific whole-line application, not a new general theorem or a direct import of the target.
GAP: Prove or obstruct F in Q with positive form norm and convergence of alpha^2 G_alpha to F in that norm uniformly along positive real exact Xi zeros; only then test the distinct-pair Gram consequence. Symmetry remains unresolved.
REASON: This separate literature-only review approves the unchanged step161 nomination for one mathematical specialization attempt. Essential tools and their hypotheses have now been inspected; the remaining local estimates are research obligations, not an unread-source blocker.
LITERATURE_REASON: Step161 changed per-zero domain inclusion to a uniform weighted common-profile target outside the domain-only and ordinary-L2 scopes; this turn supplies its missing theorem-level comparison rather than repeating ready coverage.
SCOPE: Exact TARGET only; fixed M=exp(-P/4), unchanged primitive/normalization and F of L909, positive real exact-zero asymptotics, full form-norm remainder and conditional distinct-real-pair diagnostic, with every complex-zero image retained using L910. Covers direct narrower-strip derivative/tail estimates, endpoint specialization and justified Fourier contour transfer. No metric-parameter search, new normalization, all-zero symmetry proof, completion, generalized-eigenvector claim or Xi-positivity transfer is approved.

## Step161 nomination, preserved; no mathematical conclusion

Keep the same W, L and primitives of L906/L907 and the complex
normalization of L908(1). Write F=(W''-W'^2/W)/i, precisely the
profile in L909. For f in the form domain Q of L910, use

    ||f||_Q^2 = integral_R exp(-k/4) |F_fourier f(k)|^2 dk.

This notation denotes the positive form norm only; it does not assert
that Q is complete for this norm or change the Fourier normalization.
The proposed estimate is F in Q and

    ||alpha^2 G_alpha - F||_Q <= C/alpha

for every positive real exact zero alpha, with a finite C independent
of alpha and 0<||F||_Q<infinity. None of these new weighted-profile
claims is proved or approved in step161. A weaker bound tending to zero
would also meet the intended common-profile threshold, if its
applicability and the resulting Gram consequence are fully justified.

The existing conditional diagnostic requires
(conjugate(beta)-alpha)b(G_alpha,G_beta)=0, where b is this form,
linear in its first argument. The goal is an actual nonzero
distinct-real-zero Gram entry, potentially via a uniform large-zero
bound. A finite-frequency numerical observation or a failed estimate
would not by itself refute symmetry. Retaining all complex generators
through L910 avoids silently restricting the source's domain to a
presumed real spectrum.

## Step161 source requirements, discharged by the separate review below

Reuse the known positive multiplier and Hedenmalm pair criterion; do
not reprove them. Compare the proposed estimate with the primary
finite-order oscillatory endpoint expansion, its half-line remainder
hypotheses, and imaginary-shift/Fourier norm results. Check whether
the existing source comparison covers the needed uniform remainder
after multiplication by q on the shifted line. Primary coverage must
precede any new derivative-tail estimate, contour expansion or Gram
calculation. L910 has a per-zero bound; it cannot be silently treated
as the required uniform-in-alpha estimate.

L909's audited dt/t obstruction is relevant earlier evidence, not a
theorem deciding this distinct form. The first-pair certification and
step154 phase stops remain preserved. No numerical zero indexing or
new root certificate is proposed; any use of arbitrarily large
distinct real zeros must retain the precise Hardy-theorem input
already recorded in L909. No cross-notebook input is proposed.

## Relevance and decision threshold

The main gap remains L030-L032/C032a actual-Xi mixed positivity. This
test addresses a necessary symmetry condition for one candidate
positive form, not mixed positivity itself. A rigorously nonzero
off-diagonal entry for distinct real zeros retires this fixed metric.
If the profile estimate fails, record its exact obstruction and leave
symmetry undecided unless another approved certificate settles it.
Success of a finite number of zero Gram tests would not prove all-zero
symmetry. Completion, multiplicities and Xi transfer remain separate.

This is a newly nominated continuation, not a second mathematical
attempt or a ready assessment. Next turn is literature_comparison.
Only after separate approval may the proposed shifted-norm calculation
proceed. It extends an established route and is not labeled creative;
no independently justified new central symmetrization mechanism has
been identified. Full matching Mathlib coverage is unchecked.

## Separate source approval, 9 November 2026, step162

The pending-review statements above describe the step161 nomination.
This section completes that separate review for the unchanged TARGET;
it does not prove any proposed weighted estimate. Prospective research
classification is REPRODUCTION. The source tools are known and the
remaining work develops the same endpoint-expansion mechanism.

### Primary inputs and their exact scope

- NIST DLMF, live text accessed 9 November 2026,
  [2.3(i), (2.3.4)-(2.3.6)](https://dlmf.nist.gov/2.3#i).
  Read both Fourier cases and the complete remainder paragraph.
  The finite-interval case assumes smooth amplitude. The half-line
  case also requires uniform convergence, in sufficiently large real
  frequency, of every derivative Fourier integral. After n terms
  the stated remainder is bounded by frequency^(-n) times the
  integral of the absolute nth derivative. This is an endpoint
  estimate, not a spatial norm theorem. At fixed imaginary height
  the integration variable is still real; a complex-valued amplitude
  can be treated componentwise, retaining any bound factor. No
  complex-frequency or complex-path asymptotic theorem is imported.
  The referenced Olver book passage remains unread and is unnecessary.

- NIST DLMF, same access date,
  [1.9(iii), (1.9.29)-(1.9.31)](https://dlmf.nist.gov/1.9#iii).
  Read the full Cauchy theorem and derivative-formula statements.
  They require analyticity inside, continuity on and inside, and a
  positively oriented simple closed contour. Formula (1.9.31) is
  the imported derivative tool. L910's larger strip supplies room
  for disks about a narrower closed strip; translating its bound
  into a useful uniform derivative envelope is still unpaid.
  Cauchy's theorem licenses finite rectangles, not their improper
  limits without decay estimates. Neither standard theorem is reproved.

- Gerald Teschl, *Mathematical Methods in Quantum Mechanics*,
  February 12, 2009 version, GSM99,
  [primary PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
  Rechecked (3.50)-(3.51), printed p97/PDF index108: the form domain
  is Dom(|A|^(1/2)), distinguished from Dom(A). Read Theorem7.5,
  printed p164/PDF index175, its norm-continuity proof and the preceding
  compatibility paragraph: the unitary Fourier extension agrees with
  the integral transform on L1 intersect L2. Reuse the previously
  assessed spectral calculus and momentum realization. These facts
  justify norm transfer once a valid contour identity and both traces
  are supplied; they do not assert imaginary translation for arbitrary
  L2 functions or give any theta-family remainder.

- H. Hedenmalm, *Spectral interpretation of Riemann zeta zeros*,
  [arXiv:2606.17494v1](https://arxiv.org/html/2606.17494v1#S4.SS2),
  16 June 2026. Rechecked the finite span, Definition4.2.1,
  Theorem4.2.2 and both proof cases. The span retains possible nonreal
  zeros; symmetry is a premise. Part(a) forces a nonreal generator's
  seminorm to vanish; part(b) forces distinct real generators to be
  orthogonal. Neither supplies a metric or the weighted estimate.
  Only this necessary pair condition is used for the proposed test;
  the conditional RH corollary is not an established symmetry input.

Hardy's unbounded positive-real-zero family and its completion
specialization are reused from the ready
[step155 assessment](2026-11-08-hedenmalm-large-real-zero-common-profile.md)
and audited L909. Its primary-transcription/facsimile qualification
remains unchanged. No effective onset, simplicity or zero spacing is
imported; no repeat Hardy search or reproof is needed.

### Local overlap, search evidence and limits

Read L909's complete common-profile proof and the relevant L910
strip, primitive, denominator and Fourier-transfer proof ranges.
Reused the ready domain assessment and the step155 comparison.
Checked the exact dt/t metric stop, step154 analytic-sign stop,
step158 nonlocal-metric comparison and step161 audit continuation.
They supply no duplicate weighted-profile result. L909's dt/t stop
concerns another form, and L910's constants may depend on alpha;
neither decides this target. All earlier evidence remains preserved.

Queries included `"2606.17494" "asymptotic"`, the exact title with
`metric`, `"2606.17494" asymptotic orthogonality`,
`"2606.17494" "imaginary shift"`,
`"Hedenmalm" "common-profile"`,
`"theta" "common profile" "imaginary shift"`, and
`"integration by parts" Fourier integrals complex amplitude remainder Cauchy estimates strip`.
Results included paper mirrors, unrelated spectral/metric proposals
and generic asymptotics notes. Their snippets are discovery leads,
not inspected theorem inputs. No stronger matching theorem was
identified in this bounded comparison; no originality claim follows.
The primary sources listed above, rather than mirrors or snippets,
support the decision.

### Approved application and discriminating test

The sole mathematical continuation may specialize those tools to the
saved TARGET. Its remaining obligations are explicit:

1. Control the shifted derivatives needed by the finite endpoint
   expansion and their complete half-line tails on a narrower strip.
   A Cauchy-formula application must retain a fixed positive distance
   from the outer boundary and check its spatial envelope. All
   improper derivative integrals and endpoint limits need bounds;
   real-axis derivative estimates alone do not verify them.
2. Justify lower/upper primitive and derivative cancellations using
   exact real zeros, the unchanged complex normalization L908(1),
   and L910's horizontal primitive. Retain multiplication by q
   throughout. A per-zero bound growing with alpha, including one
   from unbalanced phase factors in a contour shift, is not uniform
   vanishing error. No derivative of an uncontrolled remainder is allowed.
3. Establish F in Q, its strictly positive form norm, and the full
   form-norm error tending to zero, preferably the nominated C/alpha
   bound. Any Fourier transfer for F or the error must check its own
   holomorphy, real and shifted L1/L2 traces, and vertical limits.
   L910 proves its identity for G_alpha, not for every new function.
4. Only after those estimates, justify the joint Gram limit uniformly
   for two independently large positive real zeros and apply the
   imported necessary orthogonality condition. L910 keeps every
   complex-zero image in the original form domain throughout.

These are requested checks, not newly derived formulas or conclusions.
There is no need to reprove general endpoint asymptotics, spectral
calculus, Plancherel or Hardy; the theta-specific hypotheses, tails
and norm transfer explain the necessary application work.

A nonzero Gram entry for distinct actual real zeros retires this
fixed metric. If the proposed bound fails, record the exact obstruction
and leave symmetry unresolved unless an independently approved
certificate settles it. Pointwise asymptotics, a frequency truncation,
or a failed sufficient estimate do not decide the form. Completion,
multiplicities and all-degree mixed positivity remain independent.

No justified creative central mechanism has emerged: the present test
only checks a necessary condition for one imported form. This is the
reason to finish the bounded established-route diagnostic rather than
rename it creative. Full matching and supporting Mathlib coverage
remains unchecked, with no absence claim. No lemma, mathematical
script, DAG or PROOF.md change was made. The existing nomination has
now received its separate source approval; reuse this assessment for
the unchanged mathematical attempt next turn.
