# Positive reciprocal-theta generator: the unpaid Li interface

TARGET: Assess whether Lagarias–Rains's positive Feller generator yields a convergent representation of L984's cumulative Li germ with an independently bounded signed coefficient cost, retaining reciprocal-theta reconstruction, pole subtraction and finite-degree terms.
CHECKED: 2026-11-11
DECISION: IMPORT
SEARCH_EVIDENCE: Step422 searched exact reciprocal-theta/Feller/Li/logarithmic-transform terms, inspected the primary convergent-transform statements and essential proof cases, and reused review420's probability coverage and the recorded signed-recurrence/Gram failures. No matching signed Li-cost theorem was located; no novelty or universal impossibility is inferred.
SOURCE_EVIDENCE: Lagarias-Rains math/0104176v5 (7July2002), Theorems2.1/2.2 pp7-10, (2.9)/(2.12)-(2.22), Theorem4.4 and Lemmas4.5-4.7 pp21-23 with complete selected proofs (4.6)-(4.9), Lemma4.8 p24, Theorem5.1 statement/proof pp24-27; reuse Theorem7.4. Source details and qualifications below. L018/L019/L984 and audited C984a were read at their relevant complete statement/proof ranges.
COMPARISON: Exact source-supported convergent transforms reconstruct the entire theta family, including its actual-xi slice, with pole compensation. They do not estimate its logarithmic quotient's signed Li coefficients: compact-parameter Schwartz bounds are not an all-degree bound or a zero-free denominator. Section7.3 Question4 explicitly leaves the semigroup's zero-control role open.
GAP: No independently estimable signed component with root rate at most1 is provided for the complete cumulative Li observable. Reconstruction itself is known; the inverse/logarithmic signed-cost step remains unpaid, as do L984(H), forcing and actual-Xi positivity.
REASON: Import only the known transform contracts and their scope; park the direct generator-to-Li payment nomination because the inspected representation adds no signed-cost estimate. A separate finite zero-geometry source target is nominated below; no new reconstruction lemma or mathematical attempt is approved.
LITERATURE_REASON: The changed target asks for the inverse-theta-to-logarithmic-Li interface, whereas the inspected Section7 results prove a different positive semigroup. Exact reconstruction, convergence and signed-cost hypotheses remain unread/unmatched.
SCOPE: Completed literature-only assessment. IMPORT covers the cited transform facts and source-scope conclusion only; it authorizes no new generator specialization, reconstructed identity, model, lemma, mathematical script, sign claim or all-degree estimate. The distinct continuation remains REVIEW_REQUIRED.

The main gap remains L030-L032/C032a positivity, L966/L968 forcing,
and L984(H). Keep actual Lambda, every prime power, the complete
compensator and X_n=exp(10000(n+1)^4). L984 needs the one-sided
every-epsilon upper bound for a_n, all n>=2. Its ordinary coefficients
are lambda_n, and c_n=sum_(k=2)^n lambda_k. Do not switch to divided
coefficients or mistake a germ for a Taylor sum beyond its radius.

Essential local inputs to the new assessment: L018/L019 for exact
completion and theta normalization; L984 for its cumulative germ and
arithmetic interface; audited C984a as a contrast only. L983 and
stops235/240/284/302/305/308/417 retain their limitations where relevant.
L981/L982 need narrow reading only if a proposed arithmetic transfer
actually uses their endpoints or cutoff limits. No cross-notebook input.

The intermediate target is source coverage of one convergent transfer
with independently estimable signed cost, rather than another RH
criterion. A successful comparison could nominate a component estimate
whose error is subexponential in n (root rate at most1), even with other
signed components unresolved. It must define that error and its complete
observable before approving research. A complete coefficient conclusion
is not to be assumed as a convenient regularity premise.

First inspect the primary definitions and selected proof cases that
connect the theta family, its derivatives and its Mellin/Fourier
transforms. Search exact terminology and stronger known results for
transfer through reciprocals, the entire-completion pole factors and
logarithms. Reuse the already adequate probability theorem without
reapproval. Compare any proposed positivity mechanism with existing
logarithmic/Gram and signed-recurrence failures before loading detailed
proofs; do not broadly rescan the notebook or reopen blocked originals.

Continue only if this identifies a concrete bounded mathematical test
with hypotheses, input IDs, a separately payable component and a
decisive threshold. Park the transfer if it only recovers the already
known local germ, requires a positive convolution family at w=1, drops
the pole subtraction or finite degrees, or assumes the missing Li sign.
No universal failure theorem is asserted. If no test is justified,
record the specific source evidence and choose a different independently
testable target rather than repeat this source question.

Full matching Mathlib coverage is unchecked and unknown. This is not a
creative-proof nomination: the necessary reconstruction and signed cost
are not yet specified by an applicable inspected theorem.

## Completed source comparison — step422

The preceding discovery instructions are historical. This step tested
one question: whether the known positive generator supplies a convergent
transfer with a separately payable signed cost. Such a component could
help L984(H) without settling independent forcing or positivity gaps.
The continuation threshold was a completely defined signed error with
root rate at most1; recovering only the germ was the abandonment test.
The inspected sources meet the reconstruction part, not that threshold.

### Exact primary coverage

J. C. Lagarias and E. Rains, *On a Two-Variable Zeta Function for Number
Fields*, [arXiv math/0104176v5](https://arxiv.org/pdf/math/0104176v5),
7July2002, internally dated6July2002. Page numbers below are the
preprint's printed pages (53-page PDF), not the journal pagination.

Theorem2.1, pp7-9, defines the entire function

    xi_Q(w,s)=s(s-w) Z_Q(w,s)/(2w),

with the removable w=0 value, and identifies xi_Q(1,s) with precisely
L018's xi(s). Its proof separates the endpoints and retains
-1/s+1/(s-w) in (2.9). Theorem2.2, pp10-11, gives an absolutely
convergent integral whenever Re(s) is neither0 nor Re(w):

    Z_Q(w,s)=int_R [theta(exp(2x))^w
                  -H(s)-H(w-s)exp(-wx)] exp(sx) dx.

Here H(a)=1 or0 according as Re(a)>0 or<0; this H is the source's
Heaviside function, not L984's H(z). Cases (2.13)-(2.16) specify all
four orderings of the two real boundaries. The proof (2.17)-(2.22)
accounts for the two rational pole terms using convergent half-line
integrals. The statement excludes the boundary lines. In particular,
it does not directly supply the s=1 Li expansion point at w=1.

Theorem4.4, pp21-24, with its own notation

    h(w,r)=(theta(exp(2r))^w-1)/w      (w!=0),
    h(0,r)=log theta(exp(2r)),
    gamma(w,r)=(d^2/dr^2+w d/dr)h(w,r),

gives, using ONLY its unshifted case y=0,

    xi_Q(w,s)=1/2 int_R gamma(w,x) exp(sx) dx.

For fixed real sigma, exp(sigma*x)gamma(w,x) is Schwartz, uniformly
on compact parameter sets. Lemma4.5 bounds the theta Fourier series
and its derivatives with Re(tau)>=epsilon>0 and |w|<=R; Lemma4.6
uses superexponential decay on one half-line and the modular relation
on the other. Lemma4.7 justifies the twice-integrated-by-parts proof
away from Re(s)=0,Re(w); (4.6)-(4.9) and compact uniformity extend
the completed integral to all w,s. Lemma4.8, p24, gives polynomial
multipliers and inverse transforms with the same subtractions and
the same excluded lines for the uncompleted Z_Q integral.

These are cited source results, not locally rederived identities.
The source's displayed nonzero-y theorem and (4.8)-(4.9) do not
display the same prefactor; this review restricts the import to y=0,
where that issue is absent. The w=0 line of Lemma4.7 is not used
as an independent boundary-subtraction formula. We read
the relevant special cases rather than claiming a complete independent
audit of the paper. No shifted-contour formula is used here.

Theorem5.1, pp24-27, evaluates xi_Q(0,s) by a product of two completed
zeta functions and elementary factors. Its proof first takes the
theta-power derivative in a right half-plane, expands log theta,
and integrates the Fourier series for Re(s)>2; (5.6) evaluates the
Dirichlet series there, and analytic continuation gives the entire
identity. These domains matter: the calculation is not a positive
convolution representation at w=1. Theorem7.4's already assessed
finite positive M is the transform of gamma(0,r), not of a logarithm
of xi_Q(1,s). The source itself asks in Section7.3 Question4, p44,
whether the negative-w convolution structure controls the requisite
zeros at w=0; it does not state such a theorem.

### Comparison with the actual required observable

L984's existing, locally convergent identity is retained verbatim in
meaning: H(z)=2xi(1/(1-z)) and

    F(z)=[z H'(z)/H(z)-lambda_1 z]/(1-z)
        =sum_(n>=2) c_n z^n,   c_n=sum_(k=2)^n lambda_k.

The degree0/1 coefficients are zero. Its logarithm is only local;
its quotient may have genuine off-axis interior poles. No source
above estimates a signed component of these c_n independently of
the denominator, gives unit-disk Taylor convergence, or bounds its
negative part by D_epsilon exp(epsilon n) for every epsilon>0.
The gap is quantitative/logarithmic, not access to a convergent
integral for xi itself. Compact-parameter bounds cannot be silently
declared uniform as s=1/(1-z) leaves every compact set near z=1.
No new counterexample or theorem of impossibility follows from this
comparison. C984a remains the audited real-radius contrast only.

Reused failures: review191's Xiao/Maslanka signed-forcing comparison,
the completed theta-heat review and its Gram/moment comparison, and
stops235/240/417. Their missing signed budgets and Taylor-domain
conditions persist. The earlier general growth/ODE assessment covers
a different question; no polynomial ODE or generic positive-kernel
model is proposed. The October fixed-half-plane baseline is not
reopened: no new zeta zero-free region or reciprocal-series estimate
is claimed. Mathlib matching coverage remains unchecked and unknown.

Queries included `"Lagarias" "Rains" "Li coefficients" theta`,
`"reciprocal theta" "Li" zeta logarithm`,
`"theta" "Feller measure" logarithm zeta`,
`"Li coefficients" "theta" "logarithm" integral representation`,
and `"Riemann" "theta" "Feller" coefficients logarithmic`.
Primary Lagarias-Rains statements/proofs were actually read. Search
snippets, AI-written courses, secondary mirrors and unrelated hits
were not theorem evidence. Biane-Pitman-Yor's survey is an unread
lead, not a missing essential theorem assumed to prove this transfer.

### Decision and distinct continuation

NEGATIVE / LITERATURE / NOVELTY_UNCHECKED: exact transform coverage
closes the representation-source question and parks direct payment;
it supplies no bound toward H and no progress beyond cited mathematics.
No mathematical exploration budget was spent or reset. No lemma,
script, PROOF argument or DAG edge changed. No cross-notebook input.

A narrower independent prospect is a finite certificate in this
actual theta family at w=3/2, rather than coefficient transfer.
Section8 Lemma8.1, pp44-45, reports numerical departure of the pair
near heights42 from the center line, but its argument uses numerical
tracking and does not supply an interval enclosure. Its text also
writes 1-rho in a symmetry statement for variable w; the applicable
functional equation is s->w-s. This review imports neither that
numeric premise nor the asserted branch connectivity as a rigorous
certificate. Section6.3 expressly leaves individual motion bounds
unproved. A fixed-slice off-center zero certificate could test whether
a proposed universal center-line-preservation mechanism is viable;
it would neither refute RH nor establish transport to w=1.

The separate [review422](2026-11-11-two-variable-fixed-slice-zero-certificate-review-422.md)
asks for essential enclosure coverage before any calculation. No
creative central mechanism is yet justified: the missing signed
Li cost and collision-aware transport remain precise blockers. This
finite reproduction lead is not relabeled creative to meet a schedule.
