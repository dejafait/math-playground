# Continuum positive-law moment interface: source notes1547

18 November 2026. Literature-only comparison of assessment1546's exact
target. No continuum moment implication is proved in this document.

## Local scope and duplication check

Read C032j, C032k's statement, Section2 and audit1302, C032m's
statement and signed-integration/parity interface, C032p's statement
and source interface, and C032q's statement, signed construction and
Laplace interpretation. Reused ledger1528 and review1298's Boyer
inspection. C032k already proves the proposed positive-law argument
for finite width sums. C032m supplies the continuum entire functions;
C032p/q supply the measurable kernel and bounded Laplace identification.
Neither m nor q asserts the moment equivalence. This is a missing local
applicability statement, not evidence of a new analytic theorem.

Read stops1302/1534/1536, including the recorded audit1538 update.
Finite-family independence excludes finite support in its stated scope;
it supplies no continuum independence theorem. The recursion calculation
does not establish scalar-span closure. The direct compact-transform
bound is disproved. None is a ban on the present positive-output-law
interface, and none is reopened here. No sibling notebook was read.

## Primary analytic tools inspected

1. Jean-Baptiste Boyer, *The speed of convergence in the renewal
   theorem*, author manuscript dated 19 June 2015,
   [Definition2.1, Lemma2.2 and complete proof, printed p6](https://maths.jbboyer.fr/documents/articles/renewal.pdf).
   For a Borel probability on R with an absolute exponential moment
   of order eta>0, its transform is holomorphic on |Re(z)|<eta;
   all derivatives are bounded on smaller strips. The relevant proof
   uses exponential domination and differentiated integrals. No drift
   hypothesis occurs in this lemma. Its convention is exp(-zy), so
   use z=s for the Laplace transform. In a later specialization do not
   copy C032k's phrase "variable chosen as -s" without explicitly
   defining a reflected transform. The needed absolute moment agrees
   with the positive moment for a law supported on [0,infinity).
   This lemma is a forward theorem, not a converse moment criterion.

2. Ante Mimica, *Laplace transform*, course notes for Dresden,
   27 April-1 May 2015,
   [Definition1.1/Remark1.2, p5; Proposition1.4(i)-(ii), p6, proofs p7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
   For a positive measure on [0,infinity) with finite Laplace transform
   at every positive argument, all positive-argument derivatives are
   the signed damped moments; finiteness of the nth moment is equivalent
   to a finite right derivative limit at zero. Read both relevant proof
   cases: dominated difference quotients at positive arguments and
   monotone convergence toward zero. These statements include atomic
   laws and impose no density or zero-atom exclusion. The display in
   the first-derivative proof retains h after writing the derivative;
   its preceding domination and limiting integrand specify the intended
   limit. No use is made of that unpassed-quotient typography.

The remaining named tools are the identity theorem, Cauchy's coefficient
estimates/entire Taylor expansion and the monotone convergence theorem.
Their use is already explicit in C032k Section2 and audit1302. No new
general theorem or reproof is needed. Haslinger2.39's previously inspected
parameter-integration coverage is reused through C032m, not reapplied
to a growing test on the output half-line.

## Comparison for a later specialization, not a proof

The source hypotheses concern the output measure, independently of how
it was constructed. The proposed application is conditional on nu_eta
being nonnegative; C032q then supplies mass one and a finite Borel law.
Its positive-real Laplace identity and C032m's entire parity identity
are the exact replacements for C032k's finite-sum interfaces. The
remaining task is to write the local applicability argument, including
even-lift descent to the s variable and the positive-output moment
limits, rather than claim C032k's finite-width statement literally
already covers arbitrary eta. A citation to Boyer alone is insufficient.

The later proof must act on nu_eta throughout. It must not integrate
exp(cu), powers of u, or infinite component moments against signed eta.
C032q's bounded-test identity alone authorizes none of those operations.
Mimica supplies the positive-s derivative/moment limit tool; the entire
Taylor and nonnegative-series step is the existing C032k argument to
be specialized, not a conclusion recorded by this literature turn.

## Searches and unused leads

Queries: `Laplace transform positive measure analytic continuation entire
exponential moments abscissa singularity Landau theorem`; `Laplace
transform analytic at origin probability measure exponential moment
Widder theorem`; `Widder "The Laplace Transform" "THEOREM 5b"`;
`"Laplace" "non-negative measure" "singularity" "abscissa" theorem entire`;
`Widder Laplace Transform 1941 pdf chapter II 58 nondecreasing`;
`"exponential moment" "analytic" "Theorem" "characteristic" Lukacs pdf`.

An alternative is Widder, *The Laplace Transform* (1941), ChapterII,
Theorem5b, p58, the real-abscissa singularity theorem for monotonic
Stieltjes data. The [publisher chapter](https://www.degruyterbrill.com/document/doi/10.1515/9781400876457-003/html)
exposed metadata but denied chapter access. Nakagawa, *Tail probability
of random variable and Laplace transform*, Applicable Analysis84 (2005),
499-522, [AppendixA, p522](https://cn.ics.saitama-u.ac.jp/en/management/paper/post_print_media/649.pdf),
quotes its statement, without proof. Mimica's
[*Exponential decay of measures and Tauberian theorems*, v3, p2](https://arxiv.org/pdf/1301.2690v3)
also cites the result. These passages were inspected only as leads;
Widder's original proof was not read and is not a required import.
Use the inspected derivative/limit tools and the existing local argument
instead. No source blocker remains for that narrower specialization.

Full matching Mathlib coverage is unknown and was not checked. Inherited
fixed-v1, actual-divisor, multiplicity, counting, finite-zero and heat
positivity qualifications remain. Existence of feasible eta, actual
cone membership and unsmoothed Xi realization remain unresolved.
