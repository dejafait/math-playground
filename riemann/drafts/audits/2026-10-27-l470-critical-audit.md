# L470 critical application audit — 2026-10-27

Gate: invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-l470-critical-audit-coverage.md`.
Completed task: proof_audit/routine_audit, REPRODUCTION. This audits the
application of imported results, not their independent reproof.

The main gap is initial actual-Xi signs at unbounded heights and global
mixed positivity. The intermediate target is the exact polynomial linear
closure obstruction in L470. Its downstream use is to prevent sign
propagation from assuming such a closure. The test is whether every
hypothesis and implication survives replay; failure requires narrowing
or repairing the stop. Neither outcome supplies signs or boundary data.

## Complete application replay

1. **Imported hypotheses and conventions.** The complete saved inspection
   in `drafts/literature/2026-10-26-xi-polynomial-ode-source-notes.md`
   covers Valiron, Proposition I, printed pp. 33–34, and the full linear
   proof pp. 35–38, including exceptional radii and same-modulus branches.
   It records positive finite normal type for transcendental entire
   solutions of finite homogeneous linear equations with rational
   coefficients. No monic polynomial equation or nowhere-vanishing
   highest polynomial is required. L470 uses precisely this consequence,
   not the nonlinear cases or an assertion about polynomial solutions.
   Bornemann is corroboration only. No missing condition was found
   within this previously inspected scope; the PDFs were not retrieved again.

2. **Exact completed function.** L018 defines entire xi and proves
   xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2 on Re(s)>1.
   This is the formula in Lagarias–Rains, §4 opening, printed p. 23.
   Equality on that nonempty open set identifies the entire functions
   uniquely. Order one and infinite type are imported from that passage,
   not inferred from their Theorem 4.1's upper bound. With L470's
   maximum-modulus conventions this gives rho=1 and
   limsup log M(R)/R=infinity. A nonconstant polynomial has order zero;
   a constant cannot have order one either. Thus transcendence holds.
   No conclusion about zeros is used.

3. **Affine differentiation.** Repeated ordinary differentiation of
   Xi(z)=xi(1/2+iz) multiplies by i at each step. The factor is i^j,
   including j=0, without factorials. The inverse variable is
   z=-i(s-1/2), since 1/2+i[-i(s-1/2)]=s. Substitution gives exactly
   q_j(s)=i^j p_j(-i(s-1/2)). Affine composition preserves polynomial
   coefficients and the equation's finite order. If q_r vanished
   identically, surjectivity of the affine map and i^r!=0 would force
   p_r identically zero, contrary to hypothesis.

4. **Highest coefficient and application.** The transferred equation is
   an entire identity with a nonzero highest polynomial. Normalizing
   away from its finitely many zeros gives rational coefficients.
   Valiron permits their poles: no ordinary-point initial-value equation
   is being asserted at those locations. The entire function satisfies
   the polynomial identity everywhere. No simplicity, real-rootedness,
   RH or external half-plane estimate enters the application.

5. **Contradiction at the same order.** Valiron supplies normal type at
   xi's own order. The independent xi input fixes that order to one,
   so the type denominator is R. Its positive finite limsup contradicts
   the infinite limsup in step 2. There is no comparison of different
   orders or centers. No translation invariance of type is needed:
   the equation, rather than the growth bound, was transferred to xi.

6. **Interval extension and limits.** Each p_j Xi^(j), and hence their
   finite sum, is entire. Vanishing on a nonempty open real interval
   supplies an accumulation point in C, although the interval is not
   complex-open. The identity theorem applies on connected C. Isolated
   zeros of p_r do not affect this argument. Only exact homogeneous
   polynomial linear identities are excluded. Arbitrary analytic
   coefficients, unrestricted forcing, nonlinear equations and difference
   systems remain outside the conclusion.

Verdict: no failed implication or mathematical repair was identified.
This critically checks the existing class stop at the application level.
It produces no new theorem, sign, off-line zero or progress beyond the
checked sources. Accordingly the outcome is STALLED under the shared
definitions, rather than a repeated NEGATIVE or an ADVANCE. The canonical
proof retains all mathematics and exact citations; only its audit
qualification changes. L018 remains the sole local mathematical input.
No DAG or overview argument change is warranted. Mathlib remains
unchecked, not absent.

## Recovery comparison

Three mechanisms were compared without a second mathematical attempt.
The regular two-sided scalar height barrier is constrained by L469.
Finite homogeneous polynomial linear closure is stopped by audited L470.
A different possibility is an unconditional bound for the negative part
of the actual first Laguerre form averaged over a dyadic height interval.
This asks for arithmetic control of a sign statistic, not derivative
closure or an inference from positive mean to pointwise positivity.

Narrow negative-part/mean/Laguerre searches in notebook literature and
ATTEMPTS located related but different records: the L389 physical-pencil
discriminant measure assessment, the L405/L409 clipped-square transfer
assessment and the endpoint relative-mean-square stop. Their inspected
scope fields do not cover this exact actual-Xi statistic. The last record
warns that a small exceptional set may contain every prescribed witness
height. That limitation remains, not solved by the new nomination.
No new source theorem or estimate is asserted here.

The new assessment is REVIEW_REQUIRED. Its comparison must decide
whether mean-value or zero-density theorems control the negative part
itself at the proposed scale; a signed first moment alone does not.
A favorable result would supply at most a quantitative exceptional-sign
input. Localization, exceptional heights, higher initial signs and mixed
positivity would remain separate gaps. No justified creative proof target
exists before this essential comparison; no calculation is preapproved.
