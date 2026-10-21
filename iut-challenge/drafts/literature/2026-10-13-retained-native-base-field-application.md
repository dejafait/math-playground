# Retained native field-predicate application — ready continuation

TARGET: Record in L054 the EtTh local field-predicate specialization for the fixed once-punctured E_0 over N, justifying the local K and q_X assignments and claiming only K=K-double-dot=K_2 and the separate square-root-of-minus-one membership.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed definition comparison in drafts/literature/2026-10-13-retained-native-base-field-predicate.md and its targeted duplicate/failure checks. No new target-level theorem or new membership calculation is proposed.
SOURCE_EVIDENCE: Mochizuki, EtTh, December 2008 author PDF, section 1 opening p.10, K_n definition p.12, J_n p.13, double-dot definitions p.16, Definition 1.7/preconditions p.25, Definition 1.9 and Theorem 1.10 pp.27–28, Definition 2.5(i) p.36; IUT I May 2020 author PDF, Definition 3.1(e) p.63. Retained Tate parameter/uniformization coverage is in the L048 and L054 assessments; the relevant source clauses have been inspected.
COMPARISON: The native equality is defined by adjoining zeta_2 and a square root of the original underlying curve's q-parameter; IUT I explicitly attributes it to rational 2-torsion. Existing L054 supplies same-field roots. Only symbol/curve matching and substitution remain for this narrowly stated application.
GAP: A later research step must explain why native local K is the completion N, why original X is the base once-punctured E_0 rather than its degree-seven cover, and why its q_X is the changed geometric Tate parameter. It must retain the separate role of sqrt(-1) and withhold full local-cover and initial-data claims.
REASON: This application stays within inspected definitions and previously proved Tate/root inputs. Reproof, field enlargement, new curve selection and graph/theta work are unnecessary and outside scope. This newly saved ready continuation requires separate supervisor approval next turn.
SCOPE: Exactly TARGET; edit the existing L054 specialization with full hypotheses and precise citations, without a new membership lemma or mathematical script. No full stable-log construction, non-arithmeticity proof, graph quotient, cover-type verdict, label or theta splitting is approved.

The main gap remains finite B>=A in the original comparison and actual
input/action/pilot/essentiality. The intermediate target removes a local
notation/applicability ambiguity; it may be used in a later full native
initial-data check, but leaves those independent obligations unresolved.

Import the defining passages from
[EtTh, December 2008 author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf),
printed pp.12,16, and the existing source assertion from
[IUT I, May 2020 author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(e), p.63. The completed comparison contains the exact
indexed-field formulas and all distinct cover hypotheses. Retain its
version, byte-identity and even-level correction qualifications. A citation
alone does not document the retained curve/parameter dictionary; that is
the reason for this small specialization, not a new theorem or a reproof.

Essential inputs are L045,L048,L054, with their established L042,L044–L047
inputs. Retain E_0/Q, F=Q(zeta_60,E_0[30]), global K=F(E_0[7]), Omega,
u,w, F_u=H=Q_3(zeta_60) subset K_w=N=Q_3(zeta_420,3^(1/7)), full
rational 30-torsion, M>=max(M_tors,31), and the pointed Q_3 Tate
isomorphism with q_0 in Q_3 and v_3(q_0)=30, v_3(3)=1. Neither
global K=N nor q_0=3^30 is assumed. L051's stable-model result is
background only; full stable-log construction is outside this application.
L052 and L053 supply no extra assumption for the field equality.

Continuation test: justify the dictionary for that same underlying elliptic
curve and use existing memberships without changing N. A mismatch of
curve or parameter, or an essential new hypothesis, requires withholding
that specialization and recording a precise review target. Passing must
leave Definition 2.5(i)'s graph and compatible splitting, cusp label,
complete place selection/theta data and numerical comparison open.
ATTEMPTS/027,030 remain in force in their original scopes. Full matching
Mathlib coverage remains unchecked; this is known-method application
coverage, with no originality claim.
