# Coffey b_n transform — primary comparison completed, step205

TARGET: Assess Coffey arXiv:0912.2390v1's b_n transform for convergence and inversion bounds sufficient to transfer a one-sided subexponential estimate back to ordinary Li coefficients without RH.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact title, arXiv identifier with convergence/correction, Li coefficients with binomial/b_n/convergence/inverse, and Taylor/one-sided growth; followed reference[11]. Exact notebook searches found no matching inverse audit beyond step204's nomination. No novelty or absence claim.
SOURCE_EVIDENCE: Coffey arXiv:0912.2390v1, printed pp2-7/(1.1)-(1.3),(1.10)-(1.12), Proposition1/(2.1)/proof(3.1), Proposition6/Corollary7/Proposition7, relevant proofs pp12-15/(3.27)-(3.37), references pp19-20; He-Jejjala-Minic arXiv:0903.4321v2, p8/(3.2)-(3.4) and p14/Section3.3/(3.31); NIST DLMF1.9.30-31,1.9.48,1.9.63,1.10.1,1.10.4,4.6.7, version1.2.8. Reused L968's inspected Lagarias criterion and normalization.
COMPARISON: Local coefficient definitions and a stated positive-weight inverse are available; the displayed useful asymptotic is RH-conditional. The inspected sources do not supply the required unconditional actual-b_m lower bound. Standard analytic tools support checking the interior inverse separately.
GAP: Verify an unconditional recentered radius R>1, consistent logarithm and complete inverse differentiation; quantify a sufficient near-2^-m lower-tail condition. Even a successful transfer leaves the actual-b_m bound independently unpaid.
REASON: Reject direct source payment; retain one bounded interior-inverse specialization/audit. Its newly written assessment receives separate approval before research. No mathematical result is derived here.
SCOPE: Actual xi, ordinary Li coefficients and all zero multiplicities; no RH, simple zeros, radius2 assumption, ordinate replacement, numerical inference, forward infinite exchange or assumed signs. SPECIALIZE covers identified tools and comparison, not a proved transfer.
LITERATURE_REASON: Startup REVIEW_REQUIRED demanded unread primary convergence/inversion passages. This turn resolves that comparison without reopening the blocked2007 retrieval.

## Main gap, test and downstream role

L030-L032/C032a actual-Xi all-degree positivity remains open, including
L966's R_n<=N_n and unconditional signed cumulative forcing. This
turn's intermediate target is exactly the source comparison above.
A certified inverse could later transfer an independently proved
transformed lower bound to L968's every-epsilon Li threshold. L974's
paid eta error supplies neither that bound nor initialization signs.

Continue if the primary formulas isolate an unconditional interior
inverse and a separately testable tail requirement. Abandon direct
import if the sufficient estimate assumes RH or uses an unpaid
convergence domain. The evidence below stops direct import but leaves
one interior audit justified. No mathematical obstruction is proved.

## Inspected primary statements and essential proof cases

[M. W. Coffey, *On certain sums over the nontrivial zeta zeros*,
arXiv:0912.2390v1, 12December2009](https://arxiv.org/pdf/0912.2390v1)
defines the ordinary lambda_n in (1.1) and the two local expansions

    F(z)=log xi(1/(1-z))
        =-log2+sum_(n>=1) (lambda_n/n)z^n
        =b_0+sum_(m>=1) b_m(z+1)^m.                 (source1.3)

The domains follow (1.3), pp2-3. Equation(1.11), p4, is an infinite
alternating forward transform. Proposition1's proof (3.1), p7, invokes
convergence of the zero sum to exchange an additional infinite index.
Proposition6, Corollary7 and Proposition7, p7, explicitly assume RH;
the relevant proof passages pp12-15 reuse real-ordinate formulas and
binomial sums at unit complex arguments. No unconditional inverse
inequality was recovered there. Proposition4's proof invokes the
blocked2007 reference[8], which is unnecessary for the local audit.

Our applicability judgment: a finite orthogonality identity is not a
joint convergence bound for the forward exchange. We do not import it
as one. This identifies an unpaid justification, not a proof of
divergence or a refutation of the zero formula. Its independent
verification would require separate work. The advertised asymptotic
is not available as an unconditional payment; no certification of its
conditional proof is asserted. Companion zeros and multiplicities
cannot be silently omitted.

Coffey reference[11], [Y.-H. He, V. Jejjala and D. Minic, *Eigenvalue
Density, Li's Positivity, and the Critical Strip*, arXiv:0903.4321v2,
22April2009](https://arxiv.org/pdf/0903.4321v2), printed p8/(3.4), states

    lambda_n/n=sum_(m>=n) binom(m,n)b_m, n>=1.       (source3.4)

Their k_n is ordinary lambda_n. The preceding radius2 assertion is
not adopted. Section3.3, p14, explicitly qualifies the later positivity
formulas (3.31) as formal manipulations of divergent series, leaves
rigorous validity open and discusses implicit RH.

Our applicability judgment: those warnings block importing the later
positivity claim. They do not themselves refute the interior identity.
The audit should cite the known formula while verifying a smaller
RH-free disk, consistent logarithm and complete-sum differentiation.
A reproof of Taylor's theorem or a novelty claim for inversion is
unjustified; local verification is justified by the source's unpaid
domain assertion. A radius for the composition alone cannot simply
be used as a radius for its logarithm without excluding zeros.

[NIST DLMF1.9(vi)/(1.9.48),(1.9.63)](https://dlmf.nist.gov/1.9.vi)
gives compact-subdisk absolute uniform convergence and differentiation
inside the radius. [1.10.1](https://dlmf.nist.gov/1.10.E1) assumes
analyticity on the disk. [1.9.30-31](https://dlmf.nist.gov/1.9.E31)
requires analyticity inside a positively oriented simple contour and
continuity on it. [1.10.4](https://dlmf.nist.gov/1.10.E4) and
[4.6.7](https://dlmf.nist.gov/4.6.E7) give binomial expansions for
|z|<1. Version1.2.8, release15September2026. These tools license no
boundary substitution or actual coefficient sign. The remaining
specialization is reserved for the proposed audit, not done today.

## Local reuse, duplicates and limits

L024/L026 supply actual paired-zero summability/localization; L964
and audited L968 fix ordinary Li normalization and the downstream
all-index/every-epsilon criterion. Reuse L968's precise Lagarias,
AIF57(5)(2007), Theorem2.4(2)/(2.21), pp1702-1703, including its zeta
normalization, and the step172/173 audit assessment. Reuse step163's
analytic-tool coverage. Neither source criterion is reproved.

Scoped searches in lemmas/, foundations/, drafts/literature/ and
ATTEMPTS/ for exact arXiv identifiers, author combination and binomial
inverse terminology recovered no matching earlier b_n audit. The
finite Spira coefficient-norm and displaced spatial inverse-recovery
assessments treat different observables. Step200's Fejer source limit,
L967/L971 comparisons and L973's RH diagnostic are preserved; none
supplies this inverse or an actual-b_m lower bound. No sibling notebook
was read. No new zero-free region or reciprocal continuation is proposed,
so the notebook's external-region baseline is not needed for this step.

Queries included the exact title with inversion/convergence,
`Coffey b_n convergence Li`, `0912.2390 convergence binomial`,
`Li coefficients binomial b_n convergence`, `Li coefficients Taylor
one-sided growth`, and `Coffey 0912.2390 correction convergence`.
Other hits (AI-written notes, bibliographies, numerical Arb examples,
claimed proofs) were not used as theorem evidence. No stronger
applicable unconditional estimate was recovered; this is not an
exhaustive literature or novelty conclusion. Primary PDFs were
accessible in the web reader despite shell DNS failure.

Full Mathlib coverage of the transform-with-one-sided-bound statement
is unchecked/unknown; no Mathlib theorem is imported.

Outcome: NEGATIVE source applicability evidence. Direct source payment
fails on the inspected conditional hypotheses and explicit formal
qualifications, not on a new mathematical obstruction. No mathematical
progress beyond checked sources, lemma or script is claimed. The
interior audit is nominated in `2026-11-10-bn-local-inverse-audit-review-205.md`;
its new coverage requires separate approval before research. A creative
central attempt lacks an identified unconditional actual-b_m lower-bound
mechanism; do not relabel routine analytic specialization as creative.
