# Zero-winding actual-Xi Fredholm certificate — specialization coverage

TARGET: Specialize the zero-winding Borodin–Okounkov formula for actual G to a conditional D_(r,r-1)>0 certificate on circles with exactly r-1 enclosed zeros, proving conjugation-compatible logarithm, positive prefactor, trace class and sufficiency of ||Q_r H(b)H(tilde c)Q_r||<1 without assuming zero locations or minor signs.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step423's completed primary comparison in 2026-11-04-exceptional-toeplitz-fredholm-minor-review.md, including exact-symbol/minor searches and the step389/407/418 overlap checks. This is a conditional known-theorem application, not a new determinant formula or a novelty claim.
SOURCE_EVIDENCE: Böttcher–Widom https://arxiv.org/pdf/math/0604009v1 Section1 equations(1)–(2), Theorems1.1–1.2, pp.1–3, Section3 p.5 and Section4 pp.5–6; Bornemann https://arxiv.org/pdf/0804.2543v2 Section3 pp.9–10 (3.1)–(3.5) and p.12 (4.1); standard named argument principle and holomorphic logarithm theorem. Direct primary retrieval and read limits are recorded below.
COMPARISON: The exact zero-index Fredholm identity and norm-small Plemelj expansion are known. The remaining specialization checks the actual symbol's normalization, logarithm symmetry and sign under an explicit enclosed-zero-count hypothesis. The nonzero-index finite boundary determinant is excluded by this added, independent hypothesis; arbitrary radii remain outside scope.
GAP: No application proof is written yet. No actual norm estimate, all-r admissible-radius existence, multiplicity resolution, growing-order estimate or actual minor sign is supplied. The condition on the number of zeros is not to be inferred from a scalar saddle or from RH.
REASON: Establish the precise conditional interface before attempting an actual norm estimate; this is a different theorem case from an unpaid shifted boundary factor, and only routine specialization is approved in scope.
LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; step424 reopens only the essential cited passages to repair verifiable coverage, without extending the target or performing mathematics.
SCOPE: Actual entire G and positive coefficients of L018/L021, r>=2, R>0, G nonvanishing on |w|=R and exactly r-1 enclosed zeros counted with multiplicity. No other zero locations or signs may be assumed. The proof must leave unavailable radii and actual norm bounds as explicit independent gaps.

## Exact proposed work and imported tools

Step424 is the separate literature-only source-coverage approval of
this assessment. No application proof, operator computation or new lemma
has been performed here. A successful specialization is REPRODUCTION,
not a discovery beyond the cited sources.

Use the source conventions copied in the parent assessment: indices
start at1, H(f)_(i,j)=f_(i+j-1), tilde f(z)=f(1/z), P_r keeps the
first r coordinates and Q_r=I-P_r. For the whole shifted symbol

    phi(z)=z^(-(r-1))G(Rz), |z|=1,

apply only the zero-index theorem, after checking its exact hypotheses.
Use a normalized logarithm ell with ell(1)=log(G(R)), and verify rather
than assume its conjugation compatibility and the reality of its
Fourier coefficients. Do not assert that ell is real-valued along the
circle. Define phi_-, phi_+, b, c by Böttcher–Widom(1)–(2), without
changing their scalar normalization. The proposed correction is exactly

    A_(r,R)=Q_r H(b)H(tilde c)Q_r,
    b=phi_-/phi_+, c=phi_+/phi_-.

The theorem is for C^beta, noninteger beta>1/2, nonvanishing zero-index
symbols. Verify smoothness, the logarithm, factor regularity, the two
Hilbert–Schmidt hypotheses and trace class. An annular logarithm may
be used if justified; no logarithm over an enclosed disk containing
zeros is available or required. The argument principle and the stated
zero count must establish the index before invoking factorization.

The candidate conclusion is strictly conditional on ||A_(r,R)||<1 in
operator norm. Import the determinant identity and the trace-class
Plemelj expansion; give only the necessary specialization, symmetry,
sign and convergence arguments. Bornemann(3.3) supplies the norm-small
exponential identity, and (3.1)–(3.2)/(4.1) supply the determinant and
continuity setting. Verify why that determinant is positive for the
actual real operator under the norm hypothesis; nonvanishing alone is
not a sign argument. Check the source prefactor g(phi)^r E(phi) and the
power R^(r(r-1)) relating the source determinant to D_(r,r-1).

No numerical experiment is useful for this theorem application. If
successful, put the proof and exact source qualifications in one
canonical lemma with Hypotheses/Conclusion/Proof/Mathlib sections.
DAG edges should include only direct mathematical inputs actually used,
not L775 or other contrast results. Mathlib matching coverage is
unchecked. No cross-notebook input is proposed.

## Relevance and bounded decision

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is a correct independent conditional sign certificate. A later creative
attempt could test the actual Hankel correction norm using this explicit
operator, rather than reuse an absolute angular-complement estimate.
That later norm target needs its own source assessment and bounded
analytic discriminator; it is not approved by this assessment.

Continue only if the full conditional statement follows with a positive
prefactor and no extra boundary sign. If the specialization requires an
unprovided minor sign or more than the stated zero-count hypotheses,
record the exact defect and park it. Even success leaves actual norm
control, existence of suitable circles for all needed r (including tied
moduli/multiplicities), other minor indices and all-degree assembly open.
This small interface verification is ordinary known-theorem development,
not a protected creative attempt; creative estimation is blocked until
these hypotheses and sign conventions have been paid.

## Direct-source recovery approval — step424

On 2026-11-04 retrieved the versioned primary PDFs linked in
SOURCE_EVIDENCE. Rechecked Böttcher–Widom pp.1–3 for nonvanishing,
zero index, noninteger beta>1/2, factor conventions and both theorem
statements; p.5 Section3 for the exact identity and pp.5–6 Section4
for the prefactor identity. These are fixed-symbol statements: the
asymptotic estimate supplies no uniform varying-r or varying-R budget.
The parent assessment's nonzero-index boundary-factor stop is retained.

Rechecked Bornemann p.9 Section3 opening, p.10 (3.1)–(3.5), and
p.12 (4.1). The Plemelj representation is for trace-class operators
in its convergence domain; Lemma4.1's positive-selfadjoint setting is
not imported. A real-operator sign argument remains application work.
No further reference was read or silently imported in this repair.

The exact TARGET and SCOPE are unchanged. Reuse the parent comparison's
search and duplicate/failure checks; no new search or novelty inference
is warranted by a missing-link repair. SPECIALIZE remains ready for
the separate mathematical invocation. This is a process repair, not a
new mathematical advance or informative negative result; no exploration
budget reset is claimed. Full Mathlib matching coverage remains unchecked.
