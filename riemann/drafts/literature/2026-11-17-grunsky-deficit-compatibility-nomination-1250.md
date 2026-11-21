# Actual-Xi inverse-Grunsky deficit: nomination1250

TARGET: Review the degree-six inverse-Grunsky compatibility test c_mn(f)=delta_mn/m-tau*S_(m+n) for m,n>=1 and m+n<=6, with actual Xi moments, tau>0 and a real normalized formal jet f(z)=z+a_2*z^2+...+a_7*z^7, checking exact conventions, known compatibility identities and duplicates before one mathematical attempt.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1251 reused comparison1250 and scoped1117/1121 evidence, searched notebook Grunsky/Koebe/diagonal-deficit records and exact external coefficient/recurrence terms, and inspected Teo2003 Section2 and Choi-Helsing-Kang-Lim2023 Sections2.2-2.3. No matching actual-Xi compatibility theorem was identified; no novelty inference.
SOURCE_EVIDENCE: Teo, Lett.Math.Phys.64(2003),75-92, arXiv:hep-th/0305005v2, Section2.1 and Section2.2(2.3)-(2.4),(2.8)-(2.12), preprint pp2-6, readable primary HTML; Choi et al., SIAM J.Imaging Sci.16(2023),969-995, DOI10.1137/22M1522395, Sections2.2-2.3(2.9)-(2.11), readable full HTML. Exact source statements and normalization are recorded in review1251 below.
COMPARISON: Known formal Grunsky identities cover coefficient extraction and necessary compatibility, including explicit mixed degrees four, five and six. The fixed actual-Xi deficit still requires substitution and a decided test; the sources establish neither that realization nor its failure. Global univalence remains essential for signing.
GAP: Source coverage now supports one degree-six algebraic test; no actual S_k has been substituted or enclosed. Existence for tau>0, higher compatibility, analytic extension and disk univalence remain unresolved. New quadrature or enclosure methods are outside this approval.
REASON: The essential convention and inverse-coefficient source blockers are resolved by primary formal identities. Their fixed-ansatz specialization has a falsifiable finite target; it must be performed in a later research turn after separate supervisor approval of the new continuation.
LITERATURE_REASON: Specific new lead from comparison1250 required essential inverse-coefficient coverage at turn start; review1251 now resolves it with primary formal identities. This was source approval of the fixed representation test, with no dependent calculation.
SCOPE: Completed literature-only review1251 of the unchanged fixed ansatz; the historical nomination text below is preserved. No actual-Xi substitution, elimination, lemma or mathematical script. The newly ready calculation assessment is drafts/literature/2026-11-17-grunsky-deficit-degree-six-calculation-1251.md and needs separate supervisor approval.

## Proposed mathematical test, not an identity

Use the convention to be checked directly in the primary source:

    log((f(z)-f(w))/(z-w)) = -sum_(m,n>=0) c_mn(f) z^m w^n.

The log is the normalized formal logarithm with constant term zero.
Only mixed coefficients m,n>=1 are prescribed. Coefficients with a
zero index remain those of f, not extra independently chosen data.
All a_2,...,a_7 and tau are real, and tau must be strictly positive.
The degenerate tau=0 diagonal reference is excluded. There is no
assumption that f is odd. The ansatz is fixed as

    c_mn(f) = delta_mn/m - tau*S_(m+n),  m,n>=1.

No scaling parameters or adjustable diagonal weights are included.
For the bounded necessary test retain only m+n<=6. Higher coefficients
of f are unspecified; the review must check that a_2,...,a_7 suffice
for these mixed degrees. This is an obligation, not a result derived
in nomination1250. The actual S_k are L025's convergent zero power sums
or its normalized local Xi logarithmic coefficients, with no RH
premise. Replacing them by positive raw theta moments is forbidden.

The motivation is the standard Grunsky contraction comparison. If an
appropriate full real univalent realization and its conventions were
paid independently, its diagonal deficit is a plausible route to the
actual mixed-form sign; this proposed implication also needs exact
hypothesis/index checking. For m=i+1,n=j+1 the desired moment index is
i+j+2 as in L030. A finite formal match proves neither contraction
nor an actual Schur sign. Do not treat it as another verified zero
range or a solution of RH.

After source approval, one mathematical attempt would eliminate the
jet coefficients and test the resulting necessary relations for the
actual S_2,...,S_6 and some tau>0. A rigorously violated necessary
relation stops this exact ansatz. Symbolic conditions without a decided
actual-Xi sign are unfinished evidence; floating values do not refute
existence. Exact identities or rigorously controlled theta integrals
would be needed for any asserted actual failure. No calculation or
enclosure method has been approved yet.

Continue only after a nontrivial compatible formal jet or an identified
new necessary relation that can be decided with existing actual inputs.
Even success through degree six leaves every higher compatibility
condition, convergence, disk univalence, singular lower blocks,
initialization, all-degree positivity, theta signing and graph realization
open. Failure stops the fixed diagonal-deficit ansatz, not Grunsky
methods generally, local signed representations, or RH.

Essential input IDs for a later attempt: L025/L030, with L019/L021 only
if actual theta integral evaluation becomes necessary; L032 explains
all-degree relevance. C030x is stop context, not a mathematical input.
Reuse1117/1121 and the scoped stops; no cross-notebook result is needed.
Full matching Mathlib coverage is unchecked.

The immediate next turn is literature_comparison, standard/high. No
creative attempt is preapproved. After review, classify the actual work
by purpose: a finite coefficient elimination alone is calculation,
standard/high; a genuinely new analytic realization construction would
need a separate proof_attempt/creative nomination, central obstruction
and bounded decisive test. Do not call routine algebra creative to meet
a scheduling preference. The current blocker is uncovered compatibility
and univalence, not an old route ban.


## Completed source review1251 — 17 November 2026

The preceding nomination is preserved as proposed work, not as a
completed calculation. Its source obligations are now resolved as follows.

**Primary formal input.** L.-P. Teo, *Analytic functions and integrable
hierarchies—characterization of tau functions*, Lett. Math. Phys. 64
(2003), 75–92, [arXiv:hep-th/0305005v2, 13 June 2003](https://arxiv.org/html/hep-th/0305005v2),
Section2.1 and Section2.2, preprint pp2–6.
Hypotheses: normalized formal Taylor/Laurent series; analytic
interpretations require local univalence. Equations(2.8),(2.12) identify
the nomination's c_mn with b_(-m,-n) of f and the symmetric exterior
coefficients of g_f(Z)=1/f(1/Z). Equation(2.9) fixes the zero-index
terms; a_1=1 gives c_00=0. For exterior g(Z)=bZ+b_0+sum b_j Z^(-j),
(2.4) gives Phi_m(g(Z))=Z^m+m sum b_mn Z^(-n).
The displayed identities on preprint p5 include

    b_1n=b_n/b,
    b_22=b_3/b+(b_1/b)^2/2,
    b_23=b_4/b+b_1*b_2/b^2,
    b_33=b_5/b+b_1*b_3/b^2+(b_2/b)^2+(b_1/b)^3/3.

The proof inspected differentiates(2.1), compares coefficients to obtain
the Faber recurrence, then substitutes g into(2.1) and compares with
(2.3). Equations(2.9),(2.12) prove the interior/exterior identification.
These are known identities, not new compatibility results.

**Independent normalization check.** D. Choi, J. Helsing, S. Kang and
M. Lim, *Inverse Problem for a Planar Conductivity Inclusion*,
SIAM J. Imaging Sci.16(2)(2023),969–995,
[DOI10.1137/22M1522395](https://epubs.siam.org/doi/10.1137/22M1522395),
Sections2.2–2.3, equations(2.9)–(2.11), full primary HTML inspected.
For the exterior map Psi(w)=w+a_0+sum a_j w^(-j) of a bounded simply
connected planar domain, its Faber coefficients C_mn satisfy

    F_m(Psi(w))=w^m+sum C_mn*w^(-n),
    n*C_mn=m*C_nm, C_1m=a_m, C_m1=m*a_m,
    C_(m,n+1)=C_(m+1,n)-a_(m+n)
              +sum_(s=1)^(m-1) a_(m-s)*C_(s,n)
              -sum_(s=1)^(n-1) a_(n-s)*C_(m,s).

Subscripts with sums or differences here denote single indices.
Comparison with Teo(2.4) means C_mn=m*b_mn; direct substitution of
the nomination's symmetric c_mn into that nonsymmetric recurrence
would be erroneous. No domain/conductivity theorem is transferred to
Xi. The recurrence is an independent check; Teo supplies the formal
framework without a domain-realization assumption.

**Sign interface, with its missing hypothesis.** Duren–Schiffer,
*Grunsky inequalities for univalent functions with prescribed Hayman
index*, Pacific J.Math.131(1988),105–121,
[Section1(1)–(2), pp105–106](https://msp.org/pjm/1988/131-1/pjm-v131-n1-p06-p.pdf),
is reused from comparison1250. Its exact inequality display remains
damaged in OCR; screenshot requests again exposed no readable images.
No optimized Hayman-index formula is imported. A readable independent
operator statement is Takhtajan–Teo, *Weil–Petersson metric on the
universal Teichmuller space II*,
[arXiv:math/0406408v1, 21 June 2004](https://www.math.stonybrook.edu/~leontak/Takhtajan-Teo-II.pdf),
Section3.1, preprint pp11–13: normalized disjoint univalent disk/exterior
maps, B1_mn=sqrt(m*n)*b_(-m,-n), and the classical Grunsky inequality
is equivalent to I-B1*B1^*>=0. This supplies the contraction convention
only. A full real disk-univalent realization is absent; a finite formal
jet cannot invoke that inequality. The proposed linear diagonal deficit
and actual Hankel index must be checked explicitly if used later.

**Applicability and remaining work.** Real coefficients are an allowed
specialization of the formal identities. The defining divided
difference lowers Taylor degree by one and its normalized formal
logarithm respects positive total degree; a_2 through a_7 therefore
suffice for mixed total degree at most six. This is truncation
bookkeeping, not elimination of the prescribed ansatz. L025 fixes
S_k=sum alpha_j^(-2k) and log(Xi(z)/Xi(0))=-sum S_k*z^(2k)/k;
L030 fixes the shift S_(i+j+2). These are not raw theta moments.
No positivity of S_k, RH, or all-degree finite-test inference is assumed.
No actual substitution into the displayed source identities was made.

Local Grunsky/Koebe/diagonal-deficit searches in drafts/literature,
drafts/working, ATTEMPTS, history, foundations and lemmas found only
nomination1250/comparison1250 plus an unrelated carrier-weight deficit.
Reused the scoped finite-block stop1117 and source assessments1117/1121:
they do not prohibit falsifying a specific representation, and finite
compatibility cannot establish all-degree signing. Queries included
`Grunsky coefficients inverse coefficient relations normalized univalent
function recurrence`, `Grunsky coefficients polynomial Taylor
coefficients log f(z)-f(w)`, `Grunsky c22 c13`, and `Grunsky Hankel xi`.
No exact actual-Xi match was identified; this does not certify novelty.
Search-only surveys and unrelated search hits are not theorem inputs.

**Decision.** SPECIALIZE for the bounded algebraic test in the new
assessment1251. Necessary identities are already known: importing and
checking their conventions is local progress only. Actual feasibility
remains undecided; no new lemma, script, actual-Xi sign, or RH candidate.
Full matching Mathlib coverage is not checked. The calculation needs
separate supervisor approval; no uncovered enclosure algorithm is approved.
