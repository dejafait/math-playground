# Full-grid polynomial dual — proposed bounded continuation

TARGET: Test a P-dependent full-grid polynomial dual in C645y's identity (10) for mean_u ||kappa_u||^2>=c exp(-n/16)D_single,n in L649's unchanged integer-mass angular family.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the five-primary-source comparison in 2026-11-02-full-grid-markov-remainder.md, including finite-support, prescribed-denominator and logarithmic-derivative rational-interpolation searches; no matching quantitative theorem was identified. Local C645g/n/o/x/y, L646/L648/L649 and the relevant prefix/recovery stops were compared. This is bounded coverage, not certified originality.
SOURCE_EVIDENCE: Direct primary PDFs: https://arxiv.org/pdf/2106.05098v2 (Beckermann--Bisch--Luce, (1.1), Theorem 2.6/(2.15)--(2.16), pp.1,8); https://arxiv.org/pdf/1104.5358v1 (Frazho--ter Horst--Kaashoek, (2.1)--(2.5), Proposition 2.1 and full proof, pp.4--6). Reopened 2026-11-02. Reuse the companion five-source comparison and the rotation-averaged-anchor-line-hankel assessment's inspected Parseval, Hardy projection and residue inputs for finite algebra only; exact additional source URLs and qualifications appear below and in those assessments.
COMPARISON: Known free-pole Pade remainders, capacity lower rates and prescribed-denominator best uniform errors do not cover this finite model-space interpolation norm. C645y already supplies the full polynomial identity and a prefix obstruction; writing the identity again, estimating raw samples, or reproducing exact recovery would add nothing.
GAP: Find a P-dependent certificate using every grid coefficient with its full spatial/angular norm cost sufficient for the relative squared rate 1/16, or a rigorous obstruction to that particular certificate. Uniform constants, separation-free control and the link to L649's precise component must be justified.
REASON: This is the specific finite-support difference left by the completed source comparison. A nonlinear family-dependent certificate can use the degree-M constraint absent from a universal unit-pole dual; success is not assumed. The separate literature recovery turn has now repaired the missing direct URLs and approved this unchanged finite-algebra scope; no mathematical attempt is performed in that turn.
LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this saved ready assessment. This turn repairs provenance and checks source accessibility and scope, reusing completed searches rather than reopening the mathematical comparison.
SCOPE: One bounded proof attempt using the complete C645y identity (10), finite polynomial/residue/Fourier algebra and a dual allowed to depend on P. No new general Markov, extremal approximation or Remez theorem, replacement interpolation table, prefix-only argument, or relaxation to fractional residues is preapproved.

## Exact inputs and target

Keep n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100,
t_j=j/n, b_j=t_j u, |u|=1. The common distinct pole set Z
has Re(a)=x, |a|<=R-eta and x in Z. Original simple-pole
residues r_a are positive integers; M=sum r_a<=n/3.
There is no separation, symmetry or integer-coefficient assumption.
Keep B_u's conjugated denominator angle, all n grid factors, all
spatial modes, and normalized spatial/angular measures. Set

    P(z)=product_a(z-a)^(r_a),    L=P'/P,
    A_u(z)=product_(j<n)(z-b_j),
    D_u(z)=product_(j<n)(U-conjugate(b_j)*z).

C645y supplies the already recorded identity

    A_u V_u + P h_u = B_u(x) R^(-n) D_u P',
    deg V_u<=M-1,    deg h_u<=n-1.                       (10)

Do not replace P by its square-free part without tracking residues
and degree. L649 supplies c(u), T_u and
kappa_u=(I-T_u^*T_u)c(u), with diagonal quantity

    D_single,n=sum_a r_a^2 mean_u |B_u(x)/B_u(a)|^2
                                      /(U-|a|^2).

The target requires a positive c and onset independent of all
admissible families. Its ratio normalization must be retained;
an absolute lower bound alone is weaker when D_single,n grows.
The relation between C645y's full analytic component and kappa,
including norms and conjugations, must be checked in the attempt,
not inferred from their informal names. Both canonical results
are separately unaudited; this assessment does not audit them.

## Main gap, use, and discriminating test

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs are open. This synthetic full detector and its realization
remain independent requirements. The proposed estimate would supply
the sufficient constant-input energy comparison, hence support the
angular detector; it would not establish Xi realization or signs.

Intermediate target: use (10) and the permitted zeros of degree-M P
to construct one P-dependent polynomial dual that bounds the full
retained component, and evaluate the entire dual cost at rate 1/16.
This is a proposed calculation, not a newly derived lemma. The
certificate must depend on the complete family if that is what
escapes C645x's universal unit-pole dual obstruction.

Continue with an actual uniform lower bound, or an explicit finite
certificate leaving one identified, quantitatively bounded cost to
test. Merely posing another minimization or restating (10) is not
an advance. Abandon this proposed dual if its exact cost misses the
required relative rate, or if it uses only the first ceil(n/2) grid
coefficients, ambient recovery, or an unproved extension of a source
theorem. A counterexample to the whole target must satisfy every
integer-mass/common-pole condition and control the complete energy;
a dual failure is not such a counterexample.

Preserve the existing stops: C645n/L649 concern recovered responses;
C645y stops the initial prefix; L646 stops exact-output recovery;
L648 stops one reflected input; C645x's obstructing mixture has
fractional residues and more than n/3 distinct poles. The new test
must not repeat those constructions as an alleged general disproof.
No new lemma or mathematical script was written in this source turn.

Full matching Mathlib coverage has not been checked. The ready
Fourier/residue assessment covers supporting inputs only. Any
essential new external theorem requires a new literature gate.

Source evidence and qualifications are retained in
[the completed comparison](2026-11-02-full-grid-markov-remainder.md).

## Separate source-gate repair, 2 November 2026

The two primary arXiv PDFs linked in SOURCE_EVIDENCE were accessible.
Rechecked the Nehari hypotheses, statement and both proof directions:
bounded matrix symbol, backward-shift-invariant Hardy subspace containing
constants; the restricted distance equals the restricted Hankel norm.
The lifting and projection arguments do not evaluate that norm for this
family. No theorem-level identification with kappa is asserted.
Rechecked the Markov infinite-support definition (1.1) and disk Theorem
2.6: real support left of -1, conjugate-paired nonreal interpolation
points, and upper interpolation-error bounds. These do not supply the
required lower energy estimate. The earlier essential proof-case
inspection (2.15)--(2.16) is reused, not claimed as newly completed work.

Additional inspected-source provenance remains directly available at
[Baratchart--Yattselev v1](https://arxiv.org/pdf/0804.2206v1),
Section 2/Theorem 2.3 and (3.51)--(3.53), and
[Beckermann--Reichel author PDF](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/bernhard_beckermann/abs/paper15.pdf),
Theorem 6.1 and proof of (c). Their earlier comparisons are reused;
neither text was newly reread in this repair.

The previously inspected
[Levitt author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf)
returned an accessibility error through the web tool on this turn.
Its saved theorem and normalization notes remain reusable for the
unchanged scope; no new hypothesis depends on retrieving it again.
This single retrieval error is not evidence of a persistent source
blocker. Full matching Mathlib coverage remains unchecked.

Outcome is a process repair, not new overlap evidence or mathematics.
EXPLORE is retained for exactly the saved target and SCOPE. No new
lemma, bound, counterexample, or script was produced. The next attempt
must check the component/norm link and cost the whole dual; failure
of that certificate still does not refute the target.
