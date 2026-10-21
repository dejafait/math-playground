# Enlarged paired reference action: source comparison

Literature-only review of the exact target in
[the assessment](literature/2026-10-08-enlarged-paired-reference-action.md).
No enlarged-field integral basis, residual representation or orbit theorem
is proved here. The primary even-degree case changes the proposed route.

## Field and presentation scope

Audited L030 and L031 give L=Q_3(zeta_20,pi), pi^27=3,
absolute degree 108, ramification index 27 and residue degree 4.
They supply the genuine rank-108 Z_3-lattice J_L, without O_U-stability.
The degree-27 results L024 and L025 are methods to compare, not theorem
inputs asserting the corresponding enlarged-field conclusions.

**Kaiji Kondo, Anabelian aspects of the outer automorphism groups of the
absolute Galois groups of mixed-characteristic local fields**, RIMS1991,
December 2025, [primary PDF](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1991.pdf),
**Theorem 1.1(1–4), printed p. 8; following reciprocal setup, pp. 8–9;
Lemma 1.2 and Theorem 1.3 with proof, pp. 9–11**.
The complete statements and even-degree proof were read in the accessible
[arXiv:2512.09231v2, 12 December 2025, section 1](https://arxiv.org/html/2512.09231v2#S1).
The RIMS URL returned a 24-page PDF initially, but subsequent extraction
failed. Fresh detailed reading is credited to the versioned primary HTML;
printed-page locators are those already documented in the local assessment.

Theorem 1.1 assumes a group of MLF-type and odd residue characteristic.
It gives a full presentation, normal wild generation, the tame relation
sigma tau sigma^(-1)=tau^(p^f), and a parity-dependent wild relation.
In the even case the latter is

\[
\sigma x_0\sigma^{-1}=(x'_0)^t x_1^{p^s}
[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d],
\quad s,t\geq1,\quad x'_0\in\overline{\langle\tau,x_0\rangle}.
\]

Use the defining closed words of an admitted presentation; the source does
not permit assigning arbitrary field coordinates to their images. Here
p=3 and f=4; the tame exponent is 81, not the old field's exponent 3.
Neither this presentation nor Theorem 1.3 requires absolute abelianness
or Galoisness over Q_3. Later representation theorems with such extra
hypotheses are not imported.

## Trace kernel and exact paired subgroup

The source defines y_i by wild-inertia reciprocity followed by logarithmic
rationalization. Its setup states that y_1,...,y_d are a Q_p-basis when
p is odd and d>1, citing Hoshi–Nishio Lemma 1.3. Kondo Lemma 1.2
states invariance of the absolute trace kernel under every reconstructed
outer action. Theorem 1.3 states, in **even degree**, that this kernel
is span_Q_p(y_1,y_3,...,y_d). The omitted vector is y_2.
This is a rational theorem, not an integral intersection theorem.

In the proof, g=(d-2)/2 and a_i=x_(2i+1), b_i=x_(2i+2).
For this field the index range is 1<=i<=53. The source displays
phi_i(b_i)=b_i a_i and phi'_i(a_i)=a_i b_i^(-1).
For 1<=i<g the adjacent maps have the following changed words:

\[
\begin{aligned}
\phi''_i(a_i)&=a_i b_i^{-1}a_{i+1}b_{i+1}a_{i+1}^{-1},\\
\phi''_i(b_i)&=a_{i+1}b_{i+1}^{-1}a_{i+1}^{-1}b_i
 a_{i+1}b_{i+1}a_{i+1}^{-1},\\
\phi''_i(a_{i+1})&=a_{i+1}b_{i+1}^{-1}a_{i+1}^{-1}b_i a_{i+1}.
\end{aligned}
\]

Every family explicitly fixes sigma,tau,x_0,x_1,x_2 in even degree;
other paired generators are fixed as specified in the displayed formulas,
including b_(i+1) for the adjacent map. All four coefficient-propagation
cases in the even-degree proof and its final use of x_2 -> x_2 x_1 were
read. That last automorphism is separate from the paired families; it
must not silently enlarge the target subgroup. The odd-degree conclusion
was inspected only for comparison.

These source facts expose a fixed-generator obstruction to transferring
the old whole-trace-kernel irreducibility argument. A next-turn proof
must test the integral reduction of the exceptional direction, rather
than simply run the old chain propagation on 107 coordinates. This note
does not assert a completed proof of residual reducibility or a canonical
rank-106 quotient theorem. The source does not supply a numerical action
matrix in L031's coordinates.

## Reusable reference and analytic inputs

Reuse the already inspected general MLF theorems recorded in L019 and
audited L023, with the compatibility assessment
`drafts/literature/2026-10-06-square-zero-reference-critical-audit.md`:
**Hoshi, Introduction to Mono-anabelian Geometry**, PMB (2021), 5–44,
DOI 10.5802/pmb.42, **Proposition 3.11(i,iv), p. 22; Definition 4.1(i)
and Proposition 4.2(i,iii), pp. 25–26; Definition 5.5 and Remark 5.5.1,
p. 30; Theorem 7.6(i–ii) with proof, pp. 39–40**
([published primary PDF](https://www.numdam.org/item/10.5802/pmb.42.pdf)).
These apply to general MLFs and identify the selected reciprocal reference
lift with the reconstructed logarithmic action. They do not require the
old degree, residue field or a prescribed matrix. Arbitrary full-pair
lifts have the separate profinite-unit exponent ambiguity.

**Hoshi–Nishio, On the Outer Automorphism Groups of the Absolute Galois
Groups of Mixed-characteristic Local Fields**, June 2022 revised RIMS1931,
**section 1 setup and diagram, PDF pp. 3–4; Lemma 1.3 and proof, p. 5;
Lemma 2.3(ii) and proof, pp. 7–8**
([primary text](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf)):
reuse the prior full reading recorded in the integral-presentation and
reference-audit assessments for the general odd-prime rationalization,
normal-generation passage and logarithm compatibility. Its relator is
not substituted for Kondo's. The fresh PDF extraction/screenshots failed,
and local curl failed DNS; no fresh reading of those passages is claimed.
Kondo's directly inspected rational statements remove any dependency on
fresh access to these passages for the new parity comparison.

For the remaining integral specialization, L031 supplies compactness,
all-unit coverage and the deep log/exp ideal pi^14 O_L. Reuse its inspected
Clark and Hess–Pauli–Pohst inputs, especially **Clark, Algebraic Number
Theory II**, 161-page author-hosted version, **Proposition 2.9 and
Corollary 2.10, p. 65; Proposition 2.30, pp. 76–77**
([primary notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf)),
for Eisenstein valuations and prime-to-3 torsion lifting. The former
statement/proof was also visible in the primary indexed extract on this
review. Principal units and all units must be distinguished: the residue
field is F_81, so the old sign-only argument is unavailable. The absence
of 3-primary torsion must be justified from **ramification index 27**,
using the Eisenstein polynomial of zeta_3-1 and the actual value group;
the old odd-total-degree argument cannot be used for degree 108.
The torsion-free abelian-relator specialization and its integral kernel
conclusion remain next-turn proof obligations.

## Duplicates, failures and boundary

Scoped reads covered L019, L023–L025's relevant arguments, L030's field
model, L031's hypotheses/conclusion, the ready source/presentation/audit
assessments and source notes, history/080–087, and ATTEMPTS/022–023.
No enlarged-field paired-action proof was found. The two stops concern
the unchanged division-field packet and naive scalar transport. They
neither exclude these abstract source actions nor establish admissibility
of the enlarged field for original IUT data.

Exact-field searches found no matching theorem. The strongest inspected
results are the general reference transport and Kondo's parity-dependent
rational kernel and displayed generators. Failed searches imply no
novelty. Full matching and supporting Mathlib coverage: **not checked**.
Original input/action identification, packet/global realization, pilot
transport, essentiality and finite B>=A remain unresolved. No lemma,
mathematical script, PROOF argument or DAG row was changed in this review.
