# GC12 diagonal Landau--Mellin comparison: evidence2087

Literature only. No transform identity, new lemma, numerical experiment,
or GC12 bound is established here. This completes review2086's TARGET.

## Local relevance, duplicates and failures

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The intermediate question is whether the complete signed
GC12 diagonal transform admits a one-sided obstruction. A successful
test could bear on the low primitive upper downstream of C034r; the
high primitive upper, GC13/GC18 scale errors, full source energy and
mixed transfer remain independent gaps.

Read C034s(1)-(18), including its finite-cutoff errors and Section5's
explicit global limitation, and C034r's hypotheses/conclusion and source
scope. Reused the audit2086 supplied checkpoint. Targeted searches of
the coprime/GC12 literature paths and coprime ATTEMPTS found the existing
local stop, not a full diagonal Landau result. Read stops2076/2077/2079/2084.
Their positive-inverse, identity-only, direct-import and local-annihilation
failures keep their original scopes. No sibling notebook was read.

## Primary source comparisons

### Landau: boundary location is a hypothesis

J. Kaczorowski and J. Pintz, *Oscillatory properties of arithmetical
functions. I*, Acta Math. Hung.48(1986),173-185,
[primary article scan](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf),
p173, named Landau and Pólya theorems, and reference[8] p185.
Read those statements, not their later quantitative theorems/proofs.
The named Landau statement concerns a real function's Mellin integral:
its continuation is holomorphic on Re(s)>theta, on no larger whole
half-plane, and at the real point theta. It concludes infinitely many
sign changes. Pólya adds meromorphic continuation past that boundary.

Comparison: none of the complete-transform hypotheses is supplied by
C034s. A conjectured *real* pole at 2delta does not satisfy Landau's
regularity-at-the-real-boundary premise. Applying this sign-change
statement directly to M, or identifying theta from a selected zero,
would therefore be unsupported. A hypothetical upper may instead be
used in a proof by contradiction to define a nonnegative deficit;
this is an admissible future test, not a proved application here.
It still needs the deficit's actual integral/convergence boundary.
A continuation singularity behind an unknown convergence boundary
is insufficient evidence of a one-sided upper contradiction.

Original cited by that article: E. Landau, *Über einen Satz von
Tschebyschef*, Math. Ann.61(1905),527-550. The digitized original
[located PDF](https://www.digizeitschriften.de/download/pdf/235181684_0061/log53.pdf)
returned404; no original theorem/proof reading is claimed. This is
not essential to the present exclusion or a new Landau theorem import:
the named standard statement above was inspected in a primary article.

### Quantitative oscillation: a different boundary test

G. Bhowmik, O. Ramaré and J.-C. Schlage-Puchta, *Tauberian Oscillation
Theorems and the Distribution of Goldbach numbers*, JTNB28(2016),291-299,
DOI[10.5802/jtnb.940](https://doi.org/10.5802/jtnb.940),
[author working PDF](https://www.wsf.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/TauberianOscillations.pdf).
Read Theorem1.2/(1.1)-(1.5), PDF p2, and Section2 pp4-6.
For real B, set F(s)=integral_1^infinity B(x)x^(-s-1)dx. Its hypotheses include

\[
 \int_U^{2U}B(x)^2dx\ll U^{2\sigma_0+1}\eta(U),\qquad
 c=\limsup_{\sigma\downarrow\sigma_0}
 (\sigma-\sigma_0)|F(\sigma+it_0)|>0,\quad t_0\ne0,
\]
\[
 a=\limsup_{\sigma\downarrow\sigma_0}(\sigma-\sigma_0)F(\sigma)<\infty,
 \quad b=\liminf_{\sigma\downarrow\sigma_0}(\sigma-\sigma_0)F(\sigma)>-\infty,
\]
with positive increasing continuous subpower eta. Theorem1.2 gives
weighted dyadic measure lower bounds at thresholds b+c-epsilon and
a-c+epsilon. The proof uses both signs through positive/negative parts,
dyadic Cauchy--Schwarz and the nonreal boundary blowup; it does not
discard the negative part. The author working proof contains inconsistent
theta/sigma0 notation and apparent sign/subscript slips; no corrected
proof is imported. The publisher PDF was inaccessible.

Comparison: GC12 has no established L2 bound at the desired boundary,
no nonreal boundary blowup of its full transform, and no finite a,b
there. C034s's positive *real* local pole does not meet these conditions;
arbitrary multiplicity is also not automatically compatible with finite
first-order real limits. The theorem is a screened detour, not an input
proving an Omega result. The original Kaczorowski--Szydlo1997 Theorem4
was located on Numdam, but its extracted formulas were incomplete and
screenshots supplied no readable mathematical content in this interface;
no exact theorem or proof from it is claimed inspected or imported.

### Reciprocal-zeta continuation: extra conjectural hypotheses

K. Matsumoto, A. Nawashiro and H. Tsumura, *Double Dirichlet series
associated with arithmetic functions*,
[arXiv1801.04444v3](https://arxiv.org/pdf/1801.04444),10October2018.
Read class A/Theorem1.1 pp1-2; Assumption4.1/Lemma4.2/Theorem4.3 and
the initial Mellin--Barnes formula, contour justification, and zero-sum
convergence pp9-11. Their class A has absolute convergence for Re(s)>d>0,
meromorphic continuation with at most a simple pole at d and polynomial
growth in fixed vertical strips. Theorem4.3 treats
sum_{m,n} tilde_alpha(n)m^(-s1)(m+n)^(-s2), where
Phi(s;tilde_alpha)=Phi(s;alpha)/zeta(s), alpha in A.
It additionally assumes every nontrivial zero is simple and
1/zeta'(rho)=O(|rho|^B). The zero-residue series uses that assumption;
the contour proof also retains good heights and gamma decay.

Comparison: this is an additive kernel with a single modified coefficient,
not GC12's coprime two-coefficient sum, rho weight and ratio window.
Both simplicity and the global derivative estimate are unavailable here.
It supplies no direct continuation or uncanceled-pole conclusion for
the present target. Its proof was read to identify these exact barriers,
not to import the theorem with dropped assumptions.

### Convolution does not guarantee a surviving pole

R. Pérez-Marco, *Monodromies of singularities of the Hadamard and eñe
product*, [author PDF, file enemonodromy11](https://webusers.imj-prg.fr/~ricardo.perez-marco/publications/articles/enemonodromy11.pdf),
retrieved21November2026; no version date verified. Read Proposition2.1,
Theorem2.3 and their proofs pp7-8. The former represents the Hadamard
product of holomorphic germs by a circular convolution inside their
radii of convergence. The latter locates possible principal-branch
singularities among products of input singularities, by contour deformation.
It asserts an inclusion, not survival or a sign for every candidate.

Comparison: no identification of GC12's full transform with that
coefficientwise product has been proved. Neither the theorem's direction
nor its object supplies the missing positive real singularity.

[NIST DLMF2.5(i)](https://dlmf.nist.gov/2.5), equations2.5.1-2.5.7,
was inspected as supporting Mellin coverage. Its convolution formula
requires a common strip; its residue expansion explicitly assumes
meromorphic continuation and a permissible contour translation and
retains a remainder integral. These are requirements, not a license
to drop the complete GC12 remainder. No new inversion is derived here.

## Queries, scope and access record

Searches included `Landau theorem Mellin transform one sided oscillation
signed function real singularity theorem`; `Landau oscillation theorem
Mellin transform one sided upper bound nonnegative function Kaczorowski
Szydlo`; `Landau theorem Mellin real pole positive coefficient omega plus
one sided theorem`; `Landau Über einen Satz von Tschebyschef 1905 527 550
pdf`; `diagonal double Dirichlet series square cutoff Mellin max m n
Landau singularities coprime Mobius`; `Mellin convolution singularities
contour pinch theorem poles sum analytic continuation Hadamard product`.
Generic/secondary hits were leads only. The accidentally broad Picard
search concerned the wrong Landau theorem and contributes no evidence.

Numdam2016 item metadata was accessible; publisher/Numdam PDF attempts
returned access errors. The author working PDF was readable as text;
one screenshot request timed out and others provided no readable image.
Shell downloads failed DNS resolution and provided no source content.
Landau's original remains unread; no further access campaign is nominated.
Matsumoto and Perez-Marco readings above were directly accessible.
No full matching Mathlib theorem was checked; unknown means unknown.

## Decision and independently testable continuation

The new evidence parks direct quantitative-oscillation and additive-series
imports. It does not disprove the diagonal mechanism or the desired upper.
The remaining candidate is one bounded nonnegative-defect test using
the complete transform, with its exact scope in assessment2087.
Pass evidence would be a rigorously justified full-transform obstruction
with all complementary terms controlled at the required real boundary.
An exact initial-domain identity alone is preparatory, not that evidence.
If the attempt still requires an unproved global continuation, rightmost
zero, sign, or unpaid complementary term, preserve the exact missing
condition and park that implication instead of repeating the local residue.
No mathematical exploration turn was spent in this literature review.
