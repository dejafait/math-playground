# Normal-closure differents at three and five — source assessment

TARGET: Prove or refute d_p((C_o)_w)<=d_p(T_v)+v_p(C_0)+1/e(T_v/Q_p) for p=3,5, every L089 survivor, all six orderings and every actual v|p,w|v, using the same normal closures and absolute normalization v_p(p)=1.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step378 reused the step364/368/373 general-p source readings; searched the scoped repair/degree records for different claims and failures, read L092 hypotheses/degree table and L094 theorem/application scope, and checked ATTEMPTS/035. No exact odd-prime application already recorded; no novelty inference.
SOURCE_EVIDENCE: Reused completed primary reading of IV April 2020 reproduction Proposition 1.3(ii), entire proof pp.11–12 and notation pp.9–10, https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf ; Milne FT v5.10 Theorem 3.17 pp.39–40, https://www.jmilne.org/math/CourseNotes/FT.pdf ; freshly inspected Milne ANT v3.08 Proposition 8.10 and proof p.139, Proposition 8.13 and proof p.141, https://www.jmilne.org/math/CourseNotes/ANT.pdf . No IV retrieval or authentication retry.
COMPARISON: The general-p absolute different theorem and Galois completion/decomposition-group theorem cover the proposed method. L092 records [C_o:T]=184320 with odd valuations 2 and 1, matching the target allowances v_3(C_0)=2 and v_5(C_0)=1; only the actual-place specialization and substitution remain.
GAP: No odd-prime inequality is proved in this literature-only turn. A later application must justify local-degree divisibility in the actual Galois tower and substitute its integer valuations into IV 1.3(ii) with k_0=k_1=T_v.
REASON: Essential theorem coverage matches this bounded target; approve a later cited specialization, retaining source qualifications and independent repair gaps.
LITERATURE_REASON: Changed hypotheses p=3,5 and use of L092's global degree input instead of L093's dyadic argument require a separate applicability comparison.

SCOPE: Exact TARGET only; every survivor, all six orderings and all actual places, using L089,L090,L092 and the known different/completion theorems. No sharper different, new inertia classification or complete repair is approved.

## Completed comparison — step378

The main gap is original finite B>=A. The intermediate target remains
exactly TARGET. It could supply the three/five local contributions to
a normal-closure repair, independently of the lost global relative
degree input. This is coverage approval, not a mathematical application.

Reuse the inspected primary theorem and full proof recorded in
`2026-10-20-normal-closure-dyadic-different-transfer.md`: IV 1.3(ii)
has no restriction p=2. For finite local fields k_0 subset k_1 subset
k_i, k_i/k_1 Galois and k_1/k_0 tame, it bounds the absolute different
order d_i by d_0+n_i+1/e_0, with ord(p)=1,
n_i=v_p([k_i:k_0]), e_0=e(k_0/Q_p). Its proof covers the
unramified reduction, zero-exponent case, p-group induction and
degree-p Kummer estimate. Those inspected cases are reusable for
p=3,5; no unread prime-specific case has been identified. Theorem
1.10(ii), p.24, is the recorded downstream use at 2,3,5, not an
independent guarantee that changed fields meet all its hypotheses.

Milne ANT v3.08, 8.10 and its entire proof (printed p.139), freshly
read, identifies the completion group of a finite Galois number-field
extension with its decomposition subgroup. It explicitly establishes
that the order of that subgroup is the local degree. Proposition
8.13(a),(b) and proof (p.141) describes the subgroup intersection and
normal-quotient image in an actual tower. These are precisely the
source inputs needed for a later local-degree divisibility argument;
no equality of completions at distinct places is required. Reuse
Milne FT v5.10, 3.17, pp.39–40, for Galoisness over an intermediate
field, and ordinary Lagrange's theorem for subgroup orders.

The applicability ledger for the later research step is:

- L090 supplies T subset C_o and finite Galois C_o/Q; the application
  must retain C_o/T and actual v,w. Do not use literal G_o as a
  Galois extension and do not cancel the global core inside a local
  decomposition group.
- L092's canonical table gives [C_o:T]=184320 and its odd valuations
  2 and 1; its C_0 row has the same odd valuations. The factor-four
  relative excess is recorded there and must not be called a restored
  global bound. The source subgroup-order theorem, rather than a
  general assertion about nonnormal extension degrees, is the proposed
  bridge from this global input to the actual local integer degree.
- The proposed substitution is k_i=(C_o)_w and k_0=k_1=T_v,
  separately at p=3,5. The tame-intermediate hypothesis permits the
  identity. It makes no assertion that T_v/Q_p is tame.
- Target d_p(K)=a_K/e(K/Q_p) is exactly the absolute ord(p)=1
  different order in the source. Keep this distinct from the relative
  different exponent and from n_i, an integer degree valuation.

L094 covers only two; it is a precedent and duplicate check, not a
proof at three or five. The scoped repair/degree records supply no
already-completed application for this exact target. ATTEMPTS/034's
cyclic separator and ATTEMPTS/035's repeated authentication mechanism
remain parked and do not obstruct this different invariant.

Continue with the later written specialization only if the actual
Galois tower, degree divisibility and normalization match this ledger;
stop on a precise failed hypothesis. Failure of a sufficient bound
would leave the target unresolved, not refute it. A refutation needs
an actual survivor/place and a proved larger different. Classification
for the later application is REPRODUCTION, with no claim beyond the
checked known methods. No general theorem needs reproof: only the
specific field, place and constant identifications require justification.

Remaining limitations are the April reproduction's authentication and
current-version status, the def= boundary, global relative excess,
exact generation and repairs, other places, the height-selected prime,
independent initial data, native input/action/factorization/pilot and
essentiality. Full matching and supporting Mathlib coverage is
unchecked. No new lemma or mathematical script is written, and the
argument in PROOF.md and DAG.md is unchanged.

## Invocation-start proposal — historical

The following pending-review wording records the proposal before the
completed assessment above; it is superseded as current routing.

## Proposed bounded target and relevance

The main gap is still original finite B>=A. This proposed intermediate
test concerns the other two small primes in the recorded IV 1.10(ii)
different comparison. Its plausible use is to distinguish a genuine
local obstruction to normal closure from a loss of a global degree
input. Passing it would not settle exact generation, the full source
assembly, or essentiality.

Retain audited L089,L090,L092 and the now-audited L094 as the dyadic
precedent. Use the same arbitrary original survivor E/Q, c,h,d_*,e_*,
both domains, fixed closure and full-coordinate fields for all six
orderings: T=Q(E[2]), G_o=Q(t_o)(iota,E_o[15]), C_o=G_o^nor over Q.
The actual places v|p,w|v must be retained. C_0=46080 is L092's
comparison constant; its recorded valuations are v_3(C_0)=2 and
v_5(C_0)=1. Define d_p(K)=a_K/e(K/Q_p) for
D_(K/Q_p)=m_K^(a_K). This specifies the proposed invariant only.

The next comparison should check whether the cited decomposition-group
and Galois results allow the global degree information of L092 to
supply the needed local integer-degree valuations, then whether the
general-p IV estimate applies with the identity intermediate. It must
retain every actual place and distinguish absolute and relative
differents. No new local inertia classification is proposed.

Continue to a later mathematical application only if those precise
hypotheses and allowances are covered. If they are not, identify the
failed hypothesis or missing source case. Failure of a sufficient
upper estimate alone would not refute the target inequality; a
refutation requires an actual survivor/place with a proved larger
different. This proposal does not execute or approve either inference.

The local scopes distinguish this target from the already-completed
dyadic degree/different tests. ATTEMPTS/034's cyclic separator and
ATTEMPTS/035's source-access/reapproval stop remain intact. Reuse
existing readings; an unread essential case, if any, must be named
before retrieval.

Unresolved assumptions and limitations: April-reproduction
authentication/current-version and def= boundary; global relative
excess, exact generation and possible repairs; other places beyond
this bounded target; the height-selected prime, independent initial
data, native input/action/factorization/pilot and essentiality.
Retain d=6,epsilon_d=1 only for qualified source comparisons and do
not substitute prime seven. Full and supporting Mathlib coverage is
unchecked. No complete-solution candidate is proposed.
