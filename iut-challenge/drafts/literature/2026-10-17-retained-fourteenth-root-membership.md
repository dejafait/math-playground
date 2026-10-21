# Retained pilot radical membership — completed source comparison

TARGET: Determine whether the retained finite-torsion data force a fourteenth root of the changed Tate parameter q_0 in the unchanged embedded field N, without assuming native K_w=N.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready 2026-10-12 retained-local-square-root assessment; searched exact fourteenth/14th/seventh-root and q_0 occurrences in L042,L045,L048,L054, relevant retained assessments, history/26*, ATTEMPTS/027,031,032 and foundations/05; followed the resulting L053 chosen-root lead. External queries: Tate curve full n torsion field q 1/n roots unity uniformization; site.jmilne.org elliptic curves Tate curve q torsion. Only author-hosted sources support approval.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), III.3 pp.102–103, finite-extension statement after (26), and II.6 Proposition 6.3 pp.70–71 with its characteristic-zero proof case, https://www.jmilne.org/math/Books/EC2.pdf; Kedlaya, Introduction: the Tate curve, fall 2004, Theorem 1 p.3, group-law and surjectivity discussion p.4, Proposition 3 proof p.5, https://kskedlaya.org/18.727/tate-curve.pdf. Reopened the precise statements and relevant proof cases; Silverman V.3.1/V.4 remains an unread cited proof lead.
COMPARISON: The inspected same-field Tate theorem and geometric finite-torsion theorem cover the unchanged characteristic-zero finite field and changed parameter. They permit the required elementary specialization; neither source directly states the retained named-field fourteenth-root conclusion. L054 covers the square root; L053 chooses a seventh root only in Omega and supplies no duplicate same-N conclusion.
GAP: Research must verify full relevant geometric torsion rationality in the retained N for this same curve, handle multiplicative representatives modulo q_0^Z, and establish the requested radical in N. These are approved specialization obligations, not established results. Native marked rho, native K_w=N, all-image factorization, sufficient initial data and essentiality remain independent.
REASON: Essential same-field and full-torsion coverage is now inspected and adequate; the next turn should apply the known results rather than repeat literature or reprove uniformization.
SCOPE: Exactly TARGET using L045,L048,L054 and retained L042 context; allows finite-torsion group bookkeeping, same-field Tate representatives, representative-exponent or Galois-kernel checks and elementary coprime-root algebra. No field enlargement, curve reselection, assigned native marking, native field identification or all-image comparison is covered. REPRODUCTION is appropriate.
LITERATURE_REASON: The supplied REVIEW_REQUIRED gate concerns a newly selected radical level for changed q_0; reuse square-root coverage and inspect its exact full-torsion/same-field scope before mathematics.

## Inspected known results

Milne III.3, pp.102–103, fixes the standard Tate equation and, after
(26), gives E_q(L)=L^*/q^Z for every finite extension L/Q_p when
q is nonzero in Q_p with |q|<1. Thus this is a statement about
representatives in L, rather than just fixed geometric classes.
II.6 Proposition 6.3 applies to every positive integer prime to
FIELD characteristic and gives geometric torsion free of rank two.
Its proof on p.70 handles characteristic zero by transfer from the
complex case; its positive-characteristic Witt-vector case is not
needed. Residue characteristic is not a restriction here.

Kedlaya Theorem 1, printed p.3, states Galois-equivariant
surjectivity with kernel q^Z and explicitly includes finite
extensions. The discussion through p.4 checks the group law by
power-series identities and defers the difficult surjectivity proof
to Silverman, Advanced Topics (1994), V.3.1/V.4. Import the named
Tate theorem, without reproving it. Proposition 3's proof, p.5,
explicitly describes prime-level geometric torsion using roots of
unity and a root of q. Its additional inertia hypotheses concern
that proposition's inertia conclusion; that conclusion is not an
input to this target. No field enlargement from that proof is
approved here. Retain the earlier coefficient-display warning:
standard Tate coefficients come from Milne.

These are author-hosted versions read on the check date, with no
byte-identity claim. Search snippets and nonprimary hits were not
used as theorem evidence. No assertion of novelty follows from
finding no exact local duplicate. Full matching Mathlib coverage
remains not checked; no Lean implementation is needed for this step.

## Retained inputs, duplicates and stops

L045 gives the full geometric torsion coordinate sets and embedded
completions; L048 concerns the SAME changed curve and its pointed
Q_3-defined Tate isomorphism, q_0 in Q_3 and v_3(q_0)=30.
These match the finite-extension and nonzero strict-norm hypotheses.
L054's square-root result is reusable, not a theorem to reprove.
L042's old rational-parameter division-field calculation cannot be
substituted for the changed-parameter claim.

L053, hypotheses and chosen-point proof, selects beta in Omega with
beta^7=q_0 and a rational torsion POINT. Its separate audit paragraph
explicitly distinguishes point coordinates from multiplicative
representatives. It does not assert beta in N or the fourteenth-root
conclusion. This narrower read is a duplicate check, not a new
mathematical dependency or approval for cover/label work.
ATTEMPTS/027's exact-curve globalization stop remains intact;
ATTEMPTS/031's marked-coordinate stop and ATTEMPTS/032's conditional
native-enclosure stop are not removed by existential membership.

## Continuation and discriminating test

The main gap remains the original finite B>=A comparison. This
intermediate target could remove only L068's existential local
radical-membership premise. It supplies no source-marked pilot.
Essential inputs: L045,L048,L054, with retained L042 context and
foundations/05 as motivation. Retain E_0,F,K_glob=F(E_0[7]),Omega,
u,w,H=F_u,N=(K_glob)_w=Q_3(zeta_420,3^(1/7)), full geometric
30-torsion over F, full geometric 7-torsion over K_glob, the fixed
embedding, M>=max(M_tors,31) and v_3(3)=1. No q_0=3^30,
K_glob=N, native K_w=N or sufficient initial data is assumed.

Continue with one bounded same-N proof attempt: justify the required
full torsion and the representative passage before combining radical
information. A fixed geometric class alone is insufficient; every
q_0-power ambiguity must be controlled. Required field enlargement
fails the target; a missing essential theorem requires source review.
A positive result would close only existential membership, leaving
native identification, marked rho, all-image factorization, independent
global hypotheses, essentiality and finite B>=A unresolved.
No radical verdict, new lemma, mathematical script or derivation is
supplied in this literature-only step.
