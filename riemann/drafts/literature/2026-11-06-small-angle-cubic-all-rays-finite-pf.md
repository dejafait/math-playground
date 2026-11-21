# Small-angle cubic with finite PF information — completed source comparison

TARGET: Test whether, for every integer m>=1, P_m(z)=(1+z)(1+2cos(pi/(m+2))z+z^2) has a PF_m ordinary coefficient sequence and D_(r,k)>=0 for every r>=1 and k>=1 while having a nonreal zero.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact-family, cubic Toeplitz, finite-PF, rectangular-Schur principal-specialization and weak solid-minor searches; local comparisons with L832/L838/L839 and the two matching stops. Found a stronger known finite-PF family in Adm–Garloff–Tyaglov (5.9); no inspected source settled the combined all-ray assertion. Queries and limits below; no originality inference.
SOURCE_EVIDENCE: Rechecked Alexandersson https://arxiv.org/html/1208.5607v1 Theorem6 p.5 and Section3.2 pp.11–12; Katkova https://arxiv.org/pdf/math/0505174v1 Definition2/(8) p.4 and TheoremB p.5; Adm–Garloff–Tyaglov https://www-home.htwg-konstanz.de/~garloff/JMAA-3_Adm_Garloff_Tyaglov.pdf Theorems5.7/5.8 and (5.9), printed p.161, (5.11)–(5.12) p.162. Reuse prior finite-formula proof-case coverage; original Schoenberg proofs remain unread.
COMPARISON: The finite-PF component is covered by Schoenberg's known equal-angle family, not a prospective discovery; exact finite determinants cover the method for the remaining signs. L839 covers only its fixed cubic and L838 only adjacency. None of these local results imports the new family's all-ray conclusion.
GAP: Replay the exact coefficient and parameter match, import the finite-PF input, and establish or refute the complete all-rank signs at both interior shifts, plus boundary/exterior shifts and a nonreal zero. No all-ray formula or sign certificate for this family was derived in this literature turn.
REASON: Essential source comparison is complete for the unchanged TARGET. A separate REPRODUCTION test may specialize the finite formula; cite known PF results instead of reproving them. This review changes the finite-PF component from proposed construction to documented source overlap, while leaving the sign conjunction unresolved.
LITERATURE_REASON: The changed angular parameter and arbitrary finite PF order lie outside the supplied fixed-cubic assessment; essential source comparison is missing before any mathematics on this family.
SCOPE: Exactly TARGET, every finite integer m>=1, zero-extended ordinary coefficients a_j=[z^j]P_m and D_(r,k)=det[a_(k+j-i)]_(0<=i,j<r); PF_m means all ordered minors through rank m. Distinct complex variables and tied moduli are covered; no strict signs, coalescing-root limit, infinite-degree transfer or Xi realization is approved.

## Completed review, 6 November 2026

The main gap is L030–L032/C032a actual-Xi mixed positivity. The
intermediate target is the unchanged TARGET. Its downstream use is to
test whether adjoining any prescribed finite PF band repairs L839's
weak-sign detector. Success would restrict that detector, not give Xi
signs or RH. Continue only toward a symbolic certificate for every m,
rank and shift; one negative determinant or failed PF requirement
rejects the conjunction. Finite samples cannot meet that threshold.

### Inspected inputs and applicability

Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
[math/0505174v1](https://arxiv.org/pdf/math/0505174v1), Definition2/(8)
and TheoremB, printed pp.4–5, uses the ordinary, zero-extended upper
Toeplitz matrix and every ordered minor through order m. The sufficient
criterion is a real polynomial with positive constant and no root in
the open sector |arg z|<pi*m/(m+1); boundary roots are allowed. Import
this named Schoenberg theorem, not Katkova's separate PF44 inference.
Its proof coverage is reused from the prescribed-finite-PF assessment.

A closer overlap is in Mohammad Adm, Jürgen Garloff and Mikhail Tyaglov,
*Total nonnegativity of finite Hurwitz matrices and root location of
polynomials*, JMAA467 (2018), 148–170,
[published author PDF](https://www-home.htwg-konstanz.de/~garloff/JMAA-3_Adm_Garloff_Tyaglov.pdf),
Theorem5.7 and (5.9), p.161. It records Schoenberg's known PF_k family
g(z)=product_(j=1)^d(z+exp(i*phi*(d-2j+1))), phi=pi/(d+k-1).
The source-level match is d=3, k=2m+2, giving the three phases
pi/(m+2), 0, -pi/(m+2). This is stronger finite-PF coverage than
requested; the later certificate should record the polynomial match
and restriction to minors through m. Theorems5.7/5.8 and the quadratic
criterion (5.11)–(5.12), pp.161–162, were inspected as comparisons.
No product-necessity assertion is imported. Original Schoenberg
*On the zeros of the generating functions of multiply positive
sequences and functions*, Ann. Math.62(3) (1955), 447–471, is the cited
origin, not a newly read proof. This overlap supplies no all-ray signs.

Per Alexandersson, *Schur polynomials, banded Toeplitz matrices and
Widom's formula*, EJC19(4) (2012), P22,
[1208.5607v1](https://arxiv.org/html/1208.5607v1), Theorem6 p.5,
assumes distinct complex elementary variables, s_0=1, and gives an
exact finite subset sum at every positive rank. Its Section3.2,
pp.11–12, including Lemma15/Proposition16 and the complete formula
proof, was rechecked; the earlier assessment's case coverage is reused.
Source c is our shift, source matrix size is our rank. Equal moduli
are permitted. Import this formula without reproof; it asserts no
nonnegativity. No recurrence oscillation or infinite asymptotic theorem
is needed for the proposed finite test.

For the candidate variables 1,exp(i*theta),exp(-i*theta), the later
test must check the elementary-coefficient identity and distinctness
at theta=pi/(m+2), including m=1. Each finite parameter is inside
0<theta<=pi/3; theta=0 is an excluded limiting case, so no confluent
or uniform-in-m formula is required. Do not identify variables with
zeros: zeros correspond to -1/x. The angular endpoint in the sufficient
sector theorem is included; weak determinant zeros must also be kept.
The interior shifts1/2 use the finite formula; shifts3 and k>3 require
direct zero-extended matrix checks. This exhausts the proposed finite
scope without invoking the blocked infinite-source route. Their values
have not been calculated here.

### Search and recorded failures

Local reads were confined to L832's sector citation, L839's full
audited certificate, L838's imported inputs, the existing finite-PF
and all-fixed-shift assessments, and their matching ATTEMPTS/history.
No existing local certificate for this changed family was found.
L838's adjacency failure is preserved; the new conjunction adds every
shift. L839's finite-class stop is preserved; the new conjunction adds
arbitrary prescribed finite PF information. Neither historical stop
decides the combined target. The persistent Bultheel source blocker
stays parked and is not essential here.

External query strings included '"Toeplitz" "1+2cos" "Pólya"',
'"Schur" "rectangular" "principal specialization" roots unity
positivity Toeplitz', '"nonnegative" "solid minors" "Toeplitz" cubic',
'"Toeplitz" "cos" "cubic" "nonnegative"', '"Pólya frequency" "cubic"
"cos"', '"1+z" "cos" "Schoenberg"', '"principal specialization"
"Schur" "sine" product formula', '"(1+z)" "cos(pi" "Toeplitz"',
'"cos" "cubic polynomial" "frequency"', '"Toeplitz" "1,q,q^2"
determinant', and '"Schoenberg" "solid minors" nonnegative'.
The searches did not establish a full matching sign theorem or novelty.
Rectangular-Schur/root-of-unity and Toeplitz-minor papers appeared as
leads; their indexed extracts were not accepted as theorem evidence
or essential new inputs. The inspected finite formula already covers
the required method. Reuse the earlier Fomin–Zelevinsky strictness
comparison: strict-minor criteria do not automatically cover zeros.
No repeated access attempt or general search is needed before this test.

DECISION is SPECIALIZE because sources settle the finite-PF component
and supply the exact method, while the combined all-ray signs remain
unverified. The mathematical continuation is REPRODUCTION, not a
creative central-Xi mechanism. No new signed Xi estimate justifies
creative routing. Full matching Mathlib coverage remains unchecked.
No lemma, mathematical script, determinant evaluation or new sign
result was written in this review. Any later proof and citation
specialization belongs in a canonical lemma only after mathematics.

## Original nomination (historical; superseded by completed review)

The main gap remains L030–L032/C032a actual-Xi mixed positivity.
This proposal asks whether adding any fixed finite PF order can repair
the abstract detector refuted by L839. A successful counterexample
would rule out that more restricted completion mechanism; it would
not prove actual-Xi eventual signs or settle RH. Failure would reject
this ansatz, not establish a detector theorem.

Next turn is literature-only. Reuse ready finite-formula coverage and
the local finite-PF comparisons, inspect the primary sector statement
and the essential parameter cases, and search the exact family under
rectangular Schur principal specialization and banded Toeplitz signs.
Do not reprove the imported determinant formula or sector theorem.
State explicitly whether repeated variables, angular endpoints or
rank-dependent zeros affect applicability; no strict sign assumption
may replace weak signs. Preserve the L839 finite-class stop and the
separate persistent infinite-source blocker.

Continue toward a separately approved mathematical test only if the
assessment covers this exact family for every stated m and the
boundary/exterior shifts can be tested exhaustively. A full symbolic
description, rather than finite-rank sampling, is the later success
threshold. A negative determinant or failure of the required finite
PF order rejects the conjunction. No period, sign or PF computation
has been performed as part of this nomination.

Contextual inputs: L839 for the completed unrestricted obstruction;
L832 for the actual-Xi finite-PF motivation and its precise sector
citation. L838 is a contrast, not a mathematical premise. Any use of
the new family will need its own coefficient/variable match and
nonreal-zero check. All-degree Xi signs, infinite-degree transfer and
Xi realization remain unresolved; no cross-notebook input is proposed.
Full matching Mathlib coverage is unchecked.

This is a prospective known-method specialization, not a justified
creative actual-Xi mechanism. No concrete independent signed Xi
estimate has emerged from the audit. The source gate is essential;
do not label its review or subsequent routine specialization creative
to satisfy scheduling preferences. No lemma or mathematical script
for this new family accompanies the nomination.
