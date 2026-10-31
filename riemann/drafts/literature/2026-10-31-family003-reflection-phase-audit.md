# Conditional reflection phase audit — source coverage

TARGET: Audit family 003's eq:reflection-cross-prime-phase and eq:reflection-pair-phase in separate full M_ref^2 sectors, checking all local exponent and collision-zero cases and row/slot/dual coefficient independence while retaining canonical cusp/Gauss inputs.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed reflection-phase scope review searched the exact labels, standard cubic/sextic reciprocity terminology and the local family003 assessments, audit notes, histories and ATTEMPTS. The source claims the exact identities; no matching completed local independent audit was found. Queries and unread leads are recorded in drafts/audits/2026-10-31-family003-reflection-phase-source-notes.md; no novelty claim is made.
SOURCE_EVIDENCE: OpenAI, The Quasi-Riemann Hypothesis, September 30, 2026, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, build/paper.tex: 519–588, 1551–1781, 1881–1914, 1935–2138, 6886–7030; terminal structural-support coverage at 2714–2866 is reused. Dunn–Radziwiłł, arXiv:2109.07463v3 (14 May 2024), Section 1.2 definition/(1.4)–(1.5), Lemma 5.2/(5.25) and Corollary 5.1 statements, including the unit-Fourier hypothesis and its proof use, were inspected.
COMPARISON: DR (1.4) is the needed standard cubic reciprocity theorem on coprime primary inputs; its definition matches the square of the source sextic symbol. Family003 states both target phase identities and their separation consequences. The task is a conditional reproduction audit of its finite algebra and support application, not a new reciprocity theorem or a reproof of the full cusp transform. Direct import of the full separation would bypass the retained-premise check.
GAP: Check every source local exponent, mark sign, pair type, coefficient dependence and zero case under the retained canonical inputs. No independent full cusp/sector construction or coefficient estimate, broader row-character reciprocity, hybrid norm, uniformity, global closure or Xi sign result is provided by this scope.
REASON: SPECIALIZE permits an independent check of a source-claimed implication needed by L541 Hypothesis 1. This assessment was written in a literature-only turn and must receive separate next-turn approval before mathematical invocation; no phase identity was proved here.
SCOPE: One fixed source datum, S containing primes over 6, one fixed L with support S and (18)|(L), M_ref=lambda^12 L^4, fixed h_0 and frozen nonresidual active factors, separate full residual R and active-slot P sectors modulo M_ref^2. Retain original zero-extended symbols, source supports, units/ramified valuations, active/inactive conductor changes, product-form slot antecedents and canonical cusp/Gauss identities below. No new moving mask, source coprimality or support deletion; no cross-notebook input.

## Precise citations and allowed inputs

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, 30 September 2026, pinned
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
uses the stable labels below. Line numbers refer only to this commit.

Retain the canonical cusp functions, full supported dual indices,
fixed-sector multiplier/additive dependence and simultaneous inactive/
absent-prime branch compatibility in `prop:completed-reflection`,
especially `eq:reflection-multiplier`, `eq:reflection-additive-phase`
and its item (3). Their derivation from cusp expansions is excluded.
Retain the one-prime finite Fourier/Gauss formulas
`eq:reflection-local-fourier` and the stated unit moduli of
tau_(p,m)^+/- for nonzero m modulo six. No evaluation of their individual
Gauss roots or use of `eq:signal` is requested.

Retain the finite marked expansion `cor:marked-reflection`, with
`eq:marked-reflection-phase` and its branch compatibility. The audit
must check the use of its collision-zero assertion, active mark's
minus sign, and changed conductors; it need not reconstruct the theta
identity or prove inclusion-exclusion produces the entire transform.
For final coefficient extraction, retain the frozen-factor/source
coefficient formulas used in L541; inspect their dependence and zero
restrictions, without proving their cusp origin or numerical bounds.

Dunn–Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv v3 Section 1.2](https://arxiv.org/html/2109.07463v3#S1.SS2),
equation (1.4), gives ordinary cubic reciprocity for primary a,b
congruent to 1 modulo 3. Use it on distinct primary primes, hence
coprime inputs. Its cubic-symbol definition is reduction of
a^((q_p-1)/3) to {1,omega,omega^2}; the pinned source defines chi_p
by the sixth-power exponent and states chi_p^2=(./p)_3. The audit
must justify this normalization/application on the unit support and
handle collisions by zeros separately. The supplementary laws (1.5)
are available for comparing conventions, not permission to remove the
retained cusp-sector construction.

DR Lemma 5.2/Corollary 5.1 require a primary modulus and a periodic
multiplier with Fourier transform supported on units. They are **not**
approved replacements for the full mask transform here: the source
retains nonunit h_0 and zero local frequencies. Its independent cusp
construction remains conditional. No GRH-dependent prime asymptotic is
an input to the requested finite audit.

## Exact claims and bounded test

Use the source definitions, for active good p and c=c_F r,

\[
 \sigma_p=\lambda^2c/p,\qquad
 \epsilon_p=-((\lambda^3c/p)\sigma_p)^{-1}\pmod p,
\]

and all three cases of omega_(p,j) in 1698–1705. The first target is
the source's `eq:reflection-cross-prime-phase`, which asserts a
unit-modulus xi_(p,j) independent of every other active prime:

\[
 \chi_p(\sigma_p)^{-2}\omega_{p,j}
 =\xi_{p,j}\chi_p(c/p)^{2j+2}.
\]

The second is `eq:reflection-pair-phase`, for distinct active p,q:

\[
 \chi_p(q)^{2j_p+2}\chi_q(p)^{2j_q+2}
 = (q/p)_3^{j_p+j_q+2}.
\]

These displays are source claims, not results of this review.
Check j=0,1,...,5, including the exceptional j=4 Ramanujan case and
the changed one-prime mark sign. The source states that residual
j_p=1 and active mark j_q=0 have trivial pair phase, but j_q=4
can leave a nontrivial phase. Keep every such nonresidual prime frozen;
do not broaden the target to moving exponent-four rows.

With r=F_act R P and F_act frozen, test the claimed separation after
fixing R and P separately modulo the **full** M_ref^2. The source's
canonical cusp coefficient, additive factor and fixed multiplier must
then be common; row-row and mark-mark factors and interactions with
frozen primes must have only their stated variable dependence. Check
the angular scalar, fixed h_0 including nonunits, units/ramified parts,
and empty active lists. A class of RP alone is not an approved substitute.

Check both column identities in 7016–7023 and the extracted-frozen-factor
restrictions. Preserve row/slot and slot/cube collision masks, shared
squarefree/cube primes, allowed S-primes in dual variables and all zero
powers. Division of symbols is allowed only after verifying unit support.
Do not absorb a coupled mask into a coefficient by an asserted norm
invariance. Common smooth separation is retained from the ready terminal
assessment; no new Fourier measure or norm theorem is to be proved.

Continue if the two identities and the stated coefficient independence
follow in all these cases under the named inputs. Narrow or park on
an unaccounted phase, conductor change, zero case or coupled coefficient.
Even a successful audit removes only the phase/separation portion of
L541's retained input. Actual-Xi positivity and the remaining structural,
analytic and global contracts stay open. Mathlib matching coverage was
not checked; unknown availability is not evidence of absence.
