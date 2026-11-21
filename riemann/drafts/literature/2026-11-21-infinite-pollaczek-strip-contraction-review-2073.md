# Infinite actual-theta Poisson deformation — source review2074

TARGET: Assess whether Romik's infinite actual-theta Meixner–Pollaczek Poisson deformation admits a zero-strip contraction toward r=1, with explicit direction, analytic domain and endpoint hypotheses.
CHECKED: 2026-11-21
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Step2074 reused assessment2070 and the October21 baseline; searched the exact infinite Pollaczek/Poisson/strip terminology and stronger operator results, and checked local finite and endpoint stops. Primary Romik, de Bruijn and Branden--Chasse comparisons were read. The previously parked Koide lead resurfaced; its local access/scope record112 was reused without another access campaign. Queries and read limits below; no novelty inference.
SOURCE_EVIDENCE: Romik1902.06330v3 Theorem3.1/(3.4)-(3.5), Section3.2 concluding proof, Theorem3.6/(3.21)-(3.23)/complete proof, Theorem3.7/(3.24)/complete proof and finite Theorem3.8/Proposition3.9; de Bruijn1950 pp204-205 Theorems10-14 and proof13, with exact Gaussian normalization corroborated in Dobner2005.05142v2 Section2 Theorem3; Branden--Chasse1402.2795v2 Theorems1.6-1.8 and proof1.8. Primary links and qualifications below.
COMPARISON: The inspected infinite family is entire for 0<r<1, and r=1 is the actual Xi endpoint. Its DDE is not the heat equation: the Mellin kernel undergoes a fractional-linear argument/support change. De Bruijn's fixed-kernel Gaussian multiplier and the inspected constant-coefficient strip operators therefore supply no direct contraction import. L530/C530b remain finite contrasts, not infinite counterexamples. A fixed-r eventual-reality claim would leave compact exceptions and r-uniformity unpaid.
GAP: No actual-orbit initial global strip, quantitative transport toward r=1, shrinking-to-zero width or parameter-uniform endpoint zero control is verified. Koide's potentially adverse endpoint theorem still lacks primary coverage under the preserved block112. Neither its truth nor the nonexistence of an actual strip law is concluded.
REASON: The new source comparison rejects the proposed direct Gaussian/strip-operator import, without proving a mathematical no-go theorem. No independent precise estimate with a bounded actual-input test emerged. Park this dependent strip mechanism and retain block112; nominate materially different bounded non-flow discovery at the central mixed-form gap. This completed review approves no dependent mathematics.
SCOPE: Completed literature-only comparison2074; source identities and hypothesis matching only, no new lemma, specialization proof, script, zero count or all-degree conclusion.
LITERATURE_REASON: Essential scope changed from the ready fixed-degree finite audit to infinite actual-input transport. This single source step fills the primary domain/operator comparison, while preserving the existing inaccessible endpoint lead rather than retrying it.

## Original nomination2073 — retained scope and decision test

Main gap: full RH, represented locally by L030-L032/C032a's actual-Xi
all-degree mixed positivity. Seek a source-supported analytic mechanism
for the infinite actual-input family rather than further finite tests.
The proposed notation is

    F_r(t)=sum_(j>=0) (-1)^j (c_(2j)/c0) r^(2j)
           P_(2j)^(3/4)(t/2;pi/2).

This specifies the object to assess; its convergence domain, parameter
range and any continuation must be read from the primary sources.
No global definition away from the proved domain is assumed. At the
undeformed endpoint the source's actual Xi normalization is essential.
The proposed strip is about the real t axis, i.e. |Im(t)|<=w; strip
control at one r must not be inferred from finite truncations.

Plausible downstream use: a quantitative law shrinking a justified
initial strip as r increases to 1 might provide an alternative to the
failed finite initialization. An initial infinite-family strip, a
law with the correct direction, and a justified endpoint limit would
still be independent obligations. Neither a generic conditional law
nor convergence is RH. This source turn must not derive the law or
assume a zero-width endpoint as an input.

Before proposing a zeta zero-free consequence, read the local GOAL's
required baseline `2026-10-21-openai-quasi-rh-overlap.md` under
`drafts/literature/` and `foundations/2026-10-quasi-riemann-input.md`.
Search only narrowly relevant local infinite-Poisson/strip-contraction
claims and failures, then retrieve primary theorem hypotheses and
essential proof cases for Romik's infinite deformation and any relevant
de Bruijn comparison. Distinguish a heat multiplier from the Pollaczek
diagonal multiplier; a theorem for one is not automatically a theorem
for the other. Reuse adequate existing source reads and precise
citations. Do not reopen the parked Koide source-access campaign.

Continue only if the review identifies a precise applicable theorem or
a concrete missing estimate with a bounded independent test. A direction
mismatch, absent endpoint control, or merely a finite/heat-flow theorem
must be recorded explicitly. If no independently testable specialization
emerges, abandon this mechanism and nominate bounded discovery at the
main gap; do not convert it into a radius/degree/precision sweep or
another coefficient audit. Missing or inaccessible essential hypotheses
mean SOURCE_BLOCKED, without dependent mathematical work.

Essential local inputs for comparison: audited C530b, L530 and the
reused actual coefficient normalization C530a; these are contrasts or
normalization evidence, not premises asserting an infinite strip.
Independent gaps include all-degree signs, an actual invariant and
Xi transfer. Mathlib coverage for the proposed mechanism is unchecked.
No cross-notebook input. This new nomination must receive its separate
literature approval next turn. It is not a creative proof attempt yet.

## Completed comparison — 21 November 2026, step2074

Outcome NEGATIVE, LITERATURE/literature_comparison, NOVELTY_UNCHECKED.
The informative result is a source-applicability mismatch, not a new
theorem or a refutation of the actual family. The nomination above is
historical; the fields at the top record the completed decision.

### Exact primary inputs and scope

Dan Romik, *Orthogonal polynomial expansions for the Riemann xi function*,
[arXiv:1902.06330v3](https://arxiv.org/html/1902.06330v3), 5 May2019:
Theorem3.1 identifies the undeformed series on all complex t, with compact
remainder bound (3.5). Theorem3.6 gives, for 0<r<1 and every complex t,

    X_r(t)=integral_0^infinity omega_r(x) x^(-3/4+it/2) dx,
    eta=(1-r)/(1+r),
    omega_r(x)=(1+eta)/sqrt(1-eta) /sqrt(1-eta*x)
               *omega((x-eta)/(1-eta*x))  if eta<x<1/eta,
               0 otherwise.

The complete proof uses the coefficient integral, generating function,
then the displayed fractional-linear substitution. It explicitly notes
bounded Fourier support and exponential type. Theorem3.7, with
M(tau,t)=X_exp(-tau)(t), gives for tau>0 and complex t

    M_tau=3M/4 -(1/2)(3/4-it/2)M(tau,t+2i)
                    -(1/2)(3/4+it/2)M(tau,t-2i).

Its proof uses the basis difference equation termwise. Theorem3.8's
zero ODE instead assumes a finite monic polynomial with distinct roots
locally in time; it is not an infinite zero-product theorem. The complete
Proposition3.9 example is a generic polynomial contrast, reported by a
numerical root calculation; no new certification of it is claimed.

Here F_r=X_r/c0, using the same coefficients and basis, with c0>0 from
C530a. This is only identification of the nominated notation with the
source, with no change of zero set. Increasing r means decreasing
tau=-log r toward zero. No assertion for r>1 is imported. The r=1
identity is (2.48)/Theorem3.1; the compact estimates are relevant to a
later endpoint-limit argument, but do not supply a global zero strip
or a shrinking width. No new dominated-series or Hurwitz proof is made.

N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math.J.
17(1950),197-226, [institutional scan](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da),
Theorem10 p204 assumes integrability, Hermitian symmetry
K(u)=conj(K(-u)), and K(u)=O(exp(-|u|^b)) for some b>2.
Theorem13 p205: if every zero of G(z)=integral_R K(u)exp(izu)du
lies in |Im z|<=Delta, multiplying K by exp(lambda^2*u^2/2),
lambda>0, puts every zero in
|Im z|<=sqrt(max(Delta^2-lambda^2,0)). Positivity is not required.
The proof approximates the multiplier by
cosh(lambda*u/N)^(N^2), applies Theorem12, and uses a Gaussian majorant
and compact transform convergence. Theorems11-12 distinguish all-zero
and all-but-finitely-many variants; they cannot erase an unspecified
compact exceptional set for the actual family.

The original extracted text has mangled superscripts; screenshot calls
returned image markers only, and a local unauthenticated download failed
DNS. Exact normalization was therefore checked against Alexander Dobner,
*A proof of Newman's conjecture for the extended Selberg class*,
[arXiv:2005.05142v2](https://arxiv.org/html/2005.05142v2), Section2,
Theorem3, explicitly citing de Bruijn Theorem13. It states the same
hypotheses and width sqrt(max(Delta^2-2a,0)) for the multiplier
exp(a*u^2), a>0. Only this readable theorem statement is used; no
Selberg-class application or proof audit of Dobner's main theorems.

Petter Branden and Matthew Chasse, *Classification theorems for operators
preserving zeros in a strip*,
[arXiv:1402.2795v2](https://arxiv.org/html/1402.2795v2), 29June2016,
Theorems1.6-1.8: the stronger inspected contracting operators have constant
differential coefficients and a specified half-plane-stable symbol.
For Theorem1.8, T=h(D)exp(i*lambda*D), with h in the compact closure of
polynomials nonvanishing in the lower half-plane, and T+T* acts on real
polynomials with all zeros in the starting strip. The proof uses shifted
half-plane stability and the conjugate-sum lemma. We read that proof;
its cited stability lemmas/theorem are not independently reaudited, since
no application passes the operator-identification requirement. No
transcendental extension or stability of a Pollaczek symbol is assumed.

### Hypothesis comparison and decision

The source's fractional-linear change of kernel argument and its
parameter-dependent support have not been identified with multiplication
by a Gaussian on a fixed Fourier kernel. The DDE's t-dependent factors
also do not meet the inspected constant-coefficient operator hypothesis.
Calling both constructions a Poisson flow does not establish that
identification. Even a valid strip theorem would require a justified
initial strip for this actual deformed orbit, the correct r direction,
and a bound tending to zero at the actual endpoint. None is supplied by
the cited results. This is a failure of the proposed citation shortcut,
not a derivation that every possible actual-orbit contraction is false.

The October21 baseline/register was read as required. Its cited fixed
undeformed-Xi strip is not a common strip for X_r. No new zero-free
consequence, heat-time bound, or reassessment of L330/L331 is attempted.
L530's audited two-atom finite counterexample and C530b's audited actual
sextic counts have exactly their canonical scopes; they are not premises
about infinitely many coefficients. C530a's trust assumptions are not
replayed or silently upgraded. Mathlib matching coverage is unchecked.

The targeted search resurfaced post49's Koide reference and an author's
fixed-r eventual-real/simple claim. They remain unread theorem leads,
not inputs. The already inspected local assessment111/block112 records
the missing primary endpoint theorem and exact normalization/quantifier
issues. That source-access campaign was not reopened. Fixed-r eventual
reality alone would also leave compact exceptions and no uniform
r-to-1 bound. These facts prevent approving dependent research; the
persistently blocked endpoint route is parked, not repeatedly scheduled.

Queries included `Romik Meixner Pollaczek Poisson flow zeros de Bruijn
strip contraction`, `de Bruijn 1950 roots trigonometric integrals strip`,
`"Meixner" "Poisson" "strip" zeros Romik infinite`,
`"Romik" "Poisson flow" "zeros" infinite real simple`, and
`"Meixner-Pollaczek" "strip" "preserving"`. Narrow local searches
selected assessment2070, the October30 moment-flow comparison, the
November17 exponent/strip comparison1324, and endpoint scope111/block112.
Secondary hits and search snippets are leads only; no conclusion of
novelty or exhaustive nonexistence follows. No mathematical script ran.

Decision: abandon the direct infinite-Pollaczek strip-import mechanism
for now. Reopening requires materially new primary evidence or a precise
actual-input estimate with an independent bounded test. It does not
authorize a radius/degree/precision sweep, another coefficient audit or
another Koide access campaign. The next nomination is bounded non-flow
discovery at L030-L032/C032a, with essential coverage REVIEW_REQUIRED.
