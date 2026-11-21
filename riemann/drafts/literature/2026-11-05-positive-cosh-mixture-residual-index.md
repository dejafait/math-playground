# Positive cosh-mixtures and the residual signed form — completed source review

TARGET: Assess whether a positive cosh-mixture representation of G supplies a noncircular signed-form bound for the exact r=3, two-real-interior-zero J-Q beyond L783's local-factor premises.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step451 searched positive cosine/cosh transforms, factorial-normalized Stieltjes/Toeplitz positivity and reciprocal Loewner/negative-square terminology; inspected Csordas 1309.0055v2's exact hypotheses and relevant proof cases, a directly relevant preprint passage, and DLMF elementary interfaces; reused ready moment/PF and signed-index assessments. No matching paid r=3 index theorem or exact counterexample was located in this bounded search.
SOURCE_EVIDENCE: Csordas 1309.0055v2 Definition1.2 p.2, Remark2.1 p.3, Theorem3.5/Lemma3.6/Theorem3.7 and proofs pp.6–8, Example3.12 p.9; ready Wang–Zhu 1612.04114v1 Theorem2.3 pp.5–6, Karlin–Proschan–Barlow (1961) Theorem3 p.1027, Berkolaiko–Kuchment (2022) Theorem2.7/proof pp.88–91; exact source links and qualifications below.
COMPARISON: Existing L019–L021/L776 give the positive-mixture normalization for actual G, but the inspected sources do not identify its reciprocal Taylor tail with a signed form of controlled index. Associated-kernel positive definiteness, a PF density, global finite-negative-square membership and a controlled Schur remainder are extra premises. No exact r=3 implication or counterexample is imported.
GAP: The independent reciprocal-tail sign/index and strict nullity payment remain missing. Positive moments concern the original G; no inspected theorem transfers them through reciprocal factors, root removal and projection to J-Q.
REASON: Park the automatic positive-mixture-to-index import without declaring the implication false. An exact finite atomic-mixture diagnostic is independently testable and differs from L783's non-moment quartic and L773's Turan grid; nominate it for separate source approval, with no tuning or sign assertion here.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target adds a global positive-measure premise absent from the ready local reciprocal-factor comparison; its transform/moment hypotheses and actual normalization required essential new comparison.
SCOPE: Completed literature-only step451 for r=3 with two distinct simple negative interior zeros and locally zero-free F. No new bound, model admissibility, index calculation, lemma or mathematical script. This review does not approve a creative sign mechanism; the separately nominated fixed-model target is REVIEW_REQUIRED.

## Invocation-start proposal and bounded comparison, retained

Consider G(z)=integral_[0,infinity) cosh(t sqrt(z)) dmu(t), where
mu is finite, positive and nonzero and integral exp(A t)dmu(t)<infinity
for every A>0. The integrand is its even entire power series, so there
is no choice of square-root branch in this notation. Applicability of
this premise to the actual normalization remains a source/lemma check,
not a new conclusion of step450. The equivalent factorial-restored
moment convention and all limit interchanges must be checked in the
next review rather than assumed here.

Use the complete b=p/F, c=F/p, residues, one-based Q_3 projection and
the h_3,K,E,J,Q definitions in L783, with the prospective G replacing
the quartic and with its own two real interior roots and grouping
already supplied. Do not import L783's computed entries into that
different G. The target is an independently paid quadratic-form
constraint implying n_0(J-Q)=0 and n_-(J-Q)=n_-(J), or a precise
source obstruction to that implication. Merely embedding J-Q into a
Hermitian block or invoking positivity of a different moment matrix
does not establish the target. Global real-zero assumptions or an
RH-equivalent positivity premise are inadmissible shortcuts.

First compare exact primary statements in at most three relevant
families: cosine/cosh transforms of positive measures, factorial-moment
Hankel representations, and signed finite-rank/Schur forms. Search the
active notebook's specific corresponding assessments for duplicates
before external search. Retrieve theorem hypotheses and relevant proof
cases before larger passages. A theorem giving only a conditional
remainder sign must retain that sign as an unresolved assumption.
An explicit inspected counterexample can stop the generic implication;
an unanswered search permits no mathematical claim or novelty inference.

Continuation test: approve a creative proof attempt only if the review
identifies an explicit, independently testable integral or residual-form
identity with a credible sign/index payment not excluded by the recorded
stops. Otherwise record the exact missing premise or counterexample and
choose a materially different target. No new creative attempt is approved
here, and this source turn must not be used to derive and approve its
previously uncovered mathematics simultaneously. The completed quartic
result remains valid local progress regardless of this future gate.

## Completed comparison — step451, 2026-11-05

The main gap is actual-Xi all-degree mixed positivity. A paid local
index/nullity estimate would sign one exceptional determinant; arbitrary
orders, radii, root groupings and other mixed minors would remain open.
The discriminating source test was an independently controlled form,
not positivity of a different matrix. It was not met by the sources
checked. This is bounded EXPLORATION, not a disproof of the implication.

### Normalization already present in the notebook

Read complete L019–L021 and L776's displayed coefficient normalization.
Their existing formulas agree with the proposed measure notation by
taking mu to be one eighth of the pushforward of K(u)du under u -> u/2:
the moments are M_(2n)/(8*4^n), and L776's a_n divides these by (2n)!.
Finiteness and every exponential majorant are supplied by L019; the
locally uniform series/integral exchange is already proved in L020/L021.
There is no branch choice or missing factor of eight. These are checks
of established conventions, not a new representation theorem or sign
estimate. All exponential moments by themselves impose no stated
order-one-half bound on arbitrary prospective measures.

### Three source families

1. **Positive transforms.** George Csordas,
   [*Fourier transforms of positive definite kernels and the Riemann
   xi-function*, arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
   21 February 2014. Definition1.2 p.2 requires smoothness, positivity,
   evenness, strict decrease and super-Gaussian decay of every derivative.
   Theorem3.5, Lemma3.6 and Theorem3.7/proofs, pp.6–8, additionally use
   strict log-concavity: the associated kernels are
   K_n(t)=integral_R phi(s+t)phi(s-t)s^(2n)ds. Membership of the transform
   in Laguerre–Polya is equivalent to positive definiteness of every K_n.
   The proof cases read include the split s<t/s>t monotonicity argument,
   the double-integral change of variables and Jacobian, and the final
   Fourier/Laguerre comparison. Positivity of phi is not that additional
   positive-definiteness condition. Example3.12 p.9 has positive
   phi(t)=exp(-t^2)(15+t^2+t^4) and a transform with four nonreal zeros;
   it expressly fails Definition1.2(v). It has all exponential moments,
   but does not supply this target's two-real-root grouping or J-Q
   inertia. Remark2.1 p.3 uses k!-restored coefficients for its Turan
   conclusion. No such coefficient convention is substituted for a_n.

2. **Factorial moments and Hankel/PF structure.** Reuse the ready
   `2026-11-04-moment-compatible-turan-minor-comparison.md`, including its
   inspected proofs and repeated-parameter cases. Yi Wang and Bao-Xuan
   Zhu, [1612.04114v1](https://arxiv.org/pdf/1612.04114v1), Theorem2.3,
   pp.5–6, concerns a_k a_(k+2)-a_(k+1)^2 for raw Stieltjes moments;
   it does not cover this factorial-normalized reciprocal tail. Samuel
   Karlin, Frank Proschan and Richard E. Barlow,
   [*Moment inequalities of Polya frequency functions*](https://msp.org/pjm/1961/11-3/pjm-v11-n3-p20-p.pdf),
   Pacific J. Math.11(3) (1961),1023–1033, Theorem3/both proof directions
   p.1027, equates a PF-infinity density on the nonnegative axis with
   PF-infinity of its full moments divided by n!. A positive measure
   alone is insufficient as a theorem hypothesis; our even moments and
   (2n)! cannot be relabeled full moments and n!. The same assessment's
   Belton–Guillot–Khare–Putinar 2101.02129v2, Theorem1.6 and moment proof
   pp.16–18, concerns a special Hirschman–Widder density. None identifies
   a measure representation for h_3 or pays the signed projection.

3. **Finite-rank and signed forms.** Reuse the ready
   `2026-11-05-linked-factor-hermitian-realization-review.md` and
   `2026-11-05-reciprocal-quartic-inertia-test.md`. Gregory Berkolaiko and
   Peter Kuchment, [*Spectral shift via lateral perturbation*](https://ems.press/content/serial-article-files/33861),
   J. Spectr. Theory12 (2022),83–104, DOI10.4171/JST/395,
   Theorem2.7/proof pp.88–91, retains selfadjoint blocks, domain and
   kernel/range conditions, finite relevant indices, and the remaining
   Schur-complement index/nullity. Its invertible congruence does not
   estimate that remainder. Ready de Boor/Duits interfaces identify
   divided differences and transfer a finite-rank determinant only.
   L782 supplies the actual projection weights; L783 shows that keeping
   the linked local factors does not alone pay the index. No source
   asserts that adding a positive cosh-mixture makes these remainder
   conditions automatic. Global generalized-Nevanlinna membership is
   still an unproved extra premise, as the ready step443 review records.

### Duplicates, search limits and a directly relevant lead

Read the relevant statements/qualifications of L530/L565/L738/L772/L773
and the complete L783 calculation; no certificate replay was needed for
this source question. L530 is a finite Pollaczek flow; L565 is a failed
diagonal Hermite-CD cone; L738 concerns a Fourier critical minimum;
L772 does not realize a positive moment measure. L773 excludes its
particular two-atom grid under a *joint* order-five-minor/Turan target,
not under the present order-three residual test. None settles it.

The ready `2026-11-04-actual-theta-signed-compensation-review.md` already
parks generic direct compensation without an independently controlled
remainder. Rephrasing that desired sign as a new integral bound would
repeat this stop. Likewise, the ready signed-rank-two assessment records
substantial known low-order actual-Xi nonnegativity; an atomic diagnostic
would test generic sufficiency, not discover actual-Xi order-three signs.

Queries used: positive cosine transform/kernel/real zeros/counterexample;
Stieltjes moment/factorial-normalized/even moments/entire zeros/total
positivity; reciprocal entire cosine transform/Loewner/negative squares;
cosh/Toeplitz/moment positivity; positive measure/cosine transform/negative
squares; cosh/Loewner/reciprocal; cosh/minor/Polya. Irrelevant results,
secondary mirrors and snippets were not used as theorem evidence.

One directly relevant search lead was Avi Gershon,
[*The De Bruijn–Newman Constant Is Zero*, v1](https://www.preprints.org/manuscript/202604.1513),
posted 22 April2026, unreviewed. The relevant passage inspected was
Remark20/(56): its positive-cosh-integral paragraph concludes g(z)>0 for z>0;
it does not state a bound for this prescribed reciprocal J-Q. Its claimed
global resolution and later computational/inductive argument are
**UNVERIFIED external claims**, not an imported theorem, independently
audited candidate, or reason to change notebook status. Neither those
later proof cases nor the cited Schoenberg theorem were audited here;
the adjacent conditional remarks were not used as independent bounds.

DLMF [4.28.2](https://dlmf.nist.gov/4.28.E2) and
[4.35.2](https://dlmf.nist.gov/4.35.E2) were read as elementary
exponential-definition/addition interfaces within the transform family.
They suggest an explicit finite atomic diagnostic; no new product
identity, root list or index has been derived from them in this turn.

No exact paid bound or exact residual counterexample was found. No
novelty or nonexistence follows. Full matching Mathlib coverage for the
requested bound remains unchecked. No inaccessible essential source
was used to support the decision; the general implication remains open.

### Route and continuation

Park automatic source import from the positive measure. No creative
proof attempt is justified yet: neither an independent signed-form
identity nor credible sign/index payment was identified. This is a
source-coverage/mathematical-mechanism limitation, not a global ban on
positive integral methods.

Nominate the one fixed atomic diagnostic in
`2026-11-05-fixed-atomic-cosh-residual-index-test.md`. It introduces no
parameter sweep and must certify its own two-root grouping and complete
series before reporting inertia. Failure would refute the exact added-
premise implication; a matching index would only clear this one model
and would not justify a generic or Xi bound. Close the model after the
single test either way, without tuning. Its new target requires separate
source approval before mathematics. No mathematical exploration budget
was spent by this literature turn.
