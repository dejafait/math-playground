# Corollary 2.2 and the nonnormal-field screen — completed source comparison

TARGET: Review IUT IV Corollary 2.2(ii)'s exact quantifiers and hypotheses for applying L088's nonnormal-field screen to L086's fixed congruence family.
CHECKED: 2026-10-20
DECISION: IMPORT
SEARCH_EVIDENCE: Step350 inspected Corollary 2.2(ii)'s statement and relevant proof through (P7), compared I 3.1 and IV 1.10, reused step346 and L086's ready occurrence assessment, and checked L086–L088 plus ATTEMPTS/033–034. Exact discovery queries and retrieval qualifications are below; no novel result is claimed.
SOURCE_EVIDENCE: IUT I May 2020 author PDF Definition 3.1(a)–(c), printed pp.61–62; IUT IV April 2020 manuscript, 87 pages, Corollary 2.2 pp.41–43, proof pp.43–46 through (P7), Theorem 1.10 p.22 and Remark 2.3.1(vi) p.56, inspected through the reproduction linked below after detailed author-endpoint retrieval timed out. No byte or journal-version identity is asserted.
COMPARISON: The literal proof fixes the prescribed F and claims all initial-data clauses at (P7); its displayed antecedent does not separately assume F/F_mod Galois. This identifies a testable construction obligation. L088's one witness has no established exclusion from Exc_d, and L086 supplies neither a common compact domain nor distinct bounded-degree parameter occurrence there.
GAP: A fixed compactly bounded parameter subfamily, uniform 2-adic j control and finite-exception avoidance remain unproved. The next changed target needs separate literature coverage. No Corollary 2.2 counterexample, all-choice exclusion or essential IUT flaw follows.
REASON: The source import resolves the field-choice and quantifier ambiguity sufficiently to isolate the remaining family-applicability test; deriving that test is outside this literature-only step.
SCOPE: Import the qualified manuscript statement and fixed-F proof obligation only. This is not an import of the disputed inference as a proved theorem and does not approve new family mathematics.
LITERATURE_REASON: Corollary 2.2's additional hypotheses, choice quantifiers and relevant proof cases are outside the ready L088 audit scope; their exact implications are essential to the proposed new test.

## Completed comparison — step350

The main gap remains original finite B>=A. The intermediate target was
the exact TARGET above. Its downstream use is testing the construction
of initial data, independently of the original volume argument. The
continuation test was to locate a fixed-field obligation rather than
mistake failure of an assumed hypothesis for a counterexample. The
literal (P7) passage meets that source-level test; applicability does not.

### Sources and version limits

[IUT I, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(a)–(c), pp.61–62, was freshly read at the author endpoint.
Reuse step346's model/moduli coverage; no general theorem is reproved.

The [author-hosted IUT IV](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf)
initial response identified April 2020 and 87 pages, but detailed reads
and screenshots failed. The actual detailed reading used the
[April 2020 manuscript reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
It has the same title date, page count and cited numbering. This is a
reading of the author's primary mathematical text in a reproduction,
not authentication of identical bytes. Screenshots supplied no usable
visual evidence; continuous text supplied the passages below. Shell
download also failed DNS resolution. The accessible RIMS1759 copy is
August 2012, 62 pages including its cover, and is not substituted.
The EMS journal landing page identifies the 2021 publication but does
not supply an inspected journal proof. Conclusions here are qualified
to the inspected April 2020 text, consistent with the existing notebook.

### Exact relevant quantified scope

Use IV Corollary 2.2, pp.41–43, with its proof through (P7), p.46:

- X=P^1_Q, D={0,1,infinity}; x_E is a Legendre parameter.
- Fix K_V compactly bounded in U_X, supporting 2, with j(K_2)
  contained in 2^N O_(Qbar_2) for one integer N. Apply the open-domain
  qualification of Remark 2.3.1(vi), p.56.
- The constants H_unif>0 and C_K,H_K>0 precede d and epsilon_d;
  only the latter two constants depend on K_V.
- For each integer d>=1 and 0<epsilon_d<=1, set
  delta=2^12*3^3*5*d. There is a finite Exc_d in U_X(Qbar)_(<=d),
  depending on K_V,d,epsilon_d, containing exceptional-automorphism
  parameters, with h<=H_unif*epsilon_d^(-3)*d^(4+epsilon_d)+H_K there.
- Next take E_F/F with a lift x_E in U_X(F) of degree <=d,
  x_E in K_V minus Exc_d. Its native fields and F satisfy the stated
  Legendre generation equality; full 15-torsion of E_F is F-rational.
- The conclusion supplies initial data for E_F,F_mod, including
  sqrt(h)<=ell<=10*delta*sqrt(h)*log(2*delta*h), and (C2)'s estimates.

Here h=log(q^forall). The relevant bound is on the parameter's degree,
not [F:Q]. Theorem 1.10, p.22, begins instead with initial data;
I Definition 3.1(b) explicitly requires F/F_mod Galois of degree
prime to ell. The corollary's displayed antecedent does not repeat
that requirement. Its proof, p.46, explicitly keeps the given F and
selects C_K,V,cusp before claiming every clause and (P7). No replacement
of F by its normal closure appears in this passage. This is the precise
source assertion under examination, not a verified application here.

The relevant proof cases were read: four core j-values and successive
finite enlargements on pp.43–44; (P1)–(P3)'s prime selection and
(P4)'s cyclic-subgroup exclusion on p.45; (P5)'s nonempty bad places,
(P6)'s large image and the fixed-F assembly (P7) on p.46. These cases
explain why one cannot simply reuse L086's prime seven: the corollary
chooses ell as a function of global height. The later numerical
absorption in (C2) is not needed to isolate the Galois requirement and
has not been critically audited in this step.

### Comparison with canonical local evidence

Audited L088 already fixes native F_mod=Q, F_tpd=Q(t_star) and the
literal field equality for one L087 member. Its index four versus
index one is unchanged. Full 15-torsion for that literal equation
comes from its defining field; no further torsion theorem is needed
for this comparison. No independent initial-data result is transferred.

The literal source construction therefore has a relevant fixed-F
normality obligation if its antecedents can be met outside Exc_d.
That statement is narrower than declaring the corollary false. L086's
quadratic count produces coefficient pairs with two full images, not
infinitely many distinct parameters in one specified compact domain.
The unchanged proofs contain no such domain, 2-adic j bound or
finite-exception-avoidance argument. Infinitely many equations alone
would not suffice, since repetitions of geometric moduli must be
excluded. K_V must be fixed before the exceptional set is selected;
choosing a new singleton K_V for each witness cannot defeat that set.

The selected root ordering fixes one literal equation and field. A
statement allowing a different ordered Legendre model needs its own
choice analysis. The fixed-F wording of the proof is explicit; no
all-six-model mathematical exclusion is added here. A normal-closure
repair would also need justification against the exact generation
equality and all subsequent uses. This review neither makes that
repair nor proves its impossibility or essentiality to finite B>=A.

### Reuse, discovery and continuation

Reused the step346 assessment and foundations/05 step272, the ready
Zywina fixed-level coverage in
`drafts/literature/2026-10-19-auxiliary-full-mod120-occurrence.md`,
L086's family/count, L087's exact chosen fields and audited L088.
No new count or specialization was performed. ATTEMPTS/033's source
classification stop and ATTEMPTS/034's cyclic nonseparation remain;
neither mechanism is reopened. No duplicate family compactness test
was found in these narrowly inspected records.

Queries included `Mochizuki "Corollary 2.2" "Galois" Legendre`,
`"Inter-universal Teichmuller" "j-bounded" "Legendre"`,
`Mochizuki "Legendre" "Galois" "nonnormal"`, and
`"IUT" "Legendre" "normal closure"`. Results did not provide an
inspected published nonnormal-field objection or a ready theorem for
the proposed compact subfamily. nLab, forum, formalization and survey
snippets are discovery leads only, not imports or novelty evidence.

The concrete next frontier is an infinite, distinct, bounded-degree
parameter subfamily in a common allowed domain, retaining the actual
full-image conditions. Its changed hypotheses require the separate
REVIEW_REQUIRED assessment recorded in PROGRESS. Continue only after
essential compactness/occurrence sources are inspected; abandon a
proposed subfamily mechanism if it forces a thin image condition,
approach to a deleted point, unbounded 2-adic j, or only finitely many
distinct parameters. No lemma or mathematical script was written.
Full matching and supporting Mathlib coverage for this construction
scope is not checked; no absence or formal verification is claimed.
The imported progress is local source clarification, not mathematics
beyond the sources or a candidate complete solution.

## Invocation-start proposal — historical; superseded by comparison above

The main gap remains original finite B>=A. The intermediate target is
to identify a precise source-backed applicability test for the established
nonnormal-field screen. A possible downstream use is a test of a claimed
initial-data construction; a theorem with a failed antecedent supplies
no objection. This note proposes that review, without approving or
performing a new mathematical specialization.

Essential local inputs are audited L088 and L087, and L086's actual
fixed-family occurrence statement. Preserve their witness distinctions:
L088 fixes one member, whereas a statement about a family or selection
outside a finite set needs its own hypotheses and proof. Read only the
necessary L086 ranges after extracting the primary theorem's exact
requirements. Do not infer uniformity, infinitely many moduli values,
finite-exception avoidance or simultaneous boundedness from a single
witness. Do not substitute a normal closure or assume all allowed
Legendre choices have been excluded by L088's one-field statement.

First recover the primary statement's quantified objects and required
conclusion, then the proof passages addressing field choice and initial
data. Reuse the ready moduli/automorphism sources; additional searching
should address only a specific uncovered claim. Compare duplicates and
ATTEMPTS/033–034 without reopening their stopped mechanisms.

Continue only if the source yields a concrete, independently testable
obligation connecting the literal prescription with initial data for
the proposed family. If the claim assumes Galoisness, permits a different
field, or cannot be brought under those hypotheses, record that exact
limitation and select a materially different test. An unresolved
quantifier or source case is not a contradiction. No lemma or script is
authorized by this REVIEW_REQUIRED assessment.

Original finite B>=A, independent initial data, actual native input and
action, all-image factorization, pilot transport, essentiality and old
witness questions remain unresolved. Full matching or supporting
Mathlib coverage for this new scope has not been checked. Existing
source-version and unread journal-version qualifications remain.
