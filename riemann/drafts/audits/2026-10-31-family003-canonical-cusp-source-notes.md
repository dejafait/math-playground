# Canonical cusp compatibility: source-review notes

Literature-only, 2026-10-31. Source comparison complete; no new
mathematical implication is derived here. Main gap: actual-Xi all-degree
positivity. The bounded target is the saved canonical-cusp source gate.
Its possible use is a separate audit of L541 Hypothesis 1 and L546
Hypothesis 1, without importing either conclusion backwards.

Primary browser retrieval succeeded for the pinned family003 TeX and
Dunn–Radziwiłł arXiv:2109.07463v3. Shell downloads failed DNS resolution;
this is not a source blocker because browser access works. No source
cache file was created. Current notebook changes are preserved.

## Primary evidence actually inspected

Dunn–Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057;
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), 14 May 2024.
Read Section 1.2, definitions and (1.4)–(1.5); Sections 5.1–5.2, (5.1)–(5.16)
including all coefficient cases; Section 5.3, (5.19)–(5.26) including
the Lemma 5.2 hypothesis/proof opening; and the complete Appendix A
table, selecting rows 1,19,10 for the load-bearing comparison.

The raw theta automorphy is stated on Gamma_2, with Kubota character
(c/a)_3 on Gamma_1(3) and trivial character on SL_2(Z); see (5.2)–(5.4).
The cusp functions are defined for all w in H^3 by (5.9), and transform
by (5.10)–(5.11). Their unrestricted nonconstant expansions have support
in lambda^(-4) O excluding zero, by (5.12). Appendix A identifies
the required coefficient families at rows 1,19,10; (5.7), (5.13),
(5.14) state every unit, ramified-exponent and zero case. The coefficient
parameters in (5.8) are primary c,d with c squarefree; no coprimality
between c and d is stated. Conjugation is explicitly (5.16), including
the argument -mu; (5.15) specifies which cusps have constant terms.
These are unconditional formulas, distinct from the paper's
GRH-conditional prime asymptotics. They are citation inputs, not local
reproofs of Patterson's theta construction.

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*,
30 September 2026, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Read the relevant conventions at 546–588 and 1551–1558; fixed-data
hypotheses 1561–1618; full branch data 1655–1725; raw theta/cusp input
1762–1854; full-frequency inversion 1881–1914; and the construction
1935–2122, including all three matrix/multiplier cases and the additive
phase. Also read the full compatibility use in the marked proof
6968–6990. The Mellin continuation and global energy proof are outside
this review. Previous finite phase/separation coverage is reused.

The source identifies Theta_0,Theta_1,Theta_2 with DR's F_1,F_19,F_10
and uses conjugate coefficients in `eq:reflection-cusp-expansion`.
Its e(z)=check-e(z/lambda) differs from DR's check-e; 1551–1556 fix
the conversion. This normalization is an explicit future audit check,
not an unstated interchange of additive characters.

At 1935–1992 it gives the reduced fraction, lifts modulo M_ref^2 and
CRT conditions for delta'. The cases at 1993–2046 are v_lambda(c)>=2,
v_lambda(c)=1 and v_lambda(c)=0, followed by the asserted constant
multiplier at 2047–2062. These are distinct from the three final cusp
functions: translations/reduction identify the representative H with
one of those functions. The middle case uses supplementary laws and
reciprocity; the last case uses the inverse determinant congruence.
The exact algebra and nonzero-entry choices still require audit.

`eq:reflection-additive-phase` at 2063–2085 uses x=lambda^4 mu,
D_F=lambda^3 c_F and an inverse of r modulo D_F. At 2113–2122 the
source explicitly claims that simultaneous choices depend on the local
set only through h_0 and the active radical r. Its marked proof uses
that very claim to combine an absent prime and an inactive zero-mask
branch; that proof cannot independently establish the claim. This is
the bounded implication a later audit must check.

## Search, overlap and route decision

Scoped local searches: L541 Hypothesis 1; L546 Hypotheses 1–4 and its
phase proof interface; the reflection-phase assessments, source notes
and two corresponding histories; terminal-energy assessment/notes;
and ATTEMPTS for canonical-cusp, compatibility and unit-Fourier terms.
No completed independent canonical construction audit was located.
Existing work explicitly retains it. The earlier unit-Fourier stop is
preserved and is not reported as new evidence.

External queries: `"Dunn" "Radziwill" "theta" "cusps" Fourier`,
`"cubic theta" "non-unit" cusp`, `"completed-reflection" "cusp"`,
`"cubic theta" "rational" "cusps" Patterson coefficients`,
`"Dunn" "Radziwiłł" "5.13" "5.14"`, and
`"The Quasi-Riemann Hypothesis" "cusp" "inactive"`.
Results chiefly reproduced the two primary sources or concerned other
theta functions. No stronger independently inspected theorem proves
family003's simultaneous masked construction. Search absence establishes
no novelty. Mirrors, external reviews, alternate-proof/follow-up results
and Patterson's original paper were not used as theorem evidence.
DR explicitly reproduces the needed original coefficient formulas, so
retrieving Patterson again is not essential for this bounded audit.

Decision: SPECIALIZE. Raw cusp statements have no unit-Fourier premise
and provide the three required functions; the family003 construction
specifies an independently testable application. This changes the next
route from source retrieval to a separately approved reproduction audit.
It does not discharge L546 Hypothesis 1 or L541 Hypothesis 1. Retain
coefficient-size and finite Gauss bounds, Mellin/kernel results, broader
character identification, hybrid norm and global closure as contracts.
Mathlib matching coverage was not checked and no absence is asserted.

Test: the prepared scope permits only a bounded reproduction audit with all three cusps,
fixed S,L,h_0, full M_ref^2 sectors, original dual supports and all zero
or nonunit frequencies. A missing raw formula calls for narrowing;
do not repeat the already recorded unit-Fourier obstruction. In particular
check h_0=0, r=1 and nonunit h_0, matrix-entry degeneracies, all supported
dual indices and compatibility across changing local sets at fixed L.
No mathematical verdict or RH candidate is claimed. No lemma, script,
DAG or PROOF change was made; only source coverage and routing changed.
