# All fixed shifts — zero-detection source nomination

TARGET: Assess whether eventual nonnegativity of every fixed-shift Toeplitz ray forces all zeros of a real genus-zero entire product with nonnegative coefficients onto the negative real axis, including modulus ties and multiplicities.
CHECKED: 2026-11-06
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches under eventual total positivity, PF sequences, rectangular Schur positivity and meromorphic Toeplitz asymptotics; checked the two local adjacency stops and searched the exact cubic ansatz locally. No matching implication or counterexample was established from inspected sources; search failure does not imply novelty.
SOURCE_EVIDENCE: Inspected Alexandersson1208.5607v1 Theorem6 p.5/Section3.2 pp.11–12, Bell–Gerhold Theorem2 pp.334–335, Katkova math/0505174v1 Definition3 p.4/Theorem2 p.6, Rietsch2509.25163v3 Theorem1.1 p.2 and Fomin–Zelevinsky math/9912128v1 Lemma7/Theorem9 p.5. Bultheel DOI10.1137/0606061 full hypotheses and tied-packet cases remain inaccessible; indexed OCR is not an inspected theorem.
COMPARISON: Full PF-infinity, coefficient-tail APF_m and strictly positive solid-minor criteria differ from separate eventually nonnegative fixed-shift rays. Finite distinct-root formulas permit equal moduli but give no infinite-product transfer or automatic sign. L838 refutes adjacency only. A rational-phase cubic test is independently covered by the finite formula and does not require the blocked infinite source.
GAP: No inspected theorem settles the exact implication with ties, multiplicities and infinite products. A positive infinite-product approach needs the unread meromorphic asymptotics comparison or a separately assessed replacement. The nominated cubic's complete rank/shift signs have not been calculated; actual-Xi eventual signs remain independent.
REASON: Park the source-dependent infinite-product proof route after bounded access failure. Nominate one finite tied-modulus rational-phase test, with separate source-scope approval next turn; do not retry access or claim a counterexample before that mathematical check.
LITERATURE_REASON: The target changes finite degree and two fixed shifts to an infinite genus-zero product and independently quantified eventual signs at all shifts; those hypotheses and the tied/multiple first nonreal packet are outside the ready finite-polynomial assessment.

## Preserved nomination before this review

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The exact proposed class is

    F(z)=C product_nu (1-z/omega_nu)=sum_(n>=0) a_n z^n,
    C>0, a_n>=0, omega_nu!=0, sum_nu |omega_nu|^(-1)<infinity,

with the multiset invariant under conjugation, locally finite, and
repeated factors counted with their full finite multiplicities. Finite
products are allowed. The displayed product itself is the function:
there is no additional exponential factor. Extend a_n=0 for n<0 and
use D_(r,k)=det[a_(k+j-i)]_(0<=i,j<r). The proposed premise is
for every integer k>=1 there exists R_k such that D_(r,k)>=0 for
every integer r>=R_k. There is no common onset or uniform-in-k bound.
The question is whether this forces every omega_nu to be negative real.
This is an unproved question, not an imported theorem or a new lemma.

Plausible downstream use: a matching known implication would tell the
fixed-shift route whether separate eventual rays can detect every
off-axis packet without first proving a uniform overlap bound. It
would provide a criterion only, not actual-Xi signs or a solution of RH.
A matching counterexample would stop that different completion
mechanism. Do not report a reformulation as resolution or manufacture
an equivalence.

Compare up to three mechanisms: the L838 prescribed-finite-PF adjacency
inference is refuted; the actual L836 indexed overlap is parked on the
recorded runtime failure; this first-nonreal-packet detection question
has different hypotheses and requires no indexed-zero installation for
its source review. The completed six-moment sequence and stale overview
audit qualifiers are not reasons to repeat old tests. No changed runtime
or signed Xi input has appeared.

Essential local context is L838 as a contrast, L832's actual product
and the L018/L021/L776 normalization; read only needed ranges. Reuse
the existing adjacent-shift source/failure comparison. No cross-notebook
theorem is proposed. Full matching Mathlib coverage is unchecked. Do
not import finite-polynomial asymptotics into the infinite product,
assume simple or distinct-modulus zeros, or replace eventual
nonnegativity by strict positivity without changing the target.

Next turn is literature-only. Search exact and stronger versions under
eventual total positivity, PF sequences and compound Toeplitz asymptotics;
inspect primary theorem hypotheses and essential tied/multiple-root
cases before larger passages. A finite Widom formula or irrational
phase heuristic alone is insufficient coverage. Continue only with a
precisely matching import, documented counterexample, or newly scoped
and separately approved bounded test for a specific unmatched case.
Park this question if the only proposed use simply assumes the sought
actual-Xi signs without an additional testable mechanism, or if an
essential source remains persistently blocked. No new lemma or
mathematical script is authorized by this file.

No creative proof attempt is yet justified: the detector implication
has not been assessed, and no mechanism establishing the required
actual-Xi eventual signs is supplied. Source coverage comes first.

## Preserved preliminary checkpoint (superseded by completed review below)

The exact target and all hypotheses above are preserved. Primary
statements inspected so far: Alexandersson v1 Theorem6 and Section3.2;
Bell–Gerhold Theorem2 and the actual-root convention (printed pp.334–335);
Katkova v1 Definition3 (printed p.4) and Theorem2 (p.6);
Rietsch arXiv:2509.25163v3 Theorem1.1 (printed p.2).
Katkova's APF_m quantifies over a coefficient tail with at most m rows,
not the fixed-shift, unbounded-rank rays here. Edrei's characterization
as stated by Rietsch assumes all minors nonnegative. Neither statement
provides the proposed eventual-ray implication. No new mathematical
result has been derived. Finite-root formulas and recurrence tests
remain method inputs, with infinite-product transfer unpaid.

New primary lead: A. Bultheel, *The asymptotic behavior of Toeplitz
determinants generated by the Laurent coefficients of a meromorphic
function*, SIAM J. Algebraic Discrete Methods6(4) (1985), 624–629,
DOI10.1137/0606061. Its publisher abstract specifies fixed shifts and
growing determinant size, but is not theorem coverage. The author PDF
at https://nalag.cs.kuleuven.be/papers/ade/astoep/paper.pdf timed out
through web access; local curl failed DNS. Exact hypotheses, tied and
multiple-root cases have not yet been read. Do not import it from its
abstract. A bounded alternate-source attempt remains before the final
decision. The gate remains REVIEW_REQUIRED during this checkpoint.

## Completed source review, 6 November 2026

Rietsch's *Totally positive Toeplitz matrices: classical and modern*,
[2509.25163v3](https://arxiv.org/pdf/2509.25163v3), printed p.2,
states Edrei's theorem for **all** minors nonnegative, with summable
nonnegative root/pole parameters and a nonnegative exponential parameter.
It does not replace that premise by the eventual rays in TARGET. This
is a nonmatching characterization, not an imported solution.

Katkova's [v1](https://arxiv.org/pdf/math/0505174v1), Definition3,
printed p.4, uses the m-row matrix (a_(N+j-l)) with j>=0 and
0<=l<m. Theorem2, p.6, concerns xi_1 in this coefficient-tail class.
The unbounded index differs from TARGET. No actual-Xi fixed-shift
eventual-rank signs follow from this statement. Reuse its previously
assessed positive-consecutive-minor method, not a weak-sign extension.

Fomin–Zelevinsky, *Total positivity: tests and parametrizations*,
[math/9912128v1](https://arxiv.org/pdf/math/9912128v1), printed p.5,
Theorem9 and the following Fekete discussion require strict positivity.
Lemma7's proof divides by a nonzero initial minor; zero minors cannot
simply be retained in that proof. An indexed Borodin–Olshanski lecture
note footnote asserting sufficiency of nonnegative solid minors was
only a lead, not accepted coverage. No general counterexample from
the inaccessible 2024 *Atomic viewpoint* article is imported either.

Bell–Gerhold permits polynomial amplitudes for repeated characteristic
roots and does not assume irrational phases. Its sufficient oscillation
test excludes any positive dominating root in the actual nonzero power
sum. A packet with a positive dominating root is outside that test;
one cannot infer oscillation merely from the presence of nonreal roots.
Its previously inspected rational/mixed-frequency proof cases are reused.

The bounded Bultheel access attempt is now closed. HTTP redirected to
the timed-out PDF; the publisher PDF was inaccessible, and the author's
publication page timed out. Indexed primary-PDF OCR showed Theorems4/5
and Corollary1, but lost essential inequalities. It is not theorem
coverage. The infinite positive-implication arm is parked; this source
is not essential to the independent finite falsification test below.

Queries included “Toeplitz determinants eventual positivity all orders
zeros entire function Schoenberg”, “eventual Schur positivity rectangular”,
“meromorphic Toeplitz determinants zeros positivity”, “Hankel determinants
eventually poles”, and “nonnegative contiguous minors counterexample”.
Followed the Bultheel primary lead and strict solid-minor criterion;
secondary pages and snippets were discovery aids only. The exact ansatz
and “solid/contiguous minors” searches in local lemmas, assessments and
ATTEMPTS found no matching cubic certificate. The inspected L837/L838
stops concern degree five and selected adjacent rays, not this test.

The independent ansatz is P(z)=1+z+z^2+z^3. Its proposed elementary
variables are {1,i,-i}; check their match and every determinant sign
in a later mathematical turn. The nomination tests modulus ties,
rational phases, possible zero residues and the strict/weak distinction.
No periodic table, sign formula or counterexample was established here.
Finite products are explicitly allowed in TARGET, so a successful finite
counterexample would settle its universal implication without an
infinite-product theorem. It would not settle versions with extra Xi
hypotheses or prove/disprove RH. L832's genus-zero product and the
L018/L021/L776 normalization were checked only for the actual-Xi context.
No cross-notebook input or originality claim is made. Full matching
Mathlib coverage remains unchecked.

Separate finite-test coverage is in
`2026-11-06-cubic-tied-modulus-all-rays-test.md`. This newly written
assessment requires separate approval next turn. Continue only with
exact formulas covering all positive ranks and every shift, including
zero values and shifts above the degree; otherwise reject this ansatz
without reviving blocked access. No mathematical scripts, lemmas, PROOF
or DAG were changed. No justified creative actual-Xi mechanism emerged:
the finite test is known-method specialization and actual-Xi signs
remain missing.
