# Third-width normalized determinant: bounded test1745

TARGET: Attempt one uniform sign enclosure for the normalized third-order width determinant at y=1/8,3/16,1/4 on [1,2], including all coalescing widths; retain the full divisor and park if the enclosure contains zero.
CHECKED: 2026-11-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1745 completed the exact-kernel/stronger-result search and C032/C033 duplicate/failure screen; queries and inspected cases are in drafts/literature/2026-11-19-third-width-source-notes-1745.md. No matching theorem located in the bounded screen; no novelty inference.
SOURCE_EVIDENCE: de Boor, Divided Differences, SAT1 (2005) pp58-64, Proposition35/Definition37, Proposition43, (45)/(52) https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf ; Novaes--Torregrosa UAB July2015 p2 and Section2 pp5-6, (5)-(9)/nonvanishing Rolle proof https://mat.uab.cat/dpt/Publ/prep/p13_15.pdf ; Sra fixed2611.00345v1 Proposition A.6(ii), pp15-16 https://hexagonmath.org/pdf/2611.00345v1 ; reused qualified FLINT https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html and Bellotti--Wong Theorem1.1/Section5 https://arxiv.org/pdf/2412.15470v2 via coverage1726; Haslinger Theorem2.39 pp67-68 https://www.mat.univie.ac.at/~has/scriptneu.pdf via C032m/n.
COMPARISON: Known interpolation/ECT tools handle confluent sites only after their smoothness and all-prefix nonvanishing hypotheses are checked. Fixed-K Hankel positivity is in different variables. The audited C033g first-ratio derivative neither controls the third minor nor supplies its second-order relative errors.
GAP: Prove the C^2 width specialization, full-divisor signed core/remainder/E comparison after normalization, and all distinct/confluent cases with an explicit strict margin or rigorous refutation. Existing first-order errors cannot be differentiated or divided by vanishing width gaps without proof.
REASON: Exact changed-order source coverage is complete for one independently testable estimate. The required kernel estimates are unpaid local research obligations; no new external theorem or sign is assumed. New ready assessment requires separate next-turn approval, not another search of unchanged coverage.
SCOPE: Exactly C032j/m/n and C033f/g's full qualified actual divisor and k_sigma on widths [1,2], at the three fixed positive arguments; Gaussian half-variance, multiplicity/conjugation, fixed-v1 heat inputs, corrected inclusive count, V(3*10^12) and external certified first-zero separation persist.

## Exact test and allowable specialization

Use the existing definitions

    k_s(y)=exp(-E_s(i*y))*sin(A_s(y)),
    A_s(y)=2*pi*integral_0^y p_s(x) dx,
    f(s)=k_s(1/8)>0,
    r_2(s)=k_s(3/16)/f(s), r_3(s)=k_s(1/4)/f(s).

For 1<=s_1<s_2<s_3<=2 the target remains

    Delta_3=det[(1,r_2(s_i),r_3(s_i))_(i=1,2,3)]
               /[(s_2-s_1)*(s_3-s_1)*(s_3-s_2)].

Seek epsilon in {-1,1} and c>0 such that epsilon*Delta_3>=c
uniformly, with a justified continuous extension and the same bound
when the lower two, upper two, or all three widths coincide. Include
endpoints. No orientation, extension or margin is assumed.

Source-notes1745 lists the exact missing applicability work. First
justify second width derivatives of the profile, removable quotient,
E/A primitives and ratios using common summable/integrable majorants.
C032n's C^1 conclusion alone is not this result. Then obtain new signed
core information and errors through the necessary derivative order,
retaining every remaining divisor member and the full E correction.
The first core's common tiny Gaussian factor and the positive f must
be handled before comparing errors. Keep sine corrections explicit.

de Boor supplies general divided-difference/Hermite tools; prove the
specialization for the two general ratio columns rather than citing
his polynomial-column formula(45) as the desired identity. If the
all-prefix-Wronskian criterion is used, check its C^2 hypotheses,
every prefix and every width. The ordering (1,r_3,r_2) is an available
applicability choice because C033g already controls r_3'; track the
column permutation when returning to Delta_3. No higher Wronskian
has been evaluated or signed. Strictness away from collisions alone
does not establish a uniform bound on the closed ordered simplex.

Import the general source tools with precise citations; only the
kernel-specific regularity, error and determinant specialization may
be derived. No reproof of the external first-zero computation,
zero-counting theorem, general heat or ECT theorem is warranted.
If new essential external mathematics is needed, record REVIEW_REQUIRED
before dependent work instead of silently adding it to this scope.

## Discriminator and remaining gaps

One bounded attempt only. A complete uniform strict enclosure supports
this finite-order mechanism. A rigorous zero or opposite signs of
the normalized determinant refutes it, including a legitimate zero
of the confluent extension if the stipulated positive margin is the
claim. A zero of the raw determinant at equal widths is automatic
and supplies no evidence. A coarse enclosure containing zero is
inconclusive: record actual and required bounds and park the attempt.
Do not extend a grid or drop the remainder to manufacture a sign.

A later exclusion for two ordered sign changes is the plausible use;
its Borel/atomic hypotheses require separate review. No all-order
total positivity, variation cap, unrestricted J_eta cancellation,
output positivity, moments/tails or unsmoothed Xi realization follows
here. Sra's fixed-K Hankel result supplies no automatic nonlinear
preserver. Stops1534/1536/1711/1725 and audit-route closure1744 remain
preserved. Full matching Mathlib coverage is unchecked and unknown.
This is established-route development, not a creative central RH
mechanism or a complete candidate.
