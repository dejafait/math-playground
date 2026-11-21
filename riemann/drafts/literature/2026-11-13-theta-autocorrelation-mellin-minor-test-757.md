# Complete theta-autocorrelation mixture: one Mellin-minor test proposal757

TARGET: Test the single Mellin determinant D=q1*q3-q2^2 for the complete actual-theta A/H dilation-mixture proposal, justifying inverse-scale moments and all endpoints, then enclosing q1,q2,q3 with rigorous errors; decide only this necessary condition.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-class search and primary comparison completed757 in 2026-11-13-theta-autocorrelation-dilation-mixture-review-756.md; no new search or novelty claim.
SOURCE_EVIDENCE: Csordas1309.0055v2 (3.5),Theorems3.5/4.5, https://arxiv.org/html/1309.0055v2 ; Belomestny-Morozova-Panov2211.01799v2 Sections1-2,Mellin product identity, https://arxiv.org/html/2211.01799v2 ; Schmudgen2008.12698v1 Section3,Theorems3.1-3.2, https://arxiv.org/html/2008.12698v1 . Primary hypotheses and relevant proof passages inspected757; reuse review756 for exact reading limits.
COMPARISON: General Mellin factorization and positive moment-matrix necessity cover the mechanism; the actual-kernel normalization, inverse-scale specialization and rigorous complete-integral values are not in the sources. This is routine specialization, not a creative sign argument or a claim of originality.
GAP: No local moment inequality or determinant sign is established. Prove applicability under a hypothetical probability measure on finite b>0, then obtain one rigorous enclosure; do not assume differentiability or bounded support of that measure.
REASON: One finite necessary-condition test can discriminate this sufficient class without importing missing Fourier positivity. Cite the general inputs, justify only the local specialization and explicit integration errors; no all-order converse or representation construction is approved.
SCOPE: New ready proposal written757; separate next-turn approval is required before mathematics. Exactly r=1,2,3 and one determinant; no higher-order search, signed mixture, new tail comparison or general Mellin inversion.

Essential local inputs are L019 and L233 for complete k and A, and
C233c for established finite positive A(0) and its qualified tail.
C233c's Gaussian exclusion is contrast only. No cross-notebook input.
The main gap is L030-L032/C032a; even a representation would leave
higher/mixed signs, S3/H2 and global assembly unpaid.

Use precisely

    k(u)=K(|u|), with K from L019,
    A(t)=integral_R s^2 k(s+t)k(s-t) ds,
    H(t)=integral_R k(s+t)k(s-t) ds,
    a(t)=A(t)/A(0), h(t)=H(t)/H(0).

Here H is solely an autocorrelation, not a heat-flow contract.
The proposed representation is a(t)=integral h(bt) dmu(b) for all
real t, with mu a positive Borel probability on (0,infinity),
all scales finite and atoms allowed. For r=1,2,3 define the planned
quantities

    I_A(r)=integral_0^infinity t^(r-1) a(t) dt,
    I_H(r)=integral_0^infinity t^(r-1) h(t) dt,
    q_r=I_A(r)/I_H(r),  D=q_1*q_3-q_2^2.

No value or sign for these quantities has been calculated757.
The mathematical step must verify finite positive H(0) and I_H(r),
finite I_A(r), and legitimate normalization before division. Check
the inverse-scale moment identification under the hypothetical
representation by a positive-integrand interchange and dilation;
then specialize the cited moment-matrix necessity to this one D.
This local argument remains to be written, not assumed from terminology.
Retain unbounded support and arbitrarily small positive scales.
Do not impose finite inverse moments by assumption; establish the
needed finiteness from the actual integrals if representation holds.
Zero and infinity are not points in the stated scale space; do not
admit atoms there by an unjustified compactification. No complex
Mellin quotient, nonvanishing line, or derivative interchange is needed.

Use a single bounded analytic or validated-integration attempt to
enclose these complete integrals. Every theta truncation, integration
tail and quadrature error must be accounted for. If a script is useful
in that later research turn, save the full certificate under the notebook
scripts/ topic folder and print only the actual/required bounds and
paths. A numerical preview is not a proof.

The decision threshold is zero. A rigorous upper bound D<0 stops
this mixture class alone. A rigorous nonnegative enclosure only passes
this finite necessary test. An enclosure containing both signs leaves
it unresolved. None of these outcomes establishes a representation,
a negative actual Fourier value or RH. Stop after this single test;
a higher-order or tail target requires its own assessment.

The sources are to be cited, not reproved. Only the exact local
specialization and its effective error bounds need development.
Full matching/supporting Mathlib coverage remains unchecked.
