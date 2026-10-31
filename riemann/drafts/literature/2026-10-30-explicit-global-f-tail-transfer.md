# Explicit global F-tail transfer — completed source approval

TARGET: Specialize L493 and the cited de Bruijn strip theorem to obtain an explicit real/simple tail for F on 1/100<=lambda<=11/200, with cutoff R_0=(4*pi*exp(10000)+3)/2 and both spatial edges included.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused drafts/literature/2026-10-30-explicit-positive-time-tail-band-coverage.md and its source note; narrowly compared L488, L489, L492/L493 statements, L018/L019/L058 conventions and the direct-extraction, approval-loop and positive-endpoint stops. Four bounded external queries are recorded below; no additional usable primary theorem was located, and no novelty inference is made.
SOURCE_EVIDENCE: Inspected Polymath arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , (1)-(4), the symmetry paragraph after (4), Theorem 3.2 with its proof reference and the opening strip application in Proposition 3.3, plus Theorem 1.5(i)-(ii) and the absolute-constant convention. Versioned PDF https://arxiv.org/pdf/1904.12438v2 confirms (1)-(4), pp.1-2, Theorem 3.2, p.14, and Theorem 1.5, pp.9-10. Theorem 3.2 cites N. C. de Bruijn, The roots of trigonometric integrals, Duke Math. J. 17 (1950), 197-226, Theorem 13; the original proof was not inspected.
COMPARISON: The inspected strip theorem has exactly the H_t normalization used by L490-L493 and needs no RH or t>Lambda premise. L488 already checks the F/H identity and multiplicity/reflection transfer. L493 now supplies the missing numerical strip tail, including its closed height edge; L488 and source Theorem 1.5 alone still leave unnamed cutoffs. No existing canonical lemma states the exact numerical global F-tail.
GAP: No essential source coverage remains missing for this exact application. The next mathematical step must assemble the cited strip input with L493 and the existing F/H identity, including both closed time and spatial edges and preservation of multiplicity; this literature turn does not prove that application or replace its cutoff by an unnamed constant.
REASON: Separate approval of the saved target is complete: primary hypotheses and existing normalization cover its scope. Proceed to one mathematical specialization, classified REPRODUCTION, without another unchanged source approval. This is readiness of a known-method application, not mathematical progress beyond the checked literature.
SCOPE: Exact TARGET only. Reuse L493 and the audited L490-L492 inputs, L488's cited strip theorem and normalization, and L018/L019/L058 conventions. No new saddle estimate, collision exclusion, smaller-positive-time bound, zero-time limit or independent audit of the original strip/saddle proofs.
LITERATURE_REASON: The newly nominated all-zero global-strip/F-normalization application lay outside the exact L493 strip-exhaustion audit assessment. This turn inspects that missing primary theorem scope while reusing the completed numerical-tail literature comparison; it does not refresh an already ready target.

The main gap is actual-Xi all-degree positivity and finite positive-time
collision exclusion. The intermediate target is the numerical global
tail in TARGET. Its plausible use is to replace an existential spatial
cutoff in a later collision reduction on this band. It would give no
sign or collision certificate inside that region, or cover an arbitrarily
small positive transition. The cutoff remains an application to write,
not a theorem established by this source review.

## Inspected source statement and applicability scope

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant*, Research in the Mathematical Sciences **6** (2019), article 31,
[version 2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
Theorem 3.2, p.14, states: for real t_0 and y_0>0, absence of zeros
of H_(t_0)(x+iy) for all real x and y>y_0 implies, at every t>t_0,
absence for y>sqrt(max(y_0^2-2(t-t_0),0)). Its proof refers to de Bruijn
Theorem 13. Equations (1)-(4), pp.1-2, specify

    H_0(z)=xi(1/2+iz/2)/8,
    H_t(z)=integral_0^infinity exp(t*u^2)*Phi(u)*cos(z*u) du.

The paragraph after (4) states entirety, evenness and conjugation for
real t. The opening of Proposition 3.3's proof, p.15, uses the initial
xi strip and Theorem 3.2. This is the relevant primary application
case; no endpoint-collision premise is part of Theorem 3.2.

For the planned application, t_0=0 and y_0=1 meet its permitted parameter
conditions. L018 supplies the initial xi zero-strip input required by
source (1); L488 already records its use to obtain the closed H_t strip
|Im z|<=1 for positive t. This application needs only that weaker strip,
not a sharpened boundary estimate. The strict inequality in the theorem
does not justify excluding zeros on a new boundary by assertion; the
closed strip required by L493 suffices. Conjugation is available on each
real-time slice. Neither an all-real initial slice nor a simple initial
zero hypothesis occurs in this import.

The exact existing normalization is L488's (11),
F(lambda,z)=8 H_(4lambda)(2z). Its justification there uses L019's
K(2u)=4 Phi(u) in the absolutely convergent L058 integral. The displayed
kernel in L019 and source (3), and the defining integral in L058 and
source (4), were compared here; no new change-of-variables lemma is
needed. The already recorded source band is [1/25,11/50]. L493 assumes
that same closed band, |Im z|<=1 and Re z>=4*pi*exp(10000)+3, and
concludes reality and simplicity using L492's multiplicity-one count.
These are existing canonical statements, not new conclusions of this
review. L490-L493's proofs were not replayed.

The proposed cutoff is exactly the candidate obtained from the existing
spatial substitution, rather than a value assigned to L488's C_*.
The next proof must explicitly carry that substitution at equality,
use evenness for the opposite spatial edge, and explain why a nonzero
constant and an invertible linear substitution preserve the order of
a zero. L058 supplies evenness for each real lambda; no limiting
transition in lambda or z is required by the target. These obligations
are elementary specializations of covered inputs, with no new analytic
estimate identified by this comparison.

## Duplicate and failure comparison

The prior numerical-tail assessment and
drafts/heat/2026-10-30-explicit-positive-time-tail-source-review.md
already inspect the relevant explicit approximation and qualitative
counting cases. Their discovery coverage is reused. Source Theorem
1.5(i)-(ii) still has unnamed absolute constants, so it cannot by itself
give this numerical cutoff. L488 remains an existential global-tail
result; L493 remains a numerical strip-tail result. The exact numerical
global F statement is not already present among these local inputs.

The direct-extraction stop in
ATTEMPTS/2026-10-30-direct-numerical-tail-extraction.md is retained.
The approval-loop stop in
ATTEMPTS/2026-10-30-tail-approval-loop-recovery.md forbids gaining
nothing from unchanged approvals, not using the now audited L493 at
a new, exact application. This turn completes that one missing source
comparison. The blocked positive-endpoint Hamiltonian route in
ATTEMPTS/2026-10-30-positive-endpoint-inverse-gap-source-application.md
is independent and is not reopened. No blocked source is essential here.

For bounded duplicate discovery the actual queries were:

- `"1904.12438" "explicit" "simple" zeros cutoff`
- `"heat flow" "Riemann" "10000" "zeros"`
- `site:arxiv.org "Effective approximation" "heat flow" "simple"`
- `site:arxiv.org "H_t" "de Bruijn" "strip"`

The broad queries returned no usable additional primary match (including
unrelated third-party research pages); the arXiv-restricted queries
returned no results. None of those pages or snippets is a theorem input.
Direct access to the exact versioned Polymath source succeeded. These
search results do not establish novelty or absence of stronger results.

## Continuation and abandonment test

Disposition: SPECIALIZE, ready for the unchanged TARGET. Continue only
if its canonical application accounts for every zero on the full closed
time band, discharges L493's strip hypothesis from the cited theorem,
and preserves both closed spatial edges and multiplicities under the
existing normalization and reflection. A missing premise, failed edge
or normalization mismatch must be recorded and the proposed cutoff
revised or abandoned; an unnamed asymptotic cutoff cannot repair it.
Do not infer collision exclusion or expand to another target from this
approval. No application is proved here.

Source saddle proofs, the original strip proof and full matching
Mathlib coverage retain their unaudited/unchecked qualifications.
This source approval does not certify novelty. No new theta-specific
sign or arithmetic input overcomes the retained generic collision
obstruction, so there is no justified creative collision attempt to
nominate here. The next turn should perform the ready known-method
application. Literature work uses no mathematical exploration allowance;
this review claims no new mathematical advance.
