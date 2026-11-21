# Integrated spectral test: source comparison1582

18 November 2026. Literature only, completing assessment1581's exact
target. No specialization, new estimate or test-function transform is
proved here. C032y's existing formulas are used to identify the test.

## Purpose, comparison and bounded decision

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
The intermediate target is direct explicit-formula evaluation of
a -> e_(sigma,a)(w), with real sigma in[1,2] and complex |w|<=2.
It could supply E for dictionary1570's variation-at-most-2
residual<1/2 test. It does not supply O, that certificate, arbitrary
variation exclusion, full odd cancellation or unsmoothed realization.

Read C032y's statement and complete proof sections1-6, C032m's
definitions/source/compact-bound sections, notes1572/1555 and
assessment1570. Inspected C032w sections1-2 and its tail passages,
C032x's scoped stop and input-limit1581. Targeted searches in the
18-November Gaussian/spectral assessment and attempt paths found
no earlier inspected direct transform for e. This is a bounded
duplicate check, not a claim of novelty. No other notebook was read.

C032w transforms a shifted profile before recovering a spatial
primitive; C032x stops its literal expanding-disk procedure.
C032y has an integrated pair and a spectral cutoff bound but needs
complete certified finite coordinates for that numerical procedure.
Neither stop settles admissibility of the integrated pair on a
continuous wider strip. Conversely, C032y's estimate at actual
divisor points is not itself the wider-strip hypothesis.

## Primary input newly inspected

NIST DLMF, version1.2.8 (15 September2026),
[7.7.3 and its derivation note](https://dlmf.nist.gov/7.7.E3):

    integral_0^infinity exp(-A*t^2+2*i*z*t) dt
      =sqrt(pi/A)*exp(-z^2/A)/2+i*F(z/sqrt(A))/sqrt(A), Re(A)>0.

Here F is Dawson's integral, not C032q's width transform F_eta.
The displayed restriction is on A; z is complex. The source's note
explains the contour split at i*z/A. This is an exact integral
representation, not a real-axis asymptotic or a Cauchy integral with
an omitted lower-half-plane residue. Only positive real A is needed
in the proposed specialization, so complex square-root choices need
not be extended. Both signs of z must be retained for complex w;
taking an imaginary part is not a complex-parameter sine identity.

[DLMF7.5.1](https://dlmf.nist.gov/7.5.E1) states exactly

    F(z)=i*sqrt(pi)*(exp(-z^2)-W_F(z))/2.

Read this relation, its defining-function references, and
[Dawson's definition7.2.5](https://dlmf.nist.gov/7.2.E5).
These identify the special function in C032y's D_F with a standard
transform input. No Fourier transform of e is supplied by that
identification alone. C032y already covers entireness and reflection
through DLMF7.2.3/7.4.3; no reproof is called for.

[DLMF1.14(i), (1.14.1)-(1.14.3)](https://dlmf.nist.gov/1.14)
defines the transform with positive exponential and factor
1/sqrt(2*pi). Its inversion statement assumes absolute integrability
and bounded variation near the evaluation point, returning the
average of the one-sided limits through a principal-value integral.
Read the definition, all these hypotheses and the whole inversion
statement. A later proof must convert the convention and verify the
relevant density's hypotheses, including frequency zero. It must
not claim an absolutely convergent double Fourier integral from an
oscillatory representation alone. C032m's Haslinger2.39 coverage
supplies compact holomorphic integration only after actual integrable
dominators have been supplied. Tonelli/Fubini or justified inversion,
not formal delta functions, must identify the proposed transform.

For an effective archimedean bound, read
[DLMF5.7.6 and its domain](https://dlmf.nist.gov/5.7.E6):

    psi(z)=-gamma_E+sum_(k>=0) [1/(k+1)-1/(k+z)],
    z not in {0,-1,-2,...}.

This supplies an exact series at z=1/4+i*r/2. It does not supply a
ready uniform tail for the product with e; bounding that product
and any finite series remainder remains mathematical work. Keep
the difference in each summand together. No need to import or
differentiate a non-effective Stirling remainder was identified.

DLMF7.12(i)'s erfc expansion and remainder domains were inspected
as a comparison. They do not license unrestricted remainder bounds
on both translated complex arguments. The proposed attempt should
use the exact Gaussian representation instead; no erfc asymptotic
estimate is imported into its coverage.

## Reused explicit formula and hypotheses

Reuse notes1572/1555's primary coverage of Chirre-Goncalves,
*Bounding the log-derivative of the zeta-function*, Math. Z.300(2022),
1041-1053, [Proposition5, p.1044](https://link.springer.com/content/pdf/10.1007/s00209-021-02820-9.pdf).
Rechecked the full statement and Fourier convention in publisher
article text. For even h analytic on |Im(a)|<=1/2+epsilon,
epsilon>0, with strip decay O((1+|a|)^(-1-delta)), delta>0,
it gives the unconditional all-complex-zero sum as the gamma
integral/(2*pi), plus2*h(i/2), minus log(pi)*hat(h)(0)/(2*pi),
minus the complete sum Lambda(n)*hat(h)(log(n)/(2*pi))/(pi*sqrt(n)).
The Fourier kernel is exp(-2*pi*i*a*y). Neither RH nor real values
of h on the real axis is an extra hypothesis of this proposition.
The neighboring representation lemma does assume RH and is excluded.
There is no independent proof of Proposition5 there; it cites
Carneiro-Chirre-Milinovich Lemma8. Its previously inspected statement
and citation proof remain covered by notes1572; upstream books/proofs
were not newly inspected. That version's real-valued-test hypothesis
must not be silently extended to complex w.

The proposed strip |Im(a)|<=3/4 would meet epsilon=1/4 if the
uniform inverse-square bound is proved. This is a comparison of
required hypotheses, not a proof that e satisfies them. Its actual
evenness, analyticity and strip bound must be checked explicitly.
All-zero versus positive-ordinate normalization, multiplicity and
the pole evaluations remain obligations. Trivial zeros are already
accounted for by the gamma term. There is no imported positivity.

Connes2402.13082v1 Section2/(4)-(9), p.4, remains an alternate source
under notes1572's Mellin hypotheses; it was not reopened. Its
RH-dependent real-spectrum reading is excluded. An algebraic
spectral decay assertion does not automatically verify those Mellin
conditions or supply a prime-side tail.

## Search evidence and remaining specialization

Queries actually run: `"Guinand" "Weil" "Dawson" integral`;
`"explicit formula" "integrated" "Gaussian" "zeros"`;
`"Bounding the log-derivative of the zeta-function" "Proposition 5"`;
`Dawson integral Fourier transform sine DLMF 7.7.3`;
`"Guinand" "Dawson" "Gaussian"`;
`"Gaussian" "Cauchy transform" "Fourier transform" Dawson`.
No inspected theorem gives the exact uniform integrated-pair
evaluator with effective tails. The search result for Yurekli,
*The Dawson Transform and Its Operational Properties* (2026),
and the Cauchy/Fourier-transform paper are unread leads, not inputs.
Search snippets and nonprimary web claims were not evidence for
any mathematical conclusion. Failure to find a match implies no
novelty or absence assertion.

DECISION SPECIALIZE: general theorem coverage is adequate for one
later attempt, importing the explicit formula and exact transforms.
The source change from1572 is7.7.3's entire complex-argument integral
representation and its standard Dawson relation/inversion interface.
It removes the need to guess an unassessed special-function transform.
No essential source remains inaccessible. The specific work left is:

1. Verify the exact even spectral test and a common strip dominator
   C/(1+|Re(a)|)^2 on |Im(a)|<=3/4, uniformly in sigma,w. Any
   integration by parts must record its boundary terms and uniform
   derivative integrability, and handle small Re(a) separately.
2. Obtain the ordinary Fourier transform in the stated convention
   from the exact representation with fully justified exchanges or
   inversion. Check both frequency signs and zero, all scaling
   factors and the entire primitive normalization at w=0.
3. Apply Proposition5 with the actual complex divisor and derive
   explicit prime-power and gamma-integral truncation errors tending
   to zero uniformly on the closed parameter set. Mere qualitative
   convergence or an asymptotic with unknown constants is not enough.

Success means all three statements with proved constants/errors.
Otherwise record the precise failed bound/interchange and stop the
attempt without expanding the disk, dictionary or variation budget.
This is an application of existing tools, not creative central-gap
work or an approved numerical solve. No derivation is done in this
literature turn. The new continuation receives the supervisor's
separate approval before invocation. Full matching Mathlib coverage
is unchecked/unknown. Actual-divisor, multiplicity, zero-ordinate and
strip/counting qualifications persist; probability use also retains
C032j/m/q's finite-zero, heat and fixed-v1 qualifications.

Source transcription correction1584 (18 November2026): restored the
1/sqrt(A) multiplying Dawson F in the displayed DLMF7.7.3 input.
The previous version omitted it. Only A=1 is approved here and used
in C032z; this correction changes no approved specialization scope.
See the separate source-gate approval1584, not a correctness audit.
