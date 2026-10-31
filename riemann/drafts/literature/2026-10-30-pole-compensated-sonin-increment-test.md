# Common-pole-phase Sonin increment: bounded test coverage

TARGET: Test whether the pole-compensated Sonin trace increment for adding prime p is o(p^(-1/2)log p) on the fixed-bump two-packet family, using the same padded pole phase on the actual predecessor and successor prime sets.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed arithmetic-slope screen compared three mechanisms and searched Sonin/pole/compensation/increment/covariance terminology. Narrow searches in local October 30 Weil assessments and ATTEMPTS found no matching corrected-projection test. External exact searches returned paper 2's separate uncorrected-increment and compensated-overlap theorems, not this combination. No originality claim follows.
SOURCE_EVIDENCE: bramble_trace paper 2 v2 (16 October 2026), Section 1 conventions, (6.1)--(6.3), Theorem 6.5 and full displayed proof (6.17)--(6.26), Section 7 Theorem 7.1 and full proof (7.1)--(7.4), Section 8 qualifications; Connes--Consani--Moscovici arXiv:2310.18423v2 Sections 4.6--4.8 and Theorem 4.6 with proof. Exact primary links and detailed readings are in 2026-10-30-nullvector-arithmetic-slope-discovery.md. The manuscripts' upstream proofs are not independently audited.
COMPARISON: Paper 2's uncorrected trace increment is O_h(p^(-1/2)(log p)^(9/10)); its pole compensation controls a different overlap for fixed tests and fixed-cutoff spectral asymptotics. It supplies no compensated moving-projection increment estimate. The Euler range identity and inverse Gram formula must be checked for the changed background, not assumed to give its localization. Only the identified difference is proposed for research.
GAP: Determine the corrected increment's arithmetic-scale behavior, or a concrete obstruction to defining/estimating it, with a common pole phase and padded support. Neither uncorrected localization nor fixed-test o(sqrt(X)) can answer this. No actual nullvector or complete-Weil positivity transfer is assumed.
REASON: One independent bounded test can decide whether exact pole compensation evades the source's uncorrected local-absorption obstruction. This is a proposed new arithmetic projection mechanism, not an approved theorem or reproof of Theorem 6.5. Coverage was written during a literature-only turn and requires the supervisor's separate approval before mathematical execution.
LITERATURE_REASON: The projection and moving-test hypotheses change after the explicit pole correction. Existing L525 and uncorrected-Sonin coverage does not cover this test; the relevant source statements and proof cases have now been compared without deriving the new estimate.
SCOPE: One asymptotic/projection-geometry attempt for the exact family below. First establish the needed traces and any range/projection formula; retain inverse Gram factors. No scripts or new mathematical results were produced in preparing this assessment. No zero-free exponent target, fixed-test uniformization, or eigenvector claim is approved.

## Primary inputs and what is not imported

[bramble_trace paper 2 v2](https://rstation.ai/problems/riemann_hypothesis/papers/2)
fixes logarithmic physical coordinates, convolution T_f, Fourier
transform F(t)=integral f(x)exp(-itx)dx and V_Lh(x)=h(x-L).
Its semilocal Fourier involution is formed from the unitary cosine
transform and the finite-prime factors. Use precisely its Mellin/
reflection convention and archimedean multiplier u_infinity. Its
finite-prime factor is

    u_q(t)=(1-q^(-1/2+it))/(1-q^(-1/2-it)).

Theorem 6.5 is available as a cited comparison, with its source-proof
qualification. It is not a theorem for the new projection defined
below. Its proof's localization uses an unchanged archimedean
background, the finite Euler range identity and weighted entire
evaluations. The new background depends on p, so that proof cannot
be replayed while keeping an unspecified uniform constant.

Theorem 7.1 supplies the explicit phase chi_M and its exact pole
interpretation on its stated support/full-prime-set class. It does
not claim that phase multiplication conjugates the old Sonin
projection, that the new Sonin space is nonzero, or that its trace
increments are controlled. Its fixed-M Hilbert--Schmidt perturbation
does not bound the variation of kernel projections at zero angle.
The o(exp(M/2)) bound concerns a full negative overlap at each fixed
test, not the Sonin trace tested below. No stronger conclusion from
Theorem 7.1 is used as an input.

[Connes--Consani--Moscovici Theorem 4.6](https://arxiv.org/html/2310.18423v2#S4.SS7)
provides the uncorrected Sonin isomorphism with changed inner
product. It does not identify the new kernel projection. No reproof
of either cited source theorem is needed; the changed projection is
the precise reason an additional mathematical attempt is needed.

## Prescribed observable, not a derived estimate

Fix once and for all the real positive smooth bump
h(x)=C exp(-1/(1-x^2)) for |x|<1 and zero otherwise, with C chosen
so ||h||_2=1. Let p tend to infinity through primes; put

    L=log p, r=p^(-1/2), M=L+2,
    f_p(x)=h(x+L/2)+h(x-L/2),
    P_-={q prime:q<p}, P_+={q prime:q<=p},
    chi_M(t)=4 integral_0^M cosh(v/2) sin(tv)/v dv,
    u_tilde_(P,M)(t)=u_infinity(t) product_(q in P)u_q(t)
                                      *exp(i chi_M(t)).

The centered packets and padding are part of the proposed test;
their use in the old source's comparison must be justified, not
silently substituted into its uncentered statement. In particular
supp f_p is contained in [-M/2,M/2]. Both backgrounds use exactly
the same M and phase. Changing the pole phase at the same time as
adding p would test a different increment.

Let F_tilde_(P,M) be the involution in the source convention, and
let S_tilde_(P,M) be the orthogonal projection onto the functions
vanishing on the negative logarithmic half-line together with
their F_tilde transform (equivalently the two positive-half-line
range intersection). The test is to determine, when finite,

    T_tilde_(P,M)(f)=||T_f S_tilde_(P,M)||_HS^2,
    Delta_p=T_tilde_(P_+,M)(f_p)-T_tilde_(P_-,M)(f_p),
    Delta_p/(r L) -> 0 ?

Existence/finiteness of the two separate traces, the correct
projection/range formula and its inverse Gram factor are obligations
of the attempt. An undefined infinity-minus-infinity is a failure,
not a cancellation. Triviality of the corrected Sonin spaces, if
proved, would also be informative negative evidence. No formula for
these changed projections or their limit is established here.

The source's signed arithmetic benchmark is -2rL||h||_2^2 for its
critical pair. Check its normalization, centered-test transport and
the unchanged pole contribution in the proposed setting before
using it. Only the complete prime set up to exp(M) would give a
full-Weil trace on the whole displayed support class; neither P_-
nor P_+ is that set. These two partial backgrounds deliberately
isolate a single prime addition. Missing primes are not discarded
in an asserted full-form identity. Equality atoms and all powers of
the added prime must be handled by the actual autocorrelation.

## Decisive test and downstream limitations

A proof Delta_p=o(rL) would preserve the local Sonin-only obstruction
after pole compensation. A justified negative leading contribution
of magnitude at least 2rL (with the exact benchmark checked) is the
threshold relevant to compensating the added negative arithmetic
term; it would nominate a further collective comparison, not prove
that comparison. A nonzero coefficient of the wrong sign, proved
space triviality, or an explicit missing domain/trace condition is
informative failure evidence. An absolute O(1) bound, a fixed-test
asymptotic or a new exact identity without a signed scale estimate
does not pass. Preserve partial reasoning and park this version if
no such discriminating evidence follows from one bounded attempt.

This targets an arithmetic-specific auxiliary input plausibly useful
for a collective signed comparison underlying the L522 upper-slope
gap. It does not yet imply that slope estimate. Connecting the
projection trace to a complete form, then to the rough conditional
nullvector and its displacement derivatives, remains unproved.
The L515/L516/L521/L522 model, source-identification qualification,
nonzero-trace contradiction premise and nonresonance remain unchanged
if that later transfer is attempted. No nullvector existence,
trace vanishing, H1, simplicity, positivity or uniform inverse is
granted. All-height positivity and Xi transfer remain open.

Mathlib coverage of the full statements is unchecked. No local
mathematical input has been added to DAG.md and no cross-notebook
theorem is used. The older Abel, nodal, transport, multiplier,
raw-adjoint and resolvent stops retain their exact scopes.
