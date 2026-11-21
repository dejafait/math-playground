# Central Hermite form — one exact product-kernel diagnostic

TARGET: Construct the denominator-cleared symmetric product-theta kernel for the degree-six central Jensen Hermite form and test its pointwise positive semidefiniteness on the one-outlier family.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step495's Hermite/Newton-sum, degree-six Jensen and theta Gram searches and scoped local duplicate/failure comparison are recorded in 2026-11-05-central-hermite-theta-gram.md; no inspected source supplies this particular product kernel or its sign, and no novelty is claimed.
SOURCE_EVIDENCE: Nathanson https://arxiv.org/pdf/1911.01745v2 pp.1–4, Newton-sum convention, Lemmas1–2/Theorem1 and both proof cases; Forrester https://arxiv.org/html/1806.10411v1#S2.SS2 (1.7), Sections2.2–2.3 and complete finite permutation/row-integration proof. L019/L021 supply actual positive K, all finite moments and absolute integration. Exact scope and source qualifications in the completed parent assessment.
COMPARISON: Known central degree-six hyperbolicity does not construct this kernel. L766's Toeplitz one-outlier stop is a different matrix; only its finite expansion method is reusable. The new difference is the nonlinear coefficient-to-Newton-sum map followed by a fixed symmetric product-moment realization.
GAP: The rational Newton sums, denominator clearing, homogeneous product-kernel identity and pointwise sign are uncomputed. No Gram factor, global PSD, theta cancellation or all-degree sign is assumed.
REASON: A fixed canonical kernel admits a discriminating exact sign test without root isolation or positivity-dependent factorization. Failure stops only this sufficient direct-sign mechanism and leaves integrated positivity and alternative representations open.
SCOPE: One fixed d=6,n=0 symbolic construction and one-outlier test, using the deterministic rules below. No numerical data, new lemma quota, degree/parameter sweep or automatic enlargement. Newly written ready coverage requires separate approval next turn before mathematics; it was not executed in step495.

## Exact inputs and construction to be attempted

Use L018/L019/L021 and the coefficient normalization only from L776
and L791/L792. With actual raw moments m_j=M_(2j), j=0,...,6,
gamma(j)=j! m_j/(2j)!, R_j=gamma(j)/gamma(0), fix

    P_6(x)=sum_(j=0)^6 (-1)^j binom(6,j) R_j x^j.

All m_j are positive and finite. Normalize by its nonzero leading
coefficient. Use formal Newton identities for the resulting degree-six
monic polynomial, s_0=6, through s_10, and form H=(s_(i+j))_(i,j=0)^5.
No real-root, principal-minor or PSD assertion is an input. GORZ's
known qualitative hyperbolicity must not supply a Gram construction.

Treat m_0,...,m_6 as formal variables for this algebraic construction.
After collecting each rational matrix entry, take the least common
nonnegative exponent N such that multiplication by m_6^N removes
every variable denominator. Verify existence and all constants, rather
than silently dropping factorials or choosing another denominator.
Verify that each resulting entry is homogeneous of total moment degree
N. If either property fails, stop with that explicit construction
failure; changing the realization is outside this attempt.

For each expanded monomial c product_(ell=1)^N m_(a_ell), use the
permutation average of c product_(ell=1)^N u_ell^(2 a_ell) as its
product-moment realization. Apply this linear rule entrywise to obtain
one real symmetric matrix polynomial F(u_1,...,u_N). If N=0, treat
the constant case separately. Establish the resulting matrix integral
identity with measure product K(u_ell)du_ell and the exact positive
scalar m_6^N. This is a proposed construction, not an identity proved
in this assessment. Check absolute integrability of every finite
monomial product using L021 and justify averaging by finite Fubini.
No matrix square root, unknown root measure, fitted functions, or
assumed positive principal minors may enter the construction.

The raw theta product remains in the final identity; formal moments
are an algebraic device, not a replacement of actual K by atomic data.
No analytic evaluator, software contract, model parameter or numerical
gamma enclosure from L778/L791/L792 is required. Their numerical
conclusions and L793 are not inputs. No cross-notebook theorem is used.

## One bounded discriminating sign test

For the single prescribed family (u_1,...,u_N)=(1,...,1,t), t>=1,
test whether F is positive semidefinite. Seek an exact rational vector
v and a rigorously negative polynomial value, or a negative leading
coefficient with a certified tail threshold. A finite plot, floating
eigenvalue or truncated polynomial is not evidence. Exact congruence
or principal-minor arguments may be used, retaining nullity cases.
No general multivariate sum-of-squares search or parameter sweep is
requested. If no decisive witness or sign proof is obtained in this
one symbolic test, save the partial algebra and report inconclusive.

A negative value must extend by continuity to a nonempty open set of
positive distinct variables. Since K is strictly positive there, this
would refute pointwise PSD of this particular actual product-kernel
representation. It would not refute the PSD of its integral, the known
degree-six hyperbolicity, any alternative Gram representation, or RH.
If the family passes, record that limited outcome and stop; the family
does not cover the full product domain and does not justify repetition.

The plausible downstream use is deciding whether direct positive
product-kernel signing is viable before looking for integrated theta
compensation or growing-degree analogues. Main actual-Xi all-degree
mixed positivity, global kernel signs and degree-uniform control remain
unresolved independently. This is conventional symbolic development,
not a new creative mechanism or a claimed discovery beyond the sources
checked. Full matching Mathlib coverage is unchecked. No kernel,
mathematical lemma or script was derived while preparing this review.
