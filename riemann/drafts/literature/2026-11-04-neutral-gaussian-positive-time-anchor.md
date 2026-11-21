# Source comparison: a positive-time anchor from a verified zero window

TARGET: Assess source coverage for eventual positivity of L753's Gaussian energy from a certified real-zero window and a nonvanishing Fourier value inside it, retaining the complete complex-zero tail and keeping backward sign propagation separate.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact Weil/Gaussian/eventual-positivity and exponential-sum/lowest-zero searches; primary Platt--Trudgian and Platt theorem/proof-scope reads; reuse of the step-325 Gaussian comparison; targeted local duplicate and failure checks. An inaccessible related Perisic preprint is an unread overlap lead, not an imported theorem or evidence of novelty.
SOURCE_EVIDENCE: Platt--Trudgian arXiv:2004.09765v1 Theorem 1 and Section 2, printed p.2; Platt 2017 accepted manuscript Theorem 5.1 and preceding computation report, printed p.8, with isolation/completeness passages in Sections 4.1-4.2; Carneiro--Milinovich arXiv:2403.17803v1 Section 2.2 Lemma 4 and proof attribution, printed p.5; audited L753 statement and Section 2, L018 and L024.
COMPARISON: The finite-window certificate and the unconditional explicit formula can be imported; the fixed-test large-time comparison still requires a separate elementary specialization with a complete summable tail. No inspected theorem directly states this exact weighted anchor. No reproof of the explicit formula or zero computation is justified; no novelty is claimed for spectral dominance.
GAP: Prove eventual strict positivity for the fixed neutral test under the stipulated separation and nonvanishing, without substituting real ordinates for unverified complex zeros. Arbitrary-test visibility, backward propagation and unrestricted positivity remain open.
REASON: The source inputs suffice to prepare one independent starting-sign attempt; the new work is applicability and a full-tail estimate, not a new general positivity principle.
SCOPE: Fixed complex f in C_c^infinity(R) with both exponential moments zero; certified H>1/2 with every Xi zero |Re z|<=H real; certified real zero gamma_* with gamma_*^2<H^2-1/4 and F_f(gamma_*)!=0. Seek E_f(tau)>0 eventually, with onset depending on these data. Multiplicities and the entire unverified tail remain. No all-f uniformity, effective numerical onset, backward evolution or tau=0 sign.
LITERATURE_REASON: The proposed anchor changes the audited fixed-[0,T] scope to a large-time sign claim and introduces a verified window plus a separated visible real zero. This review fills those essential source questions; it does not repeat the identity audit.

## Main gap, target and discriminator

Unconditional actual-Xi mixed positivity and unrestricted complete neutral
Weil signs remain the main gap. The one intermediate target is the
restricted eventual-positive-time anchor in SCOPE. It could supply a
starting sign for a future differential comparison; no suitable backward
comparison has been specified or approved.

Continue the later attempt only if a strictly positive certified real-zero
contribution dominates the absolute value of the *entire* complementary
complex-zero sum. The proof must exhibit a summable majorant independent
of unbounded time in the comparison it actually uses, rather than reuse
L753's time-dependent bounded-interval constant. Failure to do this, loss
of strict separation, or loss of the stipulated nonvanishing defeats this
target as stated. Tests invisible at all suitable certified zeros and
extensions by density are outside the approved scope.

## Precise primary inputs inspected

1. Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
   3 times 10^12*, Bulletin of the London Mathematical Society 53
   (2021), 792-797, DOI 10.1112/blms.12460.
   [arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
   Theorem 1 and Section 2, printed p.2 (PDF p.2). The theorem certifies
   all nontrivial zeros through height 3,000,175,332,800. The proof report
   combines certified sign changes with Turing completeness; Section 2
   expressly distinguishes counting from high-precision isolation.
   Thus H=3*10^12 is a conservative window. L018's coordinate and
   conjugation symmetry supply the negative-height translation. For
   height zero use Platt's symmetric Theorem 5.1 below together with
   L024's exclusion of Xi(0)=0, rather than read a positive-height
   statement as covering that case. This is a published computational theorem imported by
   citation, not an independent replay. No claim of high-precision
   individual ordinates or test-function nonvanishing is imported here.

2. David J. Platt, *Isolating some non-trivial zeros of zeta*, Mathematics
   of Computation 86 (2017), 2449-2467, DOI 10.1090/mcom/3198.
   [Author accepted manuscript](https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf),
   Theorem 5.1 and preceding report, printed p.8 (PDF p.9; Bristol cover
   is PDF p.1). The theorem gives simplicity and critical-line location
   for |Im rho|<=3.0610046*10^10. The report records 103,800,788,359
   isolated positive-height zeros and Turing completeness. Sections
   4.1-4.2, printed pp.6-7, explain completeness and the final rigorous
   checks on both sides of a proposed sign change. These passages,
   not just the abstract, were read. They provide certified real zeros
   far inside the larger window without needing a decimal first-zero
   ordinate. Simplicity is stronger than needed and will not be assumed
   in the anchor statement. The individual data are not downloaded or
   replayed; F_f(gamma_*)!=0 remains a test-dependent assumption.
   Earlier /files/ and AMS URLs failed; the /ws/portalfiles/portal/
   manuscript resolved the essential access issue.

3. E. Carneiro and M. B. Milinovich, *On Littlewood's estimate for the
   modulus of the zeta function on the critical line*,
   [arXiv:2403.17803v1](https://arxiv.org/pdf/2403.17803v1),
   Section 2.2, Lemma 4, printed p.5. Read its full unconditional
   analytic-strip statement and proof attribution to Iwaniec--Kowalski,
   *Analytic Number Theory* (2004), Theorem 5.12. It requires analyticity
   on |Im z|<=1/2+epsilon and uniform power decay of exponent >1 there.
   Complex zero coordinates, both pole terms and all prime powers occur.
   Neighboring Lemma 5 assumes RH and is excluded. Reuse L753's audited
   specialization; the large-time estimate is not a source conclusion.

The dominated convergence theorem for absolutely summable series is a
standard named input already used in L753. Ordinary heat trace intuition
or a positive spectral measure is unnecessary and cannot be substituted
for its hypotheses. No self-adjoint realization of actual-Xi zeros is
assumed. A later proof must verify its majorant; no such estimate is
proved during this literature turn.

## Known-result comparison and duplicates

The step-325 assessment
`2026-11-04-neutral-gaussian-flow-discovery.md` already inspected the
Connes--Consani compact neutral criterion, Suzuki's RH-dependent norm
identification, Hunter's ordinary heat theorem and Rodgers--Tao's
backward-Xi flow. Reuse those exact scope conclusions. None supplies
unconditional backward sign propagation for this fixed-test smoothing.
The proposed anchor adds an explicit visibility hypothesis and certifies
only eventual positivity for that test, not the criterion for all tests.

Read L753's statement and Section 2 for the precise zero summability and
Fourier strip bounds, and L018/L024 for coordinates and multiplicities.
Searches of the Gaussian assessments and histories 325-329 found no
completed version of this anchor. L466's proof was read only to identify
the finite-zero source; its Laguerre conclusion is not an anchor input.
The L751 residual statement and L752 absorption-stop record were checked:
a negative sine residual and an identity that absorbs to the original
energy give no sign law here. Preserve both stops.

The September 12 Gaussian averaging stop concerns cancellation of complex
center values; September 13 finite truncation loses moving mass; October
4 first-spectrum signing retains a signed cross term and an unpaid
nonvanishing hypothesis. Their ATTEMPTS records were read. They are not
duplicates of this fixed zero-spectrum comparison, but forbid inferring
a lower bound from a positive Gaussian kernel or a finite preview. The
present target also keeps its nonvanishing assumption explicit.

## Search record and unresolved overlap lead

Actual queries included:
- `Platt Trudgian Riemann hypothesis true up to 3 10 12 Theorem 1 2004.09765`;
- `Weil positivity Gaussian heat flow fixed test function eventual positivity Riemann zeros`;
- `Riemann zeros exponential sum Gaussian large parameter lowest zero dominance positivity`;
- `"Weil" "Gaussian" "eventually positive"`;
- `"Dirichlet series" "first term" "asymptotic" complex exponents absolutely convergent`;
- `"zeta" "heat trace" "Voros" "zeros"`;
- `"Extracting the First Zeta Zero from Blurred Primes" theorem`.

A. Perisic, *Extracting the First Zeta Zero from Blurred Primes*,
[Zenodo v2, 11 August 2026, DOI 10.5281/zenodo.21885371](https://zenodo.org/records/21885371),
is a relevant overlap lead. Only its author-supplied record/description
was read. It discusses a Gaussian zero heat trace and Mellin moments
extracting the lowest zero using a finite verified window, without
global RH. The PDF download failed with a decoding error; direct/API/
preview variants failed and local curl had DNS failure. Its exact
hypotheses, theorem numbers and proof are **unread**. No theorem from it
is imported and no exact nonoverlap or stronger conclusion is asserted.
This prevents a novelty claim, not a reproduction of the already named
explicit formula plus standard absolute-sum comparison. Further access
work is not essential to that expressly REPRODUCTION target. Voros and
Kawalec references in its bibliography remain unread leads.

Open Mathematics Courses, numerical labs, AI research conversations and
claimed-RH hits are not mathematical inputs. No failed search establishes
absence. Full matching Mathlib coverage is not checked; no absence claim.

## Decision and later work

Source coverage supports a separate bounded standard specialization;
no new anchor theorem, estimate or proof was derived here. The precise
research target is saved in
`2026-11-04-neutral-gaussian-anchor-specialization.md` for the supervisor's
separate next-turn approval. A successful proof belongs in a canonical
lemma with Hypotheses, Conclusion, Proof and Mathlib, importing the named
results by citation. No fresh lemma identifier or DAG row is added now.

A creative backward-sign target remains unready: neither a concrete
comparison inequality of the required direction nor new control beyond
L751/L752 is available. This ordinary dominance specialization must not
be relabeled creative to meet cadence. No cross-notebook input was used.
