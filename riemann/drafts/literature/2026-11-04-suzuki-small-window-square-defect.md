# Suzuki: bounded small-window square-defect test

TARGET: Determine the sign of <f_t,(K_4[t]^2-K_2[t]^2)f_t> for all sufficiently small t>0, where f_t=1_[-t,t]/sqrt(2t), using Suzuki's complete kernels and a rigorous remainder estimate.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The separate parameter-descent review searched exact Suzuki/composition/semigroup terms and primary continuous Hankel product formulas; scoped searches of L618, its assessments and the construction/screw stops found no completed small-window square-defect test. No exact matching result was located; no originality is asserted.
SOURCE_EVIDENCE: Suzuki arXiv:1907.07302v2 (6 March 2020), (1.1),(1.11),(1.13), Theorem 1.2, Proposition 3.1, Proposition 3.2 and its small-x proof (3.8)-(3.10), and the full kernel identity (3.13), printed pp.1,3,5-7, were read in step 266. L618's hypotheses and support compression are reusable; its norm estimate is not to be audited again.
COMPARISON: The primary source supplies the auxiliary small-x expansion and an exact complete-kernel representation, but not this squared-operator comparison on the specified vector. Only the fixed theta=2,4 specialization, remainder transfer and quadratic-form sign remain to be done; no general compression identity or descent theorem is required.
GAP: Transfer the cited local source formula to the complete kernels on the shrinking square, bound every integral remainder, and establish the sign on the prescribed normalized vector. No coefficient, sign or quantitative onset is established by this assessment.
REASON: This tests one concrete sufficient square-order mechanism for descent, independently of RH or all-window contraction. A negative witness parks that mechanism; it does not disprove RH or refute all possible descent implications. This is routine source specialization, not a creative central-gap mechanism.
SCOPE: Fixed parameters 2 and 4 only; sufficiently small real t>0; original unweighted L2((minus infinity,t),dx) operators; f_t extended by zero; existence of a rigorous positive onset suffices. No parameter sweep, L618 replay, arbitrary defect design, growing windows or determinant equivalence.

## Precise source inputs and remaining specialization

Use L018's completion and the complete operators in L618's hypotheses.
[Suzuki v2](https://arxiv.org/pdf/1907.07302v2), Theorem 1.2, gives
real continuous causal kernels for theta>1. Proposition 3.2 states

    Psi_theta(x)=x^(theta-1)/Gamma(theta)+O_theta(x^theta), x -> 0+.

It also gives causality. Its proof (3.8) is a Volterra convolution
with the bounded-near-zero auxiliary function of Proposition 3.1;
(3.9)-(3.10) identify its Bessel contribution. These statements are
used only at theta=2 and 4, where no singular value at zero occurs.
The printed proof also contains a weaker O(x) estimate; that weaker
display alone must not be substituted for the stated remainder.
The cited Volterra formula is available if this qualification needs
explicit justification in the specialization.

Equation (3.13) expresses g_theta through Psi_theta and a Bessel J1
Volterra term. Keep its factors, exponentials and removable quotient
at zero exactly as printed. Equation (1.13) is the complete arithmetic
sum, and (1.11) fixes the coefficients and their normalization. Any
reduction of this sum on a short interval must be justified from
causality and its n=1 coefficient, not assumed from a numerical cutoff.
No small-x formula for g_theta or K_theta has been derived here.

The square means composition of the actual compressed operator with
itself, not the parameter-doubled kernel. Reality, symmetry, compact
support reduction and the vector normalization must be checked when
turning the quadratic form into norms. L618 supplies the support
argument on `[-t,t]^2`; it does not supply the desired signed comparison.
Do not apply an unweighted full-line multiplier theorem.

## Relevance and bounded decision

The main gap is actual-Xi positivity. The prospective downstream use
is to decide whether the simple favourable order
`K_2[t]^2 <= K_4[t]^2` can support parameter descent at all windows.
Only a negative scalar witness disproves that order; a nonnegative
value on this vector cannot verify the order. Either sign leaves the
bare implication between contractivity statements unresolved.

Perform this one asymptotic test with rigorous errors. If the witness
is negative, stop the simple order mechanism and record its precise
scope. If the sign remains unresolved, save the uncontrolled remainder
and park the diagnostic; do not sweep vectors or windows in the same
turn. Any further mechanism needs materially different signed input.
No complete RH route, operator realization or mixed positivity is
assumed. Essential local input IDs are L018 and L618; L001/L005 enter
only if L618's existing estimate is actually used.

This newly written ready continuation requires the supervisor's
separate next-turn approval. Recommended actual mathematical task:
calculation, standard/high. Mathlib coverage of this specialization
has not been checked; no absence claim is made.
