# Growing-window modulation: completed source comparison

TARGET: Assess whether L744's corrected modulations satisfy E_{K(t)ell}(v_{t,w}) >= (log|t|/2)||v_{t,w}||_2^2 uniformly for fixed M and chi when K(t)=floor(log log|t|/ell).
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step495 searched exact corrected/neutral Weil modulation, growing support with Sobolev bounds, and log-log-support high-frequency positivity; inspected the primary passages below and narrowly compared L744 and the two recorded stops. No full matching theorem was found; search silence establishes no novelty.
SOURCE_EVIDENCE: Read L744(1)-(18) and its step289 audit; L740 hypotheses/(3)-(5), L741 Section2 and L743(9)-(10). Read DLMF5.11.2/5.11(ii); Zhu2608.24827v2 Thm1.1, Lem3.1/proof, Section4 tail/block argument and Lem6.1/proof; Rosser--Schoenfeld1962 Thm12/(3.35), p71, with its proof routing pp77-80. Existing fixed-window assessments are reused, not relabeled as moving-window theorems.
COMPARISON: Known scalar estimates, Fourier identities, finite delay bounds and the unconditional psi bound cover the source inputs. L744's displayed error constants have no explicit K, but its conclusion is fixed-K. Establishing uniform validity of its estimates and comparing the entire prime coefficient mass with the half-log budget remain application work; no moving-window conclusion follows by citation alone.
GAP: The exact displayed target remains unproved. The next attempt must track every K-dependent term, establish uniform nonvanishing and a single onset depending only on M,chi, and retain the full prime cost and exact complex pole cancellation.
REASON: Essential source coverage is now adequate for one bounded specialization attempt. The prescribed slow support growth is a new quantifier regime for this notebook, not a new high-frequency mechanism; classify its development as REPRODUCTION, without a novelty claim.
SCOPE: ell=log(3)/2, all sufficiently large |t| with K(t)>=2, fixed finite M and fixed chi exactly as in L744, w in its F_{K(t),M}, and its unchanged v_{t,w}. Complete E, complex tests, original L2 norm and exact cell moments. Empty families make no existence claim. No other support rate, profile class or denominator is covered.
LITERATURE_REASON: The startup target was REVIEW_REQUIRED because its moving-support quantifiers were outside all ready fixed-window assessments; this turn supplies that missing comparison and no new mathematical result.

## Completed comparison, 11 November 2026, step495

The main gap is still L030-L032/C032a actual-Xi positivity. The exact
TARGET above is retained for the next mathematical attempt. This review
does not establish its inequality, a uniform onset, or nonvanishing.
It prepares a known-method specialization, rather than deriving and
approving a new result in the same turn.

### Primary coverage and limits

[NIST DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii), accessed 11 November 2026,
give the digamma expansion with principal logarithm in sectors
|arg z|<=pi-delta. The complex remainder after truncating before the
first Bernoulli term is bounded by that term's magnitude times
sec^3(arg(z)/2). L744 uses z=1/4+i xi/2, which stays in the right
half-plane. This scalar input is unchanged when support varies. It
does not itself control a varying Fourier measure or its correction;
L744's quantitative integration bounds must be used instead. There is
no reason to reprove the expansion.

[Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
arXiv date 2 September 2026, Lemma3.1/proof gives
m(t)>=log(t/(2pi))-1/t for t>=15/4 and subtracts the full finite
prime mass. The proof uses Binet's formula in Re z>0 after a digamma
shift. Theorem1.1 and Section4 retain the low-frequency block and
its tail coupling; they do not sign that block. Lemma6.1/proof
retains a negative odd pole, so the real-even formula cannot replace
our complex pole product. In Zhu's notation the support radius is
a and the prime cutoff is exp(2a); our interval has length L=2a.
This is supporting high-frequency coverage, not a matching
corrected-family or all-window theorem. Its full reduction/certificates
are not imported or independently certified here. The previously
assessed envelope-page theorem has a different form normalization;
reuse the recorded rejection in the joint-energy assessment rather
than treating its growing-support headline as an import.

[Rosser and Schoenfeld, *Approximate formulas for some functions of
prime numbers*, Illinois J. Math.6(1) (1962), 64-94](https://doi.org/10.1215/ijm/1255631807),
Theorem12, equation(3.35), printed p71, states
psi(x)<1.03883x for every real x>0, where
psi(x)=sum_(n<=x) Lambda(n), including prime powers.
The [primary paper scan](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf)
was inspected at the theorem and its proof routing: pp77-78 separate
the finite ranges from x>10^8, and p80 completes the latter using
TableI after its justification. This is an unconditional theorem
import, not a new replay of those tables. A future application may
use Abel summation with n^(-1/2) to bound L744's complete coefficient
mass. It must treat the strict cutoff n<exp L conservatively and
retain the factor two; no weighted-sum bound is proved this turn.

Plancherel and its derivative identity for smooth zero extensions,
and Abel summation for a finite arithmetic sum, are standard named
inputs. No new zero-free estimate, RH assumption, or three-cell
computer certificate is needed. Full matching Mathlib coverage of
this moving-support statement is unchecked; supporting Fourier facts
are not a formalization of the whole result.

### Quantitative obligations located, not discharged

The complete L744 proof and its step289 audit were read. Its formulas
give a more useful prospective route than substituting into its
fixed-K big-O statement. Record the following exact locations for the
later attempt; they are a source comparison, not a proof of extension.

- L744(5)-(7) use smooth-domain membership and exact finite-square
  pole cancellation for each finite window. L740(3)-(5) allows every
  finite L. Check this pointwise finite-L argument along K(t); no
  operator or infinite-window limit is required. Growing global
  exponential weights must multiply exact zero moments, never
  approximate zero moments.
- L744(8)-(11) display the symbol bounds, fourth-moment estimate,
  a(T) and U(T). Their written parameters are T,M and scalar A;
  any hidden support dependence must be excluded before use.
- L743(9)-(10) fixes one invertible two-by-two matrix on the cell.
  L744(12)-(14) uses squared sums over disjoint cell supports and
  defines R_chi,H,delta,b(T). The displayed constants involve
  ell,M,chi, not a sum of K identical worst-case errors. The
  corrected-family attempt must retain that precise square-sum
  argument, not assume uniformity from its label.
- L744(15)-(17) locate the denominator restriction delta<=1/2,
  its norm-defect term multiplied by |c_T|, and the explicit
  admissible error. Track these rather than deleting the latter
  term or substituting K(t) in O_(K,M,chi)(1/T).
- L744(2) and the final arithmetic payment are the explicit
  window-dependent sum. Compare it quantitatively with the
  remaining half-log margin using the cited unconditional psi
  bound and the stipulated floor relation. Do not use only prime
  n, half its coefficient, or the much larger semigroup norm
  bound L740(7) as though it were the exact quadratic energy.

There is adequate coverage to attempt these application checks;
there is no inspected theorem licensing the final uniform quantifiers
without doing them. A canonical proof, if obtained next turn, should
cite the external psi theorem and L744's explicit estimates, explain
why the changed quantifiers are valid, and classify this as
REPRODUCTION. No new lemma or mathematical script was written here.

### Decision and bounded test

Continue with exactly the saved TARGET. The decisive evidence sought
is one paid lower bound with a single eventual onset depending only
on fixed M,chi, valid for both signs of t, every admitted w and the
prescribed K(t), together with a uniform nonzero denominator. Stop the
attempt if an unpaid K-dependent term prevents the half-log margin;
save that specific obstruction without asserting a violating Weil
vector. A failed sufficient estimate is not a disproof of the target.
Changing the rate, family or norm requires another assessment.

The prospective downstream use is a paid high-carrier portion of a
growing neutral block. Bounded carriers, general envelopes, non-neutral
components, signed cross terms and all-window assembly remain separate
gaps. No justified creative central-sign target is prepared by this
review: the available mechanism is standard high-frequency payment,
and an independent favorable estimate on the remaining block is absent.
This is a reason for honest specialization routing, not a global ban
on discovering a new central mechanism. No exploration counter resets.

## Original step494 nomination context, retained

The main gap remains L030–L032/C032a actual-Xi positivity. A positive
high-frequency margin with support increasing explicitly with frequency
could pay a growing-window portion of that gap. It would leave bounded
frequencies, unrestricted profiles, non-neutral components and all-window
assembly unresolved. A support-dependent finite theorem alone would not
justify applying a fixed-K limit along this family.

The nominated bounded test for a later approved attempt was whether the explicit
L744 correction and complete prime cost admit the displayed half-log
margin with one onset depending only on M and chi. Continue only with
a uniform, proved error comparison and nonvanishing v; otherwise record
the specific unpaid K-dependent term, without calling a failed sufficient
bound a negative Weil vector. Changing K(t), the family, or denominator
would be a new target requiring review. Do not derive a different rate
and approve it during that review.

This does not reopen absolute summability: retain
`ATTEMPTS/2026-11-04-neutral-cell-summability-conditional-stop.md`
and L742's RH-conditional obstruction. It also does not reuse the false
exact corrected-IMS inequality stopped in
`ATTEMPTS/2026-11-04-fixed-corrected-ims-propagation-stop.md`.
The old positive-Toeplitz factorization prerequisite is recorded in
`2026-11-04-neutral-cell-coherent-mechanism-discovery.md`; it cannot supply
an unconditional sign. L743's prime-only supremum equality and L744's
paid full-energy modulation are the relevant existing local mechanisms.
No cross-notebook input is proposed.

The nomination described established-route uniformity, not a justified
creative central mechanism. The three-cell target duplicates an existing
source theorem; the quantitative regime was unassessed at step494.
The completed comparison above supplies coverage for a bounded attempt,
without claiming that the extension is already proved or novel.
