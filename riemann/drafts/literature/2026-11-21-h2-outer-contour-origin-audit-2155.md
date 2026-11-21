# Fixed outer-contour origin audit: specialization coverage

TARGET: Audit the five outer-rectangle inverse-power functionals I_k=(2*pi*i)^(-1) integral_(boundary Omega) z^(-2k) F_z/F dz, k=2,...,6, for Omega={|Re z|<100,|Im z|<1/2} and 0<=lambda<=1/20, retaining origin residues and opposite-pair multiplicities; decide whether they independently determine the signed H2 head and whether C919a transfers to the rectangular complement.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step2155 exact-target theorem/duplicate comparison in 2026-11-21-h2-signed-contour-head-review-2154.md; its inspected residue/Laurent hypotheses and accepted local product/tail inputs cover this narrowed analytic audit. No additional discovery or numerical calculation was performed.
SOURCE_EVIDENCE: NIST DLMF 1.10(iii)-(iv), (1.10.6)-(1.10.9), https://dlmf.nist.gov/1.10 ; Deng-Yang-Lu arXiv:2608.11520v1 Section2.1/Lemma2.3 and complete proof, https://arxiv.org/html/2608.11520v1#S2 ; Polymath1904.12438v2 Theorem3.2, https://arxiv.org/html/1904.12438v2#S3 , with the audited local strip specialization C919a; L018,L019,L058,L874,L919,C919a,C919b.
COMPARISON: General finite residues and Laurent coefficient extraction are known. L919 already supplies the absolutely convergent opposite-pair powers, L874 the origin logarithm germ, C919a the per-class negative-part estimate and C919b the vertical boundary. The needed difference is their exact combination for this fixed rectangle, including the extra weight pole, rather than a new residue theorem or numerical integration method.
GAP: No corrected identity, independence conclusion or rectangular-tail inequality has been derived in this assessment. Numerical head margin, complex quadrature evaluator/error budget and all higher-degree/global signs remain unresolved; the audit must not assume them or infer them from qualitative nonvanishing.
REASON: A five-functional exact obstruction test can decide whether the outer-only proposal merely returns exterior information before spending work on a new evaluator. It addresses the source mismatch found in step2155 and does not repeat the old moment-box/Rayleigh calculation.
SCOPE: Only TARGET, one analytic audit classified REPRODUCTION. No numerical integrals, scripts, finite-zero census, pole omission, changed contour, hole radius, precision/mesh sweep or new heat approximation. This newly written ready continuation requires separate supervisor approval before research.

The main gap remains L030-L032/C032a all-degree actual-Xi algebraic
mixed positivity. Define the proposed rectangular head using exactly
L919's algebraic rank-one summands and D=diag(1,200,40000), but keep
only opposite classes inside Omega. This is a target definition, not
an asserted relation to the contour integrals. Its prospective use is
a finite H2 head comparison with 1/2000000000 after a valid remainder
estimate. No positive head eigenvalue or feasible margin is assumed.

Essential inputs: L018 for the initial open strip; L019/L058 for the
actual family, entirety, real type and positive origin; L874 only for
the logarithm-germ convention (none of its contact hypotheses);
L919 for normalization, full opposite-pair identities and convergence;
C919a for the already established strip and negative-part proof;
C919b for its audited vertical boundary under the stated Decimal
contracts. The new audit must explicitly verify both horizontal
endpoints and use evenness for the other vertical side. It must not
silently upgrade qualitative compact nonvanishing into a numerical
lower bound. No RH, simple/real-zero census, continuous enumeration,
unpaid S_k value or cross-notebook result is assumed.

Fixed budget: exactly the five scalar functionals k=2,...,6 on the
one displayed rectangle and band, their 3-by-3 matrix assembly, and
one comparison of the radial versus rectangular complementary zero
sets. Use a finite-contour residue theorem; pay the origin Laurent
coefficient from the normalized local logarithm and each nonzero
zero's full multiplicity. Show how all-zero residues convert to
opposite-pair sums without losing a factor of two. Any infinite
exterior sum must use L919's proved convergence, without taking an
uncontrolled contour limit.

For the shell question, inspect the actual set difference, including
radial equality and open-rectangle conventions. A lower bound for
the original full tail cannot simply be subtracted through a signed
matrix. Either justify the required complementary-subset bound from
C919a's opposing-component proof, with conjugation and multiplicities
retained, or record precisely why it is unavailable. This is covered
routine specialization, not a claim that the transfer already holds.

Decisive test: determine exactly what these five I_k specify without
independently supplied S_2,...,S_6. If they reduce to exterior data
and reconstructing the head needs those unpaid coefficients, stop
the outer-only head proposal and preserve the obstruction. If an
independent head observable survives, record its exact prerequisites
before considering any implementation. Do not declare that all
contour methods are impossible, that a punctured contour is covered,
or that this test signs the head. No mathematics was carried out in
writing this assessment. Full matching Mathlib coverage is unchecked.
