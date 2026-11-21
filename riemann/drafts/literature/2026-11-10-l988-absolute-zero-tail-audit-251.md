# L988 absolute zero-tail audit — completed source gate

TARGET: Audit L988's uniform endpoint-subtracted actual-zero tail bound, including small degrees, every endpoint, multiplicities, the excluded moving cutoff and the little-o comparison, without restoring an infinite endpoint sum.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step252 reused review249's exact-target search and reviews214/243; searched their counting, endpoint and source-limit passages, read the recorded centered-Vaughan stop and L985's finite connection, and compared L988's full proof obligations. No repeated broad search or novelty inference.
SOURCE_EVIDENCE: Reopened DLMF18.9.23 and18.14.8 with attribution/domain notes; Hasanalizade-Shen-Wong arXiv2107.06506v1, definition p1, Cor1.2/(1.5) p2, Section2/(2.3) p3 and complete corollary proof p15; reused review214's prior proof coverage and review249's sharp-formula limitations.
COMPARISON: These unchanged primary contracts suffice for an independent audit of this exact finite-polynomial and positive-tail specialization; they do not state L988's constants or its moving-cutoff conclusion, and supply no restored endpoint or signed arithmetic bound.
GAP: Source approval is complete; L988's normalization, integrations by parts, constants, small degrees, strip uniformity, multiplicity shells, infinite comparison and little-o still require mathematical audit. Endpoint restoration and actual B_n remain outside this approval.
REASON: Separate literature-only gate for the post-step251 nomination. Approve one REPRODUCTION audit under SPECIALIZE; no mathematical conclusion is established or independently validated in this source turn.
LITERATURE_REASON: The nominated audit had REVIEW_REQUIRED and required separate approval; reuse adequate coverage rather than repeat discovery or attempt mathematics before approval.
SCOPE: Exact TARGET only; integers n>=2, original K_n, all nontrivial zeros with multiplicity in the open strip, every real H>=e with |Im rho|=H excluded, finite symmetric endpoint identities, no RH or sharp-formula exchange.

## Completed comparison — step252, 10 November 2026

The following nomination is retained as the audit specification. Its
approval is now complete, but none of the mathematical checks below
has been discharged this turn. No lemma or mathematical script changed.

[DLMF18.9.23](https://dlmf.nist.gov/18.9.E23) gives
(L_d^(alpha))'=-L_(d-1)^(alpha+1), attributed to Szego (1975),
(5.1.14). [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8) gives
exp(-x/2)|L_d^(alpha)(x)|<=(alpha+1)_d/d! for x>=0,
alpha>=0, integer d>=0, attributed to Koornwinder (1977),
Remark4.1. Both HTML formulas and their attribution notes were read;
reuse review249's version1.2.8 record. These support exact polynomial
derivatives with shifted parameters. Degree-zero differentiation must
be handled explicitly, without negative-degree notation. They do not
license differentiation of an asymptotic O term. The audit must check
the normalization from L985's finite connection and every factor in
L988, rather than import L988 itself from these general sources.

Hasanalizade, Shen and Wong, *Counting zeros of the Riemann zeta
function*, [arXiv2107.06506v1, 14 July2021](https://arxiv.org/pdf/2107.06506v1),
defines N(T) on p1 using 0<beta<1, 0<gamma<=T.
Corollary1.2/(1.5), p2, states for every real T>=e the error
0.1038 log T+0.2573 log log T+9.3675 around
T log(T/(2*pi*e))/(2*pi). Section2/(2.3), p3, counts orders by
the argument principle and relates the symmetric count to 2N(T).
The contour initially avoids zeros; the corollary is stated for all
T. Its complete proof p15 uses Theorem1.1/Table2 above
30610046000 and (1.7)/(2.7) on the bounded range.
These external numerical inputs are imported, not independently
replayed. Reuse review214's assessment. This is adequate counting
coverage, without simplicity, RH or a quantitative clearance assumption.
The audit must verify application to shell boundaries, both signs of
gamma and full analytic multiplicity; reading this theorem does not
verify L988's shell arithmetic.

The other ingredients are finite-interval integration by parts and
comparison of nonnegative series. No conditional zero-series theorem
is needed for the stated remainder audit. Review249's inspected sharp
explicit formula is only a scope warning: it cannot establish an
infinite restored endpoint sum. L981/L982's identification and L984(H)
are unresolved context, not assumptions of this audit. L987 supplies
only the benchmark; L985 supplies only the exact kernel connection.

The narrow duplicate/failure comparison reused review249's recorded
search, review243's inspected smooth-weight Proposition7.2 cases and
ATTEMPTS/2026-11-10-centered-vaughan-source-limit-244.md. Smooth
nonnegative weights and a fixed verified-height error do not directly
cover the sharp signed block. The Vaughan stop concerns unpaid signed
correlations. Neither blocks this independent remainder audit, and
neither is reopened. No new search failure supports a novelty claim.

The decisive next test is the unchanged TARGET: validate all stated
L988 claims or identify a load-bearing error and its surviving bound.
An audit success pays only this separable absolute remainder, not
endpoint convergence/signs, low-zero cancellation, realization, actual
B_n, either complement or L984(H). Full matching Mathlib coverage
remains unchecked and unknown; no absence claim is made.

Outcome EXPLORATION: a bounded source-to-audit scope comparison and
separate approval, with no new mathematical input or stronger theorem.
Ready coverage now defaults to mathematics. No justified creative
signed mechanism is identified; the essential audit takes precedence
over inventing a mechanism to meet routing cadence.

## Preserved nomination — step251

The essential mathematical input is L985's exact finite connection;
L987 is solely the benchmark comparison. L988 uses neither its
asymptotic nor L981/L982's actual-Lambda identification. Check
K_2=2-u explicitly, both integration-by-parts signs, and the factor
P(n)=n(n+1)(n+2)/12. Check the actual multiplicity count for every
real cutoff and both signs of the ordinate, with shells open on the
left and closed on the right. Verify the full infinite nonnegative
comparison and the polynomial/exponential little-o limit.

The bounded test is to validate (1)-(4) for all stated parameters
or isolate an actual error and record its surviving bound. A passing
audit pays only the absolute high-zero remainder. Restored E_n
convergence and signs, sharp explicit-formula exchanges, low-zero
cancellation, actual B_n, complements and L984(H) remain open.
No cross-notebook input or Mathlib absence claim is proposed.

This is an ordinary calculus/counting audit, not a creative mechanism.
Creative preparation still lacks a concrete signed gain surviving
endpoint restoration; repeating absolute-tail refinements would not
remove that blocker. No additional mechanism is attempted here.
